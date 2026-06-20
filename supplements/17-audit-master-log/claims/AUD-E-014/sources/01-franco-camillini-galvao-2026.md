# Source 01 · arxiv 2604.04691 真实作者与元数据

- **URL**: https://arxiv.org/abs/2604.04691
- **抓取时间**:2026-06-20 EDT (via Jina)
- **真实作者**:**Sara Franco** · **Anita Camillini** · **Ernesto F. Galvão**
- **机构**:International Iberian Nanotechnology Laboratory (INL) · Centro de Física, Universidade do Minho
- **Submitted**:2026-04-06 (v1)
- **Title**:"Interaction-free measurement of multiple objects using a universal integrated photonic processor"
- **arXiv DOI**:https://doi.org/10.48550/arXiv.2604.04691

## Abstract verbatim

> "The phenomenon of interaction-free measurement (IFM) enables the probabilistic detection of an absorbing object with reduced photon absorption. We report the experimental implementation of a simultaneous IFM of multiple objects using a single quantum probe on the cloud-based Ascella photonic processor of company Quandela. We demonstrate sequential IFM of up to 5 objects using a single photon, significantly extending the original IFM scheme for a single object. The experimental error-mitigated results confirm the theoretical predictions for this sequential IFM setup, and demonstrate a practical approach to scaling IFM to more complex quantum interrogation tasks."

## 跟我们论文 claim 对账

| 我们论文写法 | 实际 paper 信息 | 差异 |
|---|---|---|
| `[Hance 2025]` | 真实作者 **Franco-Camillini-Galvão** · 年份 **2026** | **作者完全错 · 年份错** |
| "universal integrated photonic processor" | ✓ paper 标题确实含此短语 | 内容描述准 |
| "multi-object IFM" | ✓ "simultaneous IFM of multiple objects" · "up to 5 objects" | 内容准 |
| "lab proven N=8-12" 类声明 | paper 是 "up to 5 objects" 在 Quandela Ascella cloud | 我们可能误推 N 数值 |

## 真实的 [Hance] 工作 (用于澄清)

Jonte R. Hance (Newcastle University) 在 2019 和 2025 都有相关工作:

- **Hance 2019**: "Trace-free counterfactual communication with a nanophotonic processor" (Calafell et al. 含 Hance · npj Quantum Info)
- **Hance 2025**: "Quantum Contextuality Requires Counterfactual Gain" arxiv 2505.14119 (Yuki Sagawa + Jonte R. Hance + 其他 · 不是 universal photonic processor 主题)

我们论文引 `[Hance 2025]` 时混淆了 (i) Hance 的 2019 nanophotonic communication paper (ii) Franco-Camillini-Galvão 2026 universal photonic IFM paper (iii) Hance 2025 contextuality paper。

## 真实工作的 platform 细节

- **Quandela 的 Ascella** photonic processor (cloud-based)
- 单光子 sequential probe 5 个 objects
- 不是 N=8-12 · 是 N=5 (sequential mode)
- error-mitigated experimental result
- Quandela 是法国量子光子计算公司
