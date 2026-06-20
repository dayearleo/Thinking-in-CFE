# 03 · HSM 厂商特定披露段 · 4 个示例

[← supplements README](README.md)

## 文件性质

跟 `02-hsm-disclosure-template.md` 配套 · 给 4 个主要 HSM / Secure Element 厂商的**特定段落**草案。实际发送前必须由作者本人 + 法律顾问 review。

**重要 disclaimer**:

- 本文是 **draft** · 没有任何形式的法律 binding
- 厂商产品名 / 型号基于公开信息 · 可能有 inaccuracy
- 实际披露应基于最新公开产品 spec · 不基于过时信息

## 1 · Thales (Luna HSM · payShield · CipherTrust)

**给 Thales Security Team 的特定段**:

> Thales 的 Luna HSM 系列 (FIPS 140-3 Level 3+) 是 financial services · government PKI · enterprise key management 的主要 HSM 供应商之一。payShield 系列被全球大量银行用于 PIN translation 和 EMV transaction processing。CipherTrust Manager 集中管理跨 HSM 的密钥生命周期。
>
> 我们论文的 §16.6.1 (AES-256 in HSM 反事实提取) 和 §16.6.2 (银行 PIN 反事实暴力破解) 直接 affect 这些产品的核心 use case:
>
> - **Luna HSM**:存储 AES / RSA / ECC 长期密钥 · CFE attack 提取这些密钥让 HSM 物理保护失效 · 已加密历史数据全部 retrospectively 暴露
> - **payShield**:验证 4-6 digit 银行 PIN · CFE attack 绕过 attempt counter · PIN 系统完全失效
> - **CipherTrust**:作为 root of trust manager · 若任一被管 HSM 被 CFE 攻陷 · 跨 region 密钥生命周期完整性丢失
>
> 我们特别关注:
>
> 1. Luna 7 系列对**侧后访问 (backside access)** 的物理防御 (mesh + epoxy) 是否考虑 photonic / EM IFM probe?
> 2. payShield 对**PIN verification 频率统计**是否有 anomaly detection · 还是仅靠 attempt counter (counter 可被 CFE 旁路)?
> 3. CipherTrust 是否有 **MPC-based 多 HSM 拆分**模式 · 让单 HSM 被 CFE 攻陷不导致 root key 流出?
>
> 我们建议 Thales review the paper §16 + §15 · 并考虑加入 PCC (Post-Counterfactual Cryptography · supplement 01) founder pool。

## 2 · Utimaco (CryptoServer · u.trust 系列)

**给 Utimaco Security Team 的特定段**:

> Utimaco 的 CryptoServer 系列在欧洲银行 / 政府 / 关键基础设施市场份额突出。u.trust General Purpose HSM Se / CSe 系列覆盖 telecom · enterprise · sovereign cloud 场景。
>
> 我们论文的 §16.6.1 直接 affect:
>
> - **CryptoServer Se 系列**:存储 long-term master key · CFE 提取后 · derived session keys 全部可计算
> - **u.trust General Purpose HSM**:多 tenant 共享 HSM 环境 · 一个 tenant 的 key 被 CFE 提取后 · 其他 tenant 是否也曝光?(物理 isolation 是否抗 CFE?)
>
> 我们特别关注:
>
> 1. CryptoServer 的 **physical security mesh** 设计是否考虑 quantum 物理 probe 的 R2 性质?
> 2. u.trust 的 multi-tenant isolation 是物理 isolation 还是 logical isolation · 后者在 CFE 下不充分
> 3. Utimaco 是否有 **post-quantum migration** roadmap · 该 roadmap 是否包含 PCC 维度?
>
> Utimaco 作为欧洲 sovereignty 重要 vendor · CFE 威胁的 narrative 跟 EU 数字主权契合 · 可能成为 PCC standardization 的 EU 旗手。我们建议 Utimaco 考虑 leadership role。

## 3 · Entrust (nShield HSM · Identity & Access)

**给 Entrust Security Team 的特定段**:

> Entrust 收购 nCipher 后整合的 nShield HSM 系列覆盖 enterprise PKI · CA signing key 保护 · TLS termination acceleration · cryptocurrency custody 等。Entrust Identity 平台依赖 HSM-backed certificate signing。
>
> 我们论文的 §16.6.1 + §16.6.3 (SHA-1 HMAC key 提取) 直接 affect:
>
> - **nShield Connect / Solo / Edge**:存储 CA root signing key · CFE 提取后 · 攻击者可任意签发 forged certificates · 整个 PKI trust chain 崩塌
> - **legacy SHA-1 HMAC** in old Entrust products · CFE 提取 HMAC key 后 · SHA-1 已知数学弱点立即可用 · message integrity 完全失效
>
> 我们特别关注:
>
> 1. nShield 对 root CA signing key 的 ** physical isolation 设计**是否考虑长时间 (天 / 周级) photonic IFM probing?
> 2. Entrust 的 customer base 是否有清单 · 哪些 customer 的 root CA 在 nShield 中存储 · 受影响范围?
> 3. 如果 root CA 被泄露 · Entrust 的 **emergency revocation + re-keying** SOP 是否足够快?
>
> Entrust 作为 global PKI 重要 anchor · CFE 威胁对其 customer trust 极大。我们建议高优先级 review。

## 4 · AWS CloudHSM (cloud-based HSM)

**给 AWS Security 的特定段**:

> AWS CloudHSM 提供 cloud-based dedicated HSM (基于 third-party 硬件 · AWS-managed)。它跟 KMS 互补 · CloudHSM 用于 customer 完全控制 key material 的场景 (法规要求 / 高安全需求)。
>
> 我们论文 §16 的 CFE 攻击对 cloud HSM 有**特殊适用**:
>
> - **物理访问**:AWS data center 物理安全严格 · 但**内部威胁 (恶意 employee · supply chain interception)** 仍有理论可能 · CFE attack 让物理访问后的 stealth key 提取变得可行
> - **multi-tenancy**:CloudHSM 是 dedicated 模式 · 但**共享 facility** · 如果攻击者 compromise 数据中心物理层 · 多 customer 同时 affected
> - **legal jurisdiction**:某些 customer 选择 CloudHSM 因为 customer-controlled key · 但 CFE 让 "customer-controlled" 假设受质疑 · sovereign-data 客户特别关心
>
> 我们特别关注:
>
> 1. CloudHSM 使用的硬件 (Marvell / Cavium) 是否有 CFE 评估?
> 2. AWS 是否对 internal 员工 unauthorized physical access HSM 有 detection 措施 (除了 audit log · 因为 CFE 不留 audit)?
> 3. AWS Nitro System 跟 CloudHSM 集成层是否引入新 CFE attack surface?
> 4. AWS KMS (HSM-backed) 用的硬件是否同样受影响?
>
> AWS 作为 cloud security 行业 leader · 公开 PCC review 会引领 industry。我们建议 AWS Security Engineering 考虑设立 PCC research stream。

## 5 · 通用建议给所有 4 个厂商

### 5.1 · 短期 (响应阶段)

- 确认收件 + 内部 assessment 启动
- 给 author team 一个 single point of contact
- 协调 90-day grace period

### 5.2 · 中期 (评估阶段)

- 内部模拟 CFE attack scenario (即使 lab 上不实施 · 也 model)
- 评估现有产品 line 的 CFE 风险等级
- 评估 customer base 的 exposure
- 制定 communication plan (跟 customer 怎么说)

### 5.3 · 长期 (response 阶段)

- Roadmap CFE-resistant 产品 line
- 加入 PCC standardization (supplement 01)
- 跟 NIST / ISO 协作 PCC certification 标准
- 长期 review 投入 vs 营收 (CFE 威胁可能催生新 cert level 市场)

## 6 · 给 author team 的注意事项

发送前 checklist:

- [ ] 法律顾问 review (避免任何隐含 product accusation)
- [ ] PGP key 准备好 (厂商 PSIRT 需要 encrypted channel)
- [ ] 同时给多家厂商发 · 但**单独**通信 · 不要 cross-reference
- [ ] 保留所有发送 timestamp
- [ ] 不要先在 social media / blog 提及 · disclosure 前保持低调
- [ ] 准备 grace period 内的 holding statement (媒体或被泄漏时用)
- [ ] coordinate with academic mentors / institution legal · 走 institutional disclosure 通道更稳

## 7 · 跟之外厂商的 expansion 计划

本文档只 cover 4 个 sample 厂商。完整 disclosure 应 expansion 至:

- IBM (z-system HSM / IBM Cloud HSM)
- Microsoft (Azure HSM · Pluton 集成 chip)
- Google (Titan Security Key · Google Cloud HSM)
- Yubico (YubiKey · 用 secure element)
- Ledger / Trezor (hardware wallet)
- Infineon (TPM · smart card)
- ST Microelectronics (smart card · secure element)
- NXP (smart card · automotive secure element)
- Apple (Secure Enclave Processor)
- Samsung (Knox · 移动 secure element)
- 中国厂商 (海光 · 国密 HSM)

每个厂商按 02 模板 + 本文档段落 customize。

## License

CC BY 4.0 · 详 paper root `LICENSE.md`
