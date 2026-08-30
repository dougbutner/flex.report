# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-30 17:05 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,358** |
| **EASY price** | **$0.0186** (≈6.51 XPR) |
| **EASY price in XUSDC** | **0.018912 XUSDC** |
| **Total EASY pools TVL** | **$2,302,176** |
| **Total USD backing (stables)** | **$81,825** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **740.26 EASY** (≈$13.79) in the reflection pool |
| **7d volume** | **$138,199** |
| **30d volume** | **$493,254** |
| **Flexers (holders on contract)** | **953** |
| **Market cap (fully circulating)** | **$391,235** |
| **Share of Alcor Proton swap volume (24h)** | **≈21.01%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,358 | $20,148 | **21.0%** |
| 7d | $138,199 | $225,069 | **38.0%** |
| 30d | $493,254 | $921,062 | **34.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $1,228 | $73,501 | 3,079,165 EASY | 16,259.85 XMD | +0.4% |
| EASY/XUSDC | $965.26 | $73,400 | 3,054,365 EASY | 16,496.52 XUSDC | +0.3% |
| EASY/XPR | $753.66 | $48,861 | 1,001,517 EASY | 10,554,322.95 XPR | -0.1% |
| EASY/XUSDC | $537.83 | $5,912 | 227,449 EASY | 1,674.96 XUSDC | +0.0% |
| EASY/XXRP | $486.80 | $15,321 | 418,658 EASY | 5,417.11 XXRP | -0.7% |
| EASY/XBTC | $427.34 | $6,626 | 234,357 EASY | 0.03 XBTC | -0.4% |
| EASY/XPYUSD | $306.81 | $56,910 | 3,054,690 EASY | 15,751.73 XPYUSD | +0.3% |
| EASY/METAL | $195.10 | $3,231 | 148,080 EASY | 3,701.36 METAL | -0.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,136 XMD | 3,079,165 EASY | $73,501 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,497 XUSDC | 3,054,365 EASY | $73,400 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,888 XPYUSD | 3,054,690 EASY | $56,910 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,416 XPAX | 3,108,704 EASY | $57,916 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,726 XUSDT | 3,056,329 EASY | $72,666 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,045,118 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,884,706 | - | - |
| **Swap volume** | $25,505 | $363,268 | $1,414,316 |
| **Spot volume** | $398.25 | $1,513 | $12,838 |
| **Swap fees** | $128.24 | $2,028 | $7,813 |
| **DAU (avg)** | ≈77 | ≈76 | ≈77 |
| **Liquidity pools** | 11,463 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **740.26 EASY** |
| Approx. USD | **≈$13.79** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
