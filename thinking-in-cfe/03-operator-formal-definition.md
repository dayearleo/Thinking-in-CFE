# 03 · CFE 算子的形式定义

[← 返回 README](README.md)

## 3.1 · 基础设定

设 $X = \{0,1\}^N$ 是 N 维 Boolean 输入空间 · $\mathbf{x} = (x_1, \ldots, x_N) \in X$ 是一个具体输入。**$\mathbf{x}$ 不直接可访问** · 我们只能通过 oracle 访问。

设 $O_i$ 是第 $i$ 个标准量子 oracle:

$$O_i : |b\rangle \otimes |a\rangle_{\text{anc}} \;\mapsto\; |b\rangle \otimes |a \oplus x_i\rangle_{\text{anc}}$$

设 $\hat{O}_i$ 是 $O_i$ 的 **counterfactual 变种** · 做"是否会触发"的物理探测 · 但实际触发概率被压到 $\leq \delta$。$\hat{O}_i$ 的物理实现通常基于 Quantum Zeno 链式 Mach-Zehnder 配置 [Kwiat 1995] · 详见 [Hance 2025] 的集成芯片实现。

设 $f: \{0,1\}^N \to \{0,1\}$ 是任意 Boolean 函数。

## 3.2 · 核心定义

**定义 1 · Counterfactual Function Evaluation Operator $\Phi^{CF}_f$**

对任意 Boolean 函数 $f$ · 算子 $\Phi^{CF}_f$ 定义为映射:

$$\Phi^{CF}_f : (\hat{O}_1, \ldots, \hat{O}_N) \times |\psi_0\rangle \;\longrightarrow\; y \in \{0,1\}$$

输入是 N 个反事实 oracle + 一个初始量子态 $|\psi_0\rangle$ · 输出是经典单 bit $y$ · 满足以下三条性质:

**(P1) 正确性**:

$$\Pr\left[y = f(\mathbf{x})\right] \geq 1 - \epsilon$$

**(P2) 反事实性**:对每个 $i$ 满足 $x_i = 1$ (即该 oracle 物理上有 obstacle):

$$\Pr\left[O_i \text{ 在求值期间被物理触发}\right] \leq \delta$$

**(P3) 代价上界**:实现 $\Phi^{CF}_f$ 需要的总 oracle 调用次数:

$$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$

其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度 [Lin-Lin 2015]。

## 3.3 · 关键参数

- $\epsilon \in (0, 1)$ · 算法可接受的错误概率上界 (类比 Las Vegas/Monte Carlo 算法的失败率)
- $\delta \in (0, 1]$ · 单个 oracle 的物理触发率上界
- $N$ · oracle 数量
- $B_\delta(f)$ · 总调用预算

工程取值参考:$\epsilon \sim 10^{-3}$, $\delta \sim 10^{-2}$ 到 $10^{-6}$。

## 3.4 · 极限与退化

| 参数取值 | 算子行为 |
|---|---|
| $\delta \to 0$ | 完全反事实 · 但 $B(f) \to \infty$ · 实际工程不取极限 |
| $\delta = 1$ | 退化为标准量子查询 · $B(f) = Q(f)^2$ · 失去反事实优势 |
| $N=2, f=\text{NOR}$ | 还原为 Elitzur-Vaidman bomb tester (1993 原始版本) |
| $N \geq 2, f=\text{NOR}$ | Wheeler 多路推广 |
| $f = \text{NAND-tree}$ | Farhi-Childs NAND-tree 算法 [Farhi 2008] [Childs 2009] 在 bomb query 模型下的版本 |

## 3.5 · 子算子目录

具体 $f$ 的实例化 · 形成算子库:

| 算子符号 | $f$ | 语义 | 代价 $B_\delta(f)$ |
|---|---|---|---|
| $\Phi^{CF}_{\text{OR}}$ | $\bigvee_i x_i$ | 至少一个 $x_i = 1$? | $O(\sqrt{N}/\delta)$ |
| $\Phi^{CF}_{\text{AND}}$ | $\bigwedge_i x_i$ | 全部 $x_i = 1$? | $O(\sqrt{N}/\delta)$ |
| $\Phi^{CF}_{\text{NOR}}$ | $\neg\bigvee_i x_i$ | 全部 $x_i = 0$? · Wheeler 推广原型 | $O(\sqrt{N}/\delta)$ |
| $\Phi^{CF}_{\text{MAJ}}$ | majority | 多数为 1? | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{COUNT}}$ | $\sum_i x_i$ | 多少个 1? | $O(\sqrt{N \cdot \text{ans}}/\delta)$ |
| $\Phi^{CF}_{\text{T}_t}$ | threshold $\geq t$ | 至少 $t$ 个为 1? | $O(\sqrt{Nt}/\delta)$ |
| $\Phi^{CF}_{\text{LOC}}$ | locate first 1 | 哪个 $i$ 是第一个 1? | $O(\sqrt{N}/\delta)$ 期望 |
| $\Phi^{CF}_{\text{NAND-tree}}$ | balanced NAND-tree | 平衡 NAND-tree 评估 | $O(\sqrt{N}/\delta)$ |

## 3.6 · 算法层接口

算法学家不关心物理 · 只需要知道接口签名:

```
counterfactual_eval(
    f       : Predicate[Vec[Bit]] -> Bit,    // 要算的函数
    probes  : Vec[Oracle],                   // N 个 oracle 句柄
    epsilon : Float = 1e-3,                  // 允许错误率
    delta   : Float = 1e-3,                  // 允许触发率上界
) -> Result[Bit, OperatorError]
```

行为契约:

- 返回值 $y$ 满足 $\Pr[y = f(\mathbf{x})] \geq 1 - \epsilon$
- 每个被探测的 oracle 物理触发概率 $\leq \delta$
- 接口暴露 $B_\delta(f)$ 作为可估算成本
- 失败模式:硬件保真度不足 / loss 累积时返回 `Err(UNRELIABLE)` 而非错误结果
- 可组合:算子可嵌套 (详 §4)

## 3.7 · 跟其他原语的差异化

| 性质 | 经典 OR/AND | Grover · 标准量子 | $\Phi^{CF}_f$ |
|---|---|---|---|
| 函数任意性 | ✅ | ✅ | ✅ |
| 输入并行 | ⚠️ 需 N 线程 | ✅ 叠加并行 | ✅ N 路同时探测 |
| 查询复杂度 | $N$ | $\sqrt{N}$ | $\sqrt{N}/\delta$ |
| **R1 · 触发率任意小** | ❌ 100% | ❌ 100% | ✅ 可调 $\delta$ |
| **R2 · adversary 不可检测** | ❌ | ❌ | ✅ 在 $\delta \to 0$ 极限 |
| **R3 · 输入不消耗** | ❌ | ❌ | ✅ |
| 物理 oracle 要求 | 任意 | quantum | quantum (光/微波/spin) |
| 可组合 | ✅ | ✅ | ✅ |

**只有 $\Phi^{CF}_f$ 同时具备 R1 + R2 + R3** —— 这是算子的核心 differentiator。

## 3.8 · 命名约定

采用双轨命名:

- **学术** · Counterfactual Function Evaluation (CFE) · 符号 $\Phi^{CF}_f$
  - 跟现有学术术语 ([Mitchison-Jozsa 2001] counterfactual computation) 接续
  - 便于论文引文献
- **工程 / 对外** · GhostQuery
  - 隐喻清晰 ("看见但没触碰")
  - 跨学科适用

代码符号:`Φ_CF[f]` 或 `cfe(f, probes, ε, δ)`。

## 3.9 · 物理实现要点摘要

详 [Hance 2025] · [Filatov-Auzinsh 2024]。本论文需要的实现层最小集合:

- N-mode 集成 photonic interferometer (Si / SiN / 飞秒激光写入)
- 可切换 absorber (电吸收调制器 EAM) 作为 obstacle 物理实现
- 单光子源 (heralded SPDC 或 III-V QD)
- 单光子探测器 (SNSPD 阵列)
- Quantum Zeno effect 加深 + chained interferometer 提升反事实效率

**SOTA**:N = 12 universal photonic processor 已 lab proven · 端到端 5 dB loss · counterfactual efficiency 单链路 > 99%。

## 3.10 · 限界

为防止后续滥用 · 明确算子**不能做什么**:

- 不能查询非物理 oracle (远程 API / 抽象数据)
- 不能消除单 bit 输出的局限 ($k$ bit 输出需 $k$ 次独立调用)
- 不能算 super-polynomial 的 $f$ (受 $Q(f)$ 限制)
- 不能突破 Holevo bound
- 不替代量子计算 (针对查询代价问题 · 不是计算复杂度问题)
- 不在 NISQ era 立即工程化大规模 (当前 SOTA 限 N $\leq$ 12-32)

详细限界讨论见 §11。

---

[← 上一章 · 02 先行研究](02-prior-art.md) · [下一章 · 04 组合代数 →](04-composition-algebra.md)
