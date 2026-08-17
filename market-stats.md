# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-17 13:33 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,778** |
| **EASY price** | **$0.0168** (≈6.73 XPR) |
| **EASY price in XUSDC** | **0.017020 XUSDC** |
| **Total EASY pools TVL** | **$2,077,958** |
| **Total USD backing (stables)** | **$67,892** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,156.46 EASY** (≈$19.41) in the reflection pool |
| **7d volume** | **$58,918** |
| **30d volume** | **$349,742** |
| **Flexers (holders on contract)** | **942** |
| **Market cap (fully circulating)** | **$352,432** |
| **Share of Alcor Proton swap volume (24h)** | **≈28.84%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,778 | $24,123 | **28.8%** |
| 7d | $58,918 | $164,856 | **26.3%** |
| 30d | $349,742 | $747,783 | **31.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $3,306 | $66,679 | 3,219,123 EASY | 12,806.86 XMD | +0.6% |
| EASY/XUSDC | $1,796 | $69,827 | 3,219,705 EASY | 15,829.91 XUSDC | +0.6% |
| EASY/XXRP | $1,088 | $13,070 | 192,050 EASY | 9,867.78 XXRP | +0.5% |
| EASY/XUSDT | $1,001 | $66,810 | 3,224,593 EASY | 12,708.84 XUSDT | +0.5% |
| EASY/METAL | $820.42 | $3,433 | 143,225 EASY | 10,204.59 METAL | -0.8% |
| EASY/XPR | $778.50 | $33,516 | 827,879 EASY | 7,782,728.16 XPR | -0.2% |
| EASY/XMD | $386.08 | $2,494 | 77,093 EASY | 1,211.68 XMD | +0.6% |
| EASY/XSOL | $133.12 | - | 1,680 EASY | 8.61 XSOL | +1.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,701 XMD | 3,219,123 EASY | $66,679 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,830 XUSDC | 3,219,705 EASY | $69,827 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,539 XPYUSD | 3,236,618 EASY | $54,281 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,849 XPAX | 3,290,977 EASY | $55,192 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,735 XUSDT | 3,224,593 EASY | $66,810 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $2,744,134 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,604,184 | - | - |
| **Swap volume** | $33,902 | $223,774 | $1,097,525 |
| **Spot volume** | $187.30 | $1,734 | $32,828 |
| **Swap fees** | $168.79 | $1,139 | $5,709 |
| **DAU (avg)** | ≈75 | ≈76 | ≈78 |
| **Liquidity pools** | 11,352 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,156.46 EASY** |
| Approx. USD | **≈$19.41** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
