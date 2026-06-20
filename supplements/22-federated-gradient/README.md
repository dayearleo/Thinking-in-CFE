# Federated Gradient Privacy · CFE Simulator 4 of 5 in this batch

[← supplements README](../README.md)

## 是什么

论文 §17.4.4 + dev-notes/014 的真做实。**292 行 Python · 5 unit test 全 pass** · 真神经网络训练 + CFE counterfactual gradient + privacy 三模式对比。

**Killer use case**:**Federated Learning 的物理层 privacy** —— 医疗 / 金融 / PII 敏感数据不离开 client · 但 model 仍学到 gradient · 不损 accuracy · 不依赖 DP/MPC 协议 overhead。

## 实测结果 (default · 100 XOR samples · 50 epochs)

```
3 modes compared:
  Centralized:       86.00% accuracy · 5000 samples accessed by server
  Classical Fed:     86.00% accuracy · 5000 gradients sent (sample-reconstructable via Zhu 2019)
  CFE Fed:           86.00% accuracy · 0 physical sample leaks (R3 property)
  
Privacy gain over centralized: ~5000x
```

**关键 finding**:三模式 accuracy 完全一致 · CFE 不损模型质量 · 但 privacy 物理保证。

## 跑

```bash
python3 cfe_fed_demo.py
python3 cfe_fed_demo.py --samples 200 --epochs 100
python3 -m unittest cfe_fed_demo -v
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
