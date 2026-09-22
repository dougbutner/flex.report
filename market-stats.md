# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-22 17:27 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$12,660** |
| **EASY price** | **$0.0189** (≈7.30 XPR) |
| **EASY price in XUSDC** | **0.018873 XUSDC** |
| **Total EASY pools TVL** | **$439,565** |
| **Total USD backing (stables)** | **$78,479** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **937.50 EASY** (≈$17.73) in the reflection pool |
| **7d volume** | **$135,210** |
| **30d volume** | **$545,172** |
| **Flexers (holders on contract)** | **981** |
| **Market cap (fully circulating)** | **$397,057** |
| **Share of Alcor Proton swap volume (24h)** | **≈37.89%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $12,660 | $20,754 | **37.9%** |
| 7d | $135,210 | $496,197 | **21.4%** |
| 30d | $545,172 | $1,501,322 | **26.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,815 | $73,658 | 3,057,526 EASY | 15,700.36 XUSDC | +0.3% |
| EASY/XMD | $2,885 | $74,729 | 3,081,718 EASY | 16,213.49 XMD | +0.3% |
| EASY/XUSDT | $2,581 | $73,450 | 3,040,971 EASY | 16,013.63 XUSDT | +0.8% |
| EASY/XPR | $880.86 | $24,150 | 132,196 EASY | 8,325,717.10 XPR | +0.1% |
| EASY/XXRP | $640.71 | $17,489 | 575,614 EASY | 4,223.20 XXRP | -1.8% |
| EASY/METAL | $603.81 | $6,613 | 116,844 EASY | 33,504.48 METAL | -0.0% |
| EASY/XXLM | $524.27 | $4,246 | 212,550 EASY | 1,000.72 XXLM | -0.8% |
| EASY/XSOL | $493.70 | $1,014 | 18,770 EASY | 5.62 XSOL | +0.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,213 XMD | 3,081,718 EASY | $74,729 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,700 XUSDC | 3,057,526 EASY | $73,658 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,869 XPYUSD | 3,137,322 EASY | $59,517 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,898 XPAX | 3,136,165 EASY | $59,495 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,766 XUSDT | 3,040,971 EASY | $73,450 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,243,270 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,079,514 | - | - |
| **Swap volume** | $33,414 | $631,406 | $2,046,493 |
| **Spot volume** | $26.05 | $3,330 | $11,523 |
| **Swap fees** | $133.80 | $3,456 | $10,804 |
| **DAU (avg)** | ≈73 | ≈73 | ≈75 |
| **Liquidity pools** | 11,611 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **937.50 EASY** |
| Approx. USD | **≈$17.73** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
