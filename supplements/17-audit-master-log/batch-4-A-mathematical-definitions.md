# Batch 4 · A 类数学定义类 25 条 · 批量审计

> 高效模式:每 claim 不再单独 source/query/findings/sources 子目录 · 直接 1 行 verdict
> 元方法:跟 §03/§04 章节内容对账 · 数学一致性 audit · 不再跑 EXA (因 A 类多是 internal definition 一致性 · 不是外部 attribution)
> 例外:跟 [Lin-Lin 2015] 对照的 claim (E-004 已审 PARTIAL) · 这里 inherit 同结论

---

## 审计方法论

A 类是**论文内部数学一致性** audit · 4 步:

1. Read claim 原文 (§03/§04)
2. 检查定义是否自洽 (P1/P2/P3 跟下游定理一致?)
3. 跟 prior-art (Lin-Lin 2015 / Mitchison-Jozsa 2001) 对账
4. 标 status

---

## 25 条 A 类 audit verdict

### AUD-C00-001 · 算子是 Counterfactual Function Evaluation Operator

- **CONFIRMED** ⭐⭐⭐⭐⭐
- 摘要中的定义是 §03 形式定义的 informal 版本 · 一致
- 抽象自 [Elitzur-Vaidman 1993] + [Mitchison-Jozsa 2001] 准确

### AUD-C03-001 · P1 正确性 $\Pr[y=f(\mathbf{x})] \geq 1-\epsilon$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- 标准 quantum algorithm correctness condition · 类比 BQP 复杂度类定义
- $\epsilon \in (0, 1)$ 范围合理

### AUD-C03-002 · P2 反事实性 $\Pr[O_i \text{ 触发}] \leq \delta$ for $x_i=1$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- IFM 物理性质的精确数学化 · 跟 Elitzur-Vaidman 1993 + Kwiat 1995 chained Zeno 一致
- 注意:$x_i=1$ 才有 obstacle · 才有 trigger 风险 · 条件正确

### AUD-C03-003 · P3 代价 $B_\delta(f) = O(Q(f)^2/\delta)$

- **PARTIAL** ⭐⭐⭐⭐
- 见 AUD-E-004 详细 audit · Lin-Lin 2015 原版无 $\delta$ 参数 · 我们做了 $\delta$ extension 但未明确化
- 必须修 §03.2 加 explicit "this is δ-parameterized extension of Lin-Lin 2015"

### AUD-C03-004 · 工程取值 $\epsilon \sim 10^{-3}$, $\delta \in [10^{-2}, 10^{-6}]$

- **CONFIRMED** ⭐⭐⭐⭐ · GAP one caveat
- 合理工程取值 · 但当前 lab IFM efficiency (5 dB loss · single-link >99%) 对应 $\delta \sim 10^{-2}$
- $\delta = 10^{-6}$ 工程取值偏 aggressive · 需 N=12+ 高保真 setup
- 加 caveat:"projected · not yet demonstrated at $\delta=10^{-6}$ scale"

### AUD-C03-005 · $\delta \to 0$ 极限 $B(f) \to \infty$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- 直接 from P3 公式 · trivial

### AUD-C03-006 · $\delta = 1$ 退化为 standard quantum query

- **CONFIRMED** ⭐⭐⭐⭐⭐
- 跟 Lin-Lin 2015 原版 $B(f) = \Theta(Q(f)^2)$ 在 $\delta = 1$ 时一致

### AUD-C03-007 · $N=2, f=$NOR 还原为 Elitzur-Vaidman bomb tester

- **CONFIRMED** ⭐⭐⭐⭐⭐
- Elitzur-Vaidman 1993 原版 bomb tester $f =$ "no bomb" $= \neg x = $ NOR_1 · $N=1$ (或 $N=2$ with 2 path)
- 跟 §03.4 极限退化条件一致

### AUD-C03-008 · $f=$NAND-tree 还原为 Farhi-Childs bomb 版

- **CONFIRMED** ⭐⭐⭐⭐⭐
- 跟 Lin-Lin 2015 §6 "Bomb query upper bound on read-once formula" 一致
- Farhi 2008 quantum walk · Childs 2009 discrete · 都能在 bomb query model 下表达

### AUD-C03-009 · $\Phi^{CF}_{\text{OR}}$: $B = O(\sqrt{N}/\delta)$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- $Q($OR$) = \Theta(\sqrt{N})$ Grover · 代入 $B_\delta = O(Q^2/\delta) = O(N/\delta)$
- 但 OR Bomb query 实际 better:Lin-Lin 2015 §3.2 给 $B($OR$) = \Theta(N/\log^2 N \cdot 1/\delta)$ 或类似
- §03.5 写 $\sqrt{N}/\delta$ 可能太 optimistic · 应改 $O(N/\delta)$ 或 verify Lin-Lin 精确 bound
- 这是 **PARTIAL** ⭐⭐⭐⭐ · 数学需精确化

### AUD-C03-010 · $\Phi^{CF}_{\text{AND}}$: $B = O(\sqrt{N}/\delta)$

- **PARTIAL** ⭐⭐⭐⭐
- 同上 · AND 跟 OR 对偶 · 同样需 verify 精确 bound

### AUD-C03-011 · $\Phi^{CF}_{\text{MAJ}}$: $B = O(N/\delta)$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- $Q($MAJ$) = \Theta(\sqrt{N})$ · $B = O(N/\delta)$ 跟 $Q^2/\delta$ 一致

### AUD-C03-012 · $\Phi^{CF}_{\text{COUNT}}$: $B = O(\sqrt{N \cdot \text{ans}}/\delta)$

- **PARTIAL** ⭐⭐⭐⭐
- $Q($COUNT$) = \Theta(\sqrt{N \cdot \text{ans}})$ · 代入 $B_\delta = O(Q^2/\delta) = O(N \cdot \text{ans} /\delta)$
- §03.5 写 $\sqrt{N \cdot \text{ans}}/\delta$ 漏了平方 · 应改 $(N \cdot \text{ans})/\delta$
- 这是数学 typo 错误

### AUD-C03-013 · $\Phi^{CF}_{\text{T}_t}$: $B = O(\sqrt{Nt}/\delta)$

- **PARTIAL** ⭐⭐⭐⭐
- 同上 · 漏平方

### AUD-C03-014 · 只有 $\Phi^{CF}_f$ 同时具备 R1+R2+R3 (核心 differentiator)

- **CONFIRMED** ⭐⭐⭐⭐⭐
- R1 (触发率任意小) R2 (adversary 不可检测) R3 (输入不消耗) 是 IFM 的物理 trifecta
- 经典 + Grover 都不可同时具备 · 跟 §03.7 表格一致

### AUD-C04-001 · 5 种组合 C1-C5

- **CONFIRMED** ⭐⭐⭐⭐⭐
- 5 种是封闭可组合 set · 跟 Reichardt 2010 + Belovs 2012 quantum algorithm composition 类比

### AUD-C04-002 · C1 串行 $\delta_\text{tot} \leq \delta_f + \delta_g$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- Union bound 标准 · trivially correct

### AUD-C04-003 · C2 并行 $\delta_\text{tot} = \max(\delta_f, \delta_g)$

- **PARTIAL** ⭐⭐⭐⭐
- 独立事件 max 是 OK · 但严格说应 $\leq \delta_f + \delta_g - \delta_f \delta_g \approx \max$ for small $\delta$
- 这是 informal 估计 · 可 accept

### AUD-C04-004 · C3 嵌套 $\delta_\text{tot} \leq \delta_f \cdot N_\text{deep} + \delta_g$

- **PARTIAL** ⭐⭐⭐⭐
- 嵌套深度 union bound · 跟 §11 open Q1 一致 (待严格证明)
- 实际可能更糟 (multiplicative interplay)

### AUD-C04-005 · C4 条件 $\delta_\text{tot} \leq \delta_f + \max(\delta_g, \delta_h)$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- 一条分支 union bound · OK

### AUD-C04-006 · C5 迭代 $\delta_\text{tot} \leq k \cdot \delta_f$

- **CONFIRMED** ⭐⭐⭐⭐⭐
- $k$ 次 union bound · OK

### AUD-C04-007 · Cost theorem 是 "合理估计" 不是严格证明

- **CONFIRMED** ⭐⭐⭐⭐⭐ (self-declared limitation · 透明)
- 这是 §04.3 + §11 open Q1 的 honest disclosure · 合规

### AUD-C04-008 · 嵌套深度 100 → $\delta_\text{tot} = 10^{-1}$ 反事实性丢光

- **CONFIRMED** ⭐⭐⭐⭐⭐
- $\delta = 10^{-3}$ × 100 = 0.1 trivially correct

### AUD-C04-009 · CFE 跟 indefinite causal order (ICO) 是正交方向

- **CONFIRMED** ⭐⭐⭐⭐ · 加 caveat
- ICO (Brukner-Costa-Oreshkov 2012) 跟 CFE 确实不同 axis
- 但严格说"正交"需更多 formal argument
- §04.7 写法 OK

### AUD-C06-001 · 减法计算范式 (SCP) 是新提出

- **跟 AUD-C06-002 重复** · 已审 NOVEL ⭐⭐⭐⭐
- merge as cross-ref

---

## Batch 4 汇总

| Status | 数 |
|---|---|
| CONFIRMED | 15 |
| PARTIAL | 8 (C03-003 / 004 / 009 / 010 / 012 / 013 / C04-003 / 004) |
| REFUTED | 0 |
| NOVEL | 1 (C06-001 = C06-002 merge) |
| Cross-ref | 1 (C06-001) |

### 🚨 Batch 4 关键发现

#### Finding 4.1 · 子算子 cost 公式漏 $Q(f)^2$ 平方 (C03-009/010/012/013)

§03.5 表中 OR/AND/COUNT/T_t 的 $B$ 公式漏了平方 · 应该是:

| 算子 | §03.5 写法 | 应该是 |
|---|---|---|
| $\Phi^{CF}_{\text{OR}}$ | $O(\sqrt{N}/\delta)$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{AND}}$ | $O(\sqrt{N}/\delta)$ | $O(N/\delta)$ |
| $\Phi^{CF}_{\text{COUNT}}$ | $O(\sqrt{N \cdot \text{ans}}/\delta)$ | $O(N \cdot \text{ans}/\delta)$ |
| $\Phi^{CF}_{\text{T}_t}$ | $O(\sqrt{Nt}/\delta)$ | $O(Nt/\delta)$ |

原因:从 $B_\delta(f) = O(Q(f)^2/\delta)$ 推 · $Q($OR$) = O(\sqrt{N})$ · 平方变 $N$ · 不是 $\sqrt{N}$。

**修订要求**:§03.5 表必须重新计算所有 $B$ 公式 · 或 verify 跟 Lin-Lin 2015 原版精确 bound。

#### Finding 4.2 · Cost composition theorem 是草案不是定理

§04.3 已经 explicit 标 "合理估计 · 不是严格证明" · §11 Q1 列为 open · 这是 honest practice。

#### Finding 4.3 · ICO 正交说法 weak

§04.7 "CFE 跟 ICO 正交" 缺 formal argument。建议改 "CFE 跟 ICO 是不同 axis · 可以组合" 较 honest。

---

## 触发的论文修订动作 (P0)

1. §03.5 子算子 cost 表 · 修 4 个公式 (OR/AND/COUNT/T_t)
2. §03.2 P3 加 "this is δ-parameterized extension of [Lin-Lin 2015]"
3. §04.7 ICO 句子 soften

(以上跟 batch 1 发现的 Lin-Lin extension 修订要合并)
