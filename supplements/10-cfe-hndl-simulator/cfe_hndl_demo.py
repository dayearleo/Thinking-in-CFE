#!/usr/bin/env python3
"""CFE-HNDL Demonstration Simulator.

Demonstrates paper §16.6.1 (HSM key extraction via CFE) + §16.7
(CFE-enhanced Harvest Now Decrypt Later).

This is a CLASSICAL simulation of the CFE attack narrative. It does NOT
implement actual photonic IFM hardware. The CFE operator's δ-bounded
trigger property is modeled as a Bernoulli probability per probe call.

Run:
    python3 cfe_hndl_demo.py
    python3 cfe_hndl_demo.py --help
    python3 cfe_hndl_demo.py --trials 10000 --delta 1e-12

Tests:
    python3 -m unittest cfe_hndl_demo

License: MIT (see paper/LICENSE.md)
"""

import argparse
import random
import sys
import unittest
from dataclasses import dataclass, field
from typing import List, Tuple


# ============================================================
# Mock HSM
# ============================================================


class TamperResponseTriggered(Exception):
    """Raised when HSM tamper counter exceeds threshold; key is zeroized."""


@dataclass
class MockHSM:
    """Mock HSM holding a secret key + tamper detection counter.

    Simulates two probe modes:
      - classical_probe: always increments tamper counter
      - cfe_probe: increments tamper counter with probability delta (R2)
    """

    key_bits: List[int]
    tamper_threshold: int = 100
    pin: str = "4567"
    attempt_counter_limit: int = 3

    tamper_counter: int = 0
    attempt_counter: int = 0
    lockout: bool = False
    audit_log: List[Tuple[str, int, int]] = field(default_factory=list)
    zeroized: bool = False
    rng: random.Random = field(default_factory=random.Random)

    def classical_probe(self, addr: int, t: int = 0) -> int:
        """Classical physical probe: always triggers tamper counter."""
        if self.zeroized:
            raise TamperResponseTriggered("HSM already zeroized")
        self.tamper_counter += 1
        self.audit_log.append(("CLASSICAL_PROBE", addr, t))
        if self.tamper_counter >= self.tamper_threshold:
            self.zeroize()
            raise TamperResponseTriggered(
                f"Tamper threshold {self.tamper_threshold} exceeded at addr {addr}"
            )
        return self.key_bits[addr]

    def cfe_probe(self, addr: int, delta: float, epsilon: float, t: int = 0) -> int:
        """CFE counterfactual probe: tamper trigger with prob delta (P2 property)."""
        if self.zeroized:
            raise TamperResponseTriggered("HSM already zeroized")
        triggered = self.rng.random() < delta
        if triggered:
            self.tamper_counter += 1
            self.audit_log.append(("CFE_PROBE_TRIGGERED", addr, t))
            if self.tamper_counter >= self.tamper_threshold:
                self.zeroize()
                raise TamperResponseTriggered(
                    f"Tamper threshold {self.tamper_threshold} exceeded at addr {addr}"
                )
        correct = self.rng.random() > epsilon
        true_bit = self.key_bits[addr]
        return true_bit if correct else 1 - true_bit

    def rate_limit_query(self, input_pin: str, mode: str = "classical",
                         delta: float = 1e-9, t: int = 0) -> bool:
        """PIN verification with attempt counter.

        mode='classical': counter increments every call (gets locked out fast)
        mode='cfe':       counter increments with prob delta (CFE bypass)
        """
        if self.lockout:
            return False
        if mode == "classical":
            self.attempt_counter += 1
            self.audit_log.append(("PIN_ATTEMPT_CLASSICAL", -1, t))
        else:
            if self.rng.random() < delta:
                self.attempt_counter += 1
                self.audit_log.append(("PIN_ATTEMPT_CFE_TRIGGERED", -1, t))
        if self.attempt_counter >= self.attempt_counter_limit:
            self.lockout = True
            return False
        return input_pin == self.pin

    def zeroize(self):
        self.key_bits = [0] * len(self.key_bits)
        self.zeroized = True

    def is_normal(self) -> bool:
        """HSM in normal state: not zeroized, not locked out."""
        return not self.zeroized and not self.lockout


# ============================================================
# Toy AES-CTR (for demonstration; NOT real AES)
# ============================================================


def toy_encrypt(key_int: int, plaintext: bytes, key_bits: int = 32) -> bytes:
    """Toy stream cipher (XOR with key-derived stream). DEMO ONLY.

    Real AES is a complex SPN construction; this is just a placeholder.
    """
    mask = (1 << key_bits) - 1
    state = key_int & mask
    ciphertext = bytearray()
    for byte in plaintext:
        state = ((state * 1103515245 + 12345) & mask)  # LCG-based stream
        ciphertext.append(byte ^ (state & 0xFF))
    return bytes(ciphertext)


def toy_decrypt(key_int: int, ciphertext: bytes, key_bits: int = 32) -> bytes:
    return toy_encrypt(key_int, ciphertext, key_bits)


# ============================================================
# Attack Scenarios
# ============================================================


def classical_attack(hsm: MockHSM, key_bits: int) -> Tuple[int, bool]:
    """Try to extract key via classical probing. Will likely fail."""
    extracted = 0
    try:
        for i in range(key_bits):
            bit = hsm.classical_probe(i, t=i)
            extracted |= (bit << i)
    except TamperResponseTriggered:
        return extracted, False
    return extracted, True


def cfe_attack(hsm: MockHSM, key_bits: int, delta: float, epsilon: float) -> Tuple[int, bool]:
    """Extract key via CFE counterfactual probing."""
    extracted = 0
    try:
        for i in range(key_bits):
            bit = hsm.cfe_probe(i, delta=delta, epsilon=epsilon, t=i)
            extracted |= (bit << i)
    except TamperResponseTriggered:
        return extracted, False
    return extracted, True


def cfe_pin_brute_force(hsm: MockHSM, delta: float) -> Tuple[str, bool]:
    """Brute-force 4-digit PIN via CFE counterfactual queries.
    Bypasses attempt counter via R2 (delta-bounded trigger)."""
    for trial in range(10000):
        candidate = f"{trial:04d}"
        if hsm.rate_limit_query(candidate, mode="cfe", delta=delta, t=trial):
            return candidate, True
    return "", False


# ============================================================
# Demo
# ============================================================


def make_hsm(key_bits: int, key_int: int, seed: int) -> MockHSM:
    bits = [(key_int >> i) & 1 for i in range(key_bits)]
    return MockHSM(key_bits=bits, rng=random.Random(seed))


def print_header(text: str):
    print()
    print("=" * 60)
    print(text)
    print("=" * 60)


def print_subheader(text: str):
    print()
    print(f"[{text}]")


def run_demo(key_bits: int, delta: float, epsilon: float,
             tamper_threshold: int, trials: int, seed: int):
    rng = random.Random(seed)
    key_int = rng.randrange(1 << key_bits)
    # Scale tamper threshold so classical attack reliably fails before
    # extracting the full key. A real HSM would have a much higher
    # threshold relative to its key size; we squeeze it for demo clarity.
    effective_threshold = min(tamper_threshold, max(2, key_bits // 3))
    print_header("CFE-HNDL Demonstration Simulator")
    print(f"Demo key (AES-{key_bits} toy): 0x{key_int:0{max(1, key_bits//4)}X}")
    print(f"Tamper threshold (scaled for demo): {effective_threshold}")
    print(f"CFE delta: {delta} (per-probe trigger probability)")
    print(f"CFE epsilon: {epsilon} (per-probe error rate)")

    # ── Scenario 1: Classical Attack ──
    print_subheader("Scenario 1 · Classical Attack (loud)")
    hsm1 = make_hsm(key_bits, key_int, seed)
    hsm1.tamper_threshold = effective_threshold
    extracted1, success1 = classical_attack(hsm1, key_bits)
    print(f"  Probes attempted: {hsm1.tamper_counter}")
    print(f"  HSM zeroized: {hsm1.zeroized}")
    print(f"  Audit log entries: {len(hsm1.audit_log)}")
    if success1:
        print(f"  ✓ Extracted: 0x{extracted1:0{key_bits//4}X}")
    else:
        print(f"  ✗ Attack failed at probe {hsm1.tamper_counter}")
        print(f"  Partial extraction: 0x{extracted1:0{key_bits//4}X}")

    # ── Scenario 2: CFE Attack ──
    print_subheader("Scenario 2 · CFE Attack (stealth)")
    hsm2 = make_hsm(key_bits, key_int, seed + 1)
    hsm2.tamper_threshold = effective_threshold
    extracted2, success2 = cfe_attack(hsm2, key_bits, delta, epsilon)
    print(f"  Probes attempted: {key_bits} (CFE-counterfactual)")
    print(f"  Tamper counter: {hsm2.tamper_counter}  (expected ≈ {key_bits * delta:.2e})")
    print(f"  HSM zeroized: {hsm2.zeroized}")
    print(f"  Audit log entries: {len(hsm2.audit_log)}")
    if success2:
        print(f"  ✓ Extracted: 0x{extracted2:0{key_bits//4}X}")
        if extracted2 == key_int:
            print("  ✓ Extraction matches true key (HSM still in NORMAL state)")
        else:
            wrong_bits = bin(extracted2 ^ key_int).count("1")
            print(f"  ⚠ Extraction has {wrong_bits} bit errors (epsilon-bounded)")

    # ── Scenario 3: HNDL ──
    print_subheader("Scenario 3 · CFE-Enhanced Harvest Now Decrypt Later")
    historic_messages = [
        b"TRANSFER 1000 USD TO ALICE",
        b"API_KEY=xxx PASSWORD=secret",
        b"PIN=4567 DOB=1990-01-01",
        b"ROOT_CA_PRIVATE_KEY_FRAGMENT",
        b"TREATY_VERIFICATION_CODE=42",
    ]
    print(f"  Historic ciphertexts encrypted with true key 0x{key_int:0{key_bits//4}X}:")
    ciphertexts = [toy_encrypt(key_int, m, key_bits) for m in historic_messages]
    for i, ct in enumerate(ciphertexts):
        print(f"    [{i}] {ct.hex()}")
    print(f"\n  Using CFE-extracted key 0x{extracted2:0{key_bits//4}X} to decrypt offline:")
    for i, ct in enumerate(ciphertexts):
        try:
            pt = toy_decrypt(extracted2, ct, key_bits)
            print(f"    [{i}] {pt}")
        except Exception as e:
            print(f"    [{i}] decryption error: {e}")

    # ── Statistics over many trials ──
    print_subheader(f"Statistics over {trials} trials")
    classical_successes = 0
    cfe_successes = 0
    cfe_detections = 0
    for trial in range(trials):
        k = rng.randrange(1 << key_bits)
        h1 = make_hsm(key_bits, k, seed + 100 + trial)
        h1.tamper_threshold = effective_threshold
        _, s1 = classical_attack(h1, key_bits)
        if s1:
            classical_successes += 1

        h2 = make_hsm(key_bits, k, seed + 1000 + trial)
        h2.tamper_threshold = effective_threshold
        ek, s2 = cfe_attack(h2, key_bits, delta, epsilon)
        if s2 and ek == k:
            cfe_successes += 1
        if h2.tamper_counter > 0:
            cfe_detections += 1

    print(f"  Classical attack success rate: {100*classical_successes/trials:.2f}%")
    print(f"  CFE attack success rate (exact key): {100*cfe_successes/trials:.2f}%")
    print(f"  CFE detection rate (any tamper trigger): {100*cfe_detections/trials:.4f}%")
    print(f"  CFE expected detection: {100*(1-(1-delta)**key_bits):.4f}%")

    # ── PIN brute-force ──
    print_subheader("Bonus · CFE PIN Brute-Force")
    hsm_pin = make_hsm(key_bits, key_int, seed + 9999)
    hsm_pin.attempt_counter_limit = 3
    pin, found = cfe_pin_brute_force(hsm_pin, delta=1e-6)
    print(f"  Target PIN: {hsm_pin.pin}")
    print(f"  Attempts triggered counter: {hsm_pin.attempt_counter}")
    print(f"  HSM lockout: {hsm_pin.lockout}")
    if found:
        print(f"  ✓ PIN found: {pin}")
    else:
        print(f"  ✗ PIN not found")

    # ── Final Summary ──
    print_subheader("Final Summary")
    print("  • Mathematical AES algorithm: ✓ NOT BROKEN")
    print("  • Hardware tamper protection: ✗ BYPASSED")
    print("  • Historic data confidentiality: ✗ COMPROMISED")
    print("  • PQC migration would help?  NO (attack is at hardware layer)")
    print()
    print("  See paper §15-§16 for full analysis")
    print("  See supplement 01 for proposed PCC defense")
    print("=" * 60)
    print()


# ============================================================
# Unit Tests
# ============================================================


class TestMockHSM(unittest.TestCase):
    def test_classical_probe_increments_counter(self):
        hsm = make_hsm(4, 0xA, seed=1)
        hsm.tamper_threshold = 10
        bit = hsm.classical_probe(0)
        self.assertEqual(hsm.tamper_counter, 1)
        self.assertEqual(bit, 0)

    def test_classical_probe_triggers_zeroize(self):
        hsm = make_hsm(4, 0xA, seed=1)
        hsm.tamper_threshold = 3
        hsm.classical_probe(0)
        hsm.classical_probe(1)
        with self.assertRaises(TamperResponseTriggered):
            hsm.classical_probe(2)
        self.assertTrue(hsm.zeroized)

    def test_cfe_probe_low_delta_no_trigger(self):
        hsm = make_hsm(32, 0xDEADBEEF, seed=42)
        hsm.tamper_threshold = 100
        for i in range(32):
            hsm.cfe_probe(i, delta=1e-12, epsilon=0)
        self.assertEqual(hsm.tamper_counter, 0)
        self.assertFalse(hsm.zeroized)

    def test_cfe_probe_high_delta_triggers(self):
        # delta=0.5 over 50 probes should trigger tamper counter many times.
        hsm = make_hsm(50, 0, seed=0)
        hsm.tamper_threshold = 10**6  # high enough to not zeroize
        for i in range(50):
            hsm.cfe_probe(i, delta=0.5, epsilon=0)
        # Expected ~25 triggers (50 * 0.5); allow wide tolerance
        self.assertGreater(hsm.tamper_counter, 5)


class TestAttacks(unittest.TestCase):
    def test_classical_attack_fails(self):
        hsm = make_hsm(32, 0xCAFEBABE, seed=7)
        hsm.tamper_threshold = 10
        extracted, success = classical_attack(hsm, 32)
        self.assertFalse(success)
        self.assertTrue(hsm.zeroized)

    def test_cfe_attack_succeeds(self):
        hsm = make_hsm(32, 0xCAFEBABE, seed=7)
        hsm.tamper_threshold = 100
        extracted, success = cfe_attack(hsm, 32, delta=1e-9, epsilon=0)
        self.assertTrue(success)
        self.assertEqual(extracted, 0xCAFEBABE)
        self.assertFalse(hsm.zeroized)

    def test_hndl_roundtrip(self):
        key = 0x12345678
        msg = b"hello world"
        ct = toy_encrypt(key, msg, 32)
        pt = toy_decrypt(key, ct, 32)
        self.assertEqual(pt, msg)


# ============================================================
# Main
# ============================================================


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--key-bits", type=int, default=32,
                        help="Toy AES key length in bits (default 32)")
    parser.add_argument("--trials", type=int, default=1000,
                        help="Number of statistical trials (default 1000)")
    parser.add_argument("--delta", type=float, default=1e-9,
                        help="CFE per-probe trigger probability (default 1e-9)")
    parser.add_argument("--epsilon", type=float, default=1e-3,
                        help="CFE per-probe error rate (default 1e-3)")
    parser.add_argument("--tamper-threshold", type=int, default=100,
                        help="HSM tamper counter threshold (default 100)")
    parser.add_argument("--seed", type=int, default=2026,
                        help="Random seed for reproducibility (default 2026)")
    parser.add_argument("--test", action="store_true",
                        help="Run unit tests instead of demo")
    args = parser.parse_args()

    if args.test:
        sys.argv = sys.argv[:1]
        unittest.main()
    else:
        run_demo(
            key_bits=args.key_bits,
            delta=args.delta,
            epsilon=args.epsilon,
            tamper_threshold=args.tamper_threshold,
            trials=args.trials,
            seed=args.seed,
        )


if __name__ == "__main__":
    main()
