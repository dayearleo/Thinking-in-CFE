# Thinking in CFE

> A Counterfactual Function Evaluation Paradigm for Photonic Computation

> 反事实函数求值算子体系 · 减法计算范式 · 以及对未来量子计算可挑战问题的重新评估。

## 一句话摘要

我们把 Elitzur-Vaidman 干涉无相互作用测量 (1993) 跟 Mitchison-Jozsa 反事实计算 (2001) 的物理思想抽象为算法原语 **CFE** (Counterfactual Function Evaluation Operator) · 构造组合代数 · 命名 **减法计算范式 (SCP)** · 提出 **PCC** (Post-Counterfactual Cryptography) 新密码学子领域 · 用 **12 个可跑 Python simulator (60 unit tests 全 pass)** 演示同构方法论。

## 仓库结构

```
.
├── README.md                  ← (you are here)
├── LICENSE.md                 ← CC BY 4.0 (文本) + MIT (代码)
├── CITATION.cff               ← citation metadata
├── CONTRIBUTING.md            ← RFC 流程 / falsification 提交规范
├── .gitignore
│
├── thinking-in-cfe/           ← 主论文 · 17 章 · 4166 行
│   ├── README.md              ←   论文导航 + 摘要
│   ├── 00-abstract.md
│   ├── 01-introduction.md
│   ├── ... (02-17)
│   └── 99-references.md       ←   50+ 条标准化引用
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

## 核心 claim

1. **CFE 是 quantum-only 算子** · 但用专用 photonic 硬件 (集成 IFM chip, [Hance 2025]) 实现 · 不依赖 fault-tolerant quantum computer。
2. **3 维 transcendence 框架** vs FT QC:D1 capability (FT QC superset) · D2 cost (CFE 便宜 6 数量级) · D3 interface domain (CFE 永久独占 · 外部物理 oracle)。
3. **减法计算范式 (SCP)** 跟传统加法计算正交 · sparsity / side-effects / verify-without-commit 是杀手锏问题类。
4. **17 个工业部署密码算法**(DES/AES/SHA/RSA/...)数学层未破 · 但 HSM-stored keys 全部受 CFE-HNDL 攻击影响。
5. **Universal Hardware Trust Break** · 同一 CFE 攻击模型对 HSM / TPM / 硬件钱包 / EMV / passport / 车载 ECU / satellite 7 类设备**全部有效** · 强制全球 hardware-anchored 信任体系重审。
6. **12 个 worked example 已端到端做实** (Python simulator + unit tests) · 跨 12 个不同算法子领域。

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

## 状态 · 2026-06-20

- ✅ 论文主体 17 章 · 4166 行
- ✅ 22 个 supplement (含 12 simulator)
- ✅ 14 个 dev-note (探索 + 同构深化)
- ✅ 60 unit tests 全 pass · 3579 行 Python
- ✅ 双 license (CC BY 4.0 + MIT)
- ⏳ arxiv / IACR ePrint 投稿(等作者 ORCID + 法律 review)
- ⏳ HSM 厂商 coordinated disclosure(等 90-day grace 计划)
- ⏳ NIST 公开评论提交
- ⏳ PCC founder pool 招募

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
