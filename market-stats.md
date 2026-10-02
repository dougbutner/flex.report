# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-02 18:08 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$14,981** |
| **EASY price** | **$0.0185** (≈7.77 XPR) |
| **EASY price in XUSDC** | **0.018489 XUSDC** |
| **Total EASY pools TVL** | **$439,203** |
| **Total USD backing (stables)** | **$76,641** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **824.09 EASY** (≈$15.25) in the reflection pool |
| **7d volume** | **$70,074** |
| **30d volume** | **$447,216** |
| **Flexers (holders on contract)** | **1,004** |
| **Market cap (fully circulating)** | **$388,601** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.43%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $14,981 | $39,633 | **27.4%** |
| 7d | $70,074 | $203,778 | **25.6%** |
| 30d | $447,216 | $1,415,763 | **24.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,658 | $72,251 | 3,089,076 EASY | 15,109.14 XUSDC | +0.3% |
| EASY/XPR | $2,459 | $27,122 | 234,756 EASY | 9,569,496.00 XPR | -0.4% |
| EASY/XMD | $2,205 | $73,217 | 3,115,357 EASY | 15,583.70 XMD | +0.3% |
| EASY/XXRP | $1,997 | $20,521 | 422,751 EASY | 8,438.76 XXRP | -0.4% |
| EASY/METAL | $1,271 | $3,880 | 83,732 EASY | 19,129.17 METAL | -0.1% |
| EASY/XUSDT | $824.48 | $72,251 | 3,087,296 EASY | 15,141.78 XUSDT | +0.3% |
| EASY/XPYUSD | $678.91 | $57,146 | 3,089,273 EASY | 15,105.33 XPYUSD | +0.3% |
| EASY/XBTC | $464.40 | $3,665 | 165,705 EASY | 0.01 XBTC | -0.9% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,568 XMD | 3,115,357 EASY | $73,217 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,109 XUSDC | 3,089,076 EASY | $72,251 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,230 XPYUSD | 3,089,273 EASY | $57,146 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,763 XPAX | 3,136,290 EASY | $72,774 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,142 XUSDT | 3,087,296 EASY | $72,251 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,203,753 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,055,404 | - | - |
| **Swap volume** | $54,613 | $273,852 | $1,862,979 |
| **Spot volume** | $356.73 | $3,754 | $12,607 |
| **Swap fees** | $344.82 | $1,542 | $9,761 |
| **DAU (avg)** | ≈455 | ≈415 | ≈420 |
| **Liquidity pools** | 11,660 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **824.09 EASY** |
| Approx. USD | **≈$15.25** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
