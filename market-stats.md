# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-09 18:35 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,380** |
| **EASY price** | **$0.0182** (≈8.04 XPR) |
| **EASY price in XUSDC** | **0.018306 XUSDC** |
| **Total EASY pools TVL** | **$395,516** |
| **Total USD backing (stables)** | **$74,141** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,376.14 EASY** (≈$25.06) in the reflection pool |
| **7d volume** | **$98,344** |
| **30d volume** | **$460,895** |
| **Flexers (holders on contract)** | **1,015** |
| **Market cap (fully circulating)** | **$382,456** |
| **Share of Alcor Proton swap volume (24h)** | **≈17.91%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,380 | $47,580 | **17.9%** |
| 7d | $98,344 | $228,210 | **30.1%** |
| 30d | $460,895 | $1,398,510 | **24.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,949 | $71,369 | 3,104,598 EASY | 14,827.55 XUSDC | +0.9% |
| EASY/XMD | $1,854 | $72,046 | 3,130,495 EASY | 15,307.74 XMD | +0.9% |
| EASY/XPR | $1,428 | $23,958 | 499,459 EASY | 6,561,531.03 XPR | +0.3% |
| EASY/XXRP | $1,361 | $15,237 | 355,839 EASY | 6,304.53 XXRP | -1.2% |
| EASY/XUSDT | $994.46 | $71,366 | 3,116,854 EASY | 14,601.04 XUSDT | +1.0% |
| EASY/METAL | $500.66 | $2,280 | 50,525 EASY | 11,359.78 METAL | -0.4% |
| EASY/XPYUSD | $406.68 | $56,526 | 3,103,722 EASY | 14,840.40 XPYUSD | +0.9% |
| EASY/XXLM | $171.42 | $1,736 | 59,008 EASY | 3,431.40 XXLM | -0.9% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,033 XMD | 3,130,495 EASY | $72,046 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,828 XUSDC | 3,104,598 EASY | $71,369 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,939 XPYUSD | 3,103,722 EASY | $56,526 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,454 XPAX | 3,137,404 EASY | $57,139 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,601 XUSDT | 3,116,854 EASY | $71,366 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,147,806 | (snapshot) | (snapshot) |
| **Swap TVL** | $998,514 | - | - |
| **Swap volume** | $57,960 | $326,554 | $1,859,405 |
| **Spot volume** | $114.50 | $2,589 | $12,809 |
| **Swap fees** | $320.96 | $1,763 | $9,836 |
| **DAU (avg)** | ≈400 | ≈413 | ≈419 |
| **Liquidity pools** | 11,687 | - | - |
| **Spot pairs** | 1,673 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,376.14 EASY** |
| Approx. USD | **≈$25.06** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
