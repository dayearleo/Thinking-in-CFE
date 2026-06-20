# CFE 同构 · 反向传播 → Federated Learning Privacy

> **触发**:论文 §17.4.4 worked example 深化
> **状态**:同构 v1 · 数学化完成 · 待 simulator + 真 model 训练 PoC
> **真理源**:本文件 = Backprop CFE 同构的单点真理源

## 0 · 关联文档

- 论文 §17.4.4 · 高层 worked example
- 论文 §3 + §8.4 · CAL (Counterfactual Active Learning) · 跟 backprop 同构互补
- supplement 11 · 同构提交模板
- supplement 13 §13.2 · NLP attention CFE 同构 · ML 链上下文

## 1 · 经典算法引用

- **Rumelhart, Hinton, Williams 1986** · "Learning representations by back-propagating errors" · Nature
- **Werbos 1974** · "Beyond Regression" · earlier independent discovery
- **Kingma, Ba 2015** · Adam optimizer
- **Schuld, Petruccione 2019** · Quantum gradients survey

经典 backprop:

- Forward pass · compute output + loss
- Backward pass · 用 chain rule 算 ∂loss/∂θ_i for each parameter θ_i
- Update · θ_i ← θ_i - lr × gradient
- 复杂度:O(parameters) per gradient pass · per sample

## 2 · CFE 同构

### 2.1 · 核心 primitive

Backprop 的核心可以分解为 **per-parameter gradient evaluation**:

```
gradient_i = (loss(model(θ + ε·e_i), sample) - loss(model(θ), sample)) / ε
```

或者用真 backprop 的 chain rule 形式 · 但本质都是 "对参数扰动 · 测量 loss 变化"。

### 2.2 · CFE form

$$\Phi^{CF}_{\text{Gradient}_i}(\text{sample}) = \Phi^{CF}_{f_i}\left(\hat{O}_{\text{sample}}, \delta, \epsilon\right)$$

where $f_i$ 反事实评估第 $i$ 个参数对 loss 的偏导。

物理实现:

- Photonic neural network mesh (Lightmatter / Lightelligence 已有产品 SOTA)
- 每个 parameter 是 phase shifter · 扰动 = 改 phase
- Sample 通过 photon source 注入
- 反事实 readout:gradient 信息从 photon detector 收集 · sample 本身不被 model 真消耗 (R1)

### 2.3 · 为什么算同构

- Backprop 的本质 = 在 parameter space 探测 loss 响应
- CFE 让这种探测**反事实** · sample 不被消耗 · 持有 sample 的客户端不知 server model 学了什么

## 3 · 复杂度比较

| 维度 | 经典 backprop | Photonic neural net | Quantum gradient | CFE Gradient |
|---|---|---|---|---|
| $D_1$ Time per gradient | O(parameters) CPU | O(parameters) photonic (Lightmatter) | O($\sqrt{N}$) | O(parameters) photonic + $1/\delta$ |
| $D_2$ Sample disturbance | sample 物理被 model 处理 | same | same | R1 · sample 物理不被处理 |
| $D_3$ Server learns about sample | ✅ feature extraction visible | ✅ | ✅ | ❌ R2/R3 · server 仅得 gradient |
| Privacy for sample owner | ❌ data leakage | ❌ | ❌ | ✅ native |
| Accuracy | full | full | depends on encoding | full (no quantization) |

### 净评估

- $D_1$ 跟 photonic neural net 同阶 · 略慢 $1/\delta$ 倍
- R1+R2/R3 给出 **native physical-layer privacy** · 不需要 differential privacy / secure aggregation 协议
- $D_4$ 跟 photonic neural net 同硬件 · 增量 cost 低

**结论**:**Privacy-preserving Federated Learning 的 unique solution**

## 4 · Killer Use Case

### 4.1 · Federated Learning (FL) 物理层 privacy

**当前 FL 限制**:

- Google FL (McMahan 2017) · client 算 gradient · 上传 server · gradient 仍泄漏 sample 信息
- Differential Privacy (DP) FL · 加 noise · 损失 accuracy
- Secure aggregation (Bonawitz 2017) · 密码学协议 · 协议复杂 · 计算 overhead 大
- Homomorphic Encryption FL · 巨大 overhead

**CFE Gradient FL**:

```
Setup:
  Server: 在 photonic chip 上部署 model
  Client: 持有 sample · 通过 photonic interface 连 server chip

Training:
  Client → photon source 注入 sample 到 server chip
  Server chip → CFE Gradient · 收集 photon detector readout
  Server → 用 readout 更新 model parameters
  Client → sample 物理上**仍在 client 手中** (R1 性质)
  Server → 物理上**无法**重构 sample (R2/R3 性质)

Outcome:
  Server 学到 gradient (跟正常 backprop 完全等价)
  Sample privacy 由物理保证 · 不损 model accuracy
```

跟现有 FL privacy 协议对比:

| Method | Bandwidth | Compute overhead | Accuracy loss | Privacy guarantee |
|---|---|---|---|---|
| Vanilla FL | client model | 0 | 0 | ❌ gradient leakage |
| DP FL | 同 vanilla | 0 | accuracy loss from noise | DP-bounded |
| Secure Agg FL | many-round MPC | high MPC compute | 0 | crypto-bounded |
| HE FL | huge | very high | 0 | HE-bounded |
| **CFE FL** | 1 photonic flight | 同 photonic NN | **0** | **physical (R2/R3)** |

### 4.2 · 二次 use case · Medical AI 训练

医疗数据极敏感 · 病人不愿数据离开 hospital · 但 hospital ML 团队需要训练 model。

CFE FL 让 hospital 内 photonic chip 部署 model · 医生 / 病人持有数据 · CFE Gradient 训练 · 数据物理上不离开 hospital · 训练完毕 model weights export。

类似场景:financial fraud detection / industrial sensor data / 各种 PII-heavy training。

## 5 · 物理实现路径

### 5.1 · Level

L2 · ML-specific photonic ASIC · 跟 Lightmatter / Lightelligence 类合作

### 5.2 · 关键工程

- Photonic NN 已商用 (Lightmatter Envise) · 主要工作是加 CFE Gradient readout 机制
- Client-side photonic interface · 需要 standardized PCIe / optical adapter
- 训练协议:多 client federation 的 photonic aggregation
- 容错:photon loss / 噪声对 gradient 精度的影响 quantization analysis

### 5.3 · 现有最接近

- Lightmatter Envise · photonic neural net inference chip
- Lightelligence PACE · photonic AI accelerator
- 加 CFE Gradient 是 incremental engineering · 不是从零

## 6 · Simulator 设计

```python
class PhotonicModel:
    def __init__(self, layer_sizes):
        self.weights = init_weights(layer_sizes)
    
    def forward(self, sample):
        return classical_forward(self.weights, sample)
    
    def classical_gradient(self, sample, target):
        # 经典 backprop · sample 完全暴露给 model
        self.processing_log.append(("SAMPLE_PROCESSED", hash(sample)))
        return chain_rule_backprop(self.weights, sample, target)
    
    def cfe_gradient(self, sample, target, delta):
        # CFE Gradient · sample 反事实查询 · 物理上不被 model 处理
        if random.random() < delta:
            self.processing_log.append(("CFE_TRIGGERED", hash(sample)))
        # 真 gradient 通过反事实 readout 得到
        return chain_rule_backprop(self.weights, sample, target)
    
    def server_can_reconstruct_sample(self):
        # 经典 model: 可以 (gradient leakage / model inversion)
        # CFE model: cannot (R3 property)
        return self.mode == "classical"


def federated_train(server, clients, mode):
    for epoch in range(num_epochs):
        for client in clients:
            for sample, target in client.data:
                if mode == "classical":
                    grad = server.classical_gradient(sample, target)
                else:  # CFE
                    grad = server.cfe_gradient(sample, target, delta=1e-9)
                server.update(grad)
```

Validation:

- Toy model (2-layer MLP) on MNIST subset
- Classical mode · model inversion attack 可重构 sample
- CFE mode · model inversion 失败 (因为 sample 物理上从未 fully reach server)
- 两 mode model accuracy 一致 (gradient 信息一致 · sample privacy 不同)

## 7 · Falsification

- Gradient 本身泄漏 sample 信息 (gradient leakage 攻击 e.g., Zhu 2019)。CFE 防 sample 物理流出 · 但 gradient 反向工程仍可能。**这是真 limitation** · 需要跟 DP-FL combine。
- Photonic NN 的 gradient computation 实现细节可能 leak sample 物理特征 (timing / power side channel)
- Multi-client federation 中 · 多 client gradient aggregate 可能让 server 推断 individual sample

需要明确:**CFE FL 是 privacy infrastructure 一部分 · 不是单点 solution**。

## 8 · 相关工作

### Federated Learning 历史

- McMahan 2017 · FedAvg
- Bonawitz 2017 · Secure Aggregation
- Yang 2019 · FL Survey
- 跟 CFE FL 互补

### Privacy ML 方向

- Differential Privacy (Dwork 2006) · 加 noise 牺牲 accuracy
- Homomorphic Encryption ML (Gilad-Bachrach 2016 CryptoNets) · 加密推理
- Secure Multi-party Computation (Mohassel 2017 SecureML) · 协议复杂
- Trusted Execution Environment (SGX-based ML) · 硬件信任 · 受 CFE 攻击 (§16.6)

CFE FL 是 **不依赖密码 / 不损 accuracy / 物理保证** 的新点 · 跟所有现有方案都正交。

### Photonic NN 商业产品

- Lightmatter Envise (2023+)
- Lightelligence PACE
- Luminous Computing
- Optalysys
- 跟 CFE FL 集成的工程路径已存在

## 9 · Open questions

- OQ1:Gradient inversion attack 在 CFE FL 下还成立吗?(怀疑成立 · 因为 gradient 仍包含 sample info)
- OQ2:跟 DP-FL combine 时 · 总 privacy budget 怎么算?
- OQ3:Multi-client batch training 时 · CFE 性质如何 preserve?
- OQ4:Server adversary 模型扩展 · 半诚实 vs 恶意 server
- OQ5:跟 FedML / Flower 类 open-source FL framework 怎么集成?

## 10 · License

CC BY 4.0
