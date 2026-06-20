# Supplements · 论文卫星文档

[← 返回 paper root](../) · [← thinking-in-cfe 主论文](../thinking-in-cfe/)

本目录是 `thinking-in-cfe/` 主论文的卫星文档 · 用于论文的**对外推进**:学术立项 / 行业披露 / 标准评论 / 媒体沟通 / simulator demo / 投稿封面 等。

每个文件独立可读 · 跟主论文 cross-link · 适合不同读者**单独取**。

## 目录

| 文件 | 用途 | 受众 |
|---|---|---|
| [`01-pcc-founding-document.md`](01-pcc-founding-document.md) | Post-Counterfactual Cryptography (PCC) 子领域立项书 | 密码学学者 / IACR · 学术 community |
| [`02-hsm-disclosure-template.md`](02-hsm-disclosure-template.md) | 责任披露信通用模板 | HSM 厂商 security teams |
| [`03-hsm-disclosure-specifics.md`](03-hsm-disclosure-specifics.md) | Thales / Utimaco / Entrust / AWS CloudHSM 4 个具体案例 | 同上 |
| [`04-nist-pqc-comment-letter.md`](04-nist-pqc-comment-letter.md) | 给 NIST PQC standardization 的公开评论信 | NIST / 后量子标准制定者 |
| [`05-iacr-eprint-cover.md`](05-iacr-eprint-cover.md) | IACR ePrint 投稿封面 | IACR ePrint 编辑 / 审稿人 |
| [`06-arxiv-abstract-en.md`](06-arxiv-abstract-en.md) | arxiv 英文摘要 + 关键字 + 分类 | arxiv 投稿 |
| [`07-press-release.md`](07-press-release.md) | 技术新闻稿 | 技术媒体 / 行业分析师 |
| [`08-conference-talk-outline.md`](08-conference-talk-outline.md) | 30 分钟会议讲稿大纲 + slide 草案 | 学术 / 工业 conference 演讲准备 |
| [`09-cfe-hndl-simulator-design.md`](09-cfe-hndl-simulator-design.md) | CFE-HNDL simulator 设计文档 | reviewers · 想自己跑 demo 的人 |
| [`10-cfe-hndl-simulator/`](10-cfe-hndl-simulator/) | 实际可跑 Python simulator | hands-on engineers |
| [`11-isomorphism-catalog-template.md`](11-isomorphism-catalog-template.md) | 社区贡献 CFE 同构提交模板 (10 sections + 5-step process) | 算法学者 / 工程师想贡献新同构 |
| [`12-simulator-validation-report.md`](12-simulator-validation-report.md) | Simulator 实测输出报告 + 复现指南 (7 unit test + 1000 trial 统计) | reviewers · 想验证 paper claim 的人 |
| [`13-extended-isomorphism-examples.md`](13-extended-isomorphism-examples.md) | §17.4 扩展 · 5 个新领域 worked example (compiler / NLP / graphics / numerical / bioinfo) | 算法学者 · 跨学科应用专家 |
| [`14-cfe-bloom-pir-simulator/`](14-cfe-bloom-pir-simulator/) | **第 2 个做实** · CFE Bloom Filter → Stealth Lookup · 9 unit test pass · PIR comparison | hands-on engineers · reviewers |
| [`15-cfe-bloom-validation-report.md`](15-cfe-bloom-validation-report.md) | Bloom simulator 实测输出报告 · 跟 FHE-PIR / multi-server PIR 4 维诚实对比 | reviewers · PIR researchers |
| [`16-universal-hardware-trust/`](16-universal-hardware-trust/) | **第 3 个做实 · civilization-scale** · ONE CFE 攻击 · 7 device 全攻陷 (HSM/TPM/wallet/smartcard/passport/ECU/satellite) · 5 unit test | 标准制定 / 政策 / 投资 |
| [`18-graph-reachability/`](18-graph-reachability/) | **第 4 个做实** · Graph Reachability → Stealth Network Probe · 4 unit test · 490x detection reduction | 安全研究 / 军用情报 |
| [`20-differential-crypto/`](20-differential-crypto/) | **第 5 个做实** · Differential Cryptanalysis → Rate-Limit Bypass · 真 8-round Feistel cipher · 6 unit test | 密码分析 / 密码学社区 |
| [`22-federated-gradient/`](22-federated-gradient/) | **第 6 个做实** · Backprop → CFE Federated Gradient · 3 mode accuracy 完全一致 · ~5000x privacy gain · 5 unit test | ML / FL researchers |
| [`24-monte-carlo/`](24-monte-carlo/) | **第 7 个做实** · Monte Carlo → Counterfactual Sampling · 30x expensive eval reduction · 3 unit test | 数值方法 / HPC / materials |
| [`26-abstract-interp/`](26-abstract-interp/) | **第 8 个做实** · Abstract Interpretation → SMT cost saving · cloud Z3-as-a-Service · 6 unit test | 编译器 / 形式验证 |
| [`28-attention/`](28-attention/) | **第 9 个做实** · Transformer Attention → CFE Sparse · 100M token context · 4 unit test | NLP / LLM 工程师 |
| [`30-ray-tracing/`](30-ray-tracing/) | **第 10 个做实** · Ray Tracing → CFE bbox 预筛 · 8K HDR rendering · 3 unit test | 图形学 / GPU 工程 |
| [`32-spmv/`](32-spmv/) | **第 11 个做实** · Sparse SpMV → CFE row screen · bit-identical 输出 · 4 unit test | HPC / 数值线性代数 |
| [`34-smith-waterman/`](34-smith-waterman/) | **第 12 个做实** · Smith-Waterman → CFE k-mer 预筛 · cancer genomics · 4 unit test | 生物信息学 / 基因测序 |

## 推荐阅读路径

按你的角色:

- **学术研究者** · 01 → 04 → 05 → 06
- **HSM 厂商 security team** · 02 → 03 → 10 (跑 simulator)
- **标准制定 / 监管** · 04 → 01 → 07
- **媒体 / 投资人 / 行业分析师** · 07 → 06 → 08
- **想自己验证的工程师** · 09 → 10 (跑 simulator) → 论文 §13 + §16
- **会议 / 教学准备** · 08

## 跟主论文的关系

每个 supplement 都引用主论文的具体章节。具体引用 map:

| Supplement | 引用主论文章节 |
|---|---|
| 01 PCC 立项 | §15.7 (防御方向) · §15.9 (给密码学界建议) · §16.11 (5-point ask) |
| 02 / 03 HSM 披露 | §15.4.1 (HSM tamper-bypass) · §16.6.1 (AES-256 提取) · §16.7 (CFE-HNDL) |
| 04 NIST 评论 | §15 · §16 全章 |
| 05 IACR 封面 | 论文全文 |
| 06 arxiv 英文 | §00 摘要 |
| 07 press release | §00 + §14 + §16 |
| 08 talk outline | 论文全文 (压缩) |
| 09 / 10 simulator | §16.6 · §16.7 |
