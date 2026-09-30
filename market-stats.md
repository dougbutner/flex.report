# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-30 18:13 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,053** |
| **EASY price** | **$0.0184** (≈7.69 XPR) |
| **EASY price in XUSDC** | **0.018488 XUSDC** |
| **Total EASY pools TVL** | **$439,192** |
| **Total USD backing (stables)** | **$76,584** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,076.39 EASY** (≈$19.83) in the reflection pool |
| **7d volume** | **$78,074** |
| **30d volume** | **$459,600** |
| **Flexers (holders on contract)** | **997** |
| **Market cap (fully circulating)** | **$386,856** |
| **Share of Alcor Proton swap volume (24h)** | **≈26.17%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,053 | $28,356 | **26.2%** |
| 7d | $78,074 | $190,247 | **29.1%** |
| 30d | $459,600 | $1,439,621 | **24.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,507 | $72,201 | 3,089,211 EASY | 15,292.85 XUSDC | +0.2% |
| EASY/XPR | $2,076 | $27,250 | 274,550 EASY | 9,268,103.12 XPR | -0.9% |
| EASY/XMD | $1,905 | $72,909 | 3,114,600 EASY | 15,600.03 XMD | +0.2% |
| EASY/XXRP | $1,160 | $20,470 | 416,420 EASY | 8,511.02 XXRP | -0.2% |
| EASY/GEASY | $803.91 | $17,346 | 258,792 EASY | 265,565,163.27 GEASY | -0.1% |
| EASY/XUSDT | $406.28 | $71,991 | 3,087,790 EASY | 15,133.21 XUSDT | +0.3% |
| EASY/XPYUSD | $356.49 | $56,911 | 3,089,327 EASY | 15,105.16 XPYUSD | +0.2% |
| EASY/METAL | $171.87 | $3,903 | 113,013 EASY | 14,641.87 METAL | +0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,533 XMD | 3,114,600 EASY | $72,909 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,293 XUSDC | 3,089,211 EASY | $72,201 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,150 XPYUSD | 3,089,327 EASY | $56,911 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,615 XPAX | 3,136,149 EASY | $72,388 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,108 XUSDT | 3,087,790 EASY | $71,991 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,198,175 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,049,204 | - | - |
| **Swap volume** | $38,409 | $268,321 | $1,899,222 |
| **Spot volume** | $1,385 | $3,137 | $12,732 |
| **Swap fees** | $208.57 | $1,445 | $9,961 |
| **DAU (avg)** | ≈383 | ≈410 | ≈419 |
| **Liquidity pools** | 11,639 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,076.39 EASY** |
| Approx. USD | **≈$19.83** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
