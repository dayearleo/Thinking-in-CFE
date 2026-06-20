# Thinking in CFE

> 一个反事实函数求值算子体系 · 减法计算范式 · 以及对未来量子计算可挑战问题的重新评估

## 摘要

我们提出 **反事实函数求值算子** $\Phi^{CF}_f$ (Counterfactual Function Evaluation Operator · 简称 **CFE**),把 Elitzur-Vaidman 干涉无相互作用测量 (IFM, 1993) 与 Mitchison-Jozsa 反事实计算 (2001) 的物理思想抽象为可工程化的算法原语,并在此基础上构造算子代数,提出 **减法计算范式** (Subtractive Computation Paradigm),给出 6 个算法模板与 5 步问题代数化方法论。我们论证 CFE 算子在 3 个独立维度上 (D1 capability · D2 cost · D3 interface domain) 跟未来 fault-tolerant 量子计算 (FT QC) 的关系,识别出 FT QC 永远到不了的 D3 范畴 —— 外部物理 oracle 的反事实查询能力 —— 并指出 6 个原本被认为需要 FT QC 才能解决的问题,我们当下用 photonic IFM 硬件即可挑战。诚实地,我们排除 5 类不可挑战的问题 (Shor / 大尺度量子化学 / HHL 等)。本文是工程-理论-应用三层综述,不预设读者具备量子光学背景。

## 如何阅读

本文按 GitHub-friendly 方式**分片为 15 个文件**,每个文件聚焦一个主题,独立可读。建议按以下路径:

| 路径 | 章节 | 适合谁 |
|---|---|---|
| **快读 elevator pitch** | `00-abstract.md` → `12-conclusion.md` | 决策者 / VC |
| **理解算子是什么** | `00` → `01` → `02` → `03` → `04` | 算法学家 / 量子物理学家 |
| **理解为什么超越 FT QC** | `00` → `01` → `05` | 战略 / 学术合作伙伴 |
| **理解减法计算范式** | `00` → `06` → `07` | 计算机科学家 / 教育者 |
| **应用领域如何切入** | `00` → `08` → `09` → `10` | 工程师 / 行业专家 |
| **完整精读** | 按编号顺序读 `00-12` · 再查 `99-references.md` | 论文审稿人 / 研究生 |

## 目录

- [`00-abstract.md`](00-abstract.md) · 摘要
- [`01-introduction.md`](01-introduction.md) · 引言 · 起源与论文贡献
- [`02-prior-art.md`](02-prior-art.md) · 先行研究 · 30 年回顾与差异化定位
- [`03-operator-formal-definition.md`](03-operator-formal-definition.md) · CFE 算子的形式定义
- [`04-composition-algebra.md`](04-composition-algebra.md) · 算子组合代数
- [`05-three-dim-transcendence.md`](05-three-dim-transcendence.md) · 跟 FT QC 的 3 维比较
- [`06-subtractive-paradigm.md`](06-subtractive-paradigm.md) · 减法计算范式
- [`07-complexity-analysis.md`](07-complexity-analysis.md) · 多维复杂度分析
- [`08-algorithm-templates.md`](08-algorithm-templates.md) · 6 个算法模板
- [`09-problem-algebraization.md`](09-problem-algebraization.md) · 问题代数化方法论
- [`10-six-challengeable-problems.md`](10-six-challengeable-problems.md) · 6 个可立即挑战的 FT QC 问题
- [`11-limitations-and-open-problems.md`](11-limitations-and-open-problems.md) · 诚实限界与开放问题
- [`12-conclusion.md`](12-conclusion.md) · 结论
- [`13-validation-and-rfc.md`](13-validation-and-rfc.md) · 现实性验证维度 · Request for Comments
- [`14-breakthrough-demonstration.md`](14-breakthrough-demonstration.md) · 量子计算解法的突破 · 把未来拉近到当下 (3 个 worked example)
- [`15-cryptographic-mental-model-shift.md`](15-cryptographic-mental-model-shift.md) · 密码学认知突破 · 在 FT QC 到来之前 (R2 攻击 4 层物理假设 + 3 个 worked attack + Post-Counterfactual Cryptography)
- [`16-attack-on-deployed-crypto.md`](16-attack-on-deployed-crypto.md) · CFE 对 17 个工业部署密码算法的系统化攻击 (DES/3DES/RC4/IDEA/RC5/Blowfish/AES/ChaCha20/MD5/SHA-1/RSA/DH/EDH/ECC/AES-GCM/ChaCha20-Poly1305 + 3 worked attack + 硬件根信任危机)
- [`17-isomorphism-methodology.md`](17-isomorphism-methodology.md) · CFE 算子同构方法论 · 5 步发现 SOP · 4 个跨域 worked example (Bloom→PIR / 可达性→Stealth probe / 差分→Rate-limit bypass / Backprop→Federated) · 历史算法宝库的元层视角 · 4 级 specialization L0-L3 · CFE 算子家族目录 vision
- [`18-audit-report.md`](18-audit-report.md) · 审计报告 · 230 条声明的现实性证明 · 11 个 sample 7 步审 + 219 个 batch reasoned 审 · 整体 68.7% CONFIRMED · 25.2% PARTIAL · 1.3% REFUTED (已修) · 4.8% NOVEL · 跟 `audit/` 目录对接
- [`99-references.md`](99-references.md) · 参考文献

## 引用本工作

```bibtex
@misc{thinking-in-cfe-2026,
  title  = {Thinking in CFE: A Counterfactual Function Evaluation Paradigm for Photonic Computation},
  author = {[作者待补]},
  year   = {2026},
  note   = {Draft v1, June 2026}
}
```

## 版本

- **v0.1** · 2026-06-19 · 初稿 · 15 篇章节 · 中文 · 待英译

## 关联工作 (项目内部 dev-notes)

本论文是项目 `dev-notes/001-010` 系列探索的综合成果。dev-notes 提供更详细的演化过程 + 决策记录,本论文是结晶后的对外稿。

- `dev-notes/004` · 算子定义 (本文 §3 详版)
- `dev-notes/005` · 3 维超越点 (本文 §5 详版)
- `dev-notes/006` · 组合代数 (本文 §4 详版)
- `dev-notes/007` · 减法范式 (本文 §6 详版)
- `dev-notes/008` · 算法模板 (本文 §8 详版)
- `dev-notes/009` · 代数化方法论 (本文 §9 详版)
- `dev-notes/010` · 可挑战问题清单 (本文 §10 详版)
