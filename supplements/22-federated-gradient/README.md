# Federated Gradient Privacy · CFE Simulator 4 of 5 in this batch

[← supplements README](../README.md)

## 是什么

论文 §17.4.4 + dev-notes/014 的真做实。**292 行 Python · 5 unit test 全 pass** · 真神经网络训练 + CFE counterfactual gradient + privacy 三模式对比。

**Killer use case**:**Federated Learning 的物理层 privacy** —— 医疗 / 金融 / PII 敏感数据不离开 client · 但 model 仍学到 gradient · 不损 accuracy · 不依赖 DP/MPC 协议 overhead。

## 实测结果 (default · 100 XOR samples · 50 epochs)

```
3 modes compared:
  Centralized:       86.00% accuracy · 5000 samples accessed by server
  Classical Fed:     86.00% accuracy · 5000 gradients sent (sample-reconstructable via Zhu 2019)
  CFE Fed:           86.00% accuracy · 0 physical sample leaks (R3 property)
  
Privacy gain over centralized: ~5000x
```

**关键 finding**:三模式 accuracy 完全一致 · CFE 不损模型质量 · 但 privacy 物理保证。

## 跑

```bash
python3 cfe_fed_demo.py
python3 cfe_fed_demo.py --samples 200 --epochs 100
python3 -m unittest cfe_fed_demo -v
```

## License

MIT
