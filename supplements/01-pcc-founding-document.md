# 01 · Post-Counterfactual Cryptography (PCC) · 子领域立项书

[← supplements README](README.md)

## 文件性质

**RFC / 立项书**。本文件不是论文 · 是邀请密码学社区**正式承认 PCC 作为一个独立子领域** 的提案。预期投递:IACR ePrint · 后续 CRYPTO / EUROCRYPT / ASIACRYPT rump session。

## 摘要 (Abstract)

We propose **Post-Counterfactual Cryptography (PCC)** as a new subfield of cryptography, analogous in structure and motivation to **Post-Quantum Cryptography (PQC)**. While PQC addresses the threat of quantum computers breaking mathematical hardness assumptions (RSA via Shor, AES via Grover), PCC addresses an **orthogonal threat**: the **Counterfactual Function Evaluation (CFE) operator** [Thinking-in-CFE 2026, §3] derived from 30+ years of Interaction-Free Measurement literature, which can probe physical cryptographic primitives (HSM, smart cards, secure enclaves) without triggering tamper detection, audit logs, or rate limits. Unlike PQC threats which require fault-tolerant quantum computers (FT QC) still distant, CFE threats are realizable today on integrated photonic IFM chips. We define PCC's scope, identify 5 open research directions, and call for the cryptographic community to adopt the **counterfactual adversary model** as a standard adversarial assumption.

## 1 · 为什么需要 PCC

### 1.1 · 现有密码学的两大威胁框架

| 框架 | 攻击对象 | 防御方向 | 时间线 |
|---|---|---|---|
| **Classical adversary** (传统) | 数学结构 + 实现漏洞 | 数学复杂度 · side-channel 防御 | 一直存在 |
| **PQC adversary** | 数学结构 (factoring / DLP) | lattice / code / multivariate / hash-based | 等 FT QC |
| **PCC adversary** (本提案) | 物理 oracle (HSM key / token / 物理 seal) · "probe 必检测" 假设 | 反事实-coherence 硬件 · counterfactual-aware 协议 · MPC 拆分 | **当下** |

PCC 是第三个**正交**框架 · 跟 classical / PQC 都不重叠。

### 1.2 · 为什么不在 PQC 框架内 cover

PQC 的核心是 "对手有 fault-tolerant 量子计算机"。但 CFE 攻击:

- 不需要 FT QC (用 photonic IFM 即可)
- 不攻击数学结构 (攻击物理实现)
- 攻击面跟 PQC 算法选择 **无关** (无论用 RSA 还是 lattice 都受影响 · 只要 key 进 HSM)

因此 PCC 必须 **独立成框架** · 不能塞进 PQC。

### 1.3 · 为什么不在 side-channel cryptography 框架内 cover

传统 side-channel cryptography (Kocher 1996, DPA 1999) 假设攻击者通过 power / EM / timing 等**可观察侧信道**提取秘密。CFE 攻击的关键不同:

- 传统 side channel:攻击者的 probe 仪器**物理上可被检测** (虽然实际很难)
- CFE:攻击者的 probe 在 $\delta \to 0$ 极限下**物理上不可被检测** (R2 性质)

因此 PCC 包含但不局限于 side-channel · 是 superset。

## 2 · PCC 的研究问题

定义 6 类核心 research questions:

### 2.1 · PCC-1 · Adversary Model Formalization

**问题**:把 CFE 攻击形式化为 cryptographic adversary model。

具体子问题:

- 给 counterfactual adversary 一个标准定义 (类比 CPA / CCA / IND-CCA2)
- 跟现有 quantum adversary model (QROM 等) 的关系
- 安全证明的 game-based framework 扩展

**期望产出**:正式 adversary model 文档 + 跟 standard models 的归约关系

### 2.2 · PCC-2 · Counterfactual-Resistant Hardware

**问题**:设计物理硬件 · 使 CFE probe 不可行或必触发。

具体子问题:

- **Coherence-based tamper detection** · 用 quantum coherence 替代 photo / temp sensor
- **Active probing 干扰**:HSM 主动发射 dummy probe · 让 CFE 攻击者无法区分真假 oracle
- **MPC-based root of trust** · 把 key 在多个 HSM 间拆分 · CFE 必须同时攻击全部
- **物理 randomization** · 让 oracle 在 query 间隔自我重排 · CFE 看到的 oracle 不一致

**期望产出**:至少 1 个 CFE-resistant HSM 原型设计 + 安全分析

### 2.3 · PCC-3 · Protocol Redesign

**问题**:现有协议 (TLS / Signal / 数字签名等) 在 CFE adversary 下需要怎么改?

具体子问题:

- TLS 1.3 的硬件根信任假设审计 · PCC 加固版本
- 数字签名的私钥保护 · PCC 兼容方案
- 短密码 / PIN 系统的根本重设计 (attempt counter 不能仅靠硬件)
- Zero-knowledge proof 在 CFE adversary 下的安全性

**期望产出**:1-2 个核心协议的 PCC 升级版

### 2.4 · PCC-4 · Detection of CFE Attacks

**问题**:已部署系统怎么检测自己被 CFE 攻击过?

具体子问题:

- CFE 攻击的物理痕迹 (即便 R2 让 oracle 触发率 $\delta$ 小 · 仍有 $\delta > 0$)
- Statistical anomaly detection 在 $\delta = 10^{-9}$ 下的 false-positive vs detection trade-off
- 长期 audit log 中 CFE pattern 的 ML-based 检测
- Honeypot 设计如何 evolve 应对 CFE-stealth

**期望产出**:CFE attack detection toolkit + lab 验证

### 2.5 · PCC-5 · Standards & Certification

**问题**:FIPS / Common Criteria / 中国密码法 / 各国 HSM 认证标准应如何 update?

具体子问题:

- 现有认证 (FIPS 140-3 Level 4 / CC EAL 6+) 在 CFE 攻击下的真实强度评估
- 新增 "Counterfactual Resistance Level" (CRL) 认证类别
- 标准化 PCC adversary model 跟 ISO 27001 / NIST CSF 的对接

**期望产出**:NIST / ISO TC68 / IETF 标准修订建议

### 2.6 · PCC-6 · Cross-cutting Theory

**问题**:跟现有理论框架的整合。

具体子问题:

- PCC 跟 information-theoretic security 的关系 (Holevo bound 仍 holds 吗?)
- PCC 跟 indefinite causal order 的可能组合
- PCC 跟 device-independent cryptography 的关系
- PCC 跟 quantum darwinism / decoherence theory 的关系

**期望产出**:跨学科 review 论文

## 3 · 跟现有学术工作的接续

PCC 不是凭空提出 · 接续如下既有线索:

| 既有工作 | 跟 PCC 关系 |
|---|---|
| Elitzur-Vaidman 1993 IFM | PCC 的物理基础 |
| Mitchison-Jozsa 2001 counterfactual computation | PCC 的算法雏形 |
| Lin-Lin 2015 bomb query complexity | PCC 的复杂度框架基础 |
| Gottesman 2003 quantum tamper-evident encryption | PCC 的 cryptography 早期先例 (但范围窄) |
| Hance 2025 multi-object IFM on chip | PCC 攻击的物理实物 demonstration |
| Goyal-Raizes 2025 Proofs of No Intrusion | 防御侧近邻工作 |

PCC 的**新意**:把上述分散工作**统一为 cryptography 内部一个独立子领域** · 跟 PQC 平级 · 有自己的 adversary model · 自己的 standardization track · 自己的 conference / journal venue。

## 4 · 立项要求

为正式立 PCC 子领域 · 需要密码学社区:

### 4.1 · 学术承认

- 在 CRYPTO / EUROCRYPT / ASIACRYPT 至少一个会议接受 "PCC track" 或 "PCC workshop"
- IACR 设立 PCC standing committee
- 至少 3 个独立 group 在 PCC 方向发表论文 (本文 + 邀请 2 个 follow-up)

### 4.2 · 标准对话

- NIST 设立 PCC working group (类比 PQC)
- ISO TC68 启动 PCC standardization 讨论
- IETF 设立 PCC IRTF research group

### 4.3 · 工业 awareness

- HSM 厂商 top 5 (Thales · Utimaco · Entrust · IBM · AWS) 公开承认 PCC 威胁评估
- 银行 / 央行 critical PKI 启动 PCC audit
- 国家级 critical infrastructure 启动 PCC 评估

## 5 · 立项时间线

提议路线图 (不给具体年份 · 给依赖链):

**Phase 1 · Seed** (依赖:本论文发布 + 邀请 advisor):
- 本论文 arxiv 投稿
- 邀请 5-10 位 senior cryptographer 担任 PCC advisor
- 启动 PCC mailing list

**Phase 2 · Establishment** (依赖:Phase 1 + 第一个 workshop):
- IACR workshop on PCC (申请 CRYPTO co-located)
- 第一批 follow-up 论文出现
- 第一个 CFE-resistant HSM 原型设计公开

**Phase 3 · Standardization** (依赖:Phase 2 + 多个独立 group 跟进):
- NIST PCC working group 成立
- 第一个 FIPS Counterfactual Resistance Level 草案
- ISO TC68 PCC 标准启动

**Phase 4 · Industrial deployment** (依赖:Phase 3 完成 + 至少 1 个 CFE-resistant HSM 产品上市):
- HSM 厂商 PCC-cert 产品发布
- 银行 / 央行 PCC 升级
- 跟 PQC migration 协调

每个 Phase 跟前一个 Phase 是**依赖关系** · 不预设时间。如果社区 traction 强 · 整个过程可能比 PQC 快 (因为 CFE 威胁的紧迫性 + 不依赖 FT QC 等待)。

## 6 · 立项的 risk 评估

诚实列 PCC 立项可能失败的原因:

- **Risk 1 · CFE 攻击被证伪** · 如果 [Hance 2025] 类实物 demonstration 被发现不能 scale 到 cryptographic-relevant $N$ · PCC 失去基础
- **Risk 2 · CFE 跟现有 side-channel 区分被否定** · 如果 reviewer 认为 PCC 只是 side-channel 的特例 · 不需要独立子领域
- **Risk 3 · 行业不 buy in** · HSM 厂商可能否认 CFE 威胁 · 拒绝 audit · 子领域 lacks industry pull
- **Risk 4 · 跟 PQC 资源竞争** · 密码学社区已大量投入 PQC · PCC 可能 starve for attention

为应对 risks · 本立项建议:

- 优先做 CFE 攻击的独立实物 demonstration (response to Risk 1)
- 严格 disambiguate CFE 跟传统 side channel (本立项 §1.3 + 论文 §15)
- 主动 reach out HSM 厂商 (论文 supplement 02-03)
- 寻找 PQC + PCC 协同的双重防御 narrative (Phase 4)

## 7 · 邀请加入 founder pool

我们邀请以下背景的人加入 PCC founder pool:

- 经验丰富的密码学家 (理论 + 实践)
- 量子光学实验学者 (理解 IFM 物理)
- HSM 工业界 security architect
- 标准制定者 (FIPS / ISO / NIST)
- 监管 / 政策研究者
- 投资人 / 创业者 (商业可行性视角)

理想 founder pool:**8-12 人 · 跨 academic / industry / regulatory · 跨地理 (US / EU / Asia)**。

## 8 · 联系方式

(论文正式发布后填写)

- 邮箱:`[TBD]`
- GitHub Issues:`[TBD]/issues`
- mailing list:`[TBD]@googlegroups.com`

## 9 · 引用本立项

```bibtex
@misc{pcc-founding-2026,
  title  = {Post-Counterfactual Cryptography: A Founding Document},
  author = {[作者待补]},
  year   = {2026},
  note   = {RFC, supplement to Thinking-in-CFE paper, June 2026}
}
```

## 10 · License

CC BY 4.0 · 详 paper root `LICENSE.md`
