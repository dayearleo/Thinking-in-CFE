# 05 · IACR ePrint 投稿封面

[← supplements README](README.md)

## 文件性质

**Draft cover letter** 用于 IACR Cryptology ePrint Archive 投稿。

## ── 投稿封面正文 ──

**Title**: Thinking in CFE: A Counterfactual Function Evaluation Paradigm for Photonic Computation

**Authors**: [TBD]

**Affiliations**: [TBD]

**Submitted to**: IACR Cryptology ePrint Archive

**Date**: [TBD]

## 1 · Brief Summary

We introduce the **Counterfactual Function Evaluation (CFE) operator** Φ^{CF}_f and the **Subtractive Computation Paradigm (SCP)**, abstracting 30+ years of Interaction-Free Measurement (IFM) literature [Elitzur-Vaidman 1993, Mitchison-Jozsa 2001] and Bomb Query Complexity formalization [Lin-Lin 2015] into a unified algorithmic framework.

Beyond the algorithmic abstraction, we identify a **cryptographically-relevant attack class**: CFE-based key extraction from hardware security modules (HSM), bypassing standard tamper detection via the **R2 property** (adversary-undetectable queries). This attack is **realizable today** on integrated photonic IFM chips (N ≤ 32 mode, [Hance 2025]), not requiring fault-tolerant quantum computers.

We propose **Post-Counterfactual Cryptography (PCC)** as a new cryptographic subfield, parallel to Post-Quantum Cryptography (PQC), addressing this orthogonal threat class.

## 2 · Why IACR ePrint?

This paper:

- Spans **algorithm theory** (CFE operator, composition algebra, complexity dimensions) and **cryptographic implications** (HSM attacks, PCC proposal)
- Engages **multiple subcommunities**: quantum information, complexity theory, applied cryptography, hardware security
- Is **RFC-style** (paper §13): we explicitly request external review and welcome falsification
- Benefits from **public archival**: IACR ePrint provides citation stability + community accessibility

IACR ePrint is the natural venue because it serves the entire cryptographic community without venue-specific scope restrictions, while providing immediate visibility.

## 3 · Cryptographic Contributions Highlight

For ePrint readers focused on cryptographic relevance:

### 3.1 · New adversary model (paper §15)

We propose the **Counterfactual adversary**, distinct from:

- Classical adversary (standard cryptanalysis)
- Quantum adversary (Shor, Grover via FT QC)
- Side-channel adversary (DPA, EM, timing)

Counterfactual adversary is characterized by **adversary-undetectable querying** of physical oracles via Quantum Zeno effect in chained interferometers.

### 3.2 · Attack on 17 industrial cryptographic algorithms (paper §16)

We systematically analyze 17 algorithms commonly deployed in industrial cryptography (DES, 3DES, RC4, IDEA, RC5, Blowfish, AES, ChaCha20, MD5, SHA-1, RSA, DH, EDH, ECC, AES-GCM, ChaCha20-Poly1305).

**Finding**: While none of these algorithms' mathematical structures are broken by CFE, **all 17** have keys typically stored in HSM, and **all 17** become vulnerable when the HSM is subject to CFE-based extraction.

This is a **paradigm-level** vulnerability: the industry assumption of "two-defense-line" security (mathematical algorithm + hardware tamper protection) collapses, leaving mathematics alone, which was never designed to bear the load.

### 3.3 · CFE-enhanced Harvest Now, Decrypt Later (paper §16.7)

We show that **CFE-HNDL** is realizable today, not requiring FT QC:

- Classical HNDL: intercept TLS traffic now, decrypt later when Shor's available
- CFE-HNDL: extract HSM master key now, derive all session keys immediately, decrypt traffic today

PQC migration does **not** mitigate CFE-HNDL, because the attack is at hardware layer not mathematical layer.

### 3.4 · PCC subfield proposal (paper §15.9 + supplement 01)

We propose **Post-Counterfactual Cryptography** as a new IACR-recognized subfield, with:

- Formal adversary model
- Counterfactual-resistant hardware design directions
- Protocol redesign requirements
- 6 research questions opening the field

## 4 · Honest Disclaimer

Per paper §11 + §13, we explicitly disclaim:

- We do **not** break RSA, AES, SHA, or any mathematical cryptographic algorithm
- We do **not** claim end-to-end attack against any specific commercial HSM
- The attack requires **physical access** to the target hardware (CFE bypasses tamper detection, not physical access)
- Photonic IFM hardware required is currently lab-scale, commercial-scale deployment requires engineering

Paper §11 (limitations) and §13 (RFC for verification) explicitly invite the community to challenge any claim.

## 5 · Suggested Reviewer Profile

We suggest IACR ePrint reviewers (or future conference reviewers) consider:

- **Algorithm theorists** familiar with bomb query complexity [Lin-Lin 2015] for paper §3-§4 + §7
- **Complexity theorists** for paper §7.7 (CFP complexity class)
- **Cryptographers with hardware security background** for paper §15-§16
- **Photonic quantum computing experts** for paper §3.9 + §11.2 hardware feasibility
- **Applied cryptographers** with HSM / PQC standardization experience for paper §16 + supplement 04

## 6 · Engagement

We commit to:

- Public response to all substantive review feedback
- Version control of paper (each version tagged in GitHub)
- Incorporation of strongly-supported counterarguments in subsequent versions
- Coordination of follow-up work with interested researchers

## 7 · License

CC BY 4.0 (paper text)
MIT (code in `supplements/10-cfe-hndl-simulator/`)

## 8 · Repository Pointer

Full paper + supplements + simulator code:

`[GitHub URL TBD]`

Direct entry points:

- Paper: `paper/thinking-in-cfe/README.md` (15-chapter table of contents)
- Supplements: `paper/supplements/README.md` (RFC, disclosure letters, NIST comment, simulator)
- Citation: `paper/CITATION.cff`
- License: `paper/LICENSE.md`
- Contributing: `paper/CONTRIBUTING.md`

## Submission notes

实际投稿前 checklist:

- [ ] Author names + ORCID + affiliations 填齐
- [ ] PDF 版本生成 (从 markdown 用 pandoc · 单文件)
- [ ] BibTeX entries 完整 (跟 99-references.md 对齐)
- [ ] 跟 co-authors review (如有)
- [ ] Institution legal / IP office signoff (如学术机构要求)
- [ ] PGP key 准备 (审稿沟通用)
- [ ] arxiv 同步投稿 (cross-list quant-ph + cs.CR)
