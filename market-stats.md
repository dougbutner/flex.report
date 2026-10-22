# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-22 17:45 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$14,431** |
| **EASY price** | **$0.0179** (≈9.67 XPR) |
| **EASY price in XUSDC** | **0.018135 XUSDC** |
| **Total EASY pools TVL** | **$402,146** |
| **Total USD backing (stables)** | **$72,355** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **923.53 EASY** (≈$16.50) in the reflection pool |
| **7d volume** | **$230,826** |
| **30d volume** | **$483,685** |
| **Flexers (holders on contract)** | **6,051** |
| **Market cap (fully circulating)** | **$375,295** |
| **Share of Alcor Proton swap volume (24h)** | **≈50.11%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $14,431 | $14,366 | **50.1%** |
| 7d | $230,826 | $250,947 | **47.9%** |
| 30d | $483,685 | $942,385 | **33.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XXRP | $4,424 | $24,029 | 575,651 EASY | 10,797.61 XXRP | +1.1% |
| EASY/XUSDC | $3,263 | $70,307 | 3,119,293 EASY | 14,562.05 XUSDC | -2.3% |
| EASY/XMD | $2,796 | $71,259 | 3,145,161 EASY | 15,044.22 XMD | -2.3% |
| EASY/XPR | $2,471 | $28,586 | 405,711 EASY | 11,549,759.72 XPR | +0.0% |
| EASY/XBTC | $615.58 | $6,433 | 300,397 EASY | 0.01 XBTC | -0.1% |
| EASY/XUSDT | $251.53 | $70,302 | 3,160,672 EASY | 13,816.73 XUSDT | -0.4% |
| EASY/XXLM | $224.79 | $1,633 | 30,881 EASY | 6,200.57 XXLM | +1.6% |
| EASY/XDOGE | $200.68 | $1,411 | 23,440 EASY | 12,791.18 XDOGE | +2.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,051 XMD | 3,145,161 EASY | $71,259 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,562 XUSDC | 3,119,293 EASY | $70,307 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,280 XPYUSD | 3,159,862 EASY | $56,470 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,436 XPAX | 3,156,514 EASY | $56,411 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,817 XUSDT | 3,160,672 EASY | $70,302 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $967,156 | (snapshot) | (snapshot) |
| **Swap TVL** | $856,278 | - | - |
| **Swap volume** | $28,797 | $481,774 | $1,426,071 |
| **Spot volume** | $1,645 | $2,419 | $10,945 |
| **Swap fees** | $157.86 | $2,465 | $7,575 |
| **DAU (avg)** | ≈361 | ≈386 | ≈406 |
| **Liquidity pools** | 11,796 | - | - |
| **Spot pairs** | 1,677 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **923.53 EASY** |
| Approx. USD | **≈$16.50** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
