# AUD-C15-001 · Assessment

## Claim 速述

我们提出 "Post-Counterfactual Cryptography (PCC)" 作为新密码学子领域名 · 类比 Post-Quantum Cryptography (PQC)。

## status: **PARTIAL** ⭐⭐⭐ (命名 NOVEL 但有重大 prior-art GAP)

## 推理链

1. **PCC 命名 NOVEL**:EXA 搜 `Post-Counterfactual Cryptography PCC quantum security` · 0 hits 命中我们的 phrase
2. **但发现重大 GAP**:存在 17 年的 "Counterfactual Quantum Cryptography (CQC)" 子领域:
   - [Noh 2009] "Counterfactual Quantum Cryptography" PRL 103, 230501
   - "Semi-counterfactual Cryptography" 2013 arxiv 1307.7551
   - "Counterfactual quantum cryptography based on weak coherent states" 2012 PRA 86.022313
   - 中国物理 B 2012 "Security proof of counterfactual quantum cryptography"
   - "Semi-Counterfactual Quantum Bit Commitment" 2020 Sci Rep
   - "Experimental Counterfactual Quantum Communication" 2012 PRL 109.030501
3. 我们论文 §15/§16/supplement 01 **完全没引** [Noh 2009] 这一系列
4. 命名 "Post-Counterfactual" 跟已有 "Counterfactual Quantum Cryptography" 概念冲突:
   - PQC = "Post-Quantum" 意思 "为量子时代准备" (quantum 是 future threat)
   - 但 "Counterfactual" 不是 era 转变 · 是 cryptography 的 niche
   - 直接 "Post-Counterfactual" 可能让 reviewer 误以为是 CQC 的 successor

## 触发动作 (重大 · P0)

### 1 · 加 [Noh 2009] + CQC 系列 prior-art (P0)

§02 prior-art + 99-references.md 必须加:

```
[Noh 2009] T.-G. Noh.
"Counterfactual Quantum Cryptography."
Phys. Rev. Lett. 103, 230501 (2009).
DOI: 10.1103/PhysRevLett.103.230501.
```

加 disambiguation 段在 §15.7 或 §02:

> "Counterfactual Quantum Cryptography" (CQC) 自 [Noh 2009] 起是 active 子领域 · 用反事实传输做 key distribution · 跟我们 PCC 正交:CQC 用 counterfactual 做 cryptographic protocol · 我们 PCC 是 防御 counterfactual 攻击的 cryptographic design。

### 2 · 重新评估 "PCC" 命名 (P0)

考虑改名以避免歧义:

候选 alt name:

- "Counterfactual-Resistant Cryptography" (CRC) · 跟 PQC 类比更直接 (Quantum-Resistant Cryptography)
- "Anti-Counterfactual Cryptography" · 强调防御
- "Counterfactual-Aware Cryptography" (CAC) · 强调威胁意识

如果保留 PCC 名 · 必须在 §15.9 + supplement 01 加 explicit clarification:

> "PCC 中的 'Post-' 跟 PQC 的 'Post-' 类比:不是 'counterfactual era 之后' · 而是 'for the era when counterfactual capability becomes available'。PCC 跟已有 'Counterfactual Quantum Cryptography (CQC)' 是正交研究方向 — CQC 用 counterfactual 做 cryptographic primitive,PCC 防御 counterfactual probing 攻击。"

### 3 · 更新 supplement 01 PCC founding document

加专门 §X "PCC vs CQC differentiation" · 详细对比表。

## 证据强度

⭐⭐⭐ (3 星 PARTIAL) · 命名 phrase NOVEL · 但 prior-art GAP 是高风险 reviewer-killing 缺失

## search-log 简略

- EXA query: `Post-Counterfactual Cryptography PCC quantum security`
- Top 6 hits 全部是 17 年的 "Counterfactual Quantum Cryptography" 子领域工作 · 没有 "Post-Counterfactual" namespace
- 我们论文 grep 显示:0 处引 Noh 2009 · 0 处提 CQC 子领域

## 元层

- M1 ✓ (找到 Gap)
- M2 ✓
- M3 ✓
- M4 N/A
