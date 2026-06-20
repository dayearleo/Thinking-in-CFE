# 02 · 先行研究 · 30 年回顾与差异化定位

[← 返回 README](README.md)

## 2.1 · 三条主要发展线

IFM/counterfactual 思想在过去 30 余年沿三条互相交叉的线发展:

**(I) 物理理论线** · 提出新的协议与变体
**(II) 实验实现线** · 在不同物理平台上 (光学 / 电子 / x-ray / 集成芯片) 实现
**(III) 形式化与复杂度理论线** · 把直觉变成可分析的数学对象

我们的工作处在 **第 IV 条线** —— **算法-工程抽象线** · 这一条线在 30 年里几乎是空白。

## 2.2 · 物理理论线

| 工作 | 贡献 |
|---|---|
| [Wheeler 1978] · "The 'past' and the 'delayed-choice' double-slit experiment" | 提出延迟选择思想实验 · 质疑波粒二象性的时机 |
| [Elitzur-Vaidman 1993] · "Quantum mechanical interaction-free measurements" | 提出 IFM 协议 · 著名的炸弹检测 |
| [Kwiat 1995] · "Interaction-Free Measurement" | 用 Quantum Zeno effect 把 IFM 效率推到接近 100% |
| [Mitchison-Jozsa 2001] · "Counterfactual computation" | 把 IFM 推广为反事实计算 · 提出可推断量子计算结果而不运行 |
| [Salih 2013] · "Protocol for direct counterfactual quantum communication" | counterfactual 通信协议 · 信道上无 photon 传输 |
| [Filatov-Auzinsh 2024] · "Setup for interaction-free measurement of multiple objects" | 多对象 IFM 提案 · 单 probe 检测多个 absorber |

## 2.3 · 实验实现线

| 工作 | 平台 | 关键参数 |
|---|---|---|
| [Hosten 2006] · "Counterfactual quantum computation through quantum interrogation" · Nature 439 | 桌面光学 + 偏振 | 第一次实物反事实计算 |
| [Kong 2015] · PRL 115.080501 · "Experimental Realization of High-Efficiency Counterfactual Computation" | 桌面光学 | 效率 > 99% |
| [Calafell et al. 2019] · npj Quantum Info · "Trace-free counterfactual communication with a nanophotonic processor" | SiN 集成芯片 | bit error < 1% · 多步 Zeno |
| [Kang 2020] · npj Quantum Info · "Temporal Wheeler's delayed-choice based on cold atomic quantum memory" | Rb 冷原子 | Wheeler 在量子存储介质上跑通 |
| [Franco-Camillini-Galvão 2026] · arxiv 2604.04691 · "Interaction-free measurement of multiple objects using a universal integrated photonic processor" | ASCE cloud chip | **多对象 IFM 实物 · 直接对应本文 §3 算子** |
| [Shwartz 2025] · "Loss-resilient x-ray interaction-free measurements" | X-ray + crystal | IFM 推到 x-ray regime |
| [集成多路 delayed-choice] · Nat Commun 2021 (PMC 8105384) | nanophotonic chip | N = 8 路 multipath delayed-choice |

## 2.4 · 形式化与复杂度理论线

| 工作 | 贡献 |
|---|---|
| [Vaidman 2008] · arxiv 0801.2777 · "The Elitzur-Vaidman Interaction-Free Measurements" | 综述 + 形式化 |
| [Lin-Lin 2015] · CCC + Theory of Computing v12 a18 · arxiv 1410.0932 · "Upper Bounds on Quantum Query Complexity Inspired by the Elitzur-Vaidman Bomb Tester" | 提出 bomb query complexity $B(f)$ · 证明 $B(f) = \Theta(Q(f)^2)$ |
| [Belovs 2019] · arxiv 1905.13095 · "Quantum Speedup Based on Classical Decision Trees" | bomb query 在决策树问题上的应用 |
| [Theory of coherent IFM 2023] · arxiv 2307.05214 | 三级系统 IFM 理论形式化 |
| [Quantum causal counterfactuals 2024] · arxiv 2302.11783 · Quantum journal | Pearl 因果反事实在量子框架的形式化 (注:**这跟我们的算子是不同范畴** · 那是因果推断 · 我们是计算原语) |

## 2.5 · 邻近但不重叠的工作

为防止读者混淆 · 列出 4 类**容易跟我们工作混淆但实际范畴不同**的工作:

**(A) Pearl 风格因果反事实推断** · 例 [Pearl 2009], [Quantum causal 2024]
- **它们做什么**:在因果模型里推断 "如果 X 没发生 · Y 会怎样" 的反事实陈述
- **跟我们的差异**:它们是统计 / 因果推断 · 不是计算原语 · 不涉及物理 oracle

**(B) Counterfactual reasoning in psychology / cognitive science** · 例 [Roese 1993], [Dunning 1989]
- **它们做什么**:研究人类如何想象 "如果当初..." 的认知过程
- **跟我们的差异**:它们是心理学 · 不是算法

**(C) Counterfactual explanations in machine learning** · 例 [Wachter 2017], [Mothilal 2020]
- **它们做什么**:给 ML 模型决策生成 "需要改什么才能翻转预测" 的解释
- **跟我们的差异**:它们用 "counterfactual" 一词指代 ML 解释 · 跟物理 IFM 无关

**(D) "Thinking by Subtraction" / contrastive decoding** · 例 [Yang 2026, arxiv 2602.18232]
- **它们做什么**:LLM 推理时用对比解码提升正确性
- **跟我们的差异**:它们用 "subtraction" 指代 token-level 概率运算 · 跟物理减法计算无关

**重要免责**:本论文使用 "**Subtractive Computation Paradigm**" 全称严格指代 §6 定义的基于 CFE 算子的算法构造哲学。读者**不应**将其混同于上述任一邻近概念。

## 2.6 · 30 年后我们处在什么位置?

跨越 1993-2025 · 物理与形式化层面的工作已经成熟:

- 物理协议 ✅ (Elitzur-Vaidman 单 bomb / Mitchison-Jozsa 反事实计算 / Salih counterfactual 通信 / Filatov-Auzinsh 多对象)
- 实验实现 ✅ (桌面 / 集成芯片 / 冷原子 / x-ray / 多平台)
- 形式化 ✅ (Lin-Lin bomb query complexity · Pearl-style 因果反事实)
- 算法应用 ⚠️ (零星案例 · 没有统一框架)
- **抽象-工程-应用框架** ❌ (**空白** · 这是本论文要填的空)

我们处在 IFM 跨越 "physics demo" 阶段进入 "engineering primitive" 阶段的临界点。本论文的目标是提供这一阶段需要的抽象。

## 2.7 · 跟最近活跃工作的关系 (2024-2025)

| 工作 | 跟本论文关系 |
|---|---|
| [Franco-Camillini-Galvão 2026] · Multi-object IFM on integrated chip | **直接对应本文 §3 单算子的物理实现** · 我们抽象的算子他们做了物理实现 |
| [Filatov-Auzinsh 2024] · Setup for multi-object IFM | **本文 §3 算子的物理协议来源** |
| [Shwartz 2025] · x-ray IFM | 扩展物理 platform · 跟本文正交 (我们不限定波长) |
| [Quantum causal counterfactuals 2024] | 不同范畴 (因果推断 vs 计算原语) · 不冲突 |
| [Coherent IFM theory 2023] · arxiv 2307.05214 | 三级系统 IFM 数学 · 跟本文 §3 的算子定义兼容 · 可作为底层物理实现之一 |

## 2.8 · 本论文 vs 30 年文献的差异化定位

**已有**:

- ✅ 物理协议 (单 bomb / 多 bomb / Zeno / 通信)
- ✅ 实验实现 (多平台多波长)
- ✅ 复杂度形式化 (bomb query)
- ✅ 因果反事实 (Pearl-style · 不同范畴)

**没有 · 本论文填补**:

- ❌ → ✅ 算子抽象 (统一接口 · 不必懂物理)
- ❌ → ✅ 组合代数 (5 种组合 + cost 定理)
- ❌ → ✅ 跟 FT QC 的 3 维系统对比
- ❌ → ✅ 命名的范式 (Subtractive Computation Paradigm)
- ❌ → ✅ 多维复杂度框架 (引入 disturbance + observability)
- ❌ → ✅ 6 个算法模板
- ❌ → ✅ 应用代数化方法论 (5 步 SOP + 决策树)
- ❌ → ✅ 6 个可挑战 FT QC 问题的具体清单

本论文不发明新物理 · 但建立**第一个完整的算法-工程-应用框架** · 把 30 年物理工作转化为算法学家与行业工程师可直接调用的工具集。

## 2.7 · PhD-level synthesis + critical reviews (2023-2025)

(本节 2026-06-20 audit 加入 · 跟 audit/batch-11-physics-via-phd-thesis-and-critical-review 对接)

### 完整 PhD thesis 综述

**[Hance PhD thesis 2023]** Jonte R. Hance · "The interplay between quantum foundations and quantum technologies: Counterfactual communication, and extensions of quantum mechanics" · University of Bristol Doctoral College · 2023-03-21 · supervisor James A C Ladyman + John Rarity · Handle.net: hdl.handle.net/1983/a3cf0e59-31a9-456f-800e-cd3b6533461b

7 章 PhD-level synthesis · 涵盖 IFM + counterfactual communication (CFC) + extensions of quantum mechanics + philosophical/foundational issues。**是我们论文 §02 + §03 + §15 内容的 PhD-level reference 综述。** Hance 个人贡献 (Calafell 2019 + 多篇 follow-up) 都收录。

**[Violaris DPhil thesis 2025]** "Counterfactuals in macroscopic quantum physics: irreversibility, measurement and locality" · University of Oxford Mathematical Institute · 2025-05-20 · supervisors Vlatko Vedral + Artur Ekert · examiners David Deutsch + Gerardo Adesso

用 **constructor theory** (Deutsch-Marletto) 框架研究 quantum counterfactuals · 提供我们 §05 D3 论证 (CFE 跟 FT QC categorical 差异) 的 formal foundation。

### 关键 critical paper (must-engage)

**[Frumkin-Bush 2023]** Valeri Frumkin · John W. M. Bush · "Misinference of interaction-free measurement from a classical system" · Phys. Rev. A 108, L060201 (2023-12-12) · DOI 10.1103/PhysRevA.108.L060201

**关键 challenge claim**:在 hydrodynamic pilot-wave 系统 (walking droplet on 7 mm silicon oil at 80 Hz vibration) 上实测 · droplet 25% detection statistics 跟 EV 量子 IFM 25% 等价。论证 single bomb tester 规模的 IFM **可以用经典 pilot-wave 描述** · 不严格 quantum-only。

我们 §03.7 R1/R2/R3 differentiator claim 已加 caveat 跟此 paper align (§11.2 CAVEAT 6)。**重要**:Frumkin-Bush 实测仅限 single bomb tester · 不能 reproduce chained Zeno (Kwiat 1995) 或 multi-object IFM (Franco 2026) · 我们应用 niche 在后者规模 · 论点 not affected。

**[Bush 2021]** John W. M. Bush · "Pilot-wave hydrodynamics" review · Rep. Prog. Phys. 84:017001 (2021)

综述 经典 pilot-wave 系统已模拟的 quantum 现象:single/double-slit · orbital quantization · wavelike statistics in corrals · Friedel oscillations · superradiance · spin lattices · surreal Bohmian trajectories · IFM (Frumkin-Bush 2023)。Bush 综述说明 hydrodynamic analog 在 **finite memory + finite spatial extent** 下 work · 跟量子的 arbitrary scale nonlocal wavefunction 是 fundamental 差异。

### 支持我们 R1/R2/R3 论点的 paper

**[Hance-Ladyman-Rarity 2021]** "How Quantum is Quantum Counterfactual Communication?" · Foundations of Physics 51:12 (2021) · arxiv 1909.07530 · DOI 10.1007/s10701-021-00412-5

verbatim:**"the protocols proposed so far for sending signals that don't involve matter/energy transfer associated with the bits sent must be quantum, insofar as they require wave-particle duality."**

支持我们 §03.7 differentiator 论点 · 至少在 counterfactual communication protocol 规模上 R1 必需 quantum。

### 综合 implication

5 个新 source 跟我们 §02 既有 30 年文献链互补:

- 既有 sources 给**单独 paper-level** 文献 (1993 EV → 2026 Franco)
- 新加 sources 给 **PhD-level synthesis + critical/foundational review** 视角
- Frumkin-Bush 2023 critical paper 必 engage · 已在 §03.7 + §11.2 加 caveat

完整审计落档见 `audit/batch-11-physics-via-phd-thesis-and-critical-review.md`。

---

[← 上一章 · 01 引言](01-introduction.md) · [下一章 · 03 算子形式定义 →](03-operator-formal-definition.md)
