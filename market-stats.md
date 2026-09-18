# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-18 16:50 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$18,812** |
| **EASY price** | **$0.0181** (≈7.15 XPR) |
| **EASY price in XUSDC** | **0.018243 XUSDC** |
| **Total EASY pools TVL** | **$413,965** |
| **Total USD backing (stables)** | **$73,917** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,352.64 EASY** (≈$24.45) in the reflection pool |
| **7d volume** | **$138,801** |
| **30d volume** | **$624,764** |
| **Flexers (holders on contract)** | **974** |
| **Market cap (fully circulating)** | **$379,565** |
| **Share of Alcor Proton swap volume (24h)** | **≈38.07%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $18,812 | $30,597 | **38.1%** |
| 7d | $138,801 | $411,506 | **25.2%** |
| 30d | $624,764 | $1,326,877 | **32.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $4,718 | $70,919 | 3,109,918 EASY | 14,728.50 XUSDC | +0.9% |
| EASY/XMD | $4,601 | $71,527 | 3,134,568 EASY | 15,232.69 XMD | +1.0% |
| EASY/XPR | $2,464 | $21,276 | 184,179 EASY | 7,101,158.25 XPR | -0.2% |
| EASY/XUSDT | $2,226 | $70,663 | 3,112,025 EASY | 14,688.77 XUSDT | +0.9% |
| EASY/XXRP | $1,441 | $15,651 | 468,429 EASY | 5,324.45 XXRP | -1.7% |
| EASY/XBTC | $1,167 | $6,759 | 314,306 EASY | 0.01 XBTC | -2.0% |
| EASY/XSOL | $485.11 | $944.49 | 17,447 EASY | 5.84 XSOL | -3.6% |
| EASY/XDOGE | $342.35 | $1,447 | 51,306 EASY | 6,082.98 XDOGE | -2.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,900 XMD | 3,134,568 EASY | $71,527 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,728 XUSDC | 3,109,918 EASY | $70,919 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,872 XPYUSD | 3,110,054 EASY | $56,213 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,375 XPAX | 3,136,867 EASY | $56,758 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,444 XUSDT | 3,112,025 EASY | $70,663 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,156,637 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,005,154 | - | - |
| **Swap volume** | $49,408 | $550,307 | $1,951,641 |
| **Spot volume** | $516.19 | $2,922 | $9,504 |
| **Swap fees** | $238.59 | $2,710 | $10,292 |
| **DAU (avg)** | ≈75 | ≈76 | ≈76 |
| **Liquidity pools** | 11,581 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,352.64 EASY** |
| Approx. USD | **≈$24.45** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
