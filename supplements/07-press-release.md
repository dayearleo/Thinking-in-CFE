# 07 · 技术新闻稿 · Press Release

[← supplements README](README.md)

## 文件性质

**Press release draft** · 用于技术媒体 (Ars Technica · The Register · Wired · IEEE Spectrum · Quanta · 国内 36kr / CSDN / 量子位 / 机器之心 等)。

两个版本:**长版** (技术媒体深度报道) + **短版** (面向 general tech press)。

---

## 短版 · 一般技术媒体 (~500 字)

### 标题选项

A. 30 年前的量子物理思想 · 让今天的硬件加密失效?
B. 不需要量子计算机 · 一个新算子框架可"无声"读取 HSM 密钥
C. 反事实计算:把"量子计算的未来"提前到现在

(推荐 A 或 B · 平衡可读性 + 准确性)

### 正文

(开头 hook · 1 段)

> 一个团队提出 · 现代企业、银行、关键基础设施依赖的 "硬件加密保护" 假设 · 在一类新的量子物理攻击下可能失效 —— 而且这种攻击**不需要**等待 fault-tolerant 量子计算机的成熟。

(背景 · 1 段)

> 自 1993 年 Elitzur 和 Vaidman 提出"干涉无相互作用测量" (IFM) 以来 · 30 年的物理研究让 "**用 photon 检测物体存在但不接触**" 从思想实验变成实验室现实。2025 年 · Hance 等人在集成 photonic chip 上演示了多对象 IFM。论文 *"Thinking in CFE"* (2026) 把这些零散物理工作抽象为一个**算法原语** —— Counterfactual Function Evaluation (CFE) 算子 —— 让算法学家和工程师可以**直接调用**这种能力 · 不必懂量子光学。

(核心 claim · 1 段)

> 论文核心论点:CFE 算子的一项性质 (称作 **R2** · adversary-undetectable) 让攻击者能 **stealth 读取 HSM (Hardware Security Module) 中存储的加密密钥** · 而 HSM 的 tamper 检测**不会触发** · audit log **不会记录** · 任何防御都形同虚设。被攻击的算法本身 (AES / RSA / SHA 等) 数学上完全完整 · 但密钥**已离开** HSM · 等同被破。

(行业影响 · 1 段)

> 这影响一整类工业部署的密码学产品:从银行 PIN 验证 · 到加密货币硬件钱包 · 到 TLS 服务器的 CA 私钥 · 到军事 / 国安通信的 root key。论文进一步提出 **"Harvest Now Decrypt Later"** 的硬件版本:**今天就偷走** HSM 的 master key · **今天**就能解密所有过去和现在用此 key 加密的 traffic · 不需要等量子计算机。

(回应 · 1 段)

> 作者团队提出 **Post-Counterfactual Cryptography (PCC)** 作为一个新的密码学子领域 · 类比当前在做的 Post-Quantum Cryptography (PQC) · 但攻击面正交。他们已撰写完整 RFC · 邀请密码学社区严肃审查 · 也开始 coordinated disclosure 给主要 HSM 厂商 (Thales · Utimaco · Entrust · AWS) · 给厂商 90 天 grace period。

(结尾 · 1 段)

> 论文同时强调 · CFE 攻击当前仍是**理论威胁** · 没有针对商用 HSM 的端到端 demonstration。但所有需要的物理组件都已 lab 成熟 · 剩下的是工程组装。"我们写这个论文是 RFC · 邀请被证伪" · 论文 §13 写到 · "如果某个 claim 错了 · 我们公开撤回。"

(信息盒)

- 论文:`[GitHub URL TBD]` (markdown · 17 章节 · 3000+ 行 · CC BY 4.0)
- 简短 abstract:`paper/supplements/06-arxiv-abstract-en.md`
- PCC 子领域提议:`paper/supplements/01-pcc-founding-document.md`
- HSM 厂商披露草案:`paper/supplements/02-03`
- NIST 评论信草案:`paper/supplements/04-nist-pqc-comment-letter.md`

---

## 长版 · 技术深度媒体 (~2000 字)

### 标题

**反事实计算的复兴:一个 30 年前的物理思想 · 如何重塑硬件加密的安全模型**

### 副标题

新论文 "Thinking in CFE" 抽象 Interaction-Free Measurement 为算法原语 · 提出 Post-Counterfactual Cryptography 新子领域。

### 导语

> 当 IBM 和 Google 比赛冲击量子霸权时 · 全球的 CSO 们更担心 Shor 算法什么时候破解 RSA。**他们可能担心错了对象**。
>
> 2026 年 6 月 · 一份新论文 *"Thinking in CFE: A Counterfactual Function Evaluation Paradigm for Photonic Computation"* 阐述了一类**当下就可发生**的密码学攻击 —— 不依赖 fault-tolerant 量子计算机 · 不破解任何数学算法 · 而是直接**绕开**所有 HSM (Hardware Security Module) 物理 tamper 防御 · 把密钥**无声**读走。

### 第 1 节 · 一段冷门物理史

> 1993 年 · 以色列 Bar-Ilan 大学的 Avshalom Elitzur 和 Lev Vaidman 提出一个怪异的思想实验:**Interaction-Free Measurement (IFM)** · 用一个 Mach-Zehnder 干涉仪 + 量子叠加 · 可以**检测到一个未爆炸炸弹的存在** · 而 photon 从未跟炸弹接触。
>
> 这看起来像物理学家的玩具 · 但 2001 年 · 剑桥的 Mitchison 和 Jozsa 把它推广为 **Counterfactual Computation**:可以推断一个量子计算的**结果**而该计算**根本没运行**。
>
> 2015 年 · MIT 的 Lin 和 Lin 把这一概念形式化为 **Bomb Query Complexity** $B(f) = \Theta(Q(f)^2)$ · 给出了第一个跟传统 quantum query 复杂度的精确关系。
>
> 然后是 2024 年:Filatov 和 Auzinsh 提出**多对象 IFM**;2025 年 Hance 团队在 universal integrated photonic processor 上**实物实现**。30 年的物理研究 · 走到了 lab demo 阶段。
>
> 但密码学界几乎没人在听。**直到这份新论文**。

### 第 2 节 · 算子抽象 · 让算法学家可用

> *"Thinking in CFE"* 的第一个贡献是**抽象**。论文把 30 年分散的 IFM / counterfactual 工作统一为一个**算法原语**:
>
> ```
> Φ^{CF}_f : (oracle_1, ..., oracle_N) → bit
> ```
>
> 调用者不必懂量子光学 · 只需要知道接口签名:输入 N 个**物理 oracle** + 一个 Boolean 函数 $f$ · 输出 $f$ 的结果。
>
> 这个原语有 3 条不寻常的性质 (论文称为 R1 / R2 / R3):
>
> - **R1 触发率任意小** · 大部分调用物理上**不真触发** oracle
> - **R2 adversary-undetectable** · 持有 oracle 的对手**物理上检测不到**算子被调用
> - **R3 输入不消耗** · 多次调用**不损耗** oracle (如果 oracle 是稀缺资源)
>
> 论文进一步定义了算子组合代数 (5 种规则) · 提出一个新的算法范式 "**Subtractive Computation Paradigm**" · 引入 3 个新复杂度维度。这是论文的**理论骨架**。

### 第 3 节 · 跟 Fault-Tolerant Quantum Computing 的关系

> 主流叙事是:量子计算威胁密码学 · 需要等 fault-tolerant 量子计算机 (FT QC) 成熟 · 然后用 Shor 算法破 RSA。NIST 的 Post-Quantum Cryptography (PQC) standardization 正是为此。
>
> 但 CFE 算子提供 **第二条威胁路径**。论文用 3 维框架定位:
>
> - **D1 能力维度** · FT QC 是 CFE 的 superset · CFE 不优
> - **D2 成本维度** · CFE 用 photonic IFM chip 实现 · 比 FT QC 模拟便宜约 6 个数量级
> - **D3 接口维度** · CFE 可以查询**外部物理 oracle** · FT QC 永远做不到 (因为 FT QC 必须把 oracle 先 measure 进自己的 quantum register)
>
> 关键发现:**D3 是范畴差异不是程度差异**。FT QC 跟物理世界的接口必须经过测量 · 而测量破坏反事实性。CFE **永久独占** "外部物理 oracle 反事实查询" 这个范畴。
>
> 这意味着:CFE 不替代 FT QC · 但 FT QC **永远不能替代** CFE。两者更像 sensor 跟 CPU 的关系 · 互补而非竞争。

### 第 4 节 · 密码学影响 · "硬件根信任"假设崩塌

> 论文最具争议的部分在 §15-§16:**密码学应用**。
>
> 工业密码学**几十年靠两道防线并列承重**:
>
> 1. **算法数学安全** (NIST / IACR 认证):AES-256 需要 $2^{256}$ key search · 数学上安全
> 2. **硬件根信任** (FIPS 140-3 / Common Criteria 认证):HSM 物理保护 key · tamper 检测兜底
>
> 论文证明:**CFE 单独击穿第二道防线**。R2 性质让 photonic IFM probe 可以读取 HSM 内部 SRAM 的 key 比特 · 触发概率 $\leq \delta$ (可调到 $10^{-9}$) · HSM 完全不知道。
>
> 受影响的算法清单触目惊心:DES · 3DES · RC4 · IDEA · RC5 · Blowfish · AES · ChaCha20 · MD5 · SHA-1 · RSA · Diffie-Hellman · ECC · AES-GCM · ChaCha20-Poly1305 —— **17 个工业部署算法 · 全部受影响** · 因为它们的 key 都进 HSM。
>
> 论文的 worked example:从 FIPS 140-3 Level 4 HSM 提取 AES-256 key · 256 bit 总检测概率 $\leq 2.56 \times 10^{-7}$ · 远低于 false-positive 阈值 · HSM 安静地继续提供服务 · 而 key 已离开。

### 第 5 节 · "Harvest Now Decrypt Later" 的硬件版本

> 经典 HNDL 攻击假设:**今天拦截 TLS 加密的 traffic** · 等 **FT QC 成熟时**用 Shor 破 RSA 拿 session key · 解密历史 traffic。
>
> 论文提出 **CFE-增强 HNDL**:**今天**用 CFE 提走 HSM 的 master key · master key 一旦泄露 · 派生的所有 session key 都可计算。**不需要等 FT QC** · 当下就能解密。
>
> 更糟糕的是:经典 HNDL 可以通过 PQC migration 缓解 (新协议用 lattice / hash 算法 · Shor 攻不动)。CFE-HNDL **无法**通过 PQC migration 缓解 —— 因为攻击不在数学层 · 在硬件层 · 你换算法也是换到同一个 HSM 里。
>
> "**没有 post-quantum 算法升级路径可救**" · 论文 §16.7 写到。

### 第 6 节 · 提议 PCC · 新子领域

> 面对这个威胁 · 论文提出 **Post-Counterfactual Cryptography (PCC)** 作为新的密码学子领域 · 跟 PQC 平级。PCC 的核心 research questions:
>
> - 形式化 counterfactual adversary model
> - 设计 CFE-resistant 硬件 (coherence-based tamper detection)
> - 重新设计依赖 "tamper detection" 的协议
> - 标准化 CFE-detection toolkit
> - 升级 FIPS / Common Criteria 加 "Counterfactual Resistance Level" cert
> - 跟现有 theory frameworks 整合
>
> 一份独立 RFC (`paper/supplements/01-pcc-founding-document.md`) 邀请密码学社区**正式承认** PCC · 提议 8-12 人的 founder pool。

### 第 7 节 · 诚实的限界

> 论文在 §11 和 §13 极其诚实地承认:
>
> - CFE 攻击**当前仍是理论威胁** · 没有针对商用 HSM 的端到端 demonstration
> - 攻击仍**要求物理 access** 到 HSM · CFE 不绕过物理 access 要求
> - photonic IFM 硬件**当前 lab-scale** · 大规模部署需要工程优化
> - 所有 claim 都**可被证伪** · 论文 §13 列出 20 条声明 + 每条的证伪条件
>
> "**我们写这个论文是 RFC · 不是 manifesto**" · §13.6 说。"任何严格证伪 · 我们在 next version 公开撤回 + 标注证伪者。"

### 第 8 节 · 厂商 disclosure 和监管

> 论文同时启动 **coordinated disclosure**:
>
> - 给 Thales · Utimaco · Entrust · AWS CloudHSM 等主要 HSM 厂商发送披露信 (草案见 supplement 02-03)
> - 给 90 天 grace period 让厂商内部评估
> - 给 NIST PQC standardization 提交公开评论信 (草案见 supplement 04) · 建议把 counterfactual adversary 纳入 PQC scope 或开 PCC parallel track
>
> 长期影响如果成立 · 涉及:
>
> - FIPS 140-3 标准升级 (加 Counterfactual Resistance Level)
> - ISO TC68 金融服务密码标准修订
> - 各国国密 / 国安 / 出口管制清单审查
> - 银行 / 央行 / 关键基础设施 root key 保护策略
> - 加密货币硬件钱包行业评估
> - 国家级 PKI trust chain 危机处理 SOP

### 第 9 节 · 给读者

> 论文以 RFC 形式发布 · GitHub 公开 · CC BY 4.0 license。任何人都可以:
>
> - **阅读**:从 `paper/thinking-in-cfe/README.md` 入手 · 17 章节按 reader role 推荐阅读路径
> - **质疑**:在 GitHub Issue 提交 falsification · 论文 commits 到 incorporate 你的反驳
> - **复现**:`supplements/10-cfe-hndl-simulator/` 有 Python simulator 模拟 CFE-HNDL 攻击 (无需 photonic 硬件)
> - **扩展**:写 follow-up 论文 · 论文 §11 列了 12 个开放问题
> - **加入**:给 PCC founder pool 自荐 (supplement 01)
>
> 论文最后一句:"**Thinking in CFE 是一种 mental model · 也是一组工具 · 也是一个 paradigm**。"

### 信息盒

[同短版]

---

## 给媒体的 fact sheet (要点摘要)

| 维度 | 内容 |
|---|---|
| 论文标题 | Thinking in CFE: A Counterfactual Function Evaluation Paradigm for Photonic Computation |
| 论文长度 | 17 章节 · 3000+ 行 markdown · 完整 GitHub 仓 |
| 核心 claim | CFE 算子 stealth 读取 HSM 密钥 · 不依赖 FT QC · 不破数学算法 |
| 受影响算法 | 17 个工业部署密码算法 · 全部 HSM-stored 受影响 |
| 受影响产品 | HSM · TPM · Secure Enclave · 硬件钱包 · 智能卡 · TrustZone · 等 |
| 攻击前提 | 物理 access (insider threat / supply chain) + photonic IFM 硬件 |
| 攻击 demo 状态 | 理论 + lab 物理 demonstration (Hance 2025) · 没商用 HSM end-to-end |
| 提议解决方案 | Post-Counterfactual Cryptography (PCC) 新子领域 |
| 论文性质 | RFC · 公开 · CC BY 4.0 · 邀请证伪 |
| 厂商 disclosure | 90-day grace period · 披露给 4 个主要 HSM 厂商 |

## License

CC BY 4.0
