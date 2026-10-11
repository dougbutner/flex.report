# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-11 17:51 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$3,974** |
| **EASY price** | **$0.0183** (≈8.06 XPR) |
| **EASY price in XUSDC** | **0.018342 XUSDC** |
| **Total EASY pools TVL** | **$397,255** |
| **Total USD backing (stables)** | **$74,566** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,565.91 EASY** (≈$28.67) in the reflection pool |
| **7d volume** | **$93,826** |
| **30d volume** | **$442,699** |
| **Flexers (holders on contract)** | **1,016** |
| **Market cap (fully circulating)** | **$384,434** |
| **Share of Alcor Proton swap volume (24h)** | **≈14.99%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $3,974 | $22,538 | **15.0%** |
| 7d | $93,826 | $214,161 | **30.5%** |
| 30d | $442,699 | $1,373,155 | **24.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $982.20 | $71,658 | 3,101,465 EASY | 14,881.03 XUSDC | -0.3% |
| EASY/XMD | $871.59 | $72,376 | 3,126,504 EASY | 15,378.59 XMD | -0.2% |
| EASY/XPR | $597.17 | $24,036 | 526,301 EASY | 6,346,909.69 XPR | -0.2% |
| EASY/XUSDT | $521.73 | $71,657 | 3,104,461 EASY | 14,825.92 XUSDT | +0.0% |
| EASY/METAL | $206.02 | $2,289 | 49,024 EASY | 11,600.56 METAL | +0.5% |
| EASY/XXLM | $180.80 | $1,768 | 70,375 EASY | 2,390.84 XXLM | -1.4% |
| EASY/XPYUSD | $143.98 | $56,775 | 3,101,387 EASY | 14,882.19 XPYUSD | -0.2% |
| EASY/XSOL | $120.06 | $979.91 | 15,224 EASY | 6.39 XSOL | -0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,147 XMD | 3,126,504 EASY | $72,376 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,881 XUSDC | 3,101,465 EASY | $71,658 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,805 XPYUSD | 3,101,387 EASY | $56,775 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,546 XPAX | 3,136,863 EASY | $57,425 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,826 XUSDT | 3,104,461 EASY | $71,657 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,147,043 | (snapshot) | (snapshot) |
| **Swap TVL** | $997,345 | - | - |
| **Swap volume** | $26,512 | $307,987 | $1,815,854 |
| **Spot volume** | $100.02 | $2,151 | $12,630 |
| **Swap fees** | $133.15 | $1,656 | $9,640 |
| **DAU (avg)** | ≈402 | ≈410 | ≈418 |
| **Liquidity pools** | 11,694 | - | - |
| **Spot pairs** | 1,673 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,565.91 EASY** |
| Approx. USD | **≈$28.67** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
