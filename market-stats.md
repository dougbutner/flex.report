# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-15 13:24 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,740** |
| **EASY price** | **$0.0165** (≈6.71 XPR) |
| **EASY price in XUSDC** | **0.016549 XUSDC** |
| **Total EASY pools TVL** | **$376,379** |
| **Total USD backing (stables)** | **$60,509** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **768.72 EASY** (≈$12.70) in the reflection pool |
| **7d volume** | **$58,238** |
| **30d volume** | **$361,372** |
| **Flexers (holders on contract)** | **941** |
| **Market cap (fully circulating)** | **$346,843** |
| **Share of Alcor Proton swap volume (24h)** | **≈35.92%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,740 | $15,592 | **35.9%** |
| 7d | $58,238 | $159,632 | **26.7%** |
| 30d | $361,372 | $771,560 | **31.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,347 | $65,958 | 3,265,272 EASY | 12,027.50 XUSDC | -0.2% |
| EASY/XPR | $1,771 | $25,903 | 404,399 EASY | 7,809,392.91 XPR | -0.5% |
| EASY/XUSDT | $1,593 | $66,158 | 3,294,448 EASY | 11,549.06 XUSDT | -1.1% |
| EASY/XMD | $974.11 | $65,928 | 3,265,495 EASY | 12,028.06 XMD | -0.2% |
| EASY/XXRP | $611.66 | $17,748 | 197,195 EASY | 14,556.32 XXRP | +0.1% |
| EASY/XPYUSD | $101.37 | $53,912 | 3,264,162 EASY | 12,045.28 XPYUSD | -0.2% |
| EASY/XPAX | $99.34 | $54,502 | 3,299,876 EASY | 12,652.90 XPAX | -0.2% |
| EASY/HARD | $72.05 | - | 4,427 EASY | 60,215,917.58 HARD | -41.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $11,994 XMD | 3,265,495 EASY | $65,928 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,028 XUSDC | 3,265,272 EASY | $65,958 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,098 XPYUSD | 3,264,162 EASY | $53,912 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,629 XPAX | 3,299,876 EASY | $54,502 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $11,746 XUSDT | 3,294,448 EASY | $66,158 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,054,823 | (snapshot) | (snapshot) |
| **Swap TVL** | $907,650 | - | - |
| **Swap volume** | $24,332 | $217,870 | $1,132,932 |
| **Spot volume** | $42.03 | $3,771 | $33,551 |
| **Swap fees** | $85.13 | $1,125 | $5,948 |
| **DAU (avg)** | ≈71 | ≈78 | ≈78 |
| **Liquidity pools** | 11,324 | - | - |
| **Spot pairs** | 1,655 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **768.72 EASY** |
| Approx. USD | **≈$12.70** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
