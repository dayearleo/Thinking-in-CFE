# AUD-E-014 · Assessment

## status: **REFUTED** ⭐ (严重 attribution 错误)

## 推理链

1. 我们论文 §02 prior-art / §03 / §10 / 多处引 `[Hance 2025]` 指 "universal integrated photonic processor multi-object IFM lab proven"
2. 实际查 arxiv 2604.04691 · 作者是 **Sara Franco · Anita Camillini · Ernesto F. Galvão** · 不是 Hance
3. 实际 submission date 是 **2026-04-06** · 不是 2025
4. 实际 platform 是 **Quandela Ascella** cloud · 实验 5 objects sequential · 不是 N=8-12 直接 parallel
5. Hance 真实 2019/2025 工作是别的主题 (nanophotonic comm / contextuality)

## 这是严重 attribution 错误

### 影响范围

我们 paper 至少以下处引 `[Hance 2025]`:

- `00-abstract.md` (核心论点)
- `01-introduction.md` (history line)
- `02-prior-art.md` (theoretical + experimental line · 多处)
- `03-operator-formal-definition.md` (物理实现指针 §3.9)
- `10-six-challengeable-problems.md` (lab proven 论据)
- `12-conclusion.md`
- `13-validation-and-rfc.md`
- `14-breakthrough-demonstration.md`
- `99-references.md` (refs entry)

每处都要修。

### Reviewer-killing risk

如果论文 submit 不改这个 · reviewer 一查 arxiv 2604.04691 就发现作者跟我们 cite 完全不对 · 论文直接被拒。**这是论文里最危险的一类错误**。

## 触发的修订动作 (P0 必须做)

### 1 · 全文替换 attribution

`[Hance 2025]` → `[Franco-Camillini-Galvão 2026]` (在 universal photonic processor multi-object IFM 上下文中)

### 2 · 修 99-references.md

加正确 entry:

```
[Franco-Camillini-Galvão 2026] Sara Franco, Anita Camillini, Ernesto F. Galvão.
"Interaction-free measurement of multiple objects using a universal integrated photonic processor."
arXiv:2604.04691 [quant-ph], April 2026.
Experimental implementation on Quandela Ascella photonic processor (cloud).
Sequential IFM up to 5 objects with single photon. 16 pages, 18 figures.
DOI: https://doi.org/10.48550/arXiv.2604.04691.
```

并保留 `[Hance 2019]` 作为 Calafell et al. 真实 nanophotonic comm 工作 cite (检查 §02 prior-art 是否要单列这一条):

```
[Hance 2019] Calafell, Strömberg, Arvidsson-Shukur, Rozema, Saggio, Greganti,
Harris, Prabhu, Carolan, Hochberg, Baehr-Jones, Englund, Barnes, Walther, Hance.
"Trace-free counterfactual communication with a nanophotonic processor."
npj Quantum Information 5(61) 2019. DOI: 10.1038/s41534-019-0179-2.
```

### 3 · 修内容描述

凡是说 "N=8-12 universal photonic processor lab proven" 必须改为:

> "N=5 sequential IFM on Quandela Ascella photonic processor (cloud) [Franco-Camillini-Galvão 2026] · 单 photon · 5 objects sequential"

这跟我们之前声称的 "N=12 universal photonic processor end-to-end 5 dB loss" 数字 (§03.9) **可能不准** · 需要再 audit · 因为 5 不等于 12 · 而且 sequential 不等于 parallel。

涉及的 claim:**AUD-C03-015**, **AUD-C03-016** 也得重审 (跟物理 SOTA 数字声明耦合)。

### 4 · 加新 audit task

`AUD-C03-015` (N=12 universal photonic processor lab proven) 因本 audit 发现需要重新 evaluate · 在 registry 标 PARTIAL/REFUTED 待审。

## 证据强度

⭐ (1 星 REFUTED · 但 REFUTED 本身的证据强度很高 · 因为 arxiv 元数据是 ground truth)

## search-log 简略

- EXA query: `Hance counterfactual integrated photonic chip 2025 universal processor multi-object`
- Top 8 hits 中:
  - hit 1 是 arxiv 2604.04691 (我们引为 [Hance 2025] 的 paper · 实际作者 Franco/Camillini/Galvão · 2026)
  - hit 2 是 arxiv 2505.14119 Hance 真 2025 工作 · 主题 quantum contextuality
  - hit 3 是 npj 2019 Calafell + Hance trace-free comm
  - 没有任何 paper 标题含 "universal photonic processor" 作者是 Hance

确认我们 attribution 是错的 · 不是 EXA 漏 paper。

## 元层

- M1 ✓ 找到 Gap (REFUTED 级)
- M2 ✓ 主要 Novelty 维度 (attribution 是否准)
- M3 ✓ arxiv 元数据是不可伪造证据
- M4 N/A

## 给后续审计的 lessons

1. **所有 attribution claim 都要直接抓 arxiv abstract 看作者列表** · 不能只看 EXA snippet
2. **不要凭 paper 内容描述匹配就 assume 作者** · 内容可能 match · 作者完全不一样
3. **`[Hance 2025]` 这类 attribution 必须实际去 verify** · 因为 Hance 不是唯一活跃在 IFM 领域的人
4. arxiv 提交日期 (2026-04) 比 Lin-Lin 2014 → 2015 这种 (preprint → conference 1 年差) 更明显 · 2026 不可能是 2025 cite
