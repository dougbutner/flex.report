# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-07 18:00 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$12,593** |
| **EASY price** | **$0.0189** (≈6.65 XPR) |
| **EASY price in XUSDC** | **0.019027 XUSDC** |
| **Total EASY pools TVL** | **$2,330,738** |
| **Total USD backing (stables)** | **$82,732** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **5,240.32 EASY** (≈$99.04) in the reflection pool |
| **7d volume** | **$94,745** |
| **30d volume** | **$537,555** |
| **Flexers (holders on contract)** | **958** |
| **Market cap (fully circulating)** | **$396,896** |
| **Share of Alcor Proton swap volume (24h)** | **≈30.02%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $12,593 | $29,357 | **30.0%** |
| 7d | $94,745 | $270,707 | **25.9%** |
| 30d | $537,555 | $1,016,873 | **34.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $4,159 | $43,146 | 673,553 EASY | 10,693,282.31 XPR | -0.5% |
| EASY/XMD | $2,575 | $74,320 | 3,072,078 EASY | 16,395.33 XMD | -0.1% |
| EASY/XUSDC | $1,872 | $75,167 | 3,045,142 EASY | 17,603.58 XUSDC | -0.0% |
| EASY/VIBRR | $1,063 | $1,591 | 50,181 EASY | 6,251,787.86 VIBRR | -6.5% |
| EASY/XXRP | $740.36 | $15,238 | 413,794 EASY | 5,335.26 XXRP | +0.2% |
| EASY/XXLM | $644.54 | $4,134 | 139,055 EASY | 7,920.24 XXLM | -1.4% |
| EASY/XUSDT | $317.22 | $73,367 | 3,045,035 EASY | 15,935.11 XUSDT | +0.0% |
| EASY/XPYUSD | $231.63 | $57,564 | 3,045,165 EASY | 15,932.66 XPYUSD | -0.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,392 XMD | 3,072,078 EASY | $74,320 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,604 XUSDC | 3,045,142 EASY | $75,167 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,052 XPYUSD | 3,045,165 EASY | $57,564 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,413 XPAX | 3,108,837 EASY | $58,767 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,803 XUSDT | 3,045,035 EASY | $73,367 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,154,261 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,984,922 | - | - |
| **Swap volume** | $41,950 | $365,452 | $1,554,428 |
| **Spot volume** | $87.47 | $3,233 | $9,954 |
| **Swap fees** | $216.70 | $1,931 | $8,378 |
| **DAU (avg)** | ≈75 | ≈74 | ≈76 |
| **Liquidity pools** | 11,497 | - | - |
| **Spot pairs** | 1,664 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **5,240.32 EASY** |
| Approx. USD | **≈$99.04** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
