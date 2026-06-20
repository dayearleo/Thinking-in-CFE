# CFE 同构 · Bloom Filter → Stealth Lookup (PIR 物理实现)

> **触发**:论文 §17.4.1 的 worked example · 深度展开为独立 dev-note · 供 K-knowledge-build 路径下扩展为独立论文
> **状态**:同构 v1 设计 · 数学化完成 · 待 simulator 实现 + 硬件 PoC
> **真理源**:本文件 = Bloom Filter CFE 同构的单点真理源

## 0 · 引用 / 关联文档

- 论文 §17.4.1 · 高层 worked example
- 论文 §3 · CFE 算子定义
- 论文 §17.3 · 同构发现 5 步 SOP (本文件按此 SOP 走)
- supplement 11 · 同构提交模板 (本文件是该模板的 reference filling)

## 1 · 经典算法引用

- **Bloom 1970** · "Space/Time Trade-offs in Hash Coding with Allowable Errors" · CACM 13(7)
- **Broder, Mitzenmacher 2004** · "Network Applications of Bloom Filters" · Internet Mathematics
- **Cuckoo Filter** · Fan 2014 · COMNET 2014
- **XOR Filter** · Graf 2020 · arxiv 1912.08258

经典 Bloom Filter:

- 输入:set $S$ of items · 想测 "x ∈ S?"
- 实现:bit array $B$ of size $m$ + $k$ independent hash functions $h_1, \ldots, h_k$
- 插入:for each $x \in S$, set $B[h_i(x)] = 1$ for all $i$
- 查询:return AND of $B[h_i(x)]$ for all $i$
- 复杂度:O(k) per query · 空间 O(m) · false positive rate $\sim (1 - e^{-kn/m})^k$

## 2 · 识别的 CFE 同构

### 2.1 · 核心 primitive

Bloom Filter 的查询本质是 **"k 路并行 hash 查表 AND"**:

```
result = B[h_1(x)] AND B[h_2(x)] AND ... AND B[h_k(x)]
```

### 2.2 · CFE form

$$\Phi^{CF}_{\text{BloomLookup}}(x) = \Phi^{CF}_{\text{AND}}\left(\{\hat{O}_i\}_{i=1}^k, \delta, \epsilon\right)$$

where each $\hat{O}_i$ is the photonic oracle returning $B[h_i(x)]$ counterfactually.

物理实现:

- $k$ 路 photonic mode 对应 $k$ 个 hash position
- 每路 mode 是一个 obstacle iff $B[h_i(x)] = 0$
- 全 path clear (i.e., 所有 $B[h_i(x)] = 1$) → photon 干涉到 "membership = TRUE" detector
- 任一 obstacle → 干涉破坏 · "membership = FALSE"

### 2.3 · 为什么算同构

- Boolean 语义等价:经典 AND of $k$ bits == CFE Φ_AND of $k$ oracles
- 物理可实现:bit array 可以编码为 photonic chip 上 EAM (electro-absorption modulator) 的开关配置
- R2/R3 性质适用:CFE 反事实查询不触发 bit array 物理 read 事件 (传统 DRAM access 是可观察的物理事件)

## 3 · 复杂度比较 (4-dim)

| 维度 | 经典 Bloom | Quantum Bloom [Hosseini 2016] | CFE BloomLookup |
|---|---|---|---|
| $D_1$ Query time | $k$ CPU cycles | $\sqrt{k}$ amplitude amplification | 1 photonic flight (~ns) |
| $D_2$ Disturbance | 1 (cache pollution / DRAM access detectable) | 1 | $\delta$ (per probe) |
| $D_3$ Observability | ✅ memory access pattern leaks | ✅ same | ❌ R2 ($\delta \to 0$ 不可检测) |
| $D_4$ Hardware | 通用 CPU | FT QC (理论) | 集成 photonic chip ($\sim$ $100 ASIC) |

### 净评估

- $D_1$ 跟经典基本同阶 (photonic 慢的话也只是常数倍)
- $D_2/D_3$ 是 differentiator · 经典 Bloom 必然 detectable · CFE 不
- $D_4$ 比 FT QC 便宜 6 个数量级 · 跟 CPU 同数量级 (因为只是个小 ASIC)
- **净评估**:**CFE BloomLookup 在 privacy-critical 查询 niche 完全胜出**

## 4 · Killer Use Case

### 4.1 · 物理层 PIR (Private Information Retrieval)

**当前 PIR 的限制**:

- Chor 1995 introduced PIR · 多 server 信息论 PIR
- Single-server PIR (e.g., SealPIR, OnionPIR) 用 FHE · 巨大 overhead (1000×-10⁶× single query latency / bandwidth)
- Computational PIR 仍 RAM-heavy

**CFE PIR 解决**:

```
Client → photonic IFM probe → Server's Bloom Filter (物理 EAM 配置)
Server 物理上**无法**检测到 probe (R2 性质)
Client 得到 "membership = TRUE/FALSE" 答案
Total latency: 1 photonic flight (~ns) + classical comm overhead
```

跟现有 PIR 对比:

| Method | Bandwidth overhead | Compute overhead | Server detectability |
|---|---|---|---|
| Chor 1995 (multi-server) | O(n) | O(n) | detectable |
| SealPIR (FHE) | O(n^{1/3}) | O(n) FHE ops | detectable |
| OnionPIR | O(log n) | many FHE | detectable |
| **CFE PIR** | O(1) | O(1) photonic | **undetectable** |

### 4.2 · 二次 use case · Anti-fingerprinting Bloom Filter

很多系统用 Bloom Filter 做 user fingerprinting (canvas / WebGL / IP-based blocklist)。用户想知道自己是否在某 blocklist 上 · 但**不想让 server 知道你在测试**。

CFE BloomLookup 让用户**反事实**查询自己是否在 blocklist · server 完全察觉不到。

## 5 · 物理实现路径

### 5.1 · Hardware Level (Per §17.6)

**Level 1 · Programmable**:

- 一颗 SiN photonic chip · $k$ 路 mode (典型 $k = 5$ to $20$ for Bloom)
- EAM 阵列 $\sim m$ 个 (代表 bit array · $m$ 通常 $10^4$ - $10^6$)
- 单 photon source + SNSPD detector
- $\delta$ 可达 $\sim 10^{-3}$ (lab) · $\sim 10^{-6}$ (优化后)
- 估算 chip cost:$200k - $500k

### 5.2 · 关键工程难点

- $m$ scale to 大 (Bloom Filter 通常 $m \geq 10^6$) · photonic mode 数受限 · 可能要 hybrid (frequency multiplexing)
- Bit array update 频率 (insertion) 需要 EAM 高速切换 · 当前 GHz 可达
- 跟 client-server 通信集成 · 需要 standardized API

### 5.3 · 现有最接近的硬件

- Universal photonic processor (Hance 2025) · N=12 mode · 适合 $k$ small
- AIM Photonics PDK · 可以 fab 定制 EAM 阵列

## 6 · Simulator 设计

### 6.1 · Mock structure

```python
class BloomFilter:
    def __init__(self, m, k, hash_funcs):
        self.bits = [0] * m
        self.k = k
        self.hashes = hash_funcs
    
    def insert(self, x):
        for h in self.hashes:
            self.bits[h(x) % m] = 1
    
    def classical_lookup(self, x):
        # 经典查询 · 必触发 memory access log
        self.access_log.append(("lookup", x, time.time()))
        return all(self.bits[h(x) % m] for h in self.hashes)
    
    def cfe_lookup(self, x, delta):
        # CFE 反事实查询 · 触发概率 = delta
        for h in self.hashes:
            if not self.bits[h(x) % m]:
                if random.random() < delta:
                    self.access_log.append(("CFE_TRIGGERED", x, time.time()))
                return False
        return True
```

### 6.2 · Validation tests

- 10000 queries · classical lookups all logged · CFE lookups ~10 logged (δ=1e-3)
- False positive rate 跟理论吻合
- Lookup correctness identical between classical / CFE

(此 simulator 跟 supplement 10 的 HSM simulator 是 parallel · 同样架构)

## 7 · Falsification 条件

可被以下任一证伪:

- Bloom Filter 物理 encoding 在 photonic chip 上不可行 (e.g., EAM array 太大)
- $\delta$ 在 PIR application 需要 $< 10^{-9}$ · 但物理 lab 限 $> 10^{-5}$
- 经典 PIR 找到 sublinear 解 · 让 CFE-PIR 的优势消失
- 客户端 channel 仍可让 server 推断 "什么时候查了" (e.g., timing channel)

## 8 · 跟现有工作的关系

### 跟 PIR literature

- Compatible with Chor 1995 framework · CFE 提供新的 building block
- Replaces FHE-based query with physical-layer query
- Could combine: CFE-PIR for membership + FHE for value retrieval

### 跟 quantum 工作

- Hosseini 2016 quantum Bloom Filter · 在 quantum register 内 · 跟 CFE 不冲突
- 跟 Wiesner quantum money 类似精神:用物理保证替代密码假设

## 9 · Open questions

- **OQ1**:CFE BloomLookup 跟 differentially private Bloom Filter 怎么比?
- **OQ2**:能否扩展到 counting Bloom filter (不是 Boolean · 是 count)?
- **OQ3**:多 client 并发查询同 server · 是否有 fairness / DoS 问题?
- **OQ4**:跟 secure multiparty 协议 (e.g., PSI) 怎么集成?
- **OQ5**:能否 CFE-decode 整个 Bloom Filter 内容 (而不是单 query)?

## 10 · License

CC BY 4.0
