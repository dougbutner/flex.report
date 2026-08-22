# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-22 13:25 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$50,622** |
| **EASY price** | **$0.0190** (≈6.58 XPR) |
| **EASY price in XUSDC** | **0.019084 XUSDC** |
| **Total EASY pools TVL** | **$2,339,587** |
| **Total USD backing (stables)** | **$82,127** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **850.48 EASY** (≈$16.14) in the reflection pool |
| **7d volume** | **$183,754** |
| **30d volume** | **$437,876** |
| **Flexers (holders on contract)** | **949** |
| **Market cap (fully circulating)** | **$398,572** |
| **Share of Alcor Proton swap volume (24h)** | **≈47.29%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $50,622 | $56,419 | **47.3%** |
| 7d | $183,754 | $259,253 | **41.5%** |
| 30d | $437,876 | $846,062 | **34.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $14,443 | $75,394 | 3,040,561 EASY | 17,685.39 XUSDC | -1.4% |
| EASY/XMD | $11,449 | $74,487 | 3,065,045 EASY | 16,529.40 XMD | -1.4% |
| EASY/XPR | $9,168 | $45,602 | 907,884 EASY | 9,836,664.90 XPR | -0.4% |
| EASY/XUSDT | $5,472 | $73,985 | 3,066,616 EASY | 15,528.52 XUSDT | -2.1% |
| EASY/XXRP | $3,881 | $12,883 | 370,764 EASY | 3,908.54 XXRP | -5.7% |
| EASY/XXLM | $1,263 | $1,159 | 37,452 EASY | 2,257.45 XXLM | -4.0% |
| EASY/XPYUSD | $965.30 | $58,967 | 3,106,875 EASY | 14,782.06 XPYUSD | +3.0% |
| EASY/XHBAR | $874.18 | $1,937 | 91,484 EASY | 2,615.47 XHBAR | -1.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,313 XMD | 3,065,045 EASY | $74,487 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,685 XUSDC | 3,040,561 EASY | $75,394 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,601 XPYUSD | 3,106,875 EASY | $58,967 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,041 XPAX | 3,261,253 EASY | $61,897 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,782 XUSDT | 3,066,616 EASY | $73,985 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,097,553 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,938,767 | - | - |
| **Swap volume** | $107,040 | $443,007 | $1,283,939 |
| **Spot volume** | $113.15 | $975.70 | $19,486 |
| **Swap fees** | $633.51 | $2,516 | $6,947 |
| **DAU (avg)** | ≈82 | ≈75 | ≈77 |
| **Liquidity pools** | 11,408 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **850.48 EASY** |
| Approx. USD | **≈$16.14** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
