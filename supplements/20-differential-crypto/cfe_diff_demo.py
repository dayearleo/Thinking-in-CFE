#!/usr/bin/env python3
"""CFE Differential Cryptanalysis · Rate-Limit Bypass Simulator.

Demonstrates paper §17.4.3 + dev-notes/013:
differential cryptanalysis on a toy cipher with rate-limited oracle,
showing how classical attack hits the rate-limit wall while CFE bypasses.

Toy cipher: 8-round Feistel network with 16-bit key, 16-bit blocks.
This is small enough for actual differential trail analysis but big
enough to demonstrate rate-limit dynamics.

Run:
    python3 cfe_diff_demo.py
    python3 cfe_diff_demo.py --queries 5000 --rate-limit 1000

Tests:
    python3 -m unittest cfe_diff_demo

License: MIT
"""

import argparse
import random
import sys
import unittest
from collections import Counter
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


class CipherLocked(Exception):
    pass


@dataclass
class ToyFeistelCipher:
    """Toy 8-round 16-bit Feistel network for differential analysis demo."""

    key: int
    rounds: int = 8
    block_bits: int = 16
    classical_query_count: int = 0
    cfe_query_count: int = 0
    cfe_triggered_count: int = 0
    rate_limit: int = 10000
    locked: bool = False
    audit_log: List[Tuple[str, int, int]] = field(default_factory=list)
    rng: random.Random = field(default_factory=random.Random)

    def _round_function(self, half: int, round_key: int) -> int:
        """Non-linear round function (toy)."""
        x = (half ^ round_key) & 0xFF
        # Simple S-box like permutation
        x = ((x * 23) ^ (x >> 3) ^ ((x << 5) & 0xFF)) & 0xFF
        return x

    def _round_keys(self) -> List[int]:
        keys = []
        k = self.key
        for r in range(self.rounds):
            keys.append(k & 0xFF)
            k = ((k << 3) | (k >> (16 - 3))) & 0xFFFF
            k ^= 0x5A + r
        return keys

    def encrypt(self, plaintext: int) -> int:
        left = (plaintext >> 8) & 0xFF
        right = plaintext & 0xFF
        for rk in self._round_keys():
            new_right = left ^ self._round_function(right, rk)
            left = right
            right = new_right
        return (left << 8) | right

    def classical_oracle(self, plaintext: int) -> int:
        if self.locked:
            raise CipherLocked("Cipher service locked due to rate limit")
        self.classical_query_count += 1
        self.audit_log.append(("CLASSICAL_QUERY", plaintext, 0))
        if self.classical_query_count >= self.rate_limit:
            self.locked = True
        return self.encrypt(plaintext)

    def cfe_oracle(self, plaintext: int, delta: float) -> int:
        """CFE counterfactual cipher query.

        Returns same ciphertext as encrypt(), but the cipher service
        only logs the query / increments counter with probability delta.
        """
        if self.locked:
            raise CipherLocked("Cipher service locked")
        if self.rng.random() < delta:
            self.cfe_triggered_count += 1
            self.classical_query_count += 1
            self.audit_log.append(("CFE_TRIGGERED", plaintext, 0))
            if self.classical_query_count >= self.rate_limit:
                self.locked = True
        self.cfe_query_count += 1
        return self.encrypt(plaintext)


def differential_bias_analysis(cipher: ToyFeistelCipher, delta_in: int,
                                n_pairs: int, mode: str,
                                cfe_delta: float = 1e-6) -> dict:
    """Run n_pairs of differential queries and aggregate output difference bias."""
    output_diffs = Counter()
    rng = random.Random(2026)
    pairs_completed = 0
    failed_at = None
    for i in range(n_pairs):
        try:
            p = rng.randrange(1 << cipher.block_bits)
            p_prime = p ^ delta_in
            if mode == "classical":
                c = cipher.classical_oracle(p)
                c_prime = cipher.classical_oracle(p_prime)
            else:
                c = cipher.cfe_oracle(p, cfe_delta)
                c_prime = cipher.cfe_oracle(p_prime, cfe_delta)
            output_diffs[c ^ c_prime] += 1
            pairs_completed += 1
        except CipherLocked:
            failed_at = i
            break
    return {
        "pairs_completed": pairs_completed,
        "failed_at": failed_at,
        "output_diff_histogram": output_diffs,
        "max_bias_diff": output_diffs.most_common(1)[0] if output_diffs else None,
        "audit_log_size": len(cipher.audit_log),
    }


def run_demo(key: int, n_pairs: int, rate_limit: int, delta_in: int,
             cfe_delta: float, seed: int):
    print()
    print("=" * 64)
    print("CFE Differential Cryptanalysis · Rate-Limit Bypass Demo")
    print("=" * 64)
    print(f"  Toy cipher: 8-round 16-bit Feistel network")
    print(f"  Secret key: 0x{key:04X}")
    print(f"  Cipher service rate-limit: {rate_limit}")
    print(f"  Differential analysis: {n_pairs} chosen-plaintext pairs")
    print(f"  Input difference delta_in: 0x{delta_in:04X}")
    print(f"  CFE per-query trigger probability: {cfe_delta}")
    print()

    # Classical mode
    print("[Mode 1 · Classical Differential]")
    cipher_cl = ToyFeistelCipher(
        key=key, rate_limit=rate_limit, rng=random.Random(seed))
    result_cl = differential_bias_analysis(cipher_cl, delta_in, n_pairs,
                                            mode="classical")
    print(f"  Pairs completed: {result_cl['pairs_completed']} / {n_pairs}")
    if result_cl['failed_at'] is not None:
        print(f"  ✗ Cipher LOCKED at pair {result_cl['failed_at']} (rate limit hit)")
    else:
        print(f"  ✓ Attack completed (still under rate limit)")
    print(f"  Audit log entries on cipher service: {result_cl['audit_log_size']}")
    if result_cl['max_bias_diff']:
        diff, count = result_cl['max_bias_diff']
        print(f"  Most biased output difference: 0x{diff:04X} (count={count})")

    # CFE mode
    print()
    print("[Mode 2 · CFE Differential (Rate-Limit Bypass)]")
    cipher_cfe = ToyFeistelCipher(
        key=key, rate_limit=rate_limit, rng=random.Random(seed))
    result_cfe = differential_bias_analysis(cipher_cfe, delta_in, n_pairs,
                                             mode="cfe", cfe_delta=cfe_delta)
    print(f"  Pairs completed: {result_cfe['pairs_completed']} / {n_pairs}")
    print(f"  CFE triggered count: {cipher_cfe.cfe_triggered_count}")
    print(f"  Cipher service audit log: {result_cfe['audit_log_size']} entries")
    print(f"  Cipher locked: {cipher_cfe.locked}")
    if result_cfe['max_bias_diff']:
        diff, count = result_cfe['max_bias_diff']
        print(f"  Most biased output difference: 0x{diff:04X} (count={count})")

    # Comparison
    print()
    print("[Comparison]")
    print(f"  Classical: {result_cl['pairs_completed']}/{n_pairs} pairs · "
          f"{result_cl['audit_log_size']} logged · "
          f"{'LOCKED' if cipher_cl.locked else 'OK'}")
    print(f"  CFE:       {result_cfe['pairs_completed']}/{n_pairs} pairs · "
          f"{result_cfe['audit_log_size']} logged · "
          f"{'LOCKED' if cipher_cfe.locked else 'OK'}")
    if not cipher_cfe.locked and cipher_cl.locked:
        ratio = result_cfe['pairs_completed'] / max(result_cl['pairs_completed'], 1)
        print(f"  CFE completes {ratio:.1f}x more pairs without triggering lock")

    print()
    print("[Killer Use Case · Cloud Cipher Service Attack]")
    print(f"  Classical attacker: cipher service detects {result_cl['audit_log_size']} suspicious queries,")
    print(f"                      locks account after {rate_limit} -> attack fails")
    print(f"  CFE attacker:       cipher service detects {result_cfe['audit_log_size']} queries,")
    print(f"                      account stays open -> differential analysis completes")
    print()
    print("  Real impact: short-key legacy ciphers (DES-56, WEP RC4-40) become")
    print("  attackable in cloud deployments where rate-limit was the last defense.")
    print()
    print("  See paper §17.4.3 and dev-notes/013 for full analysis.")
    print("=" * 64)


class TestCipher(unittest.TestCase):
    def test_encrypt_deterministic(self):
        c = ToyFeistelCipher(key=0x1234)
        self.assertEqual(c.encrypt(0x5678), c.encrypt(0x5678))

    def test_encrypt_different_plaintexts(self):
        c = ToyFeistelCipher(key=0x1234)
        outputs = set(c.encrypt(p) for p in range(256))
        # Should produce many distinct outputs (good diffusion)
        self.assertGreater(len(outputs), 200)

    def test_classical_locks_at_rate_limit(self):
        c = ToyFeistelCipher(key=0x1234, rate_limit=10)
        for i in range(10):
            c.classical_oracle(i)
        with self.assertRaises(CipherLocked):
            c.classical_oracle(11)

    def test_cfe_low_delta_no_lock(self):
        c = ToyFeistelCipher(
            key=0x1234, rate_limit=100, rng=random.Random(0))
        for i in range(10000):
            c.cfe_oracle(i % 256, delta=1e-9)
        self.assertFalse(c.locked)
        self.assertLess(c.cfe_triggered_count, 5)


class TestAttack(unittest.TestCase):
    def test_classical_attack_locked_for_large_n(self):
        c = ToyFeistelCipher(
            key=0x1234, rate_limit=100, rng=random.Random(0))
        result = differential_bias_analysis(c, 0x00FF, 500, mode="classical")
        self.assertIsNotNone(result['failed_at'])
        self.assertTrue(c.locked)

    def test_cfe_attack_completes_at_large_n(self):
        c = ToyFeistelCipher(
            key=0x1234, rate_limit=100, rng=random.Random(0))
        result = differential_bias_analysis(
            c, 0x00FF, 500, mode="cfe", cfe_delta=1e-9)
        self.assertIsNone(result['failed_at'])
        self.assertFalse(c.locked)
        self.assertEqual(result['pairs_completed'], 500)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--key", type=lambda x: int(x, 0), default=0x1234)
    parser.add_argument("--queries", type=int, default=2000)
    parser.add_argument("--rate-limit", type=int, default=500)
    parser.add_argument("--delta-in", type=lambda x: int(x, 0), default=0x00FF)
    parser.add_argument("--cfe-delta", type=float, default=1e-6)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        sys.argv = sys.argv[:1]
        unittest.main()
        return
    run_demo(args.key, args.queries, args.rate_limit, args.delta_in,
             args.cfe_delta, args.seed)


if __name__ == "__main__":
    main()
