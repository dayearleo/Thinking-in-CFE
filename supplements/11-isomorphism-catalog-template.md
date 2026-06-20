# 11 · CFE 同构提交模板 · 社区贡献规范

[← supplements README](README.md)

## 文件性质

**社区 RFC 提交模板** · 让任何研究者 / 工程师把自己发现的 CFE-同构算法按统一格式提交 · 形成可累积的 **CFE 算子家族目录** (论文 §17.7 vision)。类比:

- LLVM RFC 提交模板
- Python PEP 提案模板
- IETF Internet-Draft 模板

每个被接受的 catalog entry 都成为 CFE 算子家族目录的一员 · 给社区 cite。

## 当 catalog 长起来后的样子 (vision)

```
CFE 算子家族目录 · v1.0
├── 基础算子 (§3.5)
│   ├── Φ_OR / Φ_AND / Φ_NOR
│   ├── Φ_MAJ / Φ_COUNT / Φ_T_t
│   ├── Φ_LOC / Φ_NAND-tree
│   └── ...
├── 数据库类同构
│   ├── Φ_BloomLookup (本论文 §17.4.1)
│   ├── Φ_SkipList [社区贡献者 X]
│   ├── Φ_InvertedIndex [社区贡献者 Y]
│   └── ...
├── 图算法类同构
│   ├── Φ_Reachable (本论文 §17.4.2)
│   ├── Φ_ShortestPath [...]
│   ├── Φ_GraphColoring [...]
│   └── ...
├── 密码学类同构
│   ├── Φ_Differential (本论文 §17.4.3)
│   ├── Φ_Linear [...]
│   └── ...
├── ML 类同构
│   ├── Φ_Gradient (本论文 §17.4.4)
│   ├── Φ_KernelEval [...]
│   ├── Φ_Attention [...]
│   └── ...
└── 数值方法类同构
    ├── Φ_MonteCarloIntegrate (本论文 §17.4.5)
    ├── Φ_NewtonRoot [...]
    └── ...
```

每个 entry 引用一份完整提交文档 · 走本模板。

## 提交模板 (复制粘贴 · 改 [TBD] 字段)

```markdown
# CFE-Isomorphism Submission · [Algorithm Name]

## Submission Metadata

- **Title**: [Φ_XXX · Classical algorithm name 的 CFE 同构]
- **Authors**: [Name 1, Name 2, ...]
- **Submission Date**: [YYYY-MM-DD]
- **Catalog Category**: [database / graph / crypto / ML / numerical / signal /
  compiler / other]
- **Status**: [draft / accepted / superseded / withdrawn]
- **Version**: [1.0 / 1.1 / ...]
- **License**: [CC BY 4.0 · default]
- **Builds on**: [reference to prior CFE-isomorphism entries if any]

## 1 · Classical Algorithm Reference

The classical / quantum algorithm we propose to isomorphize:

- **Original publication**: [author, year, venue]
- **Algorithm name and brief description**: [...]
- **Asymptotic complexity (classical)**: [O(...)]
- **Asymptotic complexity (quantum SOTA)**: [O(...), reference]
- **Why it matters / common use cases**: [...]

## 2 · Identified CFE Isomorphism

### 2.1 · Core Primitive Operation

The classical algorithm's central primitive that maps to CFE form:

> [描述 primitive · 例 "k 个 hash 查表 AND" / "图边 reachability OR" / etc.]

### 2.2 · CFE Form

The primitive expressed as Φ^{CF}_f:

```
Φ_[Name]([inputs]) = Φ_[base_op](
  [oracle_1, oracle_2, ..., oracle_N],
  δ=[...],
  ε=[...]
)
```

### 2.3 · Why This Counts as Isomorphism

[解释 classical algorithm 跟 CFE form 在语义上等价的论证]

## 3 · Complexity Comparison (4-dim per §7)

| 维度 | Classical | Quantum SOTA | CFE Isomorphism |
|---|---|---|---|
| $D_1$ Query | [...] | [...] | [...] |
| $D_2$ Disturbance | [...] | [...] | [...] |
| $D_3$ Observability | [...] | [...] | [...] |
| $D_4$ Hardware | [...] | [...] | [...] |

### 净评估

- 抽象复杂度 net win/lose: [...]
- Photonic 物理速度补偿: [...]
- R2/R3 性质带来的不可替代价值: [...]

## 4 · Killer Use Case (Niche)

The application niche where this isomorphism is net-superior:

- **Domain**: [...]
- **Why classical / quantum SOTA insufficient**: [...]
- **Why CFE isomorphism wins**: [...]
- **Estimated market / impact**: [...]

## 5 · Physical Implementation Path

### 5.1 · Hardware Requirements (Level)

[L0 / L1 / L2 / L3 per §17.6 framework]

### 5.2 · Components

- Photonic platform: [Si / SiN / LiNbO3 / FSLW / 其他]
- N mode count: [...]
- δ achievable: [...]
- 估算单 chip cost: [...]
- 关键工程难点: [...]

### 5.3 · Existing Hardware That Could Run This

[reference to nearest existing photonic chip, if any]

## 6 · Validation Plan

### 6.1 · Simulator (mandatory before catalog acceptance)

- Repository: [GitHub URL]
- Language: [Python / Rust / other]
- Reproducibility: [seed, expected output]

### 6.2 · Lab Demonstration (optional but encouraged)

- Hardware needed: [...]
- Estimated complexity (low / medium / high):
- Existing lab(s) likely able to do it:

## 7 · Falsification Conditions (per §13 RFC framework)

This submission can be falsified by:

- [Condition 1]
- [Condition 2]
- [Condition 3]

If falsified, the authors commit to public withdrawal.

## 8 · Related Work

### 8.1 · Other CFE-isomorphism entries this builds on

[references to prior catalog entries]

### 8.2 · Other CFE-isomorphism entries this competes with / replaces

[references to entries that this supersedes, if any]

### 8.3 · Non-CFE related work

[references to classical / quantum literature on same problem]

## 9 · License

CC BY 4.0 (default for catalog entries)

## 10 · Submission Checklist

- [ ] Algorithm reference complete (author + year + venue + arxiv/DOI)
- [ ] CFE form mathematically explicit
- [ ] 4-dim complexity table filled
- [ ] Killer use case identified
- [ ] Hardware path Level (L0-L3) specified
- [ ] Working simulator submitted (or pointer to one)
- [ ] Falsification conditions specified
- [ ] Related work cited (3+ classical, 1+ quantum if exists)
- [ ] License compatible (CC BY 4.0 / MIT)
```

## 提交流程

### 1 · Pre-submission

- 跑 §17.3 的 5 步 SOP · 自验证是否值得提交
- 至少跑一个 simulator · 不要 nuked 等 reviewer 跑
- Pre-print 提交 IACR ePrint / arxiv (可选 · 不强制)

### 2 · Submission

- Fork 主 paper GitHub repo
- 在 `catalog/[category]/[Phi_Name].md` 路径填本模板
- 提 PR · label `catalog-submission`
- 等 maintainer + community review

### 3 · Review Process

- 至少 2 个 independent reviewers (algorithm 专家 + photonic 工程师 各一)
- Review 期间 maintainer 公开讨论 · 不闭门
- 接受 / 拒绝 / require revision 三种结果

### 4 · Post-acceptance

- 进 catalog · 给 catalog ID (CFE-iso-NNNN)
- 加 CITATION.cff · 单独 citable
- 列入 paper README + catalog 索引

### 5 · Maintenance

- Catalog entries 支持 versioning
- 被 falsify 时 maintainer 公开 mark superseded
- 定期 audit 整个 catalog (年级)

## 跟主论文的关系

- 主 paper §17 提供 methodology
- 本 supplement (11) 提供提交规范
- 未来 `catalog/` 子目录提供具体 entries
- 主 paper next version 会引用前 10 个 catalog entries 作为 §17.4 扩展

## 几个 sample submission (用本模板写 §17.4 的 4 个)

为示范模板用法 · 已有 4 个 sample submission 按本模板写成 dev-notes (项目内部):

- `dev-notes/011-CFE同构-Bloom-Filter-PIR.md` · 模板填法示例 · Bloom Lookup
- `dev-notes/012-CFE同构-图可达性-Stealth-Probe.md` · Reachability
- `dev-notes/013-CFE同构-差分密码分析-Rate-Limit-Bypass.md` · Differential
- `dev-notes/014-CFE同构-反向传播-Federated-Privacy.md` · Backprop Gradient

每个填了完整 10 个 sections · 是本模板的 reference implementation。

## 鼓励 First Contributors

我们特别鼓励:

- **First 10 catalog entries** · 给 "Founder Contributor" 称号 + 永久 cite 优先权
- **跨学科 entries** · 来自非传统密码学 / 量子背景的提交者
- **被淘汰算法的复兴** · 找 30+ 年前被遗忘的经典算法做 CFE 同构 · 复活老灵感
- **Counter-examples** · 证明某算法**不能** CFE 同构的 entries 也有价值 (避免别人重复尝试)

## License

CC BY 4.0
