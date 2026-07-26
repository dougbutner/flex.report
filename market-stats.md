# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-07-26 06:37 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$3,613** |
| **EASY price** | **$0.0165** (~6.46 XPR) |
| **EASY price in XUSDC** | **0.016639 XUSDC** |
| **Total EASY pools TVL** | **$386,082** |
| **Total USD backing (stables)** | **$63,302** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **2,804.82 EASY** (~$46.35) in the reflection pool |
| **7d volume** | **$104,783** |
| **30d volume** | **$382,802** |
| **Flexers (holders on contract)** | **892** |
| **Market cap (fully circulating)** | **$347,019** |
| **Share of Alcor Proton swap volume (24h)** | **~19.3%** |

USDC-style rewards dashboards inspired this layout: **liquidity**, **pending rewards**, and **volume that feeds holders**.

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $3,613 | $15,107 | **19.3%** |
| 7d | $104,783 | $159,200 | **39.7%** |
| 30d | $382,802 | $944,434 | **28.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $990.64 | $66,119 | 3,258,203 EASY | 12,338.43 XMD | +0.3% |
| EASY/XPR | $889.54 | $23,939 | 663,995 EASY | 5,055,615.51 XPR | +0.2% |
| EASY/XUSDC | $713.63 | $65,985 | 3,256,358 EASY | 12,174.97 XUSDC | +0.3% |
| EASY/XSOL | $280.93 | - | 4,184 EASY | 8.40 XSOL | -0.6% |
| EASY/XUSDT | $200.40 | $66,020 | 3,258,390 EASY | 12,140.95 XUSDT | +0.2% |
| EASY/METAL | $78.24 | $9,082 | 36,374 EASY | 80,637.19 METAL | +0.0% |
| EASY/XXRP | $76.79 | $14,268 | 116,669 EASY | 11,209.70 XXRP | +0.0% |
| EASY/XDOGE | $67.57 | $357.44 | 2,364 EASY | 4,441.63 XDOGE | -1.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,278 XMD | 3,258,203 EASY | $66,119 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,175 XUSDC | 3,256,358 EASY | $65,985 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $11,503 XPYUSD | 3,320,156 EASY | $54,940 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $11,743 XPAX | 3,413,113 EASY | $56,478 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,085 XUSDT | 3,258,390 EASY | $66,020 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,879,457 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,709,478 | - | - |
| **Swap volume** | $18,720 | $263,983 | $1,327,236 |
| **Spot volume** | $2,061 | $10,191 | $42,792 |
| **Swap fees** | $107.40 | $1,325 | $7,255 |
| **DAU (avg)** | ~74 | ~79 | ~77 |
| **Liquidity pools** | 11,147 | - | - |
| **Spot pairs** | 1,603 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **2,804.82 EASY** |
| Approx. USD | **~$46.35** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
