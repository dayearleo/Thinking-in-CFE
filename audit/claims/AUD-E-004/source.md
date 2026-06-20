# AUD-E-004 · Source

## Claim 速述

[Lin-Lin 2015] 给出 bomb query 复杂度 $B(f) = \Theta(Q(f)^2)$ · 其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度。

## 来源 (file:line)

- `paper/thinking-in-cfe/00-abstract.md` (P3 代价上界引用)
- `paper/thinking-in-cfe/03-operator-formal-definition.md:39` (P3 定义引用)
- `paper/thinking-in-cfe/07-complexity-analysis.md:多处` (复杂度章节核心引用)
- `paper/thinking-in-cfe/99-references.md` (refs entry)
- `dev-notes/004-2026-06-19-反事实算子CFE形式定义.md` (起源)

## 原文摘录

> **(P3) 代价上界**:实现 $\Phi^{CF}_f$ 需要的总 oracle 调用次数:
> $$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$
> 其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度 [Lin-Lin 2015]。
>
> — §03.2 L35-39

## 类别 + 优先级

- 类:E · 历史归属 (但跟 C 复杂度强耦合)
- 优先级:P0
- 整个论文 P3 定义 + 复杂度章节 §07 全依赖此 attribution
