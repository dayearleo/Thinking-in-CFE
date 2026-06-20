# Differential Cryptanalysis Rate-Limit Bypass · CFE Simulator 3 of 5 in this batch

[← supplements README](../README.md)

## 是什么

论文 §17.4.3 + dev-notes/013 的真做实。**270 行 Python · 6 unit test 全 pass · 真 8-round Feistel cipher (16-bit key/block)** · 实际差分密码分析跑通。

**Killer use case**:**短 key cipher 在 cloud deployment 下被破** —— 经典差分受限于 cipher service rate limit · 灌不进 chosen plaintext;CFE 反事实查询不计入 rate limit · attack 完成。

## 实测结果 (default · 2000 pairs · rate limit 500)

```
Classical: 250 / 2000 pairs · LOCKED at pair 250 · cipher service 500 audit log entries
CFE:       2000 / 2000 pairs · NOT locked · 0 audit log entries
CFE completes 8x more pairs without triggering lock
```

CFE 让 Cloud-deployed 短 key cipher 的 differential analysis 从 "rate-limit 阻断" 变成 "完整可跑"。

## 跑

```bash
python3 cfe_diff_demo.py
python3 cfe_diff_demo.py --queries 5000 --rate-limit 1000
python3 -m unittest cfe_diff_demo -v
```

## License

MIT
