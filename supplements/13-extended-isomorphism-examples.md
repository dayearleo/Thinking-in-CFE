# 13 · 扩展同构 examples · 5 个新领域

[← supplements README](README.md)

## 文件性质

**论文 §17.4 的扩展** · 把 CFE 同构方法论应用到主论文未 cover 的 5 个新领域 · 每个给一个 worked example 示范。

新增 5 个领域:

1. **形式验证 / Static analysis** · 编译器与程序语言
2. **NLP / 大语言模型 inference** · 现代 AI workload
3. **计算几何 / 光线追迹** · 图形学和 rendering
4. **稀疏线性系统** · 数值方法第二例
5. **生物信息学 · 序列比对** · 计算生物学

每个 example 都满足:

- ✅ 来自一个**完全独立**的算法子领域 (跟 §17.4 4 个不重叠)
- ✅ CFE 同构有**非显然**优势 (不止 R2/R3 性质 · 还有 sparsity 假设)
- ✅ 明确指出 killer use case 跟 hardware specialization 路径

## 13.1 · 形式验证 · 抽象解释 → CFE Counterfactual Abstract Interpretation

### 问题域

**抽象解释** (Cousot 1977) 是程序静态分析的根基框架 · 用近似 fixpoint 推算程序属性 (变量范围 / 别名 / nullability / ...) · 应用在编译器优化 / bug 检测 / 形式验证。

### 历史解法

- 经典抽象解释:迭代到 fixpoint · O(states × transitions)
- 符号执行 (DART, KLEE):每分支真跑 · path explosion
- 抽象求解 (Z3 SMT):约束求解 NP-hard
- 量子 SAT / SMT 加速:部分理论结果 · 无实物

### CFE 同构候选

抽象解释的核心 primitive = **"在某抽象状态 $\sigma$ 下 · 程序 statement $s$ 的 effect 是否落 abstract domain $D$ 内"**。这是 Boolean predicate。

CFE 版本:

```
Φ_CF[StateInDomain](σ, s, D) = Φ_AND(
  [Φ_CF[transfer(σ, s) component_i ∈ D_i] for each abstract component],
  δ=1e-6
)
```

物理实现:每个 abstract component 一路 photonic mode · transfer function 物理 encode 为 phase shift · interference 给出 "所有 component 都在 domain 内" 的 conjunction。

### 复杂度

| 维度 | 经典抽象解释 | CFE 版本 |
|---|---|---|
| Fixpoint 迭代次数 | 取决于格高度 (typically polynomial in program size) | 同 · CFE 不加速 fixpoint |
| 每次 transfer evaluation | O(abstract domain size) CPU ops | 1 photonic flight |
| **关键: SMT 子查询** | NP-hard 真求解 | **R3: 不消耗 SMT solver budget** |

### Killer Use Case

**编译器优化的 cloud SMT solver 加速**:

现代编译器 (Z3 backend, LLVM Polly) 大量 SMT solver 调用 · cloud SMT services (CVC5 on AWS) 按 query 收费 + rate limit。

CFE 抽象解释让编译器在**本地 photonic chip** 反事实跑大部分 SMT query · 只对 critical query 真调 cloud · 节省 99%+ cost。

R3 性质让本地 chip 重复 query 同样问题不损耗任何资源。

### 硬件 Specialization 路径

- L0: universal photonic processor + Z3 software 适配层
- L1: programmable photonic SMT accelerator (处理 linear / bitvector / array theories)
- L2: ASIC 专门 for LLVM Polly + Polyhedral abstract domain
- L3: 联同 Intel / AMD / ARM 集成进 CPU 旁边的 specialized co-processor

## 13.2 · NLP · Transformer Attention → CFE Counterfactual Attention

### 问题域

Transformer attention (Vaswani 2017) 是现代 LLM 核心 · 计算 attention weights = softmax(QK^T / √d) · 然后 weighted sum of V。瓶颈是 O(N²) memory + compute (N = sequence length)。

### 历史解法

- 原始 full attention · O(N² d)
- Sparse attention (Reformer, Longformer)
- Linear attention (Performer, Linformer)
- Flash attention (Dao 2022) · IO-aware
- 量子 attention · 理论提案多 · 实物 niche

### CFE 同构候选

Attention 的核心 primitive = **"token i 对 token j 的 relevance 是否 > threshold"** · 大部分 (i, j) pairs 答案是 NO (typical sparsity 90%+)。

CFE 版本:

```
Φ_CF[RelevantPair](i, j) = Φ_CF[
  attention_score(query_i, key_j) > threshold
](δ=1e-6)
```

物理实现:N×N photonic mesh · 每个 (i,j) crossing 是一个 oracle · CFE 并行筛 relevant pairs · 只对 surviving 真算 weighted sum。

### 复杂度

| 维度 | Full attention | Sparse attention | Linear attention | CFE Counterfactual |
|---|---|---|---|---|
| Time | O(N²d) | O(N√N d) | O(Nd²) | O(K d / δ) where K = relevant pairs |
| Memory | O(N²) | O(N√N) | O(Nd) | O(K) |
| Accuracy | full | approx | approx | **near-full** (反事实预筛 · 真算保持 full attention 精度 on relevant pairs) |

### Killer Use Case

**百万 token context LLM 的 inference**:

GPT-4 Turbo 128k context 已经 cost 极高 · 1M context (Gemini 1.5) 更不可承受。Linear / sparse 方法损失 accuracy。

CFE Counterfactual Attention 用反事实预筛 · 只对 sparsity K << N² 的 relevant pairs 真算 · 既不损 accuracy 又 sublinear cost · 让 100M+ token context 可行。

### 硬件 Specialization 路径

- L0: photonic mesh + GPU 后处理混合
- L1: programmable photonic attention accelerator
- L2: Transformer-specialized photonic ASIC (类比 TPU 之于 Transformer)
- L3: 集成进 GPU/TPU 板卡 · attention layer offload 到 photonic co-processor

## 13.3 · 计算几何 · 光线追迹 → CFE Counterfactual Ray Tracing

### 问题域

光线追迹 (Whitted 1980) 是 photorealistic rendering 的标准方法 · 从相机发射 ray · 找跟场景几何的 closest intersection · 着色递归求子 ray (反射 / 折射 / 阴影)。瓶颈是每像素需追多 ray · 每 ray 跟所有 (或加速结构 BVH 后 log) 个体素求交。

### 历史解法

- 朴素:每 ray 跟 N 个 primitives 求交 · O(N) per ray
- BVH (Bounding Volume Hierarchy) 加速 · O(log N)
- 实时 hardware:RTX cores (Nvidia 2018) · hardware BVH traversal
- 量子光线追迹:有理论提案 [Lanting 2014]

### CFE 同构候选

光线追迹的核心 primitive = **"ray r 是否跟 primitive p 相交"** · 大部分 ray-primitive pair 答案 NO (sparsity 极高 · BVH 已利用)。

CFE 版本:

```
Φ_CF[RayHitPrimitive](r, p) = Φ_CF[
  intersect(r, p) != null
](δ=1e-6)
```

物理实现:把场景 primitives encode 为 obstacles in photonic interferometer · ray 编为 input direction · 干涉 readout 给出 "有 hit 吗 + 哪个 hit" (CFE COUNT + LOC)。

### 复杂度

| 维度 | 经典 BVH | RTX | CFE Ray Tracing |
|---|---|---|---|
| Per ray time | O(log N) | hardware-accelerated | 1 photonic flight |
| Memory | O(N) BVH | O(N) | O(N) photonic configuration |
| Parallel rays | 多 thread | 多 RT core | N 路并行天然 |

**关键 differentiation**:**photonic 光线追迹用实际光物理实现光路追迹** —— 你**真**在用光来追光。

### Killer Use Case

**实时 8K HDR ray-traced rendering**:

当前 RTX 4090 在 4K 60fps ray tracing 已是 SOTA · 8K 跟更高 sample count 仍困难。CFE Ray Tracing 用 photonic 物理速度 + 并行 · 可能让 16K HDR 60fps 可行。

更深 niche:**physical-accurate volumetric rendering** (光在大气 / 烟雾 / 透明物质中的散射) · CFE 用真物理 photon 路径模拟 · 比经典 ray tracing 更准。

### 硬件 Specialization 路径

- L0: 实验室 prototype · 跟 PsiQuantum 类公司合作
- L1: 集成 photonic ray tracing core
- L2: 专用 GPU 替代品 · 主打 photorealistic rendering
- L3: 跟 Nvidia / AMD 合作 · CFE Ray Tracing 作为 GPU 旁边的 specialized 模块

## 13.4 · 稀疏线性代数 · Sparse SpMV → CFE Counterfactual SpMV

### 问题域

Sparse Matrix-Vector multiplication (SpMV) y = A·x where A is sparse · 是 PDE 数值求解 / iterative solver (Conjugate Gradient) / 图算法 (PageRank) / SpMV-based ML 的核心。

### 历史解法

- 经典 CSR/CSC storage + indexed SpMV · O(nnz) per multiplication
- 块稀疏 / hybrid storage · cache-friendly
- GPU SpMV · 性能瓶颈 by memory bandwidth
- HHL 量子算法 · 解 Ax = b 端到端 · sparse 假设下 polylog · 需 FT QC

### CFE 同构候选

SpMV 的核心 primitive = **"row i 的非零元素跟 x 的对应分量乘积之和"** · 大部分 row 只有 O(k) 非零元素 (k << n)。

CFE 版本:

```
Φ_CF[SpMVRow](i, A, x) = Φ_CF[
  Σ_j A[i,j] * x[j] for j ∈ nonzero_cols(i)
](δ=1e-6)
```

物理实现:photonic mesh 跟 A 的稀疏 pattern 物理对齐 · CFE 反事实跳过 zero 元素 · 物理上不耗 cycles。

### 复杂度

| 维度 | CPU SpMV | GPU SpMV | HHL (quantum) | CFE SpMV |
|---|---|---|---|---|
| Time per SpMV | O(nnz) | O(nnz / parallelism) | polylog n (sparse) | O(nnz / δ) (慢但 photonic) |
| Memory bandwidth | bottleneck | bottleneck | N/A | not bottleneck (photonic in-mesh) |
| Iteration count (CG) | O(√κ) | same | quantum precision-limited | same |

### Killer Use Case

**Real-time PDE solver in physics simulation**:

天气预报 / 油气勘探 / 半导体仿真 用 SpMV-heavy iterative solver · GPU 是 SOTA 但 memory bandwidth bound。

CFE SpMV 用 photonic in-mesh compute 突破 memory wall · 让 real-time 3D fluid simulation / EM simulation 可行 (当前是 batch 跑数小时)。

### 硬件 Specialization 路径

- L0: HPC cluster + photonic accelerator card
- L1: programmable photonic SpMV chip
- L2: PDE-domain-specific photonic ASIC
- L3: 跟 NVIDIA HGX 类整合 · CFE SpMV 为 HPC co-processor

## 13.5 · 生物信息 · 序列比对 → CFE Counterfactual Smith-Waterman

### 问题域

Smith-Waterman 算法 (1981) 是 local sequence alignment 的最优解 · 用 dynamic programming 找两 DNA / 蛋白质序列的最佳 local 匹配。瓶颈是 O(n × m) (n, m 是序列长度) · 全基因组 alignment 不实用。

### 历史解法

- 经典 Smith-Waterman · O(nm)
- Heuristic: BLAST (Altschul 1990) · 用 k-mer hash · sublinear 但牺牲 optimal
- BLAT / minimap2 · 现代快速 aligner
- FPGA-accelerated SW · 已部署
- 量子 sequence alignment · 理论提案 [Hollenberg 2000]

### CFE 同构候选

Smith-Waterman 的 DP 矩阵填充 · 每 cell 是 **"local alignment score 是否 > threshold"** · 大部分 cell 答案 NO (典型 sparsity 99%+ for divergent sequences)。

CFE 版本:

```
Φ_CF[CellAboveThreshold](i, j, scoring_matrix) = Φ_CF[
  max(H[i-1, j-1] + s(a_i, b_j),
      H[i-1, j] + gap,
      H[i, j-1] + gap,
      0) > threshold
](δ=1e-6)
```

物理实现:DP 矩阵物理 encode 为 photonic mesh (每 cell 一 mode) · CFE 并行筛 above-threshold cells · 只对 surviving cells 真填精确 score。

### 复杂度

| 维度 | Smith-Waterman | BLAST | CFE SW |
|---|---|---|---|
| Time | O(nm) | O(n log m) heuristic | O(K / δ) where K = high-score cells |
| Optimality | 最优 | 启发 · 可能漏 | 最优 (对 above-threshold cells) |
| Memory | O(nm) | O(n + m) | O(K) |
| GPU 友好? | 是 | 是 | photonic mesh |

**关键 differentiation**:CFE SW 给 BLAST 的速度 + Smith-Waterman 的最优性 · 当前两者必须取舍。

### Killer Use Case

**全基因组对比的 cancer genomics**:

肿瘤基因测序需要对比 patient 基因组跟 reference · 全基因组级别 (3 billion bp) · 当前 BLAST/minimap2 不够 sensitive · 真 SW 太慢。

CFE SW 让全基因组级 sensitive alignment 在 minutes 级完成 (vs 当前 hours-days) · 对 personalized medicine 有直接价值。

### 硬件 Specialization 路径

- L0: 集成进 sequencing 仪器 (Illumina / Oxford Nanopore) 后端
- L1: programmable photonic aligner ASIC
- L2: cancer-genomics-specific photonic chip
- L3: 部署进 hospital genomics workflow

## 13.6 · 5 个新领域的 cross-cutting 观察

回看 §17.4 (4 个) + 本 supplement (5 个) · 9 个 worked example:

| 领域 | Worked example | 关键性质 utilized |
|---|---|---|
| §17.4.1 Database | Bloom → PIR | R2 + R3 |
| §17.4.2 Network | Reachability → Stealth probe | R2 |
| §17.4.3 Crypto | Differential → Rate-limit bypass | R2 |
| §17.4.4 ML | Backprop → Federated privacy | R2 + R3 |
| §17.4.5 Numerical | Monte Carlo → Expensive sim | R1 (sparsity-aware) |
| §13.1 Compilers | Abstract interp → SMT cost saving | R3 |
| §13.2 NLP | Attention → 100M token context | sparsity-aware |
| §13.3 Graphics | Ray tracing → 16K rendering | photonic speed |
| §13.4 Numerical | SpMV → real-time PDE | memory wall bypass |
| §13.5 Bioinfo | Smith-Waterman → genomics | sparsity-aware |

**模式**:

- R2 (stealth) 主导 5 个 (database / network / crypto / federated / abstract interp)
- R3 (non-consume) 主导 3 个 (Bloom / federated / abstract interp · 有重叠)
- Sparsity-aware 主导 4 个 (MC / attention / SW / SpMV)
- Photonic speed 主导 2 个 (ray tracing / SpMV)

**meta-insight**:**几乎任何有 "稀疏性 + 物理 oracle" 假设的算法都是 CFE 同构候选**。这意味着 CFE 算子的应用空间**远大于**我们最初想到的几个 niche。

## 13.7 · 给社区的开放邀请

本 supplement 列了 5 个新例 · 但 9 个总不是终点。每个学科有 hundreds of algorithms · 每个都值得过 §17.3 的 5 步 SOP。

我们特别欢迎来自以下领域的 CFE 同构提交 (走 supplement 11 模板):

- 量子化学 (CFE-Hartree-Fock?)
- 凸优化 (CFE-interior-point?)
- 数据库 join (CFE-hash-join?)
- 编译器调度 (CFE-instruction-scheduling?)
- 区块链共识 (CFE-Byzantine-fault-tolerance?)
- 推荐系统 (CFE-collaborative-filtering?)
- 计算物理 (CFE-Monte-Carlo-renormalization?)
- 化学指纹 (CFE-Tanimoto-similarity?)
- 形式语言 (CFE-DFA-minimization?)
- 多目标优化 (CFE-Pareto-frontier?)

每个 entry 一个 PhD 论文级别工作 · 或一篇 conference paper · 或一个 startup 角度。

## License

CC BY 4.0
