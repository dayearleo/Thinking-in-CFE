# CFE 同构 · 差分密码分析 → Rate-Limit Bypass

> **触发**:论文 §17.4.3 worked example 深化
> **状态**:同构 v1 · 数学化完成 · 待 simulator + lab cipher attack PoC
> **真理源**:本文件 = 差分密码分析 CFE 同构的单点真理源

## 0 · 关联文档

- 论文 §17.4.3 · 高层 worked example
- 论文 §15.4.1 · HSM tamper bypass (类似机制)
- 论文 §16.6.2 · PIN brute force (CFE rate-limit bypass 另一例)
- supplement 11 · 同构提交模板

## 1 · 经典算法引用

- **Biham, Shamir 1990** · "Differential Cryptanalysis of DES-like Cryptosystems" · CRYPTO
- **Matsui 1993** · Linear Cryptanalysis · EUROCRYPT (parallel approach)
- **Wagner 1999** · Boomerang Attack · FSE
- **Kaplan et al. 2016** · "Breaking Symmetric Cryptosystems using Quantum Period Finding" · CRYPTO · 量子加速

经典差分密码分析的核心:

- 选择 plaintext 对 $(P, P')$ with $P \oplus P' = \Delta$ (input difference)
- 观察 ciphertext 对 $(C, C')$
- 统计 $\Delta' = C \oplus C'$ 在哪些值上 bias 高
- High-bias differentials reveal key information through differential trail

经典 DES 攻击需要 $\sim 2^{47}$ chosen plaintexts。

## 2 · CFE 同构

### 2.1 · 核心 primitive

差分分析的核心 primitive:

```
DiffMatch(Δ, Δ') = (E_K(P + Δ) - E_K(P) == Δ')
```

每对 (Δ, Δ') 是一个 Boolean test。整个 attack 是 $2^n$ 个这种 test 的 statistical aggregation。

### 2.2 · CFE form

$$\Phi^{CF}_{\text{DiffMatch}}(\Delta, \Delta') = \Phi^{CF}_{f_{\Delta, \Delta'}}(\hat{O}_{\text{cipher}}, \delta, \epsilon)$$

where $f_{\Delta, \Delta'}$ 在 cipher oracle 上反事实评估 differential match。

物理实现:

- Cipher 实现在 photonic chip 上 (modern HSM 内部 AES 加速器是 photonic 化的实物候选)
- CFE 反事实查询 cipher oracle · cipher service 的 query log 不记录
- 累积大量反事实 query · 用经典统计聚合 bias

### 2.3 · 为什么算同构

- 经典差分本质是大量 Boolean test + statistical aggregation
- CFE 直接表达每个 Boolean test
- 关键差异:CFE 让每个 test **不计入 rate limit / audit log**

## 3 · 复杂度比较

| 维度 | 经典差分 (Biham 1990) | Quantum 差分 [Kaplan 2016] | CFE Differential |
|---|---|---|---|
| $D_1$ Query 数 | $2^{47}$ for DES | $2^{24}$ for DES | $2^{47} \cdot 1/\delta$ (慢 $1/\delta$ 倍) |
| $D_2$ Disturbance | 1 · 触发 rate limit | 1 | $\delta$ · 不触发 |
| $D_3$ Persistence in audit | ✅ 全 log | ✅ | ❌ R2 |
| $D_4$ Hardware | CPU + 大量 chosen plaintext | FT QC | photonic IFM probe + cipher physical access |

### 净评估

- $D_1$ **慢很多** ($1/\delta$ 倍)
- 对 long key cipher (AES-128/256) · CFE $D_1$ 慢到无意义
- 对 **short key legacy** (DES-56 · WEP RC4-40) · 经典 $D_1$ 已可行 · CFE $D_1$ × $1/\delta = 2^{47} \cdot 10^9 = 2^{77}$ · 仍可行 if photonic 单 query 极快
- 关键 differentiation:**rate-limited cipher service 让经典差分无法实施 · CFE 完全旁路**

## 4 · Killer Use Case

### 4.1 · 短 key cipher 的 cloud deployment 攻击

**场景**:

- 某 cloud 服务用 DES (legacy enterprise system) 加密 · 暴露 cipher oracle (encrypt API) 给客户
- 经典 DES 数学早被破 · 但 cloud service 有 rate limit ($10^4$ queries/minute) + anomaly detection
- 没人能在合理时间内灌 $2^{47}$ 经典 chosen plaintext

**CFE Differential 解决**:

- 反事实 query cipher oracle · 不被 rate limit 计 (R2)
- 累积 $2^{47}$ 反事实查询 · photonic 单 flight ns 级
- Total wall-clock: $2^{47} \times 10^{-9}$ s = $10^5$ s ≈ 27 小时
- Cipher service 完全不知 · 没 lock 客户账号

**Targets**:

- Legacy banking 后端 (DES + 3DES 混用)
- 老 IoT 设备 firmware OTA verification (用短 key)
- 工业控制 (SCADA) legacy crypto
- 某些 government legacy systems

### 4.2 · WEP / WPA1 类已 broken 但部署仍在的 cipher

WEP RC4-40 数学早被破 (Fluhrer 2001) · 但很多 legacy WiFi 设备仍部署。Active attack 显眼 (WiFi probe 是物理可见的)。

CFE Differential 对 WiFi 加密 ciphertext 反事实查询 · physical receiver 不发任何 stronger signal · 完全 passive。

### 4.3 · 跟 PIN brute force (§16.6.2) 的关系

PIN brute force 是 CFE rate-limit bypass 的简单情况 (key space 10⁴)。
Differential 是 rate-limit bypass 的复杂情况 (key space 2^k)。
共同模式:**经典攻击成功的关键瓶颈是 detectability · CFE 旁路**。

## 5 · 物理实现路径

### 5.1 · Level

L3 · cipher physical access (HSM probing setup) + CFE differential analyzer

### 5.2 · 关键工程

- 跟 cipher hardware (HSM / cipher chip) 物理 photonic 耦合
- 大量并行 differential trial · photonic mesh 设计
- Classical post-processing aggregator
- Trade-off:更 deep 的 Zeno 链得 lower δ · 但更长 per query 时间

### 5.3 · 现有最接近

- Side-channel analysis lab (e.g., Riscure / NewAE) 提供 cipher physical probing 基础
- 跟 §15.4.1 HSM tamper bypass 共硬件

## 6 · Simulator 设计

```python
class CipherOracle:
    def __init__(self, key, cipher_fn, rate_limit=10000):
        self.key = key
        self.cipher = cipher_fn
        self.rate_limit = rate_limit
        self.query_counter = 0
        self.locked = False
    
    def classical_encrypt(self, plaintext):
        if self.locked:
            raise CipherLocked
        self.query_counter += 1
        if self.query_counter >= self.rate_limit:
            self.locked = True
            raise RateLimitExceeded
        return self.cipher(self.key, plaintext)
    
    def cfe_encrypt(self, plaintext, delta):
        if self.locked:
            raise CipherLocked
        if random.random() < delta:
            self.query_counter += 1
        return self.cipher(self.key, plaintext)


def classical_differential_attack(oracle, num_pairs, delta_in):
    # 经典差分:rate limit 会 lock cipher 在 num_pairs 远小于完整 attack 需要时
    pairs = []
    for _ in range(num_pairs):
        try:
            P = random_plaintext()
            P_prime = P ^ delta_in
            C = oracle.classical_encrypt(P)
            C_prime = oracle.classical_encrypt(P_prime)
            pairs.append((C ^ C_prime))
        except RateLimitExceeded:
            break
    return aggregate_bias(pairs)


def cfe_differential_attack(oracle, num_pairs, delta_in, cfe_delta):
    # CFE 差分:rate limit 不触发 · 完整 attack 可完成
    pairs = []
    for _ in range(num_pairs):
        P = random_plaintext()
        P_prime = P ^ delta_in
        C = oracle.cfe_encrypt(P, cfe_delta)
        C_prime = oracle.cfe_encrypt(P_prime, cfe_delta)
        pairs.append((C ^ C_prime))
    return aggregate_bias(pairs)
```

Validation:

- Classical attack `num_pairs >> rate_limit` 必 fail
- CFE attack 同样 `num_pairs` 不触发 lock · 给出 bias signature
- Toy cipher (e.g., reduced-round DES) 可在 simulator 实跑 + 验证 recovered key

## 7 · Falsification

- 现代 strong cipher (AES-256) · CFE differential 没用 (key space 太大 · 即便 photonic 加速 wall-clock 仍 infeasible)
- 如果 cipher service 实现 "本地 anomaly detection + 物理 tamper detection 联合" · 可能检测 CFE differential 的物理 probe
- 物理 access cipher chip 是 prerequisite · CFE 不绕过

## 8 · 相关工作

### 经典 differential / linear / boomerang / impossible differential 一系列

- 都受 rate limit 困扰
- 都是 CFE 同构候选

### 量子 differential

- Kaplan 2016 量子 query model · 假设 superposition query 可见
- CFE 跟 Kaplan 正交 · CFE 关心 R2 不可见性

### Side-channel cryptanalysis

- DPA / EM analysis · 不需要 chosen plaintext · 用泄漏的 power / EM 信号
- CFE differential 跟 side-channel 互补 · 不依赖泄漏

## 9 · Open questions

- OQ1:CFE-enhanced linear cryptanalysis 是否同样 powerful?
- OQ2:能否 CFE-attack key schedule (而不是 cipher round)?
- OQ3:跟 Grover key search 怎么 hybrid?
- OQ4:防御侧:detection of CFE differential physical probe 怎么设计?
- OQ5:法律 / 监管:CFE differential 是 "新型攻击工具" 吗?如何 export control?

## 10 · License

CC BY 4.0
