# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-29 18:23 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,854** |
| **EASY price** | **$0.0184** (≈7.54 XPR) |
| **EASY price in XUSDC** | **0.018421 XUSDC** |
| **Total EASY pools TVL** | **$439,999** |
| **Total USD backing (stables)** | **$76,325** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,830.53 EASY** (≈$33.73) in the reflection pool |
| **7d volume** | **$77,935** |
| **30d volume** | **$485,091** |
| **Flexers (holders on contract)** | **996** |
| **Market cap (fully circulating)** | **$386,948** |
| **Share of Alcor Proton swap volume (24h)** | **≈25.6%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,854 | $31,550 | **25.6%** |
| 7d | $77,935 | $202,411 | **27.8%** |
| 30d | $485,091 | $1,476,370 | **24.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XXRP | $3,108 | $20,397 | 397,708 EASY | 8,745.27 XXRP | +0.3% |
| EASY/XMD | $2,645 | $72,979 | 3,121,523 EASY | 15,471.32 XMD | -0.2% |
| EASY/XUSDC | $2,601 | $72,213 | 3,094,808 EASY | 15,188.31 XUSDC | -0.2% |
| EASY/XUSDT | $692.89 | $71,944 | 3,093,497 EASY | 15,027.60 XUSDT | -0.1% |
| EASY/XPYUSD | $597.51 | $57,024 | 3,094,760 EASY | 15,004.54 XPYUSD | -0.2% |
| EASY/XPR | $518.05 | $27,673 | 380,078 EASY | 8,462,612.44 XPR | +0.1% |
| EASY/METAL | $336.45 | $3,953 | 121,952 EASY | 13,534.61 METAL | +0.8% |
| EASY/XDOGE | $97.14 | $1,482 | 77,013 EASY | 672.43 XDOGE | -0.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,462 XMD | 3,121,523 EASY | $72,979 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,188 XUSDC | 3,094,808 EASY | $72,213 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,058 XPYUSD | 3,094,760 EASY | $57,024 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,730 XPAX | 3,136,097 EASY | $72,516 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,959 XUSDT | 3,093,497 EASY | $71,944 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,214,037 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,060,844 | - | - |
| **Swap volume** | $42,404 | $280,345 | $1,961,461 |
| **Spot volume** | $36.53 | $1,788 | $11,798 |
| **Swap fees** | $259.87 | $1,507 | $10,273 |
| **DAU (avg)** | ≈408 | ≈414 | ≈421 |
| **Liquidity pools** | 11,637 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,830.53 EASY** |
| Approx. USD | **≈$33.73** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
