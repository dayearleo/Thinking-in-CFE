# CFE 论文修订总 Checklist · 一目了然版

> **日期**:2026-06-20 v1
> **位置**:本文件 = CFE 论文剩余修订的单点 checklist · 跟着 check 就行
> **整合来源**:audit/07-prior-art-corrections.md + audit/THEORY-ADJUSTMENTS-MASTER-REPORT.md + 多次 hook system reminder 提示
> **目的**:user verbatim "把所有要修的点 · 单独列入一个 checklist 文档"

---

## 0 · 状态 legend + 总进度

| Symbol | 含义 |
|---|---|
| ✅ | 已修 (commit hash 已 mark) |
| ⏳ | 待修 |
| 🔄 | 部分修 / 进行中 |

```
总计:      18 项
├─ 已修:    9 项 (50%)
├─ 待修 P0: 3 项 (17%)
├─ 待修 P1: 5 项 (28%)
├─ 待修 P2: 3 项 (17%)
└─ Cleanup: 3 项 (17%)
```

**剩余工作量估计**:~130-150 行 · ~3-5 小时单 session。

---

## 1 · 已修 (✅ 9 项)

跟 commit hash 一一对账 · reviewer 可 `git log --oneline` + `git show <hash>` 验证。

| ID | 章节 | 内容 | Commit |
|---|---|---|---|
| ✅ P0-1 | 全文 22 处 | cite key 替换 (Hance 2025 → Franco-Camillini-Galvão 2026 · Yang 2026 → Tang et al. 2026 · Hance 2019 → Calafell et al. 2019) | `ab8aba4` |
| ✅ P0-2 | §99 | 3 entries author 字段精确化 (Calafell 14-author / Franco 3-author / Tang 7-author) | `ab8aba4` |
| ✅ — | §03.9 | SOTA 表精确化 (N=12 → N=5 区分 / 3 dB per-facet / >99% single MZI) | `ab8aba4` |
| ✅ — | §11.2 | 加 5 物理 CAVEAT (multi-object N=5 / CFC violation 2.4% / Salih thousands MZI / heralding 3% / visibility 累乘) | `ab8aba4` |
| ✅ — | §10 A2/A3/A4 | 加 N≤10 niche SOTA caveat | `ab8aba4` |
| ✅ — | §15.5 | R2 mental shift 加 violation bound formula + 4 scenario 表 | `ab8aba4` |
| ✅ P0-6 | §02 | 加 §02.7 PhD-level synthesis section (Hance 2023 PhD + Violaris 2025 DPhil + Frumkin-Bush 2023 + Bush 2021 + Hance 2021 + IOP 2024) | `9d83bb6` |
| ✅ P0-7 | §03.7 | R1/R2/R3 differentiator 加 Frumkin-Bush 2023 单 IFM 经典模拟 caveat (区分 single vs chained/multi-object 规模) | `9d83bb6` |
| ✅ P0-8 | §11.2 | 加 CAVEAT 6 (Frumkin-Bush 2023 hydrodynamic pilot-wave analog + falsification proposal) | `9d83bb6` |
| ✅ P0-9 | §99 | 加 L1 section 6 个新 entry (PhD thesis + critical reviews 2023-2025) | `9d83bb6` |

---

## 2 · ⏳ P0 必修 (3 项 · 投学术 venue 前必修)

### ✅ P0-3 · §02 加 [Noh 2009] CQC 17 年子领域 + disambig (DONE · §02.4.1 加 6 entries + §15.7 PCC vs CQC disambig + 命名候选)

**问题**:Counterfactual Quantum Cryptography (CQC) 自 [Noh 2009] PRL 103.230501 起 17 年 active 子领域 · 我们 PCC 命名跟 CQC 冲突。

**修订位置**:

- `thinking-in-cfe/02-prior-art.md` (加新段)
- `thinking-in-cfe/15-cryptographic-mental-model-shift.md` §15.9 (加 disambig)
- `thinking-in-cfe/99-references.md` (加 6 entry)
- `supplements/01-pcc-founding-document.md` (加 PCC vs CQC 对比段)

**具体修订内容**:

§02 加 5 个 paper entry:

```
**[Noh 2009]** · T.-G. Noh · "Counterfactual Quantum Cryptography" · 
Phys. Rev. Lett. 103, 230501 (2009) · DOI: 10.1103/PhysRevLett.103.230501

**[Yin 2010]** · Z.-Q. Yin, H.-W. Li, W. Chen, Z.-F. Han, G.-C. Guo · 
"Security of counterfactual quantum cryptography" · Phys. Rev. A 82, 042335 (2010)

**[Liu 2012a]** · X. Liu et al. · "Counterfactual quantum cryptography based on 
weak coherent states" · Phys. Rev. A 86, 022313 (2012)

**[Liu 2012b]** · Y. Liu et al. · "Experimental Demonstration of Counterfactual 
Quantum Communication" · Phys. Rev. Lett. 109, 030501 (2012)

**[Semi-CQBC 2020]** · "Semi-Counterfactual Quantum Bit Commitment Protocol" · 
Scientific Reports (2020) · doi:10.1038/s41598-020-62893-0
```

§15.9 加 disambig 段:

```
CQC 用 counterfactual 性质**构造** cryptographic protocol (QKD-like 协议) · 
我们 PCC 用反事实性质**防御** cryptographic attack (R2 stealth bypass 
tamper-evident hardware) · 是正交研究方向。共同构成 "counterfactual-aware 
cryptography" 完整图景。
```

**或**考虑改名 (候选):
- Counterfactual-Resistant Cryptography (CRC) · 类比 Quantum-Resistant Cryptography
- Anti-Counterfactual Cryptography
- Counterfactual-Aware Cryptography (CAC)

**工作量**:~25 行 + 1 个决策 (改名 vs 保留 PCC + disambig)

### ✅ P0-4 · §03.2 P3 加 δ-extension 明示 (DONE · 加 "注 · δ-参数化扩展明示" 段)

**问题**:我们 $B_\delta(f) = O(Q(f)^2/\delta)$ 是 [Lin-Lin 2015] 原版 $B(f) = \Theta(Q(f)^2)$ 的 δ-参数化扩展 · 论文未明示。

**修订位置**:`thinking-in-cfe/03-operator-formal-definition.md` §03.2 (line 35-39)

**具体修订内容**:

原文:

```
**(P3) 代价上界**:实现 $\Phi^{CF}_f$ 需要的总 oracle 调用次数:
$$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$
其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度 [Lin-Lin 2015]。
```

改为:

```
**(P3) 代价上界**:实现 $\Phi^{CF}_f$ 需要的总 oracle 调用次数:
$$B_\delta(f) = O\left(\frac{Q(f)^2}{\delta}\right)$$
其中 $Q(f)$ 是 $f$ 的标准量子查询复杂度。

**注**:这是 [Lin-Lin 2015] 的 $\delta \to 0$ 极限模型 $B(f) = \Theta(Q(f)^2)$ 
的显式 $\delta$-参数化扩展 · 在 $\delta \to 0$ 极限下还原 Lin-Lin 原版。Lin-Lin 
模型本身见 arXiv:1410.0932 · CCC 2015 · ToC 12(18) 2016 · doi:10.4086/toc.2016.v012a018。
```

**工作量**:~5 行

### ✅ P0-5 · §03.5 子算子 4 公式漏平方修复 (DONE · 4 公式 √N → N + 加 Q(f)² 推导表 + Lin-Lin special-case 引用)

**问题**:从 $B_\delta(f) = O(Q(f)^2/\delta)$ 推 · 4 个公式漏平方:

| 算子 | 原 (错) | 应改 |
|---|---|---|
| $\Phi^{CF}_{\text{OR}}$ | $O(\sqrt{N}/\delta)$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{AND}}$ | $O(\sqrt{N}/\delta)$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{COUNT}}$ | $O(\sqrt{N \cdot \text{ans}}/\delta)$ | $O(N \cdot \text{ans}/\delta)$ |
| $\Phi^{CF}_{\text{T}_t}$ | $O(\sqrt{Nt}/\delta)$ | $O(Nt/\delta)$ |

**修订位置**:`thinking-in-cfe/03-operator-formal-definition.md` §03.5 (line 66-71)

**先 verify**:Lin-Lin 2015 原版可能给 OR 有 tighter special-case bound (例 $O(N/\log^2 N / \delta)$) · 应先查后再修 · 否则直接 $O(N/\delta)$。

**工作量**:~8 行 (4 公式表 + 1 句话说明)

---

## 3 · ⏳ P1 应修 (5 项 · 论文 robust)

### ✅ P1-1 · §06.1 加第 5 类 algebraic disambig (Fomin 2013) (DONE · 在 §02.5 (E) 加 Fomin 2013 + 5 类完整免责)

**问题**:§06.1 当前 4 类邻近 disambig (LLM / 心理学 / ML / 因果) · 漏第 5 类 algebraic complexity 子领域。

**修订位置**:`thinking-in-cfe/06-subtractive-paradigm.md` §06.1

**具体修订内容**:

```
**(E) "Subtraction-free complexity" / algebraic complexity**:
例 [Fomin 2013, arxiv 1307.8425] "Subtraction-free complexity, cluster 
transformations, and spanning trees"。algebraic complexity 子领域 · 研究在仅允
许加 / 乘 (不允许减) 的算术电路中评估多项式的复杂度。跟 SCP 是符号 / 结构层面的
"subtractive" · 不是 quantum-physical 层面的反事实计算。
```

**工作量**:~5 行

### ⏳ P1-2 · §99 year/published 精确化

**修订位置**:`thinking-in-cfe/99-references.md`

**具体精确化清单**:

| Entry | 当前 | 应改 |
|---|---|---|
| [Wiesner 1969] | 1969 | "written c. 1969 · published 1983" + DOI 10.1145/1008908.1008920 |
| [Belovs 2019] | 2019 | "arXiv 2019 · published Quantum journal q-2020-03-02-241" |
| [Reichardt 2010] | 2010 | "STOC 2010 + ToC Vol 8 a13 (2012) DOI 10.4086/toc.2012.v008a013" |
| [Farhi 2008] | short | 改为 [Farhi-Goldstone-Gutmann 2008] long form |
| [Childs 2009] | short | 改为 [Childs-Cleve-Jordan-Yonge-Mallo 2009] long form |

**工作量**:~5 entries · ~10-15 行

### ⏳ P1-3 · §99 7 个模糊 cite entry 精确化

**修订位置**:`thinking-in-cfe/99-references.md`

**具体清单**:

| Entry | 当前模糊 | 应精确化 |
|---|---|---|
| [Gottesman 2002] | "tamper detection" | 分两条:[Barnum et al. 2002] BCGST + [Gottesman 2003] Uncloneable |
| [QIUP 2025] | 模糊 | 具体 paper (Franco 2026 + Lemos 2014 + 其他) |
| [Lord 2024] | author 名 | 完整 entry: arxiv 2411.02742 + author 列表 |
| [Hosseini 2016] | 模糊 | 具体 paper title |
| [Kaplan 2016] | 模糊 | 可能 Kaplan-Leurent-Leverrier-Naya-Plasencia 2016 |
| [Mitchison-Jozsa 2006] | 模糊 | "The limits of counterfactual computation" arxiv quant-ph/0606092 |
| [Lloyd 2008] | 模糊 | 具体 paper title |

**工作量**:~7 entries · ~15-20 行

### ⏳ P1-4 · §05 D3 加 constructor theory framing (Violaris 2025)

**问题**:[Violaris DPhil 2025] (Oxford · Vedral/Ekert) 用 constructor theory framework 给 quantum counterfactuals 提供 formal foundation · 可强化我们 D3 论点。

**修订位置**:`thinking-in-cfe/05-three-dim-transcendence.md` §05.4

**具体修订内容**:

```
注:**Violaris DPhil thesis 2025** (Oxford · supervisors Vedral + Ekert · 
examiners Deutsch + Adesso) 用 constructor theory (Deutsch-Marletto 2015) 框架研究 
macroscopic quantum counterfactuals · 跟我们 D3 论证 (CFE 跟 FT QC categorical 
差异) 同向 · 提供 formal foundation。
```

**工作量**:~5 行

### ⏳ P1-5 · §00 摘要 + §05.3 加 "N≤10 niche" 限定

**问题**:§00 摘要当前 "提前 10-20 年解锁" 是无限定 · 实际只在 N≤10 niche 成立。

**修订位置**:
- `thinking-in-cfe/00-abstract.md`
- `thinking-in-cfe/05-three-dim-transcendence.md` §05.3

**具体修订内容**:

§00 摘要:

```
CFE 在 **N≤10 multi-object IFM 规模** 上 · 用专用 photonic 硬件提前 10-20 年解锁 · 
独占 FT QC 永远到不了的 D3 interface domain。N=100+ 规模仍需未来 photonic chip 
工艺突破 (光损 + visibility + 集成度)。
```

**工作量**:~3 行

---

## 4 · ⏳ P2 nice-to-have (3 项)

### ⏳ P2-1 · §14 + §17 加 Salih 2013 thousands MZI caveat

**问题**:Calafell 2019 引述 "Salih scheme requires thousands of optical elements to achieve >95% success"。我们 §14 / §17 引用 Salih 协议时应加 caveat。

**修订位置**:
- `thinking-in-cfe/14-breakthrough-demonstration.md`
- `thinking-in-cfe/17-isomorphism-methodology.md`

**具体修订内容**:

```
**注**:Salih 2013 协议在 thousands of optical elements limit 下达到 >95% 
efficiency [Calafell et al. 2019 引述]。当前 chip 物理上 N=6 max [Calafell 2019] · 
实际工程需要 chip 集成度突破才能达到 thousands of MZI。
```

**工作量**:~5 行 (2 处)

### ⏳ P2-2 · 12 simulator README 批量加 SOTA caveat

**问题**:supplements 10/14/16-34 共 12 个 simulator README 都应加 SOTA caveat。

**修订位置**:每个 simulator 子目录的 README.md

**具体内容**:

```
**重要 SOTA caveat** (2026-06-20 audit 落地):simulator 模拟 R1/R2/R3 性质 · 
实际 photonic 硬件 SOTA:
- N ≤ 32 mode (current commercial UPP)
- Multi-object IFM N=5 max (Franco 2026)
- System efficiency ~2.7% (heralding 3% × detection 90%)
- R2 violation 2.4% per query at N=6 (Calafell 2019)

simulator 数字 (例 1000 trials 96% extraction rate) 在 R2 violation 任意小 极限
下精确成立 · 实际硬件 attack-success ~97% per attempt (1 - violation rate)。
```

**工作量**:12 README × ~3 行 = ~36 行

### ⏳ P2-3 · §03.10 限界 "N ≤ 12-32" 更新

**问题** (hook 提示):§03.10 限界提到 "N ≤ 12-32" 应 update 为 "N=5-6 multi-object/chained 实测 demonstrated · N=12-32 platform mode 数"。

**修订位置**:`thinking-in-cfe/03-operator-formal-definition.md` §03.10

**工作量**:~3 行

---

## 5 · 🧹 Cleanup (3 项 · 跟 hook 提示一致)

### ✅ C-1 · §11.2 CAVEAT 5/6 顺序错 swap (DONE)

**问题** (hook 提示):commit 9d83bb6 把 CAVEAT 6 插到 CAVEAT 5 之前 · 顺序成了 6 → 5 · 应 swap 回 5 → 6。

**修订位置**:`thinking-in-cfe/11-limitations-and-open-problems.md` §11.2

**工作量**:1 swap (cut + paste)

### ✅ C-2 · §99 BibTeX stale "Hance2025MultiObject" entry 修 (DONE · 加 4 个新 BibTeX)

**问题** (hook 提示):commit ab8aba4 修了 §99 prose entry · 但 BibTeX 块还有 stale `Hance2025MultiObject` (author "Hance, Jonte R. and others" · eprint 2604.04691) 没改。

**修订位置**:`thinking-in-cfe/99-references.md` (BibTeX 块)

**具体修订**:把 `Hance2025MultiObject` 整个 entry 改成 `FrancoCamilliniGalvao2026MultiObject` + 完整作者列表 + year 2026。

**工作量**:1 BibTeX entry · ~10 行

### ✅ C-3 · README abstract "分片为 15 个文件" 现 19 章 update (DONE · 加 v0.2 版本说明)

**问题** (hook 提示):`thinking-in-cfe/README.md` abstract 段当前写 "分片为 15 个文件" · 论文已扩到 19 章 (含 §18 audit-report)。

**修订位置**:`thinking-in-cfe/README.md` (摘要段)

**工作量**:1 string replace

---

## 6 · 工作流建议

### 推荐顺序 (按依赖关系)

```
1. 🧹 C-1/C-2/C-3 (3 个 cleanup · 最快 · ~15 行 · 30 分钟)
2. ⏳ P0-3 [Noh 2009] CQC + disambig (~25 行 · 1 小时 + 改名决策)
3. ⏳ P0-4 δ-extension 明示 (~5 行 · 15 分钟)
4. ⏳ P0-5 子算子公式漏平方 (verify Lin-Lin 后 ~8 行 · 30 分钟)
5. ⏳ P1-1 algebraic disambig (~5 行 · 15 分钟)
6. ⏳ P1-2/3 §99 entry 精确化 (~30 行 · 1 小时)
7. ⏳ P1-4 constructor theory (~5 行 · 15 分钟)
8. ⏳ P1-5 N≤10 niche 限定 (~3 行 · 10 分钟)
9. ⏳ P2-1 Salih caveat (~5 行 · 15 分钟)
10. ⏳ P2-3 §03.10 限界 N=5-6 update (~3 行 · 10 分钟)
11. ⏳ P2-2 12 simulator README batch (~36 行 · 1.5 小时)
```

**总计**:~130 行 · ~5 小时单 session。

### 推荐 Commit 拆分

**Option A · 一次大 commit** (单 session 跑完):

```
paper: 最终修订 · P0 必修 + P1 应修 + P2 nice-to-have + 3 cleanup

P0 (投学术 venue 必修):
- P0-3 §02 + §15.9 + supplement 01 加 [Noh 2009] CQC 17 年子领域 + PCC vs CQC disambig
- P0-4 §03.2 P3 加 δ-parameterized extension of Lin-Lin 2015 明示
- P0-5 §03.5 子算子 4 公式漏平方修复 (OR/AND/COUNT/T_t)

P1 (论文 robust):
- P1-1 §06.1 加第 5 类 algebraic disambig (Fomin 2013)
- P1-2/3 §99 11 个 entry 精确化 (year/published + 7 模糊)
- P1-4 §05.4 加 Violaris 2025 constructor theory framing
- P1-5 §00 摘要 + §05.3 加 "N≤10 niche" 限定

P2 (nice-to-have):
- P2-1 §14 + §17 Salih 2013 加 thousands MZI caveat
- P2-2 12 simulator README batch 加 SOTA caveat
- P2-3 §03.10 N=12-32 → N=5-6 demonstrated 区分

Cleanup:
- C-1 §11.2 CAVEAT 5/6 顺序 swap
- C-2 §99 BibTeX "Hance2025MultiObject" → "FrancoCamilliniGalvao2026MultiObject"
- C-3 thinking-in-cfe/README.md "分片为 15 个文件" → 19 章
```

**Option B · 分 4 commit** (清晰边界):

1. `paper: cleanup · CAVEAT 顺序 + BibTeX stale entry + README outdated` (3 cleanup)
2. `paper: P0 · CQC 17 年 prior-art + δ-extension + 子算子公式漏平方` (3 P0)
3. `paper: P1 · algebraic disambig + cite 精确化 + constructor theory + N≤10 niche` (5 P1)
4. `paper: P2 · Salih caveat + 12 simulator README + §03.10 限界` (3 P2)

---

## 7 · 完成判据 (terminal state)

### 必满足

- [ ] 所有 P0 (3 项) 已 ✅
- [ ] §99 BibTeX 块 0 个 stale entry
- [ ] 所有 audit/07-prior-art-corrections.md 中 P0/P1 标 ✅
- [ ] `git status --short` 干净
- [ ] supplement 17 mirror 同步 (再跑 `cp -r audit/* supplements/17-audit-master-log/`)

### 应满足

- [ ] 所有 P1 (5 项) 已 ✅
- [ ] §99 所有 entries 都有 DOI 或 arxiv ID 至少一个
- [ ] 论文 §00 / §03 / §05 / §06 / §15 / §99 跟 batch-5 + batch-11 finding 一致

### nice-to-have

- [ ] 所有 P2 (3 项) 已 ✅
- [ ] 12 simulator README 全部加 SOTA caveat
- [ ] 3 cleanup 全部解决

---

## 8 · 跟 audit/07-prior-art-corrections.md 的 mapping

本 checklist 跟 audit/07-prior-art-corrections.md 是同一信息的两种视图:

| 文件 | 角色 |
|---|---|
| `audit/07-prior-art-corrections.md` | 详细 prior-art-side rationale + 修订 narrative |
| **本文件** `audit/REVISION-CHECKLIST.md` | 一目了然 checklist + 工作量估计 + 完成判据 + commit 模板 |

跟 `audit/THEORY-ADJUSTMENTS-MASTER-REPORT.md` 的 mapping:

| 文件 | 角色 |
|---|---|
| `audit/THEORY-ADJUSTMENTS-MASTER-REPORT.md` | 10 部分系统化决策 (CFE 理论 + 跨学科 + 发布策略) |
| **本文件** `audit/REVISION-CHECKLIST.md` | 决策的 actionable checklist · 跟着改就行 |

**单点真理源**:本文件 (REVISION-CHECKLIST.md)。其他文件提供 backing。

---

## 9 · 版本

- 2026-06-20 v1 · 初版 · 整合 audit/07 + THEORY-ADJUSTMENTS-MASTER + hook 提示 · 一目了然 checklist
