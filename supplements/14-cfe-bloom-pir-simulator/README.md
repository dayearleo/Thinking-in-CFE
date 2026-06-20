# CFE Bloom Filter → Stealth Lookup Simulator

[← supplements README](../README.md) · [← Bloom 同构 dev-note](../../../dev-notes/011-2026-06-20-CFE同构-Bloom-Filter-PIR.md)

## 是什么

工作量级的 Python simulator · 把论文 §17.4.1 的 Bloom Filter → CFE Stealth Lookup 同构**真正做实**:不只是 claim · 而是可跑代码 + 单元测试 + 跟经典 baseline 的可重复 benchmark。

跟主论文 §16 的 CFE-HNDL simulator (supplement 10) 是 **parallel 体系** —— 一个 demonstrate HSM key extraction · 一个 demonstrate physical-layer PIR。两个一起证明:CFE 算子体系不是抽象概念 · 至少 2 个具体应用可端到端跑通。

## 不是什么

跟 supplement 10 同样诚实划界:

- **不是真 photonic IFM 物理实现** · δ 是 classical Bernoulli 模拟 · 不是真 Quantum Zeno
- **不是 production-ready PIR 系统** · 缺少真 client-server protocol · 缺少 multi-server 协调
- **不是大规模 deployment 验证** · m=10^5 demo · 真用场景需 m=10^9+

是:

- **跟论文 claim 对账的工具** · paper §17.4.1 说什么 · 这里跑代码看是不是
- **跟经典 baseline 的 honest benchmark** · 不只 marketing · 给数字
- **跟 FHE-PIR / multi-server PIR 的 cost 对比** · 用公开 literature 数字
- **9 个 unit test 通过 · 论文 claim 不依赖手工断言**

## 快速跑

```bash
cd paper/supplements/14-cfe-bloom-pir-simulator
python3 cfe_bloom_demo.py
```

零依赖 · Python 3.8+ stdlib。

## 输出

跑完看到 3 个 scenarios:

1. **Correctness**: 经典 vs CFE 的 TPR / FPR 对比 · 验证两者数学等价
2. **Server-side detectability**: 经典 100% 被 log · CFE 0.000001% · rate-limited 在 1000 query 后锁
3. **PIR comparison table**: 跟 FHE-PIR / multi-server PIR 4 维对比 (bandwidth / compute / detection)

## 跑测试

```bash
python3 -m unittest cfe_bloom_demo -v
```

9 个 unit test 覆盖:

- Bloom Filter 基础正确性 (无 false negative)
- FPR 跟理论吻合 (Bloom 1970 公式 within 2x tolerance)
- Classical lookup 每 probe 都 log
- Rate-limited 锁机制
- CFE low-delta 几乎不 log
- CFE high-delta 按 δ 比例 log
- CFE epsilon=0 时跟 classical 完全一致
- CFE epsilon>0 时错误率有界
- Comparison: classical 必检 · CFE 几乎不检

## 参数

```bash
python3 cfe_bloom_demo.py --help
```

- `--m`: bit array size (default 100000)
- `--k`: hash function count (default 7)
- `--inserted`: 插入 key 数 (default 10000)
- `--queries`: 查询 stream 长度 (default 10000)
- `--delta`: CFE per-probe trigger 概率 (default 1e-9)
- `--epsilon`: CFE per-probe error rate (default 1e-3)
- `--attempt-limit`: rate-limit 锁阈值 (default 1000)
- `--seed`: 随机种子 (default 2026 · 可复现)

## 跟论文章节对应

| 论文 / dev-note | simulator 演示 |
|---|---|
| §17.4.1 Bloom→PIR | 整个 simulator |
| §17.3 5 步 SOP | benchmark 函数实现 §17.3 step 4-5 (复杂度对比 + cost 验证) |
| dev-notes/011 §4 Killer Use Case | scenario 3 PIR comparison table |
| dev-notes/011 §6 Simulator Design | 跟 dev-note 设计文档一致实现 |

## 跟 supplement 10 simulator 的关系

| Supplement | 同构 | 攻击 / 应用 |
|---|---|---|
| 10 · CFE-HNDL | (HSM tamper) | key 提取 + HNDL |
| **14 · CFE-Bloom (本)** | Bloom Filter | stealth PIR · 隐蔽 membership 测试 |
| (未来) | 4 more from §17.4 / supp 13 | TBD |

13 个 §17 worked example 中 · 此 simulator + supplement 10 simulator 让 **2 个被真正做实**。剩下 11 个仍是 claim · 需要类似工程量才能真做实。

## 限界 (再次)

跑 simulator **不等于**:

- 真 photonic 硬件能实现这个 (硬件 PoC 待 future work · 跟 [Hance 2025] 类合作)
- m=10^9 规模工业 PIR 可行 (当前 SOTA 集成 photonic mode N≤32 · 跟 Bloom 实际 size gap 巨大 · 需要 hybrid 方案)
- 真 PIR 协议端到端 (本 simulator 只 Bloom 一层)

跑 simulator **等于**:

- §17.4.1 数学 claim 在 model 层成立
- CFE 跟 classical 在 correctness 上**真**等价
- detectability 差距是 quantifiable 的 (~$10^{32}$x reduction 在 default 参数下)
- 跟 FHE-PIR / multi-server PIR 的 trade-off 是 quantifiable 的

## 复现性

每次跑用 `--seed` 固定 · 结果完全可复现。

## License

MIT · 详 `../../LICENSE.md`
