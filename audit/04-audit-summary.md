# 04 · Audit Summary · 进度 + 关键发现

> 实时更新 · 每完成 10 个 claim 更新一次
> 详细 claim 列表 → `01-claim-registry.md`
> 完整 audit/claims/AUD-XXX/ 文件 → 每条 claim 各自目录

---

## 进度统计 (2026-06-20 batch 2 后)

```
Total:       230
UNVERIFIED:  219  (95.2%)
Audited:      11  ( 4.8%)
├─ CONFIRMED:   6   (E-001, E-002, E-003, E-013, E-027, E-028)
├─ PARTIAL:     2   (E-004, C15-001)
├─ GAP:         0
├─ REFUTED:     2   (E-014, E-044)
└─ NOVEL:       1   (C06-002)
```

按类别分布:

| 类 | Total | Audited | UNVERIFIED |
|---|---|---|---|
| A 数学定义 | 25 | 0 | 25 |
| B 物理可行性 | 20 | 0 | 20 |
| C 复杂度 | 30 | 0 | 30 |
| D Novelty | 15 | 2 | 13 |
| E 历史归属 | 46 | 8 | 38 |
| F vs FT QC | 20 | 0 | 20 |
| G 应用 | 40 | 0 | 40 |
| H 密码学 | 34 | 0 | 34 |

E 类做得最多 (8/46) · 是 audit 起步策略 (先做容易的)。其他类后续 batch 跟。

---

## 🚨 Top 重要发现 (按严重度排序)

### #1 · REFUTED · [Hance 2025] attribution 错误 (AUD-E-014)

我们论文 8+ 处引 `[Hance 2025]` 指 "universal integrated photonic processor multi-object IFM lab proven" · 实际:

| 字段 | 我们论文 | arxiv 2604.04691 实际 |
|---|---|---|
| 作者 | "Hance" | **Sara Franco · Anita Camillini · Ernesto F. Galvão** |
| 年份 | 2025 | **2026-04** |
| Platform | (隐含 N=12 universal photonic) | Quandela Ascella cloud (5 objects sequential) |

**Reviewer-killing**:reviewer 一查 arxiv 立即看到作者完全不一样 · 论文直接 desk reject。

修订要求:论文 8+ 处全文 replace · §99 加正确 entry · 还要重审 AUD-C03-015 / AUD-C03-016 (N=12 vs N=5 sequential 数字不准)。

### #2 · REFUTED · [Yang 2026] attribution 错误 (AUD-E-044)

我们论文 4 处引 `[Yang 2026]` 用于 §02/§06 "subtractive" disambiguation · 实际:

| 字段 | 我们论文 | arxiv 2602.18232 实际 |
|---|---|---|
| 第 1 作者 | "Yang" | **Lexiang Tang** |
| Yang 位置 | 隐含第 1 | 实际第 6 作者 (Bang Yang) |

学术 cite 标准是第 1 作者 · 应该是 `[Tang et al. 2026]` · 不是 `[Yang 2026]`。

### 🔍 #1 + #2 共同 pattern · 多作者 cite 选错 cite key

两个 REFUTED 都是**同模式错误**:多作者 paper 选错了 cite key (不是第 1 作者)。

启示:audit 完成后必跑全 §99-references **多作者 cite audit batch** · 对每个多作者 entry 核对是否用第 1 作者。预估 ~20 个多作者 cite · 都要查。新增 backlog task **AUD-meta-001**。

### #3 · PARTIAL · [Lin-Lin 2015] 公式 extension 未明确化 (AUD-E-004)

我们 §03.2 P3 写 $B_\delta(f) = O(Q(f)^2/\delta)$ · 是 Lin-Lin 原版 $B(f) = \Theta(Q(f)^2)$ 的 $\delta$ extension · 但论文没明确说 "我们扩展了"。

修订:§03.2 加 explicit 说明 · §99 完善 reference entry。

### #4 · PARTIAL · PCC 命名漏 [Noh 2009] CQC 子领域 prior-art (AUD-C15-001)

"Counterfactual Quantum Cryptography (CQC)" 已是 17 年 active 子领域 ([Noh 2009] PRL 103.230501 起源 · 多篇 follow-up 至 2020) · 我们 §15/§16 提议 "Post-Counterfactual Cryptography (PCC)" 完全没引这一系列。

修订:§02 prior-art 加 CQC 系列 · §15.9 加 disambiguation · supplement 01 PCC founding document 加 CQC vs PCC 对比段 · 考虑改 PCC 命名 (候选:CRC / Anti-CC / CAC)。

### #5 · NOVEL · Subtractive Computation Paradigm 命名 (AUD-C06-002)

EXA 搜 0 hits 撞名 · 但应加 "Subtraction-free complexity (Fomin 2013, arxiv 1307.8425)" 第 5 类邻近 disambig (algebraic complexity 子领域)。

### CONFIRMED batch (6 个)

| ID | 准在哪 |
|---|---|
| E-001 [Wheeler 1978] | book chapter 全准 |
| E-002 [Elitzur-Vaidman 1993] | Found. Phys. 23:987 全准 |
| E-003 [Mitchison-Jozsa 2001] | Proc.Roy.Soc.A 457:1175 全准 |
| E-013 [Filatov-Auzinsh 2024] | Appl Phys B 130:121 全准 |
| E-027 [Farhi 2008] | ToC Vol 4 全准 · 建议统一长 cite "Farhi-Goldstone-Gutmann 2008" |
| E-028 [Childs 2009] | ToC Vol 5 全准 · 建议统一长 cite "Childs-Cleve-Jordan-Yonge-Mallo 2009" |

---

## 衍生 Backlog (审计过程发现的新工作)

| AUD-meta ID | 任务 | 优先级 |
|---|---|---|
| AUD-meta-001 | 全 §99-references 多作者 cite key audit · 防 Hance/Yang 同模式错误 | P0 |
| AUD-meta-002 | 复审 AUD-C03-015 (N=12 photonic SOTA) · 跟 E-014 REFUTED 强耦合 | P0 |
| AUD-meta-003 | 加 [Noh 2009] CQC 子领域 6+ 文献 attribution audit | P1 |
| AUD-meta-004 | §06.1 disambiguation 加第 5 类 (algebraic complexity Fomin 2013) | P1 |

---

## 元层 self-audit

- M1 ✓ · 找到 4 个重大 Gap (2 REFUTED · 2 PARTIAL)
- M2 部分 ✓ · 已跑 Novelty + Math · Physics + Differentiation 简化 (E 类不需 Physics)
- M3 ✓ · 11 个 claim 全部有 source/ + assessment.md
- M4 N/A · 仍在 sample 阶段 · 全 230 完成时跑双向 remainder=0

## 下一 batch 建议

按 goal.md §1 onboarding · 推荐顺序:

1. AUD-meta-001 (多作者 cite audit) — P0 · 防止更多 attribution 错误延续
2. AUD-E-005 (Kwiat 1995) → E 类剩余 batch (E-006/E-008/E-010/E-011 etc)
3. AUD-C03-001 ~ C03-014 (A 类数学定义 14 条) — 论文根基
4. AUD-C16-005 ~ C16-026 (H 类 17 算法 audit batch)

---

## 版本

- 2026-06-20 v1 · batch 1 + batch 2 后初版
- 11/230 audited · ~4.8% 进度
