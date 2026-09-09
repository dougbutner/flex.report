# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-09 16:56 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,489** |
| **EASY price** | **$0.0189** (≈6.67 XPR) |
| **EASY price in XUSDC** | **0.019077 XUSDC** |
| **Total EASY pools TVL** | **$2,345,504** |
| **Total USD backing (stables)** | **$83,110** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,771.80 EASY** (≈$33.49) in the reflection pool |
| **7d volume** | **$84,398** |
| **30d volume** | **$541,536** |
| **Flexers (holders on contract)** | **959** |
| **Market cap (fully circulating)** | **$396,980** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.6%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,489 | $26,021 | **24.6%** |
| 7d | $84,398 | $251,417 | **25.1%** |
| 30d | $541,536 | $1,053,773 | **34.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $2,603 | $74,460 | 3,067,658 EASY | 16,479.68 XMD | -0.1% |
| EASY/XUSDC | $1,563 | $75,567 | 3,063,841 EASY | 17,649.19 XUSDC | -0.0% |
| EASY/XPR | $1,271 | $43,056 | 610,909 EASY | 11,116,266.29 XPR | -0.2% |
| EASY/XPYUSD | $680.39 | $57,483 | 3,040,842 EASY | 16,015.50 XPYUSD | -0.0% |
| EASY/XSOL | $574.22 | $934.61 | 12,639 EASY | 6.73 XSOL | -0.1% |
| EASY/XXRP | $432.14 | $15,393 | 427,665 EASY | 5,146.93 XXRP | +0.1% |
| EASY/XUSDT | $397.37 | $73,475 | 3,041,504 EASY | 16,002.38 XUSDT | +0.0% |
| EASY/METAL | $253.42 | $8,112 | 36,692 EASY | 57,192.27 METAL | +0.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,469 XMD | 3,067,658 EASY | $74,460 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,649 XUSDC | 3,063,841 EASY | $75,567 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,123 XPYUSD | 3,040,842 EASY | $57,483 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,413 XPAX | 3,108,844 EASY | $58,769 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,979 XUSDT | 3,041,504 EASY | $73,475 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,136,448 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,969,038 | - | - |
| **Swap volume** | $34,510 | $335,815 | $1,595,310 |
| **Spot volume** | $155.88 | $2,417 | $7,957 |
| **Swap fees** | $168.87 | $1,721 | $8,618 |
| **DAU (avg)** | ≈72 | ≈74 | ≈76 |
| **Liquidity pools** | 11,506 | - | - |
| **Spot pairs** | 1,667 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,771.80 EASY** |
| Approx. USD | **≈$33.49** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
