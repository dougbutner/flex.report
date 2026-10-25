# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-25 16:54 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$54,899** |
| **EASY price** | **$0.0202** (≈10.83 XPR) |
| **EASY price in XUSDC** | **0.020156 XUSDC** |
| **Total EASY pools TVL** | **$403,524** |
| **Total USD backing (stables)** | **$65,279** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,282.79 EASY** (≈$25.86) in the reflection pool |
| **7d volume** | **$136,642** |
| **30d volume** | **$530,886** |
| **Flexers (holders on contract)** | **6,055** |
| **Market cap (fully circulating)** | **$423,274** |
| **Share of Alcor Proton swap volume (24h)** | **≈43.09%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $54,899 | $72,497 | **43.1%** |
| 7d | $136,642 | $212,484 | **39.1%** |
| 30d | $530,886 | $976,233 | **35.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $20,074 | $77,265 | 2,958,647 EASY | 17,631.06 XUSDC | +11.5% |
| EASY/XMD | $13,090 | $43,929 | 2,154,369 EASY | 506.00 XMD | +11.5% |
| EASY/XPR | $7,869 | $16,844 | 334,743 EASY | 5,427,395.13 XPR | -11.0% |
| EASY/XXRP | $5,571 | $21,432 | 332,279 EASY | 11,387.71 XXRP | +9.4% |
| EASY/XBTC | $2,799 | $6,934 | 157,178 EASY | 0.05 XBTC | +12.2% |
| EASY/XUSDT | $2,365 | $77,325 | 3,057,282 EASY | 15,703.22 XUSDT | +4.8% |
| EASY/XMD | $797.53 | $6,130 | 291,192 EASY | 260.61 XMD | +5.4% |
| EASY/XPYUSD | $385.57 | $63,255 | 3,138,276 EASY | 14,213.73 XPYUSD | +2.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $505.91 XMD | 2,154,369 EASY | $43,929 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,631 XUSDC | 2,958,647 EASY | $77,265 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,003 XPYUSD | 3,138,276 EASY | $63,255 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,739 XPAX | 3,144,700 EASY | $63,384 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,703 XUSDT | 3,057,282 EASY | $77,325 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $994,699 | (snapshot) | (snapshot) |
| **Swap TVL** | $886,368 | - | - |
| **Swap volume** | $127,396 | $349,126 | $1,507,119 |
| **Spot volume** | $188.15 | $2,286 | $11,016 |
| **Swap fees** | $602.76 | $1,558 | $7,824 |
| **DAU (avg)** | ≈418 | ≈380 | ≈405 |
| **Liquidity pools** | 11,809 | - | - |
| **Spot pairs** | 1,678 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,282.79 EASY** |
| Approx. USD | **≈$25.86** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
