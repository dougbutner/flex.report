# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-03 16:46 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$22,087** |
| **EASY price** | **$0.0190** (≈6.59 XPR) |
| **EASY price in XUSDC** | **0.019088 XUSDC** |
| **Total EASY pools TVL** | **$2,354,074** |
| **Total USD backing (stables)** | **$81,379** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,862.33 EASY** (≈$35.37) in the reflection pool |
| **7d volume** | **$127,842** |
| **30d volume** | **$546,017** |
| **Flexers (holders on contract)** | **956** |
| **Market cap (fully circulating)** | **$398,808** |
| **Share of Alcor Proton swap volume (24h)** | **≈36.37%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $22,087 | $38,645 | **36.4%** |
| 7d | $127,842 | $291,048 | **30.5%** |
| 30d | $546,017 | $974,638 | **35.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $5,468 | $49,570 | 687,885 EASY | 12,666,689.63 XPR | -0.5% |
| EASY/XMD | $5,264 | $74,669 | 3,064,601 EASY | 16,539.55 XMD | +1.6% |
| EASY/XUSDC | $3,789 | $73,765 | 3,040,217 EASY | 16,028.83 XUSDC | +1.5% |
| EASY/XXRP | $2,725 | $18,674 | 627,611 EASY | 4,674.20 XXRP | -2.9% |
| EASY/XUSDT | $1,133 | $73,784 | 3,042,864 EASY | 15,976.83 XUSDT | +1.5% |
| EASY/XXLM | $665.55 | $4,093 | 120,259 EASY | 9,837.28 XXLM | -1.6% |
| EASY/XBTC | $647.26 | $6,828 | 262,660 EASY | 0.02 XBTC | -1.0% |
| EASY/XPYUSD | $586.53 | $57,744 | 3,040,632 EASY | 16,019.38 XPYUSD | +1.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,470 XMD | 3,064,601 EASY | $74,669 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,029 XUSDC | 3,040,217 EASY | $73,765 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,156 XPYUSD | 3,040,632 EASY | $57,744 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,316 XPAX | 3,108,787 EASY | $59,038 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,998 XUSDT | 3,042,864 EASY | $73,784 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,099,058 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,942,062 | - | - |
| **Swap volume** | $60,732 | $418,890 | $1,520,655 |
| **Spot volume** | $116.82 | $2,539 | $9,061 |
| **Swap fees** | $363.59 | $2,293 | $8,176 |
| **DAU (avg)** | ≈74 | ≈76 | ≈76 |
| **Liquidity pools** | 11,480 | - | - |
| **Spot pairs** | 1,662 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,862.33 EASY** |
| Approx. USD | **≈$35.37** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
