# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-31 17:27 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$7,318** |
| **EASY price** | **$0.0188** (≈10.11 XPR) |
| **EASY price in XUSDC** | **0.018855 XUSDC** |
| **Total EASY pools TVL** | **$367,189** |
| **Total USD backing (stables)** | **$62,905** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **998.23 EASY** (≈$18.78) in the reflection pool |
| **7d volume** | **$115,819** |
| **30d volume** | **$536,419** |
| **Flexers (holders on contract)** | **6,060** |
| **Market cap (fully circulating)** | **$395,130** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.47%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $7,318 | $22,587 | **24.5%** |
| 7d | $115,819 | $219,625 | **34.5%** |
| 30d | $536,419 | $963,434 | **35.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,568 | $73,229 | 3,058,979 EASY | 15,672.17 XUSDC | -0.3% |
| EASY/XPR | $2,364 | $14,068 | 413,067 EASY | 3,383,352.19 XPR | +1.2% |
| EASY/XBTC | $1,132 | $6,412 | 191,369 EASY | 0.04 XBTC | +1.0% |
| EASY/XUSDT | $540.42 | $73,228 | 3,062,147 EASY | 15,611.41 XUSDT | -0.1% |
| EASY/XMD | $291.66 | $5,727 | 302,224 EASY | 40.28 XMD | +0.9% |
| EASY/XXRP | $239.15 | $19,593 | 394,910 EASY | 9,634.03 XXRP | -0.5% |
| EASY/XDOGE | $36.21 | $1,341 | 447 EASY | 17,518.93 XDOGE | +1.0% |
| EASY/XMD | $36.16 | $41,120 | 2,157,383 EASY | 530.19 XMD | -0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $527.42 XMD | 2,157,383 EASY | $41,120 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,672 XUSDC | 3,058,979 EASY | $73,229 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,321 XPYUSD | 3,085,475 EASY | $58,055 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,465 XPAX | 3,089,649 EASY | $58,134 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,611 XUSDT | 3,062,147 EASY | $73,228 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $926,185 | (snapshot) | (snapshot) |
| **Swap TVL** | $824,875 | - | - |
| **Swap volume** | $29,905 | $335,444 | $1,499,853 |
| **Spot volume** | $168.98 | $805.66 | $8,251 |
| **Swap fees** | $168.02 | $1,776 | $7,829 |
| **DAU (avg)** | ≈374 | ≈372 | ≈396 |
| **Liquidity pools** | 11,826 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **998.23 EASY** |
| Approx. USD | **≈$18.78** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
