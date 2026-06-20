# CFE Abstract Interpretation · SMT Cost Saving · CFE Simulator 8 of 12

[← supplements README](../README.md)

## 是什么

论文 supplement 13 §13.1 的真做实。**220 行 Python · 6 unit tests pass**。

**Killer use case**:**Cloud SMT-as-a-Service 成本节省** —— 编译器 / 形式验证大量调用 Z3/CVC5 cloud · 按 query 收费 · CFE 反事实查询不计费 · 节省 99%+ cost。

## 实测结果 (default · 200 programs · SMT budget 100)

```
Classical: 33 / 200 programs analyzed · SMT budget exhausted at #33 · cost $0.50
CFE:       200 / 200 programs analyzed · 0 actual SMT triggered · cost $0.00
```

CFE 让大规模程序分析在 rate-limited SMT service 下变成可行。

## 跑

```bash
python3 cfe_ai_demo.py
python3 -m unittest cfe_ai_demo -v
```

## License

MIT
