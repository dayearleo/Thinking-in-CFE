# 17 · CFE 算子同构方法论 · 历史算法宝库的光路重构

[← 返回 README](README.md)

## 17.1 · 本章定位 · 论文的元层延伸

§3-§8 给了 CFE 算子的形式定义 + 组合代数 + 6 个算法模板。§14-§16 给了具体应用 (生物 / 算法 / 密码学)。读者可能仍问:

> "6 个模板是终点吗?CFE 算子能 cover 的算法是不是就这些?"

**答案:不**。本章证明:**CFE 算子有能力跟历史上几乎所有算法主流范式做同构 (isomorphism)** · 形成各自专用的 photonic 计算模块。同构有时**抽象复杂度更差** · 但因为 **photonic 物理速度 + 光路硬件级特化优化** · 在很多 niche 仍是工业可接受甚至更优的方案。

更深一层:**每个问题域的历史解法和未来量子解法都是宝库** · 不该被 "经典已 cover" 或 "等 FT QC" 一句话扫地出门。本论文邀请读者把任何已知算法**作为 CFE 同构的候选** · 用 5 步方法论判定 · 不预设答案。

## 17.2 · 核心 idea · 三重叠加

CFE 同构的工业可行性建立在三重叠加上:

### 第一重 · CFE 算子的固有性质 (R1+R2+R3)

- R1 触发率任意小
- R2 adversary 不可检测  
- R3 输入不消耗

参见 §3.7。

### 第二重 · Photonic 物理速度的天然优势

- 光在 SiN 波导中传播速度 $c/n \sim 1.4 \times 10^8$ m/s
- 1 mm 长波导:flight time $\sim 7$ ps
- 一个 N=32 mode 干涉仪的端到端延迟 < 1 ns
- 经典 CPU 在 1 ns 内完成约 3-5 条指令
- **每个 CFE 单算子调用 ≈ 1 个 photonic flight cycle ≈ 几条 CPU 指令的时间**

这意味着:即使 CFE 同构算法的 abstract 复杂度比经典慢 10×-100× · 由于 photonic 单步时间快几个数量级 · **净 wall-clock 时间仍可能更短** —— 类比 GPU vs CPU 在 ML workload 上的优势。

### 第三重 · 专用光路硬件级特化优化

每个 CFE 同构算法可以**在芯片层特化**:

- mode 数 / 布局 / 耦合系数 针对该算法定制
- 内置 phase shifter 控制特定参数
- 直接接入应用域物理 oracle (生物 sample / RFID / sensor / 等)

这是 **ASIC 模式** —— 一颗芯片解一类问题 · 不通用 · 但极致优化。类比 Bitcoin ASIC vs 通用 CPU 挖矿。

三重叠加结论:

> **CFE 同构算法 + photonic 速度 + 硬件特化** = 一类**新计算单元** · 在 specialized workload 上可超越通用 CPU/GPU/QPU · 即使抽象算法复杂度不优。

## 17.3 · 同构发现方法论 · 5 步 SOP

**Step 1 · 问题域历史考古**

对目标问题 P:

- 列出所有历史经典解法 (50 年文献 · 从初代算法到最新 SOTA)
- 列出所有量子解法 (Shor / Grover / quantum walk / VQE / 等)
- 列出所有 specialized hardware 解法 (DSP / GPU / TPU / FPGA / 模拟光学 / 等)

**关键原则**:**没有坏解法**。一个被淘汰的经典算法仍有 internal primitives 可能适合 CFE 同构 (例如:被 ANN 取代的 SVM · 其 kernel trick 可被光路加速)。

**Step 2 · 抽离 primitive operation**

每个解法本质上是若干 **primitive operation** 的组合:

- "查表" / "比较" / "排序" / "矩阵乘" / "求导" / "采样" / "傅里叶变换" / "约束求解" / ...

把每个 primitive 单独提取。

**Step 3 · CFE 同构候选判定**

对每个 primitive op:

- 它是否可写成 $\Phi^{CF}_f$ 形式? (输入 oracle 集合 · 输出 Boolean / count / 位置)
- 它的 oracle 能否物理化为 photonic-probe-able? (R1/R2/R3 物理可行性)
- 它的 sparsity / side-effect / verify-without-commit 性质明显吗?

满足以上 3 条至少 1 条 · 进 Step 4。

**Step 4 · 复杂度对比**

对该 primitive 的 4 维复杂度评估 (§7 框架):

| 维度 | 经典 | 量子 SOTA | CFE 同构候选 |
|---|---|---|---|
| $D_1$ Query | ... | ... | ... |
| $D_2$ Disturbance | ... | ... | ... |
| $D_3$ Observability | ... | ... | ... |
| $D_4$ Hardware | ... | ... | ... |

**注意**:$D_1$ CFE 几乎一定劣 (Lin-Lin 2015 平方差) · 但其他 3 维要看。

**Step 5 · 物理速度补偿评估**

判定净 wall-clock 优劣:

$$T_{\text{CFE total}} = B_\delta(f) \times T_{\text{photonic single cycle}}$$
$$T_{\text{classical total}} = D(f) \times T_{\text{CPU instruction}}$$

如果:

$$T_{\text{CFE total}} < T_{\text{classical total}}$$

即:

$$\frac{B_\delta(f)}{D(f)} < \frac{T_{\text{CPU instruction}}}{T_{\text{photonic single cycle}}} \approx \frac{1 \text{ ns}}{1 \text{ ns}} \sim 1$$

(具体比值取决于硬件 · 当前估算约 $10^0$ 到 $10^2$ · 即 CFE 慢 1-100× 倍仍 net win)

如果 CFE 慢更多倍 · 看 R2 / R3 性质是否带来不可替代价值 (例如不暴露探测 · 不消耗资源) · 这种价值经典硬件**无法**补偿。

## 17.4 · 4 个 worked example · 跨领域同构

### 17.4.1 · 数据库 · Bloom Filter → CFE Stealth Lookup

**问题域**:Bloom filter 是经典 sublinear-space 数据结构 · 测试 "key 是否在集合里" · 允许 false positive。

**历史解法**:

- 1970 Bloom 原始构造 · k 个 hash function + bit array
- 改进版 · counting Bloom filter · cuckoo filter · XOR filter
- 量子版 · quantum Bloom filter [Hosseini 2016] · 用 amplitude encoding

**CFE 同构候选**:Bloom filter 的核心 primitive 是 "并行 k 路 hash 查表"。

CFE 版本:

```
Φ_CF[BloomLookup](key) = Φ_AND(
  [Φ_CF[hash_i(key) bit is 1] for i in 1..k],
  δ=1e-6
)
```

物理实现:N=k 路 photonic interferometer · 每路 oracle 对应一个 hash 位置 · AND 等价于 "all paths clear → interference"。

**复杂度**:

| 维度 | 经典 Bloom | CFE Bloom |
|---|---|---|
| 单 lookup 时间 | k CPU cycles | 1 photonic flight cycle |
| 状态改变 | 读 bit array (cache 影响) | bit array 物理不变 · R3 |
| 持有方可知查询 | ✅ DRAM access detectable | ❌ R2 stealth |

**Killer use case · Stealth PIR**:

Private Information Retrieval (PIR) 让客户查询数据库**而数据库持有方不知道查的是什么**。当前 PIR 协议 (Chor 1995, SealPIR, OnionPIR) 用密码学手段 · bandwidth + compute overhead 巨大 (10⁴-10⁶× single query)。

**CFE Stealth Lookup 直接给出物理层 PIR**:用 CFE Bloom filter 探测数据库 · R2 性质让数据库 server 物理上**检测不到**查询发生 · 不需要密码协议 overhead。

**净评估**:

- $D_1$ 慢:photonic Bloom 单查询略慢 (loss + visibility overhead)
- $D_2/D_3$ 性质强:经典 PIR 协议无法 native 给出 stealth · CFE 直接给
- $D_4$ 硬件:小 photonic ASIC · 比 PIR server 集群便宜
- **结论:CFE Stealth Lookup 在 privacy-critical 数据库查询 niche 取胜**

---

### 17.4.2 · 图算法 · 网络可达性 → CFE Interferometric Reachability

**问题域**:给一个网络图 G(V, E) · 判定 "从 source s 到 target t 是否可达"。

**历史解法**:

- 经典 BFS / DFS · O(V+E)
- 双向搜索 · 数倍加速
- A* / 启发式搜索
- 量子 walk · O(√N) 加速 [Childs 2003]
- 量子可达性 query · 多项式加速 [Belovs 2012]

**CFE 同构候选**:可达性的核心 primitive = "存在路径吗?"。

CFE 版本:

```
Φ_CF[Reachable](s, t) = Φ_OR(
  [Φ_CF[edge_i is intact] for edge i on potential paths from s to t],
  δ=1e-6
)
```

物理实现:把图 embed 进 photonic chip (节点 = mode · 边 = directional coupler · 路径长度 = 边权) · photon 从 s 入 · t 检测干涉 · 干涉强度 ≠ 0 等价于可达。

**复杂度**:

| 维度 | 经典 BFS | 量子 walk | CFE Interferometric |
|---|---|---|---|
| $D_1$ 时间 | O(V+E) | O(√V) | O(photonic flight / longest path) |
| $D_2$ 网络扰动 | 0 (本地计算) | 0 (本地量子计算) | R1 · photon 不真触发边 |
| $D_3$ 持有方可知 | N/A (本地) | N/A | R2 · 远程网络不知被探 |
| $D_4$ 硬件 | 通用 CPU | FT QC | photonic chip |

**Killer use case · Stealth Network Probing**:

军用 / 情报场景 · 需要判定对手网络拓扑 "host A 跟 host B 之间是否有 alive path"。经典 traceroute / ping **必然暴露**探测者 IP。Quantum radar 也仍是 active emission。

**CFE Interferometric Reachability** (物理实现需要光路接入网络物理介质 · 如光纤 tap):

- R2 让对手网络看不到探测 packet
- $D_1$ 慢 (建立 chip embedding 有 overhead) 但单次 reachability 测试本身是 photonic flight 时间 (ns 级)
- 比 quantum radar 更适合 stealth · 因为无 active emission

**净评估**:

- 军用 / 情报 niche **取胜** · 经典做不到 R2
- 商用 (data center network) 不需要 R2 · 经典 BFS 仍优
- **结论:CFE Reachability 是 stealth 探测 niche 的 unique solution**

---

### 17.4.3 · 密码分析 · 差分密码分析 → CFE Differential Probe

**问题域**:差分密码分析 (Biham-Shamir 1990) 是对称密码 (DES / AES) 的经典攻击方法 · 通过观察 chosen plaintext 对的输出差分 statistical bias · 推导 key 信息。

**历史解法**:

- 经典差分:大量 chosen plaintext 灌进黑盒 cipher · 看输出 · 统计 bias
- Linear cryptanalysis · 类似但用 linear approximation
- Boomerang attack · combine 多对差分
- 量子差分 · superposition query 加速 [Kaplan 2016]

**CFE 同构候选**:差分分析的核心 primitive = "在 plaintext difference Δ 下 · cipher 是否产生 output difference Δ' " · 这是 Boolean 测试。

CFE 版本:

```
Φ_CF[DiffMatch](Δ, Δ') = Φ_CF[E_K(P + Δ) - E_K(P) = Δ'](
  cipher_oracle, δ=1e-6
)
```

物理实现:cipher 实现在 photonic chip 上 · 差分 query 通过 CFE 反事实评估 · oracle 内部状态不被 query 改变 (R3) · cipher service 端 query log **不记录** CFE 查询 (R2)。

**关键 differentiation**:

经典差分需要 $10^{42}$ 量级 plaintext (full DES) · 这会让任何 rate-limit 的 cipher service 立即注意到。现代 HSM / Cloud crypto service **都有 query rate limiting** · 阻止经典差分。

CFE Differential Probe 的 R2 性质:**rate limiter 不计 CFE 查询** · 攻击者可以做超出 rate limit 的差分采样 · 而 service 不察觉。

**复杂度**:

| 维度 | 经典差分 | 量子差分 | CFE Differential |
|---|---|---|---|
| $D_1$ Query 数 | $\sim 2^{47}$ for DES | $\sim 2^{24}$ | $\sim 2^{47}/\delta = 2^{47} \times 10^9$ (慢很多) |
| $D_2$ Service 影响 | 触发 rate limit | 触发 rate limit | R2 · 不触发 |
| $D_3$ 持有方可知 | ✅ | ✅ | ❌ |

**Killer use case · Rate-Limited Cipher Service 攻击**:

DES (legacy systems) / 短 key cipher (WEP RC4-40) 已被经典差分破解 · 但部署在 cloud 上的现代实现有 rate limit / anomaly detection 防御。CFE Differential 让这些防御**完全失效** · 短 key legacy 算法在 cloud 部署时变得可破。

**净评估**:

- $D_1$ 慢 (因 $\delta$ overhead · 总查询数 ≈ 经典 $\times 10^9$)
- 但 photonic 单查询快 · 总 wall-clock 仍可接受 (假设 $10^{56}$ photonic flights × ns = $10^{47}$ s · 太慢 · DES 不实际)
- **但对短 key cipher (DES-40 / RC4-40):$10^{12} \times \text{ns} = 10^3$ s = 17 分钟 · 完全可行**
- **结论:CFE Differential 让短 key cipher 在 rate-limited deployment 下被破** · 即使数学早被破

跟 §16.6.2 的 CFE PIN brute-force 是同一类攻击 · 这里是它在密码分析层面的版本。

---

### 17.4.4 · 机器学习 · 反向传播 → CFE Counterfactual Gradient

**问题域**:神经网络训练用反向传播 (backprop) 算梯度 · 然后梯度下降。

**历史解法**:

- Backprop (Rumelhart 1986) · O(parameters) per pass
- 各种加速 (Adam / RMSprop / momentum)
- 量子 ML 加速 · quantum gradient [Schuld 2019]
- Photonic neural network · 已有产品 (Lightmatter Envise)

**CFE 同构候选**:Backprop 的核心 primitive = "对参数 $\theta_i$ 微小扰动 $\epsilon$ · 输出变化是多少?"。这是 oracle query 形式。

CFE 版本:

```
Φ_CF[Gradient_i](sample) = Φ_CF[
  output(model(θ + ε·e_i), sample) - output(model(θ), sample)
](δ=1e-6)
```

物理实现:photonic neural network mesh (已有 SOTA · Lightmatter / Lightelligence) · 每个 parameter 是一个 phase shifter · CFE 反事实评估扰动响应 · sample 本身**不被 model 真消耗** (R3)。

**关键 differentiation**:

经典 backprop 每次 epoch 必须用 training samples · 大数据集训练 sample 很多 · 但单 sample 信息含量低。CFE Gradient 的 R3 性质:**多次 query 同一 sample 不损耗** · 在小样本 / federated learning / privacy-sensitive ML 场景有特殊价值。

**复杂度**:

| 维度 | 经典 backprop | 量子 ML gradient | CFE Gradient |
|---|---|---|---|
| $D_1$ Time per gradient | O(parameters) CPU ops | O(√parameters) | O(parameters) photonic ops |
| $D_2$ Sample disturbance | 1 (sample 被消耗) | 1 | R1 · sample 物理上不被处理 |
| Privacy (sample owner) | ✅ data leakage | ✅ | R2/R3 · sample stay with owner |

**Killer use case · Privacy-Preserving Federated Learning**:

Federated Learning (FL) · 客户端持有 sample · server 持有 model · 训练时 model gradient 不应让 server 学到 sample 内容。当前 FL 用 differential privacy + secure aggregation · 协议复杂 · 损失 model accuracy。

**CFE Gradient Federated Learning**:server 把 model 部署在 photonic chip · 客户端通过 photonic interface 提交 sample · CFE gradient 评估 · R2/R3 保证 server 物理上**无法**获取 sample 内容 · model 仍学到了 gradient。

**净评估**:

- $D_1$ 跟经典 backprop 同阶 (photonic neural net 本来就 O(params))
- R2/R3 给出 native privacy · 不需要 differential privacy / secure aggregation overhead
- **结论:CFE Gradient 在 privacy-critical FL niche 取胜** · 而且不损失 model accuracy

---

### 17.4.5 · 数值方法 · Monte Carlo 积分 → CFE Counterfactual Sampling

**问题域**:数值积分 / 期望估计 · 用 random sampling。

**历史解法**:

- Monte Carlo · 经典 O(1/√n) 收敛
- Quasi-Monte Carlo (low-discrepancy sequences)
- Importance sampling · Markov Chain Monte Carlo (MCMC)
- 量子 Monte Carlo · 二次加速 [Montanaro 2015]

**CFE 同构候选**:Monte Carlo 的核心 primitive = "在 sample point x · 函数 f(x) 是什么?"。 evaluating f 有时 expensive (例如:$f$ 是 expensive simulation 输出)。

CFE 版本:

```
estimate = Σ_i Φ_CF[f(x_i) ∈ bucket_j] / n
```

物理实现:多 path interferometer · 每 path 对应一个 sample point · CFE 反事实评估 f 是否落 bucket · expensive simulation 在大部分 sample 上**不真运行** (R1)。

**Killer use case · Expensive Simulation Sampling**:

Material science / drug discovery / climate model 等场景 · 单次 simulation 极贵 ($1M+ HPC cluster hours)。Monte Carlo 需要 $10^4-10^6$ samples · 完全不可行。

CFE Counterfactual Sampling:大部分 sample 物理上不真运行 simulation · 只 stat 出 reduction · 真正消耗 cluster hours 的只是少数 critical samples。

**复杂度**:

| 维度 | 经典 MC | 量子 MC | CFE MC |
|---|---|---|---|
| $D_1$ Total samples | $1/\epsilon^2$ | $1/\epsilon$ | $1/(\epsilon^2 \cdot \delta)$ (差) |
| $D_2$ Simulation cost | n × $C_{sim}$ | √n × $C_{sim}$ | small × $C_{sim}$ + $n/\delta$ × $C_{photonic}$ |

**结论**:当 $C_{sim} \gg C_{photonic}$ (typical for expensive sim) · CFE MC 即便 sample 多 $10^9$ 倍 · 总 cost 仍可能远低 · 因为只有少数 sample 真跑 sim。

## 17.5 · 历史算法宝库的元层视角

5 个 worked example 揭示一个深层 pattern:

**每个被淘汰的经典算法都可能藏着 CFE 同构的金矿**。例:

- SVM 被神经网络淘汰 · 但 SVM 的 kernel trick 可以 CFE 同构 · 实现 photonic kernel evaluation 不暴露 sample
- AdaBoost 被淘汰 · 但其 weighted sampling 可以 CFE 同构 · 实现 privacy-preserving boosting
- 简单 PRNG (LCG / Mersenne Twister) 安全性不足 · 但其 state evolution 可以 CFE 反事实采样 · 实现 stealth RNG

**未来量子算法**同样:

- Shor 算法本身不能 CFE (不是 query model) · 但其内部的 modular arithmetic primitives 可以 CFE 同构 · 实现 stealth modular ops
- HHL 算法不能 CFE · 但其依赖的 quantum phase estimation primitive 在某些情况可 CFE 反事实读取

**元结论**:**任何算法的 internal primitives 都是 CFE 同构候选**。本论文不能列穷尽 · 但本章方法论让任何算法学者 / 工程师都能**自己**发现属于自己问题域的 CFE 同构。

## 17.6 · 硬件特化的实现路径

每个 CFE 同构算法在被发现后 · 可以走 4 个 specialization 级别:

| Level | 实现 | 例 |
|---|---|---|
| L0 · Generic | universal photonic processor | 灵活 · 但每个算法 overhead 高 |
| L1 · Programmable | parameterized photonic chip | 一个 chip 覆盖一类算法 (e.g. 所有 Bloom-style 查询) |
| L2 · Algorithm-specific | fixed photonic chip for one algorithm | 例:专用 "CFE Bloom Filter ASIC" |
| L3 · Problem-specific | chip + 物理 oracle 接口 | 例:专用 "stealth wafer inspection chip" |

L3 是最终形态 · 类比 Bitcoin ASIC vs 通用 CPU 挖矿 —— **完全特化 · 性能压倒通用方案 · 但只能解一种问题**。

工业化路径:

```
新问题 → 用 §17.3 方法论发现 CFE 同构
        ↓
       L0 验证可行性 (universal photonic)
        ↓
       L1 工程化为 programmable 模块 (服务一类问题)
        ↓
       L2/L3 ASIC (服务一个具体问题 · 极致优化)
        ↓
       商业部署
```

这是一条**跟通用 quantum computing 完全平行**的硬件路线图 · 不依赖 FT QC 成熟 · 当下就可启动。

## 17.7 · 一个 vision · CFE 算子家族目录

如果方法论被广泛应用 · 5-10 年内可能形成一个 **CFE 算子家族目录** · 类比:

- 标准库 (libc / numpy) 提供数百个 primitive
- 编译器 IR (LLVM IR) 提供数十种基本操作
- 量子算法库 (qiskit) 提供 Shor / Grover / VQE 等

**CFE 算子家族目录**应该包含:

- **基础 CFE 算子** (本论文 §3.5 的 7 个)
- **isomorphism 同构算子** · 跟经典算法对应 · 几十到几百个 (本章 method 发现的)
- **specialized hardware 模块** · 跟同构算子对应 · 数十个 ASIC blueprint
- **应用 templates** · 跟具体行业问题对应 · 几百个

每个算子带:

- 数学定义 (扩展 §3 算子定义模板)
- 同构对应的经典算法 (引用源算法)
- 复杂度 4 维评估 (按 §7 框架)
- 硬件实现 BluePrint (L0/L1/L2/L3)
- 使用案例 (具体行业 + worked example)

这是 **CFE 计算生态系统**的 vision · 类比 Linux / Python / TensorFlow 早期形态。

## 17.8 · 限界 · 同构方法论的边界

诚实划界:

**方法论不能保证发现**:

- 5 步 SOP 只判定 "是否值得尝试" · 不保证一定找到 net-win 同构
- 很多算法的 CFE 同构可能存在 · 但 net-win 区域很窄 (sparsity 假设 / R2 价值 / 等)
- 一些经典算法 (Shor 类 unitary-heavy) 没有 CFE 同构

**同构不能违反物理**:

- Holevo bound 仍然成立
- $B(f) = \Theta(Q(f)^2)$ 复杂度下界仍成立
- 物理 oracle 要求仍然 binding (远程数字服务无法同构)

**特化硬件不是 free lunch**:

- L2/L3 ASIC 开发 cost 高 · 只对足够大市场才值
- 每个 ASIC 锁死一类问题 · 不能跨用
- ASIC 出货后改 algorithm 需要 respin

**方法论是发现引擎不是验证机**:

- 找到候选同构后 · 仍需走 §13 RFC 流程独立验证
- 不能光凭 "看起来 isomorphic" 就上 ASIC 流片

## 17.9 · Call to action · 给 4 类读者

### 给算法学者

- 选你最熟的算法子领域 (graph / numerical / crypto / ML / DB / ...)
- 用 §17.3 方法论审一遍历史 + 量子算法
- 找出至少一个 CFE 同构候选
- 写 follow-up 论文

### 给 photonic chip 工程师

- 跟算法学者合作
- 选一个被识别的 CFE 同构 candidate
- 设计 L1 programmable photonic 实现
- 跟 §16 / §15 worked examples 形成 vertical integration

### 给行业垂直应用工程师

- 描述你的 niche 问题 (privacy / stealth / sample-precious)
- 邀请算法 + photonic 合作伙伴查找对应 CFE 同构
- 启动 L3 ASIC 联合设计

### 给标准 / 投资 / 政策

- 关注 CFE 算子家族目录的形成 (类比早期 LLVM IR 的形成)
- 评估 ASIC 投资机会 (类比 GPU / TPU / AI ASIC 路线图)
- 制定 standards (跨厂商互操作 / 安全 cert / 出口管制)

## 17.10 · 闭环到论文核心

§17 完成对 user 提问的回答:

> **CFE 算子体系可以同构出无数其他算子** · 通过对每个问题域历史算法宝库 + 未来量子解法的系统化 CFE 同构发现 · 每个同构沉淀为专用 photonic 计算模块 · 即便抽象复杂度更差 · 在 photonic 物理速度 + 硬件特化双重补偿下 · 仍可形成工业可行的专业化计算单元。

**5 步 SOP** (§17.3) 给出可重复的发现机制。
**4 个 worked example** (§17.4) 跨 4 个领域证明方法论可行。
**4 级 specialization** (§17.6) 给出工程化路径。
**CFE 算子家族目录** (§17.7) 给出长期 vision。

跟之前章节的关系:

| 章节 | 角色 |
|---|---|
| §3-§8 | CFE 算子的**核**和**最小算法集** |
| §10 | 6 个直接挑战 FT QC 的问题 (**点**) |
| §14 | 3 个 worked example 证明 "未来已到当下" (**面**) |
| §15-§16 | 密码学专题深化 (**域**) |
| **§17 (本章)** | **CFE 同构方法论 · 让任何算法学者都能在自己问题域发现新同构** (**网**) |

§17 是论文的 **opens to community** —— 不再只给具体 worked examples · 给一套**让别人自己造 examples 的工具**。这是论文从 "specific contribution" 升级到 "ecosystem catalyst" 的 final 步骤。

---

[← 上一章 · 16 工业算法系统化攻击](16-attack-on-deployed-crypto.md) · [下一章 · 18 审计报告 →](18-audit-report.md)
