# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-09 13:42 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,684** |
| **EASY price** | **$0.0166** (≈6.60 XPR) |
| **EASY price in XUSDC** | **0.016913 XUSDC** |
| **Total EASY pools TVL** | **$385,202** |
| **Total USD backing (stables)** | **$63,015** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **941.62 EASY** (≈$15.67) in the reflection pool |
| **7d volume** | **$77,744** |
| **30d volume** | **$392,069** |
| **Flexers (holders on contract)** | **937** |
| **Market cap (fully circulating)** | **$349,482** |
| **Share of Alcor Proton swap volume (24h)** | **≈28.68%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,684 | $24,085 | **28.7%** |
| 7d | $77,744 | $160,859 | **32.6%** |
| 30d | $392,069 | $923,721 | **29.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XXRP | $2,398 | $19,014 | 290,774 EASY | 13,920.13 XXRP | -0.0% |
| EASY/XMD | $2,193 | $66,149 | 3,228,947 EASY | 12,639.85 XMD | +0.2% |
| EASY/XUSDC | $1,970 | $66,300 | 3,229,935 EASY | 12,618.73 XUSDC | +0.1% |
| EASY/XPR | $1,654 | $25,280 | 515,409 EASY | 6,636,508.62 XPR | -0.5% |
| EASY/XMT | $353.05 | $3,287 | 42,995 EASY | 12,337.74 XMT | +0.4% |
| EASY/XUSDT | $345.34 | $66,516 | 3,259,771 EASY | 12,118.06 XUSDT | -0.2% |
| EASY/XDOGE | $166.18 | $348.86 | 718 EASY | 4,837.33 XDOGE | +0.1% |
| EASY/XBTC | $165.26 | $2,766 | 30,522 EASY | 0.04 XBTC | -0.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,500 XMD | 3,228,947 EASY | $66,149 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,619 XUSDC | 3,229,935 EASY | $66,300 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,719 XPYUSD | 3,229,359 EASY | $53,672 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,798 XPAX | 3,291,210 EASY | $54,700 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,338 XUSDT | 3,259,771 EASY | $66,516 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,075,735 | (snapshot) | (snapshot) |
| **Swap TVL** | $936,382 | - | - |
| **Swap volume** | $33,769 | $238,603 | $1,315,789 |
| **Spot volume** | $872.80 | $2,654 | $52,441 |
| **Swap fees** | $198.96 | $1,185 | $6,856 |
| **DAU (avg)** | ≈80 | ≈78 | ≈79 |
| **Liquidity pools** | 11,256 | - | - |
| **Spot pairs** | 1,653 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **941.62 EASY** |
| Approx. USD | **≈$15.67** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
