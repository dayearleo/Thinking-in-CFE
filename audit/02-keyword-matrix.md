# 02 · 关键词矩阵 + 搜索工具 curl 模板

> 本文件 = `00-master-plan.md` §3 + §4 的执行版速查 · 给 AI 跑搜索时直接抄 verbatim
> 维度 7 (攻击场景) 是 §3 之外补的 · 防 R2 stealth 类应用漏检

---

## 0 · 三引擎 API key (已 verified · 可直接用)

| 引擎 | endpoint | key |
|---|---|---|
| EXA | `https://api.exa.ai/search` | `${EXA_API_KEY}` |
| Serper | `https://google.serper.dev/search` | `${SERPER_API_KEY}` |
| Jina | `https://r.jina.ai/<url>` | `${JINA_API_KEY}` |

详 `~/.claude/skills/search-tools/references/full-sop.md`。

---

## 1 · curl 调用模板 (直接复制可跑)

### EXA · 语义 + 学术

```bash
curl -sS -X POST "https://api.exa.ai/search" \
  -H "x-api-key: ${EXA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "<KEYWORD>",
    "num_results": 10,
    "type": "auto",
    "contents": {"text": {"max_characters": 1500}}
  }' | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f\"- {r.get('title','?')}\n  {r.get('url','?')}\n  {r.get('text','')[:300]}\n\") for r in d.get('results',[])]"
```

### Serper · Google + Scholar

```bash
curl -sS -X POST "https://google.serper.dev/search" \
  -H "X-API-KEY: ${SERPER_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"q": "<KEYWORD>", "num": 10}' | python3 -m json.tool | head -80
```

Scholar 子端点:`https://google.serper.dev/scholar`

### Jina · 抓页面全文 (markdown 化)

```bash
curl -sS -H "Authorization: Bearer ${JINA_API_KEY}" \
  "https://r.jina.ai/<URL>" | head -200
```

### arxiv 直 API · EXA 漏新 paper 时

```bash
curl -sS "http://export.arxiv.org/api/query?search_query=all:<KEYWORD>&max_results=10&sortBy=submittedDate&sortOrder=descending" | python3 -c "
import xml.etree.ElementTree as ET, sys
root = ET.fromstring(sys.stdin.read())
ns = {'a':'http://www.w3.org/2005/Atom'}
for e in root.findall('a:entry', ns):
    print(f\"- {e.find('a:title', ns).text.strip()}\")
    print(f\"  {e.find('a:id', ns).text}\")
    print(f\"  {e.find('a:summary', ns).text[:300].strip()}\")
    print()
"
```

---

## 2 · 6 维关键词矩阵 (按主题分块 · 双语)

### 维度 1 · 算子定义 / 反事实计算 (主语义场)

**英文**:

- `counterfactual quantum computation`
- `counterfactual function evaluation`
- `interaction-free measurement IFM`
- `Elitzur-Vaidman bomb tester`
- `Mitchison Jozsa counterfactual computation 2001`
- `Hance counterfactual photonic chip 2025`
- `multi-object IFM`
- `Filatov Auzinsh multiple object 2024`
- `generalized delayed-choice multi-path`
- `Wheeler delayed choice integrated photonic`

**中文**:

- `反事实量子计算`
- `干涉无相互作用测量`
- `Elitzur-Vaidman 炸弹检测`
- `量子反事实`
- `延迟选择实验 集成`
- `多路反事实测量`

### 维度 2 · 复杂度 / 算法

**英文**:

- `bomb query complexity Lin Lin 2015`
- `bomb query model quantum`
- `quantum query complexity Q(f)`
- `NAND tree quantum walk Farhi Goldstone Gutmann 2008`
- `Childs Cleve Jordan Yonge-Mallo NAND tree 2009`
- `read-once Boolean formula quantum`
- `Grover algorithm counterfactual variant`
- `Reichardt Boolean formula evaluation`
- `span program quantum algorithm`

**中文**:

- `量子查询复杂度`
- `炸弹查询模型 林`
- `NAND 树 量子游走 Farhi`
- `Grover 反事实`
- `Boolean 公式 量子算法`

### 维度 3 · 物理硬件 / 集成光子

**英文**:

- `integrated photonic processor`
- `universal photonic chip 12 mode`
- `MZI mesh nanophotonic`
- `Mach-Zehnder interferometer integrated 8 port`
- `SNSPD single photon detector efficiency`
- `AIM Photonics multi-project wafer`
- `LioniX programmable photonic`
- `Imec photonic foundry`
- `silicon nitride SiN photonic loss`
- `electro-absorption modulator switchable`
- `single photon source heralded SPDC`
- `quantum dot III-V integrated`

**中文**:

- `集成光子处理器`
- `多路马赫-曾德尔 N=8`
- `光子神经网络`
- `光子芯片 可编程`
- `氮化硅光子`
- `单光子探测器 SNSPD 效率`
- `量子点 III-V 集成`

### 维度 4 · 密码学 / HSM / 工业部署

**英文**:

- `HSM hardware security module tamper evidence`
- `tamper-evident encryption Gottesman 2003`
- `quantum tamper evident encryption`
- `Wiesner quantum money state`
- `quantum side channel HSM`
- `Common Criteria EAL 4+ tamper`
- `FIPS 140-3 Level 4 physical security`
- `Post-Counterfactual cryptography PCC`
- `quantum probe smart card`
- `Can't Touch This Skoric unconditional tamper evidence`
- `proofs of no intrusion Goyal Raizes 2025`
- `certified deletion quantum`
- `harvest now decrypt later HNDL`

**中文**:

- `硬件安全模块 抗篡改`
- `量子侧信道`
- `量子擦除加密 Gottesman`
- `量子货币 Wiesner`
- `量子密钥分发 BB84`
- `先收集后解密 HNDL`

### 维度 5 · 范式 / 新计算模型 (防 novelty 撞名)

**英文**:

- `subtractive computation`
- `subtractive algorithm paradigm`
- `negation as computation`
- `counterfactual programming language`
- `interaction-free algorithm framework`
- `algorithmic skepticism paradigm`
- `pruning based computation model`
- `non-evaluation oracle algorithm`

**中文**:

- `减法计算`
- `反事实算法范式`
- `否定计算`
- `修剪计算模型`
- `非求值算法`

### 维度 6 · 应用 / 12 simulator 对应 niche

| simulator | 英文关键词 | 中文关键词 |
|---|---|---|
| 10 HSM tamper | `quantum HSM side channel`, `tamper bypass photonic`, `HSM key extraction quantum` | `HSM 旁路 量子`, `HSM 密钥提取` |
| 14 Bloom PIR | `quantum PIR private information retrieval`, `physical layer PIR`, `Bloom filter quantum` | `物理层 PIR`, `布隆过滤器 量子` |
| 16 Universal HW | `cross-device hardware root of trust attack`, `TPM passport ECU common vulnerability`, `universal hardware tamper` | `硬件根信任 跨设备攻击`, `TPM 篡改` |
| 18 Graph reach | `stealth network reconnaissance quantum`, `counterfactual graph traversal`, `silent network probe` | `量子隐蔽网络扫描`, `静默网络探测` |
| 20 Differential | `differential cryptanalysis rate limit bypass`, `cloud cipher quantum probe`, `Feistel differential attack stealth` | `差分密码分析 cloud bypass`, `云端密码学 速率限制` |
| 22 Federated | `federated learning quantum privacy`, `counterfactual gradient`, `physical layer privacy preserving ML` | `联邦学习 量子隐私`, `反事实梯度` |
| 24 Monte Carlo | `quantum Monte Carlo expensive simulation`, `counterfactual sampling`, `IFM materials simulation` | `量子蒙特卡洛 反事实采样`, `IFM 材料模拟` |
| 26 Abstract interp | `quantum SMT solver`, `counterfactual abstract interpretation`, `compiler verification quantum oracle` | `量子 SMT 反事实抽象解释`, `编译器 形式验证` |
| 28 Attention | `quantum sparse attention transformer`, `100M context CFE`, `photonic accelerator attention` | `量子稀疏注意力 transformer`, `光子加速 注意力` |
| 30 Ray tracing | `quantum ray tracing photonic accelerator`, `8K HDR counterfactual`, `photonic graphics primitive` | `光子加速 光线追踪`, `光子图形原语` |
| 32 SpMV | `photonic sparse matrix vector multiplication`, `quantum PDE solver`, `photonic in-memory compute` | `光子稀疏矩阵向量`, `光子内存计算 PDE` |
| 34 Smith-Waterman | `quantum sequence alignment`, `genomic Smith Waterman photonic`, `IFM cancer variant detection` | `光子基因组比对 SW`, `IFM 癌症变异检测` |

### 维度 7 · 攻击场景 (R2 stealth 类应用)

**英文**:

- `stealth probing`
- `non-trigger sensor probing`
- `quantum reconnaissance`
- `silent observation quantum`
- `adversary-undetectable measurement`
- `passive quantum sensing`
- `quantum honey token`
- `IAEA seal counterfactual`

**中文**:

- `无触发探测`
- `量子静默观察`
- `对手不可察觉测量`
- `IAEA 封装 反事实`

---

## 3 · 时间窗口 + 语言策略

每 claim **必跑 4 个 search batch**:

1. 英文 全时段:`<keyword>`
2. 英文 近 12 月:`<keyword>` + filter `after:2024-12` (Serper) 或 `published_date>=2024-12` (EXA)
3. 中文 全时段:`<中文 keyword>`
4. 中文 近 12 月:`<中文 keyword> 2025`

漏任一 batch · audit 不算完整。

---

## 4 · 引用 + 抓取规范

### 抓 source 全文时:

- Jina 拉 markdown · 存 `audit/claims/AUD-XXX/sources/<n>-<short-id>.md`
- 文件名格式:`<rank>-<author-year-keyword>.md` 例:`01-mitchison2001-counterfactual.md`
- 文件内含原 URL + 抓取时间戳 + 关键段落 markdown

### 引用格式:

paper 章节里引用 audit 结论时:

```markdown
[审计 AUD-C02-003 · CONFIRMED ⭐⭐⭐⭐⭐]
```

或 long form:

```markdown
本节关于 Mitchison-Jozsa 2001 counterfactual computation 的归属经
[`audit/claims/AUD-C02-003/assessment.md`] CONFIRMED · 跟 [Mitchison 2001 PRA]
原文一致。
```

---

## 5 · 工作 cache

`audit/sources-cache/` 是 cross-claim 共享缓存:

- 多个 claim 引同一篇 paper 时 · 只抓 1 次 · symlink 到各 claim 的 sources/
- 命名规则:`<arxiv-id>.md` 或 `<doi-slug>.md`

例:`audit/sources-cache/lin-lin-2015-bomb-query.md` 可被 10+ 个 C 类 claim 共用。

---

## 6 · 反模式 (搜索时禁碰)

- ❌ 只跑英文不跑中文 (维度 6 应用 niche 多在中文社区)
- ❌ 只跑全时段不跑近 12 月 (漏 2024-2025 活跃年关键文献)
- ❌ Jina 抓的 markdown 不保存到 sources/ (压缩边界后丢)
- ❌ 凭印象 "我之前搜过" 跳过查询 (claim 间证据 sharing 必走 sources-cache · 不是凭脑回放)
- ❌ 一次 search 只看 top 3 结果 (top 10 必扫 · 漏长尾)
- ❌ 撞 rate limit 直接 abort (走降级链 EXA → Serper → arxiv API → Jina)

---

## 7 · 版本

- 2026-06-20 v1 初版 · 复制自 plan §3 + §4 · 扩展 7 维 + curl 模板 + 引用规范
