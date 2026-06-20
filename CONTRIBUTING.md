# 贡献指南 · Contributing to Thinking in CFE

本论文是 **开放 RFC** (Request for Comments) · 详 `thinking-in-cfe/13-validation-and-rfc.md`。我们邀请所有学界 / 工程界 / 行业人士参与改进。

## 贡献方式 (按门槛排)

### 1 · 简单 typo / 表达修正 (Pull Request)

直接 fork → 修改 → 提 PR。我们尽快 merge。

### 2 · 论文内容讨论 (Issue)

- 对某具体声明的质疑 → 开 Issue · 标 label `claim-challenge`
- 对引用文献的补充 → Issue · label `reference-addition`
- 对术语 / 命名的建议 → Issue · label `terminology`

### 3 · 严肃证伪 / 反证 (Issue + 附件)

如果你认为论文某声明可以被严格证伪:

- 开 Issue · 标 label `falsification`
- 附 (a) 被证伪的具体声明 (引用章节 + 段落) · (b) 反证论证 · (c) 任何必要的数学 / 实验证据
- 我们承诺 (per `13-validation-and-rfc.md` §13.6):
  - 任何严格证伪 · 在论文 next version 中明确撤回 + 标注证伪者
  - 公开 review · 不闭门审稿
  - 版本控制 · 每次 substantive 修改打 git tag

### 4 · 扩展贡献 (新章节 / 新案例 / 新算法模板)

如果你想加新内容 (例如新算法模板 / 新应用领域 / 新攻击案例):

- 先开 Issue 讨论 · label `proposal`
- 跟 maintainer 对齐 scope + 风格
- 然后提 PR

### 5 · 实验复现 (Experiment Reports)

如果你在自己 lab 复现了论文某 worked example:

- 开 Issue · label `experiment-report`
- 附 (a) 复现的具体声明 · (b) 实验 setup · (c) 数据 · (d) 偏差或确认
- 我们在论文中引用你的复现 (per §13.6)

## 不接受的贡献

- 纯 hype / 营销内容 · 不含技术 substance
- 重复已 covered 的内容 · 没有新角度
- 商业 endorsement / 厂商广告
- 未署名 / 匿名 substantive 修改

## 双 license 提醒

- 文本贡献 → 自动归 CC BY 4.0 (你的署名保留)
- 代码贡献 → 自动归 MIT (你的版权保留)
- 详 `LICENSE.md`

## RFC 路线图

论文当前 v0.1 draft。重要里程碑:

- **v0.2** · 集成 first batch of community feedback · 计划在初稿发布后第一轮 review cycle 后
- **v0.5** · 加 worked experiment reports · 计划在第一个独立实验复现后
- **v1.0** · 通过 peer review · 投递到 conference / journal · 时间不定

## 联系

- GitHub Issues · 主要沟通渠道
- 邮箱 · `[TBD · 论文正式发布时填写]`
- 学术合作邀请 · 通过 Issue 联系 maintainer

## 行为准则

简单两条:

1. 对人 polite · 对论 ruthless
2. 引用要严格 · cite or it didn't happen
