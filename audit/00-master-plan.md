# 00 · Audit Master Plan · CFE 论文现实性审计

> **本文件 = 审计工程方法论的单点真理源** · 任何参与审计的 AI / human reviewer 必读
> 受众:reviewer / 跨 session 接手 AI · 长文版 · 详细 ~500 行
> 速查版:`goal.md` (AI 自主驱动核心 ~200 行)
> 进度索引:`01-claim-registry.md` (230 claim 状态表)

---

## 0 · 一句话目标

对 `Thinking in CFE` 全部 230 条可审计 claim 跑严密联网搜索审计 · 用 EXA / Serper / Jina 三引擎 + 双语 + 双时段 · 每条 claim 留不可伪造面包屑 · 把审计本身作为论文 §18 + supplement · 完备性证明 (forward + backward remainder = 0) 通过才算完成。

---

## 1 · 元方法论 4 条 invariant (整个工程必守)

### M1 · 审计 ≠ 证明对 · 审计 = 找 Gap

不预设 "我们对了 · 找证据补" · 而预设 "可能错了 · 找证据证伪"。每条 claim 默认状态 = `UNVERIFIED` · 证据出来才转 `CONFIRMED` / `REFUTED` / `GAP` / `PARTIAL` / `NOVEL`。

### M2 · 每条声明必有 4 类查询

| 查询类 | 问什么 |
|---|---|
| **Novelty** | 有没有人 30 年前就做了?2025 最新工作有没有覆盖?跟我们 claim 的 wording 是否撞名? |
| **Math** | 数学定义在标准文献里长什么样?我们的版本一致 / 更严 / 漏 case? |
| **Physics** | 声称硬件能做 · 实际 SOTA 数字是什么?差距多大? |
| **Differentiation** | 跟相邻工作 (IFM / Grover / quantum walk / PIR / FHE / TPM 等) head-to-head 怎么比? |

### M3 · 不可伪造面包屑

每条 claim 的 audit 产物必含:

- 搜过的 query (verbatim · 含语言 / 引擎 / 时间)
- 抓到的源 (URL + 关键引用段 · file:line 精度)
- 推理链 (从源到 claim 的逻辑)
- 状态 + 证据强度 (1-5 星)

断言式 "我查了 30 篇" **不算** 面包屑 · 必须列 30 篇 URL + 关键引用段。

### M4 · 全查不抽样

claim registry 列出后必须**逐条**审 · 不允许 "重要的审 · 次要的跳"。配 `prove-completeness-against-corpus` 的双向 remainder=0:

- **产出侧**:每 claim 有 audit · 不漏
- **审计侧**:每 audit 被复审 · 不偏

---

## 2 · Claim 抽取 + 编号方案

### 编号规范

`AUD-<位置代码>-<序号>` 例:

| 编号 | 含义 |
|---|---|
| `AUD-C03-001` | paper/thinking-in-cfe/03-... 第 1 条 claim |
| `AUD-S10-005` | supplements/10-cfe-hndl-simulator/ 第 5 条 claim |
| `AUD-D004-002` | dev-notes/004-... 第 2 条 claim |

`C` = chapter (paper) · `S` = supplement · `D` = dev-note。

### 8 大 claim 类别

| 类 | 内容 | 主要来源 | 预估 |
|---|---|---|---|
| **A · 数学定义** | $\Phi^{CF}_f$ 形式 · cost theorem · 组合代数公理 | §03 / §04 / §06 | ~25 |
| **B · 物理可行性** | photonic N 路 / loss / SNSPD / fidelity / N=8-12 SOTA | §05 / §10 / supplements | ~20 |
| **C · 复杂度** | $B_\delta(f) = O(Q(f)^2/\delta)$ / D2 / D3 / D4 / Pareto | §07 / §08 | ~30 |
| **D · Novelty** | 我们 "新提出" 术语 (减法计算 / PCC / 同构方法论) | §06 / §15 / §17 | ~15 |
| **E · 历史归属** | "Wheeler 1978" / "Elitzur-Vaidman 1993" / "Farhi 2008" attribution | §02 / 全网 cite | ~50 |
| **F · vs FT QC / Grover / 量子游走** | D1/D2/D3 跟其他范式比较 | §05 / §10 | ~20 |
| **G · 应用 / 工业** | 12 simulator 对应 niche 的市场规模 / 客户故事 | §10 / §14 / §16 / supplements | ~40 |
| **H · 密码学具体声明** | 17 算法 audit / HSM tamper / R2 攻击 4 层 | §15 / §16 | ~30 |

**总计 ~230 条 claim** · 每条至少 4 类查询 = ~920 次搜索动作。

---

## 3 · 关键词矩阵 (6 维 · 详 `02-keyword-matrix.md`)

| 维 | 名 | 例 (英 / 中) |
|---|---|---|
| 1 | 算子定义 / 反事实计算 | `counterfactual quantum computation`, `interaction-free measurement` / `反事实量子计算` |
| 2 | 复杂度 / 算法 | `bomb query Lin Lin 2015`, `quantum query complexity` / `量子查询复杂度` |
| 3 | 物理硬件 / 集成光子 | `integrated photonic processor 12 mode`, `MZI mesh nanophotonic` / `集成光子处理器` |
| 4 | 密码学 / HSM | `HSM tamper evidence quantum`, `Gottesman tamper-evident` / `硬件安全模块抗篡改` |
| 5 | 范式新词防撞 | `subtractive computation`, `negation as computation` / `减法计算` |
| 6 | 应用 niche | `quantum PIR`, `stealth network probe` / `物理层 PIR` |

详细查询表 + curl 模板 → `02-keyword-matrix.md`。

---

## 4 · 搜索工具策略

### 三引擎 + 降级链

| 引擎 | 何时用 | 配额 |
|---|---|---|
| **EXA** `api.exa.ai/search` | 主力 · 语义搜 + 学术 (arxiv / PMC / journals) | 需自备 · sign up: exa.ai · 设 `${EXA_API_KEY}` |
| **Serper** `google.serper.dev` | Google / Scholar 严肃文献 / 公司白皮书 | 需自备 · sign up: serper.dev · 设 `${SERPER_API_KEY}` |
| **Jina** `r.jina.ai/<url>` | 直接抓 URL · markdown 化全文 | 需自备 · sign up: jina.ai · 设 `${JINA_API_KEY}` |
| arxiv API | EXA 漏 paper 时直接 `arxiv.org/api/query` | 公开 · 无需 key |

详 `~/.claude/skills/search-tools/references/full-sop.md` 降级链。

### 多语言策略

每 claim 至少跑 **英文 + 中文** 双轮。中文社区 (CSDN / 知乎 / 量子位 / 机器之心 / 中国密码学会) 可能藏英文检索遗漏的 review / SDK / 实际部署经验。

### 时间窗口策略

每 claim 必跑 2 次搜:

| 轮 | 范围 | 抓什么 |
|---|---|---|
| 1 · 全时段 | 无年份限制 | 历史经典 + 30 年回顾 |
| 2 · 近 12 月 | `<keyword> 2025` 或 `after:2024-12` | 最新工作 · 尤其 IFM 2024-2025 活跃年 |

---

## 5 · Per-claim 7 步执行流程 (核心 SOP)

每个 `AUD-XXX` claim 走完 7 步才算 audited:

| 步 | 动作 | 落产物 |
|---|---|---|
| 1 | 抽 claim 原文 + 来源 file:line | `audit/claims/AUD-XXX/source.md` |
| 2 | 设计 4 类 query (Novelty / Math / Physics / Differentiation) | `query-plan.md` |
| 3 | 跑 EXA + Serper + Jina · 英中双语 · 全时段 + 近 12 月 | `search-log.md` (verbatim query · 时间戳 · 结果摘要) |
| 4 | 抓 top 5 相关源 (Jina 拉全文) | `sources/<n>-<short-id>.md` |
| 5 | 提取关键引用段 + 跟我们 claim 对账 | `findings.md` |
| 6 | 判定 status + 证据强度 1-5 星 | `assessment.md` |
| 7 | 更新 master registry | `audit/01-claim-registry.md` |

### Status 判据 + 触发行为

| Status | 含义 | 证据强度 | 触发后续动作 |
|---|---|---|---|
| **CONFIRMED** | 学术 / 工程 SOTA 完全支持 | ⭐⭐⭐⭐⭐ | 加 citation 强化原章节 |
| **PARTIAL** | 部分支持 · 某 caveat 没涵盖 | ⭐⭐⭐ | 在原章节加 caveat |
| **GAP** | 我们说有 · 实际还没人做或无数据 | ⭐⭐ | §11 / §13 加 open problem |
| **REFUTED** | 已有反例 / 已被做且结论不同 | ⭐ | 必须改原章节 + 更新 §02 prior-art |
| **NOVEL** | 真没人做过 · 我们原创 | — | 加显式声明 + 防御 prior-art 索引 |

---

## 6 · 落盘结构

```
Thinking in CFE/audit/
├── 00-master-plan.md             # 本文件 · 方法论真理源
├── 01-claim-registry.md          # 230 claim 表 + 状态 + 链接
├── 02-keyword-matrix.md          # 6 维关键词矩阵 + curl 模板
├── 03-search-engine-log.md       # 总搜索日志 (timestamp / engine / query / hit)
├── 04-audit-summary.md           # 整体 summary + status 分布 + Top 20 发现
├── 05-gap-report.md              # 真 Gap 清单 + 补强建议
├── 06-novelty-defense.md         # NOVEL 部分的 prior-art 防御
├── 07-prior-art-corrections.md   # §02 修订建议
├── goal.md                       # 自主驱动协议 (跨 session AI 接手)
├── sources-cache/                # 全 session 共享的 Jina 抓取缓存
└── claims/
    ├── AUD-C02-001/
    │   ├── source.md             # 原文 file:line
    │   ├── query-plan.md         # 4 类 query 词
    │   ├── search-log.md         # 实际搜索调用 verbatim
    │   ├── sources/              # 抓到的源 (Jina markdown)
    │   ├── findings.md           # 关键引用 + 对账
    │   └── assessment.md         # status + 推理链
    └── ... (230 个目录)
```

### 进度可视化

`01-claim-registry.md` 顶部维护:

```
Total: 230 · Audited: X · CONFIRMED: A · PARTIAL: B · GAP: C · REFUTED: D · NOVEL: E
```

每 10 个 claim commit 一次 · 防长跑丢失。

---

## 7 · 整合回论文 (审计后 4 处必修)

### 7.1 · 新增 §18 · Audit Report (论文章节)

`paper/thinking-in-cfe/18-audit-report.md` · ~200 行:

- 18.1 审计方法论 (元规则 M1-M4)
- 18.2 230 claim 整体状态分布 + 直方图
- 18.3 重要发现 Top 20 (确认 / 反驳 / Gap)
- 18.4 跟 §11 限界 / §13 RFC 的对接
- 18.5 完整 audit log 指针 → `audit/`

### 7.2 · 修 §02 prior-art

按 `07-prior-art-corrections.md` · 新文献加进去 · 已被推翻的 attribution 删除。

### 7.3 · 修 §11 限界

把 `05-gap-report.md` 中 Gap 加为 §11 新条目 · 诚实标注 "审计发现 · 待社区贡献"。

### 7.4 · 新增 supplement · audit complete log

`supplements/17-audit-master-log/` · 含 `audit/` 全部内容 · 让 reviewer 自己跑 grep。

---

## 8 · 跨 session 自主驱动

详 `goal.md` (速查版 · ~200 行) · 包含:

- 任何 AI 接手时的 5 步 onboarding
- 完成判据 terminal state
- 每 session 起手 SOP
- 完整 230 claim list (跟 `01-claim-registry.md` 同步)
- 元规则速查
- 7 步流程速查
- 关键词矩阵速查
- 搜索工具 curl 模板 (含 key)
- 反模式
- 跨压缩边界 resume 协议

---

## 9 · 审计本身怎么 audit (元层)

按 `~/.claude/rules/auditability.md` · 审计本身也要可审计:

- **完备性证明 (forward)**:`audit/claims/AUD-XXX/` 数 == 230 · `find audit/claims -maxdepth 1 -type d | wc -l == 231`(含 claims/)
- **完备性证明 (backward)**:`grep -r "AUD-" paper/ supplements/` 命中的 claim 引用必跟 registry status 匹配
- **三透镜复核**:
  - 透镜 1 (数学):随机抽 10 个 C 类 · 复杂度推导是否被独立源支持
  - 透镜 2 (物理):随机抽 10 个 B 类 · SOTA 数字是否在 cited paper 里
  - 透镜 3 (历史):随机抽 10 个 E 类 · attribution 是否准
- **不可伪造证据**:每 claim 必有 `sources/` 至少 3 个 Jina 抓的 markdown
- **元审计**:`04-audit-summary.md` 顶部含 self-audit section · 标注哪些 claim 跳了哪类查询 + 理由

---

## 10 · 关键依赖文件

| 文件 | 角色 |
|---|---|
| `paper/thinking-in-cfe/00-17.md`, `99-references.md` | 17 章 paper · claim 抽取源 |
| `paper/thinking-in-cfe/02-prior-art.md` | 已有 prior-art · 审计后修正 |
| `paper/thinking-in-cfe/11-limitations-and-open-problems.md` | 已有 limitation · 审计后追加 |
| `paper/thinking-in-cfe/13-validation-and-rfc.md` | RFC framework · 审计是其 instance |
| `paper/thinking-in-cfe/99-references.md` | citation · 审计后大幅扩充 |
| `supplements/01-34/` | 26 supplement (含 12 simulator) · 也含 claim |
| `dev-notes/001-014.md` | 探索期 claim · 部分已沉淀进论文 |
| `~/.claude/skills/search-tools/references/full-sop.md` | 搜索工具降级链 |
| `~/.claude/rules/auditability.md` | 元规则底座 |
| `~/.claude/rules/prove-completeness-against-corpus.md` | 完备性证明 SOP |

---

## 11 · End-to-end test (审计完成后 reviewer 能做什么)

完成时 reviewer 应该能:

- [ ] `cat audit/04-audit-summary.md` 一页看清整体 status 分布
- [ ] `grep -l "REFUTED" audit/claims/*/assessment.md` 列出所有被驳回 claim
- [ ] 对任意 REFUTED claim · 跟 `sources/` 链接打开 → 自己读 → 自己判断
- [ ] `audit/06-novelty-defense.md` 给我们 NOVEL 部分的防御 · reviewer 能挑战
- [ ] `paper/thinking-in-cfe/18-audit-report.md` 是论文一部分 · 不是后记

---

## 12 · 起源 + 版本

- 2026-06-20 v1 · 本文件初版 · user verbatim "我选 2 · 需要写入 goal.md 让我能 /goal goal.md 推动你自主完成"
- 复制自 `~/.claude/plans/claude-code-v2-1-178-declarative-mccarthy.md` + 重组为 audit 执行版
