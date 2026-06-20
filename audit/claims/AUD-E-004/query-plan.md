# AUD-E-004 · Query Plan

## 4 类 query 设计

### N1 · Novelty 查 (谁先做了?)

- 英:`"Lin" "bomb query" complexity 2015`
- 英:`bomb query complexity Q(f)^2 quantum`
- 中:`炸弹查询 复杂度 林`

目标:确认 Lin & Lin 2015 是首次提出 bomb query 复杂度的 paper · 还是在引别人的工作。

### N2 · Math 查 (复杂度精确公式)

- 英:`bomb query Lin Lin 2015 quantum query complexity Theta`
- 英:`B(f) = O(Q(f)^2) bomb query`
- 英:`interaction-free measurement query complexity`

目标:核对公式 $B(f) = \Theta(Q(f)^2)$ 的精确陈述 · 看是 $O$ / $\Theta$ / $\Omega$ · 看是否带 $\delta$ 因子。

### N3 · Physics 查 (这个声明在物理上有什么 caveat?)

- 英:`bomb query model physical realization`
- 英:`Elitzur-Vaidman bomb tester complexity`

目标:看 Lin-Lin 模型跟物理实现的关系 · 是否要求 $\delta = $ 某个固定值。

### N4 · Differentiation 查 (跟其他相关 complexity 怎么比?)

- 英:`bomb query vs adversary bound quantum query`
- 英:`Belovs span program bomb query`

目标:看是否有其他 query model 对应同一 capability · 防 attribution 撞名。

## 必跑组合

每个 query 跑:

1. EXA all-time
2. EXA after 2024-12
3. Serper Scholar
4. (可选) arxiv API

英文优先 (Lin & Lin 2015 是英文 paper) · 中文跑 N1 看是否被中国密码学/量子信息社区翻译/引用。

## 预期产物

- 至少 5 个相关 source (Jina 抓全文)
- 至少 1 个 Lin & Lin 2015 paper 直接 link
- 公式精确陈述截图 / 引用段
