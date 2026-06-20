# 04 · 给 NIST 的 Post-Quantum Cryptography Standardization 公开评论信

[← supplements README](README.md)

## 文件性质

**Draft of public comment letter** · 拟提交至 NIST · 回应 NIST Post-Quantum Cryptography (PQC) Standardization Process。本信不是论文 · 是建议 NIST **将 Counterfactual adversary model 纳入 PQC standardization scope** · 或**启动并行 PCC standardization track**。

**重要 disclaimer**:实际提交前必须由作者本人 + 法律顾问 review · 并通过 NIST 公开评论提交流程 (federal register / pqc-comments@nist.gov 等)。

---

## ── 信件正文 (Draft) ──

**To**: National Institute of Standards and Technology, Computer Security Division
**Re**: Post-Quantum Cryptography (PQC) Standardization Process — Public Comment on Adversary Model Scope
**Date**: [TBD]
**From**: [Authors]

### 1 · Subject and Position

We submit this public comment to suggest that NIST's PQC Standardization Process **explicitly consider** a class of cryptographic threats **orthogonal** to those addressed by current PQC algorithms (CRYSTALS-Kyber, CRYSTALS-Dilithium, Falcon, SPHINCS+, etc.).

Specifically, we propose:

> NIST should formally acknowledge **Counterfactual adversary model** as a distinct threat class, either (a) within an extended PQC standardization scope, or (b) as a parallel **Post-Counterfactual Cryptography (PCC)** standardization track.

This is based on our recent paper *"Thinking in CFE: A Counterfactual Function Evaluation Paradigm for Photonic Computation"* (2026, in pre-publication review), which abstracts 30+ years of Interaction-Free Measurement (IFM) literature [Elitzur-Vaidman 1993, Mitchison-Jozsa 2001, Lin-Lin 2015, Hance 2025] into an algorithmic primitive that can attack physical implementations of cryptographic primitives **today**, **without** requiring fault-tolerant quantum computers.

### 2 · Why This Matters for PQC Standardization

NIST's PQC effort is motivated by the threat that **mathematical assumptions** (RSA factoring, ECC discrete log) will be broken when fault-tolerant quantum computers (FT QC) arrive. The proposed PQC algorithms (lattice / hash / code / multivariate) provide alternative mathematical hardness.

However, PQC algorithms — like their pre-quantum predecessors — **rely on physical hardware** to store secret keys (HSM, TPM, Secure Element, smart cards). Their security in deployment assumes:

> "Physical tampering with the hardware triggers detection, key erasure, or attack response."

Our paper shows this assumption is **broken** by Counterfactual Function Evaluation (CFE) attacks, which use integrated photonic IFM probes to extract keys from physical hardware **without triggering tamper detection** (probability of trigger ≤ δ, where δ is parameter-tunable to e.g. 10⁻⁹).

**Consequence for PQC**:

- Migrating from RSA-2048 to CRYSTALS-Kyber does NOT mitigate CFE attacks
- The new lattice / hash / code keys live in the same HSMs as old keys
- CFE extracts them with the same ease

PQC standardization, as currently scoped, leaves a critical vulnerability untouched.

### 3 · Specific Vulnerabilities in Standardization Scope

We identify the following gaps in current PQC standardization scope that PCC threats highlight:

| Gap | Description |
|---|---|
| **G1** | Adversary model assumes mathematical attacker only · does not include adversary with counterfactual physical probing capability |
| **G2** | Hardware security profiles (FIPS 140-3 Level 4, etc.) assume tamper detection is sufficient · CFE invalidates this |
| **G3** | "Harvest now, decrypt later" (HNDL) threat model focuses on intercepted ciphertext · misses CFE-enhanced HNDL where keys are stolen directly |
| **G4** | Migration timelines assume PQC deployment closes quantum threats · ignores CFE-threats that persist post-PQC |
| **G5** | No standardized **Counterfactual Resistance Level** (CRL) certification analogous to FIPS levels |

### 4 · Specific Recommendations

We respectfully suggest NIST consider the following actions:

#### Recommendation 4.1 · Adversary Model Extension

**Action**: Add a new section to the PQC standardization documentation (NIST IR 8413 or successor) explicitly addressing **counterfactual adversary**.

**Rationale**: The cryptographic community needs a clear definition of this threat class to guide algorithm + implementation design. Without standardized adversary model, vendors cannot make security claims that include CFE resistance.

**Specific text we propose**:

> "Counterfactual adversary: An adversary equipped with integrated photonic interaction-free measurement (IFM) hardware capable of querying physical oracles (HSM keys, smart card states, hardware random number generator outputs) with probe-trigger probability ≤ δ for parameter δ ∈ (0, 1]. As δ → 0, the adversary's probing becomes physically undetectable by classical tamper detection sensors. This adversary class is distinct from and complementary to standard cryptanalytic adversaries and quantum cryptanalytic adversaries."

#### Recommendation 4.2 · Hardware Security Profile Update

**Action**: Coordinate with NIST CSF (Cybersecurity Framework) and FIPS 140-3 maintainers to add **Counterfactual Resistance Level** as a new certification dimension.

**Rationale**: FIPS 140-3 currently certifies physical security based on classical tamper detection. CFE attacks bypass this. A new dimension allows vendors to claim (and customers to procure) CFE-resistant products as they emerge.

**Proposed CRL levels** (initial draft):

- **CRL-0**: No CFE resistance claimed · current default
- **CRL-1**: Statistical anomaly detection for residual δ-level disturbance
- **CRL-2**: Active probing interference + decoy probes
- **CRL-3**: Coherence-based tamper detection (quantum probe required to trigger)
- **CRL-4**: MPC-based multi-HSM key splitting · single-HSM compromise insufficient

#### Recommendation 4.3 · Parallel PCC Standardization Track

**Action**: Consider opening a parallel Post-Counterfactual Cryptography (PCC) Standardization Track, analogous to but separate from PQC.

**Rationale**: PCC threats are sufficiently distinct from PQC threats that they may benefit from separate evaluation criteria, separate submission rounds, separate algorithm classes. Combining them risks confusion and resource competition.

We provide a detailed PCC founding document in our supplementary material (see `supplements/01-pcc-founding-document.md`).

#### Recommendation 4.4 · Vendor Disclosure Coordination

**Action**: NIST could facilitate coordinated disclosure between researchers (us, future PCC researchers) and HSM vendors (Thales, Utimaco, Entrust, IBM, AWS, Microsoft, Google, etc.) to ensure responsible handling of CFE threat information.

**Rationale**: Without coordination, fragmented disclosure could lead to either premature exposure or vendor avoidance. NIST's neutral position is ideal facilitator.

#### Recommendation 4.5 · Migration Roadmap Extension

**Action**: Update PQC migration roadmap (NIST SP 800-208 or successor) to include PCC migration considerations.

**Rationale**: Organizations planning PQC migration need to know whether their planned migration also addresses CFE threats. Currently the answer is "no" but it's not clearly communicated.

### 5 · Acknowledgments and Open Issues

We acknowledge:

- This is a **theoretical threat model** at this stage · no end-to-end attack against commercial HSM has been demonstrated
- The attack requires **physical access** to the target hardware · CFE does not bypass physical access requirements (insider threat, supply chain interception remain prerequisites)
- The attack requires **specialized photonic IFM hardware** · currently lab equipment but cost trajectory uncertain

We invite NIST to:

- Independently assess credibility of CFE threats based on referenced literature
- Consult independent cryptographic experts + photonic physics experts
- Provide guidance on whether/how to integrate PCC considerations into PQC scope

### 6 · Engagement Offer

We offer to:

- Provide additional technical detail at NIST's request
- Present at NIST PQC workshops or comparable forums
- Coordinate with other researchers working in CFE / IFM space
- Connect NIST to relevant HSM vendor security teams (with consent)

### 7 · Conclusion

NIST's PQC standardization effort is a landmark achievement that has galvanized the cryptographic community. However, by focusing on mathematical hardness, it leaves the **physical security assumption layer** unaddressed. The CFE threat class — well-grounded in 30+ years of physics literature, with recent experimental demonstrations [Hance 2025] — invalidates this assumption.

We respectfully ask NIST to **extend the conversation** to include counterfactual adversary considerations, either within PQC scope or as a parallel PCC track. The cryptographic community deserves to know:

- That migrating to PQC does NOT close all quantum-related vulnerabilities
- That hardware key storage assumptions need re-examination
- That a path forward exists (PCC research direction)

We are available for follow-up discussion at NIST's convenience.

Respectfully,
[Authors]

Attachments:
- Full paper: `thinking-in-cfe/` (15 chapters, 3000+ lines)
- PCC founding document: `supplements/01-pcc-founding-document.md`
- HSM vendor disclosure templates: `supplements/02 + 03`
- IFM literature bibliography: `thinking-in-cfe/99-references.md`

---

## 提交流程注意事项

NIST 公开评论的提交方式 (基于历史先例):

1. **PQC mailing list**: `pqc-comments@nist.gov` · 或当前 NIST 公布的 channel
2. **Federal Register Notice**: 在指定 comment window 内提交
3. **NIST CSRC** workshops: 现场发言 / 海报
4. **Workshop proceedings**: 投稿 NIST PQC workshop paper

建议:

- 同时走 3 个 channel (mailing list · workshop submission · 私下 outreach to relevant NIST staff)
- 邀请知名密码学家 co-sign (增加 credibility)
- 在 IACR ePrint 同时发布论文 + 本评论信 (建立公开记录)

## License

CC BY 4.0 · 详 paper root `LICENSE.md`
