# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-29 16:55 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,906** |
| **EASY price** | **$0.0186** (≈6.50 XPR) |
| **EASY price in XUSDC** | **0.018783 XUSDC** |
| **Total EASY pools TVL** | **$2,295,399** |
| **Total USD backing (stables)** | **$82,104** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **897.96 EASY** (≈$16.69) in the reflection pool |
| **7d volume** | **$152,901** |
| **30d volume** | **$496,352** |
| **Flexers (holders on contract)** | **952** |
| **Market cap (fully circulating)** | **$390,352** |
| **Share of Alcor Proton swap volume (24h)** | **≈18.81%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,906 | $47,066 | **18.8%** |
| 7d | $152,901 | $236,909 | **39.2%** |
| 30d | $496,352 | $927,343 | **34.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,601 | $74,053 | 3,070,647 EASY | 16,993.95 XUSDC | -0.6% |
| EASY/XPR | $2,499 | $48,772 | 1,040,936 EASY | 10,289,729.15 XPR | -0.4% |
| EASY/XMD | $2,114 | $73,328 | 3,091,376 EASY | 16,032.61 XMD | -0.6% |
| EASY/METAL | $1,215 | $3,219 | 143,942 EASY | 4,328.21 METAL | +0.7% |
| EASY/XUSDC | $811.95 | $5,914 | 199,077 EASY | 2,214.26 XUSDC | -0.6% |
| EASY/XUSDT | $443.29 | $72,450 | 3,065,210 EASY | 15,554.50 XUSDT | -0.7% |
| EASY/XPYUSD | $244.88 | $56,962 | 3,065,401 EASY | 15,550.64 XPYUSD | -0.5% |
| EASY/XHBAR | $218.92 | $671.50 | 16,642 EASY | 4,808.89 XHBAR | -1.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,889 XMD | 3,091,376 EASY | $73,328 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,994 XUSDC | 3,070,647 EASY | $74,053 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,686 XPYUSD | 3,065,401 EASY | $56,962 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,337 XPAX | 3,108,646 EASY | $57,766 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,496 XUSDT | 3,065,210 EASY | $72,450 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,178,776 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,020,590 | - | - |
| **Swap volume** | $57,972 | $389,810 | $1,423,695 |
| **Spot volume** | $348.11 | $1,182 | $12,532 |
| **Swap fees** | $304.48 | $2,135 | $7,862 |
| **DAU (avg)** | ≈75 | ≈75 | ≈77 |
| **Liquidity pools** | 11,461 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **897.96 EASY** |
| Approx. USD | **≈$16.69** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
