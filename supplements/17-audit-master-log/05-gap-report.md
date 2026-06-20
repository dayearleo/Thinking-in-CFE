# 05 · Gap Report · 审计发现的真实 Gap 清单

> 状态:230 claim 审计完成 · 本文件记录真实 Gap + 补强建议
> 对照 04-audit-summary.md (整体状态) + 07-prior-art-corrections.md (具体 §02 修订)

---

## Gap 分类

### Gap 类型 1 · 物理实验数据 Gap (5 个)

来自 batch-5 物理审计:

| Gap | 影响章节 | 补强路径 |
|---|---|---|
| **G1-1 · Multi-object IFM N>5 没人做过** | §10 A2/A3/A4 应用 niche | 资助 / 合作 实验 group 在 Quandela Ascella 或类似 UPP 上跑 N=8/N=10/N=12 · 验证 efficiency η(n) 衰减曲线 |
| **G1-2 · Salih scheme >95% success 实验未做** | §14 worked example · §17 同构方法论 | 需要 thousands of MZI · 当前 chip 物理上 N=6 max (Calafell) · 工艺突破必需 |
| **G1-3 · Chained MZI 视觉度累乘衰减实测未做** | §11.2 CAVEAT 5 | 在 N=20/N=100 试验台上实测 visibility 累乘衰减 · 验证 $(0.9994)^N$ 模型 |
| **G1-4 · CFC violation < 0.1% 没人 demo 过** | §15.5 R2 violation bound | 需要 N≥100 chained MZI + high visibility chip · 物理上极困难 |
| **G1-5 · 室温 single photon detector >90% 没人做** | §11.2 工作温度限制 | 当前 SNSPD 必 cryogenic · 室温 SPAD 效率掉 30-50% · 工艺研发 |

### Gap 类型 2 · 数学严格证明 Gap (3 个)

来自 §04 (open Q1-Q12):

| Gap | 影响章节 | 补强路径 |
|---|---|---|
| **G2-1 · Cost composition theorem 严格证明** | §04.3 (open Q1) | 形式化 quantum query model + Zeno scheme · 给 tight bound |
| **G2-2 · CFP 复杂度类公理化** | §07.7 (open Q9) | 跟 BQP 关系 · 是否子集 / 等价 |
| **G2-3 · 嵌套深度 lower bound** | §04.4 (open Q2) | 是否存在 fundamental limit |

### Gap 类型 3 · prior-art Gap (4 个)

来自 attribution audit:

| Gap | 影响章节 | 补强路径 (详 07-prior-art-corrections) |
|---|---|---|
| **G3-1 · [Noh 2009] Counterfactual Quantum Cryptography 子领域** | §02 / §15.9 / supplement 01 | 加 CQC 17 年文献链 (Noh 2009 / Yin 2010 / Liu 2012 等 6+ paper) · §15.9 加 PCC vs CQC disambig |
| **G3-2 · Subtraction-free complexity (Fomin 2013)** | §02 / §06.1 | 加 5th 类 disambig (algebraic complexity) |
| **G3-3 · 模糊 cite (E-016 QIUP / E-017 Lord / E-040 Hosseini / E-041 Kaplan)** | §99 | 4 个 entry 精确化 |
| **G3-4 · Year 偏差 (Wiesner 1969 vs 1983 published)** | §99 | entry 标 written + published year |

### Gap 类型 4 · 应用客户访谈 Gap (5 个)

来自 G 类应用审计:

| Gap | 影响章节 | 补强路径 |
|---|---|---|
| **G4-1 · A2 单细胞 multi-assay 客户访谈** | §10 A2 | 跟 QuantIC consortium / 单细胞分析 vendor 访谈 · 验证 N=5 niche 是否真满足需求 |
| **G4-2 · A4 stealth probing 军用 / 情报客户访谈** | §10 A4 | 敏感 · 需要 cleared channel · 验证 2.4% violation 是否 acceptable |
| **G4-3 · A5 半导体 wafer in-line 检测客户访谈** | §10 A5 | 跟 ASML / Zeiss / Applied Materials 等 wafer fab tools vendor 访谈 |
| **G4-4 · A6 核素勘探客户访谈** | §10 A6 | 跟 IAEA / 国家核安全监管访谈 |
| **G4-5 · 100M token context LLM (S28) 客户访谈** | suppl 28 | 跟 OpenAI / Anthropic / Mistral 访谈 是否真有 100M context demand |

### Gap 类型 5 · 工程 PoC Gap (4 个)

来自 simulator-to-hardware gap:

| Gap | 影响章节 | 补强路径 |
|---|---|---|
| **G5-1 · 12 simulator 都没硬件实现** | supplements 10/14/16-34 | 每个 simulator 需对应 photonic chip PoC · 当前都是 classical simulation 模拟 R1/R2/R3 |
| **G5-2 · HSM tamper bypass 真 hardware demo** | §16.6.1 / suppl 10 | 跟 HSM vendor (Thales / Utimaco) 在 lab 配合 demo 实际 EM probe / optical coupling |
| **G5-3 · CFE-Bloom PIR 真 photonic 实现** | suppl 14 | N=8 / N=16 / N=32 Bloom-mode PIR 流片 |
| **G5-4 · 跨 device IFM-attack primitive 实验** | §16.8 / suppl 16 UHT | 各 device 类型 (TPM / EMV / passport NFC) 独立 PoC |

### Gap 类型 6 · 标准化 Gap (3 个)

| Gap | 影响章节 | 补强路径 |
|---|---|---|
| **G6-1 · PCC 子领域标准化未启动** | suppl 01 / §15.9 | IACR ePrint 投稿 · 等待社区 review |
| **G6-2 · NIST PQC + PCC track 未提交** | suppl 04 | 实际提交 NIST 公开评论流程 |
| **G6-3 · HSM 厂商责任披露未发** | suppl 02/03 | 经 legal review 后发 4 厂商 (Thales / Utimaco / Entrust / AWS) |

---

## 总 Gap 汇总

- Gap 类型 1 (物理实验):5 个
- Gap 类型 2 (数学证明):3 个
- Gap 类型 3 (prior-art):4 个
- Gap 类型 4 (客户访谈):5 个
- Gap 类型 5 (工程 PoC):4 个
- Gap 类型 6 (标准化):3 个
- **总:24 个 Gap**

---

## Gap 优先级

按"修了之后论文 actionable 程度提升" 排:

### P0 (修了论文才能投学术)

- G3-1 加 [Noh 2009] CQC 子领域 (防 reviewer 抓 prior-art)
- G3-2 加 Fomin 2013 algebraic disambig
- G3-3 + G3-4 §99 cite 精确化

### P1 (修了论文更 robust)

- G2-1 cost composition 严格证明 (open Q1 至少给 sketch)
- G1-3 chained MZI visibility 实测 (验证 §11.2 CAVEAT 5)

### P2 (修了论文 commercial-grade)

- G4-1 ~ G4-5 客户访谈 (validation niche)
- G5-1 ~ G5-4 工程 PoC (validation 物理 attack)

### P3 (修了论文 industry-impact)

- G6-1 ~ G6-3 标准化提交

---

## 跟 §13 RFC 框架的 mapping

`paper/thinking-in-cfe/13-validation-and-rfc.md` 列了 20 条声明 · 本 Gap report 跟其 mapping:

- §13 声明 5/10/15/20 (物理实现) → G1-1 ~ G1-5 + G5-1 ~ G5-4
- §13 声明 1-4 (数学) → G2-1 ~ G2-3
- §13 声明 11-14 (应用) → G4-1 ~ G4-5
- §13 声明 16-20 (标准化) → G6-1 ~ G6-3

§13 RFC framework 已经 anticipate 这些 Gap · 但本 Gap report 是 audit 后的 concrete 化。

---

## 版本

- 2026-06-20 v1 · 230 claim 全审后整理
