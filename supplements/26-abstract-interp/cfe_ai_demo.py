#!/usr/bin/env python3
"""CFE Abstract Interpretation · SMT Cost Saving Simulator.

Demonstrates paper supplement 13 §13.1: abstract interpretation
with CFE counterfactual SMT consultation.

Toy abstract interpreter for an "integer range domain" on a small
imperative language. SMT solver is the expensive oracle. Classical
mode counts every SMT call; CFE mode pre-screens via counterfactual
query so only critical cases hit the real solver.

Run:
    python3 cfe_ai_demo.py
    python3 cfe_ai_demo.py --programs 50 --smt-budget 100

Tests:
    python3 -m unittest cfe_ai_demo

License: MIT
"""

import argparse
import random
import sys
import unittest
from dataclasses import dataclass, field
from typing import Optional, List


class SMTBudgetExceeded(Exception):
    pass


@dataclass
class Interval:
    lo: int
    hi: int

    def contains(self, other: 'Interval') -> bool:
        return self.lo <= other.lo and other.hi <= self.hi

    def join(self, other: 'Interval') -> 'Interval':
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))

    def __repr__(self):
        return f"[{self.lo},{self.hi}]"


@dataclass
class SMTOracle:
    """Models expensive SMT solver with rate-limited budget."""
    budget: int = 1000
    classical_calls: int = 0
    cfe_calls: int = 0
    cfe_triggered: int = 0
    rng: random.Random = field(default_factory=random.Random)

    def classical_query(self, predicate: str) -> bool:
        if self.classical_calls >= self.budget:
            raise SMTBudgetExceeded(
                f"SMT budget {self.budget} exhausted"
            )
        self.classical_calls += 1
        # Toy: treat predicate hash as boolean evaluation
        return hash(predicate) % 3 != 0  # ~67% satisfiable

    def cfe_query(self, predicate: str, delta: float) -> bool:
        if self.classical_calls >= self.budget:
            raise SMTBudgetExceeded
        self.cfe_calls += 1
        # CFE: actual SMT call triggered with prob delta only
        if self.rng.random() < delta:
            self.classical_calls += 1
            self.cfe_triggered += 1
        # Always return the truth (CFE non-destructive readout)
        return hash(predicate) % 3 != 0


def classical_analysis(programs: List[str], smt: SMTOracle) -> dict:
    """Classical abstract interpretation: every range check hits SMT."""
    successful = 0
    failed_at = None
    for i, prog in enumerate(programs):
        try:
            for var in ['x', 'y', 'z']:
                smt.classical_query(f"in_range_{var}_{prog}")
            successful += 1
        except SMTBudgetExceeded:
            failed_at = i
            break
    return {
        "programs_analyzed": successful,
        "smt_calls": smt.classical_calls,
        "failed_at": failed_at,
    }


def cfe_analysis(programs: List[str], smt: SMTOracle, delta: float) -> dict:
    """CFE abstract interpretation: pre-screen via counterfactual SMT."""
    successful = 0
    for prog in programs:
        try:
            for var in ['x', 'y', 'z']:
                smt.cfe_query(f"in_range_{var}_{prog}", delta)
            successful += 1
        except SMTBudgetExceeded:
            break
    return {
        "programs_analyzed": successful,
        "cfe_calls": smt.cfe_calls,
        "actual_smt_triggered": smt.cfe_triggered,
    }


def run_demo(n_programs: int, smt_budget: int, delta: float, seed: int):
    print()
    print("=" * 64)
    print("CFE Abstract Interpretation · SMT Cost Saving Demo")
    print("=" * 64)
    print(f"  Programs to analyze: {n_programs}")
    print(f"  SMT budget (rate limit): {smt_budget}")
    print(f"  CFE delta: {delta}")
    print()
    rng = random.Random(seed)
    programs = [f"prog_{rng.randrange(2**32):08x}" for _ in range(n_programs)]

    print("[Mode 1 · Classical · Every range check hits SMT]")
    smt_c = SMTOracle(budget=smt_budget, rng=random.Random(seed))
    r_c = classical_analysis(programs, smt_c)
    print(f"  Programs analyzed: {r_c['programs_analyzed']} / {n_programs}")
    print(f"  SMT calls used:    {r_c['smt_calls']}")
    if r_c['failed_at'] is not None:
        print(f"  ✗ SMT budget exhausted at program {r_c['failed_at']}")
    else:
        print(f"  ✓ Analysis completed within budget")

    print()
    print("[Mode 2 · CFE · Counterfactual SMT pre-screen]")
    smt_cfe = SMTOracle(budget=smt_budget, rng=random.Random(seed))
    r_cfe = cfe_analysis(programs, smt_cfe, delta)
    print(f"  Programs analyzed: {r_cfe['programs_analyzed']} / {n_programs}")
    print(f"  CFE queries:       {r_cfe['cfe_calls']}")
    print(f"  Actual SMT triggered: {r_cfe['actual_smt_triggered']}")
    print(f"  Expected ≈ {3 * n_programs * delta:.4f}")

    print()
    print("[Comparison]")
    speedup_progs = r_cfe['programs_analyzed'] / max(r_c['programs_analyzed'], 1)
    print(f"  Programs analyzed: CFE {speedup_progs:.1f}x more than classical")
    print(f"  SMT cost reduction: ~{r_c['smt_calls'] / max(r_cfe['actual_smt_triggered'], 1):.1e}x")

    print()
    print("[Killer Use Case · Cloud SMT-as-a-Service]")
    print(f"  Z3-on-AWS: each SMT call costs $0.001-$0.01")
    print(f"  Classical: {r_c['smt_calls']} calls = ${r_c['smt_calls'] * 0.005:.2f}")
    print(f"  CFE:       {r_cfe['actual_smt_triggered']} calls = ${r_cfe['actual_smt_triggered'] * 0.005:.4f}")
    print()
    print("  See paper supplement 13 §13.1 for full analysis.")
    print("=" * 64)


class TestSMTOracle(unittest.TestCase):
    def test_classical_increments(self):
        o = SMTOracle(budget=100)
        o.classical_query("test")
        self.assertEqual(o.classical_calls, 1)

    def test_classical_exhausts_budget(self):
        o = SMTOracle(budget=3)
        for i in range(3):
            o.classical_query(f"p{i}")
        with self.assertRaises(SMTBudgetExceeded):
            o.classical_query("p4")

    def test_cfe_low_delta_rarely_triggers(self):
        o = SMTOracle(budget=10000, rng=random.Random(0))
        for i in range(1000):
            o.cfe_query(f"p{i}", delta=1e-9)
        self.assertLess(o.cfe_triggered, 5)

    def test_cfe_returns_correct_answer(self):
        o1 = SMTOracle(budget=100)
        o2 = SMTOracle(budget=100)
        self.assertEqual(
            o1.classical_query("pred"),
            o2.cfe_query("pred", delta=0)
        )


class TestAnalysis(unittest.TestCase):
    def test_classical_hits_budget(self):
        programs = [f"p{i}" for i in range(100)]
        smt = SMTOracle(budget=10)
        r = classical_analysis(programs, smt)
        self.assertIsNotNone(r['failed_at'])

    def test_cfe_completes_all(self):
        programs = [f"p{i}" for i in range(100)]
        smt = SMTOracle(budget=10, rng=random.Random(0))
        r = cfe_analysis(programs, smt, delta=1e-9)
        self.assertEqual(r['programs_analyzed'], 100)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--programs", type=int, default=200)
    parser.add_argument("--smt-budget", type=int, default=100)
    parser.add_argument("--delta", type=float, default=1e-9)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        sys.argv = sys.argv[:1]
        unittest.main()
        return
    run_demo(args.programs, args.smt_budget, args.delta, args.seed)


if __name__ == "__main__":
    main()
