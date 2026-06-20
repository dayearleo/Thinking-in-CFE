# CFE 同构 · 图可达性 → Stealth Network Probe

> **触发**:论文 §17.4.2 worked example 深化
> **状态**:同构 v1 · 数学化完成 · 待 simulator + 硬件 PoC
> **真理源**:本文件 = 图可达性 CFE 同构的单点真理源

## 0 · 关联文档

- 论文 §17.4.2 · 高层 worked example
- 论文 §3 · CFE 算子定义
- supplement 11 · 同构提交模板
- 平级:`dev-notes/011 / 013 / 014` (4 个 §17.4 同构深化)

## 1 · 经典算法引用

- **BFS / DFS** · Knuth volume 1 · 经典 O(V+E)
- **Dijkstra 1959** · "A Note on Two Problems in Connexion with Graphs"
- **A\*** · Hart, Nilsson, Raphael 1968 · IEEE Trans. Sys. Sci. Cybernet.
- **Bidirectional search** · Pohl 1971
- **Quantum walk** · Childs 2003 · arxiv quant-ph/0306054 · 给出 $\sqrt{N}$ 加速

## 2 · CFE 同构

### 2.1 · 核心 primitive

图可达性核心是 **"存在 path from s to t 吗?"**:

```
Reachable(s, t, G) = OR over all paths p (s → t in G) of (
  AND over edges e in p of (e ∈ E)
)
```

### 2.2 · CFE form

$$\Phi^{CF}_{\text{Reachable}}(s, t, G) = \Phi^{CF}_{\text{OR}}\left(\{\hat{O}_p\}_{p \in \text{paths}(s,t)}, \delta, \epsilon\right)$$

where each $\hat{O}_p$ is photonic oracle for "path p is fully traversable":

$$\hat{O}_p = \Phi^{CF}_{\text{AND}}\left(\{\hat{O}_e\}_{e \in p}, \delta', \epsilon'\right)$$

物理实现:

- 图 G 物理 embed 进 photonic chip · vertices = modes · edges = couplers
- Photon 从 s mode 注入 · t mode 接 detector
- 干涉强度 ∝ 总 reachable amplitude · CFE 反事实 readout 给 "reachable or not"
- 任何 edge 是 "broken" (network 中:packet drop / firewall) 等价于该 path 上 obstacle

### 2.3 · 为什么算同构

- 经典 reachability 是 Boolean predicate · CFE 直接表达
- 物理 photon 干涉本质上**就是**多 path superposition + readout
- 经典图算法 simulate physical 光路径在 graph 上行走;CFE 是 native 物理实现 · 不是 simulate

## 3 · 复杂度比较

| 维度 | BFS / DFS | Quantum walk | CFE Reachable |
|---|---|---|---|
| $D_1$ Time | O(V+E) | O($\sqrt{N}$) | O(photonic flight / longest path) ~ ns |
| $D_2$ Disturbance | 0 (本地计算) | 0 (本地 quantum) | R1 · 远程图 edge 不被实际 access |
| $D_3$ Observability | 远程网络可见 (e.g. ping / traceroute leak source IP) | same | ❌ R2 · stealth |
| $D_4$ Hardware | CPU | FT QC | photonic chip |

### 净评估

- $D_1$ 看场景:小图 photonic 快;大图 photonic mode 不够 · BFS 仍优
- $D_2/D_3$ 关键:远程网络拓扑探测时 · 只有 CFE 提供 stealth
- $D_4$ 中等 · 比 FT QC 便宜很多

**结论**:**stealth 远程网络可达性测试的 unique solution**

## 4 · Killer Use Case

### 4.1 · 军用情报 · stealth network mapping

**问题**:对手有 LAN · 想知道 "host A 跟 host B 之间是否有 alive route" · 不能用 traceroute / ping (暴露探测者 IP)。

**当前方案**:

- Passive listening · 等对手自己暴露 traffic pattern · 极慢
- Active probing · ping / traceroute / nmap · **暴露**
- Quantum radar · stealth detection 但仍是 active emission · 部分暴露

**CFE Reachability**:

- 物理 photon 干涉测试 reachability · 不发任何 detectable packet
- 跟对手 router / switch 物理光纤接口 (optical tap) 集成
- δ = 1e-9 · 对手网络监控完全察觉不到
- 单次可达性测试时间 ns 级

### 4.2 · 商业次 use case · supply chain hidden dependency 检测

软件供应链 · 想知道 "package A 是否最终依赖 package B" · 但不想 download A 跟 B 暴露给 package registry (e.g., for competitive intelligence)。

CFE Reachability 对依赖图反事实查询 · registry log 无 record。

## 5 · 物理实现路径

### 5.1 · Level

L3 · 跟物理光纤 / 网络硬件接口集成

### 5.2 · 关键工程

- Optical tap 跟 target network 物理介质耦合
- Photonic chip embedding 算法:把图 G 转 chip layout · NP-hard 但 ML 启发式可解
- Edge mapping:network edge → directional coupler 配置
- 失败模式:对手用 quantum-coherence detection 检测我方 probe · 但这本身极难

### 5.3 · 现有最接近

- IBM photonic interconnect (NeMo project) · photon-based network probing
- Quantum radar literature (Lloyd 2008) · 但 active emission 不 stealth

## 6 · Simulator 设计

```python
class NetworkGraph:
    def __init__(self, edges):
        self.edges = set(edges)
        self.probe_log = []
    
    def classical_reachable(self, s, t):
        # 经典 BFS · 每次访问 edge 在 access log 留痕
        visited = set([s])
        queue = [s]
        while queue:
            v = queue.pop(0)
            for w in self.neighbors(v):
                self.probe_log.append(("EDGE_PROBED", v, w, time.time()))
                if w == t:
                    return True
                if w not in visited:
                    visited.add(w)
                    queue.append(w)
        return False
    
    def cfe_reachable(self, s, t, delta):
        # CFE 反事实 · 物理上 photon 走遍 superposition · log 概率 delta
        actually_reachable = self._compute_reachability(s, t)
        if random.random() < delta * num_edges_in_paths(s, t):
            self.probe_log.append(("CFE_TRIGGERED", s, t, time.time()))
        return actually_reachable
```

Validation: 1000 reachability queries · classical 全 log · CFE log ~$\delta N$ 次。

## 7 · Falsification

可被证伪:

- 大规模 network (>10⁶ vertices) 无法 embed 进当前 photonic chip
- Optical tap 物理 interface 不可隐藏 (对手检测到 tap 设备本身)
- 物理 photonic crosstalk 让 R2 性质失效 (δ 下限受 crosstalk 主导)

## 8 · 相关工作

### Quantum walk literature

- Aharonov 2003 · discrete quantum walk
- Childs 2003 · continuous quantum walk
- Magniez 2010 · element distinctness via quantum walk
- 跟 CFE 不冲突 · CFE 提供物理实现路径

### Network reconnaissance literature

- Nmap (Lyon 2009) · 经典 active probing
- Passive OS fingerprinting (Lippmann 2003)
- Quantum radar (Lloyd 2008)

CFE Reachable 填补 "active probing 准确但暴露 / passive 不暴露但慢" 的中间空白。

## 9 · Open questions

- OQ1:跟 Tor / mix network 类匿名通信怎么比?
- OQ2:能否检测 directed reachability (s → t 但不 t → s)?
- OQ3:Multi-hop attack · 中间 hop 是 CFE-aware 防御怎么办?
- OQ4:可以扩展到 shortest path (Dijkstra 同构) 吗?
- OQ5:跟 packet-level traffic analysis 怎么结合 (hybrid attack)?

## 10 · License

CC BY 4.0
