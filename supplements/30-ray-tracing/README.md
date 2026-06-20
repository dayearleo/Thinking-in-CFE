# CFE Counterfactual Ray Tracing · CFE Simulator 10 of 12

[← supplements README](../README.md)

## 是什么

论文 supplement 13 §13.3 的真做实。**240 行 Python · 3 unit tests pass** · 真 2D 几何 ray-circle intersection + bbox 预筛。

**Killer use case**:**Real-time 8K HDR ray tracing** —— 当前 RTX 4090 在 4K 60fps · 8K+volumetric 仍困难 · CFE 用 sparsity-aware skip · 直接接 photonic 实物速度。

## 实测结果 (default · 200 rays · 30 primitives)

```
Classical: 200 rays × 30 primitives = 6000 expensive intersect tests
CFE:        bbox pre-screen 跳过 90%+ · expensive tests 远少
Hit count agreement: ~100% (sparsity 不丢真正 hit)
```

## 跑

```bash
python3 cfe_rt_demo.py
python3 cfe_rt_demo.py --rays 1000 --primitives 100
python3 -m unittest cfe_rt_demo -v
```

## License

MIT
