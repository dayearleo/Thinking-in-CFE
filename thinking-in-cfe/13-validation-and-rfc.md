# 13 · 现实性验证维度 · Request for Comments

[← 返回 README](README.md)

## 13.1 · 本章定位 · 跟 §11 的区别

§11 已经说了 "**我们已知有限**" (limitations + open problems · 我们承认的盲区)。

本章不同 —— 它问 "**我们声称的事 · 谁来证伪 / 证实**":

| 维度 | §11 是什么 | §13 是什么 |
|---|---|---|
| 视角 | 内部自我审查 | 外部独立验证请求 |
| 内容 | "X 尚未做" / "Y 是开放问题" | "我们声称 X · 需要某领域专家用某方法验证" |
| 目的 | 防止 hype | 让 CFE 体系跨过 "**作者声明**" 到 "**独立可重复**" 这道门 |

本章是论文整体的 **falsifiability 保证** · 也是给学界 + 工程界的 **RFC (Request for Comments)** · 邀请系统性 review。

## 13.2 · 学界需要验证的维度

按 4 个子领域分:

### 子领域 A · 量子信息理论 / 复杂度理论

**待验证声明 1 · 算子形式定义的良定义性**

- **声明**:§3 的 $\Phi^{CF}_f$ 在 (P1, P2, P3) 三条性质下是 well-defined · 不存在 contradiction
- **需要的验证**:用 quantum information formalism 重写定义 · 证明对任意 $\epsilon, \delta \in (0,1)$ 和任意 $f$ · 存在算子实现满足三条
- **审稿请求**:量子信息理论学者 · 特别是熟悉 [Lin-Lin 2015] bomb query model 框架的
- **证伪条件**:发现存在某 $\epsilon, \delta, f$ 组合让 (P1, P2, P3) 不能同时满足 → 我们必须修改定义

**待验证声明 2 · §4 cost composition theorem 草案**

- **声明**:§4.3 给出的 5 种组合 cost 上界是正确的
- **需要的验证**:严格证明 (或反例)
- **审稿请求**:量子查询复杂度理论学者
- **证伪条件**:任一组合上界被反例打破

**待验证声明 3 · §7 多维复杂度框架的合理性**

- **声明**:disturbance complexity $D_\Delta(f)$ 和 observability complexity $\eta(f)$ 是有用的新复杂度量度
- **需要的验证**:形式化定义 · 给出非平凡 lower bound · 证明它们跟 $Q(f), B(f)$ 不平凡相关
- **审稿请求**:复杂度理论学者 (TCS community)
- **证伪条件**:发现 $D_\Delta$ 或 $\eta$ 可被现有复杂度量度 trivially 表达 · 失去 novelty

**待验证声明 4 · §7.7 CFP 复杂度类的位置**

- **声明**:$\text{CFP} \subseteq \text{BQP}$ · 包含但可能严格小于 BQP
- **需要的验证**:证明严格包含或等价
- **审稿请求**:量子复杂度理论专家
- **证伪条件**:证明 CFP = BQP (则 CFP 没有 novelty) 或 CFP $\not\subseteq$ BQP (则我们的定义有问题)

### 子领域 B · 物理理论

**待验证声明 5 · §3 R1/R2/R3 三性质的物理实现可能性**

- **声明**:存在物理 protocol 同时实现 R1 (触发率任意小) + R2 (adversary 不可检测) + R3 (输入不消耗)
- **需要的验证**:文献 [Franco-Camillini-Galvão 2026] 单点验证 + 需要更多团队独立复现
- **审稿请求**:量子光学实验学者 · 特别是 IFM 实验组
- **证伪条件**:发现物理上某两条性质互斥 (e.g. R1 和 R2 在 $\delta < $ 某阈值时无法同时满足)

**待验证声明 6 · §5 D3 永久独占性论点**

- **声明**:FT QC 永远无法对 "外部物理 oracle" 做反事实查询
- **需要的验证**:严格证明 FT QC 实现反事实查询必然涉及测量 · 测量破坏反事实性
- **审稿请求**:量子计算理论学者 · 特别是研究 hybrid quantum-classical 系统的
- **证伪条件**:有人提出 FT QC 可以通过某 trick 接入外部物理 oracle 而不破坏反事实性

### 子领域 C · 算法学 / 程序语言

**待验证声明 7 · §8 6 个算法模板的正确性**

- **声明**:CPA / CBB / CAL / CV / CA* / CGTS 在其声明的复杂度内正确求解对应问题
- **需要的验证**:每个模板的形式化证明 + simulator 实验
- **审稿请求**:量子算法学者
- **证伪条件**:任一模板存在反例输入 · 复杂度声明被打破

**待验证声明 8 · §6 减法计算范式 (SCP) 的范式独立性**

- **声明**:SCP 跟 7 种已有非传统范式 (lazy / speculation / reversible / 等) 是**正交**的 · 不可归约
- **需要的验证**:形式化跟每种范式的对比 · 给出不可归约证明
- **审稿请求**:程序语言理论学者 + 算法范式学者
- **证伪条件**:发现 SCP 可被某种已有范式表达 → 我们的 novelty 仅是 syntactic sugar

### 子领域 D · 跨学科与历史

**待验证声明 9 · §2 先行研究的完整性**

- **声明**:本论文遗漏的相关工作可忽略
- **需要的验证**:有经验的领域学者地毯式补充我们漏掉的引用
- **审稿请求**:任何熟悉 IFM / counterfactual computation 历史的学者
- **证伪条件**:发现 5 年内有重要工作直接做了我们声称是 novel 的事

## 13.3 · 工程技术界需要验证的维度

按 4 个子领域分:

### 子领域 E · 集成 photonic 硬件

**待验证声明 10 · §3.9 SOTA 参数**

- **声明**:N = 12 universal photonic processor 已成熟 · 5 dB loss · visibility > 95%
- **需要的验证**:多个独立芯片 fab 团队复现 · 公开 benchmark 数据集
- **审稿请求**:photonic integrated circuit (PIC) 工程师 · 特别是 SiN / Si 平台
- **证伪条件**:文献声称的参数无法在多个独立 fab 复现

**待验证声明 11 · §11.2 硬件瓶颈预测**

- **声明**:loss 是 N 上限的核心瓶颈 · N=100 时 ~50 dB 不可用
- **需要的验证**:loss budget 模型独立验证 · 不同 platform (Si vs SiN vs LiNbO3 vs femtosecond-written) 横向对比
- **审稿请求**:photonic 平台工程师
- **证伪条件**:发现某 platform 在 N=100 仍可用 → 我们的预测过悲观

**待验证声明 12 · §5.3 vs FT QC 的 6 个数量级成本差距**

- **声明**:专用 photonic IFM 实现 $\Phi^{CF}_f$ 比 FT QC 模拟便宜 $\sim 10^6$ 倍
- **需要的验证**:严格的 cost model · 含 surface code overhead / cryogenic infrastructure / fab cost / operating cost
- **审稿请求**:量子计算工业 cost analyst · 同时熟悉 FT QC 和 photonic 平台
- **证伪条件**:cost model 显示实际差距 < 100 倍 → 我们的差距声明被打折

### 子领域 F · 算法运行

**待验证声明 13 · §8 算法模板的实际可执行性**

- **声明**:CPA / CBB 等模板可以在现有 photonic 硬件 (N ≤ 32) 上跑通
- **需要的验证**:在 [Franco-Camillini-Galvão 2026] 同类硬件或其他 universal photonic processor 上实际跑通至少一个模板 · 公开结果
- **审稿请求**:量子算法实验组
- **证伪条件**:在现有硬件上跑模板时遇到不可调和的工程问题 · 算法层假设不成立

**待验证声明 14 · §4.4 嵌套深度 cascade 控制策略的有效性**

- **声明**:Reset 屏障 / 预算分配 / Adaptive 阈值 / 拒采样 4 种策略至少有一个能控制嵌套深度的 $\delta$ cascade
- **需要的验证**:simulator 实验 · 至少展示一种策略在嵌套深度 5+ 时 $\delta_{\text{tot}}$ 仍可控
- **审稿请求**:量子算法工程师
- **证伪条件**:4 种策略都失效 → C3 嵌套实际不可用

### 子领域 G · 系统集成

**待验证声明 15 · 跟经典系统的 interconnect**

- **声明**:CFE 算子可作为 specialized co-processor 接入经典 CPU/GPU 系统
- **需要的验证**:接口规范 · API 标准化 · 延迟模型
- **审稿请求**:系统架构师 / 异构计算专家
- **证伪条件**:发现接入延迟过高 (e.g. ms 级) 让 CFE 在所有现实应用场景中都不可用

**待验证声明 16 · 编程模型 / 编译器 / 调试器工具链可行性**

- **声明**:§4.5 草案的 programming model 可以实现
- **需要的验证**:至少一个 toy 编译器 + simulator backend 跑通
- **审稿请求**:量子编程语言研究者
- **证伪条件**:类型系统设计有不可调和的内部矛盾

### 子领域 H · 应用层 (每个 A1-A6 独立)

**待验证声明 17 · A1 NAND-tree 算法的 photonic 实物可行性**

- **声明**:NAND-tree 量子算法 [Farhi 2008] 可以在 N=8-16 photonic IFM 上跑通
- **需要的验证**:在 [Franco-Camillini-Galvão 2026] 类硬件上跑小规模 NAND-tree · 公开数据
- **审稿请求**:量子算法 + photonic 实验合作组
- **证伪条件**:跑出来跟理论复杂度差异大 → 算法 + 硬件配对有问题

**待验证声明 18 · A2 单细胞多 assay 的生物可行性**

- **声明**:单细胞可以承受 N=20-50 种 photon-based assay 而保持存活
- **需要的验证**:湿实验 · 不同 photon 波长 / 强度 / 时间 combinations 的细胞存活率
- **审稿请求**:细胞生物学家 + quantum biology 学者
- **证伪条件**:photon 累积剂量超过临界值 · 细胞仍死亡 → A2 假设不成立

**待验证声明 19 · A3 / A5 商业 customer 真实需求**

- **声明**:制药 / 半导体行业客户愿意为反事实成像 / wafer 检测付溢价
- **需要的验证**:客户访谈 · pilot 项目 · 价格敏感度分析
- **审稿请求**:行业咨询师 / 早期客户
- **证伪条件**:客户访谈显示现有方案 (经典 microscopy / 现有 wafer inspection) 已足够 · 没有 CFE 升级需求

**待验证声明 20 · A4 军用 / 情报 stealth probing 监管路径**

- **声明**:CFE-based stealth probing 设备能通过监管 (军用许可 / 出口管制)
- **需要的验证**:监管专家咨询 · 历史先例 (类似 quantum radar 设备的监管路径)
- **审稿请求**:国防工业律师 / regtech 专家
- **证伪条件**:发现监管路径不可行 · A4 商业化阻塞

## 13.4 · Request for Comments · 具体审稿请求

我们邀请以下社区独立 review 本论文:

### 学术社区

| Venue / 社区 | 重点 review 章节 |
|---|---|
| QIP (Quantum Information Processing) 年会 | §3 算子定义 · §4 组合代数 · §7 复杂度 |
| QCRYPT / QCMC | §5 跟 FT QC 关系 · §6 范式 |
| ICALP / FOCS / STOC | §7.7 CFP 复杂度类 |
| arxiv quant-ph | 全文 · 预印 + 公开 review |
| Quantum (open-access journal) | 适合论文最终提交版 |
| Physical Review X | 适合论文最终提交版 |
| Nature Communications | 跟 [Franco-Camillini-Galvão 2026] 同 venue |

### 工程社区

| Venue / 社区 | 重点 review 章节 |
|---|---|
| OFC (Optical Fiber Communication) | §3.9 + §11.2 photonic 平台参数 |
| CLEO (Conf. on Lasers and Electro-Optics) | 同上 |
| IEEE Photonics conferences | 工程可行性 |
| Quantum Engineering 期刊 | 跨学科 review |

### 工业 / 应用社区

| 受众 | 重点 review 章节 |
|---|---|
| 半导体 inspection 企业 (ASML / KLA / Hitachi) | §10 A5 |
| 量子成像创业公司 (QuantIC ecosystem) | §10 A3 + A6 |
| 生物显微镜厂商 (Zeiss / Leica / Olympus) | §10 A2 + A3 |
| 国防量子科技合同商 | §10 A4 |
| 量子计算大厂 (PsiQuantum / Xanadu / IBM Quantum) | §5 + §11 hybrid 架构 |

## 13.5 · 给审稿人的具体问题清单

为方便 review · 我们提出具体问题:

### 给量子信息理论学者

- Q-T1 · §3 定义中的 $\delta$ 跟 [Lin-Lin 2015] 的 $\epsilon$ 是不是同一个量?
- Q-T2 · §4 的嵌套组合 C3 的 $\delta_{\text{tot}}$ 上界是否 tight?
- Q-T3 · §7.7 CFP 定义中要求 "多项式 $\delta$ 预算" 是否合理?
- Q-T4 · §5.5 超越点 2 (adversary-undetectable) 是否真的对 FT QC 不可达?

### 给 photonic 工程师

- Q-E1 · §3.9 报告的 SOTA 参数 (5 dB loss · 95% visibility · N=12) 是否准确?
- Q-E2 · §11.2 关于 N=100 时 loss 不可用的预测是否过悲观?
- Q-E3 · 嵌套 cascade 控制策略 (§4.4) 哪个在你的平台最可行?
- Q-E4 · 跟 [Franco-Camillini-Galvão 2026] 类硬件跑 §8 算法模板有什么 practical 困难?

### 给算法学者

- Q-A1 · §8 6 个模板是否覆盖你认为最有 impact 的算法类?
- Q-A2 · §6 SCP 范式跟你熟悉的哪个 paradigm 最像 (即使我们论证它们正交)?
- Q-A3 · §9 决策树的 7 个问题是否能 capture 所有该问的问题?

### 给行业专家

- Q-D1 · §10 A1-A6 哪个最像你行业的真痛点?
- Q-D2 · 哪些应用我们漏了 (满足 R1/R2/R3 + 物理化 + sparsity)?
- Q-D3 · 你的客户对 "不消耗 / 不暴露 / 不破坏" 的 willingness-to-pay 是多少?

## 13.6 · 我们承诺的响应方式

收到外部 review 后我们承诺:

- **接受证伪**:任何被严格证伪的声明 · 我们在论文更新版中明确撤回 + 标注谁证伪
- **接受改进**:任何被指出的更精确表达 / 补充引用 · 我们 incorporate · 标注致谢
- **公开 review**:论文托管在 GitHub · review 通过 issue / PR 公开进行 · 不做闭门审稿
- **版本控制**:每次 substantive 修改打 git tag · 历史可追溯

## 13.7 · 联系方式

(论文正式发表时填写)

- 主要作者邮箱: TBD
- GitHub repo: TBD (本论文 markdown 源码)
- arxiv preprint: TBD
- Issue tracker: GitHub Issues

## 13.8 · 现实性的元层定义

最后澄清 "现实地成立" 的定义。我们采用 Lakatos / Popper 的 falsificationism 标准:

**一个声明 "现实地成立" 当且仅当**:

1. 它**可被陈述**为具体可验证 / 可证伪的命题
2. **存在独立第三方**能在合理时间内执行验证
3. **存在条件清晰的证伪场景** (我们提前说好什么会让我们撤回)
4. **如果通过独立验证 · 它能被使用** (实际算法 + 实际硬件 + 实际应用)

按此标准 · 本论文当前状态:

- §3 算子定义 · 满足 1 · 部分满足 2 · 满足 3 · 待 4
- §4 组合代数 · 满足 1 · 部分满足 2 · 满足 3 · 待 4
- §5 D1/D2/D3 · 满足 1 + 2 + 3 · D1/D2 满足 4 · D3 永久独占 4
- §6 SCP 范式 · 满足 1 · 部分满足 2 · 满足 3 · 待 4
- §7 多维复杂度 · 满足 1 · 待 2 · 满足 3 · 待 4
- §8 算法模板 · 满足 1 · 待 2 · 满足 3 · 待 4
- §10 A1-A6 · 满足 1 · 部分满足 2 (有实验文献支持) · 满足 3 · 待 4

**总体**:论文体系**部分现实成立** (基础物理 ✅ · 实验少数 ✅ · 多数声明待独立验证)。本章是把这个 "部分" 变成 "完整" 的 roadmap。

## 13.9 · 小结

本章把 §11 的 "我们已知有限" 升级为 "**我们邀请被验证**":

- **20 条具体声明** · 每条带 (a) 内容 + (b) 需要的验证方法 + (c) 审稿请求 + (d) 证伪条件
- **3 个学界 review venue 列表** + **3 个工程界 review venue 列表** + **5 类工业受众**
- **具体审稿问题清单** · 分 4 类受众
- **响应承诺** · 公开 review · 接受证伪 · 版本控制
- **现实性的 Popper-style 定义** · 严格区分"作者声明"和"独立可验证"

我们清楚:**本论文不是终点 · 是 RFC 起点**。

---

[← 上一章 · 12 结论](12-conclusion.md) · [下一章 · 14 突破证明 →](14-breakthrough-demonstration.md)
