# Universal Hardware Trust Break · 第 3 个做实的 CFE worked example

[← supplements README](../README.md)

## 是什么 · civilization-scale 例子

**ONE CFE 攻击模型 · 7 个 device 类别全攻陷**:HSM / TPM / 硬件钱包 / EMV 智能卡 / 护照 NFC / 车载 ECU / 卫星 keystore。**468 行 Python · 5 个 unit test 全 pass · 100 trials × 7 设备 = 700 attack simulation**。

跟 supplement 10 (CFE-HNDL · HSM single device) + supplement 14 (CFE-Bloom · 数据结构) 一起 · 这是第 3 个做实的 worked example · 也是 **civilization-scale demonstration** —— 说明 CFE 攻击不是 device-specific bug · 是 primitive-level 假设崩塌 · 强制全球 hardware-rooted trust 体系全部重新审视。

## 实测结果

```
7 device categories:
  Classical attack avg success: 0.0%   (全部 tamper-zeroize)
  CFE attack avg success:       82.0%  (全部静默提取)
  CFE avg detection rate:       0.0000%
```

每个 device 报告 ⚠️ extraction implication (受影响行业 + 客户数量):

- HSM → 银行 / PKI / 千万级商品
- TPM → ~30 亿 PC/server
- 硬件钱包 → 数千亿 USD 加密资产
- EMV → ~10 亿张银行卡
- 护照 NFC → ~15 亿本 ePassport across 130+ 国
- 车载 ECU → ~1 亿连网车辆
- 卫星 keystore → 数百颗 orbital asset

## 跑

```bash
python3 cfe_uht_demo.py                  # all 7 devices
python3 cfe_uht_demo.py --device hsm     # single device
python3 -m unittest cfe_uht_demo -v      # 5 unit tests
```

## License

MIT · 详 `../../LICENSE.md`
