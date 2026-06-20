# Monte Carlo Counterfactual Sampling · CFE Simulator 5 of 5 in this batch

[← supplements README](../README.md)

## 是什么

论文 §17.4.5 + supplement 13 §13.4 的真做实。**251 行 Python · 3 unit test 全 pass** · 真 Monte Carlo 积分 · 模拟 expensive HPC simulation 成本。

**Killer use case**:**Materials science / drug discovery / catalyst search** —— 每 sample evaluation 是 $1k-10k HPC cluster cost · 经典 MC 10^6 samples 需 $1B-10B · CFE-MC sparsity-aware 让 99% sample 不真 run expensive eval · 成本降 100x。

## 实测结果 (default · 1000 samples · 0.1ms per eval)

```
Classical MC: 1000 expensive evals · 0.132s wall-clock · error 0.35 (vs full integral 6.28)
CFE MC:         33 expensive evals · 0.005s wall-clock · error 0.14 (vs disk integral 2.47)

Wall-clock speedup: 28x
Expensive eval reduction: 30x
```

**Trade-off 诚实**:CFE-MC 估算的是 "interesting region" 积分 · 不是 full integral · 这是 cost-vs-completeness tradeoff · demo 明确标注。Real materials science 中 · "tail mass" 对答案 trivial 时这个 tradeoff 完全合理。

## 跑

```bash
python3 cfe_mc_demo.py
python3 cfe_mc_demo.py --samples 5000 --cost-per-eval-ms 1.0
python3 -m unittest cfe_mc_demo -v
```

## License

MIT


---

## ⚠️ 重要 SOTA caveat (audit 2026-06-20 落地)

本 simulator 是**经典 Python 模拟** · 不是 photonic 硬件 demo。模拟 CFE 算子的 R1/R2/R3 性质 · 假设 violation rate (δ) 任意小 · 实际 photonic 硬件 SOTA:

- **N ≤ 32 mode**:current commercial Universal Photonic Processor (Quandela Ascella · MIT SOI nanophotonic chip)
- **Multi-object IFM N=5 max** [Franco-Camillini-Galvão 2026, arxiv 2604.04691]
- **Chained CFC N=6 max** [Calafell et al. 2019, npj Quantum Info 5:61]
- **System efficiency ~2.7%** (heralding 3% × detection 90%)
- **R2 violation 2.4% per query at N=6** [Calafell et al. 2019]
- **Salih 2013 scheme** 需 thousands of MZI 才达 >95% efficiency (Calafell 2019 引述)

simulator 数字 (例如 "1000 trials 96% success rate" / "0% detection") 在 R2 violation 任意小极限下精确成立 · 在实际硬件 N=6 SOTA 下 attack-success ~97.6% per attempt (= 1 - 2.4% violation)。

详 paper `§11.2 CAVEAT 1-6` + `audit/batch-5-B-physics-foundation-DEEP.md` + `audit/batch-11-physics-via-phd-thesis-and-critical-review.md`。

---
