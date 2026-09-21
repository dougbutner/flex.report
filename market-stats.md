# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-21 18:23 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$22,312** |
| **EASY price** | **$0.0187** (≈7.32 XPR) |
| **EASY price in XUSDC** | **0.018795 XUSDC** |
| **Total EASY pools TVL** | **$412,683** |
| **Total USD backing (stables)** | **$77,633** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **836.48 EASY** (≈$15.61) in the reflection pool |
| **7d volume** | **$138,504** |
| **30d volume** | **$550,269** |
| **Flexers (holders on contract)** | **981** |
| **Market cap (fully circulating)** | **$391,819** |
| **Share of Alcor Proton swap volume (24h)** | **≈35.9%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $22,312 | $39,833 | **35.9%** |
| 7d | $138,504 | $523,159 | **20.9%** |
| 30d | $550,269 | $1,510,224 | **26.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $7,469 | $73,647 | 3,089,754 EASY | 16,060.67 XMD | +1.2% |
| EASY/XUSDC | $4,516 | $72,745 | 3,063,835 EASY | 15,579.60 XUSDC | +1.3% |
| EASY/XXRP | $1,955 | $16,987 | 557,099 EASY | 4,448.57 XXRP | -3.5% |
| EASY/XPR | $1,854 | $25,290 | 122,956 EASY | 9,017,330.70 XPR | -1.1% |
| EASY/XUSDT | $1,807 | $72,611 | 3,065,271 EASY | 15,552.39 XUSDT | +1.4% |
| EASY/XXLM | $1,443 | $4,172 | 205,009 EASY | 1,672.29 XXLM | -2.5% |
| EASY/METAL | $1,221 | $5,616 | 77,113 EASY | 32,218.59 METAL | +1.5% |
| EASY/XDOGE | $599.28 | $1,527 | 80,501 EASY | 263.11 XDOGE | -4.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,999 XMD | 3,089,754 EASY | $73,647 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,580 XUSDC | 3,063,835 EASY | $72,745 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,810 XPYUSD | 3,135,552 EASY | $58,503 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,870 XPAX | 3,136,253 EASY | $58,516 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,419 XUSDT | 3,065,271 EASY | $72,611 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,206,024 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,045,849 | - | - |
| **Swap volume** | $62,145 | $661,663 | $2,060,494 |
| **Spot volume** | $226.96 | $3,362 | $11,566 |
| **Swap fees** | $316.98 | $3,644 | $10,891 |
| **DAU (avg)** | ≈72 | ≈73 | ≈75 |
| **Liquidity pools** | 11,611 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **836.48 EASY** |
| Approx. USD | **≈$15.61** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
