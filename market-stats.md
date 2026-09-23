# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-23 17:36 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,897** |
| **EASY price** | **$0.0186** (≈7.33 XPR) |
| **EASY price in XUSDC** | **0.018655 XUSDC** |
| **Total EASY pools TVL** | **$436,735** |
| **Total USD backing (stables)** | **$80,131** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **990.52 EASY** (≈$18.40) in the reflection pool |
| **7d volume** | **$120,190** |
| **30d volume** | **$532,573** |
| **Flexers (holders on contract)** | **983** |
| **Market cap (fully circulating)** | **$390,092** |
| **Share of Alcor Proton swap volume (24h)** | **≈19.81%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,897 | $40,066 | **19.8%** |
| 7d | $120,190 | $477,774 | **20.1%** |
| 30d | $532,573 | $1,517,466 | **26.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $3,020 | $73,253 | 3,100,508 EASY | 15,862.22 XMD | -0.6% |
| EASY/XUSDC | $2,216 | $72,494 | 3,075,415 EASY | 15,365.84 XUSDC | -0.6% |
| EASY/XXRP | $1,485 | $17,023 | 562,199 EASY | 4,392.89 XXRP | +1.4% |
| EASY/XUSDT | $1,304 | $72,407 | 3,075,807 EASY | 15,357.20 XUSDT | -1.2% |
| EASY/XXLM | $701.47 | $4,149 | 191,611 EASY | 2,914.75 XXLM | +2.2% |
| EASY/XPR | $415.83 | $26,479 | 118,107 EASY | 9,582,558.63 XPR | -0.2% |
| EASY/XDOGE | $221.53 | $1,492 | 68,205 EASY | 2,441.01 XDOGE | +3.1% |
| EASY/METAL | $199.55 | $6,422 | 106,704 EASY | 34,991.67 METAL | +0.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,658 XMD | 3,100,508 EASY | $73,253 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,366 XUSDC | 3,075,415 EASY | $72,494 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,916 XPYUSD | 3,135,856 EASY | $58,251 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,900 XPAX | 3,136,068 EASY | $58,255 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,271 XUSDT | 3,075,807 EASY | $72,407 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,223,832 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,068,686 | - | - |
| **Swap volume** | $49,963 | $597,964 | $2,050,039 |
| **Spot volume** | $36.05 | $3,274 | $11,309 |
| **Swap fees** | $268.76 | $3,296 | $10,821 |
| **DAU (avg)** | ≈114 | ≈78 | ≈76 |
| **Liquidity pools** | 11,614 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **990.52 EASY** |
| Approx. USD | **≈$18.40** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
