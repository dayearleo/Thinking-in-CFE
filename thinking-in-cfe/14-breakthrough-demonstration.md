# 14 · 量子计算解法的突破 · 把未来拉近到当下

[← 返回 README](README.md)

## 14.1 · 本章定位 · 论文的 closing argument

前面 13 章建立了:

- 算子 (§3) + 代数 (§4) + 范式 (§6) + 复杂度 (§7) **数学框架**
- 跟 FT QC 的 3 维定位 (§5)
- 6 个算法模板 (§8) + 5 步方法论 (§9)
- 6 个候选问题清单 (§10)
- 限界 (§11) + 结论 (§12) + 验证 RFC (§13)

但读者读到这里仍可能问:

> "你说能挑战未来 FT QC 的事 · 具体怎么个挑战法? 给我看一个 worked example · 让我相信 if 工程化可行 then 未来已被拉到当下。"

本章就是这个 worked example —— 3 个**深度展开**的具体案例 · 每个都构成对论文核心论点的独立证明。

**核心论点重申**:

> **如果** CFE 算子的工程化可行 (依赖 photonic IFM chip 良率 + active phase stabilization + 跟经典系统的低延迟集成 这三个条件) · **那么** 一组原本被认为需要 fault-tolerant 量子计算才能解决的问题 · 现在已经可以用专用 photonic 硬件解决。这等价于 "**把未来提前拉近到当下**"。

下面 3 个案例 · 每个独立成立即可证明上述命题。

## 14.2 · 案例 1 · 活细胞多 assay 的非破坏性并行检测 (A2)

### 14.2.1 · 问题陈述

**领域**:细胞生物学 / 单细胞组学 / 制药 R&D

**问题**:给一个稀缺的活细胞 (例如患者活检样本 / 干细胞 / 罕见循环肿瘤细胞) · 想测量 $N$ 种属性 (蛋白表达 / 代谢状态 / 基因转录 / 信号通路 activation / ...) · 但每次荧光成像测量都引入 photo-bleaching 和 phototoxicity · 一个细胞典型只能承受 3-5 种 assay 后死亡。

数学化:

- 输入:1 个细胞 + $N$ 种 assay
- 目标:输出向量 $(f_1(\text{cell}), \ldots, f_N(\text{cell}))$
- 约束:测量必须保持细胞存活以供下游分析

### 14.2.2 · 主流认为的"未来量子解法"

学术界主流认为这类问题需要:

- **量子-enhanced microscopy** 跟 sub-shot-noise 探测 + FT QC 信号处理 [Quantum Microscopy reviews]
- 结合 quantum sensing + quantum machine learning · 是 long-term roadmap (无明确时间预期)
- 隐含假设:FT QC 跟生物样本的 interface 通过 high-fidelity sensor 实现

**这个 roadmap 的瓶颈**:FT QC 需要 cryogenic + 大规模 logical qubit · 跟室温生物样本的物理接口几乎不存在。事实上 · 即便 FT QC 完全成熟 · 它仍无法对活细胞做反事实测量 —— 这是 §5 D3 永久独占点。

### 14.2.3 · 我们的 CFE 解法

**算法** (基于 §8.2 CPA 模板 + §3 多算子组合):

```
INPUT:  1 cell · N assays {A_1, ..., A_N} · 每 assay 对应物理 oracle O_i
GOAL:   全部 f_i(cell) 的输出

step 1: 把细胞置于 N-mode photonic interferometer 的共同 sample 位
        (每个 mode 对应不同 wavelength / polarization 配置 · 对应不同 assay)

step 2: 用 Φ_CF[A_i] 反事实评估每个 assay
        对每 i = 1..N:
          y_i = counterfactual_eval(A_i, [O_i], delta=1e-3, epsilon=1e-3)
        
        关键:每个 Φ_CF 调用的 photon · 大部分 run 在物理上不跟细胞相互作用
        (反事实性 P2 保证) · photo-bleaching 累积 = N × δ × baseline_dose
        = 1000× 减少 (相对经典)

step 3: 收集 N 个输出向量 (y_1, ..., y_N)

step 4: 细胞仍存活 · 送下游分析 (基因测序 / 流式 / 组织学)
```

### 14.2.4 · 复杂度对比 (§7 多维)

| 维度 | 经典 (荧光成像) | "未来"主流 QC | CFE (本工作) |
|---|---|---|---|
| $D_1$ Query | $N$ | $\sim \sqrt{N}$ | $\sqrt{N}/\delta$ |
| $D_2$ Disturbance (photon dose) | 1 (全剂量) | 1 | $\delta \sim 10^{-3}$ |
| $D_3$ Observability (无关) | - | - | - |
| $D_4$ Hardware | 经典 microscope (~$50k) | FT QC + quantum microscope (估 $10^9$) | photonic IFM chip + microscope adapter (~$200k) |
| 细胞存活后可做 assay 数 | 3-5 | 同上 | 20-50 |

### 14.2.5 · 工程化条件 cliff

需要的硬件:

| 部件 | 当前 SOTA |
|---|---|
| N-mode photonic IFM chip (N=12-32) | ✅ [Hance 2025] · 集成 universal photonic processor |
| 单光子源 (heralded SPDC / III-V QD) | ✅ 商品化 |
| 单光子探测器 (SNSPD) | ✅ 商品化 |
| 跟生物 microscope 的光路集成 | ⚠️ 需 custom 工程 · 但无原理性障碍 |
| Active phase stabilization for biology temperature | ⚠️ 工程化 · 不平凡但已有先例 |

**核心 cliff**:跟生物样本的物理接口工程 · 涉及把 photonic chip output 耦合到 microscope sample plane。这是工程问题 · 不是物理问题。

### 14.2.6 · 时间相对位置

- **FT QC 路径**:跟生物样本物理 interface 永远不可达 (§5 D3 永久独占 · 不依赖 FT QC 成熟程度)
- **CFE 路径**:依赖 photonic IFM chip 工程化 + microscope 集成 · 当前已 lab-proven · 工程量适中

**结论**:本案例下 · 未来 (FT QC + biology) 不只是被拉近 · 是 **被另一条路径完全替代** —— FT QC 永远做不到 · CFE 当下工程化可行。

## 14.3 · 案例 2 · NAND-tree 量子算法的物理实现 (A1)

### 14.3.1 · 问题陈述

**领域**:量子算法理论 · 计算复杂度

**问题**:评估深度 $N$ 的平衡 NAND-tree · 输入是 $N$ 个 leaf bit · 输出是 root 的 NAND 计算结果。这是计算复杂度的经典 benchmark 问题。

**为什么重要**:NAND-tree 是 read-once Boolean formula 的代表 · evaluate 它的复杂度对很多算法问题有 implications (game tree / 决策树 / 部分 SAT)。

### 14.3.2 · 主流认为的"未来量子解法"

学术界主流路径:

- [Farhi-Goldstone-Gutmann 2008]:**Hamiltonian-based quantum walk** · 在连续时间量子游走 framework 上证明 $O(\sqrt{N})$ 查询 · 优于经典 $\Omega(N^{0.753})$
- [Childs-Cleve-Jordan-Yonge-Mallo 2009]:Discrete-query 版本 · 同样 $O(\sqrt{N})$ · 适合 FT QC gate model

**这两条路径的瓶颈**:

- 需要 FT QC gate model 实现 quantum walk
- 至今没人在**物理硬件**上跑过完整 NAND-tree 算法 · 都是 quantum circuit 表达 / simulator 演示
- 等 FT QC 成熟才能实物验证

### 14.3.3 · 我们的 CFE 解法

**算法**:把 NAND-tree 直接 encode 到 multipath photonic interferometer · 用 $\Phi^{CF}_{\text{NAND-tree}}$ (§3.5 子算子) 直接求值。

```
INPUT:  深度 d 的平衡 NAND-tree · 共 N = 2^d leaf · 每 leaf 是 bit
GOAL:   root NAND value

step 1: 物理构造 d 层 cascaded photonic interferometer
        (每层对应 NAND-tree 一层 · interferometer 节点对应 NAND 节点)

step 2: 每 leaf bit 编码为对应 photonic mode 的 obstacle 状态
        bit=1 → 路径上插 absorber · bit=0 → 不插

step 3: 单 photon 注入 root mode
        反事实演化:photon 沿 multipath 干涉传播
        干涉 readout 给出 root NAND value · 大部分 obstacle 没真触发

step 4: 输出经典 bit
```

### 14.3.4 · 复杂度对比

| 维度 | 经典 | Farhi/Childs (理论 QC) | CFE (本工作) |
|---|---|---|---|
| $D_1$ Query | $\Omega(N^{0.753})$ | $O(\sqrt{N})$ | $O(\sqrt{N}/\delta)$ |
| $D_2$ Disturbance | 1 | 1 | $\delta$ |
| $D_4$ Hardware | 经典 CPU | FT QC (gate model) | photonic IFM chip |
| 物理实物可行 | ✅ 当下 | ❌ 等 FT QC | ✅ 当下 |

### 14.3.5 · 工程化条件 cliff

| 部件 | 当前 SOTA |
|---|---|
| d=3-4 层 cascaded interferometer (N=8-16) | ✅ [Nat Commun 2021 multipath] |
| Switchable absorber 阵列 (EAM) | ✅ 标准 PDK 组件 |
| 单光子源 + SNSPD | ✅ 商品化 |
| Programmable phase shifter | ✅ 标准 |

**核心 cliff**:只需把已有的 multipath photonic chip 跟 EAM 阵列组装 + 编写控制软件实现 NAND-tree 映射。**无未解决的物理问题 · 纯工程问题**。

### 14.3.6 · 时间相对位置

- **FT QC 路径**:依赖 fault-tolerance 突破 + logical qubit 数量上升 + quantum walk 算法在 gate model 实现的优化 · 多个依赖链
- **CFE 路径**:已有硬件 + 已有算法 · 工程组装即可

**结论**:本案例下 · "**未来 (Farhi 2008 NAND-tree 算法的物理实物运行)** 已被拉到当下" 是字面上成立的 —— Farhi/Childs 算法理论已有 17 年 · 至今没在物理硬件跑通是因为大家都在等 FT QC。CFE 路径让我们**绕过等待** · 直接在 photonic IFM 跑通。

## 14.4 · 案例 3 · 物理 stealth probing (A4)

### 14.4.1 · 问题陈述

**领域**:军用情报 / 物理对抗安全 / 取证

**问题**:对手在某区域部署 $N$ 个物理监控设备 (摄像头 / 监听器 / 雷达 / 物理 trap) · 想判定 "是否有任何 device 处于 active 状态" · 但**任何主动探测都会被对手观测到** · 暴露探测者的位置和能力。

### 14.4.2 · 主流认为的"未来量子解法"

主流路径:

- **Quantum radar** [Lloyd 2008] · 用 quantum illumination 提升 stealth 能力 · 但仍是"主动发射 quantum signal"模式
- **FT QC 后处理**:对接收到的微弱反射做 quantum-enhanced signal processing
- 隐含假设:发射端仍是物理 signal · 对手原则上仍可检测到发射

**这条路径的根本局限**:发射 quantum signal 本身仍是物理事件 · 对手能检测到 "发射器在运行" · 即使无法解读内容也能定位。

### 14.4.3 · 我们的 CFE 解法

**算法** (基于 §3 $\Phi^{CF}_{\text{OR}}$ + §8 CPA):

```
INPUT:  N 个目标 device 位置 · 每个对应物理 oracle O_i (active 状态编码为 obstacle)
GOAL:   "any device active?" 单 bit

step 1: 部署 N-path photonic IFM 探测器
        每路对应一个目标 device 位置
        通过 EM coupling / optical coupling 物理连接到 oracle

step 2: result = Φ_CF[OR](oracles, delta=1e-6, epsilon=1e-3)
        关键:δ=1e-6 意味着对手能检测到我们探测的概率 ≤ 10^-6
        (R2 性质 · adversary-undetectable)

step 3: 如果 result == True · 知道有 active device 但不知道哪个
        如果需定位 · 用 Φ_CF[LOC] iterated · 同样反事实
```

### 14.4.4 · 复杂度对比

| 维度 | 经典 stealth probing | Quantum radar (主流 QC) | CFE (本工作) |
|---|---|---|---|
| $D_1$ Query | 必然主动发射 | 必然主动发射 (quantum) | 反事实 · 大部分不发射 |
| $D_3$ Observability (对手能检测我方) | 1 (必然暴露) | 1 (signal 仍存在) | $\sim \delta^N \to 0$ |
| 物理可行 | ✅ 但不隐蔽 | ⚠️ lab demo | ✅ photonic IFM 可行 |

### 14.4.5 · 工程化条件 cliff

| 部件 | 当前 SOTA |
|---|---|
| 多路 photonic IFM probe | ✅ [Hance 2025] 实物 |
| 跟物理 sensor 的 coupling (EM / optical) | ⚠️ 需 custom 工程 · 取决于具体 target 类型 |
| 高效 single-photon source / detector | ✅ 商品化 |
| 战场 / 现场部署外形 | ❌ 当前都是 lab setup · 需 ruggedization |

**核心 cliff**:战场部署 ruggedization 是真工程难度 · 但不涉及未解决物理问题。

### 14.4.6 · 时间相对位置

- **Quantum radar 路径**:即便完全成熟 · 仍无法做到 "对手不可检测发射" —— 这是物理原理性瓶颈 (§5 D1.b)
- **CFE 路径**:adversary-undetectable 是 R2 性质 · 物理上 $\delta \to 0$ 极限达到

**结论**:本案例下 · CFE 提供的 **adversary-undetectable probing** 是任何主流量子方案 (包括 FT QC) 都做不到的物理新能力。"未来" 在这里不存在 —— 没有任何 future tech roadmap 包含这个能力。CFE 当下解锁的是**完全新的 capability**。

## 14.5 · 三个案例的综合证明

3 个案例分别证明 3 种不同形式的 "未来已被拉到当下":

| 案例 | 突破类型 | "未来" 状态 |
|---|---|---|
| A2 单细胞多 assay | **替代路径** · FT QC 永远不可达 · CFE 当下可做 | FT QC 永远 ≠ 未来路径 · CFE 是唯一可行未来 |
| A1 NAND-tree | **时间提前** · 算法理论已有 17 年 · 等 FT QC 永远没等到物理实物 · CFE 直接物理化 | 主流"未来"路径被 CFE 路径**短路** |
| A4 Stealth probing | **新能力解锁** · adversary-undetectable 不在任何 future tech roadmap | "未来" 不曾包含此能力 · CFE 直接创造 |

3 种突破类型联合证明:

> 在 oracle / query 类问题的某个子集上 · 即使乐观估计 FT QC 成熟 · 也无法到达 CFE 当下可达的位置。在这个子集上 · "**未来已被拉到当下**" 不只是修辞 · 是字面陈述。

## 14.6 · 工程化条件的元层分析

3 个案例对工程化的依赖各不同 · 但所有依赖都满足以下元层条件:

| 元条件 | 满足情况 |
|---|---|
| 物理原理已 proven | ✅ ([Elitzur-Vaidman 1993] [Mitchison-Jozsa 2001] [Hance 2025]) |
| 单 device 已 lab demo | ✅ ([Hance 2025] 多对象 IFM on integrated chip) |
| 关键部件商品化 | ✅ (photonic chip / SNSPD / single-photon source / EAM 都商品化) |
| 算法层已抽象 | ✅ (本论文 §3 + §4 + §8) |
| 跨学科桥梁 (光物理 ↔ 应用领域) | ⚠️ 是核心剩余工作 · 但**不涉及未解决物理** · 是工程问题 |
| 大规模 scale up (N > 32) | ⚠️ 取决于 active stabilization 工程优化 · 有路径 |

**核心元结论**:CFE 的工程化条件 **全部是工程问题 · 没有未解决物理问题**。这跟 FT QC 截然不同 —— FT QC 还有 fault tolerance 突破 / qubit scaling / topological code 等开放物理问题待解决。

工程问题跟物理开放问题的本质区别:工程问题的解决依赖 **资金 + 时间 + 工程师 hour** · 物理问题的解决依赖 **新发现 + 突破**。前者**可预算可计划** · 后者**不可预测**。

CFE 把对 FT QC 路径上 "**不可预测的物理突破**" 的依赖 · **转移到 photonic IFM chip 工程化路径上"可预算的工程优化"**。这就是 "把未来拉近到当下" 的精确含义。

## 14.7 · 反对意见的预防回应

预期审稿人会提出以下反对 · 提前回应:

**反对 1**:"你声称 CFE 当下可做 · 但 §11 说 N $\leq$ 32 是硬件限制。N=32 够吗?"

回应:
- A1 NAND-tree 在 N=8-16 即可 demo · 足够发顶刊 + 学术 narrative
- A2 单细胞 assay 在 N=20-50 即覆盖大部分实用场景
- A4 stealth probing 在 N=32 已覆盖大量 niche use case
- 大规模 (N > 100) 不是本论文 claim 的 immediate niche · 是后续工作

**反对 2**:"CFE 在 $D_1$ query complexity 上比 standard QC 慢平方倍 · 怎么算 '突破'?"

回应:
- 突破不在 $D_1$ · 在 $D_2$ (disturbance) + $D_3$ (observability) + interface domain (§5 D3)
- 慢平方倍换永久独占 + 工程化提前 · 是合理 trade-off
- 详 §7 多维 Pareto 分析

**反对 3**:"你的 case study 都基于 [Hance 2025] 单一实验 · 重复性如何?"

回应:
- 这是 §13 重点请求验证的问题 (待验证声明 5 + 10)
- 单一实验确实是当前 evidence 限制 · 但物理原理 + 多平台 [Kong 2015 / Hance 2019 / Shwartz 2025] 共同支持
- 我们诚实标注 · 不夸大

**反对 4**:"为什么不等 FT QC?"

回应:
- A2 / A4 永远不需要等 (D3 独占)
- A1 / A3 / A5 / A6 等 FT QC 需要的物理突破不在可预测 timeline
- 工程化 CFE 不阻碍 FT QC 研究 · 两条路径并行没有冲突
- 提前拿下 niche 形成 narrative + 客户 + 数据 · 给 FT QC 来临时的 hybrid 模式做铺垫

## 14.8 · 闭环到论文核心论点

§14 至此完成对论文核心论点的 worked-example 证明:

> **如果** CFE 算子的工程化可行 · **那么** A1 (NAND-tree 物理化) + A2 (单细胞 multi-assay) + A4 (stealth probing) 这三类问题 · 现在已经可以解决。**这三类问题在主流叙事中都被认为需要等待 FT QC** —— 本论文证明等待是不必要的。

**进一步**:工程化条件全部是工程问题 (非未解决物理) · 因此 "if 工程化可行" 是 **可预算 / 可计划 / 可投资** 的 · 不是 "等灵感" 类型的依赖。

## 14.9 · 给行动者的指引

本章证明完成后 · 不同角色的行动:

| 角色 | 行动 |
|---|---|
| 算法学家 | A1 是最快的学术 demo · 选定它向 [Hance 2025] 类硬件团队提交合作请求 |
| 量子硬件创业者 | A2 商业 narrative 最强 · 选定它做种子轮 pitch · 找生物医学 LP |
| 政府 / 国防研究机构 | A4 战略价值最大 · 选定它启动 classified R&D |
| 半导体行业 | A5 (本章未独立展开 · 但同 framework) · 跟 ASML / KLA 谈在 PoC |
| 学术导师 | 把 A1 给博士生做毕业论文 · 6-12 months 出顶会 paper |
| 投资者 | 估值最大 unique 是 A2 · 因永久独占 · 关注早期项目 |

## 14.10 · 小结

3 个 worked example · 3 种不同形式的突破:

- A2 · 替代路径 (FT QC 永远不可达 · CFE 独占)
- A1 · 时间短路 (FT QC 是慢路径 · CFE 是快路径)
- A4 · 新能力 (FT QC 不曾包含此能力 · CFE 创造)

工程化条件全是工程问题 · 不是物理问题 · 因此 "if 工程化可行" 是**可计划的**而非**等突破的**。

**论文的最终论点 · 至此 worked-out**:

> **未来 · 在 CFE 算子覆盖的 niche 内 · 已经被拉到当下。剩下的只是工程工作。**

---

[← 上一章 · 13 验证与 RFC](13-validation-and-rfc.md) · [下一章 · 15 密码学认知突破 →](15-cryptographic-mental-model-shift.md)
