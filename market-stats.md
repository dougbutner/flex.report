# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-25 13:41 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$12,675** |
| **EASY price** | **$0.0185** (≈6.58 XPR) |
| **EASY price in XUSDC** | **0.018790 XUSDC** |
| **Total EASY pools TVL** | **$2,278,716** |
| **Total USD backing (stables)** | **$81,159** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **851.85 EASY** (≈$15.73) in the reflection pool |
| **7d volume** | **$216,470** |
| **30d volume** | **$462,366** |
| **Flexers (holders on contract)** | **950** |
| **Market cap (fully circulating)** | **$387,840** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.07%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $12,675 | $30,934 | **29.1%** |
| 7d | $216,470 | $290,073 | **42.7%** |
| 30d | $462,366 | $869,041 | **34.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $2,796 | $72,995 | 3,091,116 EASY | 16,035.31 XMD | -0.2% |
| EASY/XPR | $2,579 | $42,968 | 853,393 EASY | 9,683,326.64 XPR | -0.0% |
| EASY/XUSDC | $2,494 | $73,854 | 3,083,290 EASY | 16,877.86 XUSDC | -0.2% |
| EASY/XUSDT | $1,264 | $72,001 | 3,060,670 EASY | 15,639.48 XUSDT | -0.0% |
| EASY/XXRP | $1,249 | $12,553 | 350,378 EASY | 4,160.42 XXRP | +0.6% |
| EASY/XBTC | $1,179 | $4,640 | 206,884 EASY | 0.01 XBTC | -0.5% |
| EASY/XXLM | $283.92 | $1,140 | 34,400 EASY | 2,638.36 XXLM | +0.8% |
| EASY/XHBAR | $195.70 | $423.34 | 22,852 EASY | 13.17 XHBAR | -1.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,865 XMD | 3,091,116 EASY | $72,995 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,878 XUSDC | 3,083,290 EASY | $73,854 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,239 XPYUSD | 3,092,106 EASY | $57,139 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $16,002 XPAX | 3,141,428 EASY | $58,051 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,434 XUSDT | 3,060,670 EASY | $72,001 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,020,584 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,863,579 | - | - |
| **Swap volume** | $43,609 | $506,543 | $1,331,407 |
| **Spot volume** | $143.78 | $1,101 | $16,441 |
| **Swap fees** | $290.91 | $2,879 | $7,200 |
| **DAU (avg)** | ≈78 | ≈77 | ≈77 |
| **Liquidity pools** | 11,429 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **851.85 EASY** |
| Approx. USD | **≈$15.73** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
