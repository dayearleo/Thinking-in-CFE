# 04 · 算子组合代数

[← 返回 README](README.md)

## 4.1 · 为什么需要组合代数

单算子 $\Phi^{CF}_f$ (§3) 只能算单个 Boolean 函数。现实问题通常需要:

- 多步推理 (分类 → 排序 → 验证)
- 条件分支 (if hit then deep test else skip)
- 嵌套查询 (反事实判断 "假如 X 那么 Y 的反事实结果是什么")
- 迭代收敛 (类比 Grover 迭代)

没有组合规则 · 算子只是一次性原语 · 工程价值有限。组合代数让算子成为**可编程构件**。

## 4.2 · 5 种基础组合

设 $\Phi_f, \Phi_g, \Phi_h$ 是反事实算子 · 各自作用于 oracle 集合 $\mathcal{O}_f, \mathcal{O}_g, \mathcal{O}_h$。

### C1 · 串行 (Sequential)

$$\Phi_g \circ \Phi_f$$

**操作**:先跑 $\Phi_f(\mathcal{O}_f) \to y_f$ · 把 $y_f$ 合成为虚拟 oracle $\tilde{O}_{y_f}$ 接入 $\Phi_g$ · 跑 $\Phi_g(\mathcal{O}_g \cup \{\tilde{O}_{y_f}\}) \to y$

**语义**:前算子的结果作为后算子的输入 bit。

**用例**:multi-stage 过滤 (先粗筛再精筛)

### C2 · 并行 (Parallel)

$$\Phi_f \parallel \Phi_g$$

**操作**:同时跑 $\Phi_f(\mathcal{O}_f) \to y_f$ 和 $\Phi_g(\mathcal{O}_g) \to y_g$ (oracle 集不相交) · 经典后处理 $h(y_f, y_g) \to y$

**语义**:不同 oracle 子集独立运行 · 不共享量子态 · 结果经典合并。

**用例**:多 region 独立检测后汇总

### C3 · 嵌套 (Nested · 最强 · 最危险)

$$\Phi_f[\Phi_g]$$

**操作**:$\Phi_f$ 的某个 oracle $O_i$ 由 $\Phi_g$ 的"虚拟 oracle"提供 · 该虚拟 oracle 的 "obstacle 在不在" 由 $\Phi_g$ 反事实结果决定 · 全程不真测 $\Phi_g$ 的实际 oracle

**语义**:**反事实地评估 "假如 $\Phi_g$ 结果是 X · 那么 $\Phi_f$ 的值是什么"** —— 全程不真触发任何 oracle。

**用例**:counterfactual lookahead · 反事实的反事实推理

**警告**:嵌套深度大时 $\delta$ 累积失控 (§4.4)

### C4 · 条件 (Conditional)

$$\Phi_g \;|\; \Phi_f \;:\; \Phi_h$$

**操作**:跑 $\Phi_f(\mathcal{O}_f) \to y_f$ · if $y_f = 1$ 返回 $\Phi_g$ 结果 · else 返回 $\Phi_h$ 结果

**语义**:分支算子树。未走的分支 oracle 不被触发 (省一支代价)。

**用例**:if-then-else 决策 · adaptive algorithm 主干

### C5 · 迭代 (Iterative)

$$\Phi_f^k$$

**操作**:$\text{state}_0 = |\psi_0\rangle$ · for $j = 1..k$: $\text{state}_j = \Phi_f(\text{state}_{j-1}, \mathcal{O})$ · 输出 $\text{state}_k$ 测量结果

**语义**:类比 Grover 迭代 · 但每次迭代反事实 (oracle 不被消耗)。

**用例**:amplitude amplification 反事实版本 · 反事实搜索定位

## 4.3 · Cost Composition Theorems (草案)

记 $\delta_{\text{tot}}$ 为整个组合算子对原始 oracle 的总触发概率上界 · $B_{\text{tot}}$ 为总 oracle 调用次数上界。

### 串行 (C1)

$$\delta_{\text{tot}}(\Phi_g \circ \Phi_f) \leq \delta_f + \delta_g$$
$$B_{\text{tot}}(\Phi_g \circ \Phi_f) = B_{\delta_f}(f) + B_{\delta_g}(g)$$

(加性 · 失败率叠加 · 调用次数相加)

### 并行 (C2)

$$\delta_{\text{tot}}(\Phi_f \parallel \Phi_g) = \max(\delta_f, \delta_g)$$
$$B_{\text{tot}}(\Phi_f \parallel \Phi_g) = B_{\delta_f}(f) + B_{\delta_g}(g)$$

(取最大 · 独立事件 · 调用相加但物理并行)

### 嵌套 (C3)

$$\delta_{\text{tot}}(\Phi_f[\Phi_g]) \leq \delta_f \cdot N_{\text{deep}} + \delta_g$$
$$B_{\text{tot}}(\Phi_f[\Phi_g]) = B_{\delta_f}(f) \cdot B_{\delta_g}(g)$$

(深度放大 · 危险 · $N_{\text{deep}}$ 是嵌套深度;调用次数相乘 · 指数膨胀)

### 条件 (C4)

$$\delta_{\text{tot}} \leq \delta_f + \max(\delta_g, \delta_h)$$
$$B_{\text{tot}} = B_{\delta_f}(f) + \max(B_{\delta_g}(g), B_{\delta_h}(h))$$

(条件分支只走一支)

### 迭代 (C5)

$$\delta_{\text{tot}}(\Phi_f^k) \leq k \cdot \delta_f$$
$$B_{\text{tot}}(\Phi_f^k) = k \cdot B_{\delta_f}(f)$$

(线性累积)

### 重要警告

上述全部是**合理估计** · 不是严格证明。严格证明需要建立在 quantum query model + Zeno scheme 上的形式分析,是本论文的 **开放问题 Q1** (§11)。

## 4.4 · 嵌套深度的 $\delta$ cascade 问题

C3 嵌套时 $\delta_{\text{tot}} \propto N_{\text{deep}}$:

- 深度 5 · $\delta = 10^{-3}$ → $\delta_{\text{tot}} = 5 \times 10^{-3}$
- 深度 100 · $\delta_{\text{tot}} = 10^{-1}$ · 反事实性丢光

**工程控制策略** (类比经典分布式系统的 cascading failure mitigation):

| 策略 | 做什么 | 代价 |
|---|---|---|
| **Reset 屏障** | 每嵌套 $k$ 层强制 fresh oracle reload · 重置 $\delta$ 累积 | 实现复杂度上升 · oracle 制备成本 |
| **预算分配** | 总 $\delta_{\text{budget}}$ 按嵌套深度分配 · 每层 $\delta_i = \delta_{\text{budget}}/N_{\text{deep}}$ | 每层 $B$ 上升 |
| **Adaptive 阈值** | 嵌套到一定深度后切换到 standard quantum query (放弃反事实保证 · 保住正确性) | 部分失去 R1/R2/R3 |
| **拒采样** | 检测到 $\delta$ 超预算 · 整个 chain 作废重跑 | 期望调用次数上升 |

## 4.5 · Programming Model 草案

为让算子代数能被算法学家直接用 · 需要 programming model 抽象。

### 表达式层

```
expr  := Φ(f, [oracle_1, ..., oracle_N], δ, ε)
      | expr ∘ expr             // sequential
      | expr ‖ expr             // parallel
      | expr [oracle ← expr]    // nested
      | expr ? expr : expr      // conditional
      | iter(expr, k)           // iterative
      | const_oracle(value)     // 经典 bit 包装为 oracle
```

### 类型系统层

- Type `Oracle[T]` · 类型化 oracle (T 是被探测属性)
- Type `Probe[N, δ]` · N 路 probe · 触发率上界 $\delta$
- Type `Result[ε]` · 结果 · 错误率 $\epsilon$
- 编译期检查 $\delta$/$\epsilon$ 是否在预算内 (类比 Rust borrow checker 思路)

### 编译器优化层

可以做的优化:

- **代数简化**:$\Phi_{OR}(\Phi_{OR}(a, b), c) = \Phi_{OR}(a, b, c)$
- **嵌套展开**:深度小时把 $\Phi_f[\Phi_g]$ 展开为 $\Phi_{f \circ g}$
- **预算分配**:自动分配 $\delta_{\text{budget}}$ 到每个子算子
- **死代码消除**:条件分支检测到不会走到的子树直接消除

### 后端目标

- **Photonic chip backend** · 编译到集成芯片 (mode 数 / EAM 配置)
- **FT QC backend** · 当 FT QC 可用 · 编译到 quantum circuit (供未来用)
- **Simulator backend** · 经典 simulator 用于算法 prototyping

## 4.6 · 跟标准 quantum circuit composition 的关系

$\Phi^{CF}_f$ 组合代数跟标准 quantum circuit composition (gate 组合) 有 3 个本质差异:

| 维度 | Quantum circuit composition | CFE composition |
|---|---|---|
| 组合基本对象 | unitary gates | algorithmic-level operators $\Phi^{CF}_f$ |
| 中间结果 | quantum state (amplitude) | classical bit (after measurement) |
| 组合成本可加性 | gate count 加性 | $\delta$/$B$ 各自有不同合成规则 |
| 嵌套语义 | function composition · 无 $\delta$ 概念 | 反事实嵌套 · $\delta$ cascade |

CFE 组合是 **algorithmic-level 而非 circuit-level** · 这跟 high-level functional programming 之于 assembly programming 的关系类似。

## 4.7 · 跟 indefinite causal order (ICO) 的关系

近年量子信息有一支 **indefinite causal order** 工作 [Quantum journal 2024 q-2024-02-05-1241] · 研究 quantum process 不假设固定时序时的能力。ICO 跟 CFE 是**正交**方向:

- ICO 关注 **时序的不确定性**
- CFE 关注 **触发的不确定性 (反事实)**

两者可以组合 (例如 ICO-aware CFE 算子) · 但本论文暂不展开 · 留为 §11 开放问题。

## 4.8 · 小结

5 种基础组合 + cost composition theorem 草案构成 CFE 算子的最小代数。从这一代数可以构造任意复杂的反事实算法 (§8 算法模板就是直接使用这一代数的实例)。

代数本身有 7 个开放问题 (详 §11):严格 cost 证明 / 嵌套深度上限 / 公理化 / 等价性判定 / 最优编译 / 跟标准 QC 互操作 / 类型系统设计。

---

[← 上一章 · 03 算子定义](03-operator-formal-definition.md) · [下一章 · 05 3 维超越点 →](05-three-dim-transcendence.md)
