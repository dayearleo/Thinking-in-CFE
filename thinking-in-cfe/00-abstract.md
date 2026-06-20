# 00 · 摘要

[← 返回 README](README.md)

> *"We are participators in bringing into being not only the near and here but the far away and long ago."*
> — John Archibald Wheeler, 1978

本工作的**思想起航起点**是 Wheeler 1978 延迟选择思想实验 [Wheeler 1978] 提出的 **"participatory universe"** 哲学命题 — 物理实在的内容由测量配置决定 · 而不由写入时机决定。

我们沿这一哲学起源 · 把 Elitzur-Vaidman 1993 干涉无相互作用测量 [Elitzur-Vaidman 1993] 与 Mitchison-Jozsa 2001 反事实计算 [Mitchison-Jozsa 2001] 的物理思想抽象为可工程化的算法原语 **反事实函数求值算子** $\Phi^{CF}_f$ (Counterfactual Function Evaluation Operator · **CFE**)。

(*Wheeler ↔ CFE 是 **哲学/概念 lineage** · 不是 **物理实现 lineage** · 详 §02 prior-art + audit/THEORY-ADJUSTMENTS-MASTER-REPORT.md 的 3 层 honest disclaimer。*)

算子定义于三条性质:

- **(P1) 正确性**:输出 $y$ 满足 $\Pr[y = f(\mathbf{x})] \geq 1 - \epsilon$
- **(P2) 反事实性**:对 $x_i = 1$ 的 oracle, 物理触发概率 $\leq \delta$ (参数可调)
- **(P3) 代价上界**:$B_\delta(f) = O(Q(f)^2/\delta)$,其中 $Q(f)$ 是标准量子查询复杂度 [Lin-Lin 2015]

在算子之上,我们建立 **5 种组合规则** (串行 / 并行 / 嵌套 / 条件 / 迭代),推导对应的代价合成定理草案,提出 **减法计算范式** (Subtractive Computation Paradigm,简称 **SCP**) —— 一个跟传统加法计算正交的算法构造哲学:算法的输出由 "**没发生的事件**" 决定,而不是 "发生的事件"。

我们论证 CFE 算子跟 fault-tolerant 量子计算 (FT QC) 的关系沿 3 个独立维度:

- **D1 capability** (能算什么):FT QC 是 CFE 的超集
- **D2 cost** (硬件成本):CFE 比 FT QC 实现同一 capability 便宜约 6 个数量级
- **D3 interface domain** (oracle 来源):**CFE 永久独占** —— 外部物理 oracle 是 FT QC 永远到不了的范畴

基于 D3 独占性,我们识别出 6 个**原本被认为需要 FT QC 才能解决**的问题,我们当下用 photonic IFM 硬件即可挑战 (单细胞多 assay 检测 / 物理对抗 stealth 探测 / 半导体晶圆缺陷扫描 / 稀有资源勘探 / NAND-tree 评估 / 光毒性显微分类),并诚实排除 5 类不可挑战的问题 (Shor / 量子化学 / HHL / 量子机器学习训练 / boson sampling)。

我们提出 **5 步问题代数化方法论** + **7 题决策树** + **5 个反模式**,让领域专家不必懂量子光学就能判断自身问题是否适合 CFE 重构。

本文核心论点:

> CFE 算子是 **quantum-only** 的能力 (在 chained Zeno + multi-object IFM 规模 · single bomb tester 规模的 quantum-only 论点是 contested in physics community · 详 §11.2 CAVEAT 6) · 但用**远小于 FT QC** 的硬件代价实现 · 且独占 FT QC 永远到不了的 **external physical oracle** interface domain · 在 **N ≤ 10 multi-object IFM 规模**上把一个原本被认为属于"未来量子计算"的 capability 提前 10-20 年解锁 (N=100+ 规模仍需未来 photonic chip 工艺突破)· 在 6 个具体问题域形成永久或临时的不可替代位置。

本文不是物理论文 (我们不发明新物理) · 是 **算法-工程-应用** 的抽象与综述论文 · 第一次把 30 年分散的 IFM / counterfactual computation 文献系统化为可被算法学家与行业专家直接调用的工具集。

---

[下一章 · 01 引言 →](01-introduction.md)
