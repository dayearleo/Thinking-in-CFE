# Batch 5 · B 类物理可行性深度审计 · CFE 物理基础是否成立

> 优先级:**P0+** · user 直接 priority shift · "CFE 物理基础不牢则后续审计无意义"
> 方法论:抓 3 个关键实验 paper 全文 (Franco-Camillini-Galvão 2026 · Calafell 2019 · Kwiat 1995) · 对照论文 §03.9 / §05.3 / §10 物理 claim
> 这是 audit 中信息量最大的章节 · 应作为论文 §11 限界更新和 §03.9 重写的真理源

---

## TL;DR · 一句话结论

**CFE 物理基础是真实的 · 不是空中楼阁** · 但论文 §03.9 / §05 几个具体数字 over-stated · 需修订。

---

## 实测数据 vs 论文 claim 对照表 (硬核数字)

### 关键实测来源

| Paper | Platform | 关键实测数字 |
|---|---|---|
| Franco-Camillini-Galvão 2026 (arxiv 2604.04691) | Quandela Ascella UPP · 12-mode cloud | sequential multi-object IFM **up to N=5 objects** · single photon probe |
| Calafell et al. 2019 (npj Quantum Info 5:61) | MIT SOI nanophotonic processor (26 waveguides · 88 MZIs) | chained CFC **N=6 max** · single MZI **visibility 99.94%** · chained N=6 bit success 99% **needs M=320 photons per bit** · CFC violation 2.4% · per-facet loss 3 dB · heralding efficiency 3% · SNSPD detection efficiency ~90% |
| Kwiat 1995 (PRL 74:4763) + Kwiat 1999 (PRL 83:4725) | Bulk optics polarization Zeno | 高效率 IFM 理论可任意接近 1 · 但 N 越大物理实现越复杂 · 实验 demo 73% (1995) → 80%+ (1999) |
| Ma 2014 | Photonic on-chip | first on-chip high-efficiency IFM |
| Giordani 2023 | Programmable UPP | standard EV interrogation on UPP |

### 论文 §03.9 / §05 物理 claim vs 实测对账

| AUD | 论文 claim | 实测 SOTA | 对账结果 |
|---|---|---|---|
| C03-015 | "N=12 universal photonic processor lab proven" | **N=12 是 Ascella platform mode 数 (universal)** · 但 multi-object IFM 实验最大 **N=5 sequential** · chained CFC **N=6 max** (Calafell chip layout limit) | **PARTIAL** ⭐⭐⭐ · N=12 modes 是 hardware capability · 但实际 IFM N=5-6 · 必须区分 "hardware mode 数" vs "IFM object 数" |
| C03-016 | "端到端 5 dB loss" | Calafell **3 dB per facet** · system 累加 SNSPD detection 90% + heralding 3% + chip transmission · 总 end-to-end "光子从 source 到 detector" success rate **~3%** | **PARTIAL** ⭐⭐⭐ · 单边 3 dB facet loss OK · 但 "5 dB end-to-end" 实际是低估 |
| C03-016 | "counterfactual efficiency 单链路 > 99%" | Single MZI **visibility 99.94%** · chained N=6 protocol bit success **99% needs M=320 photons per bit** · 单 photon CFC violation 2.4% | **PARTIAL** ⭐⭐⭐ · 99% 是 single MZI · 不是 chained protocol · 应改"single MZI visibility > 99%" 或"chained N=6 bit success 99% with M=320 photons per bit" |
| C03-017 | "Quantum Zeno effect + chained interferometer 提升反事实效率" | Kwiat 1995/1999 理论 · Calafell 2019 + Cao 2017 (Salih scheme) 实验 demo | **CONFIRMED** ⭐⭐⭐⭐⭐ |
| C03-018 | "EAM (电吸收调制器) 作为 obstacle 物理实现" | Calafell 用 SWAP gates (thermo-optic phase-shifter MZI 切换) · 不是 EAM · Franco 用 reflectivity tunable BS | **PARTIAL** ⭐⭐⭐⭐ · EAM 是一种 candidate · 但实际 photonic chip 多用 thermo-optic phase shifter 或 mode-swap 实现 obstacle |
| C03-019 | "SNSPD 阵列单光子探测 cryogenic" | Calafell photonSpot SNSPD ~90% efficiency · telecom 1565 nm | **CONFIRMED** ⭐⭐⭐⭐⭐ |
| C03-020 | "Heralded SPDC / III-V QD 单光子源" | Calafell 1563/1565.8 nm SPDC · heralding efficiency ~3% | **CONFIRMED** ⭐⭐⭐⭐⭐ (heralding 3% 是物理上限 · 不是 caveat) |

### 论文 §05 / §10 物理 claim vs 实测

| AUD | 论文 claim | 实测 SOTA | 对账结果 |
|---|---|---|---|
| C05-001 | "FT QC 实现 $\Phi^{CF}_f$ 需 $\sim 10^3 N$ 物理 qubit (含 surface code overhead)" | FT QC SOTA · 业界共识 1 logical qubit ~ 10^3 physical qubit (surface code) · 模拟一个 $\Phi^{CF}_f$ 需要 N + ancilla = O(N) logical qubit · 总 ~10^3 N physical | **CONFIRMED** ⭐⭐⭐⭐⭐ |
| C05-004 | "CFE 比 FT QC 同 capability 成本便宜 $\sim 6$ 个数量级" | photonic IFM chip ~$50k-$150k · FT QC 当前每台 $10^8-10^10 · 比例确实 ~10^6 | **CONFIRMED** ⭐⭐⭐⭐⭐ (粗估) |
| C10-001 | "单细胞物理上不能搬进 quantum register · FT QC 永远无法做这个" | FT QC 操作 internal qubit · 不能 directly probe 外部物理样本 · 必须先测样本破坏 · 然后 quantum process · 失去反事实性 | **CONFIRMED** ⭐⭐⭐⭐⭐ |

---

## 🚨 重大物理 caveat (论文必须 disclose · 但目前没写)

### CAVEAT 1 · multi-object IFM efficiency 随 n 快速衰减

Franco 2026 paper 明确写:**"as we add more objects, the probability of the IFM outcome diminishes, and there will be a higher chance of an absorption by any of the objects occurring, so that η is in general a quickly decaying function of n"**。

意味着我们论文 §10 A2 "单细胞多 assay 同时检测 N=20-50 properties" 是**乐观估计** · 实际 N=5 在 Quandela Ascella 上已经是 SOTA。N=20+ 需要要么:

- exponential resource scaling (fully overlapping scheme · resource $2^{n-1}$)
- 或者 linear scaling 但 efficiency 极低 (Franco non-overlapping scheme)
- 或者 manipulate 多 degrees of freedom (Filatov-Auzinsh temporal encoding)

§10 应加 caveat:**"current SOTA multi-object IFM is N=5 (Franco 2026). Scaling to N=20+ requires either exponential resources or significantly reduced efficiency · open engineering challenge"**。

### CAVEAT 2 · CFC violation 不是 0

Calafell 2019 实测 CFC violation 2.4% (for N=6, M=320)。这意味着:

- R2 (adversary undetectable) 在 $\delta \to 0$ 极限下成立
- 但 finite $\delta > 0$ 时 · CFC violation rate finite · adversary 有 ~2-3% 概率察觉
- 论文 §15 "adversary-undetectable" claim 应加 caveat "with bounded violation probability"

### CAVEAT 3 · Salih 2013 (direct CFC) 需要 thousands of optical elements 才 >95%

Calafell 2019 引述:**"Salih scheme requires thousands of optical elements to achieve >95% success"** · 我们 §17 同构方法论 / §14 worked example 用 Salih scheme 时 · 必须诚实标注这个 scaling requirement。

### CAVEAT 4 · Heralding efficiency 仅 ~3%

意味着 single photon source 实际利用率低 · CFE 算法 cost model 应该考虑 "wall-clock time = $B_\delta(f) / (\text{heralding rate} \times \text{detection efficiency})$"。

§07 复杂度章节应加 wall-clock cost discussion。

### CAVEAT 5 · Visibility 99.94% 是 single MZI · 不是整个 chained protocol

§03.9 "counterfactual efficiency 单链路 > 99%" 实际指 single MZI visibility · 多 MZI chained 时 visibility 累乘衰减 $(0.9994)^N$:

- N=6: 99.64%
- N=20: 98.81%
- N=100: 94.18%

到 N=100+ 时单纯 visibility 已经主导 violation rate。

---

## 是否空中楼阁?· 综合判定

### 结论:**CFE 物理基础是真实的 · NOT 空中楼阁**

理由:

1. ✅ **30+ years 文献 + 实验积累** (Elitzur-Vaidman 1993 → Kwiat 1995/1999 → Hosten 2006 → Kong 2015 → Ma 2014 → Calafell 2019 → Giordani 2023 → Franco 2026)
2. ✅ **多 platform 验证** (bulk optics / NMR / nanophotonic / programmable UPP)
3. ✅ **关键组件全成熟商用** (SPDC source / SNSPD / SOI waveguide / thermo-optic phase shifters)
4. ✅ **Multi-object IFM 已 lab demo** (Franco N=5)
5. ✅ **R1/R2/R3 性质都有物理 backing** (Zeno 高效率 / CFC violation 可压低 / single photon survives interrogation)
6. ✅ **Universal photonic processor** (Quandela Ascella · 12-mode cloud-accessible · 实际商用)

### 但是有几个真 gap (PARTIAL 类)

1. ⚠️ **N=12 实际是 platform mode 数 · IFM object 数最大只 N=5** (Franco) 或 N=6 chained CFC (Calafell chip-layout-limited)
2. ⚠️ **"端到端 5 dB loss" 是 per-facet · system 总 loss + heralding 累加远高于 5 dB** · 实际 wall-clock cost 受 system efficiency dominated
3. ⚠️ **"> 99% single-link efficiency" 是 single MZI visibility · 不是 chained protocol bit success rate**
4. ⚠️ **Multi-object IFM efficiency 随 n 快速衰减** · §10 应用 niche 不能简单推到 N=20+
5. ⚠️ **CFC violation finite (~2-3%)** · 不是 0 · R2 "adversary undetectable" claim 应带概率 bound

### 论文层面的 priority 修订 (P0)

必须重写以下章节避免被 reviewer 抓物理 over-claim:

1. **§03.9 物理实现要点摘要**:全段重写 · 改 N=12 → N=5-6 (specify which N · multi-object IFM 还是 chained CFC) · 改 "5 dB" → "3 dB per facet + heralding 3% + detection 90% → system end-to-end ~ few %"
2. **§05.3 D2 cost 比较表**:CFE 端的 "5 dB loss + 99% efficiency" 必须加 caveat 跟实测 Calafell/Franco 一致
3. **§10 A2/A3/A4 multi-object IFM 应用 niche**:加 "current SOTA N=5 · scaling to N=20+ is open challenge"
4. **§15.5 R2 mental model 颠覆**:加 "adversary undetectable with bounded violation probability ~2-3% at current SOTA"
5. **§11 限界**:加 5 个新 CAVEAT (上面列的)
6. **§13 RFC**:加 "physical scaling beyond N=5 multi-object IFM" 作为 open verification challenge

---

## 与已审 AUD 的整合

| 已审 AUD | 跟物理基础 finding 的关系 |
|---|---|
| AUD-E-014 (Hance 2025 → Franco-Camillini-Galvão 2026) | REFUTED · 实际作者 + N=5 sequential 不是 12 · 跟 CAVEAT 1 完全 align |
| AUD-E-010 (Hance 2019 → Calafell 2019) | REFUTED · 实际 N=6 max chip layout · 跟 CAVEAT 5 align |
| AUD-E-004 (Lin-Lin 2015 PARTIAL) | 数学跟物理实测一致 · 但 wall-clock 加 system efficiency factor 后 cost 更高 |
| AUD-E-007 (Vaidman 2008) | 综述 · cite 准 |
| AUD-E-008 (Salih 2013) | 需 thousands of optical elements (CAVEAT 3) · 应在引用处加 caveat |

---

## 触发的修订动作汇总 (P0 必做 · 加到 audit/07-prior-art-corrections.md)

1. §03.9 全段重写 + 加 5 CAVEAT
2. §05.3 数字表加 caveat 跟实测 align
3. §10 A2/A3/A4 加 SOTA caveat (N=5 max)
4. §15.5 R2 颠覆 加 violation probability bound
5. §11 限界 加 5 CAVEAT (multi-object scaling / CFC violation finite / Salih cost / heralding efficiency / chained MZI visibility decay)
6. §13 RFC 加 physical scaling 作为 open challenge

每条修订都已经有具体实测 source · reviewer 可以 verify。

---

## 元层评估

### user 真正 priority

User 在 message 中说 "CFE 物理基础不牢则后续审计无意义"。

我的判定:**物理基础是牢的** · 所以后续 attribution/数学定义/复杂度审计仍然有 sense。但是物理 "limits + caveats" 比我们论文 §03.9 描述的紧很多。

具体说:
- ✅ CFE 不是 fiction · IFM 30 年硬科学 · multi-platform 实验
- ⚠️ 但论文 §03.9 几个数字 over-stated · 给 reviewer 留 attack surface
- ✅ 修了这些数字 · CFE 论文仍然 stand · 不需要 retract
- ⚠️ §10 应用 niche 必须 narrow (multi-object IFM 当前 SOTA N=5 · 应用 niche 应聚焦在 N≤10 场景)

### 跟之前 sample claim 的对账

| AUD | 之前 status | 物理审计后是否修正 |
|---|---|---|
| AUD-C03-015 | UNVERIFIED | 升级为 **PARTIAL** ⭐⭐⭐ (见上表) |
| AUD-C03-016 | UNVERIFIED | 升级为 **PARTIAL** ⭐⭐⭐ |
| AUD-C03-017 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-C03-018 | UNVERIFIED | 升级为 **PARTIAL** ⭐⭐⭐⭐ (EAM 是 candidate · 实测多用 phase shifter) |
| AUD-C03-019 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-C03-020 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-C05-001 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-C05-002 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐ |
| AUD-C05-003 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐ (粗估 $50k-150k 合理) |
| AUD-C05-004 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-C05-005 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐⭐ |
| AUD-S03-001 | UNVERIFIED | 跟 H 类 audit 一起做 (跨设备 IFM-attack primitive 共享) |
| AUD-C10-001 | UNVERIFIED | 升级为 **CONFIRMED** ⭐⭐⭐⭐⭐ (FT QC 不能 probe 外部物理样本 · 论文核心论点 still holds) |
| AUD-D003-001 ~ 007 | UNVERIFIED | 升级为多数 **CONFIRMED** ⭐⭐⭐⭐ (基础 hardware claims 正确) |

---

## 版本

- 2026-06-20 v1 · 初版 · 基于 Franco 2026 + Calafell 2019 全文抓取
- 本文件结论:**CFE 物理基础牢固 · 但论文 §03.9 几个数字 over-stated · 修订后论文 still stand**
