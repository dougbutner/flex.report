# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-06 15:54 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$7,383** |
| **EASY price** | **$0.0189** (≈6.58 XPR) |
| **EASY price in XUSDC** | **0.019090 XUSDC** |
| **Total EASY pools TVL** | **$2,332,014** |
| **Total USD backing (stables)** | **$81,462** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,251.59 EASY** (≈$23.61) in the reflection pool |
| **7d volume** | **$117,301** |
| **30d volume** | **$533,041** |
| **Flexers (holders on contract)** | **958** |
| **Market cap (fully circulating)** | **$396,135** |
| **Share of Alcor Proton swap volume (24h)** | **≈13.75%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $7,383 | $46,301 | **13.8%** |
| 7d | $117,301 | $301,071 | **28.0%** |
| 30d | $533,041 | $1,012,249 | **34.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $1,827 | $74,176 | 3,065,218 EASY | 16,524.93 XMD | +0.4% |
| EASY/XUSDC | $1,600 | $73,376 | 3,040,044 EASY | 16,030.06 XUSDC | +0.4% |
| EASY/XPR | $1,289 | $41,342 | 599,107 EASY | 10,482,252.63 XPR | +0.1% |
| EASY/XUSDT | $851.13 | $73,397 | 3,040,314 EASY | 16,024.83 XUSDT | +0.4% |
| EASY/XDOGE | $720.71 | $1,492 | 48,148 EASY | 6,563.75 XDOGE | -1.2% |
| EASY/XPYUSD | $280.14 | $57,346 | 3,040,011 EASY | 16,030.61 XPYUSD | +0.4% |
| EASY/VIBRR | $244.41 | $1,449 | 33,181 EASY | 9,168,169.38 VIBRR | -2.0% |
| EASY/XMT | $107.05 | $862.02 | 24,790 EASY | 1,613.73 XMT | -1.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,355 XMD | 3,065,218 EASY | $74,176 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,030 XUSDC | 3,040,044 EASY | $73,376 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,158 XPYUSD | 3,040,011 EASY | $57,346 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,411 XPAX | 3,108,800 EASY | $58,643 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,046 XUSDT | 3,040,314 EASY | $73,397 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,145,127 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,975,493 | - | - |
| **Swap volume** | $53,684 | $418,372 | $1,545,290 |
| **Spot volume** | $1,379 | $3,592 | $10,368 |
| **Swap fees** | $249.13 | $2,210 | $8,328 |
| **DAU (avg)** | ≈76 | ≈75 | ≈76 |
| **Liquidity pools** | 11,489 | - | - |
| **Spot pairs** | 1,664 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,251.59 EASY** |
| Approx. USD | **≈$23.61** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
