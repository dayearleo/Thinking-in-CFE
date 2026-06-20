# 06 · 减法计算范式 · Subtractive Computation Paradigm

[← 返回 README](README.md)

## 6.1 · 严肃的术语免责 (放在最前面)

"Subtractive computation" / "subtractive reasoning" / "thinking by subtraction" 在以下三个相邻领域有**完全不同**的预设含义:

- **认知心理学** [Roese 1993], [Dunning 1989]:研究人类反事实思维 ("如果当初没做...")
- **机器学习 explainability** [Wachter 2017], [Mothilal 2020]:counterfactual explanations 解释模型决策
- **LLM 推理** [Yang 2026, arxiv 2602.18232]:contrastive decoding 用减法 token 概率

本论文提出 **Subtractive Computation Paradigm (SCP)** 时使用**全称** · 严格指代:

> **基于 CFE 算子 (§3) · 把算法输出由 "没物理触发的事件" 决定的算法构造哲学**

读者**不应**将其混同上述任一概念。论文内部为简洁会写 "减法范式" 或 "subtractive paradigm" · 全部指代上述定义。

## 6.2 · 哲学定位 · 米开朗基罗的雕塑

米开朗基罗对自己的雕塑说过一段流传的话:

> I saw the angel in the marble and carved until I set him free.
> (我看见天使藏在大理石里 · 我雕刻 · 直到把他释放出来。)

这是 **subtractive sculpture** (减法雕塑) 的哲学:**艺术家不是在添加什么 · 是在移除多余的部分 · 让作品显形**。

跟之相对的是 **additive sculpture** · 比如黏土塑形 / 3D 打印 · 一点点添加材料构建作品。

**减法计算范式** 提议:

> 算法的真正力量 · 不在它执行了什么 · 而在它**没执行**什么。
> 答案不是 build 出来的 · 是从所有可能 state 里 carve 出来的。
> 大部分计算 "would have happened" 但物理上没真发生 —— 这就是 counterfactual。

## 6.3 · 传统范式 · 加法计算 (Additive Computation)

为对比 · 先精确化传统范式的特征:

| 维度 | 加法范式特征 |
|---|---|
| 核心隐喻 | building / accumulating · 添加 / 累积 |
| 算法学家关注什么 | what TO DO at each step |
| state 演化 | input 通过 operations 逐步加工到 output |
| state 起点 | 单个 initial state |
| 输出位置 | 最终 state |
| 失败处理 | retry / backtracking · 都有成本 |
| 主要 cost driver | operation 次数 |
| 不可见操作的语义 | 没意义 (没做就是没做) |
| 代表算法 | 经典并行 / Grover / 标准 quantum query / 大部分主流算法 |

## 6.4 · 新范式 · 减法计算 (Subtractive Computation)

| 维度 | 减法范式特征 |
|---|---|
| 核心隐喻 | sculpting / pruning · 雕塑 / 剪枝 |
| 算法学家关注什么 | what NOT TO DO · 让 "no-trigger" 自然形成 answer |
| state 演化 | 所有可能 state 在 superposition 并存 · counterfactual probes 筛掉不要的 |
| state 起点 | 所有可能 state 同时存在 |
| 输出位置 | surviving state |
| 失败处理 | "failure" 物理上不发生 · 没有重试代价 |
| 主要 cost driver | surviving 项数 (不是总尝试次数) |
| 不可见操作的语义 | 是核心 (counterfactual 评估的灵魂) |
| 代表算法 | §8 的 6 个模板 (CPA / CBB / CAL / CV / CA* / CGTS) |

## 6.5 · 关键对比表

| 维度 | 加法计算 | 减法计算 |
|---|---|---|
| 隐喻 | 建造 / 累积 | 雕塑 / 剪枝 |
| 算法学家关注 | what TO DO | what NOT TO DO |
| state 起点 | 单个 initial | 所有可能并存 |
| 演化方式 | 逐步 transform | 筛除不符合的 |
| 答案位置 | 最终 state | 幸存 state |
| 失败成本 | 高 (要重做) | 0 (没真做) |
| 主要 cost driver | 操作次数 | 幸存项数 |
| 不可见操作 | 没意义 | 是核心 |
| 适合问题 | 多数 (default) | 稀疏 + 副作用 + verify-without-commit |

## 6.6 · 减法范式的杀手锏问题类

减法范式特别适合 3 类问题:

### 类 K1 · 几乎所有候选都该被淘汰 (Sparsity)

- 例:$10^9$ 分子里找一个 binding affinity > threshold 的
- 加法成本:测 $10^9$ 次
- 减法成本:并行反事实测全部 · 真测的只有少数 hit · $\sim O(K)$ where $K \ll N$

### 类 K2 · 评估有不可逆副作用 (Side Effects)

- 例:测试是否能 jailbreak 某 system · 测试本身可能触发 alert / 启动防御
- 加法成本:每次测都暴露 · 测 N 次暴露 N 次
- 减法成本:反事实测 · 大部分物理上没发生 · 不留痕

### 类 K3 · 需要 verify 但不想 commit (Verify-without-commit)

- 例:加密 token 是否有效 · 但用了就 burn
- 加法成本:用了才知道 · 没用没法知
- 减法成本:反事实验证 · 知道有效性但不消耗

### 3 类的共性

都涉及 **queries 有物理代价** · 而不是 query 本身复杂度高。减法范式的核心是把"查询代价"重新定义为"实际发生的查询代价" · 而不是"所有尝试查询的代价"。

## 6.7 · 跟其他非传统范式的关系

减法范式不是孤立提出 · 跟若干已有范式有亲缘:

| 范式 | 跟减法计算的关系 |
|---|---|
| **Probabilistic computing** (Monte Carlo / SAT) | 都接受随机性 · 但概率算法仍是加法 (每个 sample 真执行) · 减法是反事实 |
| **Approximate computing** | 都接受不精确 · 但近似算法仍真执行所有 op · 减法是不真执行 |
| **Lazy evaluation / call by need** | 都"延后执行" · 但 lazy 是 "用到才执行" · 减法是 "用到也不一定真执行" |
| **Speculation in CPU** | 都"先假设再修正" · speculation 真执行了 · 失败时回滚 · 减法是物理上没执行 |
| **Reversible computing** [Bennett 1973] | 都关心"操作的可撤销性" · reversible 是 logical 可逆 · 减法是 physical 不发生 |
| **Quantum amplitude amplification** | Grover 是加法 (每次迭代真触发) · 减法版本是反事实 Grover (大部分迭代不触发) |
| **MCTS** (Monte Carlo Tree Search) | rollout 真执行 · 减法版 CGTS (§8.7) 是反事实 rollout |

减法范式跟它们的差异化在 R1+R2+R3 三个性质**同时**具备 (见 §3.7)。

## 6.8 · 哲学意义 · "计算的本体论"

加法范式默认:**计算是发生在物理世界的事件** · 每个 op 都是一次物理操作 · 都消耗资源 · 都留痕迹。

减法范式提出:**计算可以发生在"潜在事件"层面** · 大部分 op 没真物理发生 · 但算法的输出依赖于它们 would-have-done。这跟物理学的 **counterfactual definiteness** 哲学问题深度相关 (Bell 不等式 / EPR / Wheeler 哲学全部围绕这点) [Bell 1964], [EPR 1935], [Wheeler 1978]。

减法计算的工程实现 (CFE 算子) 把这个哲学问题变成可工程化的实际能力。这是计算机科学跟物理基础研究的少有真接触点。

类比:**Microservices 之于 monolith** · 不只是"小一点的服务" · 而是**计算的部署粒度本体变了**。
减法范式之于加法范式 · 不只是 "更少操作的算法" · 而是 **计算的"事件" 本体变了**。

## 6.9 · 用减法范式重新看 5 个经典问题

| 问题 | 加法视角 | 减法视角 |
|---|---|---|
| Search (在 N 中找 hit) | Grover · $O(\sqrt{N})$ 真查询 | 反事实 OR · 测 "有没有 hit" · $O(\sqrt{N}/\delta)$ 真查询期望 $\ll \sqrt{N}$ |
| Verification (token 是否有效) | 用一次 · 消耗 | 反事实验证 · 不消耗 · 后续仍可用 |
| Multi-assay (N 样本测属性) | 每样本测 · 销毁 N 个 | 反事实测全部 · 物理上销毁 0 个 · 只统计结果 |
| Adversarial probe (对手有 trap?) | 暴露探测者 | 反事实探测 · 对手物理上看不到 |
| Active learning (标 N 候选要 label 谁) | 选 informative 的 · 付 label cost | 反事实预筛 · label cost 0 · 只对 surviving 真 label |

每个问题都从 "怎么少做几次操作" 变成 "怎么让大部分操作物理上不发生"。**问题没变 · 范式变了 · 解法变了**。

## 6.10 · 范式 vs 算法 vs 算子的层级关系

避免读者把这三个层级混淆:

| 层级 | 内容 | 例 |
|---|---|---|
| 范式 (Paradigm) | 哲学定位 · 思维方式 | Subtractive Computation Paradigm |
| 算子 (Operator) | 数学对象 · 可调用接口 | $\Phi^{CF}_f$ (§3) · 组合代数 (§4) |
| 算法 (Algorithm) | 具体过程 · 解决具体问题 | CPA · CBB · CAL · CV · CA* · CGTS (§8) |

三层是 **范式 → 算子 → 算法** 的 instantiation 链。范式启发算子设计 · 算子组合产生算法 · 算法解决具体问题。

## 6.11 · 减法范式还没做的事

- **数学严格基础**:把 SCP 作为正式范畴 · 公理化定义 + 跟 quantum measurement theory 的形式关系
- **编程语言**:第一个真正 native 支持减法计算的语言 (类似 Haskell native 支持 lazy)
- **设计模式集**:减法范式下的常见设计模式集 (类比 GoF 23 个加法范式 patterns)
- **教育材料**:在 algorithm course 里教 "subtractive thinking" · 培养下一代算法学家

这些是 §11 列出的开放问题中的一部分。

## 6.12 · 小结

减法计算范式 (SCP) 是 CFE 算子体系自然涌现的算法哲学 · 跟传统加法范式正交。

核心提议:**计算的真正力量 · 不在执行了什么 · 而在没执行什么**。这把物理学的 counterfactual definiteness 工程化为可调用的算法构造范式。

在 3 类杀手锏问题 (sparsity / side-effects / verify-without-commit) 上 · 减法范式给出经典加法范式无法达到的解法。

---

[← 上一章 · 05 3 维超越点](05-three-dim-transcendence.md) · [下一章 · 07 多维复杂度分析 →](07-complexity-analysis.md)
