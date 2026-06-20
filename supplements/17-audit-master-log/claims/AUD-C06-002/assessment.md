# AUD-C06-002 · Assessment

## Claim 速述

"Subtractive Computation Paradigm (SCP)" 是我们提出的新计算范式名 · 跟传统加法计算正交。

## status: NOVEL ⭐⭐⭐⭐

## 推理链

1. EXA 搜 `subtractive computation paradigm algorithm framework` · 8 hits
2. 8 hits 中 0 个对应我们的语义 "用 CFE 算子做 subtractive (反事实) 算法构造范式"
3. 邻近 hits 分布:
   - "Sublinear computation paradigm" (Springer 2021) — 不同概念
   - "Subtractive design in social robotics" (Irtolo) — 哲学/设计
   - "Subtractive mixture models" (Loconte et al. 2023) — ML probabilistic
   - "Subtraction-free complexity" (Fomin 2013) — algebraic complexity (最近概念但不同)
4. 我们 §06.1 已 disambiguate 4 类邻近用法 (LLM / 心理学 / ML explainability / 因果) · 搜索 confirm 这 4 类确实存在 · 但都不是 "subtractive computation paradigm" 这个 phrase

## 证据强度

⭐⭐⭐⭐ (4 星 NOVEL) · 强证据 · 但要 caveat:

- "Subtraction-free complexity" (Fomin 2013, arxiv 1307.8425) 是 algebraic complexity 子领域 · 不是直接撞名但概念邻近 · 应该 §02 prior-art 加 disambiguation
- "Subtractive mixture models" 在 ML 是已知 phrase · 我们 §06.1 disambiguate 但 wording 可强化

## 触发动作

1. P0 · §02 prior-art 加 "Subtraction-free complexity (Fomin 2013)" 作为 5th 类邻近 disambiguation (algebraic complexity)
2. P1 · `06-novelty-defense.md` 应加防御:"Subtractive Computation Paradigm" 在量子算法/反事实计算语境下没人用过的搜索证据 (本次审计的 8 个 hit list)
3. P0 · 论文 §06.1 disambiguation 加 algebraic complexity 那一类 (现版本只 4 类)

## search-log 简略

- EXA query: `subtractive computation paradigm algorithm framework`
- Top 8 全部不撞我们的 phrase 语义
- 中文查询 (跳过 · "减法计算" 是直译 · 中文社区无独立来源)

## 元层

- M1 ✓
- M2 ✓ Novelty 重点
- M3 ✓ 8 hits source 列在 search-log
- M4 N/A
