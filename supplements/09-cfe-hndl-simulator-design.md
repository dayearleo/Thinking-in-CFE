# 09 · CFE-HNDL Simulator · 设计文档

[← supplements README](README.md)

## 文件性质

**Simulator 设计文档** · 配套 `10-cfe-hndl-simulator/` 实际 Python 代码 · 描述 simulator 的 scope / 模型 / 输出 / 限界。

## 目的

让任何 Python 用户 · **不需要 photonic 硬件** · 通过 classical simulation 跑通论文 §16.6.1 + §16.7 的 CFE-HNDL 攻击 · 直观看到:

- HSM 在传统攻击下会触发 tamper response
- HSM 在 CFE 攻击下**不触发** · 但 key 被偷
- 攻击者用偷来的 key 解密所有 historic + future traffic

## 不是什么

- **不**是真 CFE 算子实现 (那需要 photonic 硬件)
- **不**是密码学攻击 production tool (是 educational simulator)
- **不**是 zero-day vulnerability exploit
- **不**针对任何特定 HSM 厂商产品

## Simulator Architecture

```
┌─────────────────────────────────────────────────┐
│           HSM Model (mock_hsm.py)               │
│                                                  │
│  • Stores secret key K (toy AES-32 for demo)    │
│  • Tamper counter (init 0)                      │
│  • Audit log                                    │
│  • Methods:                                     │
│    - classical_probe(addr) -> bit, counter++    │
│    - cfe_probe(addr, δ) -> bit, counter+=δ      │
│    - rate_limit_query(input) -> bool, log+=1    │
│    - check_tamper() -> bool                     │
└─────────────────────────────────────────────────┘
              ▲                ▲
              │                │
              │                │
  ┌───────────┴────┐    ┌──────┴──────────┐
  │Classical Attack│    │  CFE Attack     │
  │(loud)          │    │  (stealth)      │
  │                │    │                 │
  │ for i in K:    │    │ for i in K:     │
  │   classical    │    │   cfe_probe(    │
  │   _probe(i)    │    │     i, δ=1e-9)  │
  │ ── triggers!   │    │ ── undetectable │
  └────────────────┘    └─────────────────┘
              ▲
              │
              ▼
  ┌─────────────────────────────────────────────┐
  │     HNDL Demonstration                      │
  │                                              │
  │  • Encrypt historic data with K              │
  │  • Attack HSM (classical vs CFE)             │
  │  • If CFE: K extracted, decrypt all historic │
  │  • Output comparison report                  │
  └─────────────────────────────────────────────┘
```

## Model · HSM 行为模拟

### 经典物理 probe 模型

```python
def classical_probe(addr):
    """Classical physical probe of HSM internal state.
    Always triggers tamper counter."""
    self.tamper_counter += 1
    self.audit_log.append(("PROBE", addr, time.time()))
    if self.tamper_counter > self.threshold:
        self.zeroize_keys()
        raise TamperResponseTriggered
    return self.key_bits[addr]
```

### CFE 反事实 probe 模型

```python
def cfe_probe(addr, delta=1e-9, epsilon=1e-3):
    """CFE counterfactual probe of HSM internal state.
    Triggers tamper counter with probability delta.
    Returns correct bit with probability 1 - epsilon."""
    triggered = random.random() < delta  # Bernoulli(delta)
    if triggered:
        self.tamper_counter += 1
        self.audit_log.append(("PROBE", addr, time.time()))
        if self.tamper_counter > self.threshold:
            self.zeroize_keys()
            raise TamperResponseTriggered

    correct = random.random() > epsilon  # Bernoulli(1 - epsilon)
    return self.key_bits[addr] if correct else 1 - self.key_bits[addr]
```

### Rate-limit query 模型 (PIN 验证)

```python
def rate_limit_query(input_pin):
    """PIN verification with attempt counter.
    Classical: increment counter every call.
    CFE: counter increment probability = delta."""
    if self.attempt_counter >= self.max_attempts:
        self.lockout = True
        return False
    self.attempt_counter += 1
    self.audit_log.append(("PIN_ATTEMPT", input_pin, time.time()))
    return input_pin == self.pin
```

## 三个 Demo Scenario

### Scenario 1 · Classical Attack (Loud)

```
1. Attacker tries to extract K bit by bit via classical_probe
2. Each probe increments tamper counter
3. Counter exceeds threshold → HSM zeroizes K
4. Attack failed · K destroyed before fully extracted
```

### Scenario 2 · CFE Attack (Stealth)

```
1. Attacker uses cfe_probe with δ=1e-9
2. Each probe increments tamper counter with probability 1e-9
3. For 32-bit demo key: expected tamper count = 32 × 1e-9 ≈ 3e-8
4. Effectively zero · HSM doesn't notice
5. K extracted · attack succeeds silently
```

### Scenario 3 · CFE-HNDL End-to-End

```
1. Generate historic AES-32 ciphertext using HSM key K
2. CFE-extract K from HSM (Scenario 2)
3. Use K to decrypt historic ciphertext offline
4. Output: 
   - HSM state (still "secure", no tamper triggered)
   - Extracted K
   - Decrypted historic data
   - Proof: HNDL succeeded today, no FT QC needed
```

## Simulator 输出 (示例)

```
============================================================
CFE-HNDL Demonstration
============================================================

[Setup]
  Generated random AES-32 key K = 0xA3F2B19E
  Encrypted 5 historic messages
  HSM tamper threshold = 100
  HSM attempt counter limit = 10

[Scenario 1 · Classical Attack]
  Probing bit 0... tamper_counter = 1
  Probing bit 1... tamper_counter = 2
  ...
  Probing bit 99... tamper_counter = 100
  ❌ HSM zeroized! Attack failed.

[Scenario 2 · CFE Attack]
  Probing bit 0 (CFE δ=1e-9)... tamper_counter = 0
  Probing bit 1 (CFE δ=1e-9)... tamper_counter = 0
  ...
  Probing bit 31 (CFE δ=1e-9)... tamper_counter = 0
  ✅ Key extracted: 0xA3F2B19E
  HSM state: NORMAL (no tamper triggered)
  Audit log entries: 0

[Scenario 3 · HNDL Decryption]
  Using extracted K to decrypt historic data...
  Message 1: "TRANSFER $1000 TO ALICE"
  Message 2: "API_KEY=xxx PASSWORD=yyy"
  Message 3: "PIN=4567 DOB=1990-01-01"
  Message 4: "ROOT_CA_PRIVATE_KEY=..."
  Message 5: "TREATY_VERIFICATION_CODE=..."

[Comparison]
  Classical attack: ❌ HSM destroyed key, attack failed
  CFE attack:       ✅ Key stolen silently, HNDL succeeded

[Statistics from 1000 trials]
  Classical success rate: 0%
  CFE success rate: 99.7%
  CFE detection rate: 0.003% (consistent with δ=1e-9 × 32 bits)

[Conclusion]
  Mathematical algorithm (AES) is intact.
  Hardware key storage (HSM) is bypassed.
  PCC defenses needed - see paper §15.7
============================================================
```

## 限界

明确这个 simulator **不是**:

- **真 CFE 算子物理实现**:δ 是软件参数 · 不是物理 Quantum Zeno effect 模拟
- **HSM 真实行为模拟**:商用 HSM 行为远比 mock 复杂
- **可重现的物理攻击**:跑通 simulator 不等于跑通真 HSM 攻击
- **教学的全面性**:只演示 §16.6.1 + §16.7 · 不 cover 其他章节

是:

- **概念演示** · 直观展示 R2 性质的攻击 narrative
- **可读代码** · 跑出来比读论文快
- **可 fork / 改** · 让 reviewer 加自己的 attack scenario
- **教育材料** · 课堂 / workshop 用

## 跑法

```bash
cd paper/supplements/10-cfe-hndl-simulator
python3 cfe_hndl_demo.py

# 或带参数
python3 cfe_hndl_demo.py --key-bits 64 --trials 10000 --delta 1e-12
```

## Tests

simulator 包含基础 tests:

- HSM mock 行为正确性
- Classical attack 必然触发 tamper
- CFE attack 触发概率 = δ × N (统计 1000 次)
- HNDL decrypt 输出正确

详 `10-cfe-hndl-simulator/README.md`

## 跟论文章节对应

| 论文章节 | simulator 演示 |
|---|---|
| §3 算子定义 | `cfe_probe()` 函数 (P2 性质模拟) |
| §15.4.1 HSM tamper bypass | Scenario 2 |
| §16.6.1 AES key 提取 | Scenario 2 + 3 (key extract) |
| §16.6.2 PIN 暴力 | Scenario 用 `rate_limit_query()` 变体 |
| §16.7 CFE-HNDL | Scenario 3 |

## License

MIT (代码) · 详 paper root `LICENSE.md`
