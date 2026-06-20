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

## 11.2 · 硬件层限界

当前 SOTA (2024-2025) 的硬件参数:

| 维度 | 当前可达 | 限制因素 |
|---|---|---|
| Photonic mode 数 $N$ | $\leq$ 12-32 集成 universal | 累积 loss / phase 漂移 / fab 良率 |
| End-to-end loss | $\sim$ 5 dB (12-mode SiN) | 在 N=100 累积成 $\sim 50$ dB 不可用 |
| Counterfactual efficiency | 单链路 $> 99\%$ · 多对象 $\sim 75\%$ | Zeno 阶数有限 |
| Visibility (干涉对比度) | $> 95\%$ on chip | $\delta$ 下限由 visibility 限制 |
| 工作温度 | SNSPD 需 cryogenic 1-4 K | 探测器替代品 SPAD 效率掉 30-50% |
| Photon source 速率 | 1-100 MHz | 不是瓶颈 |
| 切换速度 (EAM) | GHz | 不是瓶颈 |

**核心瓶颈**:loss + visibility · 决定 $N$ 上限 · 当前 $N$ 上限约 30-50 在实物可行 · 远低于很多算法理论上要求的 $10^6+$。

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
