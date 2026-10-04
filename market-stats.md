# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-04 17:12 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,726** |
| **EASY price** | **$0.0184** (≈7.77 XPR) |
| **EASY price in XUSDC** | **0.018467 XUSDC** |
| **Total EASY pools TVL** | **$421,229** |
| **Total USD backing (stables)** | **$76,205** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,794.12 EASY** (≈$33.03) in the reflection pool |
| **7d volume** | **$66,738** |
| **30d volume** | **$428,007** |
| **Flexers (holders on contract)** | **1,007** |
| **Market cap (fully circulating)** | **$386,555** |
| **Share of Alcor Proton swap volume (24h)** | **≈18.46%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,726 | $25,289 | **18.5%** |
| 7d | $66,738 | $207,010 | **24.4%** |
| 30d | $428,007 | $1,398,973 | **23.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $1,437 | $72,913 | 3,115,931 EASY | 15,573.80 XMD | +0.0% |
| EASY/XPR | $1,225 | $25,833 | 187,897 EASY | 9,455,330.91 XPR | -0.4% |
| EASY/XUSDC | $1,040 | $71,972 | 3,090,923 EASY | 15,075.75 XUSDC | -0.0% |
| EASY/METAL | $538.66 | $3,922 | 114,073 EASY | 14,631.90 METAL | -0.6% |
| EASY/XUSDT | $430.49 | $71,921 | 3,102,675 EASY | 14,858.79 XUSDT | -0.1% |
| EASY/XXRP | $249.03 | $20,346 | 366,158 EASY | 9,133.20 XXRP | -0.2% |
| EASY/XSOL | $247.97 | $1,032 | 22,376 EASY | 5.08 XSOL | -6.3% |
| EASY/XPYUSD | $182.74 | $56,847 | 3,090,989 EASY | 15,073.72 XPYUSD | +0.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,621 XMD | 3,115,931 EASY | $72,913 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,076 XUSDC | 3,090,923 EASY | $71,972 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,105 XPYUSD | 3,090,989 EASY | $56,847 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,733 XPAX | 3,136,359 EASY | $57,682 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,859 XUSDT | 3,102,675 EASY | $71,921 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,174,237 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,024,491 | - | - |
| **Swap volume** | $31,015 | $273,748 | $1,826,980 |
| **Spot volume** | $166.03 | $4,241 | $12,798 |
| **Swap fees** | $165.63 | $1,555 | $9,551 |
| **DAU (avg)** | ≈409 | ≈416 | ≈421 |
| **Liquidity pools** | 11,672 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,794.12 EASY** |
| Approx. USD | **≈$33.03** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
