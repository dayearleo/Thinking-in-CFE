# CFE Counterfactual Sparse SpMV · CFE Simulator 11 of 12

[← supplements README](../README.md)

## 是什么

论文 supplement 13 §13.4 的真做实。**217 行 Python · 4 unit tests pass** · 真 sparse matrix-vector multiplication + cheap row screen + bit-identical correctness。

**Killer use case**:**Real-time 3D PDE solver** —— 天气预报 / 油气勘探 / EM 仿真 用 SpMV-heavy iterative solver · 当前 GPU 受 memory bandwidth 限 · CFE photonic in-mesh compute 突破 memory wall。

## 实测结果 (default · 100×100 matrix · 10 active rows · 20% density)

```
Classical SpMV: iterate 全 100 rows (含 90 空 row)
CFE SpMV:       pre-screen 跳 90 空 row · 仅算 10 active rows
Output:         bit-identical to classical (zero numerical error)
Op reduction:   ~10x (= n / n_active)
```

## 跑

```bash
python3 cfe_spmv_demo.py
python3 cfe_spmv_demo.py --n 500 --active-rows 50 --density 0.3
python3 -m unittest cfe_spmv_demo -v
```

## License

MIT
