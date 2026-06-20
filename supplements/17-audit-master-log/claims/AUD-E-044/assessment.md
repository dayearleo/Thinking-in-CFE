# AUD-E-044 · Assessment

## Claim 速述

[Yang 2026] "Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning" arxiv:2602.18232 · 用于 §02/§06 "subtractive" disambiguation。

## status: **REFUTED** ⭐ (attribution 错误 · 第 1 作者不是 Yang)

## 推理链

1. 论文 4 处引 `[Yang 2026]`:§01 L35 · §02 L64 · §06 L11 · §99 L125
2. Jina 抓 arxiv 2602.18232 · 真实作者列表:
   - **Lexiang Tang** (第 1 作者 · 实际应 cite)
   - Weihao Gao
   - Bingchen Zhao
   - Lu Ma
   - Qiao jin
   - **Bang Yang** (第 6 作者)
   - Yuexian Zou
3. arxiv 2602.18232 真实信息:
   - 标题:"Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning" ✓ (跟我们引一致)
   - 提交日期:2026-02-20
   - 类别:cs.CL (Computation and Language)
4. 学术 cite 标准是用**第 1 作者** · 应该是 `[Tang 2026]` 或 `[Tang et al. 2026]` · **不是** `[Yang 2026]`

## 严重程度

这是第 2 个 reviewer-killing attribution 错误 (跟 AUD-E-014 `[Hance 2025]` 同类问题):

- reviewer 一查 arxiv 立刻发现作者不对
- 我们在 §06 减法计算 disambiguation 关键段引这篇 · 错的 attribution 等于削弱整个 disambiguation 论证

## 触发动作 (P0 必做)

### 1 · 4 处替换 attribution

`[Yang 2026]` → `[Tang et al. 2026]` 全文 replace

`paper/thinking-in-cfe/`:
- 01-introduction.md L35
- 02-prior-art.md L64
- 06-subtractive-paradigm.md L11
- 99-references.md L125

### 2 · 修 99-references.md entry

```
[Tang et al. 2026] Lexiang Tang, Weihao Gao, Bingchen Zhao, Lu Ma, Qiao jin, Bang Yang, Yuexian Zou.
"Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning."
arXiv:2602.18232 [cs.CL], Feb 2026.
```

### 3 · 这次发现的 meta-lesson

第二个 attribution 错误 · 模式跟 AUD-E-014 一致:**作者列表里有多个名字时 · 我们选错了人当 cite key**。

可能原因:论文写作时 · 凭印象记 "Yang" 因为 6 个作者之一 · 但没回查第 1 作者。

应该在 audit 完成后跑 grep 检查 §99 所有多作者 cite · 确认每个都用第 1 作者作为 cite key。

## 证据强度

⭐ (1 星 REFUTED) · arxiv 是 ground truth

## search-log 简略

- EXA: `Yang 2026 counterfactual quantum computation photonic` → 0 hits 匹配我们 cite
- Jina: arxiv 2602.18232 全文 → 作者列表 ground truth
