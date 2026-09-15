# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-15 17:24 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$17,252** |
| **EASY price** | **$0.0182** (≈7.12 XPR) |
| **EASY price in XUSDC** | **0.018238 XUSDC** |
| **Total EASY pools TVL** | **$409,010** |
| **Total USD backing (stables)** | **$75,949** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,106.61 EASY** (≈$20.09) in the reflection pool |
| **7d volume** | **$125,852** |
| **30d volume** | **$611,713** |
| **Flexers (holders on contract)** | **969** |
| **Market cap (fully circulating)** | **$381,165** |
| **Share of Alcor Proton swap volume (24h)** | **≈25.88%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $17,252 | $49,407 | **25.9%** |
| 7d | $125,852 | $393,554 | **24.2%** |
| 30d | $611,713 | $1,278,375 | **32.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $5,054 | $72,022 | 3,136,600 EASY | 15,194.78 XMD | -0.5% |
| EASY/XXRP | $3,040 | $17,172 | 597,130 EASY | 4,557.24 XXRP | -0.5% |
| EASY/XUSDC | $2,353 | $71,174 | 3,110,335 EASY | 14,719.43 XUSDC | -0.5% |
| EASY/XPR | $1,825 | $30,275 | 173,215 EASY | 10,643,545.62 XPR | -0.7% |
| EASY/XUSDT | $1,490 | $71,028 | 3,099,315 EASY | 14,920.38 XUSDT | +0.3% |
| EASY/XPR | $961.26 | $847.37 | 7,344 EASY | 280,129.95 XPR | -0.9% |
| EASY/XBTC | $866.92 | $6,844 | 273,193 EASY | 0.02 XBTC | +0.0% |
| EASY/XXLM | $522.37 | $4,027 | 173,315 EASY | 4,585.84 XXLM | -0.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,090 XMD | 3,136,600 EASY | $72,022 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,719 XUSDC | 3,110,335 EASY | $71,174 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,746 XPYUSD | 3,111,438 EASY | $56,475 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,561 XPAX | 3,120,002 EASY | $56,630 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,773 XUSDT | 3,099,315 EASY | $71,028 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,162,358 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,009,166 | - | - |
| **Swap volume** | $66,660 | $519,406 | $1,890,088 |
| **Spot volume** | $58.29 | $2,848 | $9,013 |
| **Swap fees** | $337.43 | $2,509 | $9,969 |
| **DAU (avg)** | ≈75 | ≈76 | ≈76 |
| **Liquidity pools** | 11,565 | - | - |
| **Spot pairs** | 1,668 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,106.61 EASY** |
| Approx. USD | **≈$20.09** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
