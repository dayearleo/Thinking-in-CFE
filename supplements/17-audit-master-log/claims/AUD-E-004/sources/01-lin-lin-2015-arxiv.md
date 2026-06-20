# Source 01 · Lin-Lin 2015 arxiv abstract page

- **URL**:https://arxiv.org/abs/1410.0932
- **抓取时间**:2026-06-20 EDT
- **工具**:Jina r.jina.ai

## 关键 metadata

- Title: "Upper bounds on quantum query complexity inspired by the Elitzur-Vaidman bomb tester"
- Authors: Cedric Yen-Yu Lin, Han-Hsuan Lin
- arXiv: 1410.0932 [quant-ph]
- Submitted: 3 Oct 2014 (v1) · Last revised: 26 Nov 2014 (v2)
- Published in TOC: Volume 12 (18), 2016, pp. 1-35 · CCC 2015
- DOI: https://doi.org/10.48550/arXiv.1410.0932
- Report number: MIT-CTP/4592

## 原文 abstract 完整摘录

> Inspired by the Elitzur-Vaidman bomb testing problem [arXiv:hep-th/9305002], we introduce a new query complexity model, which we call bomb query complexity B(f). We investigate its relationship with the usual quantum query complexity Q(f), and show that **B(f)=Θ(Q(f)²)**.
>
> This result gives a new method to upper bound the quantum query complexity: we give a method of finding bomb query algorithms from classical algorithms, which then provide nonconstructive upper bounds on Q(f)=Θ(√B(f)). We subsequently were able to give explicit quantum algorithms matching our upper bound method. We apply this method on the single-source shortest paths problem on unweighted graphs, obtaining an algorithm with O(n^1.5) quantum query complexity, improving the best known algorithm of O(n^1.5·√log n) [arXiv:quant-ph/0606127]. Applying this method to the maximum bipartite matching problem gives an O(n^1.75) algorithm, improving the best known trivial O(n^2) upper bound.

## 关键对账点

| 论文写法 | 原文写法 | 差异 |
|---|---|---|
| $B_\delta(f) = O(Q(f)^2/\delta)$ | $B(f) = \Theta(Q(f)^2)$ | (1) 我们加了 $\delta$ 参数;(2) $O$ 变 $\Theta$ |

## Lin-Lin 2015 模型本质

- 没有 $\delta$ 参数 · 隐含 $\delta \to 0$ 极限 ($B(f)$ 是 "no-trigger" 极限下的代价)
- $\Theta$ (tight bound) · 我们写 $O$ 是 weaker statement (上界)

## 应用 contribution

Lin-Lin 2015 用此 bound 改进了 2 个具体 quantum query 问题的上界:

- Single-source shortest paths · $O(n^{1.5})$ vs prior $O(n^{1.5}\sqrt{\log n})$
- Maximum bipartite matching · $O(n^{1.75})$ vs prior trivial $O(n^2)$

— 这是 bomb query 模型的实用价值证明 · 不只是理论 framework。
