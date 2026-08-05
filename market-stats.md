# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-05 15:09 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,910** |
| **EASY price** | **$0.0167** (≈6.57 XPR) |
| **EASY price in XUSDC** | **0.016939 XUSDC** |
| **Total EASY pools TVL** | **$400,028** |
| **Total USD backing (stables)** | **$63,297** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **740.43 EASY** (≈$12.37) in the reflection pool |
| **7d volume** | **$73,622** |
| **30d volume** | **$376,755** |
| **Flexers (holders on contract)** | **930** |
| **Market cap (fully circulating)** | **$350,736** |
| **Share of Alcor Proton swap volume (24h)** | **≈36.86%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,910 | $11,835 | **36.9%** |
| 7d | $73,622 | $205,389 | **26.4%** |
| 30d | $376,755 | $917,923 | **29.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,106 | $66,598 | 3,227,396 EASY | 12,662.29 XUSDC | -0.0% |
| EASY/XMD | $1,454 | $66,457 | 3,227,706 EASY | 12,661.01 XMD | -0.0% |
| EASY/XUSDT | $1,280 | $66,818 | 3,258,926 EASY | 12,132.67 XUSDT | -0.7% |
| EASY/XPR | $815.34 | $22,843 | 455,773 EASY | 5,983,083.06 XPR | -0.2% |
| EASY/METAL | $681.16 | $4,207 | 51,431 EASY | 33,937.73 METAL | -1.0% |
| EASY/XMT | $131.70 | $3,031 | 15,604 EASY | 13,752.10 XMT | +0.4% |
| EASY/XHBAR | $80.32 | $563.31 | 2,899 EASY | 7,519.36 XHBAR | +0.5% |
| EASY/XXRP | $74.05 | $19,845 | 359,970 EASY | 13,122.85 XXRP | -0.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,548 XMD | 3,227,706 EASY | $66,457 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,662 XUSDC | 3,227,396 EASY | $66,598 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,656 XPYUSD | 3,235,507 EASY | $54,072 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,001 XPAX | 3,297,630 EASY | $68,111 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,388 XUSDT | 3,258,926 EASY | $66,818 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,093,751 | (snapshot) | (snapshot) |
| **Swap TVL** | $952,317 | - | - |
| **Swap volume** | $18,745 | $279,011 | $1,294,678 |
| **Spot volume** | $205.29 | $6,920 | $51,904 |
| **Swap fees** | $64.96 | $1,656 | $6,856 |
| **DAU (avg)** | ≈73 | ≈78 | ≈79 |
| **Liquidity pools** | 11,231 | - | - |
| **Spot pairs** | 1,643 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **740.43 EASY** |
| Approx. USD | **≈$12.37** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
