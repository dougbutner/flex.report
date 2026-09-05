# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-05 15:42 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,502** |
| **EASY price** | **$0.0187** (≈6.60 XPR) |
| **EASY price in XUSDC** | **0.018932 XUSDC** |
| **Total EASY pools TVL** | **$2,299,277** |
| **Total USD backing (stables)** | **$80,567** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,325.68 EASY** (≈$24.73) in the reflection pool |
| **7d volume** | **$117,180** |
| **30d volume** | **$545,218** |
| **Flexers (holders on contract)** | **957** |
| **Market cap (fully circulating)** | **$391,709** |
| **Share of Alcor Proton swap volume (24h)** | **≈18.76%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,502 | $23,830 | **18.8%** |
| 7d | $117,180 | $277,827 | **29.7%** |
| 30d | $545,218 | $997,873 | **35.3%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,468 | $72,882 | 3,052,872 EASY | 16,044.79 XUSDC | +0.0% |
| EASY/XMD | $1,267 | $73,451 | 3,077,965 EASY | 16,284.49 XMD | +0.1% |
| EASY/XXRP | $672.07 | $18,180 | 588,714 EASY | 5,181.10 XXRP | +0.0% |
| EASY/XPR | $651.65 | $40,790 | 570,381 EASY | 10,671,715.40 XPR | -0.1% |
| EASY/XMT | $336.79 | $844.71 | 23,320 EASY | 1,725.50 XMT | -0.1% |
| EASY/XUSDT | $215.43 | $72,552 | 3,051,471 EASY | 15,813.05 XUSDT | +0.1% |
| EASY/XSOL | $171.49 | - | 12,597 EASY | 6.75 XSOL | +0.0% |
| EASY/VIBRR | $121.55 | $1,394 | 23,409 EASY | 11,246,746.33 VIBRR | -1.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,178 XMD | 3,077,965 EASY | $73,451 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,045 XUSDC | 3,052,872 EASY | $72,882 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,917 XPYUSD | 3,053,053 EASY | $56,913 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,293 XPAX | 3,108,748 EASY | $57,877 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,677 XUSDT | 3,051,471 EASY | $72,552 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,074,856 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,916,575 | - | - |
| **Swap volume** | $29,333 | $395,008 | $1,543,091 |
| **Spot volume** | $97.65 | $2,612 | $9,189 |
| **Swap fees** | $140.12 | $2,118 | $8,314 |
| **DAU (avg)** | ≈70 | ≈75 | ≈76 |
| **Liquidity pools** | 11,483 | - | - |
| **Spot pairs** | 1,664 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,325.68 EASY** |
| Approx. USD | **≈$24.73** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
