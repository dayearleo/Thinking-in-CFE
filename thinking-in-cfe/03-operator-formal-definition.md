# 03 · CFE 算子的形式定义

[← 返回 README](README.md)

## 3.1 · 基础设定

设 $X = \{0,1\}^N$ 是 N 维 Boolean 输入空间 · $\mathbf{x} = (x_1, \ldots, x_N) \in X$ 是一个具体输入。**$\mathbf{x}$ 不直接可访问** · 我们只能通过 oracle 访问。

设 $O_i$ 是第 $i$ 个标准量子 oracle:

$$O_i : |b\rangle \otimes |a\rangle_{\text{anc}} \;\mapsto\; |b\rangle \otimes |a \oplus x_i\rangle_{\text{anc}}$$

设 $\hat{O}_i$ 是 $O_i$ 的 **counterfactual 变种** · 做"是否会触发"的物理探测 · 但实际触发概率被压到 $\leq \delta$。$\hat{O}_i$ 的物理实现通常基于 Quantum Zeno 链式 Mach-Zehnder 配置 [Kwiat 1995] · 详见 [Franco-Camillini-Galvão 2026] 的集成芯片实现。

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

其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度。

**注 · δ-参数化扩展明示** (audit 2026-06-20 落地):本公式是 [Lin-Lin 2015] 原版 $B(f) = \Theta(Q(f)^2)$ 的显式 $\delta$-参数化扩展 · 在 $\delta \to 0$ 极限下还原 Lin-Lin 原版。Lin-Lin 模型本身**没有** $\delta$ 参数 (隐含 $\delta \to 0$ 极限 · 给 $\Theta$ tight bound)。我们引入 $\delta$ 作为显式 trigger probability 参数 · 把 $\Theta$ 放宽为 $O$ 上界 · 让算子在 $\delta > 0$ finite trigger budget 下可工程化。Lin-Lin 原模型见 arXiv:1410.0932 · CCC 2015 · ToC 12(18) 2016 · doi:10.4086/toc.2016.v012a018。

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
| $\Phi^{CF}_{\text{OR}}$ | $\bigvee_i x_i$ | 至少一个 $x_i = 1$? | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{AND}}$ | $\bigwedge_i x_i$ | 全部 $x_i = 1$? | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{NOR}}$ | $\neg\bigvee_i x_i$ | 全部 $x_i = 0$? · Wheeler 推广原型 | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{MAJ}}$ | majority | 多数为 1? | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{COUNT}}$ | $\sum_i x_i$ | 多少个 1? | $O(N \cdot \text{ans}/\delta)$ |
| $\Phi^{CF}_{\text{T}_t}$ | threshold $\geq t$ | 至少 $t$ 个为 1? | $O(Nt/\delta)$ |
| $\Phi^{CF}_{\text{LOC}}$ | locate first 1 | 哪个 $i$ 是第一个 1? | $O(N/\delta)$ 期望 |
| $\Phi^{CF}_{\text{NAND-tree}}$ | balanced NAND-tree | 平衡 NAND-tree 评估 | $O(N/\delta)$ |

**注 · 公式修正** (audit 2026-06-20 落地):上表 cost 公式来自 P3 主公式 $B_\delta(f) = O(Q(f)^2/\delta)$ + 各 $f$ 的标准量子查询复杂度 $Q(f)$:

| $f$ | $Q(f)$ | $Q(f)^2$ | $B_\delta(f) = O(Q(f)^2/\delta)$ |
|---|---|---|---|
| OR | $\Theta(\sqrt{N})$ (Grover) | $\Theta(N)$ | $O(N/\delta)$ |
| AND | $\Theta(\sqrt{N})$ | $\Theta(N)$ | $O(N/\delta)$ |
| MAJ | $\Theta(\sqrt{N})$ | $\Theta(N)$ | $O(N/\delta)$ |
| COUNT (k=ans) | $\Theta(\sqrt{N \cdot \text{ans}})$ | $\Theta(N \cdot \text{ans})$ | $O(N \cdot \text{ans}/\delta)$ |
| T_t | $\Theta(\sqrt{Nt})$ | $\Theta(Nt)$ | $O(Nt/\delta)$ |
| NAND-tree | $\Theta(\sqrt{N})$ (Farhi 2008) | $\Theta(N)$ | $O(N/\delta)$ |

[Lin-Lin 2015] 给出 OR / AND / specific 函数的 tighter special-case bound (例如 OR 可达 $O(N/\log^2 N \cdot 1/\delta)$) · 上表给的是 generic 上界。具体函数的精确 bound 见 [Lin-Lin 2015] §3-§5。

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

**重要 caveat** (审计 2026-06-20 落地 · 见 §11 + audit/batch-11):

- **Single bomb tester 规模**:single IFM 的 25% detection statistics 可以在 classical hydrodynamic pilot-wave 系统中模拟 [Frumkin-Bush 2023, PRA 108:L060201]。在这一规模上 · R1 性质 (统计意义) **不严格 quantum-only**
- **Chained Zeno 规模** (N≥6 chained MZI, Kwiat 1995):需要任意 scale 的 nonlocal wavefunction · 经典 pilot-wave 系统受 finite spatial extent + finite memory 限 · 不可 reproduce
- **Multi-object IFM 规模** (N≥5 sequential, Franco-Camillini-Galvão 2026):同上 · 全局 entangled probe state · 经典不可

CFE 算子的实际工程 niche (§10 应用) 都假设 N≥2 chained · 在这些规模 R1/R2/R3 differentiator 严格成立。Single bomb tester 规模的 caveat 仅是 honest 标注 · 不影响应用论点。

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

详 [Franco-Camillini-Galvão 2026] · [Filatov-Auzinsh 2024] · [Calafell et al. 2019]。本论文需要的实现层最小集合:

- N-mode 集成 photonic interferometer (SOI silicon-on-insulator / SiN / 飞秒激光写入)
- 可切换 obstacle 实现 · 多种 candidate:
  - 电吸收调制器 (EAM)
  - thermo-optic phase shifters + SWAP gates (Calafell 2019 实测路径)
  - tunable BS reflectivity (Franco 2026 实测路径)
- 单光子源 (heralded SPDC · 1565 nm telecom band · 或 III-V QD)
- 单光子探测器 (SNSPD 阵列 · ~90% detection efficiency)
- Quantum Zeno effect 加深 + chained interferometer 提升反事实效率

**SOTA · 精确化** (2026 年 4 月数据):

| 维度 | SOTA 数字 | Source |
|---|---|---|
| Universal photonic processor mode 数 | **12 modes** (Quandela Ascella cloud-accessible) | Franco-Camillini-Galvão 2026 |
| Multi-object IFM 实测 object 数 | **N = 5 sequential** (single quantum probe) | Franco-Camillini-Galvão 2026 |
| Chained CFC (Salih scheme) 实测 N | **N = 6 max** (chip-layout-limited) | Calafell et al. 2019 |
| Single MZI visibility | **99.94%** average | Calafell et al. 2019 |
| Insertion loss per facet | **3 dB** | Calafell et al. 2019 |
| Heralding efficiency (SPDC) | **~3%** | Calafell et al. 2019 |
| SNSPD detection efficiency | **~90%** at telecom 1565 nm | photonSpot via Calafell 2019 |
| Chained N=6 bit success rate | **99% with M=320 photons per bit** · CFC violation 2.4% | Calafell et al. 2019 |

**重要 caveats** (跟早期论文版本 N=12 / 5 dB loss / >99% 等数字的对比 · 详 §11):

- N=12 是 platform mode 数 (hardware capability) · **不是 multi-object IFM 实测 object 数** (后者目前 SOTA N=5)
- "5 dB loss" 是 per-facet · system end-to-end success rate ~ few % (受 heralding + chip transmission + detection 累乘 dominated)
- "> 99% efficiency 单链路" 指 single MZI visibility (99.94%) · chained protocol 整体 bit success rate 需 M photons per bit 编码才能达到
- Multi-object IFM efficiency 随 n 快速衰减:Franco 2026 verbatim "η is in general a quickly decaying function of n"

## 3.10 · 限界

为防止后续滥用 · 明确算子**不能做什么**:

- 不能查询非物理 oracle (远程 API / 抽象数据)
- 不能消除单 bit 输出的局限 ($k$ bit 输出需 $k$ 次独立调用)
- 不能算 super-polynomial 的 $f$ (受 $Q(f)$ 限制)
- 不能突破 Holevo bound
- 不替代量子计算 (针对查询代价问题 · 不是计算复杂度问题)
- 不在 NISQ era 立即工程化大规模:**实测 SOTA 限 N=5-6** (multi-object IFM [Franco-Camillini-Galvão 2026] N=5 sequential · chained CFC [Calafell et al. 2019] N=6 max) · N=12-32 是 platform mode capability (Quandela Ascella · MIT SOI nanophotonic chip) 而**非 IFM object 数** (audit 2026-06-20 精确化 · 详 §11.2)

详细限界讨论见 §11。

---

[← 上一章 · 02 先行研究](02-prior-art.md) · [下一章 · 04 组合代数 →](04-composition-algebra.md)
