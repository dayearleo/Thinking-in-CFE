# AUD-E-004 · Search Log

## 查询 1 · EXA all-time

**Query**:`Lin Lin bomb query complexity 2015 quantum`
**时间**:2026-06-20 EDT
**引擎**:EXA `api.exa.ai/search`
**结果数**:10 hits

**Top 3 hits**:

1. arxiv 1410.0932 · Lin-Lin original paper
2. Theory of Computing v012a018 (2016) · journal version
3. drops.dagstuhl LIPIcs.CCC.2015.537 · conference version

所有 top 10 全部是同一 paper 的不同 hosting (arxiv / TOC / IIT Kanpur mirror / Chicago / researchr / QIP slides) · 表明这是 unique attribution · 没有 namesake/混淆。

## 查询 2 · EXA 近 12 月 cite 状态

**Query**:`bomb query complexity Lin 2015 cite 2024 quantum`
**时间**:2026-06-20 EDT
**引擎**:EXA · `start_published_date: 2024-01-01`
**结果数**:5 hits

**Top hits**:

1. Quantum Journal 2025-06-23 · "Improved Quantum Query Upper Bounds Based on Classical Decision Trees" · 直接 follow-up
2. Springer 2025-10 · "An Exponential Separation Between Quantum Query Complexity and the Polynomial Degree"
3. INSPIRE 2025-08 · "A Brief Introduction to Quantum Query Complexity" (综述)
4. INSPIRE 2025-10 · "Explicit relation between all lower bound techniques for quantum query complexity"
5. 同 1 的 Eindhoven 镜像

**关键**:Lin-Lin 2015 在 2025 仍是 active 文献 · 被 6 月 / 8 月 / 10 月最新 paper cite。

## 查询 3 · Jina 抓 follow-up Quantum 2025

**URL**:`https://quantum-journal.org/papers/q-2025-06-23-1777/`
**时间**:2026-06-20 EDT
**引擎**:Jina r.jina.ai

**关键发现**:cite 形式为:

```
Cedric Yen-Yu Lin and Han-Hsuan Lin. Upper bounds on quantum query
complexity inspired by the Elitzur–Vaidman bomb tester. Theory of
Computing, 12(1):1–35, 2016. doi:10.4086/toc.2016.v012a018.
```

`grep -iE "delta|trigger"` 在 2025 paper 全文中**未发现**带 $\delta$ 参数的 bomb query 变体 · 即 2025 工作仍使用 Lin-Lin 原版无 $\delta$ 的 $B(f) = \Theta(Q(f)^2)$。

## 跳过的查询

- 中文查询:跳过 · Lin-Lin 2015 是英文学术 paper · 中文社区主要做翻译综述 · 不影响 attribution accuracy
- (后续如需中文社区 reception 调查 · 单独 add audit)

## 总搜索成本

3 个 query · 1 个全文抓取 · ~5K token 输出
