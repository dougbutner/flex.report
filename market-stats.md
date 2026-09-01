# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-01 17:04 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$14,403** |
| **EASY price** | **$0.0187** (≈6.44 XPR) |
| **EASY price in XUSDC** | **0.018889 XUSDC** |
| **Total EASY pools TVL** | **$435,891** |
| **Total USD backing (stables)** | **$80,418** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **814.62 EASY** (≈$15.23) in the reflection pool |
| **7d volume** | **$151,304** |
| **30d volume** | **$522,231** |
| **Flexers (holders on contract)** | **955** |
| **Market cap (fully circulating)** | **$392,643** |
| **Share of Alcor Proton swap volume (24h)** | **≈36.42%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $14,403 | $25,140 | **36.4%** |
| 7d | $151,304 | $266,711 | **36.2%** |
| 30d | $522,231 | $903,441 | **36.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $4,454 | $47,333 | 948,524 EASY | 10,215,238.46 XPR | -0.7% |
| EASY/XMD | $3,181 | $73,588 | 3,081,693 EASY | 16,213.13 XMD | -0.7% |
| EASY/XUSDC | $3,134 | $73,149 | 3,069,213 EASY | 15,818.80 XUSDC | -0.6% |
| EASY/XUSDT | $659.93 | $72,810 | 3,055,576 EASY | 15,735.28 XUSDT | -0.7% |
| EASY/XXLM | $628.17 | $7,410 | 215,024 EASY | 19,371.54 XXLM | -0.9% |
| EASY/XXRP | $619.23 | $14,718 | 370,691 EASY | 5,737.20 XXRP | -1.0% |
| EASY/XBTC | $561.86 | $6,675 | 212,734 EASY | 0.03 XBTC | -0.6% |
| EASY/XUSDC | $260.18 | $4,133 | 167,644 EASY | 1,001.93 XUSDC | -0.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,086 XMD | 3,081,693 EASY | $73,588 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,819 XUSDC | 3,069,213 EASY | $73,149 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,854 XPYUSD | 3,057,160 EASY | $57,067 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,417 XPAX | 3,108,653 EASY | $58,028 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,735 XUSDT | 3,055,576 EASY | $72,810 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,208,472 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,041,571 | - | - |
| **Swap volume** | $39,542 | $418,015 | $1,425,672 |
| **Spot volume** | $908.57 | $2,483 | $9,433 |
| **Swap fees** | $203.51 | $2,240 | $7,564 |
| **DAU (avg)** | ≈70 | ≈76 | ≈76 |
| **Liquidity pools** | 11,466 | - | - |
| **Spot pairs** | 1,658 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **814.62 EASY** |
| Approx. USD | **≈$15.23** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
