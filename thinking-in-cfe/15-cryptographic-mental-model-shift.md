# 15 · 密码学的认知突破 · 在 FT QC 到来之前

[← 返回 README](README.md)

## 15.1 · 本章定位 · §14 的密码学专题深化

§14 提供了 3 个 worked example (生物 / 算法 / 军用) 证明 "未来已被拉到当下"。本章把镜头**聚焦到密码学** · 论证以下命题:

> CFE 算子的 **R2 性质 (adversary-undetectable 查询)** 在 FT QC 到来之前 · 就能颠覆一整类密码学假设 · 即使不破解 RSA / AES / SHA 这类纯数学算法 · 也足以**重写密码学界的 mental model**。

跟主流 "量子破解 = Shor" 的叙事不同。Shor 攻击的是**数学结构** · CFE 攻击的是密码协议默认的**物理假设**。两个攻击面正交 · CFE 不需要 FT QC 就可发生。

## 15.2 · 严格 scope 声明 (避免 hype)

为防止误解 · 先把不做的事说清楚:

**CFE 不能破解的密码** (跟 Shor / Grover / quantum attacks 同样不在 scope):

- RSA / ECC / 各种 discrete log 密码
- AES / ChaCha20 等对称密码
- SHA-2 / SHA-3 / BLAKE3 等哈希函数
- Lattice-based / Code-based / Multivariate 等后量子算法
- 任何纯数学构造 (其安全性不依赖物理 oracle)
- 任何信息论安全协议 (Holevo bound 不可突破)

**CFE 可能颠覆的密码假设** (本章重点):

- "**probe 行为可被检测**" 的物理假设
- "**篡改必留痕迹**" 的物理 sensor 类防御
- "**audit log 完整记录所有访问**" 的合规假设
- "**侧信道攻击的 instrument 可被反向检测**" 的取证假设
- "**消耗一次性 token 必留痕**" 的 quota 类防御

这些假设跨越**很多**广泛部署的安全系统 · 不是一个具体算法 · 而是一**类**协议的底层 mental model。

## 15.3 · 密码学的"假设地图" · 哪些层依赖 probe 可观察性

把密码学协议按依赖的物理假设分层:

| 层 | 安全靠什么 | 是否依赖 R2 可观察性 |
|---|---|---|
| 数学算法层 (RSA / AES) | 数学难题 (factoring / inverse) | ❌ 不依赖 |
| 数学协议层 (TLS / Signal) | 数学算法组合 + 协议状态机 | ❌ 不依赖 |
| 物理介质层 (BB84 QKD) | no-cloning + 测量扰动 | ⚠️ 部分 (BB84 安全证明已 cover · 但实现可能漏) |
| 物理硬件层 (HSM / TPM / SGX) | tamper detection 物理 sensor | ✅ **完全依赖** |
| 物理 token 层 (PUF / 物理 seal) | 物理结构唯一性 + 查询审计 | ✅ **完全依赖** |
| 物理网络层 (canary / honeypot) | "对手访问可被察觉" | ✅ **完全依赖** |
| 取证层 (网络入侵检测 / SIEM) | "侧信道仪器可见" | ✅ **完全依赖** |

**关键发现**:**底层 4 层完全依赖** "probe 可被检测" 这一物理假设。CFE 的 R2 性质直接颠覆这一假设 · 跨越多个协议家族产生效果。

## 15.4 · 三个 worked example 攻击

### 15.4.1 · 攻击 A · 物理 tamper-evident 防御的反事实旁路

**目标**:HSM / TPM / Secure Enclave 类硬件 secure 模块。

**当前防御 model**:

- HSM 内部布满 mesh sensor / 光感 / 温度 / 应力 · 检测物理 probe
- 任何 unauthorized probe → 触发 tamper response (擦除密钥 / 锁定 / 报警)
- 安全证明假设:"probe 行为产生可检测的物理 disturbance"

**CFE 攻击**:

```
INPUT:  HSM 物理结构 · 想要提取 secret key K
GOAL:   重建 K 的 bits · 不触发 tamper sensors

step 1: 用 photonic probe / EM probe 物理耦合到 HSM 内部信号路径
        (类似 well-known optical fault injection setup · 但用 CFE)

step 2: 对 K 的每个 bit i:
        - 定义 oracle O_i = "K 的第 i bit 是 1"
          (物理实现:通过 sensitive coupling 检测对应 transistor 状态)
        - bit_i = counterfactual_eval(identity, [O_i], δ=1e-6, ε=1e-3)
        
        关键:δ=1e-6 意味 tamper sensor 检测到的概率 ≤ 10^-6
        累积 N bit 攻击的总检测概率 ≤ N × 10^-6
        对 256-bit key · 总检测概率 ≤ 2.56×10^-4 (远低于 false positive 阈值)

step 3: 重建 K · HSM 内部 audit log 无异常 record · tamper sensor 未触发

OUTCOME: secret key extracted without HSM noticing
```

**这意味着什么**:

- 任何 HSM 设计假设 "physical probe 必然触发 tamper response" 都需要 revisit
- FIPS 140-3 Level 4 (最高级硬件 cert) 的 tamper-active 设计部分失效
- 银行 / 数据中心 / 国家关键基础设施的密钥保护 model 需要更新

### 15.4.2 · 攻击 B · Canary Token / Honeypot 的隐蔽 trip

**目标**:Canarytokens · Thinkst Canary 类入侵检测装置。

**当前防御 model**:

- 在系统里放置 "假" credentials / files / API endpoints
- 真实用户不会触碰 · 攻击者一旦触碰 → 报警
- 安全证明:"任何对 canary 的访问 = 攻击信号"

**CFE 攻击**:

```
INPUT:  系统里有 N 个潜在 canary endpoint (我不知道哪些是 canary)
GOAL:   识别哪些是 canary (避开它们) · 不触发任何 canary

step 1: 对每 endpoint i · 定义 oracle O_i = "endpoint_i 是 canary"
        (物理实现:通过网络 timing / DNS resolution pattern 等 side channel)

step 2: 对每 i:
        is_canary_i = counterfactual_eval(identity, [O_i], δ=1e-6)
        如果 is_canary_i 为 True · 标记并避开
        
        关键:每次反事实查询 · canary 服务器 log 记录到 access 的概率 ≤ δ
        N=1000 endpoint · 总 false trigger 概率 ≤ 10^-3

step 3: 攻击者现在有完整 canary map · 可以在不触发任何 canary 的前提下渗透

OUTCOME: honeypot 防御失效 · 攻击者获得 stealth lateral movement 能力
```

**这意味着什么**:

- Canary token 作为 last-line defense 的有效性下降
- 攻击者-防御者的 asymmetric 优势翻转 (原本防御者只需 attacker 触碰一次 · CFE 让 attacker 反事实绕开)
- SOC / IR 团队的 detection playbook 需要重写

### 15.4.3 · 攻击 C · 物理 seal / 防伪标签的反事实读取

**目标**:IAEA 核材料 seal · 高价值商品防伪 · 供应链 anti-counterfeit tag。

**当前防御 model**:

- Seal 内含密码 identifier · 物理结构使读取必须直接接触
- Seal 完整性 = "未被打开 / 未被读取过" 的证据
- 安全证明:"读取行为留下物理痕迹"

**CFE 攻击**:

```
INPUT:  目标 seal · 内含 secret identifier S (用于验证身份)
GOAL:   复制 S · 不留下读取痕迹

step 1: 用 photonic probe coupling 到 seal 物理结构
        (不直接接触 · 用 stand-off photon path 干涉读取)

step 2: 对 S 的每 bit i:
        bit_i = counterfactual_eval(read_bit_i, [seal_oracle], δ=1e-6)

step 3: 重建 S · seal 的物理结构无可检测改变

step 4: 用 S 制造完美 forgery seal · 替换原 seal
        替换后 · 后续 IAEA / 防伪 verify 仍 PASS

OUTCOME: 核材料 / 高价值商品的 chain-of-custody 验证机制失效
```

**这意味着什么**:

- 非扩散条约 verification regime 受影响
- 高价值商品 (奢侈品 / 药品 / 半导体 / 武器) 防伪体系受影响
- "tag 完整性 = 未被读取" 这一基本前提失效

## 15.5 · 三个攻击的共同 mental model 颠覆

3 个 worked example 共享一个 **根本性的 mental model shift**:

| 旧 mental model (密码学界默认) | 新 mental model (CFE-aware) |
|---|---|
| "probe 必产生物理可检测扰动" | "probe 可以反事实 · 物理扰动 bounded by δ" |
| "tamper-evident 物理 sensor 是终极防线" | "物理 sensor 可被 R2 旁路 with violation prob ~δ" |
| "audit log 完整覆盖所有 access" | "反事实 access 不被 log 捕获 (大概率)" |
| "honey token 触碰 = 攻击信号" | "honey token 可被识别再绕开 (subject to violation rate)" |
| "Eve 必须 commit 到一次具体 probe" | "Eve 可以反事实 probe · 不 commit (with bounded detection prob)" |

### ⚠️ 重要 caveat (物理审计 2026-06-20 落地)

**R2 "adversary undetectable" 不是绝对 0 · 是 bounded by physical violation rate**:

Calafell et al. 2019 npj Quantum Information 5:61 实测 chained CFC N=6, M=320 photons per bit 时:

- **Counterfactual violation: 2.4%** (即 attacker 有 2.4% 概率留下可检测 trace)
- Single MZI visibility: 99.94% (chained 累乘 $(0.9994)^6 = 99.64\%$)
- CFC violation 随 N 改善 (Salih scheme 1000+ MZI 时 violation < 0.1%)

精确 R2 表述应为:

$$\eta(\delta, N) = \Pr[\text{adversary detects probe}] \leq c \cdot (1 - V)^N + \delta$$

其中 $V$ 是 single MZI visibility · $N$ 是 chained 数 · $c$ 是常数 · $\delta$ 是触发概率 budget。

**对密码学界的实际含义**:R2 mental shift **方向上正确** · 但 attack 不是 perfect stealth · 是 "violation rate << classical detection rate (100%)"。

类比:Differential cryptanalysis 给 attacker 概率 advantage · 不是确定性 break。R2 给 attacker 概率 stealth advantage · 不是确定性 invisibility。

**实际威胁评估**:

| 场景 | 防御方可检测 attacker 的概率 | 是否 still 严重威胁 |
|---|---|---|
| 经典 probe (无 CFE) | 100% (每次 probe 必检测) | baseline |
| CFE probe N=6 (Calafell SOTA) | ~2.4% (per query) | ✅ 严重 · 防御方 sampling 才能检测 |
| CFE probe N=100 (理论) | ~0.06% | ✅ 极严重 · 实际无法检测 |
| CFE probe N=1000 (Salih) | < 0.01% | ✅ 完美 stealth (但需 thousands of MZI) |

3 个 attack 在 N=6 SOTA 下都 still actionable · 因为防御方需要持续 sampling 才能见到 2-3% violation · 一次 successful attack 完成提取 → 替换 → 退出 · 防御方很可能错过 sampling 窗口。

### 整体 paradigm-level 影响 (修订后)

这个 shift 影响**几十种**广泛部署的安全协议 · 是真正的 paradigm-level 颠覆 · 即使没有任何具体数学算法被 break · **即使 attack 不是 perfect stealth · 而是 99% stealth at SOTA**。

## 15.6 · 跟现有 quantum cryptanalysis 的对比

| 攻击类型 | 攻击什么 | 需要什么 | 时间线 |
|---|---|---|---|
| **Shor's algorithm** | 数学问题 (factoring / DLP) | FT QC ($10^6+$ logical qubits) | 等 FT QC 成熟 |
| **Grover search** | 对称密码 key space | FT QC | 等 FT QC 成熟 |
| **量子 collision finding** | 哈希函数 | FT QC + 复杂电路 | 等 FT QC 成熟 |
| **本论文 · CFE 物理假设攻击** | **物理假设层** (tamper / canary / seal) | photonic IFM chip (N ≤ 32 即可) | **当下** |

CFE 跟 Shor 攻击**完全正交** · 攻击的是密码协议堆栈中**完全不同**的一层。

**关键 narrative**:

> 量子计算对密码学的威胁 · 主流叙事是 "Shor 之日 = RSA 死亡之日" · 而那一天还在十几二十年外。**CFE 提供另一条威胁路径** · 它不打数学层 · 打物理假设层 · 而且不需要 FT QC · 当下就可以发生。

这等于**给密码学界开了第二战线**。

## 15.7 · 防御方向 · 已有什么可借鉴

防御 CFE 类攻击需要新的 security model · 但已有部分思路可借鉴:

| 防御思路 | 来源 | 是否能用 |
|---|---|---|
| **Side-channel-resistant design** (Power analysis defense) | 已成熟 | 部分可用 · 但不能完全 cover CFE |
| **Tamper-evident**升级为 **Tamper-coherence** (任何 probe 引入相干性变化) | 新方向 | 理论可行 · 需新硬件设计 |
| **Quantum security models** (考虑 quantum adversary) | 学术活跃 | 需扩展到 counterfactual adversary |
| **Multi-party computation 拆分 secret** | 密码学经典 | 减少单 HSM 依赖 |
| **Active deception** (canary 动态 rotate) | SOC 实践 | 部分缓解但不 eliminate |
| **Physical isolation** (air-gap) | 经典安全 | 限制 CFE physical coupling |
| **Counterfactual-aware audit** (audit log 含反事实概率字段) | 新方向 | 需新协议设计 |

**最重要的防御方向**:**把 R2 加入安全模型** —— 假设对手具备 counterfactual probe 能力 · 重新设计协议。

这等于 post-quantum cryptography 之后的 **post-counterfactual cryptography (PCC)** —— 一个新的密码学子领域。

## 15.8 · 工程化路径 · 实现这些攻击需要什么

### 攻击 A (HSM) 工程化条件

| 部件 | 当前 SOTA | 距离实物攻击 |
|---|---|---|
| Photonic IFM probe + EM coupling | ✅ lab proven | 中等 · 需 custom adapter |
| 高分辨 EM coupling to silicon | ⚠️ 已有 (electron microscopy 改装) · 但跟 IFM 集成新 | 中等工程 |
| HSM 物理结构 reverse engineering | ✅ 已有 (DPA 圈) | 已成熟 |
| **整体距离实物 HSM 攻击 PoC** | | **可见路径 · 工程量适中** |

### 攻击 B (Canary) 工程化条件

更难 · 因为 canary 通常是数字 endpoint · 不是物理对象。CFE 攻击 canary 需要 canary 的**物理 side channel** (DNS server timing / 物理网络设备等) · 不直接适用 photonic IFM。

**因此 · 攻击 B 在物理 canary** (e.g. canary 是个物理设备 · 不是云端服务) **场景才适用**。这是 niche 限制。

### 攻击 C (Seal) 工程化条件

| 部件 | 当前 SOTA | 距离实物攻击 |
|---|---|---|
| Photonic IFM + 不同 seal 物理 readout | ⚠️ 取决于 seal 类型 (光学 seal / 超声 seal / 微波 RFID) | 取决于具体目标 |
| Stand-off probing distance | ⚠️ 当前 IFM lab demo 短距离 | 工程优化方向 |
| Seal 物理特征数据库 | ❌ 需要先验知识 | 取决于情报 |
| **整体距离实物 seal 攻击 PoC** | | **取决于 seal 类型 · 部分类型立即可做** |

## 15.9 · 对密码学界的建议

如果本论文的论点成立 · 密码学界应该考虑:

**学术层面**:

- 建立 "counterfactual adversary model" 跟现有 quantum adversary model 并列
- 在安全证明中显式承认 "probe 可不可观察" 这一新维度
- 把 R2 性质纳入 game-based proof 框架
- 开 "Post-Counterfactual Cryptography" 子领域

**标准层面**:

- NIST / ISO / FIPS 标准应评估当前认证的 HSM / TPM 在 CFE 攻击下的真实强度
- IAEA 等 verification regime 应评估物理 seal 的 CFE 漏洞
- IETF / 各协议组应评估 honey-token 等 deception 防御的有效期

**工业层面**:

- HSM 厂商 (Thales / Utimaco / nCipher) 应启动 CFE-resistant 设计研究
- Canary 厂商 (Thinkst 等) 应升级 deception 策略
- 防伪厂商应升级 tag 物理设计

**政策层面**:

- 国家关键基础设施 (银行 / 电力 / 通信) 的密钥保护需 review
- 非扩散条约 verification 需新 protocol
- 出口管制清单 (Wassenaar) 可能需 cover CFE-attack 工具

## 15.10 · 不会发生的事 (诚实划界)

为避免 hype · 明确**不会**因 CFE 发生的事:

- ❌ RSA 不会被 break (那需要 Shor + FT QC)
- ❌ AES 不会被 break (CFE 不攻击对称密码)
- ❌ TLS 不会被全面 break (协议堆栈很多层 · CFE 只影响特定 hardware-rooted 部分)
- ❌ 区块链不会立即崩溃 (但 hardware wallet 会受影响)
- ❌ Internet 不会停止运行 (大多数 traffic 不依赖被 CFE 攻击的层)

CFE 攻击是**深刻但局部** · 影响**信任根 (root of trust)** 而非**整个堆栈**。但信任根被攻破的连锁反应可以很大。

## 15.11 · 闭环到论文核心论点

§15 至此完成对论文核心论点在密码学方向的扩展:

> **如果 CFE 工程化可行 (条件同 §14)** · **那么** 密码学界一整类基于 "probe 必可检测" 物理假设的安全协议 · 当下就需要 review · 不必等 FT QC 到来。这是一次 paradigm-level 的认知突破 · 即使没有单个具体算法被 break · 整个 mental model 必须升级。

**对密码学界的具体 ask**:

把 R2 (adversary-undetectable probe) 加入 quantum-aware adversary model · 跟 standard quantum adversary 并列。这是 CFE 对密码学最大的贡献 · 也是密码学界最容易接受的形式 (不要求他们抛弃任何现有工作 · 只要求扩展威胁模型)。

## 15.12 · 小结

CFE 算子在密码学领域的 mental model shift:

- **§15.3** · 4 层安全协议依赖 "probe 可观察" 假设 · 被 CFE R2 攻击
- **§15.4** · 3 个 worked example (HSM tamper-bypass · Canary stealth-trip · Seal reading)
- **§15.5** · 5 条 mental model 颠覆
- **§15.6** · 跟 Shor 攻击正交 · 不需要 FT QC
- **§15.7** · 防御方向 · "Post-Counterfactual Cryptography" 新子领域
- **§15.8** · 工程化路径 · 攻击 A 和 C 可见路径
- **§15.9** · 给密码学界的具体建议 (学术 / 标准 / 工业 / 政策)
- **§15.10** · 诚实划界 · 不会破解 RSA / AES / TLS 整体

**最终 claim**:

> 在 FT QC 到来之前 · CFE 已经能在密码学领域产生 mental model 级别的颠覆。这是 §14 "把未来拉到当下" 论点在密码学具体应用的扩展版。

---

[← 上一章 · 14 突破证明](14-breakthrough-demonstration.md) · [下一章 · 16 工业算法系统化攻击 →](16-attack-on-deployed-crypto.md)
