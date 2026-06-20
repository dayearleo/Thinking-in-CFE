# 01 · Claim Registry · 230 条可审计声明

> 本文件 = 全部 audit claim 的单点真理源 · 进度追踪在这里
> 编号规范见 `00-master-plan.md` §2 · 类别 A-H 8 大类
> Status 初始全 `UNVERIFIED` · 走完 7 步流程后转 CONFIRMED/PARTIAL/GAP/REFUTED/NOVEL
> 每完成 10 个 claim · 更新顶部进度统计 + 提交一次 commit

---

## 进度统计 (最近一次更新:2026-06-20 sample batch 2 后)

```
Total:       230
UNVERIFIED:  219  (95.2%)
Audited:      11  ( 4.8%)
├─ CONFIRMED:   6   (E-001, E-002, E-003, E-013, E-027, E-028)
├─ PARTIAL:     2   (AUD-E-004, AUD-C15-001)
├─ GAP:         0
├─ REFUTED:     2   (AUD-E-014 [Hance 2025] · AUD-E-044 [Yang 2026] · **同模式 attribution 错误**)
└─ NOVEL:       1   (AUD-C06-002)
```

最后审计:AUD-E-044 · 下一个待审:推荐 AUD-E-005 (Kwiat 1995) → AUD-E-013 → E 类剩余 attribution batch

### sample batch 1 + 2 关键发现 (落 04-audit-summary.md 详)

1. **REFUTED [Hance 2025]**:论文多处引 `[Hance 2025]` 实际是 `[Franco-Camillini-Galvão 2026]` (arxiv 2604.04691) · 必须全文 replace 并修 §99
2. **REFUTED [Yang 2026]**:论文 4 处引 `[Yang 2026]` 实际是 `[Tang et al. 2026]` (arxiv 2602.18232 · 第 1 作者是 Lexiang Tang · Yang 是第 6 作者) — **同模式错误** · 多作者 cite 选错 cite key
3. **PARTIAL [Lin-Lin 2015]**:公式 $B_\delta(f) = O(Q(f)^2/\delta)$ 是对 Lin-Lin 原版 $B(f) = \Theta(Q(f)^2)$ 的 $\delta$ extension · 论文未明确说 · 必须修
4. **PARTIAL [PCC 命名]**:漏 [Noh 2009] CQC 子领域 17 年 prior-art · §02 必须加 + 考虑改 PCC 名
5. **NOVEL Subtractive Computation Paradigm**:命名 NOVEL · 但 §06.1 应加 "Subtraction-free complexity (Fomin 2013)" 第 5 类邻近 disambig
6. **CONFIRMED batch**:Mitchison-Jozsa 2001 · Wheeler 1978 · Elitzur-Vaidman 1993 · Filatov-Auzinsh 2024 · Farhi 2008 · Childs 2009 — 6 个 attribution 全部 verified · 但 Farhi/Childs 建议统一为多作者 cite

### 🚨 Meta-pattern 警告

2 个 REFUTED 错误 (Hance 2025 + Yang 2026) **同模式** — 都是**多作者 paper 选错 cite key**。

启示:audit 完成后必跑 **全 §99-references grep audit** · 对每个多作者 cite 核对第 1 作者是否真实匹配 cite key。预估全文有 ~20 个多作者 cite · 都要查。

加新 task to backlog · AUD-meta-001 · "全 §99 多作者 cite key audit"。

---

## 类别速查 + 优先级

| 类 | 含义 | 数量 | 优先级 | 备注 |
|---|---|---|---|---|
| A | 数学定义 | 25 | P0 | 论文根基 · 错就垮 |
| B | 物理可行性 | 20 | P0 | 硬件 SOTA 数字必须真 |
| C | 复杂度 | 30 | P0 | $B_\delta(f)$ 是核心声明 |
| D | Novelty | 15 | P1 | 撞名风险 · 必先查 |
| E | 历史归属 | 46 | P1 | 引用是否准 · 错伤可信度 |
| F | vs FT QC / Grover | 20 | P0 | 论文核心论点 |
| G | 应用 / 工业 | 40 | P2 | 市场声明 · 可有 caveat |
| H | 密码学具体声明 | 34 | P0 | 17 算法 audit · 错就被密码学界拒 |

P0=必审 · P1=高优 · P2=可降级。但按 M4 全查不抽样 · 都得审完。

---

## A · 数学定义类 (25 条)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-C00-001 | §00 摘要 | $\Phi^{CF}_f$ 算子是 Counterfactual Function Evaluation Operator · 把 Elitzur-Vaidman + Mitchison-Jozsa 抽象为算法原语 | P0 | UNVERIFIED |
| AUD-C03-001 | §03.2 (L27-29) | P1 正确性 $\Pr[y=f(x)] \geq 1-\epsilon$ | P0 | UNVERIFIED |
| AUD-C03-002 | §03.2 (L31-33) | P2 反事实性 $\Pr[O_i\ \text{触发}] \leq \delta$ for $x_i=1$ | P0 | UNVERIFIED |
| AUD-C03-003 | §03.2 (L35-39) | P3 代价 $B_\delta(f) = O(Q(f)^2/\delta)$ · [Lin-Lin 2015] | P0 | UNVERIFIED |
| AUD-C03-004 | §03.3 (L48) | 工程取值 $\epsilon \sim 10^{-3}$, $\delta \in [10^{-2}, 10^{-6}]$ | P1 | UNVERIFIED |
| AUD-C03-005 | §03.4 (L54) | $\delta \to 0$ 极限 $B(f) \to \infty$ | P1 | UNVERIFIED |
| AUD-C03-006 | §03.4 (L55) | $\delta = 1$ 退化为 standard quantum query · $B(f) = Q(f)^2$ | P0 | UNVERIFIED |
| AUD-C03-007 | §03.4 (L56) | $N=2, f=$NOR 还原为 Elitzur-Vaidman bomb tester (1993 原版) | P0 | UNVERIFIED |
| AUD-C03-008 | §03.4 (L58) | $f=$NAND-tree 还原为 Farhi-Childs bomb 版 | P0 | UNVERIFIED |
| AUD-C03-009 | §03.5 (L66) | $\Phi^{CF}_{\text{OR}}$: $B = O(\sqrt{N}/\delta)$ | P0 | UNVERIFIED |
| AUD-C03-010 | §03.5 (L67) | $\Phi^{CF}_{\text{AND}}$: $B = O(\sqrt{N}/\delta)$ | P0 | UNVERIFIED |
| AUD-C03-011 | §03.5 (L69) | $\Phi^{CF}_{\text{MAJ}}$: $B = O(N/\delta)$ | P0 | UNVERIFIED |
| AUD-C03-012 | §03.5 (L70) | $\Phi^{CF}_{\text{COUNT}}$: $B = O(\sqrt{N \cdot \text{ans}}/\delta)$ | P0 | UNVERIFIED |
| AUD-C03-013 | §03.5 (L71) | $\Phi^{CF}_{\text{T}_t}$: $B = O(\sqrt{Nt}/\delta)$ | P0 | UNVERIFIED |
| AUD-C03-014 | §03.7 (L109) | 只有 $\Phi^{CF}_f$ 同时具备 R1+R2+R3 (核心 differentiator) | P0 | UNVERIFIED |
| AUD-C04-001 | §04.2 | 5 种组合 C1-C5 (串/并/嵌/条/迭) | P0 | UNVERIFIED |
| AUD-C04-002 | §04.3 (L78) | C1 串行 $\delta_\text{tot} \leq \delta_f + \delta_g$ | P0 | UNVERIFIED |
| AUD-C04-003 | §04.3 (L85) | C2 并行 $\delta_\text{tot} = \max(\delta_f, \delta_g)$ | P0 | UNVERIFIED |
| AUD-C04-004 | §04.3 (L92) | C3 嵌套 $\delta_\text{tot} \leq \delta_f \cdot N_\text{deep} + \delta_g$ | P0 | UNVERIFIED |
| AUD-C04-005 | §04.3 (L99) | C4 条件 $\delta_\text{tot} \leq \delta_f + \max(\delta_g, \delta_h)$ | P0 | UNVERIFIED |
| AUD-C04-006 | §04.3 (L106) | C5 迭代 $\delta_\text{tot} \leq k \cdot \delta_f$ | P0 | UNVERIFIED |
| AUD-C04-007 | §04.3 (L113) | Cost theorem 是 "合理估计" 不是严格证明 (open Q1) | P1 | UNVERIFIED |
| AUD-C04-008 | §04.4 | 嵌套深度 100 → $\delta_\text{tot} = 10^{-1}$ 反事实性丢光 | P1 | UNVERIFIED |
| AUD-C04-009 | §04.7 | CFE 跟 indefinite causal order (ICO) 是正交方向 | P2 | UNVERIFIED |
| AUD-C06-001 | §06 | 减法计算范式 (SCP) 是新提出 | P0 | UNVERIFIED |

## B · 物理可行性类 (20 条)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-C03-015 | §03.9 (L134) | N=12 universal photonic processor lab proven | P0 | UNVERIFIED |
| AUD-C03-016 | §03.9 (L134) | 端到端 5 dB loss · counterfactual efficiency 单链路 > 99% | P0 | UNVERIFIED |
| AUD-C03-017 | §03.9 (L132) | Quantum Zeno effect + chained interferometer 提升反事实效率 | P0 | UNVERIFIED |
| AUD-C03-018 | §03.9 | EAM (电吸收调制器) 作为 obstacle 物理实现 | P1 | UNVERIFIED |
| AUD-C03-019 | §03.9 | SNSPD 阵列单光子探测 cryogenic | P1 | UNVERIFIED |
| AUD-C03-020 | §03.9 | Heralded SPDC / III-V QD 单光子源 | P1 | UNVERIFIED |
| AUD-C05-001 | §05.3 | FT QC 实现 $\Phi^{CF}_f$ 需 $\sim 10^3 N$ 物理 qubit | P0 | UNVERIFIED |
| AUD-C05-002 | §05.3 | FT QC 错误率 $10^{-3} \to 10^{-15}$ 需 $\sim 10^5$ 表面码循环 | P0 | UNVERIFIED |
| AUD-C05-003 | §05.3 | CFE 专用 photonic 单芯片 $50k-$150k 成本 | P1 | UNVERIFIED |
| AUD-C05-004 | §05.3 | CFE 比 FT QC 同 capability 成本便宜 $\sim 6$ 个数量级 | P0 | UNVERIFIED |
| AUD-C05-005 | §05.3 | 光学 4f Fourier 是历史类比 (60s-70s) | P1 | UNVERIFIED |
| AUD-S03-001 | suppl §16 UHT | 7 种 device (HSM/TPM/wallet/EMV/passport/ECU/satellite) 物理上共享 IFM-attack primitive | P0 | UNVERIFIED |
| AUD-C10-001 | §10 A2 | 单细胞物理上不能搬进 quantum register · FT QC 永远无法做这个 | P0 | UNVERIFIED |
| AUD-D003-001 | dev-notes/003 | AIM Photonics / LioniX / Imec MPW · 6 月流片周期 | P1 | UNVERIFIED |
| AUD-D003-002 | dev-notes/003 | N=4 桌面 demo $\sim$$300k · 6 月内可搭 | P1 | UNVERIFIED |
| AUD-D003-003 | dev-notes/003 | N=8-12 on chip $\sim$$1M · 18 月可发顶刊 | P1 | UNVERIFIED |
| AUD-D003-004 | dev-notes/003 | rare-earth doped crystal 存 1.9 ms 集成波导 | P2 | UNVERIFIED |
| AUD-D003-005 | dev-notes/003 | EIT in Pr:YSO 晶体 1 秒级存储 | P2 | UNVERIFIED |
| AUD-D003-006 | dev-notes/003 | telecom band (1550nm) IFM 效率 10-30% retrieval | P2 | UNVERIFIED |
| AUD-D003-007 | dev-notes/003 | undetected photons imaging 已商业化 (QuantIC consortium) | P1 | UNVERIFIED |

## C · 复杂度类 (30 条)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-C07-001 | §07.1 | 引入 D2 disturbance complexity $D_\Delta(f) = \delta$ (新定义) | P0 | UNVERIFIED |
| AUD-C07-002 | §07.1 | 引入 D3 adversary observability complexity $\eta(f)$ (新定义) | P0 | UNVERIFIED |
| AUD-C07-003 | §07.1 | 引入 D4 hardware cost $\mathcal{H}(f)$ (新定义) | P1 | UNVERIFIED |
| AUD-C07-004 | §07.2 | bomb query 复杂度 $B_\delta(f) = O(Q(f)^2/\delta)$ [Lin-Lin 2015] | P0 | UNVERIFIED |
| AUD-C07-005 | §07.2 | CFE $\delta \to 0$ 时 $\eta \to 0$ (没纠缠产生) | P0 | UNVERIFIED |
| AUD-C07-006 | §07.3 | Pareto:经典 OR/AND $D_1=N, D_2=1, D_3=1$ | P1 | UNVERIFIED |
| AUD-C07-007 | §07.3 | Pareto:Grover $D_1=\sqrt{N}, D_2=D_3=1$ · D4 high | P1 | UNVERIFIED |
| AUD-C07-008 | §07.3 | Pareto:CFE $D_1=Q(f)^2/\delta, D_2=\delta, D_3 \sim \delta^N$ | P0 | UNVERIFIED |
| AUD-C07-009 | §07.4 | CFE 严格优于经典 · 当 oracle 有副作用时 | P0 | UNVERIFIED |
| AUD-C07-010 | §07.4 | CFE 严格优于 Grover · 在 D2/D3 维度 | P0 | UNVERIFIED |
| AUD-C07-011 | §07.4 | classical 严格优于 CFE · 当 sparsity 不成立 | P1 | UNVERIFIED |
| AUD-C07-012 | §07.5 | C1 串行 D1 加性 $B_f + B_g$ · D2 加性 $\delta_f + \delta_g$ | P0 | UNVERIFIED |
| AUD-C07-013 | §07.5 | C3 嵌套 D1 乘性 $B_f \cdot B_g$ (指数膨胀) | P0 | UNVERIFIED |
| AUD-C07-014 | §07.5 | C5 迭代 D2/D3 线性 $k \cdot \delta_f$ | P0 | UNVERIFIED |
| AUD-C07-015 | §07.7 | CFE 定义新复杂度类 CFP (Counterfactual Function class) | P1 | UNVERIFIED |
| AUD-C08-001 | §08 模板 1 | CPA: classical N → CFE K (K ≪ N) speedup | P0 | UNVERIFIED |
| AUD-C08-002 | §08 模板 2 | CBB Branch & Bound: 反事实 prune 不可行分支 | P0 | UNVERIFIED |
| AUD-C08-003 | §08 模板 3 | CAL Active Learning: 反事实预筛 candidate | P0 | UNVERIFIED |
| AUD-C08-004 | §08 模板 4 | CV Verification: 反事实验签名不消耗 token | P0 | UNVERIFIED |
| AUD-C08-005 | §08 模板 5 | CA* A* Search: 反事实 lookahead 不付路径代价 | P0 | UNVERIFIED |
| AUD-C08-006 | §08 模板 6 | CGTS MCTS: rollout 不触发对手反应 | P0 | UNVERIFIED |
| AUD-C10-002 | §10 A1 NAND-tree | 经典 $\Omega(N^{0.753})$ · FT QC $\sqrt{N}$ · CFE $O(\sqrt{N}/\delta)$ | P0 | UNVERIFIED |
| AUD-C10-003 | §10 A1 | Farhi 2008 NAND-tree 算法 + Childs 2009 离散版本 | P1 | UNVERIFIED |
| AUD-C14-001 | §14.3 NAND | CFE NAND-tree 速度跟 FT QC standard query 同阶 ($\sqrt{N}$) | P0 | UNVERIFIED |
| AUD-S14-001 | suppl 14 Bloom | CFE Bloom Filter 经典 Bloom 1970 FPR 公式跟实测 ±2x | P0 | UNVERIFIED |
| AUD-S14-002 | suppl 14 | CFE Bloom 9 unit test 全 pass | P0 | UNVERIFIED |
| AUD-S20-001 | suppl 20 differential | CFE 差分密码分析 8-round Feistel 16-bit key 真跑通 | P0 | UNVERIFIED |
| AUD-S22-001 | suppl 22 federated | CFE Federated 3 mode accuracy 完全一致 (~86%) | P0 | UNVERIFIED |
| AUD-S24-001 | suppl 24 MC | CFE Monte Carlo 30x expensive eval reduction · CFE 估 interesting region (有 caveat) | P1 | UNVERIFIED |
| AUD-S32-001 | suppl 32 SpMV | CFE SpMV bit-identical 输出 vs classical | P0 | UNVERIFIED |

## D · Novelty 类 (15 条)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-C06-002 | §06 | Subtractive Computation Paradigm (SCP) 是我们提出的新范式 | P0 | **NOVEL** ⭐⭐⭐⭐ (5th 邻近 Fomin 2013 algebraic 待加 disambig) |
| AUD-C06-003 | §06.1 | "subtractive" 跟 LLM reasoning / 心理学 / ML explainability / 因果推断 4 类用法 disambiguate | P0 | UNVERIFIED |
| AUD-C06-004 | §06 | 米开朗基罗 "see the angel in the marble" 哲学定位 | P2 | UNVERIFIED |
| AUD-C07-016 | §07 | 我们引入 D2/D3/D4 三个新复杂度维度 (主张此前没人系统定义) | P0 | UNVERIFIED |
| AUD-C15-001 | §15.9 | Post-Counterfactual Cryptography (PCC) 是我们提出的新子领域 | P0 | **PARTIAL** ⭐⭐⭐ (命名 NOVEL 但漏 [Noh 2009] CQC 子领域 17 年 prior-art) |
| AUD-C17-001 | §17 | CFE 同构方法论 5 步发现 SOP 是新提出 | P0 | UNVERIFIED |
| AUD-C17-002 | §17.6 | L0-L3 4 级硬件特化 (通用 photonic → ASIC) 类比 | P1 | UNVERIFIED |
| AUD-C17-003 | §17.7 | CFE 算子家族目录 vision · 类比 LLVM IR / qiskit | P1 | UNVERIFIED |
| AUD-S01-001 | suppl 01 PCC | PCC 子领域 4 项核心研究方向 (R1-R4) | P0 | UNVERIFIED |
| AUD-S11-001 | suppl 11 catalog | CFE 同构提交模板 (10 sections + 5-step process) 新提出 | P1 | UNVERIFIED |
| AUD-D007-001 | dev-notes/007 | "Subtractive Computation" 命名提出 + 跟 4 类邻近术语 disambiguate | P0 | UNVERIFIED |
| AUD-D008-001 | dev-notes/008 | 6 算法模板 (CPA/CBB/CAL/CV/CA*/CGTS) 是新命名 | P0 | UNVERIFIED |
| AUD-D009-001 | dev-notes/009 | 5 步问题代数化方法论 + 7 题决策树 + 5 反模式 是新提出 | P0 | UNVERIFIED |
| AUD-D013-001 | dev-notes/013 | CFE Differential Cryptanalysis Rate-Limit Bypass 是新攻击模型 | P0 | UNVERIFIED |
| AUD-C00-002 | §00 摘要 | "Quantum-only capability 用远小于 FT QC 代价提前 10-20 年解锁" 是核心论点 | P0 | UNVERIFIED |

## E · 历史归属类 (46 条 · attribution audit)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-E-001 | 多 | [Wheeler 1978] 延迟选择思想实验 | P1 | **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-E-002 | 多 | [Elitzur-Vaidman 1993] interaction-free measurement | P0 | **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-E-003 | 多 | [Mitchison-Jozsa 2001] counterfactual computation | P0 | **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-E-004 | 多 | [Lin-Lin 2015] bomb query complexity $B(f) = \Theta(Q(f)^2)$ | P0 | **PARTIAL** ⭐⭐⭐⭐ |
| AUD-E-005 | §02 | [Kwiat 1995] high-efficiency IFM | P1 | UNVERIFIED |
| AUD-E-006 | §02 | [Hosten 2006] experimental counterfactual computation (Nature 439) | P1 | UNVERIFIED |
| AUD-E-007 | §02 | [Vaidman 2008] past of a photon | P2 | UNVERIFIED |
| AUD-E-008 | §02 | [Salih 2013] direct counterfactual communication protocol | P1 | UNVERIFIED |
| AUD-E-009 | §02 | [Kong 2015] experimental Wheeler delayed choice in NMR | P2 | UNVERIFIED |
| AUD-E-010 | §02 | [Hance 2019] trace-free counterfactual communication on nanophotonic | P1 | UNVERIFIED |
| AUD-E-011 | §02 | [Kang 2020] temporal Wheeler delayed-choice cold atomic memory | P1 | UNVERIFIED |
| AUD-E-012 | §02 | [Belovs 2019] adversary bound IFM-related | P1 | UNVERIFIED |
| AUD-E-013 | §02 | [Filatov-Auzinsh 2024] multi-object IFM | P0 | **CONFIRMED** ⭐⭐⭐⭐⭐ (Appl Phys B 130:121) |
| AUD-E-014 | §02 | [Hance 2025] universal integrated photonic processor multi-object IFM | P0 | **REFUTED** ⭐ (实际 [Franco-Camillini-Galvão 2026] arxiv 2604.04691) |
| AUD-E-015 | §02 | [Shwartz 2025] high-efficiency counterfactual on photonic chip | P1 | UNVERIFIED |
| AUD-E-016 | §02 | [QIUP 2025] 集成芯片 IFM 最新工作 | P1 | UNVERIFIED |
| AUD-E-017 | §02 | [Lord 2024] relating QTE to other notions (79 页) | P1 | UNVERIFIED |
| AUD-E-018 | §02 | [Goyal-Raizes 2025] proofs of no intrusion | P1 | UNVERIFIED |
| AUD-E-019 | §02 | [Gottesman 2002] quantum tamper detection | P1 | UNVERIFIED |
| AUD-E-020 | §02 | [Gottesman 2003] quantum tamper-evident encryption | P1 | UNVERIFIED |
| AUD-E-021 | §02 | [Wiesner 1969] quantum money / coding | P1 | UNVERIFIED |
| AUD-E-022 | §02 | [Roese 1993] counterfactual thinking psychology | P2 | UNVERIFIED |
| AUD-E-023 | §02 | [Dunning 1989] norm theory counterfactual | P2 | UNVERIFIED |
| AUD-E-024 | §02 | [Wachter 2017] counterfactual explanations GDPR | P2 | UNVERIFIED |
| AUD-E-025 | §02 | [Mothilal 2020] counterfactual explanations for ML | P2 | UNVERIFIED |
| AUD-E-026 | §02 | [Pearl 2009] causal counterfactuals | P2 | UNVERIFIED |
| AUD-E-027 | §03 | [Farhi 2008] NAND-tree quantum walk algorithm | P0 | **CONFIRMED** ⭐⭐⭐⭐⭐ (建议统一为 3-author cite) |
| AUD-E-028 | §03 | [Childs 2009] discrete NAND-tree algorithm | P0 | **CONFIRMED** ⭐⭐⭐⭐⭐ (建议统一为 4-author cite) |
| AUD-E-029 | §06 | [Bennett 1973] reversible computation | P2 | UNVERIFIED |
| AUD-E-030 | §06 | [Bell 1964] Bell inequality | P2 | UNVERIFIED |
| AUD-E-031 | §06 | [EPR 1935] EPR paradox | P2 | UNVERIFIED |
| AUD-E-032 | §09 | [Dean-Ghemawat 2004] MapReduce | P2 | UNVERIFIED |
| AUD-E-033 | §09 | [Evans 2003] abstract interpretation | P2 | UNVERIFIED |
| AUD-E-034 | §09 | [Miner-Shook 2012] (待确认引用主题) | P2 | UNVERIFIED |
| AUD-E-035 | §14 | [Farhi-Goldstone-Gutmann 2008] (跟 [Farhi 2008] 是否同一) | P1 | UNVERIFIED |
| AUD-E-036 | §14 | [Childs-Cleve-Jordan-Yonge-Mallo 2009] (跟 [Childs 2009] 是否同一) | P1 | UNVERIFIED |
| AUD-E-037 | §14 | [Lloyd 2008] (待确认引用主题) | P2 | UNVERIFIED |
| AUD-E-038 | §17 | [Belovs 2012] span program algorithm | P1 | UNVERIFIED |
| AUD-E-039 | §17 | [Childs 2003] quantum walk | P1 | UNVERIFIED |
| AUD-E-040 | §17 | [Hosseini 2016] (待确认引用主题) | P2 | UNVERIFIED |
| AUD-E-041 | §17 | [Kaplan 2016] (待确认引用主题) | P2 | UNVERIFIED |
| AUD-E-042 | §17 | [Montanaro 2015] quantum algorithms survey | P1 | UNVERIFIED |
| AUD-E-043 | §17 | [Schuld 2019] quantum machine learning | P2 | UNVERIFIED |
| AUD-E-044 | §01 | [Yang 2026] (跟我们工作时间最近的同领域工作 · 必查) | P0 | **REFUTED** ⭐ (实际 [Tang et al. 2026] · 第 1 作者错 · arxiv 2602.18232) |
| AUD-E-045 | §99 | [Mitchison-Jozsa 2006] (跟 [Mitchison-Jozsa 2001] 是同一组后续工作?) | P1 | UNVERIFIED |
| AUD-E-046 | §99 | [Reichardt 2010] read-once formula evaluation quantum | P1 | UNVERIFIED |

## F · vs FT QC / Grover 比较类 (20 条)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-C05-006 | §05.2 | D1 capability:FT QC 是 CFE 超集 (能算 CFE 能算的 + unitary) | P0 | UNVERIFIED |
| AUD-C05-007 | §05.2 | D1 隐藏子维度:CFE $\delta\to 0$ adversary 不可见;FT QC 仍可见 | P0 | UNVERIFIED |
| AUD-C05-008 | §05.3 | D2 cost:CFE 比 FT QC 便宜 $\sim 6$ 数量级 (单 capability) | P0 | UNVERIFIED |
| AUD-C05-009 | §05.4 | D3 interface domain:CFE 永久独占外部物理 oracle | P0 | UNVERIFIED |
| AUD-C05-010 | §05.4 | D3 是 categorical 差异 (类比 CPU vs sensor) | P0 | UNVERIFIED |
| AUD-C05-011 | §05.4 | FT QC 永远只能 oracle = quantum circuit · 内部抽象 | P0 | UNVERIFIED |
| AUD-C05-012 | §05.4 | CFE oracle = 任何 photon 物理耦合的真实物体 | P0 | UNVERIFIED |
| AUD-C05-013 | §05 | "我们不超越 FT QC capability" honest 声明 | P1 | UNVERIFIED |
| AUD-C03-021 | §03.7 | CFE vs Grover:Grover $\sqrt{N}$ · CFE $\sqrt{N}/\delta$ (有 $\delta$ 代价) | P0 | UNVERIFIED |
| AUD-C03-022 | §03.7 | Grover/经典 R1=R2=R3=❌ · 只有 CFE 同时具备 | P0 | UNVERIFIED |
| AUD-C03-023 | §03.7 | Grover oracle 跟主系统纠缠 · 可见 | P0 | UNVERIFIED |
| AUD-C10-004 | §10 A2 | "FT QC 永远不可达单细胞 multi-assay" (D3 论证) | P0 | UNVERIFIED |
| AUD-C10-005 | §10 A4 | "FT QC 不含 adversary-undetectable 能力" | P0 | UNVERIFIED |
| AUD-C14-002 | §14.2 | A1 NAND-tree = 时间短路 (CFE 直接物理化 · FT QC 需等) | P0 | UNVERIFIED |
| AUD-C14-003 | §14.3 | A2 单细胞 = 替代路径 (FT QC 永远不可达) | P0 | UNVERIFIED |
| AUD-C14-004 | §14.4 | A4 Stealth probe = 新能力解锁 (FT QC 不含) | P0 | UNVERIFIED |
| AUD-C14-005 | §14.6 | "工程问题 vs 未解决物理" 元层论证 (CFE 工程化全工程问题) | P0 | UNVERIFIED |
| AUD-C14-006 | §14.7 | 4 类预防 reviewer 反对 (N≤32 / $D_1$ 慢 / 重复性 / 等 FT QC) | P1 | UNVERIFIED |
| AUD-C11-001 | §11 | CFE 不能取代 FT QC 在 Shor / Grover 已 cover 区域 | P0 | UNVERIFIED |
| AUD-C11-002 | §11 | CFE 实际是 photonic IFM 专用 ASIC · 不是通用 QC | P1 | UNVERIFIED |

## G · 应用 / 工业类 (40 条)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-C10-006 | §10 A1 | NAND-tree:lab 完全可行 · 没人 photonic 实现过 | P0 | UNVERIFIED |
| AUD-C10-007 | §10 A2 | 单细胞 multi-assay:部分有公司在做 (QuantIC) | P1 | UNVERIFIED |
| AUD-C10-008 | §10 A3 | 光毒性显微 + 分类:商业雏形 (QuantIC / Quantum Optical Systems) | P1 | UNVERIFIED |
| AUD-C10-009 | §10 A4 | 物理 stealth probing:军/情报 niche · 极开放 | P1 | UNVERIFIED |
| AUD-C10-010 | §10 A5 | 半导体 wafer in-line 检测:大 niche · 开放 | P1 | UNVERIFIED |
| AUD-C10-011 | §10 A6 | 稀有资源勘探 (核素/稀土):lab proven · 商用化中 | P1 | UNVERIFIED |
| AUD-S10-001 | suppl 10 HSM | 7 unit test pass + 1000 trial 96.10% CFE 成功率 | P0 | UNVERIFIED |
| AUD-S10-002 | suppl 10 | classical 0% · CFE ~99% · detection 0% (HSM 攻击) | P0 | UNVERIFIED |
| AUD-S14-003 | suppl 14 Bloom | classical 100% detection · CFE 0% (per query) | P0 | UNVERIFIED |
| AUD-S14-004 | suppl 14 | 跟 SealPIR / FHE-PIR / Chor 1995 multi-server PIR 4 维对比 | P0 | UNVERIFIED |
| AUD-S16-001 | suppl 16 UHT | 7 device 共 700 attack · classical 0% / CFE 82% avg | P0 | UNVERIFIED |
| AUD-S16-002 | suppl 16 | 受影响:HSM (千万级) / TPM (~30 亿 PC) / 加密货币 / EMV (10 亿 card) / passport (15 亿) / ECU (1 亿) / satellite | P0 | UNVERIFIED |
| AUD-S18-001 | suppl 18 reach | Graph reachability 490x detection reduction | P1 | UNVERIFIED |
| AUD-S20-002 | suppl 20 diff | classical 250/2000 锁卡 · CFE 2000/2000 完成 | P1 | UNVERIFIED |
| AUD-S22-002 | suppl 22 fed | 3 mode accuracy 完全一致 (86.00%) · CFE 0 物理 leak | P0 | UNVERIFIED |
| AUD-S24-002 | suppl 24 MC | 30x expensive eval reduction · materials science niche | P1 | UNVERIFIED |
| AUD-S26-001 | suppl 26 AI | SMT cost saving cloud Z3-as-a-Service · 99%+ cost reduction | P1 | UNVERIFIED |
| AUD-S28-001 | suppl 28 attn | 100M token context · CFE sparse attention | P1 | UNVERIFIED |
| AUD-S30-001 | suppl 30 RT | 8K HDR real-time rendering · CFE bbox 预筛 | P1 | UNVERIFIED |
| AUD-S32-002 | suppl 32 SpMV | 3 billion bp genome 比对 · photonic in-mesh 突破 memory wall | P1 | UNVERIFIED |
| AUD-S34-001 | suppl 34 SW | cancer genomics whole-genome SW · CFE k-mer 预筛 | P1 | UNVERIFIED |
| AUD-S13-001 | suppl 13 extended | 5 个跨域 worked example 全部填模板格式 (无 simulator) | P1 | UNVERIFIED |
| AUD-D004-001 | dev-notes/004 | 4 个 IFM/counterfactual 真存在工作:Ardehali 1995 / UIUC 2003 / Bristol 2013 / Yu 2020 | P0 | UNVERIFIED |
| AUD-D005-001 | dev-notes/005 | NTT / Hitachi / QC Ware Coherent Ising Machine (CIM) 在卖 | P1 | UNVERIFIED |
| AUD-D005-002 | dev-notes/005 | Lightmatter / Lightelligence / Luminous 卖 MZI mesh 神经网络 | P1 | UNVERIFIED |
| AUD-D011-001 | dev-notes/011 | Bloom Filter → CFE PIR 同构方法 | P1 | UNVERIFIED |
| AUD-D012-001 | dev-notes/012 | Graph 可达性 → CFE Stealth Probe 同构 | P1 | UNVERIFIED |
| AUD-D014-001 | dev-notes/014 | Backprop → CFE Federated 不损 accuracy | P0 | UNVERIFIED |
| AUD-C10-012 | §10 排除 | Shor 不可挑战 · 是 unitary-heavy 非 query 模型 | P0 | UNVERIFIED |
| AUD-C10-013 | §10 排除 | 大规模量子化学模拟 不可挑战 | P0 | UNVERIFIED |
| AUD-C10-014 | §10 排除 | HHL 量子线性代数 不可挑战 | P0 | UNVERIFIED |
| AUD-C10-015 | §10 排除 | QML 训练 不可挑战 | P0 | UNVERIFIED |
| AUD-C10-016 | §10 排除 | Boson sampling 不可挑战 | P0 | UNVERIFIED |
| AUD-S07-001 | suppl 07 press | 新闻稿"30 年理论化身" 表述准 | P2 | UNVERIFIED |
| AUD-S04-001 | suppl 04 NIST | "NIST PQC standardization 加 PCC track" 提议合理性 | P1 | UNVERIFIED |
| AUD-S04-002 | suppl 04 | NIST 提交流程描述 (federal register / pqc-comments@nist.gov) | P1 | UNVERIFIED |
| AUD-S05-001 | suppl 05 IACR | IACR ePrint 投稿封面格式准 | P2 | UNVERIFIED |
| AUD-S02-001 | suppl 02 HSM | 90-day grace period · PGP · 不接 NDA · CVD 标准 | P1 | UNVERIFIED |
| AUD-S03-002 | suppl 03 specifics | Thales / Utimaco / Entrust / AWS CloudHSM 4 厂商特定段 | P1 | UNVERIFIED |
| AUD-S01-002 | suppl 01 PCC | PCC founding · 类比 PQC 接受过程 | P1 | UNVERIFIED |

## H · 密码学具体类 (34 条)

| ID | 来源 | claim 速述 | 优先级 | Status |
|---|---|---|---|---|
| AUD-C15-002 | §15.3 | 密码协议堆栈底 4 层完全依赖 "probe 可被检测" 物理假设 | P0 | UNVERIFIED |
| AUD-C15-003 | §15.4 | A · HSM tamper-bypass 攻击 (FIPS 140-3 Level 4) | P0 | UNVERIFIED |
| AUD-C15-004 | §15.4 | B · Canary / honey token stealth-trip 攻击 | P0 | UNVERIFIED |
| AUD-C15-005 | §15.4 | C · IAEA seal 反事实读取 攻击 | P0 | UNVERIFIED |
| AUD-C15-006 | §15.5 | 5 条 mental model 颠覆 (probe 必检测 → 不必 etc) | P0 | UNVERIFIED |
| AUD-C15-007 | §15.6 | Shor 打数学层 · CFE 打物理假设层 · 正交战线 | P0 | UNVERIFIED |
| AUD-C15-008 | §15.9 | PCC 加 quantum-aware adversary model (跟 standard quantum adv. 并列) | P0 | UNVERIFIED |
| AUD-C16-001 | §16.1 | "数学层 vs 工业部署层" 二分 · CFE 攻第二层不攻第一层 | P0 | UNVERIFIED |
| AUD-C16-002 | §16.2 | CFE 一定不破 RSA 数学 / AES 数学 / SHA 数学 (严格 disclaimer) | P0 | UNVERIFIED |
| AUD-C16-003 | §16.3 | 工业密码 "两道防线" 模型:数学算法 + 硬件根信任 | P0 | UNVERIFIED |
| AUD-C16-004 | §16.4 | CFE R1/R2/R3 独立击穿第二道防线 (3 attribute) | P0 | UNVERIFIED |
| AUD-C16-005 | §16.5 DES | 56-bit · HSM key 提取 + 短 key 暴力 → 完全破 | P0 | UNVERIFIED |
| AUD-C16-006 | §16.5 3DES | 112-168 bit · HSM key 流失 | P0 | UNVERIFIED |
| AUD-C16-007 | §16.5 IDEA | 128 bit · HSM key 流失 | P0 | UNVERIFIED |
| AUD-C16-008 | §16.5 RC5 | 可变 key · HSM 提取可行 | P1 | UNVERIFIED |
| AUD-C16-009 | §16.5 Blowfish | 32-448 bit · HSM key 流失 | P1 | UNVERIFIED |
| AUD-C16-010 | §16.5 AES | 128/192/256 · HSM key 流失 | P0 | UNVERIFIED |
| AUD-C16-011 | §16.5 ChaCha20 | 256 bit · HSM key 流失 | P0 | UNVERIFIED |
| AUD-C16-012 | §16.5 RC4 | 完全破 (WEP 40-bit + CFE 加 stealth) | P0 | UNVERIFIED |
| AUD-C16-013 | §16.5 MD5 | HMAC key 流失 + deprecated | P1 | UNVERIFIED |
| AUD-C16-014 | §16.5 SHA-1 | HMAC key R2 提取 + SHAttered deprecated | P0 | UNVERIFIED |
| AUD-C16-015 | §16.5 RSA | 2048+ · 私钥 R2 提取 · 数学未破 | P0 | UNVERIFIED |
| AUD-C16-016 | §16.5 DH | HSM 私钥流失 | P0 | UNVERIFIED |
| AUD-C16-017 | §16.5 EDH | 临时窗口流失风险 (生成-销毁) | P0 | UNVERIFIED |
| AUD-C16-018 | §16.5 ECC | HSM 私钥流失 | P0 | UNVERIFIED |
| AUD-C16-019 | §16.5 AES-GCM | HSM key 流失 | P0 | UNVERIFIED |
| AUD-C16-020 | §16.5 ChaCha20-Poly1305 | HSM key 流失 | P0 | UNVERIFIED |
| AUD-C16-021 | §16.6.1 | AES-256 in HSM 反事实提取 · detection ≤ 2.56e-7 | P0 | UNVERIFIED |
| AUD-C16-022 | §16.6.2 | 银行 PIN 反事实暴力破 · 10^4 query 不触发 attempt counter | P0 | UNVERIFIED |
| AUD-C16-023 | §16.6.3 | SHA-1 HMAC key 反事实提取 · 数学弱点立即可用 | P0 | UNVERIFIED |
| AUD-C16-024 | §16.7 | CFE-增强 HNDL · 现在提 HSM master key · 立即派 session key · 没有 post-quantum 路径救 | P0 | UNVERIFIED |
| AUD-C16-025 | §16.8 | 硬件根信任危机:HSM/TPM/Secure Enclave/TrustZone/SGX/wallet/smart card 同时失去 implicit guarantees | P0 | UNVERIFIED |
| AUD-C16-026 | §16.9 | 17 算法 audit 中 0/17 数学层被破 · 17/17 HSM 层被破 | P0 | UNVERIFIED |
| AUD-C16-027 | §16.11 | 给密码学社区 5-point ask (PCC standardization etc) | P1 | UNVERIFIED |

## 索引补丁 · 待审计 claim 补全机制

**M4 全查不抽样原则**:本 registry 第一版列 230 条 · 是基于已读 §03/§04 + 跨章节扫描的批量编号。审计过程中如发现遗漏 claim · 必走以下 SOP:

1. 在本表对应类目尾部追加新 ID (例 `AUD-C03-022`)
2. 更新顶部进度统计 Total 数字 (+1)
3. 提交 commit 标 "registry: 补漏 AUD-XXX"
4. 不算违反 M4 · 反而是 M4 自审反馈

**预留扩展容量**:每类预留 ~5 个编号位置 · 防 ID 不连续。

---

## 审计执行顺序建议 (P0 优先)

按依赖关系建议顺序:

1. **E 类 attribution** 先做 (~46 条) · 因为后续章节都依赖它们 · 而且最容易做 (查文献)
2. **A 类数学定义** (~25 条) · 整个论文根基
3. **C 类复杂度** (~30 条) · 跟 A 类强耦合
4. **B 类物理可行性** (~20 条) · 独立可做
5. **F 类 vs FT QC** (~20 条) · 依赖 A/B/C 已审完
6. **H 类密码学** (~34 条) · 17 算法可批量做 (用统一 H-template)
7. **D 类 Novelty** (~15 条) · 必须等 A/E 完成才能判断真 novel
8. **G 类应用** (~40 条) · 最后 · 多数是 caveat 类不影响核心论点

合计 ~230 条 · 跨 5-8 session 完成。

---

## 版本

- 2026-06-20 v1 · 初始化 · 230 claim 编号 · 全部 UNVERIFIED
