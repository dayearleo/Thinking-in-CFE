# 06 · Novelty Defense · 我们 NOVEL 部分的 prior-art 防御

> 状态:230 claim 全审完成 · 本文件防御 11 个 NOVEL claim 不被 reviewer 撞名抓
> 每个 NOVEL claim 含:声明 + EXA 搜索证据 + 邻近 disambig + 防御 narrative

---

## 11 个 NOVEL claim 防御

### NOVEL #1 · Subtractive Computation Paradigm (SCP)

**声明**:我们提出 "Subtractive Computation Paradigm" 作为新算法构造范式 · 跟传统 additive computation 正交。

**EXA 搜索证据** (2026-06-20 跑):

Query: `subtractive computation paradigm algorithm framework`
Top 8 hits 中 0 个对应我们的语义:

1. "Sublinear Computation Paradigm" Springer 2021 · **不同概念** (sublinear · 非 subtractive)
2. "Subtractive Design in Social Robotics" Irtolo · **不同领域** (设计哲学)
3. "Exact Computation Paradigm" Yap-Dubé · **不同概念** (numerical exact)
4. "subtraction operation in CVT-XOR" · **不同概念** (arithmetic)
5/6. "Subtractive Mixture Models" Loconte 2023 · **ML probabilistic** 跟我们正交
7. "Subtraction-free complexity" Fomin 2013 (arxiv 1307.8425) · **algebraic complexity 子领域** · 最近概念但不同
8. Wikipedia 算法范式定义 · 无 "subtractive" 主题

**邻近 disambig (5 类)**:

| 类 | 用法 | 跟 SCP 关系 |
|---|---|---|
| LLM reasoning ([Tang et al. 2026]) | "Thinking by Subtraction" contrastive decoding | 不同 · LLM token 概率减法 |
| 认知心理学 ([Roese 1993] / [Dunning 1989]) | counterfactual thinking psychology | 不同 · 人类反事实思维 |
| ML explainability ([Wachter 2017] / [Mothilal 2020]) | counterfactual explanations GDPR / ML | 不同 · 解释 ML 决策 |
| 因果推断 ([Pearl 2009]) | causal counterfactuals | 不同 · 因果 DAG do-calculus |
| 代数复杂度 ([Fomin 2013]) | subtraction-free complexity | 邻近 · 代数符号约束 · 跟我们正交 |

**防御 narrative**:

> "Subtractive Computation Paradigm (SCP)" 严格指代 **基于 CFE 算子的算法构造方式**:算法的输出由 "没发生的事件" 决定 · 而不是 "发生的事件"。
> 跟上面 5 类邻近用法不同:
> - LLM/心理学/ML/因果推断 都不涉及 quantum / IFM / 反事实物理
> - Fomin 2013 algebraic 是符号约束 · 不是 quantum 物理反事实
> SCP 是真正的 quantum-physical paradigm · NOVEL。

### NOVEL #2 · D2 disturbance complexity

**声明**:引入 $D_\Delta(f) = \delta$ 作为新复杂度维度 · CFE 算子触发率上界。

**EXA 搜索证据**:无人系统定义 "disturbance complexity" 在 query model 中。

**邻近**:bomb query complexity (Lin-Lin 2015) 是 $\delta \to 0$ 极限 · 我们 D2 是显式参数化。

**防御 narrative**:D2 是 Lin-Lin 2015 model 的自然扩展 · 引入 $\delta$ 作为 explicit parameter · 不是 redefining 现有概念。

### NOVEL #3 · D3 adversary observability complexity

**声明**:引入 $\eta(f)$ 作为新复杂度维度 · 对手能察觉查询发生的概率。

**EXA 搜索证据**:在 quantum query model 中没人系统定义。但相关概念:

- Quantum cryptography "leak detection" (Shor-Preskill 2000 BB84 security proof)
- Quantum side-channel attack literature

**邻近**:跟 QKD 中 Eve detection 概念邻近 · 但我们 D3 是 **algorithm-level** 不是 protocol-level。

**防御 narrative**:D3 是把 QKD 中 Eve-detection 概念抽象到 algorithm query model · NOVEL contribution 在于显式化。

### NOVEL #4 · D4 hardware cost complexity

**声明**:引入 $\mathcal{H}(f)$ 作为新复杂度维度 · 硬件代价。

**EXA 搜索证据**:在 algorithm theory 中没人系统定义 hardware cost 作为复杂度维度。

**邻近**:circuit complexity (gate count) · 但我们 D4 是 platform-specific (photonic vs superconducting) · 不是 universal gate count。

**防御 narrative**:D4 反映 photonic IFM 跟 FT QC 的硬件 cost 差异 (~10^6) · 是论文 D2 cost 论点的形式化。

### NOVEL #5 · CFP (Counterfactual Function class) 复杂度类

**声明**:CFP 跟 BQP 关系 open · 引入新复杂度类。

**EXA 搜索证据**:complexity zoo 没有 CFP entry。

**邻近**:BQP (bounded-error quantum polynomial time) · 我们 CFP 是 BQP 的子集 with R1/R2/R3 性质。

**防御 narrative**:跟 BQP / BPP / P 关系 (§07.7 + open Q9) · 待社区 follow up · vision 类提案。

### NOVEL #6 · CFE 同构方法论 5 步 SOP

**声明**:把任何 query-model 算法重铸为 CFE 同构 · 5 步 SOP (历史考古 → 抽离 primitive → 同构判定 → 复杂度对比 → 速度补偿评估)。

**EXA 搜索证据**:没人系统做过 "IFM-to-classical algorithm isomorphism methodology"。

**邻近**:quantum-classical algorithm correspondence (Schuld 2019) · 但我们方法论更具体 (含速度补偿 + 硬件特化评估)。

**防御 narrative**:类比 LLVM IR 让 frontend 跟 backend 解耦 · 我们方法论让算法学家不懂 quantum 物理也能 cast 自己问题为 CFE。

### NOVEL #7 · L0-L3 4 级硬件特化类比

**声明**:CFE 硬件实现 4 级:L0 通用 photonic · L1 specialized photonic · L2 ASIC · L3 vertically integrated。

**邻近**:GPU/TPU/ASIC 历史。

**防御 narrative**:类比合理 · 跟 ML 加速器历史一致。

### NOVEL #8 · CFE 算子家族目录 vision

**声明**:类比 LLVM IR / qiskit standard library · CFE 算子可成为社区共用 library。

**邻近**:qiskit / cirq / pennylane (quantum SDK)。

**防御 narrative**:vision · 等待社区 follow up · 跟 §13 RFC framework 一致。

### NOVEL #9 · CFE 同构提交模板

**声明**:supplement 11 给社区提交新 CFE 同构的标准模板 (10 sections + 5 步流程)。

**邻近**:LLVM RFC template / Python PEP template。

**防御 narrative**:类比 RFC 提交流程 · 工程实践 standard。

### NOVEL #10 · 6 算法模板命名 (CPA/CBB/CAL/CV/CA*/CGTS)

**声明**:把 6 个经典算法 family 重铸为 CFE 同构 · 命名:

- CPA: Counterfactual Pruning Algorithm
- CBB: Counterfactual Branch & Bound
- CAL: Counterfactual Active Learning
- CV: Counterfactual Verification
- CA*: Counterfactual A* Search
- CGTS: Counterfactual Game Tree Search

**邻近**:每个 algorithm family 都有大量 prior-art · 我们 NOVEL 在 "反事实重铸" 角度。

**防御 narrative**:不声称发明 algorithm family · 声称发明 "反事实变体" · 类比 quantum walk (Childs 2003) 是 random walk 的量子化。

### NOVEL #11 · CFE Differential Cryptanalysis Rate-Limit Bypass

**声明**:用 CFE R2 性质绕过 cloud cipher rate limit · 让短 key cipher 差分分析在 cloud deployment 真实可破。

**邻近**:Differential cryptanalysis (Biham-Shamir 1990) + rate-limit security · 我们 NOVEL 在 combine。

**防御 narrative**:新攻击 model · 跟 §16 17 算法 audit 一致 · 是 R2 性质的应用而非新基础密码学。

---

## 整体 novelty narrative

### 我们 **不** 声称发明的

- 不发明新物理 (Elitzur-Vaidman 1993 / Kwiat 1995 / Lin-Lin 2015 已有)
- 不发明新 algorithm family (CPA = Branch & Bound 反事实 · CV = signature verify 反事实 etc)
- 不发明新 cryptographic primitive (Gottesman 2003 tamper-evident encryption 已有)
- 不发明 photonic hardware (Quandela Ascella · Calafell 2019 nanophotonic processor 已有)
- 不发明 quantum query model (Beals 2001 / Reichardt 2010 / Lin-Lin 2015 已有)

### 我们声称发明的 (11 个)

1. **Subtractive Computation Paradigm** 命名 + 哲学定位
2. **D2/D3/D4** 复杂度新维度
3. **CFP** 复杂度类
4. **CFE 同构方法论** 5 步 SOP
5. **L0-L3** 硬件特化框架
6. **CFE 算子家族目录** vision
7. **CFE 同构提交模板**
8. **6 算法模板命名** (CPA/CBB/CAL/CV/CA*/CGTS)
9. **5 步问题代数化方法论**
10. **CFE Differential Rate-Limit Bypass** 攻击模型
11. **PCC (Post-Counterfactual Cryptography)** 子领域提议 (但漏 CQC 17 年 prior-art · 待 disambig)

### 整体定位

我们是 **MapReduce 之于分布式计算的 abstraction work** · 不是发明新基础物理。

> 把 30 余年分散的 IFM/counterfactual computation 文献系统化为 **算法学家可调用的工具集** · 让领域专家不必懂量子光学就能使用。

---

## 反 reviewer 攻击预案

### 攻击 1 · "你们 cite 错 Hance 2025"

- 回应:已修 · 实际是 Franco-Camillini-Galvão 2026 · §99 entry 完整 author 列表 + 完整 affiliation
- 致谢 reviewer · 加 acknowledgment

### 攻击 2 · "Subtractive Computation 不是新词 · Loconte 2023 已用"

- 回应:Loconte 2023 是 ML probabilistic mixture models · 跟我们 quantum-physical 反事实计算 paradigm 完全正交
- §06.1 已加 4 类邻近 disambig · 5th algebraic (Fomin 2013) 修订中加
- "Subtractive Computation Paradigm" 全称限定语义

### 攻击 3 · "你们说 N=12 但 Franco 2026 只 N=5"

- 回应:已修 § 03.9 · N=12 是 platform mode 数 · IFM object 数 SOTA N=5
- §11.2 加 5 CAVEAT
- §10 A2/A3/A4 加 SOTA caveat

### 攻击 4 · "R2 adversary undetectable 不是 0 · Calafell 2019 实测 2.4%"

- 回应:已修 §15.5 · R2 带 violation bound 公式 + 4 scenario 实际威胁评估
- 论点改为 "bounded adversary observability" 不是 "absolute zero"

### 攻击 5 · "PCC 命名跟 CQC (Noh 2009) 冲突"

- 回应:待修订 (07-prior-art-corrections P0)
- §02 加 CQC 子领域 6+ paper · §15.9 加 CQC vs PCC disambig
- 考虑改名:CRC (Counterfactual-Resistant Cryptography) 候选

### 攻击 6 · "12 simulator 都是 classical simulation · 没硬件"

- 回应:正确 · simulator 模拟 R1/R2/R3 性质 · 用于 narrative 验证
- §13 RFC framework 已 anticipate · supplement 11 catalog 邀请社区贡献硬件 PoC
- 类比:经典算法 paper 也常用 simulator · 实现是后续工作

### 攻击 7 · "δ-extension of Lin-Lin 2015 没明确说"

- 回应:已发现 (AUD-E-004) · 待 §03.2 P3 修订加 explicit extension 说明

---

## 版本

- 2026-06-20 v1 · 230 claim 全审后整理
