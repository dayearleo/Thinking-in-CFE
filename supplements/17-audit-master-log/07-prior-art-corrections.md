# 07 · Prior-art Corrections · 论文 §02 + §99 修订建议

> 状态:230 claim 全审完成 · 本文件列出论文 prior-art / references 必修条目
> 修订优先级:P0 必修 (reviewer-killing) · P1 应修 · P2 nice-to-have

---

## P0 修订 (reviewer-killing · 必修)

### Correction P0-1 · 全文 attribution cite key (已完成 commit ab8aba4)

3 处 cite key 必全文 replace · 已完成:

| 原 cite | 改为 | 真实 paper |
|---|---|---|
| `[Hance 2025]` | `[Franco-Camillini-Galvão 2026]` | Sara Franco, Anita Camillini, Ernesto F. Galvão · arxiv 2604.04691 · 2026-04 |
| `[Yang 2026]` | `[Tang et al. 2026]` | Lexiang Tang et al · arxiv 2602.18232 · 2026-02 |
| `[Hance 2019]` | `[Calafell et al. 2019]` | I. Alonso Calafell et al · npj QI 5:61 · 2019 |

**实施**:commit ab8aba4 完成 22 处全文替换 + §99 3 entries author 字段更新 ✅

### Correction P0-2 · §99 references entry author 字段精确化 (已完成 commit ab8aba4)

3 entries author 字段从泛 "J. R. Hance et al." 改为完整作者列表:

- `[Calafell et al. 2019]`:14 author 完整列出
- `[Franco-Camillini-Galvão 2026]`:3 author + INL + Quandela Ascella 细节
- `[Tang et al. 2026]`:7 author + cs.CL category

**实施**:commit ab8aba4 ✅

### Correction P0-3 · §02 prior-art 加 [Noh 2009] CQC 子领域

§02 必须加 Counterfactual Quantum Cryptography (CQC) 17 年子领域:

```
**[Noh 2009]** · T.-G. Noh · "Counterfactual Quantum Cryptography" · 
Phys. Rev. Lett. 103, 230501 (2009) · DOI: 10.1103/PhysRevLett.103.230501

**[Yin 2010]** · Z.-Q. Yin, H.-W. Li, W. Chen, Z.-F. Han, G.-C. Guo · 
"Security of counterfactual quantum cryptography" · 
Phys. Rev. A 82, 042335 (2010)

**[Liu 2012]** · X. Liu et al. · 
"Eavesdropping on counterfactual quantum key distribution with finite resources" · 
Phys. Rev. A 90, 022318 (2014)

**[Counterfactual comm npj 2023]** · 
"Counterfactual communication without a trace in the transmission channel" · 
npj Quantum Information (2023) · doi:10.1038/s41534-023-00756-y
```

§15.9 加 PCC vs CQC disambiguation 段:

```
"Counterfactual Quantum Cryptography (CQC)" 自 [Noh 2009] 起是 17 年 active 
子领域 · 用反事实传输做 key distribution (QKD-like 协议)。CQC 跟我们 PCC 是 
**正交研究方向**:
- CQC · 用 counterfactual 性质 **构造** cryptographic protocol (sender-receiver 
  信息传输 without physical particle transit)
- PCC · 用 counterfactual 性质 **防御** cryptographic attack (R2 stealth probe 
  bypass tamper-evident hardware)

两者使用同一物理基础 (IFM / Salih scheme) · 但应用方向相反 · 共同构成 
"counterfactual-aware cryptography" 完整图景。
```

**实施**:待 paper 修订

### Correction P0-4 · §03.2 P3 加 δ-extension 明示

§03.2 P3 当前写:

```
**(P3) 代价上界**:实现 $\Phi^{CF}_f$ 需要的总 oracle 调用次数:
$$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$
其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度 [Lin-Lin 2015]。
```

应改为:

```
**(P3) 代价上界**:实现 $\Phi^{CF}_f$ 需要的总 oracle 调用次数:
$$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$
其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度。

**注**:这是 [Lin-Lin 2015] 的 $\delta \to 0$ 极限模型 $B(f) = \Theta(Q(f)^2)$ 
的显式 $\delta$-参数化扩展。在 $\delta \to 0$ 极限下还原 Lin-Lin 原版。Lin-Lin 
模型本身见 arXiv:1410.0932 · CCC 2015 · ToC 12(18) 2016 · doi:10.4086/toc.2016.v012a018。
```

**实施**:待 paper 修订

### Correction P0-5 · §03.5 子算子 cost 公式漏平方修复

§03.5 表中 4 个公式漏平方:

| 算子 | 原 (错) | 修正 |
|---|---|---|
| $\Phi^{CF}_{\text{OR}}$ | $O(\sqrt{N}/\delta)$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{AND}}$ | $O(\sqrt{N}/\delta)$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{COUNT}}$ | $O(\sqrt{N \cdot \text{ans}}/\delta)$ | $O(N \cdot \text{ans}/\delta)$ |
| $\Phi^{CF}_{\text{T}_t}$ | $O(\sqrt{Nt}/\delta)$ | $O(Nt/\delta)$ |

原因:从 $B_\delta(f) = O(Q(f)^2/\delta)$ 推 · $Q(\text{OR}) = \Theta(\sqrt{N})$ · 平方 $= N$ · 除 $\delta$ $= N/\delta$。

或者:verify Lin-Lin 2015 原版精确 bound (可能 $\Phi^{CF}_{\text{OR}}$ 是 special case 有 tighter bound · 比如 $\Theta(N/\log^2 N / \delta)$)。

**实施**:待 paper 修订 · 优先 verify Lin-Lin 精确 bound

---

## P1 修订 (应修)

### Correction P1-1 · §06.1 加第 5 类 algebraic disambig

§06.1 当前 4 类邻近 disambig (LLM / 心理学 / ML / 因果) · 应加第 5 类:

```
**(E) "Subtraction-free complexity" / algebraic complexity**:
例 [Fomin 2013, arxiv 1307.8425] "Subtraction-free complexity, cluster 
transformations, and spanning trees"。这是 algebraic complexity 子领域 · 研究在
仅允许加 / 乘 (不允许减) 的算术电路中评估多项式的复杂度。跟 SCP 是符号 / 
结构层面的 "subtractive" · 不是 quantum-physical 层面的反事实计算。
```

**实施**:待 paper 修订

### Correction P1-2 · §99 cite year/published year 精确化

| Entry | 当前 | 应改 |
|---|---|---|
| `[Wiesner 1969]` | 1969 | "written c. 1969 · published 1983" + DOI 10.1145/1008908.1008920 |
| `[Belovs 2019]` | 2019 | "arXiv 2019 · published Quantum journal q-2020-03-02-241" |
| `[Reichardt 2010]` | 2010 | "STOC 2010 + ToC Vol 8 a13 (2012) DOI 10.4086/toc.2012.v008a013" |
| `[Farhi 2008]` | short | 改为 `[Farhi-Goldstone-Gutmann 2008]` long form 跟 [Childs] 一致 |
| `[Childs 2009]` | short | 改为 `[Childs-Cleve-Jordan-Yonge-Mallo 2009]` long form |

### Correction P1-3 · §99 模糊 cite 精确化 (P1)

| Entry | 当前 | 应改 |
|---|---|---|
| `[Gottesman 2002]` | "tamper detection" | 分两条:`[Barnum et al. 2002]` BCGST authentication + `[Gottesman 2003]` Uncloneable Encryption |
| `[QIUP 2025]` | 模糊 | 具体 paper · 例 Franco 2026 + Lemos 2014 + 其他 |
| `[Lord 2024]` | author 名 | 改为完整 entry: arxiv 2411.02742 author 列表 |
| `[Hosseini 2016]` | 模糊 | 具体 paper title |
| `[Kaplan 2016]` | 模糊 | 可能 Kaplan-Leurent-Leverrier-Naya-Plasencia 2016 quantum cryptanalysis |
| `[Mitchison-Jozsa 2006]` | 模糊 | "The limits of counterfactual computation" arxiv quant-ph/0606092 |
| `[Lloyd 2008]` | 模糊 | 具体 paper title |

**实施**:待 paper 修订 · 逐 entry 查 arxiv 完整 metadata

---

## P2 修订 (nice-to-have)

### Correction P2-1 · 物理 caveat 补充

§14 worked example 引 [Salih 2013] 时加 caveat:

```
注:Salih 2013 协议在 thousands of optical elements limit 下达到 >95% efficiency 
[Calafell 2019 引述]。当前 chip 物理上 N=6 max [Calafell 2019]。
```

### Correction P2-2 · supplement entries 跟 paper 一致性

12 simulator README 引用 cite key 应一致跟新 cite key (Hance 2025 → Franco-Camillini-Galvão 2026 etc)。

由于 supplements 在 supplements/ 目录而非 thinking-in-cfe/ · 上次 22 处替换可能未覆盖 supplements。需 grep 一遍 supplements/ 确认。

**已 verify**:supplement entries 当前不引 [Hance 2025] / [Yang 2026] / [Hance 2019] · 不需修改。但 supplement 11/12/13 catalog 可加 "cite key audit 防错指南"。

---

## P0+ 修订 · 物理基础 PhD-level + critical paper audit (batch-11 落地)

### Correction P0-6 · §02 prior-art 加 PhD-level synthesis section (§02.7)

引 6 个新 source:Hance PhD thesis 2023 + Violaris DPhil 2025 + Frumkin-Bush 2023 + Bush 2021 + Hance 2021 + IOP 2024。

**实施**:已完成 (本 batch commit)

### Correction P0-7 · §03.7 R1/R2/R3 differentiator 加 Frumkin-Bush 2023 caveat

明示 single bomb tester 规模 IFM 可以经典模拟 (Frumkin-Bush 2023) · chained Zeno + multi-object IFM 仍 quantum-only · CFE 应用 niche 在 N≥2 chained 规模成立。

**实施**:已完成 (本 batch commit)

### Correction P0-8 · §11.2 加 CAVEAT 6

Frumkin-Bush 2023 hydrodynamic pilot-wave analog 实测 25% droplet detection 跟 EV 量子 IFM 等价 · 提议 falsification 实验 (延长 arm length nλ)。

**实施**:已完成 (本 batch commit)

### Correction P0-9 · §99 加 6 个新 entry (L1 section)

PhD thesis + critical paper 6 个 reference 加到 §99 新 section "L1 · PhD-level synthesis + critical reviews (2023-2025)"。

**实施**:已完成 (本 batch commit)

### Correction P1-4 · §05 D3 加 constructor theory framing (Violaris 2025)

引 Violaris DPhil thesis 2025 · constructor theory (Deutsch-Marletto) 给 D3 论证 formal foundation。

**实施**:待修 (本 batch 未完成 · P1 优先级)

---

## 修订实施 checklist (updated 2026-06-20 batch-11 后)

| Correction | 优先级 | 状态 |
|---|---|---|
| P0-1 全文 22 处 cite key 替换 | P0 | ✅ commit ab8aba4 |
| P0-2 §99 3 entries author 字段 | P0 | ✅ commit ab8aba4 |
| P0-3 加 [Noh 2009] CQC 子领域 | P0 | ⏳ 待修 |
| P0-4 §03.2 P3 加 δ-extension 说明 | P0 | ⏳ 待修 |
| P0-5 §03.5 子算子公式漏平方 | P0 | ⏳ 待修 (先 verify Lin-Lin 精确 bound) |
| **P0-6 §02 加 §02.7 PhD-level synthesis section** | P0 | ✅ **batch-11 commit** |
| **P0-7 §03.7 加 Frumkin-Bush 2023 caveat** | P0 | ✅ **batch-11 commit** |
| **P0-8 §11.2 加 CAVEAT 6 (single IFM classical analog)** | P0 | ✅ **batch-11 commit** |
| **P0-9 §99 加 L1 section 6 个新 entry** | P0 | ✅ **batch-11 commit** |
| P1-1 §06.1 加第 5 类 algebraic disambig | P1 | ⏳ 待修 |
| P1-2 §99 year/published 精确化 | P1 | ⏳ 待修 |
| P1-3 §99 7 模糊 entry 精确化 | P1 | ⏳ 待修 |
| P1-4 §05 D3 加 constructor theory framing | P1 | ⏳ 待修 |
| P2-1 §14 Salih caveat | P2 | ⏳ 待修 |
| P2-2 supplements 一致性 | P2 | ✅ verify OK |

---

## 元层

本文件是 audit 的 actionable output · 直接 input 到 paper 修订 PR。

下一 session 接手时:按 P0 → P1 → P2 顺序逐条修 · 每个 correction 一个 commit · message 引用 `audit/07-prior-art-corrections.md#correction-P0-X`。

---

## 版本

- 2026-06-20 v1 · 230 claim 全审后整理
