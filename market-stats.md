# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-07-28 16:59 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$21,968** |
| **EASY price** | **$0.0163** (≈6.42 XPR) |
| **EASY price in XUSDC** | **0.016412 XUSDC** |
| **Total EASY pools TVL** | **$373,120** |
| **Total USD backing (stables)** | **$61,235** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **701.34 EASY** (≈$11.46) in the reflection pool |
| **7d volume** | **$99,129** |
| **30d volume** | **$398,005** |
| **Flexers (holders on contract)** | **898** |
| **Market cap (fully circulating)** | **$343,083** |
| **Share of Alcor Proton swap volume (24h)** | **≈44.1%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $21,968 | $27,848 | **44.1%** |
| 7d | $99,129 | $158,359 | **38.5%** |
| 30d | $398,005 | $950,193 | **29.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $7,149 | $65,374 | 3,278,897 EASY | 11,805.60 XUSDC | -0.8% |
| EASY/XMD | $5,360 | $65,324 | 3,278,333 EASY | 12,007.67 XMD | -0.8% |
| EASY/XPR | $3,221 | $23,757 | 777,022 EASY | 4,345,100.19 XPR | +0.3% |
| EASY/XUSDT | $1,930 | $65,135 | 3,277,592 EASY | 11,824.50 XUSDT | -0.8% |
| EASY/XXRP | $1,241 | $13,504 | 28,422 EASY | 12,550.09 XXRP | +1.1% |
| EASY/XUSDC | $1,210 | $8,856 | 344,153 EASY | 3,233.87 XUSDC | -1.2% |
| EASY/METAL | $881.92 | $4,171 | 26,344 EASY | 37,986.84 METAL | -0.8% |
| EASY/XMT | $481.22 | $1,702 | 18,979 EASY | 6,971.21 XMT | +1.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $11,765 XMD | 3,278,333 EASY | $65,324 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $11,806 XUSDC | 3,278,897 EASY | $65,374 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $11,381 XPYUSD | 3,319,264 EASY | $54,228 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $11,462 XPAX | 3,413,242 EASY | $55,763 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $11,588 XUSDT | 3,277,592 EASY | $65,135 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,106,958 | (snapshot) | (snapshot) |
| **Swap TVL** | $894,453 | - | - |
| **Swap volume** | $49,816 | $257,487 | $1,348,198 |
| **Spot volume** | $816.62 | $5,865 | $44,201 |
| **Swap fees** | $240.69 | $1,281 | $7,370 |
| **DAU (avg)** | ≈76 | ≈78 | ≈77 |
| **Liquidity pools** | 11,159 | - | - |
| **Spot pairs** | 1,603 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **701.34 EASY** |
| Approx. USD | **≈$11.46** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
