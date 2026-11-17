# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-17 21:28 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,397** |
| **EASY price** | **$0.0171** (≈11.01 XPR) |
| **EASY price in XUSDC** | **0.017142 XUSDC** |
| **Total EASY pools TVL** | **$347,973** |
| **Total USD backing (stables)** | **$52,735** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,106.43 EASY** (≈$18.94) in the reflection pool |
| **7d volume** | **$75,386** |
| **30d volume** | **$344,282** |
| **Flexers (holders on contract)** | **6,072** |
| **Market cap (fully circulating)** | **$359,430** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.27%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,397 | $14,394 | **27.3%** |
| 7d | $75,386 | $190,773 | **28.3%** |
| 30d | $344,282 | $795,603 | **30.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,652 | $67,899 | 3,208,258 EASY | 12,987.40 XUSDC | -0.6% |
| EASY/XPR | $1,631 | $9,630 | 120,471 EASY | 4,867,226.30 XPR | -3.3% |
| EASY/XXLM | $600.37 | $3,526 | 41,324 EASY | 21,045.18 XXLM | -2.6% |
| EASY/XXRP | $410.83 | $12,069 | 109,494 EASY | 10,850.81 XXRP | -1.6% |
| EASY/XUSDT | $395.71 | $67,899 | 3,210,676 EASY | 12,945.73 XUSDT | +0.0% |
| EASY/XPYUSD | $219.12 | $54,904 | 3,207,816 EASY | 12,994.72 XPYUSD | -0.6% |
| EASY/XBTC | $133.37 | $6,069 | 114,170 EASY | 0.07 XBTC | -0.6% |
| EASY/XPAX | $118.60 | $54,804 | 3,201,961 EASY | 13,156.41 XPAX | -0.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $527.15 XMD | 2,158,481 EASY | $37,471 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,987 XUSDC | 3,208,258 EASY | $67,899 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,991 XPYUSD | 3,207,816 EASY | $54,904 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,208 XPAX | 3,201,961 EASY | $54,804 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,946 XUSDT | 3,210,676 EASY | $67,899 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $821,879 | (snapshot) | (snapshot) |
| **Swap TVL** | $732,926 | - | - |
| **Swap volume** | $19,791 | $266,158 | $1,139,885 |
| **Spot volume** | $82.52 | $2,055 | $5,820 |
| **Swap fees** | $104.62 | $1,546 | $6,062 |
| **DAU (avg)** | ≈362 | ≈373 | ≈365 |
| **Liquidity pools** | 11,861 | - | - |
| **Spot pairs** | 1,681 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,106.43 EASY** |
| Approx. USD | **≈$18.94** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
