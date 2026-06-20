# Graph Reachability Stealth Probe · CFE Simulator 2 of 5 in this batch

[← supplements README](../README.md)

## 是什么

论文 §17.4.2 + dev-notes/012 的真做实。**235 行 Python · 4 unit test 全 pass**。

**Killer use case**:**stealth network topology mapping** —— 攻击者扫描对手网络可达性 (host A→B 是否通) · 经典 BFS 每次 edge probe 在目标端 log · CFE 反事实可达性测试 · 目标端**0 log entry**。

## 实测结果 (default · 30 节点 · density 0.15 · 500 queries)

```
Classical BFS accuracy: 100.00%       CFE Reachable accuracy: 99.80%
Classical detected:     488 / 500     CFE detected:           0 / 500
Detection reduction:    ~490x
```

## 跑

```bash
python3 cfe_reach_demo.py
python3 cfe_reach_demo.py --nodes 50 --density 0.1 --queries 1000
python3 -m unittest cfe_reach_demo -v
```

## License

MIT
