# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-12 15:56 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,067** |
| **EASY price** | **$0.0185** (≈6.74 XPR) |
| **EASY price in XUSDC** | **0.018772 XUSDC** |
| **Total EASY pools TVL** | **$2,298,612** |
| **Total USD backing (stables)** | **$78,982** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **990.29 EASY** (≈$18.36) in the reflection pool |
| **7d volume** | **$80,633** |
| **30d volume** | **$558,283** |
| **Flexers (holders on contract)** | **967** |
| **Market cap (fully circulating)** | **$389,401** |
| **Share of Alcor Proton swap volume (24h)** | **≈21.75%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,067 | $29,016 | **21.8%** |
| 7d | $80,633 | $251,642 | **24.3%** |
| 30d | $558,283 | $1,069,035 | **34.3%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,927 | $72,391 | 3,065,672 EASY | 15,544.92 XUSDC | -0.5% |
| EASY/XMD | $1,471 | $73,224 | 3,091,085 EASY | 16,035.26 XMD | -0.5% |
| EASY/XPR | $1,384 | $42,893 | 432,593 EASY | 12,662,774.31 XPR | -0.2% |
| EASY/XXRP | $621.02 | $14,912 | 386,803 EASY | 5,706.96 XXRP | +0.8% |
| EASY/XUSDT | $599.73 | $72,312 | 3,068,206 EASY | 15,497.31 XUSDT | -0.5% |
| EASY/XPR | $413.50 | $887.73 | 40,536 EASY | 49,435.32 XPR | -0.0% |
| EASY/VIBRR | $352.85 | $1,555 | 71,743 EASY | 1,733,442.91 VIBRR | -4.1% |
| EASY/METAL | $299.54 | $6,477 | 53,202 EASY | 40,859.49 METAL | -0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,907 XMD | 3,091,085 EASY | $73,224 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,545 XUSDC | 3,065,672 EASY | $72,391 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,632 XPYUSD | 3,066,390 EASY | $56,860 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,146 XPAX | 3,108,893 EASY | $57,668 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,393 XUSDT | 3,068,206 EASY | $72,312 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,092,832 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,929,353 | - | - |
| **Swap volume** | $37,082 | $332,276 | $1,627,318 |
| **Spot volume** | $298.76 | $2,521 | $7,752 |
| **Swap fees** | $185.96 | $1,641 | $8,696 |
| **DAU (avg)** | ≈75 | ≈75 | ≈75 |
| **Liquidity pools** | 11,535 | - | - |
| **Spot pairs** | 1,667 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **990.29 EASY** |
| Approx. USD | **≈$18.36** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
