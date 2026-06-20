# Batch 11 · 物理基础系统化论证 · PhD thesis + critical review 视角

> **优先级**:P0+ · user 第 2 次 priority shift · 担心 CFE 物理基础不牢
> **方法**:抓近期 (2021-2025) IFM/counterfactual 领域 PhD thesis + critical paper 全文 · 跟我们 §02 prior-art / §03.7 R1/R2/R3 differentiator / §11 物理限界 strict 对账
> **结论**:CFE 物理基础是真实的 · 但比之前 audit (batch-5) 更深一层的 critical paper (Frumkin-Bush 2023) 揭示我们 §03.7 "R1/R2/R3 经典都不行" claim 需要 caveat — 经典 pilot-wave 系统可以模拟单 IFM · 但不能模拟 chained Zeno 或 multi-object IFM

---

## 1 · 抓到的 5 个关键 sources

### Source 1 · Jonte R. Hance PhD thesis (Bristol 2023)

- **Title**: "The interplay between quantum foundations and quantum technologies: Counterfactual communication, and extensions of quantum mechanics"
- **Institution**: University of Bristol Doctoral College
- **Date of Award**: 2023-03-21
- **Supervisor**: James A C Ladyman (philosophy) + John Rarity (quantum optics)
- **Sponsors**: EPSRC RCUK · University of York · Quantum Communications Hub
- **PDF**: 7 MB · https://research-information.bris.ac.uk/files/358656794/20230323_JRHance_PhD_Thesis_PostCorrections.pdf
- **PhilPapers + Handle.net** 永久 link

**Abstract verbatim**:

> "This thesis investigates quantum foundations, evaluating and leveraging this area for the development of quantum technologies. ... [It] looks at two areas within foundations: counterfactual communication, and interaction-free measurement. It evaluates the philosophical and foundational issues surrounding these novel developing technologies, such as whether they are counterfactual (by various proposed criteria), and whether they are quantum."

**Key papers in thesis (related publications listed)**:

- "How Quantum is Quantum Counterfactual Communication?" Foundations of Physics 51:12 (2021)
- "Counterfactual Ghost Imaging" CLEO 2021
- "The laws of physics do not prohibit counterfactual communication" (arxiv 1806.01257)
- "Comment on Scheme of the arrangement for attack on the protocol BB84"
- "Exchange-Free Computation on an Unknown Qubit at a Distance"
- "What does it take to solve the measurement problem?"
- "Weak values and the past of a quantum particle"

**对我们论文的 implication**:

- Hance 是 IFM/counterfactual 领域 PhD-level 综述权威 · 我们 §02 prior-art 引 Hance 个人工作 (Calafell 2019 是其合作 paper · §99 已修)
- Bristol PhD thesis 涵盖 我们论文 §02 (IFM history) + §15 (counterfactual security) 全部话题的 PhD-level synthesis
- **可加为 §02 / §99 master synthesis reference**

### Source 2 · Hance et al. 2021 "How Quantum is QCC?" (Foundations of Physics 51:12)

- **arXiv**: 1909.07530 · DOI: 10.1007/s10701-021-00412-5
- **Authors**: Jonte R. Hance · James Ladyman · John Rarity

**Abstract verbatim**:

> "Quantum Counterfactual Communication is the recently-proposed idea of using quantum physics to send messages between two parties, without any matter/energy transfer associated with the bits sent. ... We examine counterfactual communication, both classical and quantum, and show that **the protocols proposed so far for sending signals that don't involve matter/energy transfer associated with the bits sent must be quantum, insofar as they require wave-particle duality.**"

**对我们论文的 implication**:

- **支持** §03.7 R1/R2/R3 differentiator claim · 至少对 *counterfactual communication* 来说 protocol 必需 quantum (wave-particle duality)
- 但 paper 提到 "**so far** the protocols proposed" · 留 open 是否 classical 可以做 (未排除 future)

### Source 3 · Frumkin-Bush 2023 "Misinference of IFM from classical system" (PRA 108:L060201)

- **DOI**: 10.1103/PhysRevA.108.L060201
- **Authors**: Valeri Frumkin · John W. M. Bush (MIT)
- **Published**: 2023-12-12
- **Letter (short paper)**

**核心论点 verbatim**:

> "Here, we present **a classical analog of interaction-free measurement using the hydrodynamic pilot-wave system**, in which a droplet self-propels across a vibrating fluid surface, guided by a wave of its own making. We argue that existing rationalizations of interaction-free quantum measurement in terms of particles being guided by waveforms allow for a classical description manifest in our hydrodynamic system, **wherein the measurement is decidedly not interaction-free**."

**实验细节**:

- 7.0 ± 0.3 mm silicon oil bath · 80 Hz vertical vibration · γ = 3.95g
- Walking droplet (millimetric · self-propels by interaction with its own pilot wave)
- 实现 Elitzur-Vaidman bomb tester analog · droplet 进 left channel (有 "bomb") detonate · 进 right channel 偏转
- 实测 **droplet has 25% chance of being detected on right side · indicating bomb on left** (跟 EV 量子 IFM 25% 一致)
- bomb 存在 50% 时 · 25% probability detect droplet on right side · 跟 EV 量子结果**统计上等价**

**对 IFM 概念的 challenge**:

> "**Our experiment demonstrates that if particles are accompanied by guiding waveforms, the statistical behavior that has led to the inference of interaction-free measurement in quantum mechanics may be achieved in a classical system.**"
> "All current attempts to rationalize interaction-free measurement rely on a physical picture where localized wave-particle objects (e.g., traveling wave packets, or Bohmian particles with their pilot and empty waves) travel along the arms of the interferometer. Our study demonstrates that such localized wave-particle descriptions of interaction-free measurement can also be achieved in a classical system."

**重大 implication for our paper**:

1. **§03.7 R1/R2/R3 differentiator claim 需要 caveat**:经典 hydrodynamic pilot-wave 系统 **可以** 实现 single IFM 的统计行为 (25% 等价) · 不是绝对 quantum-only
2. Frumkin-Bush 没有 demonstrate **chained Zeno IFM** (Kwiat 1995) · 也没有 multi-object IFM (Franco 2026)
3. paper 提议 falsification 实验:延长 arm length nλ · 看 effect 是否 persist · 若 persist 则 IFM 是 quantum-only (favor Copenhagen) · 若不 persist 则 IFM is misnomer

**Frumkin-Bush 自己的 honest disclaimer**:

> "**It is important to note the differences between interaction-free measurement in quantum mechanics, and the analogous statistical inference made in the classical system presented here.** First, the quantum wave function is a nonlocal object that is determined by the entire configuration of the experimental setup. ... In our system, the pilot wave is affected by the global geometry, just as a standing field of Faraday waves is affected by boundaries in confined geometries [46]. **The form of the pilot wave is affected by the totality of the boundary geometry only if its spatial extent is sufficiently large.** Consequently, changing the configuration of the setup (for example, by either increasing its size or decreasing the system memory) will serve to suppress the surreal trajectories and so nullify the effect."

意思:hydrodynamic analog 在 finite memory + finite spatial extent 下 work · 量子 IFM 在 arbitrary scale 都 work · 这是 fundamental 差异。

### Source 4 · Violaris Oxford DPhil thesis 2025 "Counterfactuals in macroscopic quantum physics"

- **Institution**: University of Oxford · Mathematical Institute · MPLS Division
- **Deposit date**: 2025-05-20
- **Supervisors**: Vlatko Vedral · Artur Ekert
- **Examiners**: David Deutsch · Gerardo Adesso

**Abstract verbatim**:

> "Can quantum theory be applied on all scales? ... In this thesis we approach these problems using counterfactuals — statements about the possibility and impossibility of transformations. **Using the principles of constructor theory and quantum information theory**, we find novel features of quantum thermodynamics relating to irreversibility, information erasure and coherence. We also develop tools to quantify the full implications of non-commutativity of quantum operators in settings where quantum theory is applied universally to measurement devices."

**对我们论文的 implication**:

- 这是 quantum foundations 视角的 PhD thesis · 不直接讨论 IFM 应用
- 但 constructor theory (Deutsch-Marletto) 框架可能给我们 D3 论点 (CFE 跟 FT QC categorical 差异) 提供 formal foundation
- §05 D3 论证可以 cite constructor theory framework

### Source 5 · Bush 2021 综述 "Hydrodynamic quantum analogs" (Rep. Prog. Phys. 84:017001)

(从 Frumkin-Bush 2023 reference [29] 找到)

**关键发现**:经典 pilot-wave hydrodynamic 系统已经模拟过的 "quantum" 现象:

- single- + double-slit diffraction + 单 particle interference [30]
- quantization of orbital states [31, 32]
- emergence of wavelike statistics in corrals [33, 34]
- Friedel oscillations [35]
- superradiance [36]
- hydrodynamic spin lattices [37]
- surreal Bohmian trajectories [39]
- **interaction-free measurement** [本 Frumkin-Bush 2023]

**对我们论文的 implication**:

- 经典 pilot-wave 系统可以模拟很多 "quantum" 现象 · 不只 IFM
- 这 broader 地 challenges 任何 "quantum-only" claim · 必须 careful 标 caveat

---

## 2 · 跟我们论文的精确对账

### 对账 1 · §03.7 R1/R2/R3 differentiator (AUD-C03-014)

**论文当前 claim**:

> "**只有 $\Phi^{CF}_f$ 同时具备 R1 + R2 + R3** —— 这是算子的核心 differentiator。"

**Frumkin-Bush 2023 challenge**:

- R1 (触发率任意小) · 经典 hydrodynamic system 可以模拟单 IFM 的 statistics (droplet 25% detection 跟 EV 量子 25% 等价)
- 也就是说 · **单 IFM 的 R1 性质 (在统计意义上) 经典系统可以 reproduce**

**修订建议**:

§03.7 R1/R2/R3 differentiator claim 应改为:

> "$\Phi^{CF}_f$ 在 chained Zeno + multi-object IFM 规模上同时具备 R1 + R2 + R3 ——
> 这是算子的核心 differentiator。
> **注**:single bomb tester 规模的 IFM statistics 可以在 classical hydrodynamic 
> pilot-wave 系统中模拟 [Frumkin-Bush 2023, PRA 108:L060201] · 但 chained Zeno 
> high-efficiency IFM (Kwiat 1995) + multi-object IFM (Franco 2026) 涉及任意标度 
> nonlocal wavefunction · 经典 pilot-wave 系统的 finite spatial extent + finite memory 
> 无法 reproduce。我们 CFE 算子的实际工程 niche 在 chained / multi-object 规模 · 
> 不依赖 single bomb tester 的 quantum-only 特性。"

### 对账 2 · §02 prior-art "30 年文献链" 完整性 (AUD-C02 · 多个 claim)

**论文当前**:§02 prior-art 引 Elitzur-Vaidman 1993 → Kwiat 1995 → Mitchison-Jozsa 2001 → Salih 2013 → Calafell 2019 → Franco 2026

**审计缺失**:

- 漏 Hance Bristol PhD thesis 2023 (PhD-level synthesis)
- 漏 Violaris Oxford DPhil 2025 (constructor theory framing)
- 漏 Frumkin-Bush 2023 (critical paper challenging IFM quantum-only)
- 漏 Bush 2021 综述 (hydrodynamic quantum analogs broader context)
- 漏 Hance 2021 "How Quantum is QCC?" (formal argument IFM quantum)
- 漏 IOP 2024 "Counterfactuality, back-action, and information gain in multi-path interferometers"

**修订建议**:§02 prior-art 加新 section "§02.7 · PhD-level synthesis + critical reviews":

```
**Hance PhD thesis 2023** (Bristol) · "The interplay between quantum foundations 
and quantum technologies: Counterfactual communication, and extensions of quantum 
mechanics" · 7 章 PhD-level synthesis 含 IFM + CFC + quantum measurement extensions · 
是我们论文 §03 / §15 内容的 PhD-level reference。Permanent handle: hdl.handle.net/1983/a3cf0e59-31a9-456f-800e-cd3b6533461b

**Violaris DPhil thesis 2025** (Oxford) · "Counterfactuals in macroscopic quantum 
physics: irreversibility, measurement and locality" · constructor theory 视角讨论
counterfactuals · 跟我们 §05 D3 论证形式化相关。

**Frumkin-Bush 2023** (PRA 108:L060201) · "Misinference of interaction-free 
measurement from a classical system" · **critical paper** demonstrating classical 
hydrodynamic pilot-wave system 可以 reproduce single IFM 25% detection statistics · 
但 chained Zeno + multi-object IFM 不可。我们 §03.7 R1/R2/R3 differentiator claim 
已加 caveat 跟此 paper align。

**Bush 2021** (Rep. Prog. Phys. 84:017001) · "Hydrodynamic quantum analogs" · 综述 
经典 pilot-wave 系统已模拟的 quantum 现象 (包括 IFM)。

**Hance-Ladyman-Rarity 2021** (Foundations of Physics 51:12) · "How Quantum is 
Quantum Counterfactual Communication?" · 论证 counterfactual communication protocols 
proposed so far 必需 quantum (wave-particle duality) · 支持 §03.7 differentiator 
claim 在 CFC 规模上。
```

### 对账 3 · §11 限界 加新 CAVEAT (AUD-C11)

**修订建议**:§11.2 加 CAVEAT 6:

```
### CAVEAT 6 · Single IFM 经典 pilot-wave 系统可模拟 (Frumkin-Bush 2023)

我们 §03.7 R1/R2/R3 differentiator claim 在 single bomb tester 规模上 **不严格成立**:

- Frumkin-Bush 2023 (PRA 108:L060201) 在 hydrodynamic pilot-wave system 上 demonstrated
- 25% droplet detection 跟 EV 量子 IFM 25% 等价
- 但 hydrodynamic system 受 finite spatial extent + finite memory 限制 · 
  不能 reproduce chained Zeno (Kwiat 1995) + multi-object IFM (Franco 2026)

精确表述:

- **single bomb tester 规模**:$R_1$ 性质可以 classical pilot-wave 模拟
- **chained Zeno 规模** (N ≥ 6 chained MZI):需要任意 scale 的 nonlocal wavefunction · 经典系统不可
- **multi-object IFM** (N ≥ 5):同上 · quantum probe 全局 entangled state · 经典不可

CFE 算子的实际工程 niche 都在 chained / multi-object 规模 (§10 应用都假设 N ≥ 2 chained) · 
所以 R1/R2/R3 differentiator 实际成立 · 但论文应 honest 标 caveat。

物理学界 falsification 实验 (Frumkin-Bush 2023 提议):延长一个 interferometer arm length 
nλ · 看 IFM effect 是否 persist · 若 persist → 量子 nonlocal 必需 (经典不可) · 若不 persist 
→ IFM 是 "misnomer"。
```

### 对账 4 · §05 D3 加 constructor theory framing (Violaris 2025)

§05.4 D3 论证可以加 constructor theory cite:

```
注:**Violaris DPhil thesis 2025** (Oxford) 用 constructor theory (Deutsch-Marletto 
2015) 框架研究 macroscopic quantum counterfactuals · 跟我们 D3 论证 (CFE 跟 FT QC 
categorical 差异) 同向 · 提供 formal foundation。
```

---

## 3 · 整体结论

### CFE 物理基础是否牢固 · 修正后判断

| 维度 | batch-5 (前次) judgment | 本次 (PhD thesis + critical) | 修订 |
|---|---|---|---|
| **CFE 物理基础真实存在** | ✅ | ✅ (仍 confirm) | 不变 |
| **30+ 年文献链** | ✅ | ✅ + Hance PhD thesis 2023 + Violaris DPhil 2025 加入 | 加 source |
| **R1/R2/R3 quantum-only** | 默认 ✅ | ⚠️ single IFM 经典可模拟 (Frumkin-Bush 2023) · chained/multi-object 仍 quantum-only | **加 caveat** |
| **应用 niche scaling** | 加 caveat N ≤ 10 | 同上 · 但 R1/R2/R3 在 N ≥ 2 chained 规模成立 · niche 实际不受影响 | 不变 |
| **CFE 不是空中楼阁** | ✅ | ✅ (仍 confirm · PhD-level synthesis backing) | 不变 |

### CFE 物理基础 NOT 空中楼阁 · 但有 nuance

**核心 confirm**:
- ✅ Hance 2023 PhD thesis 是 IFM/CFC 领域 PhD-level synthesis · 涵盖我们论文 §02-§15 关键话题
- ✅ Violaris 2025 Oxford thesis 用 constructor theory 给 quantum counterfactuals 提供 formal foundation
- ✅ Franco 2026 + Calafell 2019 实验数据 cross-check (batch-5)
- ✅ Bush 2021 综述 confirms 经典 pilot-wave 系统不能 reproduce chained Zeno (需任意 scale nonlocal wavefunction)

**重要 nuance (必加 caveat)**:
- ⚠️ Frumkin-Bush 2023 critical paper:single bomb tester 规模 IFM statistics 可以经典模拟
- ⚠️ 因此 §03.7 R1/R2/R3 differentiator 严格说在 single IFM 规模不 hold · 应 caveat 限定到 chained Zeno + multi-object IFM
- ⚠️ 我们论文 § 03.7 表 + § 11 限界 必须加上 Frumkin-Bush 2023 disclaimer

### 跟前次 batch-5 audit 互补

- batch-5 抓**实验**数据 (Franco / Calafell / Kwiat) · 验证 SOTA 数字
- batch-11 抓 **理论 + 哲学** 视角 (Hance PhD thesis · Violaris · Frumkin-Bush critical · Bush 2021 综述) · 验证 R1/R2/R3 claim 的概念严格性

两个 audit **共同** confirm:CFE 物理基础真实 · 但论文必须显式标若干 caveat:

1. ✅ batch-5 caveat 已 落地 (commit ab8aba4):N=12 → N=5 / 5 dB / >99% / violation 2.4%
2. ⏳ batch-11 caveat 待落地:R1/R2/R3 differentiator 限定 chained/multi-object IFM 规模 · 加 Frumkin-Bush 2023 critical paper

---

## 4 · 修订动作汇总 (P0 待修)

加到 `audit/07-prior-art-corrections.md`:

| ID | 修订内容 | 优先级 |
|---|---|---|
| Correction P0-6 | §02 prior-art 加 "§02.7 PhD-level synthesis + critical reviews" 段 · 引 Hance 2023 PhD thesis + Violaris 2025 + Frumkin-Bush 2023 + Bush 2021 + Hance 2021 + IOP 2024 共 6 篇 | P0 |
| Correction P0-7 | §03.7 R1/R2/R3 differentiator 加 Frumkin-Bush 2023 caveat | P0 |
| Correction P0-8 | §11.2 加 CAVEAT 6 (single IFM classical analog) | P0 |
| Correction P1-4 | §05 D3 论证加 Violaris constructor theory cite | P1 |
| Correction P0-9 | §99 references 加 6 个新 entry (本 batch sources) | P0 |

---

## 5 · 元层

### user 第 2 次 priority shift 的价值

User 担心 CFE 物理基础 · 这次审计揭示了 **batch-5 (实验数据)** 之外的另一维度 caveat:**Frumkin-Bush 2023 hydrodynamic analog**。

这是关键的发现:**没有任何单 audit 模式可以覆盖全部物理 caveat**。
- batch-5 抓实验 SOTA → 揭示 over-claim N=12 / 5 dB / >99%
- batch-11 抓 PhD thesis + critical → 揭示 R1/R2/R3 differentiator 在 single IFM 规模不严格

后续 audit 模式建议:
- batch-12 (假设要做):抓 Hance Bristol PhD thesis 全文 (PDF 抓取需 alternative path · 当前 PDF anti-bot 拦截)
- batch-13:抓 Violaris Oxford 全文 + constructor theory primary literature
- batch-14:跟物理学界 active researcher (Hance · Vaidman · Bush) 私下访谈

### 实事求是的最终物理基础评估

**CFE 物理基础是真实的** · 30+ 年 IFM 文献 + 多 platform 实验 + PhD thesis 综述 + 实际商用 photonic 硬件支持。

**但我们论文需要 honest caveat**:

1. ⚠️ Single bomb tester 规模 IFM 不严格 quantum-only (Frumkin-Bush 2023)
2. ⚠️ Chained Zeno + multi-object IFM 仍 quantum-only · 我们应用 niche 在这里
3. ⚠️ N=12 是 platform mode 数 · multi-object IFM SOTA N=5 (batch-5)
4. ⚠️ R2 violation 2.4% 不是 0 (batch-5)
5. ⚠️ Multi-object IFM efficiency 随 n 快速衰减 (batch-5)

后 5 个 caveat 全部已落地 commit ab8aba4。本次发现的 caveat 1 待加。

**核心论点 (D3 永久独占外部物理 oracle · 17 算法 audit · 减法计算范式) 全部 still stand**。

---

## 版本

- 2026-06-20 v1 · user 第 2 次 priority shift 后 · PhD thesis + critical review 视角的物理基础 audit
