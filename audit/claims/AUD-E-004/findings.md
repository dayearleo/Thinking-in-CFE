# AUD-E-004 · Findings

## 关键发现

### F1 · Lin-Lin 2015 paper 存在且 attribution 准确

- 原 arxiv: 1410.0932 (2014-10 submitted · 2014-11 revised)
- 出版:
  - **CCC 2015** (LIPIcs.CCC.2015.537) · 30th Conference on Computational Complexity
  - **Theory of Computing (TOC)** Vol 12 Article 18 (2016) pp. 1-35
- 作者:Cedric Yen-Yu Lin · Han-Hsuan Lin (MIT Center for Theoretical Physics)
- 时间:虽 arxiv 是 2014 · 但 conference 接收 + 引用约定按 2015 (CCC 2015)
- DOI:`10.4086/toc.2016.v012a018`

### F2 · 模型核心 claim:$B(f) = \Theta(Q(f)^2)$

原文 abstract verbatim:

> "we introduce a new query complexity model, which we call bomb query complexity B(f). We investigate its relationship with the usual quantum query complexity Q(f), and show that **B(f)=Θ(Q(f)²)**."

注意:

- **没有** $\delta$ 参数
- 是 $\Theta$ (tight bound) · 不是 $O$ (上界)
- 隐含的物理 model:trigger 概率 → 0 极限

### F3 · 我们论文写法跟原文有差异

我们 §03.2 P3 写:

$$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$

vs Lin-Lin 原文:

$$B(f) = \Theta(Q(f)^2)$$

**差异 2 处**:

| 维度 | Lin-Lin 2015 原文 | 我们 §03.2 |
|---|---|---|
| 是否有 $\delta$ 参数 | 无 (隐含极限) | 有 (显式参数) |
| 紧度 | $\Theta$ (tight) | $O$ (upper bound) |

**论文里 attribution `[Lin-Lin 2015]` 是 correct** · 因为我们的 $B_\delta(f)$ 是 Lin-Lin 模型的**显式 $\delta$ 参数化扩展** · 不是 Lin-Lin 原始公式。

但论文**没明确说**我们做了 extension · 容易被 reviewer 抓:"你引 Lin-Lin 但公式跟原文不同 · 哪里 cite 的扩展?"

### F4 · 2025 后续工作的 cite 状态

跑 search 2:

- Quantum Journal 2025-06 follow-up 直接 cite Lin-Lin 2015 (DOI 10.4086/toc.2016.v012a018)
- 综述 2025-08 也 cite
- 但所有 2025 工作都用**Lin-Lin 原版** $B(f) = \Theta(Q(f)^2)$ · **无人**做我们这种 $\delta$ 参数化 extension

### F5 · 应用 contribution

Lin-Lin 2015 用 bomb query bound 改进:

- single-source shortest paths · $O(n^{1.5})$ vs prior $O(n^{1.5}\sqrt{\log n})$
- maximum bipartite matching · $O(n^{1.75})$ vs prior trivial $O(n^2)$

这些是 query complexity theory 的实用 contribution · 跟我们论文 §10 A1 "NAND-tree 评估" 的 lineage 一致 · 都是用 bomb-style bound 改进 query problem。

## 跟论文 claim 的对账

| 论文声明 | 审计结果 |
|---|---|
| 存在 [Lin-Lin 2015] paper | ✅ CONFIRMED · arxiv 1410.0932 + TOC 12-18 |
| paper 提出 "bomb query complexity" model | ✅ CONFIRMED · 原文 verbatim |
| $B(f)$ 跟 $Q(f)^2$ 同阶 | ⚠️ PARTIAL · 原文是 $\Theta$ · 我们写 $O$ · 公式形式 strict 不同 |
| 我们 $B_\delta(f) = O(Q(f)^2/\delta)$ 公式直接来自 Lin-Lin | ❌ REFUTED · 我们加了 $\delta$ 参数 · 是 extension · 但论文没明确说 |

## 跟其他相关 model 的差异化

- **Adversary bound** (Ambainis 2000, Belovs 2012) · lower bound technique · 跟 bomb query 互补
- **Polynomial method** (Beals et al. 2001) · 另一 lower bound 技术
- **Span program** (Reichardt 2009) · 给 quantum query 紧 bound

Bomb query 在这些技术里**独特**之处:它专门做 *upper bound* (给 bomb 算法 → 翻译成量子算法) · 不是 lower bound。

## 建议给论文的修订

§03.2 P3 改写为:

> **(P3) 代价上界**:实现 $\Phi^{CF}_f$ 需要的总 oracle 调用次数:
> $$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$
> 其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度。**注:这是把 [Lin-Lin 2015] 的 $\delta \to 0$ 极限模型 $B(f) = \Theta(Q(f)^2)$ 显式参数化为 $\delta$-trigger 上界的 extension · 跟原 Lin-Lin 模型在 $\delta \to 0$ 极限下重合。** Lin-Lin 模型本身见 [arXiv:1410.0932, CCC 2015, ToC 12 (18) 2016]。
