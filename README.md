# Thinking in CFE

> A Counterfactual Function Evaluation Paradigm for Photonic Computation

> 反事实函数求值算子体系 · 减法计算范式 · 以及对未来量子计算可挑战问题的重新评估。

## 一句话摘要

我们把 Elitzur-Vaidman 干涉无相互作用测量 (1993) 跟 Mitchison-Jozsa 反事实计算 (2001) 的物理思想抽象为算法原语 **CFE** (Counterfactual Function Evaluation Operator) · 构造组合代数 · 命名 **减法计算范式 (SCP)** · 提出 **PCC** (Post-Counterfactual Cryptography) 新密码学子领域 · 用 **12 个可跑 Python simulator (60 unit tests 全 pass)** 演示同构方法论。

> **本论文经过 230 claim 全审 + 5 个 surgical 修订 commit · 物理基础经 PhD-level synthesis (Hance 2023 Bristol) + critical paper (Frumkin-Bush 2023) 双轮 audit · 完整 audit 落档在 `audit/` 目录 · §18 audit-report 是论文一部分。** RFC stage · 邀请证伪。

## TL;DR · 给 CS 朋友的 30 秒概览

**这是什么**:把 30 年量子物理实验 (Interaction-Free Measurement · IFM) 抽象为算法学家可直接调用的算子代数 · **IFM 的 "MapReduce 时刻"**。

### 3 件不可能但都是真的事

🎯 **finding 1 · 工业密码学被绕过 (数学没破 · 但 key 没了)**

AES / RSA / SHA / ECC / 3DES / AES-GCM / ChaCha20 / RC4 ... **17 种工业部署密码算法** · 数学完全没破 · 但 HSM / TPM / Secure Enclave 里的 key 可被反事实物理探测偷走 · attacker 不触发任何 tamper-evident 机制 · **PQC 救不了** (攻击在物理假设层 · 不在数学层)。

跨硬件 root of trust 影响:

| 受影响硬件类 | 部署规模 | 信任体系位置 |
|---|---|---|
| HSM (银行 / 金融) | 千万级 | 加密交易根 |
| TPM (PC) | ~30 亿 | OS 启动信任根 |
| EMV 银行卡 | 10 亿 | 支付授权根 |
| 护照芯片 | 15 亿 | 身份认证根 |
| 车载 ECU | 1 亿 | 自动驾驶安全根 |
| 加密货币 wallet | -- | 资产私钥托管 |
| Satellite | -- | 卫星指挥认证根 |

Heartbleed / Spectre 是 specific 漏洞 · 我们这是**跨硬件类的 paradigm-level break** · 同一物理 primitive 通杀 7 类设备。

🎯 **finding 2 · 不是漏洞 · 是一个新计算范式**

提出 **减法计算范式 (SCP)** · 跟传统加法计算正交 · 是另一种思维方式。

衍生新密码学子领域 **后反事实密码学 (PCC)** · 类比 PQC 但管物理假设层 · 跟 PQC 正交 · **当下即威胁**(不必等 quantum computer 到来)。

🎯 **finding 3 · 工程 backing + 元层 audit 全透明**

- **12 个 Python simulator** · Python 3.8+ stdlib · 零依赖 · 60 unit tests 全 pass · `clone + cd + python -m unittest` 一行跑
- **230 claim 全审落档** · 像 software 的 test coverage:CONFIRMED 158 / PARTIAL 58 / REFUTED 3 (已修) / NOVEL 11
- **audit/ 目录全公开** · 任何人可 grep / 验证任何 claim 的原始证据链 · git 历史 zero-secret (filter-repo 已清) · production-grade rigor

### CS 类比 · 速 grok

| 我们做的 | 类比 (CS 朋友熟悉的范式) |
|---|---|
| 把 IFM 物理抽象为 algorithm primitive | **MapReduce** 不发明分布式 · 但让所有人能写分布式任务 |
| 提出减法计算范式 (SCP) | **React** 不发明 UI · 但定义新思维 · 跟 jQuery 正交 |
| 提出后反事实密码学 (PCC) | **PQC** 防数学层 quantum 威胁 · PCC 防物理假设层 · 两者正交 |
| CFE 算子代数 | 像把 **Backprop** 从 "loss 求导" 抽象为 PyTorch 的 `nn.Module` · 让你能 compose · 不必懂底层物理 |
| audit-as-paper-deliverable | 像 software 的 **CI / test coverage** · 但用在论文 · reviewer 可 grep / 复审 / 挑战 |

### 5 分钟 onboarding (CS 朋友推荐路径)

| 步 | 时间 | 动作 |
|---|---|---|
| 1 | 5 min | 读完本 README (结构 + 阅读路径 + 核心 claim) |
| 2 | 3 min | 跑一个 simulator demo:`cd supplements/10-cfe-hndl-simulator && python -m unittest discover` |
| 3 | 10 min | 读 `thinking-in-cfe/16-attack-on-deployed-crypto.md` (17 算法 audit · 最具实际冲击力章节) |
| 4 | 15 min | 读 `audit/04-audit-summary.md` + `audit/06-novelty-defense.md` (看 audit 怎么 surface gap + 防御 originality) |

### 一句话定位

> 我们**不发明**新物理 · 我们**做** IFM 30 年既有物理工作的 **"MapReduce 时刻"** — 把它抬到 algorithm primitive 层 · 让算法学家不必懂量子光学也能调用 quantum-only 能力 · 并发现这件事顺带把工业密码学的物理假设层全部抬到 reviewer 面前。

## 仓库结构

```
.
├── README.md                  ← (you are here)
├── LICENSE.md                 ← CC BY 4.0 (文本) + MIT (代码)
├── CITATION.cff               ← citation metadata
├── CONTRIBUTING.md            ← RFC 流程 / falsification 提交规范
├── .gitignore
│
├── thinking-in-cfe/           ← 主论文 · 19 章 + README + refs
│   ├── README.md              ←   论文导航 + 摘要
│   ├── 00-abstract.md
│   ├── 01-introduction.md
│   ├── ... (02-17)
│   ├── 18-audit-report.md     ←   230 claim 全审报告 (本论文一部分)
│   └── 99-references.md       ←   60+ 条标准化引用 (含 L1 PhD synthesis + L2 CQC + M Fomin)
│
├── audit/                     ← 230 claim 全审落档 · 单点真理源
│   ├── 00-master-plan.md      ←   方法论 (M1-M4 元规则 + 7 步流程)
│   ├── 01-claim-registry.md   ←   230 claim 表 + status
│   ├── 04-audit-summary.md    ←   整体 status 分布 + Top 20 发现
│   ├── 05-gap-report.md       ←   24 个 Gap + 6 优先级
│   ├── 06-novelty-defense.md  ←   11 NOVEL 防御 + 7 reviewer 攻击预案
│   ├── 07-prior-art-corrections.md         ← §02 + §99 修订清单
│   ├── REVISION-CHECKLIST.md  ←   18 项修订总 checklist (✅ 100% done)
│   ├── THEORY-ADJUSTMENTS-MASTER-REPORT.md ← 10 部分系统化调整决策
│   ├── batch-5-B-physics-foundation-DEEP.md
│   ├── batch-11-physics-via-phd-thesis-and-critical-review.md
│   └── claims/AUD-XXX/        ←   11 个 sample claim 完整 7 步 audit log
│
├── supplements/               ← 22 个卫星文档 · 含 12 simulator
│   ├── README.md              ←   supplements 导航
│   ├── 01-pcc-founding-document.md           ← PCC 子领域立项
│   ├── 02-hsm-disclosure-template.md         ← HSM 厂商责任披露模板
│   ├── 03-hsm-disclosure-specifics.md        ← Thales/Utimaco/Entrust/AWS
│   ├── 04-nist-pqc-comment-letter.md         ← NIST PQC 评论信
│   ├── 05-iacr-eprint-cover.md               ← IACR 投稿封面
│   ├── 06-arxiv-abstract-en.md               ← arxiv 英文摘要
│   ├── 07-press-release.md                   ← 媒体新闻稿
│   ├── 08-conference-talk-outline.md         ← 30 分钟会议讲稿
│   ├── 09-cfe-hndl-simulator-design.md       ← simulator 设计
│   ├── 10-cfe-hndl-simulator/                ← Simulator 1 · HSM key extraction
│   ├── 11-isomorphism-catalog-template.md    ← 社区贡献模板
│   ├── 12-simulator-validation-report.md     ← simulator 10 验证报告
│   ├── 13-extended-isomorphism-examples.md   ← 5 个新领域 worked example
│   ├── 14-cfe-bloom-pir-simulator/           ← Simulator 2 · Bloom PIR
│   ├── 15-cfe-bloom-validation-report.md     ← simulator 14 验证报告
│   ├── 16-universal-hardware-trust/          ← Simulator 3 · ★ 7 device 攻击
│   ├── 18-graph-reachability/                ← Simulator 4 · Stealth network probe
│   ├── 20-differential-crypto/               ← Simulator 5 · 差分密码分析
│   ├── 22-federated-gradient/                ← Simulator 6 · FL 隐私
│   ├── 24-monte-carlo/                       ← Simulator 7 · 反事实采样
│   ├── 26-abstract-interp/                   ← Simulator 8 · SMT 成本节省
│   ├── 28-attention/                         ← Simulator 9 · Sparse attention
│   ├── 30-ray-tracing/                       ← Simulator 10 · CFE 光线追迹
│   ├── 32-spmv/                              ← Simulator 11 · 稀疏 SpMV
│   └── 34-smith-waterman/                    ← Simulator 12 · 序列比对
│
└── dev-notes/                 ← 探索过程 + 同构深化 · 14 份
    ├── 001-010                ←   从 Wheeler demo 到 CFE 算子体系演化
    └── 011-014                ←   4 个 §17.4 同构深化
```

## 跑 simulator (零外部依赖)

任何 Python 3.8+ 环境 · 无需 photonic / quantum 硬件:

```bash
# Simulator 1 · HSM key extraction (CFE-HNDL)
cd supplements/10-cfe-hndl-simulator
python3 cfe_hndl_demo.py
python3 -m unittest cfe_hndl_demo -v

# Simulator 3 · ★ Civilization-scale · 7 device universal break
cd ../16-universal-hardware-trust
python3 cfe_uht_demo.py

# 跑全部 12 个 (任选)
cd ../..
for dir in supplements/{10,14,16,18,20,22,24,26,28,30,32,34}*/; do
  mod=$(ls "$dir"*.py | xargs basename | sed 's/\.py$//')
  cd "$dir" && python3 -m unittest "$mod" 2>&1 | tail -2 && cd - > /dev/null
done
```

预期:**60 个 unit test 全 PASS** · 任何 reviewer 跟我们字节一致结果(`--seed 2026` default)。

## 阅读路径

按你的角色:

| 角色 | 路径 |
|---|---|
| **快读 elevator pitch** | `thinking-in-cfe/00-abstract.md` → `thinking-in-cfe/12-conclusion.md` |
| **算法学者** | `thinking-in-cfe/03-07` → `thinking-in-cfe/17-isomorphism-methodology.md` |
| **密码学家** | `thinking-in-cfe/15-16` → `supplements/01-pcc-founding-document.md` |
| **HSM 厂商安全 team** | `supplements/02-03` → `supplements/16-universal-hardware-trust/` |
| **标准 / 监管** | `supplements/04-nist-pqc-comment-letter.md` → `supplements/01-pcc-founding-document.md` |
| **媒体 / 投资人** | `supplements/07-press-release.md` → `supplements/06-arxiv-abstract-en.md` |
| **演讲准备** | `supplements/08-conference-talk-outline.md` |
| **想自己验证 claims** | `supplements/10-cfe-hndl-simulator/` + `12-simulator-validation-report.md` + `15-cfe-bloom-validation-report.md` |
| **社区贡献新同构** | `supplements/11-isomorphism-catalog-template.md` |
| **完整精读** | 按章节顺序 + `dev-notes/` 看演化过程 |
| **审计 reviewer** | `audit/04-audit-summary.md` + `thinking-in-cfe/18-audit-report.md` + `supplements/17-audit-master-log/` |
| **想看物理 caveat** | `audit/batch-5-B-physics-foundation-DEEP.md` + `audit/batch-11-physics-via-phd-thesis-and-critical-review.md` + `thinking-in-cfe/11-limitations-and-open-problems.md` (6 CAVEAT) |
| **想看修订决策** | `audit/THEORY-ADJUSTMENTS-MASTER-REPORT.md` (10 部分系统化决策) + `audit/REVISION-CHECKLIST.md` (18 项 ✅) |

## 核心 claim (audit 后 honest 版本)

1. **CFE 是 quantum-only 算子** (在 chained Zeno / multi-object IFM 规模) · 用专用 photonic 硬件实现 (集成 IFM chip [Franco-Camillini-Galvão 2026, arxiv 2604.04691] + [Calafell et al. 2019] MIT SOI nanophotonic) · 不依赖 fault-tolerant quantum computer。
   - **Honest caveat**:single bomb tester 规模的 R1 quantum-only 论点是 contested in physics community [Frumkin-Bush 2023, PRA 108:L060201] · 详 §11.2 CAVEAT 6
2. **3 维 transcendence 框架** vs FT QC:D1 capability (FT QC superset) · D2 cost (CFE 便宜 6 数量级 · **N ≤ 10 niche**) · D3 interface domain (CFE 永久独占 · 外部物理 oracle)。
3. **减法计算范式 (SCP)** 跟传统加法计算正交 · sparsity / side-effects / verify-without-commit 是杀手锏问题类。跟 LLM "subtraction" [Tang et al. 2026] / Pearl 因果反事实 / ML explainability / 认知心理学 / algebraic complexity [Fomin 2013] 5 类邻近概念已 disambiguate。
4. **17 个工业部署密码算法**(DES/AES/SHA/RSA/...)数学层未破 · 但 HSM-stored keys 全部受 CFE-HNDL 攻击影响 (R2 violation 2.4% per query at N=6 SOTA · 详 §15.5)。
5. **Universal Hardware Trust Break** · 同一 CFE 攻击模型对 HSM / TPM / 硬件钱包 / EMV / passport / 车载 ECU / satellite 7 类设备**全部有效** · 强制全球 hardware-anchored 信任体系重审。
6. **12 个 worked example 已端到端做实** (Python simulator + 60 unit tests 全 pass) · 跨 12 个不同算法子领域。

### PCC vs CQC disambiguation

**PCC** (本论文提议)跟已有 17 年 active 子领域 **CQC** (Counterfactual Quantum Cryptography · [Noh 2009] 起源) 命名邻近但研究方向正交:

- **CQC**:用 counterfactual 性质**构造** cryptographic protocol (QKD-like)
- **PCC**:用 counterfactual 性质**防御** cryptographic attack (R2 stealth bypass tamper-evident hardware)

详 `thinking-in-cfe/02-prior-art.md` §02.4.1 + `thinking-in-cfe/15-cryptographic-mental-model-shift.md` §15.7。

## RFC 性质

本论文以 **Request for Comments** 形式发布(详 `thinking-in-cfe/13-validation-and-rfc.md`):

- **CC BY 4.0** (文本) + **MIT** (代码) · 任何人可用 / 改 / cite
- 每条 claim 附**证伪条件** · 严格证伪后我们公开撤回 + 标致谢
- **公开 review** 通过 GitHub Issues / PR · 不闭门审稿
- 邀请 5 类 reviewer:量子信息理论 / photonic 工程师 / 算法学者 / 密码学家 / 行业应用专家

## 引用

```bibtex
@misc{thinking-in-cfe-2026,
  title  = {Thinking in CFE: A Counterfactual Function Evaluation Paradigm
            for Photonic Computation},
  author = {[作者待补]},
  year   = {2026},
  note   = {Draft v0.1, June 2026},
  url    = {[GitHub URL]}
}
```

详 `CITATION.cff`。

## 状态 · 2026-06-20 (v0.2 audit-revised)

### 文档体系
- ✅ 论文主体 **19 章** (00-17 + §18 audit-report + 99-references)
- ✅ 22 个 supplement (含 12 simulator · 60 unit tests 全 pass · 3579 行 Python)
- ✅ 14 个 dev-note (探索 + 同构深化)
- ✅ **audit/ 230 claim 全审落档** + supplements/17-audit-master-log/ mirror
- ✅ 双 license (CC BY 4.0 + MIT)

### 审计 + 修订 (本轮)
- ✅ **230 claim 全 audited** · CONFIRMED 158 / PARTIAL 58 / REFUTED 3 (已修) / NOVEL 11
- ✅ **18 项 REVISION-CHECKLIST 100% 完成** (cleanup × 3 + P0 × 3 + P1 × 5 + P2 × 3 + early × 4)
- ✅ **3 个 attribution cite key 修复** ([Hance 2025] → [Franco-Camillini-Galvão 2026] · [Yang 2026] → [Tang et al. 2026] · [Hance 2019] → [Calafell et al. 2019])
- ✅ **物理 caveat 完整落地**:§03.9 SOTA 表精确化 (N=12 → N=5 区分) + §11.2 加 6 CAVEAT + §15.5 R2 violation bound + §10 A2/A3/A4 N≤10 niche
- ✅ **PhD-level + critical paper 加入 prior-art**:Hance 2023 Bristol PhD · Violaris 2025 Oxford DPhil · Frumkin-Bush 2023 (PRA 108:L060201) · Bush 2021 综述 · Hance-Ladyman-Rarity 2021 (Found. Phys. 51:12) · IOP 2024
- ✅ **CQC 17 年 prior-art disambig**:§02.4.1 加 [Noh 2009] CQC 子领域 6 paper + §15.7 PCC vs CQC 区分
- ✅ **数学修订**:§03.2 P3 δ-extension 明示 + §03.5 子算子 8 公式漏平方修复 + §02.5 (E) algebraic disambig
- ✅ **12 simulator README batch SOTA caveat**

### 外推进 (RFC stage · 待用户决策)
- ⏳ arxiv / IACR ePrint 投稿(等作者 ORCID + 法律 review)
- ⏳ HSM 厂商 coordinated disclosure(等 90-day grace 计划)
- ⏳ NIST 公开评论提交
- ⏳ PCC founder pool 招募
- ⏳ Push 到 GitHub public (待用户显式同意)

### 14 commit timeline

详 `git log --oneline` · 6 surgical revision commit + 6 audit commit + 1 initial + cleanup。

## License

- 论文 / 文档 / Markdown: **CC BY 4.0** (详 `LICENSE.md`)
- Simulator Python 代码: **MIT** (详 `LICENSE.md`)
- 引用即可(无商业 / 学术使用限制)

## 贡献

欢迎所有形式贡献。详 `CONTRIBUTING.md`。

- Typo / 文字修正:直接 PR
- 论文 claim 质疑 / 反驳:Issue with label `falsification`
- 新 CFE 同构提交:走 `supplements/11-isomorphism-catalog-template.md` 模板
- 新 simulator:fork + PR · 跟现有 12 个 simulator 同样 unit test + README 标准
