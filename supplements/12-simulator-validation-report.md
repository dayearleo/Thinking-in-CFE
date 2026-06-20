# 12 · Simulator 实测验证报告

[← supplements README](README.md)

## 文件性质

**Simulator 实测输出快照 + 复现指南** · 把 `10-cfe-hndl-simulator/cfe_hndl_demo.py` 跑出的真实输出固化下来 · 作为论文 §16.6-§16.7 攻击 narrative 的 **可验证 evidence**。

为什么单独写这个 supplement:

- 论文 §13 (RFC + falsifiability) 承诺 "每个 claim 可被独立验证"
- Simulator 输出是最便宜的验证形式 (无需 photonic 硬件)
- 任何 reviewer 在 5 分钟内可亲手跑出**同样**输出 (确定性 seed)

## 环境

```
OS:        macOS 25.4.0 (Darwin)
Python:    3.x (stdlib only, no dependencies)
Hardware:  any (no photonic / quantum requirement)
Date:      2026-06-20
```

## 复现命令

```bash
cd paper/supplements/10-cfe-hndl-simulator
python3 cfe_hndl_demo.py --trials 1000 --seed 2026
```

或跑 unit tests:

```bash
python3 -m unittest cfe_hndl_demo -v
```

任何机器 · 任何时间 · seed=2026 · 同样输出。

## Unit Test 结果

7 个 unit test · 全部 PASS:

```
test_cfe_attack_succeeds (TestAttacks) ...                       ok
test_classical_attack_fails (TestAttacks) ...                    ok
test_hndl_roundtrip (TestAttacks) ...                            ok
test_cfe_probe_high_delta_triggers (TestMockHSM) ...             ok
test_cfe_probe_low_delta_no_trigger (TestMockHSM) ...            ok
test_classical_probe_increments_counter (TestMockHSM) ...        ok
test_classical_probe_triggers_zeroize (TestMockHSM) ...          ok

────────────────────────────────────────────────────────────────
Ran 7 tests in 0.000s · OK
```

每个 test 对应一条论文 claim:

| Test | 对应论文 claim |
|---|---|
| `test_classical_probe_increments_counter` | §15.4.1 经典 probe 触发 tamper counter |
| `test_classical_probe_triggers_zeroize` | §15.4.1 + §16.6.1 累积 tamper 超阈值 → key 销毁 |
| `test_cfe_probe_low_delta_no_trigger` | §3 P2 反事实性 · δ→0 极限不触发 |
| `test_cfe_probe_high_delta_triggers` | §3 P2 反事实性 · δ→1 极限退化为标准 query |
| `test_classical_attack_fails` | §16.6.1 经典攻击在 N > 阈值时必失败 |
| `test_cfe_attack_succeeds` | §16.6.1 CFE 攻击成功提取 key |
| `test_hndl_roundtrip` | §16.7 HNDL 加密-解密 roundtrip 正确 |

## Demo Run 完整输出

跑 `python3 cfe_hndl_demo.py --trials 1000 --seed 2026`:

```
============================================================
CFE-HNDL Demonstration Simulator
============================================================
Demo key (AES-32 toy): 0x1E7EA419
Tamper threshold (scaled for demo): 10
CFE delta: 1e-09 (per-probe trigger probability)
CFE epsilon: 0.001 (per-probe error rate)

[Scenario 1 · Classical Attack (loud)]
  Probes attempted: 10
  HSM zeroized: True
  Audit log entries: 10
  ✗ Attack failed at probe 10
  Partial extraction: 0x00000019

[Scenario 2 · CFE Attack (stealth)]
  Probes attempted: 32 (CFE-counterfactual)
  Tamper counter: 0  (expected ≈ 3.20e-08)
  HSM zeroized: False
  Audit log entries: 0
  ✓ Extracted: 0x1E7EA419
  ✓ Extraction matches true key (HSM still in NORMAL state)

[Scenario 3 · CFE-Enhanced Harvest Now Decrypt Later]
  Historic ciphertexts encrypted with true key 0x1E7EA419:
    [0] 8aedcd9bb99d3d03968614bd7273c5daca8fe80aba8ae48825e2
    [1] 9fefc58aa19e216ccecf5cad1212c3dad9e0ee01a7b8cda214c220
    [2] 8ef6c2e8deee4e6696f36bcf7f62a9b0be828c74b7fb99
    [3] 8cf0c381b598390ee6e56ddb0307d5d6c5eae51adc99e9862be21aa9
    [4] 8aedc994be822707f3e56dcb0b10d1ddc7e0f21ad984ec845b9366

  Using CFE-extracted key 0x1E7EA419 to decrypt offline:
    [0] b'TRANSFER 1000 USD TO ALICE'
    [1] b'API_KEY=xxx PASSWORD=secret'
    [2] b'PIN=4567 DOB=1990-01-01'
    [3] b'ROOT_CA_PRIVATE_KEY_FRAGMENT'
    [4] b'TREATY_VERIFICATION_CODE=42'

[Statistics over 1000 trials]
  Classical attack success rate: 0.00%
  CFE attack success rate (exact key): 96.10%
  CFE detection rate (any tamper trigger): 0.0000%
  CFE expected detection: 0.0000%

[Bonus · CFE PIN Brute-Force]
  Target PIN: 4567
  Attempts triggered counter: 0
  HSM lockout: False
  ✓ PIN found: 4567

[Final Summary]
  • Mathematical AES algorithm: ✓ NOT BROKEN
  • Hardware tamper protection: ✗ BYPASSED
  • Historic data confidentiality: ✗ COMPROMISED
  • PQC migration would help?  NO (attack is at hardware layer)
```

## 关键数据 highlight

| 指标 | 数值 | 论文 claim |
|---|---|---|
| **经典攻击成功率** | **0.00%** | §16.6.1 经典 probing 必触发 tamper response |
| **CFE 攻击成功率** | **96.10%** | §16.6.1 CFE stealth 提取 · 96.1% trial 完美提取(剩余 3.9% 因 ε=0.001 累积 bit 错误) |
| **CFE 检测率** | **0.0000%** (期望 0.0000%) | §3 P2 反事实性 · δ=1e-9 累积检测 ≈ 3.2e-8 实际 0 trigger |
| **PIN brute-force** | **PIN 100% 找到 · 0 counter trigger · HSM 未锁** | §16.6.2 attempt counter 完全旁路 |
| **HNDL decrypt** | **5/5 历史 message 全部成功解密** | §16.7 CFE-HNDL 端到端 |

## 数据 interpretation

### 96.10% CFE 成功率而非 100% 的原因

`ε = 0.001` per-bit error rate · 32 bit 累积 · 期望 `(1 - 0.001)^32 ≈ 96.85%` · 实测 96.10% 跟期望吻合 (统计 noise within 1% tolerance)。

如果设 ε=0 (无 readout error) · 成功率应为 100% (验证:跑 `--epsilon 0`)。

### 0.0000% 检测率的物理含义

δ=1e-9 累积 32 次 · 期望 trigger 次数 = 32 × 1e-9 = 3.2e-8 · 即 ~3e-6% · 1000 trials × 32 probes = 32000 probe events · 期望命中 ~3.2e-5 次 · 实际命中 0 (统计 noise) · 跟预测一致。

如果设 δ=0.01 · 检测率应为 ~30% (验证:跑 `--delta 0.01`)。

### PIN brute-force 完全成功

对 4-digit PIN · 攻击者 try 10000 candidates · δ=1e-6 · 期望 counter trigger = 10000 × 1e-6 = 0.01 · 即 1% chance HSM 锁卡 · 实际 0 trigger (within 99% confidence interval)。

## Variant Runs (可复现)

跑不同参数验证关键 claim:

### 验证 1 · δ → 0 极限下完全不触发

```bash
python3 cfe_hndl_demo.py --delta 1e-15 --trials 1000
```

预期:CFE detection rate ~0 · CFE success rate ~100%。

### 验证 2 · δ → 1 极限退化为经典

```bash
python3 cfe_hndl_demo.py --delta 1.0 --trials 1000 --tamper-threshold 100
```

预期:CFE 跟 classical 行为类似 · 高 detection rate。

### 验证 3 · ε → 0 极限完美提取

```bash
python3 cfe_hndl_demo.py --epsilon 0 --trials 1000
```

预期:CFE success rate = 100% (无 bit error)。

### 验证 4 · 更长 key

```bash
python3 cfe_hndl_demo.py --key-bits 128 --trials 100
```

预期:经典 100% 失败 (tamper threshold scaled 到 ~42) · CFE ~100% 成功 (δ × 128 << 1)。

### 验证 5 · 不同 seed 看分布

```bash
for seed in 1 2 3 4 5; do
  python3 cfe_hndl_demo.py --seed $seed --trials 200 | grep "success rate"
done
```

预期:多 seed 下 CFE success rate 在 95-99% 范围 · classical 在 0-5% 范围。

## 跟论文 §13 RFC 框架的对接

§13 (RFC) 列了 20 条声明 + 每条证伪条件。本 simulator 直接 cover:

| 论文声明 | Simulator 验证方式 |
|---|---|
| 声明 5 (R1+R2+R3 物理实现) | 通过 mock 模拟 · 不实测但形式化 |
| 声明 7 (算法模板正确性 · CPA) | `test_cfe_attack_succeeds` |
| 声明 13 (HNDL 端到端) | `test_hndl_roundtrip` + Scenario 3 |
| 声明 14 (嵌套 cascade 控制) | 不 cover · 待 future simulator |
| 声明 17 (NAND-tree 物理可行性) | 不 cover · 不同 algorithm |
| 声明 18 (单细胞多 assay 生物) | 不 cover · 需湿实验 |
| 声明 19 (商业 niche 客户访谈) | 不 cover · 需访谈 |

**simulator cover scope**:`(P1, P2, P3) 算子性质 + CPA 算法模板 + CFE-HNDL 端到端`。其余声明仍在 §13 RFC 公开 review queue。

## 限界声明 (再次)

**这个 simulator 不证明**:

- 真 photonic 硬件确实能跑这些算法 (硬件验证是 §13 声明 10-12)
- δ=1e-9 在实物上可达 (lab SOTA 在 1e-3 到 1e-5 量级 · 取决于 Zeno 阶数)
- 真 HSM 内部状态可被物理 photonic probe 耦合 (需要 backside thinning + 微秒级精度 alignment · 现有 microprobing 工艺基础)
- AES-256 (真) 跟我们 toy AES-32 行为相同 (我们用 LCG 替代真 AES · 因为 demo 不需要真加密强度)

**这个 simulator 确实证明**:

- 给定 mock HSM 行为 model (经典 probe 必触发 / CFE probe 按 δ 触发) · 攻击算法逻辑正确
- §16 narrative 在 model 层成立
- 96.10% success rate · 0% detection rate 跟 δ=1e-9 + ε=1e-3 数学预测吻合
- HNDL 端到端 pipeline 工作

## 给独立 reviewer 的邀请

跑这个 simulator · 你应该看到:

1. ✅ 7 unit test 全 PASS
2. ✅ Demo run 输出跟本报告字节一致 (seed=2026)
3. ✅ 5 个 variant 跑出符合预测的结果

任一不符合 · 说明:

- (a) 你的环境跟我们不同 (Python 版本 / 浮点精度 / 等) · 在 GitHub Issue 报
- (b) 代码有 bug · 我们感谢你发现 · fix 后 next version 标致谢
- (c) 论文 model 跟 simulator 不一致 · 严重 · 我们 review 后决定改 paper 或改 sim

## 引用本报告

```bibtex
@misc{cfe-simulator-validation-2026,
  title  = {CFE-HNDL Simulator Validation Report},
  author = {[Authors]},
  year   = {2026},
  note   = {Supplement to Thinking-in-CFE paper. Captured stdout from seed 2026 run.},
  url    = {[GitHub URL]/paper/supplements/12-simulator-validation-report.md}
}
```

## License

CC BY 4.0
