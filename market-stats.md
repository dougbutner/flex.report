# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-14 18:36 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,822** |
| **EASY price** | **$0.0176** (≈9.66 XPR) |
| **EASY price in XUSDC** | **0.017740 XUSDC** |
| **Total EASY pools TVL** | **$365,848** |
| **Total USD backing (stables)** | **$56,215** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,119.78 EASY** (≈$19.69) in the reflection pool |
| **7d volume** | **$71,352** |
| **30d volume** | **$491,494** |
| **Flexers (holders on contract)** | **6,072** |
| **Market cap (fully circulating)** | **$369,289** |
| **Share of Alcor Proton swap volume (24h)** | **≈17.12%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,822 | $42,715 | **17.1%** |
| 7d | $71,352 | $240,594 | **22.9%** |
| 30d | $491,494 | $905,681 | **35.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $2,796 | $13,749 | 528,748 EASY | 2,443,724.19 XPR | -2.9% |
| EASY/XUSDC | $2,687 | $69,398 | 3,153,656 EASY | 13,940.44 XUSDC | -3.0% |
| EASY/XUSDT | $1,210 | $69,396 | 3,167,539 EASY | 13,694.61 XUSDT | -2.9% |
| EASY/XXRP | $671.23 | $17,266 | 73,887 EASY | 16,831.42 XXRP | +2.9% |
| EASY/XPAX | $505.97 | $55,494 | 3,155,728 EASY | 13,964.94 XPAX | -3.0% |
| EASY/XBTC | $277.42 | $6,249 | 108,696 EASY | 0.07 XBTC | +1.4% |
| EASY/XXLM | $211.16 | $3,614 | 3,678 EASY | 26,392.34 XXLM | +4.8% |
| EASY/XPYUSD | $137.20 | $55,460 | 3,153,776 EASY | 13,937.24 XPYUSD | -0.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $497.60 XMD | 2,157,676 EASY | $38,441 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,940 XUSDC | 3,153,656 EASY | $69,398 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,938 XPYUSD | 3,153,776 EASY | $55,460 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,007 XPAX | 3,155,728 EASY | $55,494 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,695 XUSDT | 3,167,539 EASY | $69,396 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $868,057 | (snapshot) | (snapshot) |
| **Swap TVL** | $770,467 | - | - |
| **Swap volume** | $51,537 | $311,946 | $1,397,176 |
| **Spot volume** | $476.36 | $1,482 | $5,325 |
| **Swap fees** | $313.79 | $1,835 | $7,432 |
| **DAU (avg)** | ≈377 | ≈372 | ≈370 |
| **Liquidity pools** | 11,852 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,119.78 EASY** |
| Approx. USD | **≈$19.69** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
