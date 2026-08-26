# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-26 13:46 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$17,370** |
| **EASY price** | **$0.0182** (≈6.65 XPR) |
| **EASY price in XUSDC** | **0.018313 XUSDC** |
| **Total EASY pools TVL** | **$2,241,198** |
| **Total USD backing (stables)** | **$78,596** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **954.95 EASY** (≈$17.36) in the reflection pool |
| **7d volume** | **$223,250** |
| **30d volume** | **$467,312** |
| **Flexers (holders on contract)** | **951** |
| **Market cap (fully circulating)** | **$381,819** |
| **Share of Alcor Proton swap volume (24h)** | **≈39.76%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $17,370 | $26,321 | **39.8%** |
| 7d | $223,250 | $295,768 | **43.0%** |
| 30d | $467,312 | $868,819 | **35.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $4,516 | $43,718 | 621,744 EASY | 11,861,658.07 XPR | -0.5% |
| EASY/XUSDC | $4,456 | $75,949 | 3,233,592 EASY | 17,172.09 XUSDC | -1.3% |
| EASY/XMD | $3,094 | $72,098 | 3,130,945 EASY | 15,296.38 XMD | -1.3% |
| EASY/XXRP | $2,262 | $15,124 | 476,737 EASY | 4,648.11 XXRP | +1.1% |
| EASY/XUSDT | $865.58 | $71,124 | 3,101,886 EASY | 14,872.96 XUSDT | -1.3% |
| EASY/XUSDC | $760.21 | $3,893 | 186,158 EASY | 508.91 XUSDC | -1.1% |
| EASY/XBTC | $561.85 | $4,473 | 218,473 EASY | 0.01 XBTC | -1.4% |
| EASY/XDOGE | $232.15 | $1,121 | 50,564 EASY | 2,344.04 XDOGE | +0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,190 XMD | 3,130,945 EASY | $72,098 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,172 XUSDC | 3,233,592 EASY | $75,949 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,987 XPYUSD | 3,103,784 EASY | $56,418 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,597 XPAX | 3,142,025 EASY | $57,113 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,744 XUSDT | 3,101,886 EASY | $71,124 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $2,961,447 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,809,537 | - | - |
| **Swap volume** | $43,690 | $519,018 | $1,336,131 |
| **Spot volume** | $84.81 | $1,153 | $15,888 |
| **Swap fees** | $235.78 | $2,959 | $7,224 |
| **DAU (avg)** | ≈78 | ≈79 | ≈77 |
| **Liquidity pools** | 11,434 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **954.95 EASY** |
| Approx. USD | **≈$17.36** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
