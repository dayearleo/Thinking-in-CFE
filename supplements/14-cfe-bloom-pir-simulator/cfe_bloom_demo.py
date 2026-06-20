#!/usr/bin/env python3
"""CFE Bloom Filter Stealth Lookup · Working Simulator + Validation.

Demonstrates paper §17.4.1 + dev-notes/011: Bloom Filter → CFE Stealth Lookup
(Physical-layer PIR). Provides a runnable comparison of three modes:

  1. Classical Bloom lookup     · every probe logged · 100% detectable
  2. Rate-limited Bloom         · classical lookup with attempt counter · fails
                                   under PIR-scale query volume
  3. CFE Bloom lookup           · counterfactual · δ-bounded detection

Compared against theoretical FHE-PIR / multi-server PIR overhead.

Run:
    python3 cfe_bloom_demo.py
    python3 cfe_bloom_demo.py --m 1000000 --k 7 --queries 10000 --delta 1e-9

Tests:
    python3 -m unittest cfe_bloom_demo

License: MIT (see paper/LICENSE.md)
"""

import argparse
import hashlib
import math
import random
import sys
import time
import unittest
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


# ============================================================
# Bloom Filter (with three lookup modes)
# ============================================================


class RateLimitExceeded(Exception):
    """Raised when classical rate-limited mode exceeds query budget."""


@dataclass
class BloomFilter:
    """Bloom filter supporting three lookup modes for direct comparison.

    All three modes return the *same* Boolean answer (modulo CFE's epsilon).
    They differ only in observability / consumption side effects:

      - classical_lookup  : every bit probe logged, query counted
      - rate_limited_lookup : adds an attempt counter that locks at threshold
      - cfe_lookup        : per-probe log triggers with probability delta
    """

    m: int                  # bit array size
    k: int                  # number of hash functions
    bits: List[int] = field(default_factory=list)
    classical_log: List[Tuple[str, int, str]] = field(default_factory=list)
    cfe_log: List[Tuple[str, int, str]] = field(default_factory=list)
    classical_query_count: int = 0
    rate_limited_query_count: int = 0
    cfe_query_count: int = 0
    attempt_counter: int = 0
    attempt_limit: int = 1000
    locked: bool = False
    rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self):
        if not self.bits:
            self.bits = [0] * self.m

    # ---- hash function (deterministic, seed-parameterized) ----

    def _hash(self, key: str, seed: int) -> int:
        h = hashlib.sha256(f"{seed}:{key}".encode()).digest()
        return int.from_bytes(h[:8], "big") % self.m

    # ---- insertion (only one mode; insertion is not the focus) ----

    def insert(self, key: str):
        for seed in range(self.k):
            self.bits[self._hash(key, seed)] = 1

    # ---- mode 1: classical lookup (every probe logged) ----

    def classical_lookup(self, key: str) -> bool:
        self.classical_query_count += 1
        for seed in range(self.k):
            idx = self._hash(key, seed)
            self.classical_log.append(("READ_BIT", idx, key))
            if not self.bits[idx]:
                return False
        return True

    # ---- mode 2: rate-limited classical lookup ----

    def rate_limited_lookup(self, key: str) -> bool:
        if self.locked:
            raise RateLimitExceeded(
                f"Locked after {self.attempt_counter} attempts (limit {self.attempt_limit})"
            )
        self.rate_limited_query_count += 1
        self.attempt_counter += 1
        if self.attempt_counter >= self.attempt_limit:
            self.locked = True
        for seed in range(self.k):
            idx = self._hash(key, seed)
            if not self.bits[idx]:
                return False
        return True

    # ---- mode 3: CFE counterfactual lookup ----

    def cfe_lookup(self, key: str, delta: float, epsilon: float) -> bool:
        """CFE counterfactual lookup.

        Per-probe semantics (modeling Φ^{CF}_AND of k oracles):
          - With probability delta, the probe triggers physical log (R2 leak)
          - With probability 1 - epsilon, the readout is correct
          - Returns AND of all k readouts
        """
        self.cfe_query_count += 1
        result = True
        for seed in range(self.k):
            idx = self._hash(key, seed)
            true_bit = self.bits[idx]
            if self.rng.random() < delta:
                self.cfe_log.append(("CFE_TRIGGERED", idx, key))
            read_bit = true_bit if self.rng.random() > epsilon else (1 - true_bit)
            if not read_bit:
                result = False
        return result

    # ---- theoretical false positive rate (Bloom 1970) ----

    def theoretical_fpr(self, n_inserted: int) -> float:
        return (1 - math.exp(-self.k * n_inserted / self.m)) ** self.k


# ============================================================
# Benchmark scenarios
# ============================================================


def benchmark_correctness(bf: BloomFilter, inserted: List[str],
                          not_inserted: List[str], delta: float,
                          epsilon: float) -> dict:
    """Compare correctness of three modes against ground truth.

    Returns dict of {mode: {true_positive, true_negative, false_positive, false_negative}}.
    """
    results = {
        "classical": {"tp": 0, "tn": 0, "fp": 0, "fn": 0},
        "cfe": {"tp": 0, "tn": 0, "fp": 0, "fn": 0},
    }
    # inserted keys -> should return True
    for key in inserted:
        if bf.classical_lookup(key):
            results["classical"]["tp"] += 1
        else:
            results["classical"]["fn"] += 1
        if bf.cfe_lookup(key, delta, epsilon):
            results["cfe"]["tp"] += 1
        else:
            results["cfe"]["fn"] += 1
    # not-inserted keys -> should return False (or rare false positive)
    for key in not_inserted:
        if bf.classical_lookup(key):
            results["classical"]["fp"] += 1
        else:
            results["classical"]["tn"] += 1
        if bf.cfe_lookup(key, delta, epsilon):
            results["cfe"]["fp"] += 1
        else:
            results["cfe"]["tn"] += 1
    return results


def benchmark_detectability(bf: BloomFilter, queries: List[str],
                            delta: float, epsilon: float) -> dict:
    """Measure server-side detectability for three modes.

    Classical: every query logged → 100% detection per query
    Rate-limited: query attempts capped → fails at limit
    CFE: per-probe trigger probability δ → P[any trigger per query] ≈ kδ
    """
    bf.classical_log.clear()
    bf.cfe_log.clear()
    bf.classical_query_count = 0
    bf.cfe_query_count = 0
    bf.rate_limited_query_count = 0
    bf.attempt_counter = 0
    bf.locked = False

    classical_detected_queries = 0
    cfe_detected_queries = 0
    rate_limited_completed = 0
    rate_limited_failed_at = None

    for i, key in enumerate(queries):
        # classical
        log_before = len(bf.classical_log)
        bf.classical_lookup(key)
        if len(bf.classical_log) > log_before:
            classical_detected_queries += 1
        # rate-limited
        if not bf.locked:
            try:
                bf.rate_limited_lookup(key)
                rate_limited_completed += 1
            except RateLimitExceeded:
                if rate_limited_failed_at is None:
                    rate_limited_failed_at = i
        # cfe
        log_before = len(bf.cfe_log)
        bf.cfe_lookup(key, delta, epsilon)
        if len(bf.cfe_log) > log_before:
            cfe_detected_queries += 1

    n = len(queries)
    return {
        "total_queries": n,
        "classical_detected_queries": classical_detected_queries,
        "classical_detection_rate": classical_detected_queries / n,
        "rate_limited_completed": rate_limited_completed,
        "rate_limited_failed_at_query": rate_limited_failed_at,
        "cfe_detected_queries": cfe_detected_queries,
        "cfe_detection_rate": cfe_detected_queries / n,
        "cfe_expected_detection_per_query": 1 - (1 - delta) ** bf.k,
    }


def pir_comparison_table(m: int, k: int, queries: int, delta: float) -> str:
    """Theoretical comparison vs FHE-PIR / multi-server PIR."""
    classical_bw_per_query = 1   # 1 bit answer
    fhe_pir_bw_per_query = m ** (1 / 3)   # SealPIR-like
    multi_server_bw = m            # naive Chor 1995 (per server)
    cfe_bw = 1                    # 1 photonic readout
    classical_compute = k
    fhe_pir_compute = m            # FHE eval over all entries
    multi_server_compute = m
    cfe_compute = k
    classical_detect = 1.0
    fhe_pir_detect = 1.0           # server sees query event (not content)
    multi_server_detect = 1.0
    cfe_detect = 1 - (1 - delta) ** k

    return f"""
PIR comparison table (per query)
─────────────────────────────────────────────────────────────────
Method               | Bandwidth       | Compute       | Server-detects-event
─────────────────────|─────────────────|───────────────|─────────────────────
Classical lookup     | {classical_bw_per_query} bit         | O({classical_compute})        | 100%
Multi-server PIR     | O(m) = {multi_server_bw}      | O(m) = {multi_server_compute}   | 100% (per server)
FHE-PIR (SealPIR)    | O(m^(1/3)) ~ {fhe_pir_bw_per_query:.0f}  | O(m) FHE = {fhe_pir_compute}  | 100% (content hidden)
CFE Bloom (this)     | {cfe_bw} bit         | O({cfe_compute})        | {100*cfe_detect:.4f}%
─────────────────────────────────────────────────────────────────

For m={m}, k={k}, delta={delta}:
  Total queries = {queries}
  CFE expected detection rate per query = {cfe_detect:.2e}
  CFE expected total detection events  ≈ {queries * cfe_detect:.2e}
  vs Classical = {queries}, Multi-server PIR = {queries}, FHE-PIR = {queries}
"""


# ============================================================
# Demo
# ============================================================


def make_keys(n: int, prefix: str, seed: int) -> List[str]:
    rng = random.Random(seed)
    return [f"{prefix}-{rng.randrange(2**32):08x}" for _ in range(n)]


def print_header(text: str):
    print()
    print("=" * 64)
    print(text)
    print("=" * 64)


def print_subheader(text: str):
    print()
    print(f"[{text}]")


def run_demo(m: int, k: int, n_inserted: int, queries: int,
             delta: float, epsilon: float, attempt_limit: int, seed: int):
    print_header("CFE Bloom Filter → Stealth Lookup Demo")
    print(f"  Bloom Filter params: m={m} bits, k={k} hashes")
    print(f"  Inserted keys: {n_inserted}")
    print(f"  Query volume: {queries}")
    print(f"  CFE params: delta={delta}, epsilon={epsilon}")
    print(f"  Rate-limit attempt cap: {attempt_limit}")

    bf = BloomFilter(m=m, k=k, attempt_limit=attempt_limit,
                     rng=random.Random(seed))

    # Insert population
    inserted = make_keys(n_inserted, "inserted", seed)
    not_inserted = make_keys(n_inserted, "notinserted", seed + 1)
    for key in inserted:
        bf.insert(key)

    # ── Scenario 1: Correctness ──
    print_subheader("Scenario 1 · Correctness (Classical vs CFE)")
    sample_size = min(500, n_inserted)
    correctness = benchmark_correctness(
        bf,
        inserted=inserted[:sample_size],
        not_inserted=not_inserted[:sample_size],
        delta=delta,
        epsilon=epsilon,
    )
    theoretical_fpr = bf.theoretical_fpr(n_inserted)
    for mode in ["classical", "cfe"]:
        r = correctness[mode]
        tpr = r["tp"] / (r["tp"] + r["fn"]) if (r["tp"] + r["fn"]) else 0
        fpr = r["fp"] / (r["fp"] + r["tn"]) if (r["fp"] + r["tn"]) else 0
        print(f"  {mode:10s}  TPR={tpr*100:.2f}%  FPR={fpr*100:.2f}%  "
              f"(theoretical FPR={theoretical_fpr*100:.2f}%)")

    # ── Scenario 2: Detectability ──
    print_subheader("Scenario 2 · Server-side detectability over query stream")
    query_stream = make_keys(queries, "query", seed + 2)
    detect = benchmark_detectability(bf, query_stream, delta, epsilon)
    print(f"  Total client queries: {detect['total_queries']}")
    print(f"  ── Classical lookup ──")
    print(f"     Queries logged by server: {detect['classical_detected_queries']}")
    print(f"     Detection rate: {detect['classical_detection_rate']*100:.2f}%")
    print(f"  ── Rate-limited lookup ──")
    print(f"     Completed queries: {detect['rate_limited_completed']}")
    if detect['rate_limited_failed_at_query'] is not None:
        print(f"     Locked at query #{detect['rate_limited_failed_at_query']}")
    else:
        print(f"     Did not hit lock (queries below limit)")
    print(f"  ── CFE counterfactual lookup ──")
    print(f"     Queries with any trigger: {detect['cfe_detected_queries']}")
    print(f"     Empirical detection rate: {detect['cfe_detection_rate']*100:.6f}%")
    print(f"     Theoretical (1-(1-δ)^k): {detect['cfe_expected_detection_per_query']*100:.6f}%")

    # ── Scenario 3: PIR comparison ──
    print_subheader("Scenario 3 · Stealth PIR comparison vs FHE / multi-server")
    print(pir_comparison_table(m, k, queries, delta))

    # ── Summary ──
    print_subheader("Summary")
    print(f"  CFE Bloom lookup achieves the same correctness as classical Bloom")
    print(f"  while reducing server-side observability by ~{100/(100*detect['cfe_detection_rate']+1e-30):.2e}x")
    print(f"  vs the classical baseline. Compared to FHE-PIR, CFE Bloom additionally")
    print(f"  hides the query event itself (R2) rather than only the query content.")
    print()
    print(f"  See paper §17.4.1 and dev-notes/011 for full analysis.")
    print("=" * 64)
    print()


# ============================================================
# Unit Tests
# ============================================================


class TestBloomFilter(unittest.TestCase):
    def test_no_false_negatives(self):
        bf = BloomFilter(m=10000, k=5, rng=random.Random(0))
        keys = [f"key_{i}" for i in range(100)]
        for key in keys:
            bf.insert(key)
        for key in keys:
            self.assertTrue(bf.classical_lookup(key))

    def test_fpr_approximately_matches_theory(self):
        m, k, n = 10000, 5, 1000
        bf = BloomFilter(m=m, k=k, rng=random.Random(0))
        for i in range(n):
            bf.insert(f"present_{i}")
        false_positives = sum(
            1 for i in range(2000) if bf.classical_lookup(f"absent_{i}")
        )
        empirical_fpr = false_positives / 2000
        theoretical = bf.theoretical_fpr(n)
        # Allow 2x tolerance for finite-sample noise
        self.assertLess(empirical_fpr, theoretical * 2 + 0.01)
        self.assertGreater(empirical_fpr, theoretical * 0.5 - 0.01)

    def test_classical_log_every_probe(self):
        bf = BloomFilter(m=100, k=3, rng=random.Random(0))
        bf.insert("hello")
        bf.classical_log.clear()
        bf.classical_lookup("hello")
        self.assertEqual(len(bf.classical_log), 3)  # k=3 probes

    def test_rate_limit_locks(self):
        bf = BloomFilter(m=100, k=3, attempt_limit=5, rng=random.Random(0))
        for _ in range(5):
            bf.rate_limited_lookup("any")
        with self.assertRaises(RateLimitExceeded):
            bf.rate_limited_lookup("any")
        self.assertTrue(bf.locked)


class TestCFEMode(unittest.TestCase):
    def test_cfe_low_delta_logs_rarely(self):
        bf = BloomFilter(m=100, k=5, rng=random.Random(0))
        bf.insert("known")
        bf.cfe_log.clear()
        for _ in range(1000):
            bf.cfe_lookup("known", delta=1e-6, epsilon=0)
        # Expected trigger count ≈ 1000 * 5 * 1e-6 = 0.005
        self.assertLess(len(bf.cfe_log), 5)

    def test_cfe_high_delta_logs_proportionally(self):
        bf = BloomFilter(m=100, k=5, rng=random.Random(0))
        bf.insert("known")
        bf.cfe_log.clear()
        for _ in range(1000):
            bf.cfe_lookup("known", delta=0.5, epsilon=0)
        # Expected trigger count ≈ 1000 * 5 * 0.5 = 2500
        self.assertGreater(len(bf.cfe_log), 1500)
        self.assertLess(len(bf.cfe_log), 3500)

    def test_cfe_correctness_with_zero_epsilon(self):
        bf = BloomFilter(m=10000, k=5, rng=random.Random(0))
        for i in range(100):
            bf.insert(f"present_{i}")
        # With epsilon=0, CFE lookup should match classical
        for i in range(100):
            self.assertEqual(
                bf.classical_lookup(f"present_{i}"),
                bf.cfe_lookup(f"present_{i}", delta=1e-9, epsilon=0),
            )

    def test_cfe_epsilon_bounded_errors(self):
        bf = BloomFilter(m=10000, k=5, rng=random.Random(0))
        for i in range(100):
            bf.insert(f"present_{i}")
        errors = 0
        for i in range(100):
            if not bf.cfe_lookup(f"present_{i}", delta=1e-9, epsilon=0.01):
                errors += 1
        # Probability of all k=5 bits read correctly: (1-0.01)^5 ≈ 0.951
        # Expected false negative rate ≈ 1 - 0.951 = 0.049
        # Allow generous tolerance
        self.assertLess(errors, 20)


class TestComparison(unittest.TestCase):
    def test_classical_detected_more_than_cfe(self):
        bf = BloomFilter(m=1000, k=5, attempt_limit=10000, rng=random.Random(0))
        for i in range(100):
            bf.insert(f"k_{i}")
        queries = [f"k_{i % 100}" for i in range(500)]
        result = benchmark_detectability(bf, queries, delta=1e-6, epsilon=0)
        # Classical: every query detected
        self.assertEqual(result["classical_detected_queries"], 500)
        # CFE: ~ 500 * 5 * 1e-6 = 0.0025 expected → empirical near 0
        self.assertLess(result["cfe_detected_queries"], 5)


# ============================================================
# Main
# ============================================================


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m", type=int, default=100000,
                        help="Bloom filter bit array size (default 100000)")
    parser.add_argument("--k", type=int, default=7,
                        help="Number of hash functions (default 7)")
    parser.add_argument("--inserted", type=int, default=10000,
                        help="Number of keys to insert (default 10000)")
    parser.add_argument("--queries", type=int, default=10000,
                        help="Number of test queries (default 10000)")
    parser.add_argument("--delta", type=float, default=1e-9,
                        help="CFE per-probe trigger prob (default 1e-9)")
    parser.add_argument("--epsilon", type=float, default=1e-3,
                        help="CFE per-probe error rate (default 1e-3)")
    parser.add_argument("--attempt-limit", type=int, default=1000,
                        help="Rate-limit attempt cap (default 1000)")
    parser.add_argument("--seed", type=int, default=2026,
                        help="Random seed (default 2026)")
    parser.add_argument("--test", action="store_true",
                        help="Run unit tests instead of demo")
    args = parser.parse_args()

    if args.test:
        sys.argv = sys.argv[:1]
        unittest.main()
    else:
        run_demo(
            m=args.m, k=args.k, n_inserted=args.inserted, queries=args.queries,
            delta=args.delta, epsilon=args.epsilon,
            attempt_limit=args.attempt_limit, seed=args.seed,
        )


if __name__ == "__main__":
    main()
