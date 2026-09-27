# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-27 17:22 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$11,398** |
| **EASY price** | **$0.0185** (≈7.47 XPR) |
| **EASY price in XUSDC** | **0.018585 XUSDC** |
| **Total EASY pools TVL** | **$455,972** |
| **Total USD backing (stables)** | **$77,338** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,659.33 EASY** (≈$30.77) in the reflection pool |
| **7d volume** | **$93,762** |
| **30d volume** | **$481,373** |
| **Flexers (holders on contract)** | **986** |
| **Market cap (fully circulating)** | **$389,464** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.93%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $11,398 | $29,415 | **27.9%** |
| 7d | $93,762 | $211,068 | **30.8%** |
| 30d | $481,373 | $1,484,645 | **24.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,084 | $72,402 | 3,081,198 EASY | 15,258.32 XUSDC | -0.4% |
| EASY/XMD | $2,340 | $73,339 | 3,108,073 EASY | 15,721.84 XMD | -0.4% |
| EASY/XUSDT | $1,882 | $72,295 | 3,078,775 EASY | 15,301.56 XUSDT | -0.5% |
| EASY/XPR | $1,040 | $41,363 | 412,479 EASY | 13,576,178.67 XPR | +0.1% |
| EASY/XBTC | $918.66 | $3,648 | 160,447 EASY | 0.01 XBTC | -0.9% |
| EASY/XXRP | $854.85 | $19,893 | 414,642 EASY | 8,005.28 XXRP | +0.6% |
| EASY/XPYUSD | $482.13 | $57,154 | 3,081,778 EASY | 15,244.81 XPYUSD | +1.0% |
| EASY/METAL | $441.77 | $3,370 | 95,961 EASY | 12,215.34 METAL | -0.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,697 XMD | 3,108,073 EASY | $73,339 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,258 XUSDC | 3,081,198 EASY | $72,402 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,393 XPYUSD | 3,081,778 EASY | $57,154 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,831 XPAX | 3,135,993 EASY | $72,991 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,196 XUSDT | 3,078,775 EASY | $72,295 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,255,024 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,097,150 | - | - |
| **Swap volume** | $40,813 | $304,830 | $1,966,018 |
| **Spot volume** | $69.40 | $913.29 | $11,408 |
| **Swap fees** | $218.45 | $1,516 | $10,232 |
| **DAU (avg)** | ≈409 | ≈416 | ≈421 |
| **Liquidity pools** | 11,632 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,659.33 EASY** |
| Approx. USD | **≈$30.77** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
