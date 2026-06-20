# 08 · 30 分钟会议讲稿大纲 + Slide 草案

[← supplements README](README.md)

## 文件性质

**30 分钟会议演讲准备** · 适合 IACR / Crypto / QIP / CCS / Black Hat / DEFCON / 量子信息会议 等不同场合的版本。

## 整体结构 (30 分钟)

```
00:00-02:00  Hook + 反直觉问题                      (2 min)
02:00-05:00  30 年物理史 · 谁也没听过的 IFM         (3 min)
05:00-10:00  CFE 算子定义 + R1/R2/R3 三性质         (5 min)
10:00-15:00  跟 FT QC 的 3 维关系 (D1/D2/D3)        (5 min)
15:00-20:00  减法计算范式 + 算法模板 (CPA + CV)      (5 min)
20:00-25:00  密码学应用 · 17 算法系统化分析 + HSM   (5 min)
25:00-28:00  PCC 子领域提议 + RFC                   (3 min)
28:00-30:00  Q&A 引导 + 联系方式                    (2 min)
```

## Slide 草案 (30 张)

### Slide 1 · Title

```
            Thinking in CFE

A Counterfactual Function Evaluation Paradigm
        for Photonic Computation

         [Authors] · 2026
         [GitHub URL]
```

### Slide 2 · The Hook · 反直觉问题

```
                问题:

你能 "读取" 一个加密 HSM 里的密钥
        而 HSM **完全不知道** 吗?

  • 不触发 tamper sensor
  • 不留 audit log
  • 不消耗任何 API quota
  • 不需要 fault-tolerant 量子计算机

  答案:可以。靠 30 年前的物理。
```

### Slide 3 · 谁还记得 Elitzur-Vaidman 1993?

```
"未爆炸炸弹检测器"

      Mach-Zehnder 干涉仪
         ┌────────┐
   ──────│ BS1    │──────────┐
         └────────┘          │
              │              │
              ▼              ▼
        ┌─────────┐     ┌─────────┐
        │ Bomb?   │     │ Mirror  │
        └─────────┘     └─────────┘
              │              │
              ▼              ▼
         ┌────────┐
   ──────│ BS2    │──── D0
         └────────┘──── D1

如果 bomb 在 · D1 偶尔响 (但 photon 没接触 bomb!)
如果 bomb 不在 · 只有 D0 响

         ★ 检测到了 · 但没接触 ★
```

### Slide 4 · 30 年的物理史

```
1993  Elitzur-Vaidman    Interaction-Free Measurement
1995  Kwiat              Zeno-enhanced IFM (~100%)
2001  Mitchison-Jozsa    Counterfactual Computation
2006  Hosten             First lab demo
2013  Salih              Counterfactual Communication
2015  Lin-Lin            Bomb Query Complexity formalization
2019  Hance              On-chip counterfactual
2021  [N=8 paper]        Multi-path delayed-choice on chip
2024  Filatov-Auzinsh    Multi-object IFM proposal
2025  Hance              Multi-object IFM on universal chip

物理已经成熟 30 年 · 算法学家没在听
```

### Slide 5 · 我们要做什么

```
            本论文 = 算法抽象

      物理 (30 年)        算法学家 (从未)
      ────────────       ──────────────
      Φ_IFM 协议         不知道存在
      Zeno 实验           看不懂
      Bomb query          不知道怎么用

      ────────────────────────────────
              我们补这一层
      ────────────────────────────────

         CFE 算子 Φ^{CF}_f
         可调用接口
         组合代数
         算法模板
         应用方法论
```

### Slide 6 · CFE 算子 · 定义

```
   Φ^{CF}_f : (Ô_1, ..., Ô_N) × |ψ_0⟩ → y ∈ {0,1}


   P1 · 正确性    Pr[y = f(x)] ≥ 1 - ε

   P2 · 反事实    Pr[O_i triggered | x_i = 1] ≤ δ

   P3 · 代价      B_δ(f) = O(Q(f)² / δ)


   δ 是参数 · 可调到 10^-9 (实际工程值)
```

### Slide 7 · R1 / R2 / R3 三性质

```
        CFE 的本质 differentiator:


   R1 · 触发率任意小      δ → 0
        (物理上不真触发 oracle)

   R2 · 对手不可检测      adversary undetectable
        (oracle 持有者不知被查)

   R3 · 输入不消耗        non-consuming
        (oracle 可重复 query 不损耗)


   经典 / Grover / 标准量子查询 · 都不具备 R1+R2+R3
```

### Slide 8 · "等等 · 这不是已被 Lin-Lin 2015 cover 吗?"

```
   Lin-Lin 2015:bomb query 形式化 + B(f) = Θ(Q(f)²)
   ✅ 是的 · 这是基础

   我们补充的:

   • 多算子组合代数 (5 种 composition)
   • R2 / R3 性质对密码学的影响 (Lin-Lin 没分析)
   • 应用方法论 (Lin-Lin 是纯理论)
   • 跟 FT QC 关系的 3 维框架
   • 17 个工业算法的系统化 audit
   • PCC 子领域提议

   即:从 "纯理论" → "可工程化范式"
```

### Slide 9 · 跟未来 FT QC 的关系

```
              D1   能算什么 (capability)
              ↓
              FT QC ⊇ CFE   (FT QC 是 superset)
              
              ─────────────────────────────
              
              D2   硬件成本 (cost)
              ↓
              CFE ~ 6 个数量级便宜
              (photonic IFM vs FT QC overhead)
              
              ─────────────────────────────
              
              D3   接口域 (interface)
              ↓
              CFE 永久独占
              (外部物理 oracle · FT QC 永远到不了)
```

### Slide 10 · D3 是范畴差异

```
   FT QC 要查询外部物理对象?

   必须先 measure 它 → 数字化 → 进 quantum register

   但 measurement 是 destructive · 反事实性丢光

   ────────────────────────────────────────

   类比:CPU 跟 sensor 的关系

   CPU 再强大 · 也不能直接感受温度
   必须经过 sensor (CFE 是 quantum 版 sensor)
   sensor 永远不可替代

   即使 FT QC 普及 · CFE 仍然不可替代 D3
```

### Slide 11 · 时间窗口

```
                      时间 →
   现在 ───────────────────────────────────►
   │
   │  FT QC 状态           CFE 状态
   │  ────────             ────────
   │  没成熟               专用方案 · 占 niche 黄金期
   │  早期 demo            仍唯一可行
   │  中期可用             D2/D3 仍优
   │  普及                 退守 D3 · 永久占有
   │
   ▼
   永远

   整条时间线 · CFE 不会被淘汰
   D3 永久独占
```

### Slide 12 · 减法计算范式 (SCP) · 米开朗基罗

```
   "I saw the angel in the marble and
    carved until I set him free."
                       — Michelangelo

   ────────────────────────────────

   传统范式 · 加法
   build / accumulate
   每个 op 都执行 · 都付钱

   新范式 · 减法
   sculpt / prune
   大部分 op 不执行 · 不付钱
   答案是 "剩下的"
```

### Slide 13 · 减法范式的杀手锏问题类

```
   K1 · Sparsity
        (10^9 候选里找一个 hit)

   K2 · Side Effects
        (测试触发对手 alert)

   K3 · Verify Without Commit
        (验 token 但不消耗)

   ────────────────────────────────

   全部都是:
   "查询有物理代价"
   而不是
   "查询复杂度高"
```

### Slide 14 · 算法模板 · CPA 例

```
   Counterfactual Pruning Algorithm

   输入:N 候选 · sparsity K << N

   step 1: 编 N 路 photonic IFM
   step 2: Φ_OR · "有 hit 吗?"
           如无 · 返回空集 (oracle 0 触发)
   step 3: Φ_COUNT · 多少 hit?
   step 4: Φ_LOC · 定位每个
   step 5: 对 K 个真测 (这步才付钱)

   总 cost: K (远小于 N)
   经典 cost: N

   加速比 = N/K  · 由 sparsity 决定
```

### Slide 15 · 现在到了密码学部分

```
              所以呢?

   这些都对算法学者好玩
   但密码学界凭什么 care?

           ↓
           
   下面 5 张 · 给密码学家
```

### Slide 16 · 工业密码学的"两道防线"

```
   工业部署密码学 · 几十年靠两道防线**并列**承重:


   第一道 · 数学算法安全
   ────────────────────
   • AES-256 数学难度
   • RSA-2048 factoring
   • SHA-256 collision
   • 由 NIST / IACR 认证


   第二道 · 硬件根信任
   ────────────────────
   • HSM tamper detection
   • Smart card 物理保护
   • TPM / Secure Enclave
   • 由 FIPS 140 / Common Criteria 认证


   工业假设:两道**都破**才算密码被破
```

### Slide 17 · CFE 单独击穿第二道

```
   CFE 的 R2 性质 · 直接攻击第二道:

   • R2 让 HSM tamper sensor 不触发
   • R3 让 HSM query quota 不消耗
   • R1 让 HSM 物理状态不被扰动

   ────────────────────────────────

   结果:
   ✗ 第二道防线**被绕过**
   ✗ 第一道防线**单独承重**
   
   第一道**从未被设计**成单独承重
   (例 AES-256 数学上 Grover 给 2^128 · FT QC 时不安全)
   工业靠 HSM 兜底 · 兜底失效
```

### Slide 18 · 17 算法系统化 audit

```
   File 给的 17 个工业部署算法:

   DES / 3DES / RC4 / IDEA / RC5 / Blowfish / AES /
   ChaCha20 / MD5 / SHA-1 / RSA / DH / EDH / ECC /
   AES-GCM / ChaCha20-Poly1305

   ────────────────────────────────

   数学层被破:    0 / 17
   HSM key 提取:  17 / 17  ✗

   即:数学完全完整 · 但工业部署 17 个全部 vulnerable
```

### Slide 19 · CFE-增强 Harvest Now Decrypt Later

```
   经典 HNDL:
   现在拦 traffic → 等 FT QC → Shor 破 → 解密
   
   缓解:迁 PQC · session key 不基于 RSA

   ────────────────────────────────

   CFE-增强 HNDL:
   现在提 HSM master key → 立即派生 session key → 立即解
   
   缓解:**没有** post-quantum 算法升级路径救
        (因为攻击不在数学层 · 在硬件层)

   ────────────────────────────────

         ↑ 这才是真威胁
```

### Slide 20 · Worked Example · AES-256 in HSM

```
   for i = 1..256:
     k_i = Φ_CF[read_bit_at(K_addr + i),
                δ=1e-9, ε=1e-3]
   
   累积检测概率 ≤ 256 × 10^-9 = 2.56 × 10^-7
   
   (远低于 HSM false-positive 阈值)
   
   ────────────────────────────────
   
   ✓ Key K 完整提取
   ✓ HSM tamper response 未触发
   ✓ Audit log 无 record
   ✓ HSM 继续正常工作
   ✓ 攻击者离线用 K 解密历史 + 未来 traffic
```

### Slide 21 · 银行 PIN 反事实暴力

```
   4-digit PIN · attempt counter 锁卡防御

   for P' in {0000, ..., 9999}:
     match = Φ_CF[verify_PIN(P'),
                  δ=1e-6, ε=1e-4]
     if match: return P'

   累积 attempt counter 触发概率 ≤ 10^4 × 10^-6 = 10^-2

   ────────────────────────────────

   ✓ PIN 100% 找到
   ✓ HSM 没锁卡
   ✓ 同样攻击对 SMS / TOTP 6-digit 适用
```

### Slide 22 · 硬件根信任的危机

```
   所有 root of trust **同时**失去 implicit guarantees:

   • HSM (enterprise crypto)
   • TPM (PC boot chain)
   • Secure Enclave (Apple)
   • TrustZone (ARM)
   • SGX (Intel)
   • Hardware wallet (crypto assets)
   • Smart card (banking / ID)

   ────────────────────────────────

   而且:**软件层无法补救**
   因为问题在 "root" 概念基础 · 不在 root 之上
```

### Slide 23 · 提议 · Post-Counterfactual Cryptography

```
              PCC = 新密码学子领域

   类比但**正交**于 Post-Quantum Cryptography (PQC)


   Threat              | PQC            | PCC
   ────────────────────┼────────────────┼────────────────
   攻击对象            | 数学结构       | 物理假设
   需要 FT QC          | 是             | 否 (今天)
   防御方向            | lattice/hash   | coherence/MPC
   时间线              | 等             | 现在


   论文 supplement 01:PCC 立项书
   邀请 8-12 人 founder pool
```

### Slide 24 · 5-point ask 给密码学社区

```
   1. 承认 CFE adversary model
      (跟 classical / quantum adversary 并列)

   2. 重审 HSM-based 安全证明
      (哪些假设 "tamper detection")

   3. PIN / 短密码体系重新设计
      (attempt counter 不能仅靠硬件)

   4. HNDL 防御策略升级
      (不只防 Shor · 也防 CFE-HSM-extraction)

   5. 标准化 PCC 子领域
      (类比 PQC 接受过程)
```

### Slide 25 · 论文是 RFC · 不是 manifesto

```
              本论文 = Request for Comments


   • 17 chapters · 3000+ 行 markdown · GitHub 公开
   • CC BY 4.0 license · 任何人可 fork / 改 / 引
   • 20 条具体声明 · 每条给证伪条件
   • 公开 review 通过 GitHub Issues / PR
   • 接受证伪 · next version 标注证伪者
   • 不闭门审稿


   "如果某 claim 错了 · 我们公开撤回"
                          — paper §13.6
```

### Slide 26 · 诚实划界

```
              CFE 不会做的事:


   ✗ 不破 RSA / AES / SHA 数学
   ✗ 不破 lattice / code / multivariate PQC 数学
   ✗ 不需要 FT QC 但需要专用 photonic 硬件
   ✗ 不绕过物理 access 要求
   ✗ 不替代量子计算 · 是 specialized co-processor
   ✗ 不会让 Internet 停止 (大部分 traffic 不受影响)


   只攻击:依赖 "probe 必检测" 假设的部分
   攻击深 · 但 scope 明确
```

### Slide 27 · 时间线提议

```
   Phase 1 · Seed       (依赖:论文 arxiv 投稿 + advisor pool)
                        本月

   Phase 2 · Establishment  (依赖:IACR workshop 申请通过)
                            未来 1-2 conference cycle

   Phase 3 · Standardization (依赖:NIST 设 PCC WG)
                              不依赖具体时间

   Phase 4 · Industrial deployment (依赖:第一个 PCC-cert HSM 上市)
                                    多年

   每 Phase 是 dependency · 不是日历
```

### Slide 28 · 加入

```
   How to engage:

   • Read     · paper/thinking-in-cfe/README.md
   • Verify   · supplements/10/ 跑 simulator (Python · 无硬件)
   • Challenge · GitHub Issues label `falsification`
   • Disclose · paper supplements 02-03 (HSM vendors)
   • Comment  · NIST PQC public comments (supplement 04)
   • Join PCC · supplement 01 founder pool 自荐


   [GitHub URL]
   [Contact email]
```

### Slide 29 · Final Thought

```
   "未来已被拉到当下 · 在 CFE 算子覆盖的 niche 内。
    剩下的只是工程工作。"

                        — Thinking in CFE, §14.10
   
   ────────────────────────────────
   
              Questions?
```

### Slide 30 · Backup · 算子复杂度细节

```
   D1 · Query        Q(f)²/δ
   D2 · Disturbance  δ
   D3 · Observability δ^N (cumulative)
   D4 · Hardware     ~6 orders cheaper than FT QC

   Pareto frontier:
   CFE 占据**别的算子族到不了的角**
   (低 D2 + 低 D3 + 中 D4 + 略高 D1)
```

## 演讲准备 checklist

- [ ] Slides 转 PDF / Keynote / PowerPoint (按会场 spec)
- [ ] Speaker notes 每张 slide 补关键讲点
- [ ] Backup slides 备好 (复杂度细节 / 物理实现 / 等)
- [ ] Demo video 备好 (simulator 跑通的录屏)
- [ ] Q&A 预演 · 准备 5-10 个 sharp question 回答
- [ ] 论文 + supplements 提前 GitHub 公开 · slide 引用直接给 URL
- [ ] Backup printout 准备 (会场设备故障兜底)

## 不同场合的版本调整

| 场合 | 重点调整 |
|---|---|
| IACR Crypto / Eurocrypt | §15-§16 + PCC 提议 · 弱化 §6 范式哲学 |
| QIP / quantum info | §3-§7 + §14 物理实现 · 弱化 §15-§16 密码学 |
| Black Hat / DEFCON | §15-§16 攻击 + worked examples · 弱化算子代数 |
| 量子位 / 国内 AI 会议 | 减法范式 + photonic 实物 · 弱化攻击 narrative |
| NIST workshop | §15-§16 + supplement 04 评论信 + PCC 提议 |
| 投资 pitch | §10 商业 niche + §14 时间窗口 · 弱化技术细节 |

## License

CC BY 4.0
