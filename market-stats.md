# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-08 13:39 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,946** |
| **EASY price** | **$0.0166** (≈6.53 XPR) |
| **EASY price in XUSDC** | **0.016861 XUSDC** |
| **Total EASY pools TVL** | **$384,679** |
| **Total USD backing (stables)** | **$62,937** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **950.22 EASY** (≈$15.78) in the reflection pool |
| **7d volume** | **$76,238** |
| **30d volume** | **$398,294** |
| **Flexers (holders on contract)** | **936** |
| **Market cap (fully circulating)** | **$348,819** |
| **Share of Alcor Proton swap volume (24h)** | **≈25.73%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,946 | $25,824 | **25.7%** |
| 7d | $76,238 | $157,443 | **32.6%** |
| 30d | $398,294 | $939,505 | **29.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $2,598 | $66,222 | 3,234,259 EASY | 12,549.65 XMD | -0.3% |
| EASY/XUSDC | $1,695 | $66,268 | 3,234,849 EASY | 12,535.47 XUSDC | -0.3% |
| EASY/XXRP | $1,542 | $19,125 | 174,504 EASY | 15,975.84 XXRP | +0.8% |
| EASY/XUSDT | $1,302 | $66,393 | 3,252,830 EASY | 12,233.57 XUSDT | -0.7% |
| EASY/XPR | $601.10 | $24,602 | 558,743 EASY | 6,026,429.71 XPR | -0.2% |
| EASY/XMT | $321.63 | $3,305 | 48,708 EASY | 11,887.04 XMT | -1.3% |
| EASY/METAL | $246.31 | $3,603 | 69,866 EASY | 24,299.73 METAL | +0.0% |
| EASY/XPYUSD | $167.79 | $53,730 | 3,234,717 EASY | 12,537.28 XPYUSD | -0.3% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,500 XMD | 3,234,259 EASY | $66,222 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,535 XUSDC | 3,234,849 EASY | $66,268 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,636 XPYUSD | 3,234,717 EASY | $53,730 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,863 XPAX | 3,291,202 EASY | $54,668 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,362 XUSDT | 3,252,830 EASY | $66,393 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,074,145 | (snapshot) | (snapshot) |
| **Swap TVL** | $934,453 | - | - |
| **Swap volume** | $34,770 | $233,681 | $1,337,799 |
| **Spot volume** | $480.29 | $2,065 | $51,992 |
| **Swap fees** | $154.56 | $1,128 | $6,994 |
| **DAU (avg)** | ≈81 | ≈78 | ≈79 |
| **Liquidity pools** | 11,253 | - | - |
| **Spot pairs** | 1,644 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **950.22 EASY** |
| Approx. USD | **≈$15.78** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
