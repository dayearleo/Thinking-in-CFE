# AUD-E-010 · Assessment

## Claim 速述

[Hance 2019] trace-free counterfactual communication on nanophotonic processor。

## status: **REFUTED** ⭐ (第 3 个 cite key 错误 · 同模式 Hance/Yang)

## 推理链

EXA + Jina 抓 npj Quantum Information article s41534-019-0179-2:

- Title: "Trace-free counterfactual communication with a nanophotonic processor"
- 作者列表 (14 人 · 顺序):
  - **I. Alonso Calafell** (第 1 作者)
  - T. Strömberg
  - D. R. M. Arvidsson-Shukur
  - L. A. Rozema
  - V. Saggio
  - C. Greganti
  - N. C. Harris
  - M. Prabhu
  - J. Carolan
  - M. Hochberg
  - T. Baehr-Jones
  - D. Englund
  - C. H. W. Barnes
  - P. Walther
  - **Hance 不在 14 名作者列表中** (我搜的时候顺序混了一下 · 实际作者列表里 Hance 也可能是 contributor 但不是 listed author)

实际重新查 npj 全文:作者**仅 14 人 · 全部为 Calafell-Strömberg-Arvidsson-Shukur-Rozema-Saggio-Greganti-Harris-Prabhu-Carolan-Hochberg-Baehr-Jones-Englund-Barnes-Walther**。Hance **完全不是** 作者!

我之前的搜索 hit 上看到 "Walther, Hance" 其实是误读;npj entry 的 author 列表里没有 Hance · Hance 跟 Rarity 的 "Counterfactual Ghost Imaging" 2021 才是 Hance 的相关工作。

## 严重程度

第 3 个 cite key 错误。Pattern 升级:不仅是"多作者选错 key" · 还有"完全不是作者" 类。

## 触发动作 (P0)

### 1 · 论文 §02 prior-art 替换

`[Hance 2019]` → `[Calafell et al. 2019]` 全文 replace

### 2 · §99 entry 修正

```
[Calafell et al. 2019] I. Alonso Calafell, T. Strömberg, D. R. M. Arvidsson-Shukur, L. A. Rozema, V. Saggio, C. Greganti, N. C. Harris, M. Prabhu, J. Carolan, M. Hochberg, T. Baehr-Jones, D. Englund, C. H. W. Barnes, P. Walther.
"Trace-free counterfactual communication with a nanophotonic processor."
npj Quantum Information 5, 61 (2019). DOI: 10.1038/s41534-019-0179-2.
```

### 3 · meta-pattern 升级

batch 1+2 发现 Hance 2025 / Yang 2026 · batch 3 又发现 Hance 2019 · 都是 cite key 错。**AUD-meta-001 紧迫度升级 P0+** · 必须在审计完成前跑全 §99 audit。

可能凭"Hance 是 IFM 领域 active 学者"的印象错把"Calafell et al. 2019" cite 为 [Hance 2019] · 因为 Hance 2025 (实际是 Franco) 同样模式。
