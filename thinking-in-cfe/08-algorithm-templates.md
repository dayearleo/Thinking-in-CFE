# 08 · 6 个算法模板

[← 返回 README](README.md)

本章提出 6 个反事实算法模板 · 每个对应一类经典算法的反事实重铸。每个模板包含:对应的经典算法 · 适用场景 · 伪代码 · 复杂度对比 · 限界条件。

## 8.1 · 模板库设计原则

每个模板满足:

- **跟一个经典算法对应** (便于读者理解 + 直接对标)
- **明确 §6.6 的 R1/R2/R3 中哪个性质 unlock 优势**
- **完整 Cost 分析** (按 §7 的 4 维度)
- **限界明确** (知道什么时候退回经典)

## 8.2 · CPA · Counterfactual Pruning Algorithm

### 经典对应

线性扫描 · `filter(predicate, list)`

### 适用场景

在 $N$ 个候选里找出满足谓词 $P$ 的子集 · 假设 sparsity ($K = |\text{hits}| \ll N$) · 评估 $P(x)$ 有 cost。

### 算法

```
INPUT:  候选集 S (size N) · 评估函数 f · 阈值 τ
GOAL:   {x ∈ S : f(x) ≥ τ}
ASSUME: K = |hits| ≪ N (稀疏)

step 1: 把 S 编码到 N 路 photonic interferometer
step 2: 每路 i 的 oracle O_i = "f(x_i) ≥ τ" 判定
step 3: Φ_OR(oracles, δ_1=1e-3) → "至少一个 hit?"
        if NO: return ∅, cost = 0 (no oracle fired)
step 4: Φ_COUNT(oracles, δ_2=1e-3) → "总共多少个 hit?" (count K)
step 5: Φ_LOC(oracles, δ_3=1e-3) iterated K 次 → 定位每个 hit
step 6: 对定位到的 K 个 · 真实评估 f (此步才付经典代价)
```

### Cost (§7 多维度)

- $D_1 = O(\sqrt{N}/\delta \cdot K)$ (略劣于经典线性扫描)
- $D_2 = K\delta$ (远优 · 因大部分 oracle 没触发)
- $D_3 = O(K\delta)$
- $D_4 = $ medium (photonic IFM)
- 真实经典 evaluation cost = $K$ 次 (远小于 $N$)

### 加速比

$N/K$ · 由 sparsity 决定。典型 wafer 检测 $\sim 100\times$。

### 限界

sparsity 假设失败 ($K \approx N$) 时退化为线性 · 但不变差太多 (常数倍 overhead)。

## 8.3 · CBB · Counterfactual Branch-and-Bound

### 经典对应

Branch-and-Bound 求最优化 (TSP / 整数规划 / SAT 求解)

### 适用场景

组合优化 · 搜索树有大量分支需 prune · 每个 prune 检查 ("此分支是否能优于当前 best") 有 cost。

### 算法

```
INPUT:  优化问题 P · 搜索树 T (root + branches)
GOAL:   全局最优解

queue := [root]
best  := -∞
while queue 非空:
  node := queue.pop()
  
  # 反事实剪枝判断
  if Φ_CF[bound(node) ≤ best](node) == True:
    continue   # 此分支被 prune · oracle 大部分时间没触发
  
  if node 是 leaf:
    best := max(best, evaluate(node))   # 这才付实际代价
  else:
    queue.extend(children(node))
```

### Cost

- 反事实 bound 判定:$O(\sqrt{N_{\text{branches}}}/\delta)$ · 大部分 prune 不触发实际 bound 计算
- 真实 leaf 评估:$O(K_{\text{leaves visited}})$ · 比经典 BB 少很多 (因为 prune 更精)

### 加速比

依赖 prune 比例 · 实测可能 10×-100× 经典 BB

### 限界

需 bound 函数能编为 quantum oracle · 不是所有问题都满足

## 8.4 · CAL · Counterfactual Active Learning

### 经典对应

Active learning (uncertainty sampling / query-by-committee)

### 适用场景

ML 训练 · 标注 cost 高 · 想用最少 label 训练好模型

### 算法

```
INPUT:  unlabeled pool U (size N) · model M · budget B
GOAL:   选 B 个最 informative samples · label 它们

step 1: 对每 unlabeled x_i · 定义 oracle O_i = "informative(x_i, M)" 判定
        (informative 通常基于 model uncertainty)
step 2: 反事实预筛 · Φ_CF[top-B informative] 给 B 个 candidate ids
        (预筛过程不真触发 informative 计算 · 大部分情况)
step 3: 对 B 个 candidate 真实 query informative score 排序
step 4: 真实 label 这 B 个 · 加入训练集
step 5: 重训 M · 回 step 1 (循环)
```

### Cost

- 反事实预筛:不付 informative score 计算的成本 (model forward pass 不便宜)
- 真实 query:$B$ 次 · 远少于 $N$
- 经典 active learning:每 round 算所有 $N$ 个 score · 成本 $N \times \text{forward pass}$

### 加速比

$N/B$ · 通常 100×-1000× (因为 $B$ 通常 $\sim$ 10-100, $N$ 可能 $10^5+$)

### 限界

需 informative oracle 能编为物理 oracle · 当 model 在远程 server 时不适用 (跟 §9.4 反模式 2 同)

## 8.5 · CV · Counterfactual Verification

### 经典对应

签名验证 / token 验证 / 凭证检查

### 适用场景

需要确认某 token / credential / signature 有效性 · 但每次验证会:
- 消耗一次性 token quota
- 暴露给对手 (验证被监控)
- 触发审计 log

### 算法

```
INPUT:  待验证 token t · 验证 oracle V (经典 verification function 包装的 quantum oracle)
GOAL:   y = V(t) ∈ {valid, invalid}

result := Φ_CF[V](t, δ=1e-6)
return result
```

### Cost

- 单次反事实验证 · oracle 触发率 $\leq \delta$
- 如果 $\delta = 10^{-6}$ · 平均 $10^6$ 次反事实验证才会真消耗一次 token quota
- 多次验证累积:$N$ 次反事实 · 期望消耗 $N\delta$ 次真 token

### 加速比

不是"加速" · 是"省 token quota" · $1/\delta$ 倍

### 限界

- token 必须能编为物理 oracle (single-photon authentication / quantum money 兼容)
- 对手如果在 $\delta$ 触发的极小概率事件下仍能检测 · CF 性质丢失

### 跟 Wiesner quantum money 的关系

[Wiesner 1969] 提出 quantum money 可以 "被 bank 验证而不被消耗" · 概念上跟 CV 一致。CV 推广到任意 V function · 不限于 quantum money 协议。

## 8.6 · CA* · Counterfactual A* Search

### 经典对应

A* 路径搜索 / heuristic search

### 适用场景

图上找 shortest path · 但每个"路径展开" (expand a node) 有 cost (例如 robotics 中真物理移动 robot 探测)

### 算法

```
INPUT:  graph G · start s · goal g · heuristic h
GOAL:   shortest path s → g

open := priority queue [s]
while open 非空:
  current := open.pop_min(by f = cost + h)
  if current == g: return reconstruct_path()
  
  for neighbor in expand(current):
    # 反事实判断 neighbor 是否值得展开
    if Φ_CF[promising(neighbor, current_best)](neighbor) == True:
      open.push(neighbor, f(neighbor))
    # 不 promising 的 neighbor 物理上没被 expand
```

### Cost

- 反事实 promising 判定:大部分 neighbor 不真 expand
- 真实 expand:只对幸存的 promising 节点
- 经典 A*:expand 所有 neighbor

### 加速比

依赖 heuristic 锐度 · 通常 5×-50× 经典 A*

### 限界

- promising 判定需要能编为 quantum oracle
- robotics 等 physical agent · 反事实判断只在 simulator 里有意义 · 真物理 expand 仍要付代价

## 8.7 · CGTS · Counterfactual Game Tree Search

### 经典对应

MCTS (Monte Carlo Tree Search) / alpha-beta pruning

### 适用场景

零和博弈 · 玩家轮流走 · 需 rollout 评估局面价值。Rollout 本身**对对手可见**时 (adversarial setting · 例如 cybersec wargame · 高频交易) · 反事实价值巨大。

### 算法

```
INPUT:  game state s · player P · depth d
GOAL:   best move

if d == 0 or s 是 terminal: return evaluate(s)

best_value := -∞
for move in legal_moves(s):
  new_state := apply(s, move)
  
  # 反事实 rollout · 对手不知道我们在 simulate
  value := Φ_CF[CGTS(new_state, opponent(P), d-1)](rollout_oracle)
  
  if value > best_value:
    best_value := value
    best_move := move

return best_move
```

### Cost

- 反事实 rollout:大部分 simulate 不触发 (对手观察不到)
- 经典 MCTS:每次 rollout 都触发 + 留痕 (对手可能 detect)

### 加速比

不是"加速" · 是"隐蔽性" · 经典做不到

### 限界

- 仅在 adversarial setting (对手会观察我们的 rollout) 有意义
- single-player 优化场景 (例 solitaire) 经典 MCTS 已够 · CGTS 无优势

## 8.8 · 6 个模板的共同模式

提取出来的 design pattern:

### 通用骨架

```
1. 把候选 / 分支 / 状态 encode 为 N 路 oracle
2. 用 Φ_CF[某 predicate] 做 counterfactual filter
3. 幸存的少数才付真实评估代价
4. 必要时迭代
```

### 何时使用 CFE 算法 (决策树摘要)

```
Q1: 问题是否有 sparsity / side-effects / verify-without-commit 性质?
  - 都没有 → 用经典算法
  - 有 → Q2

Q2: 候选 / 分支 / 状态能否 encode 为物理 oracle?
  - 不能 → 用经典算法
  - 能 → Q3

Q3: N 在 photonic 硬件能处理的范围 ($\leq$ 100) 吗?
  - 不在 → 等硬件 / 用经典
  - 在 → Q4

Q4: 有对应的算法模板 (§8 6 个之一)?
  - 没有 → 用 §4 组合代数自定义
  - 有 → 跑
```

详细决策树见 §9.5。

### 共同设计原则

- **稀疏才有意义** · $K \ll N$
- **真实评估的 cost >> 反事实评估的 cost** · 否则没动机
- **物理 oracle 是核心约束** · 数字 oracle 都不适用

## 8.9 · 尚未模板化的方向

后续工作可以模板化:

- **CDB · Counterfactual Database query** (private information retrieval 反事实版)
- **CC · Counterfactual Compiler optimization** (反事实静态分析)
- **CD · Counterfactual Debugging** (反事实 trace · 看 bug 在不在某 path 上)
- **CR · Counterfactual Recommendation** (反事实 A/B test · 不真 expose user)
- **CG · Counterfactual Generative model sampling** (反事实拒采样)

每个都需要单独深度分析 (后续工作)。

## 8.10 · 小结

6 个算法模板把 CFE 算子体系从抽象提升到具体可用。每个模板:

- 对应一类经典算法
- 用 §3 算子 + §4 组合代数构造
- 在 §7 多维复杂度下分析
- 体现 §6 减法范式的不同侧面

下一章 (§9) 给出方法论 · 帮领域专家把自己问题 cast 成本章某个模板。

---

[← 上一章 · 07 复杂度分析](07-complexity-analysis.md) · [下一章 · 09 代数化方法论 →](09-problem-algebraization.md)
