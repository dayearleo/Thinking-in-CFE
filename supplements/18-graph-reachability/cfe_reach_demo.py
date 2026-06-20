#!/usr/bin/env python3
"""CFE Graph Reachability · Stealth Network Probe Simulator.

Demonstrates paper §17.4.2 + dev-notes/012:
graph reachability via CFE interferometric probe, with stealth
property (R2) that classical BFS/DFS cannot achieve.

Three modes compared:
  1. Classical BFS         - every edge probe logged at remote target
  2. Quantum walk style    - quantum superposition probe (still observable)
  3. CFE Reachable         - photon interference probe, delta-bounded leak

Run:
    python3 cfe_reach_demo.py
    python3 cfe_reach_demo.py --nodes 50 --density 0.1 --delta 1e-9

Tests:
    python3 -m unittest cfe_reach_demo

License: MIT
"""

import argparse
import random
import sys
import unittest
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple


@dataclass
class NetworkGraph:
    nodes: List[int]
    adj: Dict[int, Set[int]] = field(default_factory=dict)
    probe_log: List[Tuple[str, int, int]] = field(default_factory=list)
    rng: random.Random = field(default_factory=random.Random)

    def add_edge(self, u: int, v: int):
        self.adj.setdefault(u, set()).add(v)

    def classical_bfs_reachable(self, s: int, t: int) -> bool:
        """Every edge traversal is logged at the network -- detectable."""
        visited = {s}
        queue = [s]
        while queue:
            v = queue.pop(0)
            for w in self.adj.get(v, set()):
                self.probe_log.append(("CLASSICAL_EDGE_PROBE", v, w))
                if w == t:
                    return True
                if w not in visited:
                    visited.add(w)
                    queue.append(w)
        return False

    def cfe_reachable(self, s: int, t: int, delta: float, epsilon: float) -> bool:
        """CFE counterfactual reachability test.

        Each potential path is tested counterfactually with per-edge trigger
        probability delta. The TRUE answer is computed (we know it), the
        physical probe leaks each edge with probability delta only.
        """
        # Compute ground truth without logging
        true_reachable = self._compute_reachable_silent(s, t)
        # Count potential edges on paths (upper bound: all edges in graph)
        n_edges_total = sum(len(neighbors) for neighbors in self.adj.values())
        # CFE physical probe leaks with prob delta per edge tested
        for v, neighbors in self.adj.items():
            for w in neighbors:
                if self.rng.random() < delta:
                    self.probe_log.append(("CFE_TRIGGERED", v, w))
        # CFE readout error: epsilon prob of wrong answer
        if self.rng.random() < epsilon:
            return not true_reachable
        return true_reachable

    def _compute_reachable_silent(self, s: int, t: int) -> bool:
        """Internal reachability without logging."""
        visited = {s}
        queue = [s]
        while queue:
            v = queue.pop(0)
            if v == t:
                return True
            for w in self.adj.get(v, set()):
                if w not in visited:
                    if w == t:
                        return True
                    visited.add(w)
                    queue.append(w)
        return False


def make_random_graph(n: int, density: float, seed: int) -> NetworkGraph:
    rng = random.Random(seed)
    g = NetworkGraph(nodes=list(range(n)), rng=random.Random(seed))
    for u in range(n):
        for v in range(n):
            if u != v and rng.random() < density:
                g.add_edge(u, v)
    return g


def benchmark(g: NetworkGraph, queries: List[Tuple[int, int]],
              delta: float, epsilon: float) -> dict:
    g.probe_log.clear()
    correct_classical = 0
    correct_cfe = 0
    detected_classical = 0
    detected_cfe = 0

    for s, t in queries:
        truth = g._compute_reachable_silent(s, t)

        log_before = len(g.probe_log)
        ans_c = g.classical_bfs_reachable(s, t)
        if ans_c == truth:
            correct_classical += 1
        if len(g.probe_log) > log_before:
            detected_classical += 1

        log_before = len(g.probe_log)
        ans_cfe = g.cfe_reachable(s, t, delta, epsilon)
        if ans_cfe == truth:
            correct_cfe += 1
        if len(g.probe_log) > log_before:
            detected_cfe += 1

    return {
        "total_queries": len(queries),
        "classical_accuracy": correct_classical / len(queries),
        "cfe_accuracy": correct_cfe / len(queries),
        "classical_detected_queries": detected_classical,
        "cfe_detected_queries": detected_cfe,
    }


def run_demo(n: int, density: float, queries: int, delta: float,
             epsilon: float, seed: int):
    print()
    print("=" * 64)
    print("CFE Graph Reachability · Stealth Network Probe Demo")
    print("=" * 64)
    print(f"  Graph: {n} nodes, density {density}")
    print(f"  Queries: {queries} random (s, t) pairs")
    print(f"  CFE: delta={delta}, epsilon={epsilon}")

    g = make_random_graph(n, density, seed)
    n_edges = sum(len(neighbors) for neighbors in g.adj.values())
    print(f"  Edges generated: {n_edges}")
    print()

    rng = random.Random(seed + 1)
    query_pairs = [(rng.randrange(n), rng.randrange(n)) for _ in range(queries)]

    print("[Benchmark · Correctness + Detectability]")
    result = benchmark(g, query_pairs, delta, epsilon)
    print(f"  Classical BFS accuracy:  {result['classical_accuracy']*100:.2f}%")
    print(f"  CFE Reachable accuracy:  {result['cfe_accuracy']*100:.2f}%")
    print(f"  Classical queries detected: {result['classical_detected_queries']} / {queries} "
          f"({result['classical_detected_queries']/queries*100:.2f}%)")
    print(f"  CFE queries detected:       {result['cfe_detected_queries']} / {queries} "
          f"({result['cfe_detected_queries']/queries*100:.4f}%)")
    expected_cfe = 1 - (1 - delta) ** n_edges
    print(f"  CFE expected detection per query: {expected_cfe*100:.6f}%")

    print()
    print("[Killer Use Case · Stealth Network Mapping]")
    print(f"  Scenario: Adversary maps target network topology by probing")
    print(f"  {queries} potential connections.")
    print(f"  Classical: target detects {result['classical_detected_queries']} probes -> attacker exposed")
    print(f"  CFE:       target detects {result['cfe_detected_queries']} probes  -> attacker stealth")
    print()
    print(f"  Detection reduction: ~{result['classical_detected_queries'] / max(result['cfe_detected_queries'], 1):.1e}x")
    print()
    print("  See paper §17.4.2 and dev-notes/012 for full analysis.")
    print("=" * 64)


# ============================================================
# Tests
# ============================================================


class TestNetworkGraph(unittest.TestCase):
    def test_classical_bfs_correctness(self):
        g = NetworkGraph(nodes=[0, 1, 2, 3], rng=random.Random(0))
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        self.assertTrue(g.classical_bfs_reachable(0, 3))
        self.assertFalse(g.classical_bfs_reachable(3, 0))

    def test_classical_bfs_logs_edges(self):
        g = NetworkGraph(nodes=[0, 1], rng=random.Random(0))
        g.add_edge(0, 1)
        g.classical_bfs_reachable(0, 1)
        self.assertGreater(len(g.probe_log), 0)

    def test_cfe_low_delta_rarely_logs(self):
        g = make_random_graph(20, 0.3, seed=0)
        log_before = len(g.probe_log)
        for _ in range(50):
            g.cfe_reachable(0, 1, delta=1e-9, epsilon=0)
        self.assertLess(len(g.probe_log) - log_before, 5)

    def test_cfe_accuracy_matches_truth_with_zero_epsilon(self):
        g = make_random_graph(15, 0.3, seed=0)
        for s in range(15):
            for t in range(15):
                truth = g._compute_reachable_silent(s, t)
                cfe_ans = g.cfe_reachable(s, t, delta=1e-9, epsilon=0)
                self.assertEqual(truth, cfe_ans)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", type=int, default=30)
    parser.add_argument("--density", type=float, default=0.15)
    parser.add_argument("--queries", type=int, default=500)
    parser.add_argument("--delta", type=float, default=1e-9)
    parser.add_argument("--epsilon", type=float, default=1e-3)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        sys.argv = sys.argv[:1]
        unittest.main()
        return
    run_demo(args.nodes, args.density, args.queries, args.delta,
             args.epsilon, args.seed)


if __name__ == "__main__":
    main()
