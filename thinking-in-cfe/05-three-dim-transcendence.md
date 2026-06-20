# 05 · 跟 FT QC 的 3 维比较 · 超越点定位

[← 返回 README](README.md)

## 5.1 · 为什么需要 3 维拆解

"我们超越未来 fault-tolerant 量子计算吗?" 是一个会导致混乱的问题 · 答案要么是 "是" (听起来夸张) · 要么是 "否" (听起来自贬)。

正确的提问方式是把 "超越" 拆成 **3 个独立维度** · 分别评估:

| 维度 | 评什么 |
|---|---|
| **D1 · capability** | 算子能算什么 · 给什么保证 |
| **D2 · cost** | 需要多少硬件 / 量子资源实现同一 capability |
| **D3 · interface domain** | 什么样的 oracle 能被算子作用 |

每个维度都给独立判断 · 再综合。

## 5.2 · D1 · capability 对比

### 能算什么 Boolean 函数

| 算子族 | 可算的函数 $f$ |
|---|---|
| 经典 OR/AND/XOR 等 | 任意 Boolean |
| Grover oracle queries | 任意 oracle 包装的 Boolean |
| Standard quantum query $Q(f)$ | 任意 Boolean |
| **$\Phi^{CF}_f$** | 任意 Boolean |
| FT QC (gate model) | 任意 Boolean + 任意 unitary |

**结论 D1 (主)**:在 Boolean 函数能力层面 · $\Phi^{CF}_f$ 跟经典 / 标准量子等价 · 是 FT QC 的子集。**我们不在 D1 主维度上超越 FT QC**。

### D1 隐藏子维度 · "查询的可观察性"

一个被传统讨论忽略的子维度:**查询行为本身是否对持有 oracle 的对手可见**?

| 算子族 | 持 oracle 对手能否检测查询发生? |
|---|---|
| 经典 | ✅ 必然可见 (查询就是经典通信) |
| Standard quantum query | ✅ 可见 · oracle 跟主系统纠缠 · 纠缠可测 |
| **$\Phi^{CF}_f$** $(\delta \to 0)$ | ❌ **不可见** · 没有纠缠产生 |
| FT QC implementing same | ✅ 仍可见 · unitary oracle calls 必然纠缠 |

**关键发现 D1.b**:在这个 D1 子维度上 · **$\Phi^{CF}_f$ 超越 FT QC**。FT QC 即使无限大也无法做"对手不可检测的查询" · 因为 unitary 调用本质产生纠缠。

## 5.3 · D2 · cost 对比

### 实现单个 $\Phi^{CF}_f$ 调用的硬件代价

| 实现方式 | 量子比特/资源 | 错误率要求 | 时钟 | 平台规模 |
|---|---|---|---|---|
| FT QC 实现 $\Phi^{CF}_f$ | $\sim 10^3 N$ 物理 qubit (含 surface code overhead) | 物理 $10^{-3}$ → 逻辑 $10^{-15}$ (需 $\sim 10^5$ 表面码循环) | 逻辑门 $\sim$ μs | 全球各 $\sim 10^{10}$ 投资 |
| **专用 photonic IFM** (本工作) | N 路 photonic mode | 5 dB loss + visibility 95% 足够 | 飞行时间 $\sim$ ns | 单芯片 $50k-$150k |

**比例**:约 6 个数量级的成本差。

### 历史类比 · "专用 unlock 通用计算才能做的事"

每一代新计算原语都经历 "**专用先到 · 通用后追 · 专用永远占某 niche**" 的模式:

| 时代 | 通用方案 | 专用方案 | 差异 |
|---|---|---|---|
| 1960s-70s · FFT 兴起 | 数字 CPU 跑 Cooley-Tukey | 光学 4f 透镜系统 | 光学瞬时 · 但只能做 FFT |
| 1990s · DSP | 通用 CPU 浮点 | 专用 DSP 芯片 | DSP 拿下 modem / 音频 |
| 2000s · GPU | 多核 CPU | GPU | GPU 拿下 3D / 后来 AI |
| **当前 · counterfactual** | FT QC (未来) | **专用 photonic IFM (本工作)** | 提前 unlock · 抢占 niche |

**结论 D2**:CFE 在 D2 上**显著领先** FT QC 约 6 个数量级 · 这一差距在 FT QC 量产前不会消失 · 即使 FT QC 普及后仍然在特定 niche 维持。

## 5.4 · D3 · interface domain 对比 (本论文核心超越点)

### 谁能当 oracle?

| 算子族 | oracle 必须是什么 |
|---|---|
| FT QC | 自己构造的 quantum circuit (内部抽象) |
| Standard quantum query (theory) | 黑盒 quantum oracle (内部抽象) |
| **$\Phi^{CF}_f$** | **任何能跟 photon 物理耦合的真实物体** |

### D3 上 $\Phi^{CF}_f$ 独占覆盖的 oracle 类型

下面这些 oracle · FT QC **永远到不了**(因为它需要把 oracle 放进自己的 quantum register):

- 一根真实爆炸物的引信状态
- 一颗真实稀土晶体里某核素的存在
- 一束真实对手雷达光是否在工作
- 一个真实生物细胞当前是否活着
- 一片真实晶圆某 die 是否有缺陷
- 一束真实远程激光信号的存在性
- 任何真实物理对象的某个 binary 属性

FT QC 要查询这些 · 必须先**测量它们** → 但测量本身 destructive · 反事实性丢光。

而 $\Phi^{CF}_f$ 天然能接:photon path 直接物理穿过 / 反射 / 吸收 物理样本 · 不需要数字化先。

### D3 是 categorical 差异 · 不是程度差异

D1 D2 都是程度差异 (FT QC 可以 "更好" / 我们可以 "更便宜")。**D3 是范畴差异** —— FT QC 跟物理世界的 interface 必须经过测量这道关卡 · 而测量破坏反事实性。

类比已有的成功范例:

| 类比对象 | 关系本质 |
|---|---|
| CPU vs Sensor | CPU 再强大也不能直接感受温度 · 必须经过 sensor 接口 · sensor 永远不可替代 |
| Memory vs Cache | Cache 不是 "更小的 memory" · 是有局部性约束的特殊 memory · 范畴不同 |
| Compiler vs Linker | Linker 不是 "另一种 compiler" · 它处理跨文件符号解析 · compiler 处理不了 |
| DAC/ADC vs CPU | analog-digital 边界控制器 · 即使 FT QC 普及也仍需要 |

**$\Phi^{CF}_f$ 跟 FT QC 的关系类似 sensor 之于 CPU · 不互相替代 · 互相需要**。

## 5.5 · 三个超越点综合

综合 D1 子维度 + D3 的发现:

### 超越点 1 · D3 · 外部物理 oracle 的反事实查询

- **谁有**:只有 CFE (集成 photonic IFM)
- **谁没有**:FT QC 永远没有 (oracle 必须先被测进 quantum register)
- **应用**:物理样本检测 / 物理 trap probing / 现实世界的反事实感知
- **跟 FT QC 关系**:不竞争 · 形成 co-processor 关系

### 超越点 2 · D1.b · adversary-undetectable 查询

- **谁有**:$\Phi^{CF}_f$ 在 $\delta \to 0$ 极限
- **谁没有**:FT QC 即使无限大也没有 (unitary oracle calls 必然纠缠 → 可测 → 可被检测)
- **应用**:对抗性 reconnaissance / 不可察觉 audit / 涉密系统 stealth probe
- **永久性**:FT QC 量产后我们仍然独占

### 超越点 3 · D2 · 硬件成本-能力曲线

- **谁更便宜**:CFE · $\sim 6$ 数量级
- **延续性**:FT QC 量产后差距缩小但不消失 (类比模拟光学 FFT vs 数字 FFT)
- **应用**:任何需要 counterfactual 但量级 N 适中 ($\leq 100$) 的场景
- **过渡性**:FT QC 普及前的窗口 · CFE 占 niche

## 5.6 · 时间窗口分析

### 各阶段相对地位

| 阶段 | FT QC 状态 | CFE 地位 |
|---|---|---|
| 现在 (2026) | 没成熟 | 专用方案是唯一可行实现 · 占 niche 黄金期 |
| FT QC 早期可用 ($\sim$ 50-100 logical qubits) | 仅能做 demo · 不能解 100+ N 问题 | 仍然唯一可行 |
| FT QC 中期 ($\sim$ 1k logical qubits) | 能模拟 CFE · 但成本仍极高 | 在 D2 上仍便宜 · D3 上仍独占 |
| FT QC 后期 (普及) | 可以替代 CFE 做 D1 工作 | 退守 D3 (外部物理 oracle) · 永久占有 |

**整条时间线 CFE 都不会被完全淘汰** · 在 D3 上**永久独占**。

## 5.7 · 战略层结论

不要号称 "CFE 超越 FT QC" · 容易被学术界笑话。

应该号称:

> 用专用 photonic 硬件 · 在 FT QC 普及前提前解锁了 counterfactual function evaluation 算子。独占 FT QC 永远到不了的 interface domain (外部物理 oracle)。提供 FT QC 即便无限大也做不到的 adversary-undetectable 查询能力。

这三句都站得住 · 都不夸张 · 都有 narrative。

## 5.8 · 跟其他 quantum primitive 的关系

为完整 · 补充跟其他常见 quantum primitive 的关系:

| Primitive | 跟 CFE 的关系 |
|---|---|
| Grover search | 是标准 quantum query · CFE 是其反事实版本 (D2 + D1.b 优势) |
| Quantum walk | 不直接对应 · 但 NAND-tree 算法 [Farhi 2008] 可在 CFE 实现 |
| Amplitude amplification | $\Phi^{CF}_f$ 内部使用 (Lin-Lin 构造) |
| Quantum phase estimation | 跟 CFE 正交 · CFE 不替代 QPE |
| Hamiltonian simulation | 跟 CFE 正交 · 那是 unitary 主导 |
| Quantum signal processing (QSP) | 部分可用 · QSP 可作为 $f$ 的 oracle 实现 |
| Quantum singular value transformation (QSVT) | 同 QSP · 正交 |
| Variational quantum algorithms (VQE/QAOA) | 不直接对应 · CFE 可作为子例程 (active learning step) |
| Indefinite causal order | 正交 · 可组合 (未来工作) |

---

[← 上一章 · 04 组合代数](04-composition-algebra.md) · [下一章 · 06 减法计算范式 →](06-subtractive-paradigm.md)
