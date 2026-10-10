# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-10 17:33 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,811** |
| **EASY price** | **$0.0183** (≈8.04 XPR) |
| **EASY price in XUSDC** | **0.018445 XUSDC** |
| **Total EASY pools TVL** | **$397,341** |
| **Total USD backing (stables)** | **$75,137** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,061.24 EASY** (≈$19.42) in the reflection pool |
| **7d volume** | **$95,628** |
| **30d volume** | **$455,568** |
| **Flexers (holders on contract)** | **1,015** |
| **Market cap (fully circulating)** | **$384,252** |
| **Share of Alcor Proton swap volume (24h)** | **≈23.67%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,811 | $18,738 | **23.7%** |
| 7d | $95,628 | $220,792 | **30.2%** |
| 30d | $455,568 | $1,387,512 | **24.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,926 | $71,644 | 3,092,903 EASY | 15,043.23 XUSDC | +0.3% |
| EASY/XPR | $1,086 | $24,098 | 549,237 EASY | 6,167,428.16 XPR | +0.4% |
| EASY/XMD | $682.02 | $72,487 | 3,118,298 EASY | 15,532.20 XMD | +0.3% |
| EASY/XUSDT | $623.81 | $71,640 | 3,105,240 EASY | 14,813.04 XUSDT | +0.3% |
| EASY/XXRP | $517.09 | $15,347 | 380,085 EASY | 5,991.42 XXRP | -0.3% |
| EASY/XPYUSD | $204.10 | $56,633 | 3,093,111 EASY | 15,035.63 XPYUSD | +0.3% |
| EASY/XXLM | $183.16 | $1,753 | 61,482 EASY | 3,209.06 XXLM | -0.4% |
| EASY/METAL | $126.98 | $2,316 | 57,435 EASY | 10,324.21 METAL | -0.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,417 XMD | 3,118,298 EASY | $72,487 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,043 XUSDC | 3,092,903 EASY | $71,644 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,951 XPYUSD | 3,093,111 EASY | $56,633 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,553 XPAX | 3,136,869 EASY | $57,434 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,813 XUSDT | 3,105,240 EASY | $71,640 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,148,099 | (snapshot) | (snapshot) |
| **Swap TVL** | $998,236 | - | - |
| **Swap volume** | $24,549 | $316,420 | $1,843,080 |
| **Spot volume** | $172.59 | $2,220 | $12,679 |
| **Swap fees** | $129.01 | $1,706 | $9,789 |
| **DAU (avg)** | ≈423 | ≈412 | ≈419 |
| **Liquidity pools** | 11,691 | - | - |
| **Spot pairs** | 1,673 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,061.24 EASY** |
| Approx. USD | **≈$19.42** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
