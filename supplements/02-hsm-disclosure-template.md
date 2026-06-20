# 02 · HSM / Secure Element 责任披露信 · 通用模板

[← supplements README](README.md)

## 文件性质

**披露信通用模板** · 用于给 HSM / TPM / Secure Element / Smart Card 厂商的 security team。具体厂商版本在 `03-hsm-disclosure-specifics.md`。

**重要 disclaimer**:本文是 **draft template** · 实际发送前必须由作者本人 + 法律顾问 review。本文档没有任何形式的法律 binding · 也没有任何 endorsement。

## 责任披露原则

本披露遵循 **CVD (Coordinated Vulnerability Disclosure)** 原则:

- 给厂商**合理 grace period** (建议 90 天) · 让厂商 review + plan response
- grace period 内 · 我们**不公开**具体厂商相关细节
- grace period 后 · 公开论文 + 厂商正式 response (如有)
- 厂商提交 response 后 · 我们 incorporate 到论文 v0.2

---

## ── 披露信正文 (模板) ──

**To**: [Vendor Security Team]
**From**: [Authors]
**Date**: [TBD]
**Subject**: Coordinated Disclosure · Theoretical Vulnerability Class Affecting Hardware Root of Trust Products

### 1 · Executive Summary

We have authored an academic paper, *"Thinking in CFE: A Counterfactual Function Evaluation Paradigm for Photonic Computation"* (currently in pre-publication review), which identifies a **theoretical vulnerability class** affecting a broad range of HSM, TPM, Secure Element, and similar hardware-root-of-trust products **including products in your portfolio**.

**Key facts**:

- The vulnerability is based on **Counterfactual Function Evaluation (CFE)** · a quantum-physical primitive abstracting 30+ years of Interaction-Free Measurement literature [Elitzur-Vaidman 1993, Mitchison-Jozsa 2001, Lin-Lin 2015, Hance 2025]
- The attack does **not** require fault-tolerant quantum computers · current SOTA integrated photonic IFM chips (N ≤ 12-32 mode) are sufficient for proof of concept
- The attack does **not** break the mathematical algorithms (AES / SHA / RSA / etc.) running on the device · it extracts secret keys from physical storage **without triggering tamper detection**
- The attack is **theoretical at this stage** · no end-to-end demonstration against a commercial HSM has been performed
- However, all required components (IFM chip · photonic probe · physical coupling techniques) exist in lab settings today

We are reaching out **before public disclosure** of the full paper to give your security team time to (a) independently assess the threat, (b) plan response, (c) optionally collaborate on mitigation research.

### 2 · Affected Product Categories

Any product where:

- A cryptographic secret (key, PIN, seed) is stored in physical hardware
- Tamper detection relies on physical sensors (mesh, photodiode, temperature, voltage)
- The security model assumes "physical probing triggers detection"

This includes (non-exhaustive):

- General-purpose HSM (network-attached, PCIe, USB)
- Hardware wallets (cryptocurrency)
- Smart cards (banking, ID)
- TPM (PC, server)
- Secure Element (mobile, IoT)
- Hardware crypto accelerators with embedded keys

### 3 · Specific Concerns for Your Portfolio

We have reviewed your publicly documented product line. The following products appear to be in scope (please correct any inaccuracies):

- [Product 1]: [Specific concern]
- [Product 2]: [Specific concern]
- ...

(Specific concerns customized per vendor in `03-hsm-disclosure-specifics.md`.)

### 4 · Attack Outline (Summary · Full Paper §16.6.1)

```
INPUT:  Target HSM with secret key K stored in physical structure
GOAL:   Extract K bit-by-bit without triggering HSM tamper detection

step 1: Physical access to HSM (decapsulation / backside thinning)
        — this step IS detectable · CFE does not bypass physical access requirement
        — but: many HSMs are physically accessible to insiders (data center theft, supply chain interception)

step 2: Couple photonic IFM probe to internal SRAM / fuse / register storing K
        — using existing techniques from optical microprobing (Tarnovsky 2010, Skorobogatov 2011)
        — combined with CFE counterfactual readout (Hance 2025)

step 3: For each bit i of K:
          k_i = counterfactual_eval(read_bit_at(K_addr + i), δ=1e-9, ε=1e-3)
        — each readout has probability ≤ 1e-9 of triggering tamper sensors
        — for 256-bit key: cumulative detection probability ≤ 2.56e-7

step 4: K extracted · HSM continues operating normally
        — audit log shows no anomaly
        — tamper response not triggered
        — key可以离线使用 to decrypt all data ever encrypted under K
```

### 5 · Mitigation Directions (Tentative)

We suggest your team consider:

- **Coherence-based tamper detection** · replace classical photo / temp sensors with quantum-coherence detection
- **Active probing interference** · HSM emits dummy decoy quantum probes to confuse CFE attacker
- **MPC-based key storage** · split key across multiple HSMs; CFE must attack all simultaneously
- **Physical randomization** · let oracle self-permute between queries
- **Tamper response that includes statistical anomaly detection** · monitor for the residual $\delta$-level disturbance

We acknowledge none of these are off-the-shelf solutions. Our paper §15.7 + supplement 01 (PCC founding document) propose a new cryptography subfield to systematically address this.

### 6 · Coordinated Disclosure Timeline · Proposed

- **Day 0** (Today): This letter sent to you
- **Day 0-7**: Your acknowledgment and initial assessment
- **Day 7-30**: We hold private discussions with your security team (optional)
- **Day 30-90**: You internally assess + plan response
- **Day 90**: Public release of full paper
- **Day 90+**: We publish your formal response (if provided) as supplement to paper

We are **flexible on timeline** if you request extension for legitimate research / engineering reasons.

### 7 · What We Are Not Asking

- We are **not** requesting bug bounty or monetary compensation
- We are **not** requesting NDAs preventing publication of the academic paper
- We are **not** asking you to admit specific product vulnerabilities publicly
- We are **not** providing exploit code · the paper is theoretical framework

### 8 · What We Ask

- **Acknowledge receipt** within 7 days
- **Internal assessment** of CFE threat applicability to your products
- **Optional engagement** on mitigation research
- **Provide a response** (positive or negative) we can publish alongside the paper

### 9 · Independent Verification

The theoretical basis is publicly verifiable:

- [Elitzur-Vaidman 1993] IFM original paper
- [Mitchison-Jozsa 2001] counterfactual computation
- [Lin-Lin 2015] bomb query complexity formalization
- [Hance 2025] multi-object IFM on integrated photonic chip (arxiv 2604.04691)

We recommend your security team consult these directly to assess credibility independently of our claims.

### 10 · Contact

- Primary: `[Author Email TBD]`
- PGP: `[Fingerprint TBD]`
- Encrypted only: please use PGP for any specific product vulnerability discussion

We look forward to your response.

Sincerely,
[Authors]

---

## 模板使用注意事项

1. 给每个厂商**单独**发 · 不要 BCC 群发
2. 邮件 subject 用 "Coordinated Disclosure" 字样 · 避免被 spam filter 拦
3. 附 PDF 版论文 (从 markdown 转 · 用 pandoc) · 不要直接发链接
4. 发送渠道:
   - 厂商 PSIRT (Product Security Incident Response Team) 官方 email · 优先
   - 厂商 CSO / CISO · 备用
   - 厂商研究院 contact · 长期合作目的
5. **不要**发到 sales / support · 那不是 security team
6. **保留 timestamp 证据** · 邮件 read receipt · 邮件服务器日志
7. **不要在 grace period 内** 跟其他厂商谈论已发送的具体 attack details
8. **不要在 grace period 内** 接受 NDA · 那等同于把 academic 工作绑死

## 相关资源

- Coordinated Vulnerability Disclosure 标准:CERT/CC Guide
- HackerOne / Bugcrowd 协议参考
- Google Project Zero 90-day disclosure 实践
- ISO/IEC 29147 Vulnerability Disclosure

## License

CC BY 4.0 · 详 paper root `LICENSE.md`
