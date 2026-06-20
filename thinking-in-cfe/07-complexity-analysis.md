# 07 · 多维复杂度分析

[← 返回 README](README.md)

## 7.1 · 为什么单一 query complexity 不够

传统算法复杂度分析以 **query complexity** $Q(f)$ 为核心 (经典 / Grover / 量子查询)。但 CFE 算子引入了**新的代价维度** · 这些维度在传统分析里不被关心:

- **触发率 / disturbance complexity** ($\delta$) · 物理触发概率上界
- **adversary observability complexity** ($\eta$) · 对手能察觉查询发生的概率
- **硬件成本维度** · 集成度 / 错误率 / 平台规模

本章建立多维复杂度框架 · 把 CFE 的优势精确定位到正确的维度上。

## 7.2 · 维度定义

### 维度 D1 · Query Complexity $Q(f)$

经典定义:算法在 worst-case input 下最少需要多少次 oracle query 才能算出 $f(x)$。

- 经典确定性 query: $D(f)$
- 经典随机 query: $R(f)$
- 量子 query: $Q(f)$
- **Bomb query (CFE)**: $B_\delta(f) = O(Q(f)^2/\delta)$ [Lin-Lin 2015]

CFE 在 D1 维度上**严格劣于** standard quantum query (慢 $1/\delta$ 倍)。

### 维度 D2 · Disturbance Complexity $D_\Delta(f)$ (本论文新定义)

**定义 2**:算法在 worst-case 下,对 oracle 的总物理触发概率上界。

$$D_\Delta(f) = \max_{x \in X, i \in [N]} \Pr[O_i \text{ 物理触发} \mid x_i = 1]$$

- 经典算法 / Grover / standard quantum query · $D_\Delta(f) = 1$ (必然触发)
- **CFE 算子**:$D_\Delta(f) = \delta$ (任意小 · 参数可调)
- FT QC 即使无限大: $D_\Delta(f) = 1$ (unitary call 必然纠缠 = 触发)

CFE 在 D2 维度上**严格优于**所有其他算子族 · 这是新的 differentiator。

### 维度 D3 · Adversary Observability Complexity $\eta(f)$ (本论文新定义)

**定义 3**:持有 oracle 的对手 (有 perfect 量子测量能力) 能正确检测到算法执行过的概率。

$$\eta(f) = \Pr[\text{adversary detects algorithm execution}]$$

- 经典算法:$\eta = 1$
- Standard quantum query / Grover:$\eta = 1$ (纠缠可测)
- FT QC: $\eta = 1$ (同理)
- **CFE 算子** ($\delta \to 0$): $\eta \to 0$ (没纠缠产生)

CFE 在 D3 维度上**严格优于** FT QC · 这是 §5 的 D1.b 子维度的精确化表达。

### 维度 D4 · Hardware Cost $\mathcal{H}(f)$ (本论文新定义)

**定义 4**:实现算法需要的物理硬件总成本 · 含 qubit count / fidelity / cryogenic / cost。

我们建议用 "logical qubit equivalent" (LQE) 作为统一单位:

$$\mathcal{H}(f) \approx (\text{logical qubits}) \times (\text{cost per logical qubit})$$

- 经典算法: $\mathcal{H} = 0$ (不需 quantum 硬件)
- Grover / standard quantum query (理论): 跟 FT QC 同
- FT QC 实现 $\Phi^{CF}_f$: $\sim 10^3 N \times \text{cost-per-physical-qubit}$
- **CFE 专用 photonic IFM**: $N$ photonic modes $\times \sim$1k each = $\sim N$k cost

CFE 在 D4 维度上**显著优于** FT QC · 约 6 个数量级。

## 7.3 · Pareto 边界

把 D1 + D2 + D3 + D4 当 4 维空间 · 各算子族在这空间的位置:

| 算子族 | D1 | D2 | D3 | D4 |
|---|---|---|---|---|
| 经典 OR/AND | $N$ | 1 | 1 | 0 |
| Grover | $\sqrt{N}$ | 1 | 1 | high (需 FT QC) |
| Standard quantum query | $Q(f)$ | 1 | 1 | high |
| **CFE $\Phi^{CF}_f$** | $Q(f)^2/\delta$ | $\delta$ | $\sim \delta^N$ | medium (photonic IFM) |
| FT QC 模拟 CFE | $Q(f)^2/\delta$ | 1 | 1 | very high |

**Pareto 不可比性**:CFE 在 D1 上劣 · 在 D2/D3/D4 上优 · 谁 dominate 取决于问题对各维度的权重。

### Pareto 边界图 (示意)

```
           D2 (disturbance) ↓
                |
                |        ★ CFE (low D2, low D3, medium D4, slightly higher D1)
                |
                |  ● FT QC (high D2, high D3, very high D4, lowest D1)
                |
                |  ● Grover (high D2, high D3, high D4, medium D1)
                |
                |  ● Classical (highest D2, highest D3, zero D4, highest D1)
                |
                +─────── D1 (query) →
```

CFE 占据 Pareto 边界上**别的算子族到不了**的位置:**低 D2 + 低 D3 + 中等 D4 + 略高 D1**。

## 7.4 · 何时 CFE 严格优 / 严格劣

### CFE 严格优于经典

满足任一:

- D2 maters (查询有副作用)
- D3 matters (查询不能被观察)

(因为经典在 D1 不算劣 · 但 D2/D3/D4 都劣 · 任一权重高时 CFE 胜)

### CFE 严格优于 Grover / Standard QC

满足任一:

- D2 matters (CFE 给 $\delta$ · QC 给 1)
- D3 matters (CFE 给 $\to 0$ · QC 给 1)
- D4 matters (CFE 便宜 6 个数量级)

(因为 CFE 在 D1 上劣 · 但 D2/D3/D4 都优)

### CFE 严格优于 FT QC 模拟 CFE

满足任一:

- D3 matters (FT QC 模拟仍 unitary · 有纠缠)
- D4 matters (FT QC overhead 高)

### Classical 严格优于 CFE

满足全部:

- D2 不重要 (查询无副作用)
- D3 不重要 (查询不需隐蔽)
- D4 重要 (不想买 quantum 硬件)

(经典在 D4 上免费 · 其他维度不 matter 时 · 经典胜)

## 7.5 · 算子组合在多维复杂度上的演化

§4 的 5 种组合在 4 维上的代价合成:

| 组合 | $D_1$ | $D_2$ | $D_3$ | $D_4$ |
|---|---|---|---|---|
| C1 串行 | $B_f + B_g$ | $\delta_f + \delta_g$ | $\eta_f + \eta_g$ | $\max$ |
| C2 并行 | $B_f + B_g$ | $\max(\delta_f, \delta_g)$ | $\max(\eta_f, \eta_g)$ | $\mathcal{H}_f + \mathcal{H}_g$ |
| C3 嵌套 | $B_f \cdot B_g$ | $\delta_f \cdot N_{\text{deep}} + \delta_g$ | $\eta_f + \eta_g$ | $\max$ |
| C4 条件 | $B_f + \max(B_g, B_h)$ | $\delta_f + \max(\delta_g, \delta_h)$ | $\eta_f + \max(\eta_g, \eta_h)$ | $\max$ |
| C5 迭代 ($k$ 次) | $k \cdot B_f$ | $k \cdot \delta_f$ | $k \cdot \eta_f$ | $\mathcal{H}_f$ |

(这些都是上界估计 · 严格证明是 §11 的 Q1)

## 7.6 · 具体算法的复杂度分析示例

以 §8 的 CPA (Counterfactual Pruning Algorithm) 为例:

**问题**:在 $N$ 个候选里找 $K$ 个满足 predicate 的 · sparsity $K \ll N$。

**经典算法** (linear scan):
- $D_1 = N$ · $D_2 = 1$ · $D_3 = 1$ · $D_4 = 0$

**Grover variant** (找 hit 的):
- $D_1 = O(\sqrt{N})$ · $D_2 = 1$ · $D_3 = 1$ · $D_4 = $ high

**CPA (我们的)**:
- $D_1 = O(\sqrt{N}/\delta \cdot K)$ (略劣)
- $D_2 = K\delta + (N-K) \cdot 0 \approx K\delta$ (远优 · 因为大部分 oracle 没触发)
- $D_3 = O(K\delta)$
- $D_4 = $ medium (photonic IFM)

如果 sparsity 极端 ($K \ll N$ 且 $\delta$ 小) · CPA 的总 disturbance 远小于经典 / Grover · 是真正的 paradigm-level 改进。

## 7.7 · "复杂度类"层面 · CFE 算子定义了什么类?

类比经典/量子复杂度类 (P / NP / BQP 等) · CFE 算子定义了一个新的复杂度类:

**定义 5 · CFP (Counterfactual Polynomial)**:

> $f \in \text{CFP}$ iff 存在多项式 $p$ 使得 $B_{1/p(N)}(f) \leq p(N)$

即:可以在多项式时间 · 多项式 $\delta$ 预算内求值的函数类。

**关系**:
- $\text{CFP} \subseteq \text{BQP}$ (CFE 比 BQP 慢 · 但能算的不超过)
- $\text{P} \subseteq \text{CFP}$ (经典多项式 trivially 可被 CFE 模拟 · 通过 $\delta = 1$ 退化)
- 是否 $\text{CFP} = \text{BQP}$?(开放问题 Q11 · §11)

CFP 是 quantum 复杂度类层面对 CFE 算子的形式化。它本身值得一篇专门的论文 (本论文不展开)。

## 7.8 · 小结

CFE 算子的真正价值不在传统单一 query complexity (D1) · 而在引入了 3 个新维度:

- **D2 disturbance** · 物理触发率任意小
- **D3 adversary observability** · 对手不可察觉
- **D4 hardware cost** · 比 FT QC 便宜 6 个数量级

这 3 个新维度在传统复杂度分析中**没被考虑** · 但在实际工程中**至关重要**。

CFE 占据 Pareto 边界上别的算子族到不了的位置 · 这正是它在 §5 D3 维度独占性的精确表达。

---

[← 上一章 · 06 减法计算范式](06-subtractive-paradigm.md) · [下一章 · 08 算法模板 →](08-algorithm-templates.md)
