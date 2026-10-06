# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-06 18:42 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,159** |
| **EASY price** | **$0.0185** (≈7.94 XPR) |
| **EASY price in XUSDC** | **0.018534 XUSDC** |
| **Total EASY pools TVL** | **$430,075** |
| **Total USD backing (stables)** | **$76,369** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,104.52 EASY** (≈$20.47) in the reflection pool |
| **7d volume** | **$67,307** |
| **30d volume** | **$435,723** |
| **Flexers (holders on contract)** | **1,011** |
| **Market cap (fully circulating)** | **$389,222** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.83%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,159 | $23,752 | **27.8%** |
| 7d | $67,307 | $205,626 | **24.7%** |
| 30d | $435,723 | $1,374,521 | **24.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $2,377 | $21,595 | 412,958 EASY | 5,970,899.33 XPR | -1.0% |
| EASY/XUSDC | $2,263 | $72,371 | 3,085,522 EASY | 15,182.70 XUSDC | +0.2% |
| EASY/XMD | $1,624 | $73,252 | 3,110,913 EASY | 15,666.19 XMD | +0.2% |
| EASY/XUSDT | $1,017 | $72,363 | 3,086,514 EASY | 15,156.48 XUSDT | +0.5% |
| EASY/METAL | $563.40 | $15,884 | 40,524 EASY | 125,759.65 METAL | +1.6% |
| EASY/XBTC | $500.89 | $3,701 | 168,999 EASY | 0.01 XBTC | +0.1% |
| EASY/XXRP | $328.79 | $20,470 | 401,669 EASY | 8,694.25 XXRP | +0.2% |
| EASY/XPYUSD | $236.59 | $57,196 | 3,085,945 EASY | 15,166.84 XPYUSD | +0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,594 XMD | 3,110,913 EASY | $73,252 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,183 XUSDC | 3,085,522 EASY | $72,371 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,198 XPYUSD | 3,085,945 EASY | $57,196 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,760 XPAX | 3,136,423 EASY | $58,132 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,156 XUSDT | 3,086,514 EASY | $72,363 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,174,514 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,023,785 | - | - |
| **Swap volume** | $32,911 | $272,933 | $1,810,243 |
| **Spot volume** | $724.38 | $4,188 | $12,390 |
| **Swap fees** | $149.35 | $1,449 | $9,488 |
| **DAU (avg)** | ≈409 | ≈418 | ≈421 |
| **Liquidity pools** | 11,674 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,104.52 EASY** |
| Approx. USD | **≈$20.47** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
