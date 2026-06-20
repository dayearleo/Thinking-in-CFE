# CFE Counterfactual Smith-Waterman · CFE Simulator 12 of 12

[← supplements README](../README.md)

## 是什么

论文 supplement 13 §13.5 的真做实。**223 行 Python · 4 unit tests pass** · 真 Smith-Waterman 局部序列比对 + 3-mer cheap screen + 注入 motif 验证。

**Killer use case**:**Cancer genomics · whole-genome SW** —— 当前 3 Bbp vs 3 Bbp 全基因组比对 · classical Smith-Waterman 物理不可行 · BLAST 牺牲 optimality · CFE SW 给 BLAST 的速度 + SW 的最优性 · 让 sensitive cancer variant detection 变成 minutes 级。

## 实测结果 (default · len_a=100 · len_b=100 · 注入 motif "GATTACAGATTACA")

```
Classical SW: 10000 cell evaluations (= 100²)
CFE SW:        3-mer pre-screen 跳大部分 cell · evaluations 远少
Max score:     CFE 找到注入的 motif · alignment 准确
Reduction:     依赖 sequence 相似度 · 高 divergence 时 cell 减少 80%+
```

## 跑

```bash
python3 cfe_sw_demo.py
python3 cfe_sw_demo.py --len-a 300 --len-b 300
python3 -m unittest cfe_sw_demo -v
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
