# CFE-HNDL Simulator

[← supplements README](../README.md) · [← simulator 设计文档](../09-cfe-hndl-simulator-design.md)

## 是什么

一个 ~300 行 Python simulator · 演示论文 §16.6.1 (HSM key 提取) + §16.7 (CFE-HNDL) 的攻击 narrative。**不需要任何 photonic 硬件** · 纯 classical simulation。

## 不是什么

详见 [`09-cfe-hndl-simulator-design.md`](../09-cfe-hndl-simulator-design.md) §限界。**这不是真 CFE 物理实现 · 不是 HSM 攻击 production tool**。

## 快速跑

```bash
cd paper/supplements/10-cfe-hndl-simulator
python3 cfe_hndl_demo.py
```

无依赖 · 用 Python 3.8+ stdlib。

## 输出

跑完会看到 3 个 scenario 对比:

- **Scenario 1**: 经典攻击 · HSM 触发 tamper response · 攻击失败
- **Scenario 2**: CFE 攻击 · key 静默提取 · HSM 没察觉
- **Scenario 3**: HNDL · 用提取的 key 解密历史 traffic

外加 1000 trial 统计 · 验证 δ-bounded detection rate 符合理论。

## 参数

```bash
python3 cfe_hndl_demo.py --help
```

可调:

- `--key-bits`: AES toy key 长度 (默认 32 · 演示用 · 真 AES-256)
- `--trials`: 统计跑多少次 (默认 1000)
- `--delta`: CFE 触发率 (默认 1e-9)
- `--epsilon`: CFE 错误率 (默认 1e-3)
- `--tamper-threshold`: HSM tamper counter 阈值 (默认 100)
- `--seed`: 随机种子 · 复现结果用

## 跑 unit tests

```bash
python3 -m unittest cfe_hndl_demo.TestMockHSM
python3 -m unittest cfe_hndl_demo.TestAttacks
```

## 修改 / 扩展

随便 fork。常见扩展方向:

- 加 PIN brute-force scenario (§16.6.2 用 `rate_limit_query`)
- 加多 HSM MPC 防御 demo (§15.7 防御方向)
- 加 statistical anomaly detection (§15.7 检测)
- 加 GUI / 可视化

## 复现性

每次跑用 `--seed` 固定随机种子 · 结果完全可复现 · 用于 paper claim 验证。

## License

MIT · 详 `../../LICENSE.md`


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
