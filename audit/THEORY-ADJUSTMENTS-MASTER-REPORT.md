# CFE 理论 + 跨学科挑战调整总报告

> **日期**:2026-06-20 · v1
> **触发**:user verbatim "CFE 理论本身以及其后续我们分析的各种引用和对现有其他学科研究的挑战 · 需要作出怎样的调整"
> **基础**:audit/batch-5 (物理 SOTA 实验数据) + audit/batch-11 (PhD thesis + critical paper) 两轮深度审计
> **位置**:本文件 = CFE 论文修订决策的单点真理源 · supplement 17 同步 mirror

---

## 0 · 一句话总结

**CFE 理论核心论点 still stand** · 但**论文必须做 8 类系统性调整** · 涵盖 R1/R2/R3 严格成立规模 / 物理 SOTA 数字 / 公式严格性 / 对密码学 prior-art / 对 quantum foundations critical paper 的 engagement / 应用 niche scaling / 命名 disambiguation / 学术发布策略。修订后论文 still publishable · 但**单 IFM 规模 R1/R2/R3 "quantum-only" claim 是 contested in physics community** · 必须 honest disclose。

---

## Part I · CFE 理论本身的调整 (6 项)

### 调整 I.1 · R1/R2/R3 differentiator 必须分规模 ⚠️ 关键

**原 claim** (§03.7):

> 只有 $\Phi^{CF}_f$ 同时具备 R1 + R2 + R3 —— 这是算子的核心 differentiator (经典都不行)。

**实际**:

| IFM 规模 | R1/R2/R3 quantum-only? | 经典系统可 reproduce? | Source |
|---|---|---|---|
| Single bomb tester (1 obstacle) | ❌ **不严格成立** | ✅ hydrodynamic pilot-wave 25% 等价 | [Frumkin-Bush 2023, PRA 108:L060201] |
| Chained Zeno (Kwiat 1995, N≥6) | ✅ 严格成立 | ❌ 需任意 scale nonlocal wavefunction | [Calafell et al. 2019, npj QI 5:61] |
| Multi-object IFM (Franco 2026, N≥5) | ✅ 严格成立 | ❌ 全局 entangled probe state | [Franco-Camillini-Galvão 2026, arxiv 2604.04691] |

**调整内容**:

§03.7 / §11.2 加 caveat (✅ 已落地 commit 9d83bb6):

> **Single bomb tester 规模**:R1 性质可以 classical pilot-wave 模拟 (Frumkin-Bush 2023)
> **Chained / multi-object IFM 规模**:R1/R2/R3 严格 quantum-only · CFE 算子的实际工程 niche 都在这个规模 (§10 假设 N≥2 chained) · 论点 not affected

**为什么 not affected**:CFE 12 simulator 全部假设 chained / multi-object · §10 6 个挑战问题全部假设 N≥2 oracle · single bomb tester caveat 仅是 honest disclosure。

### 调整 I.2 · 物理 SOTA 数字精确化

**原 claim** (§03.9):

> N=12 universal photonic processor lab proven · 端到端 5 dB loss · counterfactual efficiency 单链路 > 99%

**实际**:

| 维度 | 论文原 claim | 实测 SOTA |
|---|---|---|
| N=12 | "已 lab proven" | **N=12 是 Quandela Ascella platform mode 数** · multi-object IFM 实测 **N=5** [Franco 2026] |
| 5 dB loss | "端到端" | **3 dB per facet** [Calafell 2019] · system 加 heralding 3% + detection 90% · 总 efficiency ~few % |
| > 99% 单链路 | "counterfactual efficiency" | **single MZI visibility 99.94%** [Calafell 2019] · chained N=6 protocol bit success **99% needs M=320 photons per bit** · CFC violation 2.4% |

**调整内容**:✅ 已落地 commit ab8aba4

§03.9 SOTA 表 8 维度精确化 · §11.2 加 5 个 CAVEAT · §10 A2/A3/A4 加 N≤10 niche caveat

### 调整 I.3 · R2 violation finite (~2.4%)

**原 claim** (§03.7 / §15.5):

> R2 · adversary 不可检测 · 在 $\delta \to 0$ 极限

**实际**:

- Calafell 2019 实测 chained N=6, M=320 时 CFC violation **2.4%**
- R2 应为 "**bounded adversary observability** with probability $\eta(\delta, N) \leq c \cdot (1-V)^N + \delta$"
- 不是绝对 0 · 是 finite bounded

**调整内容**:✅ 已落地 commit ab8aba4 (§15.5 加 4 scenario 实际威胁评估表)

但 attack 仍 actionable · 因为 attacker 一次 successful 提取就够 · 防御方需 sampling 才能 catch 2.4% violation · 实际攻击 window 短。

### 调整 I.4 · 数学公式漏平方 ⏳ 必修未修

**原 claim** (§03.5 子算子目录):

| 算子 | 论文公式 |
|---|---|
| $\Phi^{CF}_{\text{OR}}$ | $O(\sqrt{N}/\delta)$ |
| $\Phi^{CF}_{\text{AND}}$ | $O(\sqrt{N}/\delta)$ |
| $\Phi^{CF}_{\text{COUNT}}$ | $O(\sqrt{N \cdot \text{ans}}/\delta)$ |
| $\Phi^{CF}_{\text{T}_t}$ | $O(\sqrt{Nt}/\delta)$ |

**实际**:从 $B_\delta(f) = O(Q(f)^2/\delta)$ 推 · $Q(\text{OR}) = \Theta(\sqrt{N})$ · 平方 $= N$ · 不是 $\sqrt{N}$。

正确公式:

| 算子 | 正确公式 |
|---|---|
| $\Phi^{CF}_{\text{OR}}$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{AND}}$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{COUNT}}$ | $O(N \cdot \text{ans}/\delta)$ |
| $\Phi^{CF}_{\text{T}_t}$ | $O(Nt/\delta)$ |

**或者**:verify Lin-Lin 2015 原版精确 bound (可能 OR 有 tighter special-case bound · 如 $O(N/\log^2 N / \delta)$)。

**调整内容**:⏳ P0-5 待修 (audit/07-prior-art-corrections.md)

### 调整 I.5 · δ-extension of Lin-Lin 2015 必须明示

**原 claim** (§03.2 P3):

$$B_\delta(f) = O(Q(f)^2/\delta) \quad [\text{Lin-Lin 2015}]$$

**实际**:Lin-Lin 2015 原版是 $B(f) = \Theta(Q(f)^2)$ · 无 δ 参数。我们的 $B_\delta$ 是显式 δ-参数化扩展 · 论文未明示。

**调整内容**:⏳ P0-4 待修 · 加 explicit 说明 "this is δ-parameterized extension of Lin-Lin 2015"。

### 调整 I.6 · Cost composition theorem 是草案

§04.3 5 种组合的 cost 公式当前已 honest 标 "合理估计 · 不是严格证明 · open Q1"。状态 **OK** · 不需调整 · 但论文投学术 venue 时 reviewer 可能要 sketch proof · 应在 §11 Q1 加可证明的方向。

---

## Part II · 对量子计算的调整 (4 项)

### 调整 II.1 · D3 仍永久独占 (但措辞调整)

**核心论点不变**:CFE 永久独占外部物理 oracle interface domain · FT QC 不可达。

**措辞调整建议**:

| 原措辞 (易被误解) | 改后 (精确) |
|---|---|
| "我们超越未来 FT QC" | "FT QC 永远到不了 D3 interface domain · 不是 capability superset" |
| "CFE 算子是 quantum-only" | "CFE 算子是 quantum-physical edge controller · 跟 FT QC 正交不替代" |

**为什么**:reviewer 会误以为我们 claim D1 capability 超越 · 实际我们 honest 说 D1 是 FT QC 子集 (§05.2)。措辞统一更安全。

### 调整 II.2 · D1 capability 我们是 FT QC 子集 · honest 不变

**调整**:无 · 现状 OK。

### 调整 II.3 · D2 cost 6 数量级优势 confirmed

**调整**:无 · batch-5 confirmed $100k vs $10^8-10^{10}。但建议加 caveat:这是 **同 capability** 比较 · CFE 是 specialized · FT QC 是 universal · 不严格 "便宜 6 数量级" 是公平比较。

### 调整 II.4 · "提前 10-20 年解锁" 改为 "在 N≤10 niche 提前解锁"

**原 claim** (§00 摘要):

> CFE 算子是 quantum-only 能力 · 但用专用 photonic 硬件提前 10-20 年解锁

**实际**:N≤10 niche 当前可解锁 (Franco 2026 N=5 实测) · N=100+ 仍需未来突破。

**调整内容**:§00 摘要 + §05.3 加 caveat:

> CFE 在 **N≤10 multi-object IFM 规模** 上 · 用专用 photonic 硬件提前 10-20 年解锁。N=100+ 规模仍需未来 photonic chip 工艺突破 (光损 + visibility + 集成度)。

---

## Part III · 对量子物理基础 (quantum foundations) 的调整 ⭐ 关键

### 调整 III.1 · Frumkin-Bush 2023 critical paper 必须 engage ⚠️ 关键

[Frumkin-Bush 2023, PRA 108:L060201] 是 IFM 文献中的 critical paper · 我们论文必 cite + must engage。

**Frumkin-Bush 核心论点**:

> "We argue that existing rationalizations of interaction-free quantum measurement in terms of particles being guided by waveforms allow for a classical description manifest in our hydrodynamic system, wherein the measurement is decidedly not interaction-free."

**实验**:walking droplet on 7 mm silicon oil at 80 Hz vibration · 实测 droplet 25% detection 跟 EV 量子 IFM 25% 等价。

**对论文 implication**:

- §03.7 R1/R2/R3 严格 "quantum-only" claim 在 single bomb tester 规模 **不成立**
- 但 Frumkin-Bush 自己 honest 标:hydrodynamic system 受 finite memory + finite spatial extent 限 · 不能 reproduce chained Zeno / multi-object

**调整内容**:✅ 已落地 commit 9d83bb6

§02.7 加 PhD-level synthesis section 引 Frumkin-Bush 2023 + Bush 2021 综述 · §11.2 加 CAVEAT 6 · §03.7 加 caveat。

### 调整 III.2 · 引 constructor theory framework (Violaris 2025)

[Violaris DPhil thesis 2025, Oxford] 用 constructor theory (Deutsch-Marletto 2015) 框架研究 macroscopic quantum counterfactuals。

**对论文 implication**:

- §05 D3 论证 (CFE 跟 FT QC categorical 差异) 可以用 constructor theory 形式化
- 加 cite 让论文更 rigorous (Oxford Vedral/Ekert/Deutsch supervisor 阵容是 quantum foundations 权威)

**调整内容**:⏳ P1-4 待修 · §05.4 加 constructor theory cite

### 调整 III.3 · Hance-Ladyman-Rarity 2021 form proof for CFC

[Hance-Ladyman-Rarity 2021, Found. Phys. 51:12] 形式论证 counterfactual communication protocols 必需 quantum (wave-particle duality)。

**对论文 implication**:**支持** 我们 §03.7 differentiator 在 CFC 规模 (= multi-object) 的论点 · 但 paper 限定 "proposed so far" · 留 open 是否经典 future 可以做。

**调整内容**:✅ 已加到 §02.7 + §99 L1 section (commit 9d83bb6)

### 调整 III.4 · wave-particle duality 必需性的 nuance

**整合上 3 项的精确表述**:

| 规模 | wave-particle duality 必需? | 经典可模拟? |
|---|---|---|
| Single bomb tester | ❌ 不严格必需 (Hardy 1992 / Frumkin-Bush 2023 pilot-wave 描述够) | ✅ hydrodynamic 25% etfc 等价 |
| Chained Zeno | ✅ 必需 (Kwiat 1995 polarization-based + nonlocal wavefunction) | ❌ finite memory 限 |
| Multi-object IFM | ✅ 必需 (Franco 2026 全局 entangled probe) | ❌ 同上 |
| Counterfactual communication | ✅ 必需 (Hance-Ladyman-Rarity 2021 形式证明) | ❌ |

**调整内容**:§03.7 R1/R2/R3 表加 nuance 列 (✅ 已加 commit 9d83bb6)

---

## Part IV · 对密码学的调整 (4 项)

### 调整 IV.1 · [Noh 2009] CQC 17 年子领域必须 disambiguate ⏳ 必修

**Counterfactual Quantum Cryptography (CQC)** 自 [Noh 2009] PRL 103:230501 起是 17 年 active 子领域:

- Noh 2009 · Counterfactual Quantum Cryptography 起源
- Yin 2010 · Security proof
- Liu 2012 · Eavesdropping analysis
- Liu 2012 (PNAS · 实验) · Direct CFC via Zeno
- 2020 Sci Rep · Semi-counterfactual Quantum Bit Commitment
- npj 2023 · Counterfactual communication without trace

**我们 PCC 命名跟 CQC 容易冲突**。

**调整内容**:⏳ P0-3 待修

§02 加 CQC 6+ paper · §15.9 + supplement 01 加 PCC vs CQC disambiguation 段:

> CQC 用 counterfactual 性质**构造** cryptographic protocol (QKD-like) · 我们 PCC 用反事实性质**防御** cryptographic attack (R2 stealth bypass tamper-evident hardware) · **正交研究方向** · 共同构成 "counterfactual-aware cryptography" 完整图景。

**或者**:考虑改名:

- 候选 1:Counterfactual-Resistant Cryptography (CRC) · 类比 Quantum-Resistant Cryptography
- 候选 2:Anti-Counterfactual Cryptography
- 候选 3:Counterfactual-Aware Cryptography (CAC)

### 调整 IV.2 · R2 stealth attack 严格成立条件

**实测**:Calafell 2019 N=6, M=320 时 R2 violation **2.4%** · 不是 0。

**对 attack model 的影响**:

| 场景 | 防御方可检测 attacker 的概率 | 是否仍严重 |
|---|---|---|
| 经典 probe (无 CFE) | 100% (每次必检测) | baseline |
| CFE probe N=6 (Calafell SOTA) | ~2.4% (per query) | ✅ 严重 · 需 sampling 才检测 |
| CFE probe N=100 (理论) | ~0.06% | ✅ 极严重 |
| CFE probe N=1000 (Salih) | < 0.01% | ✅ 完美 stealth (但需 thousands MZI) |

**调整内容**:✅ 已加 §15.5 4 scenario 表 (commit ab8aba4)

attack 仍 actionable 因为 attacker 单次提取就够 · 防御方 sampling 窗口短。

### 调整 IV.3 · 17 算法 audit 论点不变

**核心论点不变**:0/17 数学破 + 17/17 HSM 层破 · narrative strong。

**调整**:无 · 跟 §16 内容 strict 一致。但每算法的 attack-success-probability 应加 (1-2.4%) ≈ 97.6% per single attack · 多 attempt 仍 actionable。

### 调整 IV.4 · Salih 2013 scaling 必加 caveat

Calafell 2019 引述 Salih scheme:**"thousands of optical elements 才 >95% success"**。

**调整内容**:⏳ P2-1 待修 · §14 + §17 引用 Salih 2013 时加 caveat:

> "Salih 协议在 thousands of MZI limit 下达到 >95% efficiency [Calafell 2019 引述]。当前 chip 物理上 N=6 max [Calafell 2019] · 实际工程需要 chip 集成度突破。"

---

## Part V · 对各应用学科的调整 (5 项)

### 调整 V.1 · 生物 / 单细胞 multi-assay (A2 / S22) · N≤10 niche

**原 claim** (§10 A2):"测 N 个 property (N 可能 20-50)"

**实际**:Franco 2026 multi-object IFM SOTA **N=5**。

**调整内容**:✅ 已落地 commit ab8aba4 · §10 A2 加 "Niche 当前应聚焦 N≤10 场景 (例 5 种 binding affinity assay 而非 50 种)"

### 调整 V.2 · 半导体 wafer in-line 检测 (A5) · scaling caveat

同 V.1 · scaling 受 N=5 multi-object IFM 限。

**调整内容**:✅ 已加 §10 A5 SOTA caveat (commit ab8aba4)

### 调整 V.3 · stealth probing 军用 (A4) · violation 2.4% caveat

**调整内容**:✅ 已加 §10 A4 + §15.5 (commit ab8aba4)

### 调整 V.4 · ML / Federated Learning (S22 / D014) · privacy 是 bounded

**原 claim** (S22):"3 mode accuracy 完全一致 · CFE 0 物理 leak"

**实际**:CFE 0 leak 是 simulator 模拟 · 实际硬件 violation 2.4%。

**调整内容**:supplement 22 README 加 caveat:

> simulator 模拟 R3 性质 (input 不消耗) · 跟 R2 violation finite 互相 orthogonal · privacy claim 在 R3 维度严格 · R2 维度 bounded by violation rate。

### 调整 V.5 · 12 simulator 都加 SOTA caveat

所有 12 simulator README (supplements 10/14/16-34) 都应加:

> simulator 模拟 R1/R2/R3 性质 · 实际硬件 SOTA N≤32 mode · multi-object IFM N=5 max · system efficiency ~2.7% (heralding 3% × detection 90%)。

**调整内容**:⏳ 待修 · 12 simulator README 批量加 caveat

---

## Part VI · 对算法理论 / 计算复杂度的调整 (3 项)

### 调整 VI.1 · D2/D3/D4 NOVEL 维度 confirmed

**调整**:无 · NOVEL 维度框架 ✅ 已 confirm (audit/06-novelty-defense.md NOVEL #2-5)。

但 D3 adversary observability 应精确化:

$$D_3 = \eta(f, \delta, N) \leq c \cdot (1-V)^N + \delta$$

不是 $\eta \to 0$ · 是 $\eta$ bounded · 单调降 with N + V。

**调整内容**:⏳ §07.2 D3 定义加 explicit formula

### 调整 VI.2 · 减法计算范式 NOVEL + 加第 5 类 algebraic disambig

§06.1 当前 4 类邻近 disambig (LLM / 心理学 / ML / 因果) · 应加第 5 类:

> **(E) "Subtraction-free complexity" / algebraic complexity** · 例 [Fomin 2013, arxiv 1307.8425] "Subtraction-free complexity, cluster transformations, and spanning trees"。algebraic complexity 子领域 · 研究在仅允许加 / 乘 (不允许减) 的算术电路中评估多项式的复杂度。跟 SCP 是符号 / 结构层面 · 不是 quantum-physical 反事实。

**调整内容**:⏳ P1-1 待修

### 调整 VI.3 · 6 算法模板 + 5 步代数化方法论 NOVEL

**调整**:无 · ✅ 已 confirm。但 6 模板 (CPA/CBB/CAL/CV/CA*/CGTS) 复杂度上界应加 caveat:都受 R2 violation 2.4% 限 · 实际 attack-success ~97% per attempt。

### 调整 VI.4 · CFP 复杂度类 vision · 跟 BQP 关系 open

§07.7 当前已 open · 状态 OK。

---

## Part VII · 对学术发布策略的调整 (5 项)

### 调整 VII.1 · 投稿前必修清单 (待修)

| Correction | 优先级 | 状态 |
|---|---|---|
| P0-3 加 [Noh 2009] CQC 子领域 | P0 | ⏳ 必修 |
| P0-4 §03.2 P3 加 δ-extension 说明 | P0 | ⏳ 必修 |
| P0-5 §03.5 子算子公式漏平方 | P0 | ⏳ 必修 |
| P1-1 §06.1 加 5th algebraic disambig | P1 | ⏳ 应修 |
| P1-2 §99 year/published 精确化 | P1 | ⏳ 应修 |
| P1-3 §99 7 模糊 entry 精确化 | P1 | ⏳ 应修 |
| P1-4 §05 D3 加 constructor theory framing | P1 | ⏳ 应修 |
| P2-1 §14 Salih caveat | P2 | ⏳ nice-to-have |

### 调整 VII.2 · 投稿 venue 选择 (按 fit 排)

**学术 venue (paper)**:

1. **Quantum Science and Technology** (IOPscience) · 已含 IFM / counterfactuality 多 paper (IOP 2024 ad63c7) · §04 组合代数 + §07 复杂度框架 fit
2. **Foundations of Physics** · 已含 Hance-Ladyman-Rarity 2021 + Vaidman 历史 paper · §05 D3 + §03.7 quantum foundations 论点 fit
3. **Physical Review A** · 已含 Frumkin-Bush 2023 critical paper · 我们必 cite + engage · §03/§04 数学定义 + 实验 SOTA fit
4. **Nature Communications** · 已含 Franco 2026 multi-object IFM · §10 + §17 应用层 fit
5. **IACR ePrint + EUROCRYPT** · §15 + §16 + supplement 01 PCC 子领域 + 17 算法 audit fit
6. **arxiv quant-ph + cs.CR** · cross-listing · 投稿前 mirror

**RFC / 标准化**:

7. **NIST PQC 公开评论** · supplement 04 NIST PCC track proposal · 在 PCC 改名后投
8. **IETF / ISO 量子密码标准 WG** · supplement 01 PCC founding 投

### 调整 VII.3 · RFC 流程加 audit/ 指针

`paper/thinking-in-cfe/13-validation-and-rfc.md` 已 outline RFC framework。加 audit/ + supplement 17 / §18 指针:

> reviewer 可 `cd audit/ && grep AUD-` 验证任意 230 claim 的证据链。3 个 REFUTED 已修 · 58 个 PARTIAL 含 caveat · 11 个 NOVEL 有 EXA 撞名 0-hit 证据 + 5 类邻近 disambig。

### 调整 VII.4 · 同行评审 anticipation

`audit/06-novelty-defense.md` 已含 7 个 reviewer 攻击预案:

1. cite Hance 2025 错 → 已修 Franco-Camillini-Galvão 2026
2. SCP 不是新词 → 5 类邻近 disambig
3. N=12 vs Franco 2026 N=5 → §03.9 精确化
4. R2 violation 2.4% → §15.5 加 bound
5. PCC vs CQC 命名冲突 → ⏳ P0-3 待修 + 考虑改名
6. 12 simulator classical 模拟 · 没硬件 → 跟 §13 RFC framework 一致
7. δ-extension of Lin-Lin 没明确 → ⏳ P0-4 待修

加第 8 攻击预案 (本次 batch-11 加入):

**攻击 8 · "Frumkin-Bush 2023 challenge R1/R2/R3 quantum-only"**

- 回应:已 cite + engage in §02.7 + §11.2 CAVEAT 6 + §03.7 caveat
- 论点改为:single IFM 规模 R1 可以经典模拟 · chained / multi-object 规模 quantum-only (受 finite memory 限)
- CFE 应用 niche 全部在 chained / multi-object 规模 · 论点 not affected

### 调整 VII.5 · 共同 author / 致谢策略

**潜在共同 author** (跟我们论文有直接 cite + collaboration potential):

- Cedric Lin / Han-Hsuan Lin (Lin-Lin 2015 · MIT) · 数学层
- Jonte R. Hance (Bristol PhD 2023 · Newcastle) · 物理基础 + CFC
- Sara Franco / Anita Camillini / Ernesto F. Galvão (Franco 2026 · INL) · 实验
- I. Alonso Calafell + 13 co-authors (Calafell 2019 · MIT QPL) · 实验 chip
- Stanislav Filatov / Marcis Auzinsh (Latvia · multi-object IFM theory) · 理论

**致谢**:论文 §18.8 已 outline · 应加 Frumkin-Bush 2023 (critical paper engagement) + Hance-Ladyman-Rarity 2021 (form support)。

---

## Part VIII · 核心论点 status 总结

### ✅ Still stand (论文修订后仍成立)

| 核心论点 | Status | 修订? |
|---|---|---|
| **D3 永久独占外部物理 oracle** (FT QC 不能 probe 外部样本) | ✅ | 措辞统一 (II.1) |
| **17 算法 audit 0/17 数学破 + 17/17 HSM 破** | ✅ | 加 attack probability 97.6% per attempt caveat |
| **减法计算范式 NOVEL** | ✅ | 加第 5 类 algebraic disambig (VI.2) |
| **12 simulator 工程 backing** (60 unit test 全 pass) | ✅ | 加 SOTA caveat (V.5) |
| **30+ 年文献链 + PhD thesis synthesis** | ✅ | batch-11 加 6 新 source (III.1-4) |
| **D2 cost 6 数量级优势** | ✅ | 加 specialized vs universal caveat |
| **CFE 物理基础真实 NOT 空中楼阁** | ✅ | (batch-5 + batch-11 双确认) |
| **D2/D3/D4 NOVEL 维度** | ✅ | D3 加 explicit formula (VI.1) |
| **6 算法模板 + 5 步代数化方法论 NOVEL** | ✅ | 加 R2 violation 影响 (VI.3) |

### ⚠️ 已 caveat (论文已加 honest disclosure)

| Claim | Caveat | 落地 |
|---|---|---|
| R1/R2/R3 quantum-only | 仅 chained / multi-object 规模 · single IFM 经典可模拟 (Frumkin-Bush 2023) | ✅ commit 9d83bb6 |
| N=12 lab proven | platform mode 数 · IFM SOTA N=5 | ✅ commit ab8aba4 |
| 5 dB end-to-end | per-facet · system 端到端 ~few % | ✅ commit ab8aba4 |
| >99% efficiency 单链路 | single MZI visibility · chained 需 M=320 photons per bit | ✅ commit ab8aba4 |
| R2 adversary undetectable | bounded violation ~2.4% · 不是绝对 0 | ✅ commit ab8aba4 |
| Multi-object IFM η(n) | 随 n 快速衰减 (Franco verbatim) | ✅ commit ab8aba4 |
| "10-20 年提前解锁" | N≤10 niche · N=100+ 仍需突破 | ⏳ §00 摘要修 (II.4) |

### ⏳ 必修未修 (投学术 venue 前必修)

| 修订 | 优先级 | 内容 |
|---|---|---|
| §02 加 [Noh 2009] CQC 子领域 | P0-3 | 17 年 prior-art + PCC vs CQC disambig + 考虑改 PCC 名 |
| §03.2 P3 加 δ-extension | P0-4 | "is δ-parameterized extension of Lin-Lin 2015" |
| §03.5 子算子公式漏平方 | P0-5 | OR/AND/COUNT/T_t 4 公式 |
| §06.1 加 5th algebraic disambig | P1-1 | Fomin 2013 |
| §99 cite 精确化 | P1-2/3 | year + published + 7 模糊 entry |
| §05 D3 加 constructor theory | P1-4 | Violaris 2025 framing |
| §14 + §17 加 Salih caveat | P2-1 | thousands MZI 限制 |

---

## Part IX · 物理基础的元判断 (诚实最终评估)

### 物理基础是否牢固?

**是 · CFE 物理基础真实存在** · 5 条独立 evidence 支持:

1. ✅ 30+ 年文献链 · Elitzur-Vaidman 1993 → Kwiat 1995 → Mitchison-Jozsa 2001 → Salih 2013 → Calafell 2019 → Franco 2026 → Shwartz 2025
2. ✅ Multi-platform 实验 · bulk optics / NMR / nanophotonic / programmable UPP / cold atom / electron
3. ✅ 关键组件全成熟商用 · SPDC source / SNSPD detector / SOI waveguide / thermo-optic phase shifter / Quandela Ascella cloud
4. ✅ Multi-object IFM 已 lab demo (Franco N=5)
5. ✅ R1/R2/R3 性质都有物理 backing (chained Zeno + multi-object IFM 规模严格 quantum-only)

### 但有 critical caveat

⚠️ Frumkin-Bush 2023 (PRA 108:L060201) 在 hydrodynamic pilot-wave 系统 demonstrate 单 IFM 经典模拟。**R1/R2/R3 严格 "quantum-only" claim 是 contested in physics community**:

- 在 **single bomb tester** 规模:不严格 quantum-only · 经典 pilot-wave 可 reproduce 25% statistics
- 在 **chained Zeno + multi-object IFM** 规模:严格 quantum-only · 经典 pilot-wave 因 finite memory + finite spatial extent 无法 reproduce

### CFE 应用 niche 在哪个规模?

**全部在 chained / multi-object 规模**:

- §10 6 个 challenge problem · 全部假设 N≥2 oracle
- §14 / §17 worked example · 全部 chained MZI 实现
- §15 / §16 attack model · 全部用 R2 stealth (chained Zeno 才有 high efficiency)
- §17 12 simulator · 全部假设 multi-object IFM

**所以 CFE 应用论点 not affected by Frumkin-Bush 2023**。

### 跟 reviewer 的预期对话

**预期 reviewer 问 1**:"Frumkin-Bush 2023 challenge IFM quantum-only · 你们 R1/R2/R3 怎么 still stand?"

回答:见 §11.2 CAVEAT 6 · §03.7 caveat · single IFM 规模我们 honest acknowledge · 但应用 niche 在 chained / multi-object 规模 (Calafell 2019 chain N=6 已 demo · 经典系统不可 reproduce 因 nonlocal wavefunction 必需)。

**预期 reviewer 问 2**:"你们 N=12 但 Franco 2026 N=5 · 怎么解释?"

回答:N=12 是 platform mode 数 (hardware capability) · N=5 是 multi-object IFM 实测 object 数。两个不同维度 · §03.9 SOTA 表已精确化。

**预期 reviewer 问 3**:"PCC 跟 [Noh 2009] CQC 子领域冲突 · 改名?"

回答:P0-3 待修 · 加 CQC vs PCC disambiguation · 或改名为 CRC (Counterfactual-Resistant Cryptography) · 类比 Quantum-Resistant Cryptography。

**预期 reviewer 问 4**:"你们 cite 错了 Hance 2025 / Yang 2026 / Hance 2019 · 论文可信度?"

回答:全部已修 (commit ab8aba4) · 22 处全文替换 + §99 entries 完整 author 列表。审计本身 (audit/ + §18 + supplement 17) 是论文 contribution 一部分 · 透明化。

---

## Part X · 跟 dev-notes / claude-mem 知识库的关系

本文件作为 CFE 论文修订的**单点真理源** · 跟既有知识库的关系:

| 既有文档 | 跟本文件的关系 |
|---|---|
| `audit/00-master-plan.md` | 方法论 · 本文件是 audit 的 actionable output |
| `audit/04-audit-summary.md` | 整体 status · 本文件是 stat-to-action 翻译 |
| `audit/05-gap-report.md` | 24 个 Gap · 本文件 cover 修订侧 (action-side) |
| `audit/06-novelty-defense.md` | 11 NOVEL 防御 · 本文件加第 8 攻击预案 (Frumkin-Bush) |
| `audit/07-prior-art-corrections.md` | P0/P1/P2 修订清单 · 本文件加 P0-6/7/8/9 落地状态 |
| `audit/batch-5-B-physics-foundation-DEEP.md` | 物理实验 SOTA · 本文件 Part I.2 引用 |
| `audit/batch-11-physics-via-phd-thesis-and-critical-review.md` | PhD thesis + critical · 本文件 Part I.1 + III 引用 |
| `paper/thinking-in-cfe/18-audit-report.md` | 论文章节 · 本文件是其修订决策 backing |
| `dev-notes/004-014` | 探索期 · 本文件是 final 修订 decision |

---

## 版本

- 2026-06-20 v1 · 基于 batch-5 + batch-11 + 全 audit 累计 finding · user verbatim "CFE 理论本身以及对各学科挑战 · 需要作出怎样的调整"

---

## 附录 · 一目了然的修订对账表

| § | 论文 claim | 修订状态 | 优先级 |
|---|---|---|---|
| §00 摘要 | "提前 10-20 年解锁" | ⏳ 加 N≤10 niche caveat (II.4) | P1 |
| §02 prior-art | 30 年文献链 | ✅ +§02.7 PhD synthesis (III.1-4 · commit 9d83bb6) | ✅ |
| §02 prior-art | 漏 [Noh 2009] CQC | ⏳ 加 CQC 6 paper (IV.1) | P0 |
| §03.2 P3 | $B_\delta(f) = O(Q(f)^2/\delta)$ | ⏳ 加 δ-extension 说明 (I.5) | P0 |
| §03.5 子算子 | OR/AND/COUNT/T_t 公式 | ⏳ 修漏平方 (I.4) | P0 |
| §03.7 R1/R2/R3 | "经典都不行" | ✅ +Frumkin-Bush 2023 caveat (I.1 · commit 9d83bb6) | ✅ |
| §03.9 | "N=12 / 5 dB / >99%" | ✅ SOTA 表精确化 (I.2 · commit ab8aba4) | ✅ |
| §05.4 D3 | categorical 差异 | ⏳ +Violaris constructor theory (III.2) | P1 |
| §06.1 | 4 类 subtractive disambig | ⏳ 加 5th algebraic (VI.2) | P1 |
| §10 A2/A3/A4/A5 | 应用 niche | ✅ +N≤10 caveat (V.1-3 · commit ab8aba4) | ✅ |
| §11.2 | 5 CAVEAT | ✅ +CAVEAT 6 (III.1 · commit 9d83bb6) | ✅ |
| §14 / §17 | Salih 2013 | ⏳ 加 thousands MZI caveat (IV.4) | P2 |
| §15.5 | R2 mental shift | ✅ +violation bound formula (commit ab8aba4) | ✅ |
| §15.9 / §16.11 | PCC 命名 | ⏳ 加 CQC disambig + 考虑改名 (IV.1) | P0 |
| §99 | 全文 cite | ✅ 22 处替换 + 3 entry author 修正 + L1 section 加 6 entries (commit ab8aba4 + 9d83bb6) | 部分 ✅ |
| §99 | 7 模糊 cite + year 偏差 | ⏳ 精确化 (VII.1) | P1 |
| 全文 12 simulator README | SOTA caveat | ⏳ 批量加 (V.5) | P2 |

**已落地**:9 处 · **待修**:8 处 P0/P1 · 4 处 P2。

---

## 元层结论

**CFE 物理基础牢固 · 但论文 R1/R2/R3 严格 "quantum-only" claim 是 contested in physics community**。

修订后论文 still publishable · 但**必须 honest disclose** Frumkin-Bush 2023 critical paper + 5 个物理 over-claim 已修。

**core narrative still stand**:

> "CFE 算子是 quantum-only 能力 (chained / multi-object IFM 规模) · 用专用 photonic 硬件提前 10-20 年解锁 (N≤10 niche) · 独占 FT QC 永远到不了的 D3 interface domain · 启发减法计算范式 (SCP)。"

**待 8 处必修 + 4 处应修完成后 · 论文可投学术 venue (PRA / Found. Phys. / Q. Sci. Tech. / Nat. Comm. / IACR ePrint)**。
