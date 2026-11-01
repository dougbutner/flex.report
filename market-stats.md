# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-01 18:12 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$3,501** |
| **EASY price** | **$0.0189** (≈10.03 XPR) |
| **EASY price in XUSDC** | **0.018965 XUSDC** |
| **Total EASY pools TVL** | **$366,875** |
| **Total USD backing (stables)** | **$63,561** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **991.90 EASY** (≈$18.78) in the reflection pool |
| **7d volume** | **$64,589** |
| **30d volume** | **$524,732** |
| **Flexers (holders on contract)** | **6,061** |
| **Market cap (fully circulating)** | **$397,580** |
| **Share of Alcor Proton swap volume (24h)** | **≈17.62%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $3,501 | $16,371 | **17.6%** |
| 7d | $64,589 | $171,084 | **27.4%** |
| 30d | $524,732 | $943,165 | **35.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,672 | $73,585 | 3,050,048 EASY | 15,839.96 XUSDC | +0.5% |
| EASY/XXRP | $634.54 | $18,975 | 404,357 EASY | 8,941.43 XXRP | -0.4% |
| EASY/XUSDT | $446.31 | $73,584 | 3,052,690 EASY | 15,789.67 XUSDT | +0.5% |
| EASY/XPR | $335.27 | $13,939 | 409,067 EASY | 3,281,762.78 XPR | +0.7% |
| EASY/XPYUSD | $87.11 | $58,284 | 3,078,546 EASY | 15,304.20 XPYUSD | +0.5% |
| EASY/XDOGE | $82.81 | $1,334 | 446 EASY | 17,519.43 XDOGE | +1.6% |
| EASY/XPAX | $62.91 | $58,369 | 3,083,028 EASY | 15,284.42 XPAX | +0.4% |
| EASY/XMD | $41.03 | $41,350 | 2,156,733 EASY | 520.80 XMD | +0.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $518.30 XMD | 2,156,733 EASY | $41,350 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,840 XUSDC | 3,050,048 EASY | $73,585 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,500 XPYUSD | 3,078,546 EASY | $58,284 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,591 XPAX | 3,083,028 EASY | $58,369 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,790 XUSDT | 3,052,690 EASY | $73,584 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $929,989 | (snapshot) | (snapshot) |
| **Swap TVL** | $826,981 | - | - |
| **Swap volume** | $19,872 | $235,673 | $1,467,897 |
| **Spot volume** | $71.55 | $702.49 | $7,966 |
| **Swap fees** | $100.11 | $1,316 | $7,593 |
| **DAU (avg)** | ≈351 | ≈362 | ≈392 |
| **Liquidity pools** | 11,828 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **991.90 EASY** |
| Approx. USD | **≈$18.78** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
