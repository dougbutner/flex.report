# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-21 19:53 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$14,178** |
| **EASY price** | **$0.0166** (≈10.86 XPR) |
| **EASY price in XUSDC** | **0.017010 XUSDC** |
| **Total EASY pools TVL** | **$346,680** |
| **Total USD backing (stables)** | **$50,330** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,470.76 EASY** (≈$24.37) in the reflection pool |
| **7d volume** | **$91,803** |
| **30d volume** | **$352,098** |
| **Flexers (holders on contract)** | **6,072** |
| **Market cap (fully circulating)** | **$347,999** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.65%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $14,178 | $37,106 | **27.6%** |
| 7d | $91,803 | $194,522 | **32.1%** |
| 30d | $352,098 | $850,839 | **29.3%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $5,251 | $66,148 | 3,220,706 EASY | 12,776.53 XUSDC | +1.8% |
| EASY/XUSDT | $1,994 | $66,138 | 3,263,021 EASY | 12,065.00 XUSDT | +0.5% |
| EASY/XXRP | $1,367 | $14,768 | 91,567 EASY | 14,582.15 XXRP | -1.3% |
| EASY/XBTC | $1,334 | $5,721 | 56,481 EASY | 0.08 XBTC | +1.6% |
| EASY/XPR | $1,268 | $9,336 | 114,530 EASY | 4,873,750.26 XPR | +1.0% |
| EASY/XXLM | $774.86 | $3,289 | 13,526 EASY | 24,598.34 XXLM | -0.1% |
| EASY/XMD | $663.83 | $36,303 | 2,159,358 EASY | 538.58 XMD | +1.9% |
| EASY/XPYUSD | $413.45 | $54,200 | 3,270,697 EASY | 11,941.81 XPYUSD | -1.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $519.44 XMD | 2,159,358 EASY | $36,303 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,777 XUSDC | 3,220,706 EASY | $66,148 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,310 XPYUSD | 3,270,697 EASY | $54,200 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,550 XPAX | 3,251,010 EASY | $53,874 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,065 XUSDT | 3,263,021 EASY | $66,138 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $837,289 | (snapshot) | (snapshot) |
| **Swap TVL** | $744,249 | - | - |
| **Swap volume** | $51,284 | $286,325 | $1,202,937 |
| **Spot volume** | $296.44 | $1,583 | $4,618 |
| **Swap fees** | $228.42 | $1,430 | $6,395 |
| **DAU (avg)** | ≈428 | ≈381 | ≈369 |
| **Liquidity pools** | 11,967 | - | - |
| **Spot pairs** | 1,682 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,470.76 EASY** |
| Approx. USD | **≈$24.37** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
