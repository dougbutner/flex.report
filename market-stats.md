# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-23 17:37 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,188** |
| **EASY price** | **$0.0183** (≈9.63 XPR) |
| **EASY price in XUSDC** | **0.018261 XUSDC** |
| **Total EASY pools TVL** | **$410,681** |
| **Total USD backing (stables)** | **$73,112** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,078.29 EASY** (≈$19.69) in the reflection pool |
| **7d volume** | **$235,801** |
| **30d volume** | **$483,812** |
| **Flexers (holders on contract)** | **6,051** |
| **Market cap (fully circulating)** | **$383,529** |
| **Share of Alcor Proton swap volume (24h)** | **≈21.96%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,188 | $36,203 | **22.0%** |
| 7d | $235,801 | $271,079 | **46.5%** |
| 30d | $483,812 | $938,806 | **34.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,750 | $71,532 | 3,108,494 EASY | 14,760.41 XUSDC | +0.6% |
| EASY/XMD | $1,610 | $72,454 | 3,135,181 EASY | 15,226.60 XMD | +0.6% |
| EASY/XPR | $1,386 | $29,882 | 427,629 EASY | 11,631,781.34 XPR | +0.5% |
| EASY/XUSDT | $1,257 | $71,527 | 3,125,446 EASY | 14,446.53 XUSDT | +2.2% |
| EASY/XXRP | $1,162 | $24,696 | 591,081 EASY | 10,584.20 XXRP | -0.4% |
| EASY/XXLM | $191.72 | $1,660 | 32,500 EASY | 6,031.64 XXLM | -0.5% |
| EASY/VIBRR | $134.09 | - | 8,938 EASY | 2,874,413.13 VIBRR | -39.1% |
| EASY/XDOGE | $122.52 | $1,380 | 22,609 EASY | 12,242.25 XDOGE | -0.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,194 XMD | 3,135,181 EASY | $72,454 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,760 XUSDC | 3,108,494 EASY | $71,532 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,169 XPYUSD | 3,158,507 EASY | $57,685 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,345 XPAX | 3,156,653 EASY | $57,651 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,447 XUSDT | 3,125,446 EASY | $71,527 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $995,544 | (snapshot) | (snapshot) |
| **Swap TVL** | $883,373 | - | - |
| **Swap volume** | $46,391 | $506,879 | $1,422,617 |
| **Spot volume** | $192.39 | $2,396 | $11,102 |
| **Swap fees** | $154.96 | $2,526 | $7,461 |
| **DAU (avg)** | ≈392 | ≈384 | ≈405 |
| **Liquidity pools** | 11,797 | - | - |
| **Spot pairs** | 1,677 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,078.29 EASY** |
| Approx. USD | **≈$19.69** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
