# Differential Cryptanalysis Rate-Limit Bypass · CFE Simulator 3 of 5 in this batch

[← supplements README](../README.md)

## 是什么

论文 §17.4.3 + dev-notes/013 的真做实。**270 行 Python · 6 unit test 全 pass · 真 8-round Feistel cipher (16-bit key/block)** · 实际差分密码分析跑通。

**Killer use case**:**短 key cipher 在 cloud deployment 下被破** —— 经典差分受限于 cipher service rate limit · 灌不进 chosen plaintext;CFE 反事实查询不计入 rate limit · attack 完成。

## 实测结果 (default · 2000 pairs · rate limit 500)

```
Classical: 250 / 2000 pairs · LOCKED at pair 250 · cipher service 500 audit log entries
CFE:       2000 / 2000 pairs · NOT locked · 0 audit log entries
CFE completes 8x more pairs without triggering lock
```

CFE 让 Cloud-deployed 短 key cipher 的 differential analysis 从 "rate-limit 阻断" 变成 "完整可跑"。

## 跑

```bash
python3 cfe_diff_demo.py
python3 cfe_diff_demo.py --queries 5000 --rate-limit 1000
python3 -m unittest cfe_diff_demo -v
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
