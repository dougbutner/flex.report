# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-19 13:37 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,590** |
| **EASY price** | **$0.0173** (≈6.66 XPR) |
| **EASY price in XUSDC** | **0.017315 XUSDC** |
| **Total EASY pools TVL** | **$2,135,590** |
| **Total USD backing (stables)** | **$67,775** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,045.25 EASY** (≈$18.11) in the reflection pool |
| **7d volume** | **$63,712** |
| **30d volume** | **$343,747** |
| **Flexers (holders on contract)** | **942** |
| **Market cap (fully circulating)** | **$363,901** |
| **Share of Alcor Proton swap volume (24h)** | **≈33.93%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,590 | $20,625 | **33.9%** |
| 7d | $63,712 | $134,263 | **32.2%** |
| 30d | $343,747 | $741,118 | **31.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,418 | $68,584 | 3,192,279 EASY | 13,266.24 XUSDC | +1.1% |
| EASY/XMD | $2,407 | $68,549 | 3,193,141 EASY | 13,254.59 XMD | +1.0% |
| EASY/XPR | $2,270 | $34,864 | 947,279 EASY | 7,091,176.57 XPR | +0.6% |
| EASY/XUSDT | $1,093 | $68,593 | 3,192,069 EASY | 13,267.37 XUSDT | +1.2% |
| EASY/XMT | $844.82 | $2,169 | 8,962 EASY | 10,834.39 XMT | -0.3% |
| EASY/XMD | $423.52 | $2,539 | 49,688 EASY | 1,682.47 XMD | +0.8% |
| EASY/METAL | $240.02 | $2,785 | 120,329 EASY | 6,387.11 METAL | -1.6% |
| EASY/XHBAR | $169.78 | $887.89 | 13,305 EASY | 9,754.17 XHBAR | -0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $13,216 XMD | 3,193,141 EASY | $68,549 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,266 XUSDC | 3,192,279 EASY | $68,584 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,933 XPYUSD | 3,217,616 EASY | $55,757 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,319 XPAX | 3,290,498 EASY | $57,020 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,279 XUSDT | 3,192,069 EASY | $68,593 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $2,824,940 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,680,481 | - | - |
| **Swap volume** | $31,215 | $197,975 | $1,084,865 |
| **Spot volume** | $31.98 | $1,339 | $25,094 |
| **Swap fees** | $155.19 | $972.33 | $5,642 |
| **DAU (avg)** | ≈69 | ≈73 | ≈77 |
| **Liquidity pools** | 11,361 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,045.25 EASY** |
| Approx. USD | **≈$18.11** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
