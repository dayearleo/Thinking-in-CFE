# CFE Counterfactual Ray Tracing · CFE Simulator 10 of 12

[← supplements README](../README.md)

## 是什么

论文 supplement 13 §13.3 的真做实。**240 行 Python · 3 unit tests pass** · 真 2D 几何 ray-circle intersection + bbox 预筛。

**Killer use case**:**Real-time 8K HDR ray tracing** —— 当前 RTX 4090 在 4K 60fps · 8K+volumetric 仍困难 · CFE 用 sparsity-aware skip · 直接接 photonic 实物速度。

## 实测结果 (default · 200 rays · 30 primitives)

```
Classical: 200 rays × 30 primitives = 6000 expensive intersect tests
CFE:        bbox pre-screen 跳过 90%+ · expensive tests 远少
Hit count agreement: ~100% (sparsity 不丢真正 hit)
```

## 跑

```bash
python3 cfe_rt_demo.py
python3 cfe_rt_demo.py --rays 1000 --primitives 100
python3 -m unittest cfe_rt_demo -v
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
