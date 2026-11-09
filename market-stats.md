# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-09 22:47 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$12,111** |
| **EASY price** | **$0.0176** (≈10.69 XPR) |
| **EASY price in XUSDC** | **0.017948 XUSDC** |
| **Total EASY pools TVL** | **$355,259** |
| **Total USD backing (stables)** | **$56,656** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **6,264.06 EASY** (≈$110.46) in the reflection pool |
| **7d volume** | **$53,005** |
| **30d volume** | **$476,373** |
| **Flexers (holders on contract)** | **6,064** |
| **Market cap (fully circulating)** | **$370,323** |
| **Share of Alcor Proton swap volume (24h)** | **≈23.15%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $12,111 | $40,200 | **23.1%** |
| 7d | $53,005 | $182,428 | **22.5%** |
| 30d | $476,373 | $892,653 | **34.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $4,669 | $69,556 | 3,135,334 EASY | 14,266.64 XUSDC | -0.1% |
| EASY/XPR | $2,683 | $14,163 | 346,502 EASY | 4,880,500.51 XPR | -0.3% |
| EASY/XXRP | $1,696 | $15,143 | 134,295 EASY | 11,874.60 XXRP | +2.6% |
| EASY/XUSDT | $960.39 | $69,558 | 3,196,707 EASY | 13,185.89 XUSDT | -3.1% |
| EASY/XPAX | $639.87 | $55,344 | 3,138,400 EASY | 14,273.71 XPAX | -0.2% |
| EASY/XXLM | $553.99 | $2,043 | 8,812 EASY | 12,971.23 XXLM | +0.8% |
| EASY/XPYUSD | $465.07 | $55,440 | 3,143,869 EASY | 14,113.42 XPYUSD | -0.6% |
| EASY/XMD | $132.49 | $38,553 | 2,157,508 EASY | 506.94 XMD | +0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $507.07 XMD | 2,157,508 EASY | $38,553 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,267 XUSDC | 3,135,334 EASY | $69,556 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,180 XPYUSD | 3,143,869 EASY | $55,440 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,378 XPAX | 3,138,400 EASY | $55,344 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,186 XUSDT | 3,196,707 EASY | $69,558 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $851,502 | (snapshot) | (snapshot) |
| **Swap TVL** | $760,675 | - | - |
| **Swap volume** | $52,310 | $235,433 | $1,369,026 |
| **Spot volume** | $70.65 | $523.10 | $5,750 |
| **Swap fees** | $309.10 | $1,350 | $7,145 |
| **DAU (avg)** | ≈364 | ≈344 | ≈373 |
| **Liquidity pools** | 11,844 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **6,264.06 EASY** |
| Approx. USD | **≈$110.46** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
