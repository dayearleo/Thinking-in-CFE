# Goal · CFE 论文 230 claim 现实性审计 · 跨 session 自主驱动协议

> **任何未来 AI 收到 `/goal goal.md` 命令 · 读完本文件就能续作 · 不需要 user 重新解释 context**
> 受众:future AI · 速查版 · ~250 行
> 长文版方法论 → `00-master-plan.md` (500 行 · 详细推理 + 候选讨论)

---

## 0 · 一句话目标

对 `Thinking in CFE` 全部 **230 条可审计 claim** 跑严密联网搜索审计 ·
用 EXA / Serper / Jina 三引擎 + 双语 + 双时段 ·
每条 claim 留**不可伪造面包屑** ·
把审计本身作为论文 **§18** + **supplement 17** 落盘 ·
完备性证明 (forward + backward remainder=0) 通过才算完成。

---

## 1 · 任何 AI 接手的 5 步 onboarding

```
1. Read 本 goal.md 全文              (你正在做 ✓)
2. Read audit/01-claim-registry.md   (看进度 · 找下一个 status=UNVERIFIED 的 claim)
3. Read audit/00-master-plan.md      (看完整 7 步流程 + 元规则 M1-M4)
4. Read audit/02-keyword-matrix.md   (看关键词矩阵 + curl 模板)
5. 选下一个 P0 UNVERIFIED claim · 走 7 步 · 落盘 · update registry · commit
```

不需要回看任何之前对话。所有 context 都在 audit/ 目录里。

---

## 2 · 完成判据 (terminal state)

整个工程完成的 acceptance criteria:

- [ ] `audit/01-claim-registry.md` 230 条全部 `status ∈ {CONFIRMED, PARTIAL, GAP, REFUTED, NOVEL}` · 无 `UNVERIFIED` 残留
- [ ] `audit/04-audit-summary.md` 写完整体统计 · 含直方图 + Top 20 发现
- [ ] `audit/05-gap-report.md` 写完真 Gap 清单 + 建议补强路径
- [ ] `audit/06-novelty-defense.md` 写完 NOVEL 部分 prior-art 防御
- [ ] `audit/07-prior-art-corrections.md` 写完 §02 修订建议
- [ ] `paper/thinking-in-cfe/18-audit-report.md` 写完 (论文新章节)
- [ ] `paper/thinking-in-cfe/02-prior-art.md` 按 audit/07 更新
- [ ] `paper/thinking-in-cfe/11-limitations-and-open-problems.md` 按 audit/05 追加 Gap
- [ ] `paper/thinking-in-cfe/99-references.md` 按 audit 扩充 citation
- [ ] `supplements/17-audit-master-log/` 全部 audit/ 内容备份
- [ ] git status 干净 · 每 10 claim 一次 commit
- [ ] 完备性证明跑通:`find audit/claims -maxdepth 1 -type d | wc -l == 231` (230 claim + claims/)

---

## 3 · 每个 session 起手 SOP (强制 · 不许跳)

```bash
# Step 1 · 检查上轮欠债
cd "<your-clone-path>/Thinking-in-CFE"
grep -L 'status:' audit/claims/*/assessment.md 2>/dev/null
# ↑ 如果输出非空 · 有 half-done claim · 必先收尾再开新

# Step 2 · 看当前进度
head -20 audit/01-claim-registry.md
# ↑ 看顶部进度统计 + 下一待审

# Step 3 · 选下一 P0 UNVERIFIED
grep "P0 | UNVERIFIED" audit/01-claim-registry.md | head -5
# ↑ 选第一条 · 按 AUD-XXX 编号开始

# Step 4 · 创建 claim 目录
mkdir -p audit/claims/AUD-XXX/sources
# ↑ XXX = 选定的 claim ID

# Step 5 · 走 7 步流程 (详 00-master-plan §5)
```

---

## 4 · per-claim 7 步流程 (速查 · 详 00-master-plan §5)

每 AUD-XXX 必走 7 步:

| 步 | 动作 | 产物文件 |
|---|---|---|
| 1 | 抽 claim 原文 + 来源 file:line | `claims/AUD-XXX/source.md` |
| 2 | 设计 4 类 query (Novelty/Math/Physics/Differentiation) | `claims/AUD-XXX/query-plan.md` |
| 3 | 跑 EXA + Serper + Jina · 英中双语 + 双时段 | `claims/AUD-XXX/search-log.md` |
| 4 | 抓 top 5 源 (Jina markdown) | `claims/AUD-XXX/sources/<n>-<short-id>.md` |
| 5 | 提取关键引用段 + 跟 claim 对账 | `claims/AUD-XXX/findings.md` |
| 6 | 判 status + 证据强度 1-5 星 | `claims/AUD-XXX/assessment.md` |
| 7 | 更新 master registry status 列 | `audit/01-claim-registry.md` 改行 |

每 10 个 claim 完成后:

```bash
# 更新进度统计
# (顶部 Total/UNVERIFIED/CONFIRMED 等数字 update)

# commit
cd "<your-clone-path>/Thinking-in-CFE"
git add audit/claims/AUD-XXX/ audit/01-claim-registry.md audit/04-audit-summary.md
git commit -m "audit: AUD-XXX through AUD-YYY (10 claims audited)"
```

---

## 5 · 元规则 M1-M4 (不可违)

### M1 · 审计 ≠ 证明对 · 审计 = 找 Gap

预设 "可能错了 · 找证据证伪" · 不预设 "对了 · 找证据补"。

### M2 · 每条 claim 必有 4 类 query

- Novelty:有没有人 30 年前就做了?2025 最新工作覆盖没?
- Math:数学定义跟标准文献一致?
- Physics:声称硬件能做 · SOTA 数字真实?
- Differentiation:跟邻近工作 head-to-head 怎么比?

### M3 · 不可伪造面包屑

断言 "我查了 30 篇" **不算面包屑** · 必须列 30 篇 URL + 关键引用段 · 跟 `sources/` 子目录文件名一一对应。

### M4 · 全查不抽样

230 claim 一条不漏 · 不允许 "重要的审 · 次要的跳"。中途发现遗漏 claim 可追加 (走 `00-master-plan` 补漏 SOP) · 不允许已编号 claim 跳过。

---

## 6 · Status 判据 (6 选 1)

| Status | 含义 | 触发动作 |
|---|---|---|
| **CONFIRMED** ⭐⭐⭐⭐⭐ | SOTA 完全支持 | 加 citation 强化原章节 |
| **PARTIAL** ⭐⭐⭐ | 部分支持 + caveat | 原章节加 caveat |
| **GAP** ⭐⭐ | 我们说有 · 实际还没人做 | §11 / §13 加 open problem |
| **REFUTED** ⭐ | 已有反例 / 不同结论 | 改原章节 + 更新 §02 prior-art |
| **NOVEL** | 真没人做过 · 原创 | 加显式声明 + prior-art 防御 |
| **UNVERIFIED** | 未审 (初始状态) | (无 · 不能保留作终态) |

---

## 7 · 关键词矩阵速查 (详 02-keyword-matrix.md)

7 个维度 × 双语:

1. **算子定义 / 反事实计算** · `counterfactual quantum computation`, `interaction-free measurement`, 反事实量子计算
2. **复杂度 / 算法** · `bomb query Lin Lin 2015`, `NAND tree quantum walk Farhi`, 量子查询复杂度
3. **物理硬件 / 集成光子** · `integrated photonic processor N=12`, `MZI mesh nanophotonic`, 集成光子处理器
4. **密码学 / HSM** · `HSM tamper evidence quantum`, `Gottesman tamper-evident`, 硬件安全模块抗篡改
5. **范式新词防撞** · `subtractive computation`, `negation as computation`, 减法计算
6. **应用 niche** · 每 simulator 单独关键词组 (详 02-keyword-matrix.md §2 表)
7. **攻击场景** · `stealth probing`, `adversary-undetectable measurement`, 无触发探测

---

## 8 · 搜索工具 curl 模板 (含 key · 详 02-keyword-matrix.md §1)

### EXA · 主力

```bash
curl -sS -X POST "https://api.exa.ai/search" \
  -H "x-api-key: ${EXA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"query": "<KEYWORD>", "num_results": 10, "type": "auto", "contents": {"text": {"max_characters": 1500}}}'
```

### Serper

```bash
curl -sS -X POST "https://google.serper.dev/search" \
  -H "X-API-KEY: ${SERPER_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"q": "<KEYWORD>", "num": 10}'
```

### Jina · 抓全文

```bash
curl -sS -H "Authorization: Bearer ${JINA_API_KEY}" \
  "https://r.jina.ai/<URL>"
```

### arxiv 直 API (EXA 漏新 paper)

```bash
curl -sS "http://export.arxiv.org/api/query?search_query=all:<KEYWORD>&max_results=10&sortBy=submittedDate&sortOrder=descending"
```

---

## 9 · 反模式 (看到立即停)

- ❌ 跳过 claim · "这个不重要"
- ❌ 断言式审 "我读了 30 篇" 不列 source URL
- ❌ 一次 session 审完不 commit
- ❌ 审了不修论文 · audit 完不回灌 §02/§11/§18
- ❌ 只跑英文不跑中文
- ❌ 只跑全时段不跑近 12 月
- ❌ Jina 抓的 markdown 不存 sources/
- ❌ Top 3 看完就走 · 不扫 top 10
- ❌ 撞 rate limit 直接 abort (走降级链 EXA → Serper → arxiv → Jina)
- ❌ 不 update registry 顶部进度统计

---

## 10 · 跨压缩边界 resume 协议

跨压缩边界 (开机 summary 含 "continued from a previous conversation" · `SessionStart:compact` hook · claude-mem obs 不是当前 session):

1. 先按最高指示第三条 4 步补完上轮欠债
2. 再按本文件 §1 onboarding 5 步起步
3. 不预设 "上轮搞清楚什么" · 一切以 audit/ 落盘文件为准

---

## 11 · 审计本身的 audit · 元层完备性证明

按 `~/.claude/rules/auditability.md` · 审计也要可审计。完成后跑:

```bash
# Forward · 每 claim 有目录
find audit/claims -maxdepth 1 -type d | wc -l
# 期望:231 (230 claim + claims/ 自身)

# Backward · 引用 == status
grep -r "AUD-" paper/ supplements/ | wc -l
# 跟 registry 里的 status 数对账

# 三透镜复核 (随机抽 3 类 10 个)
# 透镜 1 (数学 C 类):复杂度推导跟独立源对账
# 透镜 2 (物理 B 类):SOTA 数字跟 referenced paper 对账
# 透镜 3 (历史 E 类):attribution 准
```

跑通这 3 项 · 完备性证明 PASS · 才能写 §18 闭合。

---

## 12 · session 末尾 SOP

每 session 收尾前必做:

1. 把本 session 新审的 claim status 写到 registry
2. update 进度统计 (顶部 Total/UNVERIFIED/Audited 等)
3. `git add audit/claims/<新审的目录>/ audit/01-claim-registry.md` (显式路径 · 禁 `-A`/`-.`)
4. `git commit -m "audit: AUD-XXX through AUD-YYY (N claims)"`
5. 不 push (除非 user 显式当轮同意 `推 / go / ok / yes / push it`)
6. session 末输出当前进度 + 下一 session 接手指针

---

## 13 · 起源

- 2026-06-20 v1 · user verbatim: "我选 2 · 需要全部写入 goal.md · 让我之后可以通过 /goal goal.md 推动你自主全部完成"
- 模式 X (全 230 sequential) + scope 全 (paper + supplements + dev-notes) + 落 Thinking in CFE/audit/
