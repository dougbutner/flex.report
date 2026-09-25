# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-25 17:39 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$12,864** |
| **EASY price** | **$0.0185** (≈7.50 XPR) |
| **EASY price in XUSDC** | **0.018778 XUSDC** |
| **Total EASY pools TVL** | **$455,404** |
| **Total USD backing (stables)** | **$77,631** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,153.24 EASY** (≈$21.39) in the reflection pool |
| **7d volume** | **$124,930** |
| **30d volume** | **$502,930** |
| **Flexers (holders on contract)** | **985** |
| **Market cap (fully circulating)** | **$389,531** |
| **Share of Alcor Proton swap volume (24h)** | **≈32.95%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $12,864 | $26,178 | **33.0%** |
| 7d | $124,930 | $483,674 | **20.5%** |
| 30d | $502,930 | $1,501,307 | **25.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,124 | $72,412 | 3,065,273 EASY | 15,553.72 XUSDC | +0.8% |
| EASY/XMD | $2,989 | $73,190 | 3,091,962 EASY | 16,020.48 XMD | +0.7% |
| EASY/XXRP | $1,849 | $20,208 | 517,670 EASY | 6,770.79 XXRP | -1.2% |
| EASY/XUSDT | $1,332 | $72,165 | 3,061,713 EASY | 15,619.77 XUSDT | +0.9% |
| EASY/XPR | $1,131 | $41,413 | 372,514 EASY | 13,950,012.77 XPR | +0.0% |
| EASY/XXLM | $726.97 | $1,791 | 89,363 EASY | 624.48 XXLM | -0.6% |
| EASY/METAL | $324.07 | $2,007 | 70,880 EASY | 5,424.37 METAL | -0.4% |
| EASY/XBTC | $313.49 | $3,632 | 150,346 EASY | 0.01 XBTC | +0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,837 XMD | 3,091,962 EASY | $73,190 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,554 XUSDC | 3,065,273 EASY | $72,412 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,069 XPYUSD | 3,106,117 EASY | $57,616 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,806 XPAX | 3,136,056 EASY | $72,977 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,373 XUSDT | 3,061,713 EASY | $72,165 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,260,210 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,102,196 | - | - |
| **Swap volume** | $39,042 | $608,604 | $2,004,237 |
| **Spot volume** | $325.57 | $3,092 | $11,447 |
| **Swap fees** | $167.43 | $3,342 | $10,486 |
| **DAU (avg)** | ≈416 | ≈416 | ≈420 |
| **Liquidity pools** | 11,630 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,153.24 EASY** |
| Approx. USD | **≈$21.39** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
