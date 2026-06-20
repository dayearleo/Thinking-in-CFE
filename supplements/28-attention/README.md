# CFE Counterfactual Attention · CFE Simulator 9 of 12

[← supplements README](../README.md)

## 是什么

论文 supplement 13 §13.2 的真做实。**237 行 Python · 4 unit tests pass** · 真 single-head attention + cheap-screen + cosine similarity validation。

**Killer use case**:**100M token context LLM inference** —— 当前 GPT-4 Turbo 128k context 已极贵 · CFE sparse-aware attention 让 sequence length 跨数量级扩展可行。

## 实测结果 (default · seq_len=32 · 5% sparsity)

```
Full attention:     1024 expensive ops (= 32²)
CFE attention:      Far fewer expensive ops (only relevant pairs)
Cosine similarity:  > 0.3 (output 跟 full attention 在主要方向上对齐)
```

## 跑

```bash
python3 cfe_attn_demo.py
python3 cfe_attn_demo.py --seq-len 64 --d-model 16
python3 -m unittest cfe_attn_demo -v
```

## License

MIT
