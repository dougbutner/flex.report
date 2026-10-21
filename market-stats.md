# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-21 17:47 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$22,590** |
| **EASY price** | **$0.0183** (≈9.68 XPR) |
| **EASY price in XUSDC** | **0.018558 XUSDC** |
| **Total EASY pools TVL** | **$410,207** |
| **Total USD backing (stables)** | **$73,992** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,542.22 EASY** (≈$28.19) in the reflection pool |
| **7d volume** | **$225,348** |
| **30d volume** | **$482,080** |
| **Flexers (holders on contract)** | **6,050** |
| **Market cap (fully circulating)** | **$383,816** |
| **Share of Alcor Proton swap volume (24h)** | **≈36.39%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $22,590 | $39,486 | **36.4%** |
| 7d | $225,348 | $260,499 | **46.4%** |
| 30d | $482,080 | $948,423 | **33.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $8,116 | $29,225 | 405,245 EASY | 11,549,676.24 XPR | -6.8% |
| EASY/XUSDC | $4,907 | $71,574 | 3,083,463 EASY | 15,217.72 XUSDC | +4.6% |
| EASY/XMD | $3,697 | $72,238 | 3,108,996 EASY | 15,706.39 XMD | +4.6% |
| EASY/XXRP | $1,849 | $24,914 | 635,874 EASY | 9,965.87 XXRP | +0.7% |
| EASY/XUSDT | $1,740 | $71,580 | 3,153,678 EASY | 13,940.42 XUSDT | +1.5% |
| EASY/XBTC | $764.94 | $6,577 | 298,684 EASY | 0.01 XBTC | +3.2% |
| EASY/XPYUSD | $266.30 | $57,722 | 3,158,212 EASY | 13,859.76 XPYUSD | -0.1% |
| EASY/XXLM | $262.93 | $1,696 | 35,608 EASY | 5,715.74 XXLM | +2.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,415 XMD | 3,108,996 EASY | $72,238 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,218 XUSDC | 3,083,463 EASY | $71,574 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,680 XPYUSD | 3,158,212 EASY | $57,722 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,506 XPAX | 3,156,312 EASY | $57,688 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,940 XUSDT | 3,153,678 EASY | $71,580 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $986,894 | (snapshot) | (snapshot) |
| **Swap TVL** | $874,223 | - | - |
| **Swap volume** | $62,076 | $485,847 | $1,430,503 |
| **Spot volume** | $31.32 | $845.92 | $9,323 |
| **Swap fees** | $238.79 | $2,458 | $7,550 |
| **DAU (avg)** | ≈357 | ≈394 | ≈408 |
| **Liquidity pools** | 11,794 | - | - |
| **Spot pairs** | 1,676 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,542.22 EASY** |
| Approx. USD | **≈$28.19** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
