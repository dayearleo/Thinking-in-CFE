# 09 · 问题代数化方法论

[← 返回 README](README.md)

## 9.1 · 为什么需要方法论

新计算范式刚提出时 · 应用都靠领域专家 + 算法学家**反复对话**完成 · 没有清晰方法论 → 应用化周期慢。

历史先例:

- **早期 MapReduce** (2004-2006) [Dean-Ghemawat 2004]:一个问题套不套 MapReduce 全靠工程师直觉 · 后来 MapReduce Design Patterns 书 [Miner-Shook 2012] 才给出方法论
- **早期 Deep Learning** (2010-2015):一个问题"能不能 deep learn"靠直觉 · 后来才有方法论
- **早期 Microservices**:怎么拆 service 完全靠经验 · 后来才有 Domain-Driven Design [Evans 2003]

我们当前处在 CFE 应用最早期。**系统化方法论能加速 10× 应用周期**。本章建立 5 步 SOP + 4 案例研究 + 7 题决策树 + 5 个反模式。

## 9.2 · 5 步代数化 SOP

### Step 1 · 问题刻画

把领域问题写成数学陈述。要找到:

- **输入集** $\mathcal{X}$ (例 N 个 sample / N 个网络节点 / N 个 token)
- **目标判定** $f: \mathcal{X} \to \{0,1\}$ (例 "有缺陷?" / "有 trap?" / "有效?")
- **当前评估方式** · 经典上怎么算 $f(x)$? cost 是多少?

### Step 2 · 寻找 R1/R2/R3 trigger

检查问题里是否有 §3.7 的 3 个性质之一:

- **R1 trigger** · 触发率任意小有价值? (测试是否会销毁 / 消耗 / disturb sample)
- **R2 trigger** · adversary 不可检测有价值? (测试是否会暴露给对手)
- **R3 trigger** · 输入不消耗有价值? (输入是稀缺资源 · 测了就少一个)

至少一个 trigger 触发才值得继续。三个都不触发 → 用经典算法 · 不要硬套 CFE。

### Step 3 · oracle 物理化检查

CFE 算子要求 oracle 是物理实体 · 检查:

- 问题里的 $x_i$ 是**物理对象** (样本 / sensor / 物质) 还是**抽象数据** (远程 API / 数据库行)?
- $x_i$ 能否被 photon 物理 probe? (光路径穿过 / 反射 / 吸收 能否表达 $x_i$ 的属性?)
- 如果不能 · 但有间接物理表达 (例 用 single-photon detector 表达 sensor 响应) · 该怎么 wrap?

不能物理化 → 退出 · 不适用 CFE。能物理化但需要 wrap → 设计 wrapper interface。

### Step 4 · 选模板

从 §8 的 6 个模板里匹配:

| 问题特征 | 选模板 |
|---|---|
| 稀疏 + 评估贵 + 找 hit | CPA (Pruning) |
| 组合优化 + 大量分支 prune | CBB (Branch-and-Bound) |
| ML 训练 · 标贵 · 选谁标 | CAL (Active Learning) |
| token / signature 验证 · 不消耗 | CV (Verification) |
| 路径搜索 · expand 贵 | CA* (A* Search) |
| 博弈 · rollout 对手可见 | CGTS (Game Tree Search) |
| 都不匹配 | 自定义 · 用 §4 组合代数构造新算法 |

### Step 5 · Cost 验证

用 §7 多维复杂度框架算出反事实算法的预期 cost:

- 真实 oracle 触发期望 = $\delta \cdot B(f)$
- 真实经典评估 cost = (surviving items) $\times$ (per-evaluation cost)
- 跟经典算法 cost 在每个维度直接比

如果反事实算法在所有 matter 的维度上都不优于经典 → 不要硬上 · 用经典。如果反事实算法显著优 (>3×) 且劣势维度可接受 → 进入实施。

## 9.3 · 4 个案例研究

### 案例 1 · 半导体晶圆缺陷扫描

**Step 1**:
- $\mathcal{X}$ = 一片 wafer 上的 $N$ 个 die
- $f$ = "die_i 是否有缺陷"
- 当前评估:逐 die 扫描 · 高分辨率成像 · 每 die 引入 photo-damage

**Step 2**:**R1 trigger** · 扫描有 photo-damage · 反事实扫描可以避免

**Step 3**:**物理化 ✅** · 每 die 是物理区域 · photon 路径直接物理 probe (相干光照射 die · 缺陷会散射 · 散射 = obstacle)

**Step 4**:选 **CPA** · 大部分 die 没缺陷 (sparsity 满足)

**Step 5**:
- 经典:$N$ 次高分辨扫描 · $N \times \text{cost}_{\text{scan}}$
- CPA:反事实预筛 · 真扫描只对 K 个 hit · $K \times \text{cost}_{\text{scan}}$ where $K \ll N$
- 加速 = $N/K$ · 典型 wafer $\sim 100\times$

**结论**:适合 CFE · 优先级高。

### 案例 2 · 信用卡欺诈检测 (反例 · 不适合)

**Step 1**:
- $\mathcal{X}$ = $N$ 笔交易
- $f$ = "transaction_i 是否欺诈"
- 当前评估:每笔过 ML 模型 · GPU inference

**Step 2**:**R1/R2/R3 都不 trigger** · 评估不破坏交易 · 不暴露给对手 · 不消耗资源

**Step 3**:**物理化 ❌** · 交易是数字记录 · 不能物理 probe

**结论**:不适合 CFE · Step 2 就该停。用经典 ML inference。**这是反模式 · 强行套 CFE 会自残**。

### 案例 3 · 单细胞多 assay 同时检测

**Step 1**:
- $\mathcal{X}$ = 1 个单细胞 + $N$ 种 assay (表面 markers / gene expression / metabolic state)
- $f$ = vector $(f_1, ..., f_N)$ where $f_i$ = "assay_i 结果"
- 当前评估:常规免疫荧光 · 每 assay 引入 photo-bleaching · 一个细胞只能测 $\sim 3-5$ assay 就死

**Step 2**:**R1 + R3 trigger** · 评估会破坏样本 + 样本稀缺

**Step 3**:**物理化 ✅** · 每个 assay 用不同波长 / polarization · photon 路径物理穿过细胞

**Step 4**:不在 6 模板中直接对应 · 但接近 **CAL** (选哪几个 assay 真测) 或**自定义** (parallel evaluation)

**Step 5**:
- 经典:测 3-5 assay 后细胞死 · 其余 assay 无法测
- CFE:反事实测全部 N · 大部分不触发 · 真消耗的 photon 远少于经典
- 收益:同一细胞测 N 个 assay (N 可能 20-50)

**结论**:适合 CFE · 商业价值大 · 跟生物显微镜厂商合作可能。

### 案例 4 · honeypot / canary 探测 (军用情报)

**Step 1**:
- $\mathcal{X}$ = $N$ 个可疑物理设备 (摄像头 / 监听器 / 物理 sensor)
- $f$ = "device_i 是否 active"
- 当前评估:无源探测 + 频谱分析 · 主动探测就 leak 信号给对手

**Step 2**:**R2 trigger** · adversary 不可检测查询有巨大价值

**Step 3**:**物理化 ✅** · device 是物理对象 · 电磁场 / 光信号能耦合

**Step 4**:**CPA** + 反事实 OR · 找出 "有任何 active device 吗?"

**Step 5**:
- 经典:主动探测一定 leak · cost = 损失情报优势
- CFE:反事实探测 · 物理上不留痕 · 对手不知
- 收益:不可替代 · 不是 cost 比较 · 是 capability 比较 (经典做不到)

**结论**:适合 CFE · 军用 / 情报 niche · 客户少但 ARPU 高。

## 9.4 · 重构反模式 (看到立即停)

### 反模式 1 · 硬套 (R1/R2/R3 都不 trigger 仍上 CFE)

**症状**:领域问题 evaluation 没副作用 / 不暴露 / 不消耗 · 但开发者觉得 "酷" 就用 CFE。

**后果**:CFE 比经典慢 (因为 $\delta$ overhead) · 且需要复杂硬件 · 100% 失败。

**正确做法**:Step 2 不通过就退。

### 反模式 2 · 物理化伪装 (oracle 不是真物理但开发者假装是)

**症状**:把远程 API call 包装成 "假 oracle" · 想用 CFE 减少 API quota。

**后果**:CFE 算子根本不能 query 远程经典 API · 你 wrap 出来的"oracle"本身就是 N 次 API call · 没省任何 cost。

**正确做法**:Step 3 物理化失败就退 · 不要假装。

### 反模式 3 · Sparsity 假设强行成立 (实际 $K \approx N$)

**症状**:用 CPA 但实际大部分候选都 hit。

**后果**:反事实预筛没 prune 掉任何东西 · 真实评估仍 $\approx N$ 次 · 加上 $\delta$ overhead 反而更慢。

**正确做法**:Step 5 cost 验证发现 $K \approx N$ 就退 · 用经典。

### 反模式 4 · 嵌套深度失控

**症状**:用 C3 嵌套构造算法 · 嵌套 10+ 层。

**后果**:$\delta_{\text{tot}} = 10\delta$ 把反事实性破坏 · 等于经典 evaluation。

**正确做法**:嵌套深度 $\leq 3$ · 或加 reset 屏障 (§4.4)。

### 反模式 5 · 忽略硬件 N 上限

**症状**:设计算法假设 $N = 1000$ photonic mode · 实际 SOTA $N = 12$。

**后果**:跑不起来 · 或要等硬件成熟。

**正确做法**:Step 5 + 硬件检查 · 当前 $N \leq 32$ 才考虑实物 demo。

## 9.5 · 决策树 · 某问题适不适合 CFE

```
START
  │
  ▼
[Q1] 评估有 R1/R2/R3 中至少一个 trigger 吗?
  │  No  → ❌ 用经典算法
  │  Yes ↓
[Q2] 输入能物理化 (光 / 微波 / spin) 吗?
  │  No  → ❌ 用经典算法
  │  Yes ↓
[Q3] N 在硬件可行范围 ($\leq 32$ 当前 / $\leq 100$ 中期)?
  │  No  → ⏸ 暂存方案 · 等硬件
  │  Yes ↓
[Q4] 有对应的算法模板吗 (§8 6 个之一)?
  │  No  → 自定义 (用 §4 组合代数构造) · 复杂度高
  │  Yes ↓
[Q5] Sparsity / cost-asymmetry 假设成立?
  │  No  → ❌ 用经典 · CFE 没优势
  │  Yes ↓
[Q6] 反事实算法 cost < 经典 cost 至少 3×?
  │  No  → 边际收益 · 不值得搞 CFE
  │  Yes ↓
[Q7] 嵌套深度 $\leq 3$ 或有 reset 策略?
  │  No  → 改设计 · 减嵌套
  │  Yes ↓
✅ 适合 CFE · 进实施
```

## 9.6 · 方法论的局限

本方法论是**启发式** · 不是定理。两个局限:

- **Step 2 的 R1/R2/R3 判断主观** · 不同领域专家可能判断不同
- **Step 5 的 cost 比较依赖 sparsity 估计** · 估错时方法论给错误答案

防止方法论被滥用的措施 · 见 §11 关于元层警示。

## 9.7 · 小结

本章给出领域专家把传统问题 cast 成 CFE 表达式的 5 步 SOP + 7 题决策树 + 5 反模式。配合 §3 算子 + §4 代数 + §8 模板 + §10 具体问题清单 · 构成完整的应用层方法论。

---

[← 上一章 · 08 算法模板](08-algorithm-templates.md) · [下一章 · 10 6 个可挑战问题 →](10-six-challengeable-problems.md)
