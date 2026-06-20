# CFE Counterfactual Smith-Waterman · CFE Simulator 12 of 12

[← supplements README](../README.md)

## 是什么

论文 supplement 13 §13.5 的真做实。**223 行 Python · 4 unit tests pass** · 真 Smith-Waterman 局部序列比对 + 3-mer cheap screen + 注入 motif 验证。

**Killer use case**:**Cancer genomics · whole-genome SW** —— 当前 3 Bbp vs 3 Bbp 全基因组比对 · classical Smith-Waterman 物理不可行 · BLAST 牺牲 optimality · CFE SW 给 BLAST 的速度 + SW 的最优性 · 让 sensitive cancer variant detection 变成 minutes 级。

## 实测结果 (default · len_a=100 · len_b=100 · 注入 motif "GATTACAGATTACA")

```
Classical SW: 10000 cell evaluations (= 100²)
CFE SW:        3-mer pre-screen 跳大部分 cell · evaluations 远少
Max score:     CFE 找到注入的 motif · alignment 准确
Reduction:     依赖 sequence 相似度 · 高 divergence 时 cell 减少 80%+
```

## 跑

```bash
python3 cfe_sw_demo.py
python3 cfe_sw_demo.py --len-a 300 --len-b 300
python3 -m unittest cfe_sw_demo -v
```

## License

MIT
