# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-05 20:25 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,838** |
| **EASY price** | **$0.0186** (≈10.06 XPR) |
| **EASY price in XUSDC** | **0.018834 XUSDC** |
| **Total EASY pools TVL** | **$365,918** |
| **Total USD backing (stables)** | **$63,181** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **985.19 EASY** (≈$18.32) in the reflection pool |
| **7d volume** | **$45,576** |
| **30d volume** | **$509,593** |
| **Flexers (holders on contract)** | **6,062** |
| **Market cap (fully circulating)** | **$390,535** |
| **Share of Alcor Proton swap volume (24h)** | **≈32.0%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,838 | $14,531 | **32.0%** |
| 7d | $45,576 | $145,725 | **23.8%** |
| 30d | $509,593 | $906,249 | **36.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,943 | $72,666 | 3,060,694 EASY | 15,638.99 XUSDC | -2.4% |
| EASY/XXRP | $1,048 | $18,699 | 417,901 EASY | 8,743.75 XXRP | +1.5% |
| EASY/XUSDT | $811.16 | $72,664 | 3,080,631 EASY | 15,265.52 XUSDT | -2.0% |
| EASY/XPR | $569.31 | $12,387 | 380,208 EASY | 2,863,458.42 XPR | -0.3% |
| EASY/XBTC | $389.36 | $6,929 | 222,240 EASY | 0.04 XBTC | +1.4% |
| EASY/USDC | $329.33 | $3,732 | 198,571 EASY | 31.90 USDC | +0.5% |
| EASY/XXLM | $278.29 | $566.62 | 6,975 EASY | 2,881.94 XXLM | +9.6% |
| EASY/XPAX | $118.13 | $57,203 | 3,070,140 EASY | 15,524.90 XPAX | +0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $519.74 XMD | 2,156,811 EASY | $40,706 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,639 XUSDC | 3,060,694 EASY | $72,666 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,691 XPYUSD | 3,070,277 EASY | $57,206 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,737 XPAX | 3,070,140 EASY | $57,203 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,266 XUSDT | 3,080,631 EASY | $72,664 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $909,880 | (snapshot) | (snapshot) |
| **Swap TVL** | $809,381 | - | - |
| **Swap volume** | $21,368 | $191,301 | $1,415,842 |
| **Spot volume** | $100.50 | $855.23 | $6,327 |
| **Swap fees** | $131.41 | $1,105 | $7,393 |
| **DAU (avg)** | ≈334 | ≈346 | ≈381 |
| **Liquidity pools** | 11,834 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **985.19 EASY** |
| Approx. USD | **≈$18.32** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
