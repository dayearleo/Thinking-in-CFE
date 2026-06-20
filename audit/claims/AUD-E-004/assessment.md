# AUD-E-004 · Assessment

## status: PARTIAL ⭐⭐⭐⭐

## 推理链

1. attribution `[Lin-Lin 2015]` 本身准 (CONFIRMED · 见 findings F1)
2. 但我们论文公式 $B_\delta(f) = O(Q(f)^2/\delta)$ 跟原文 $B(f) = \Theta(Q(f)^2)$ **不字面一致** (findings F3)
3. 我们做了 $\delta$ 参数化 extension · 这是合理 model 扩展 · 但**论文没明确说**是 extension
4. 2025 follow-up 全部用原版 · 没人做 $\delta$ extension · 所以这是我们独立加的

## 证据强度

⭐⭐⭐⭐ (4 星) · attribution 强 · 但 extension 没明确化导致 PARTIAL

## 触发的后续动作

### 修论文 (P0 必做)

§03.2 P3 必须明确说 "这是 Lin-Lin model 的 $\delta$ 参数化 extension" · 草稿见 `findings.md` § 建议修订

§07 复杂度章节同步检查 · 是否也用了 $B_\delta$ 而未说 extension · 若是 · 也得改

### 加 prior-art 防御 (P1)

`audit/06-novelty-defense.md` 应加一条:

> "$\delta$ 参数化 bomb query complexity $B_\delta(f) = O(Q(f)^2/\delta)$ 是我们对 Lin-Lin 2015 model 的小幅 extension · 引入 trigger probability 作为显式参数 · 在 $\delta \to 0$ 极限下还原 Lin-Lin 原版 $\Theta(Q(f)^2)$。截 2025-10 · 跑 EXA + Serper · 未发现独立同样 extension · 算我们 incremental novelty。"

### 加 reference (P0)

更新 `paper/thinking-in-cfe/99-references.md` 中 [Lin-Lin 2015] entry:

```
[Lin-Lin 2015] Cedric Yen-Yu Lin and Han-Hsuan Lin.
"Upper bounds on quantum query complexity inspired by the Elitzur-Vaidman bomb tester."
arXiv:1410.0932 [quant-ph], Oct 2014 (revised Nov 2014).
CCC 2015 · LIPIcs.CCC.2015.537.
Theory of Computing, Vol 12 Article 18 (2016), pp. 1-35.
DOI: 10.4086/toc.2016.v012a018.
```

(确认引用元数据精确化 · 之前 §99 可能简写)

## 元层 self-audit

- M1 ✓ 找了 Gap (公式 extension 没明确说)
- M2 部分 ✓ 跑了 Novelty + Math · Physics + Differentiation 简化跳过 (claim 是数学 attribution 类 · physics 维度不重要)
- M3 ✓ source/ 含 Jina 抓的全文 · 关键引用段 verbatim
- M4 N/A (我们只审 1 个 claim · 不是全 230)

## 给后续审计的 lessons

1. attribution 不是 "存不存在 paper" · 还要看 "我们公式跟原文一致吗"
2. 把数学 extension 标 explicit · 防 reviewer 抓 attribution
3. EXA + Jina 组合够用 · Serper 这次没必要 (只跑 attribution audit)
4. 近 12 月查询很有价值 · 看 active follow-up 工作
