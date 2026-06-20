# 11 · 诚实限界与开放问题

[← 返回 README](README.md)

## 11.1 · 算子层限界

CFE 算子 (§3) 不能做的事:

| 限界 | 原因 |
|---|---|
| 不能查询非物理 oracle | oracle 必须有光 / 微波 / spin 的物理实现 · 不能是远程 API / 抽象数据 |
| 不能消除单 bit 输出的局限 | $f$ 输出 $k$ bit 需 $k$ 次独立调用 · 总成本 $k \cdot B_\delta(f)$ |
| 不能算 super-polynomial 的 $f$ | 受 $Q(f)$ 限制 · CFE 是 $Q(f)^2/\delta$ |
| 不能突破 Holevo bound | 从 $\Phi^{CF}_f$ 提取的信息量上界跟 standard quantum query 相同 |
| 不替代量子计算 | 算子针对查询代价问题 · 不是计算复杂度问题 |
| 不在 NISQ era 立即工程化大规模 | 需要稳定多模 photonic chip + 高 fidelity probes |

## 11.2 · 硬件层限界 (基于 §03.9 精确化 SOTA + 物理审计 finding)

当前 SOTA (2026-04 数据 · 经物理审计验证):

| 维度 | 当前可达 (精确化) | 限制因素 |
|---|---|---|
| Universal photonic processor mode 数 | **12 modes** (Quandela Ascella cloud) [Franco 2026] | 累积 loss / phase 漂移 / fab 良率 |
| **Multi-object IFM 实测 object 数** | **N=5 sequential** (single quantum probe) [Franco 2026] | η(n) 随 n 快速衰减 (Franco verbatim) |
| Chained CFC 实测 N | **N=6 max** (chip-layout-limited) [Calafell 2019] | 物理 chip 设计 |
| Single MZI visibility | **99.94%** average [Calafell 2019] | thermo-optic phase shifter precision |
| Insertion loss per facet | **3 dB** [Calafell 2019] | SOI coupling efficiency |
| Heralding efficiency (SPDC) | **~3%** [Calafell 2019] | SPDC nonlinear conversion + coupling |
| SNSPD detection efficiency | **~90%** at 1565 nm [Calafell 2019] | 跟 cryogenic 一起的 trade-off |
| Chained N=6 bit success rate | **99% with M=320 photons per bit** · CFC violation 2.4% [Calafell 2019] | 整体 protocol fidelity 累乘 |
| 工作温度 | SNSPD 需 cryogenic 1-4 K | 探测器替代品 SPAD 效率掉 30-50% |
| Photon source 速率 | 1-100 MHz | 不是瓶颈 |
| 切换速度 (thermo-optic) | 130 kHz [Calafell 2019] | thermal time constant |

### 5 个物理 CAVEAT (审计 2026-06-20 落地 · 跟早期声明的 reconciliation)

**CAVEAT 1 · multi-object IFM efficiency 快速衰减**

Franco 2026 verbatim:**"η is in general a quickly decaying function of n"**。意味着 §10 A2/A3/A4 的 N=20+ 假设 over-stated。**当前 SOTA N=5** · scaling to N=20+ 需要:

- exponential resource scaling (fully overlapping scheme $2^{n-1}$)
- 或 linear scaling 但 efficiency 极低 (Franco non-overlapping)
- 或 manipulate 多 degrees of freedom (Filatov-Auzinsh temporal encoding)

§10 应用 niche **当前应聚焦 N $\leq$ 10 场景** · N=20+ 是 open engineering challenge。

**CAVEAT 2 · CFC violation 不是 0**

Calafell 2019 实测 N=6, M=320 时 CFC violation **2.4%**。R2 "adversary undetectable" claim (§5.2 / §15) 应改为 "**bounded** adversary observability complexity $\eta$ · 不是绝对 0"。

精确表述:$\eta = (1 - \text{visibility})^N \cdot k$ for some constant · 在 N=6, visibility 99.94% 时 $\eta \sim 0.024$。

**CAVEAT 3 · Salih 2013 protocol scaling 限制**

Calafell 2019 引述:**"Salih scheme requires thousands of optical elements to achieve >95% success"**。我们 §14 / §15 / §17 引用 Salih 协议时必须诚实标注 "需 thousands of MZI 才 >95%" · 当前 chip 物理上 N=6 max (Calafell)。

**CAVEAT 4 · Heralding efficiency 限制 wall-clock cost**

Calafell 2019 heralding efficiency **~3%**。CFE 算法 wall-clock cost model 应该是:

$$T_{\text{wall}} = \frac{B_\delta(f)}{\text{rate}_{\text{source}} \cdot \eta_{\text{heralding}} \cdot \eta_{\text{detection}}}$$

3% heralding × 90% detection = ~2.7% system efficiency · 即每个理论 oracle call 实际 wall-clock $\sim$ 37 个 photon period。§07 复杂度章节应加 wall-clock cost discussion。

**CAVEAT 5 · Chained MZI visibility 累乘衰减**

Single MZI visibility 99.94% · chained N 时累乘 $(0.9994)^N$:

| N | Visibility 累乘 |
|---|---|
| 6 | 99.64% |
| 20 | 98.81% |
| 100 | 94.18% |
| 1000 | 54.69% (CFC 已 broken) |

N=100+ 时 visibility 已经 dominate violation rate · 这是 Salih scheme "thousands of elements" 的物理瓶颈来源。

**CAVEAT 6 · Single IFM 经典 pilot-wave 系统可以模拟 (Frumkin-Bush 2023)**

[Frumkin-Bush 2023, PRA 108:L060201] "Misinference of interaction-free measurement from a classical system" 在 hydrodynamic pilot-wave 系统 demonstrated:

- 7.0 mm silicon oil bath · 80 Hz vibration · walking droplet self-propelled by its own pilot wave
- 实测 droplet **25% chance** of detection on right side when "bomb" present on left · 跟 EV 量子 IFM 25% 等价

这意味着我们 §03.7 R1/R2/R3 differentiator claim 在 **single bomb tester 规模** 不严格成立 · 必须 caveat:

- **Single IFM (R1 性质)** · 经典 hydrodynamic pilot-wave 可以模拟同一 statistics
- **Chained Zeno (Kwiat 1995, N≥6)** · 经典不可 (任意 scale nonlocal wavefunction 必需)
- **Multi-object IFM (Franco 2026, N≥5)** · 经典不可 (全局 entangled probe state 必需)

Frumkin-Bush 2023 提议的 falsification 实验:延长 interferometer arm length nλ · 看 effect 是否 persist。这是物理学界 open question · 我们论文 not affected · 因为应用 niche 都在 chained / multi-object 规模 (N≥2)。

诚实 disclaimer:**单 IFM 的 R1 "quantum-only" 论点是 contested in physics community** · 但 chained / multi-object IFM 的 R1/R2/R3 仍 quantum-only (跟 [Hance-Ladyman-Rarity 2021] "How Quantum is QCC?" Foundations of Physics 51:12 一致)。

### 核心瓶颈总结

loss + visibility + heralding 三者共同决定 effective $N$ 上限。当前 multi-object IFM 实测 $N = 5$ (Franco 2026) · chained CFC 实测 $N = 6$ (Calafell 2019)。两者都 **6 倍以内**于 12-mode platform capability · 但 **指数 / 多项式倍**远于很多算法理论上要求的 $10^6+$。

### 跟早期论文 §03.9 / §05.3 数字的 reconciliation

| 早期 claim | 实测对账 | 论文修订 |
|---|---|---|
| "N=12 lab proven" | N=12 是 Ascella platform mode 数 · multi-object IFM 实测 N=5 | §03.9 重写 (已完成) · 区分 hardware capability vs IFM object 数 |
| "5 dB end-to-end loss" | 3 dB per facet · 系统总 efficiency ~2.7% | §03.9 重写 (已完成) |
| ">99% efficiency 单链路" | single MZI visibility 99.94% · 不是 chained protocol success | §03.9 重写 (已完成) · 区分单 MZI vs chained |

## 11.3 · 应用层限界

§9.4 的 5 个反模式 + 决策树 (§9.5) 是应用层"什么时候不该用 CFE"的精炼。

总结性原则:**CFE 只适合"oracle 是物理对象 + 评估有副作用 / 隐蔽性 / 不消耗需求"的问题**。强行套到不符合条件的问题上 · 100% 失败。

## 11.4 · 范式层限界

减法计算范式 (§6) 本身有局限:

- **数学基础不严格** · "subtractive" 作为范畴尚无公理化定义
- **没有原生编程语言** · 当前都是 mental model + 算子组合表达 · 没有 native 工具链支持
- **设计模式集稀疏** · 6 个模板 (§8) 远远不够 · 类比 GoF 23 个 patterns 是目标 · 我们差很远
- **教育空白** · 没有教材 · 没有课程 · 没有培训路径 · 算法学家需要重新训练

## 11.5 · 元层警示 · 不要 hype 自己

容易犯的 hype 错误:

- ❌ "我们超越未来 FT QC" → 不正确 · D1 上 FT QC 是超集 (§5.2)
- ❌ "我们解决了量子计算的关键问题" → 不正确 · 我们解决一个 niche 子集
- ❌ "我们的算子能加速任何问题" → 不正确 · 仅 sparsity / side-effect / verify-without-commit 类
- ❌ "光子计算的革命" → 不正确 · 我们是 specialized co-processor · 不是 universal photonic computer
- ❌ "FT QC 不再必要" → 不正确 · A2/A3/A5 之外的大量问题 FT QC 仍必须

应该说的:

- ✅ "我们用专用硬件提前解锁了一个 quantum-only 算子"
- ✅ "我们独占 FT QC 永远到不了的 interface domain"
- ✅ "我们提供 FT QC 也做不到的 adversary-undetectable 查询"
- ✅ "我们识别了 6 个具体可挑战问题 + 5 个诚实排除"

## 11.6 · 12 个开放问题 (研究路线图)

按主题分类:

### 算子代数层

**Q1 · 严格 cost composition theorem**:证明 §4.3 的上界 (或给 tight bound)。当前都是合理估计。

**Q2 · 嵌套深度上限**:在给定 $\delta_{\text{budget}}$ 下最多能嵌套多深?是否存在 lower bound 表明深度有本质极限?

**Q3 · 算子代数公理化**:能否给 $\Phi^{CF}$ 一组公理 (类似线性代数 / 关系代数) · 使所有 cost 定理可推导?

**Q4 · 等价性判定**:两个组合表达式 $E_1, E_2$ 等价 (输出分布相同 + 触发率相同) 是否可判定?

**Q5 · 最优编译**:给定算法 expression · 找成本最小的等价表达式 (compiler optimization)。

### 跟其他范式的 interop

**Q6 · 跟标准量子电路的 interop**:能否在 quantum circuit 中嵌入 $\Phi^{CF}$ 作为 sub-routine? 如果可以 · 跟 standard quantum query 怎么 hybrid?

**Q7 · 类型系统设计**:Linear types / affine types / 量子专用 type system 哪个更合适?

**Q8 · 跟 indefinite causal order (ICO) 的组合**:ICO-aware CFE 算子有意义吗?

### 复杂度理论层

**Q9 · CFP 复杂度类**:CFP (§7.7 定义) 跟 BQP 的关系是什么?是否严格子集?是否等价?

**Q10 · Disturbance / observability 复杂度的下界**:对 specific $f$ · $D_\Delta(f)$ 和 $\eta(f)$ 的紧致下界是什么?

### 范式层

**Q11 · 减法计算的形式化**:能否把 SCP 作为正式范畴 · 跟 quantum measurement theory 的形式关系?

**Q12 · 减法编程语言**:第一个真正 native 支持减法计算的语言怎么设计?

## 11.7 · 跨学科开放问题

不属于本论文核心但相关:

- 减法范式跟 free will / counterfactual definiteness 的哲学讨论
- 减法范式在认知科学中的对应 (人脑是否做反事实推理 in subtractive way?)
- 跟 [Pearl 因果反事实](https://en.wikipedia.org/wiki/Causal_inference) 框架的整合可能
- 跟 information theory 的 Landauer principle / 可逆计算 [Bennett 1973] 的关系

## 11.8 · 工程层开放问题

- 大规模 photonic IFM chip 设计 (N > 100) 的架构
- Active stabilization for phase drift in deep interferometers
- 室温 single-photon detector with > 90% efficiency
- 跟经典 CMOS 系统的 interconnect 标准化
- 编程框架 / 编译器 / 调试器工具链
- 测试方法学 (怎么 unit test 反事实算法?)

## 11.9 · 商业层开放问题

- 真实客户访谈验证 (A2 / A5 / A4 客户到底要不要?)
- 监管路径 (FDA / FCC / 各国军方对 IFM-based 产品的审批)
- 标准化 (CFE 算子作为 quantum SDK 中的标准 primitive?)
- 跟 PsiQuantum / Xanadu / ORCA 等量子公司的合作/竞争策略
- IP 战略 (核心专利布局)

## 11.10 · 小结

CFE 算子体系 + SCP 范式是**起点而非终点**。本论文给出 12 个开放问题 + 跨学科 + 工程 + 商业 4 个层次的延伸方向 · 任一方向都值得一篇专门论文或一个工程项目。

诚实的结语:**我们做了 abstraction · 没做硬件 · 没做客户访谈 · 没做严格证明**。本论文是综合框架 · 后续工作可以填充每个空白。

---

[← 上一章 · 10 6 个挑战问题](10-six-challengeable-problems.md) · [下一章 · 12 结论 →](12-conclusion.md)
