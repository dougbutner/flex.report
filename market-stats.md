# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-15 17:31 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,953** |
| **EASY price** | **$0.0179** (≈7.99 XPR) |
| **EASY price in XUSDC** | **0.017955 XUSDC** |
| **Total EASY pools TVL** | **$389,224** |
| **Total USD backing (stables)** | **$72,091** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **861.58 EASY** (≈$15.43) in the reflection pool |
| **7d volume** | **$57,396** |
| **30d volume** | **$388,298** |
| **Flexers (holders on contract)** | **1,020** |
| **Market cap (fully circulating)** | **$376,206** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.64%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,953 | $21,257 | **29.6%** |
| 7d | $57,396 | $205,276 | **21.9%** |
| 30d | $388,298 | $1,184,561 | **24.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,153 | $70,436 | 3,134,770 EASY | 14,277.60 XUSDC | -0.3% |
| EASY/XMD | $1,445 | $71,412 | 3,162,188 EASY | 14,731.67 XMD | -0.3% |
| EASY/XUSDT | $1,118 | $70,435 | 3,146,225 EASY | 14,071.96 XUSDT | -0.4% |
| EASY/XXRP | $670.78 | $12,029 | 280,599 EASY | 5,272.82 XXRP | +0.0% |
| EASY/XPR | $609.76 | $23,651 | 538,285 EASY | 6,250,086.40 XPR | -0.1% |
| EASY/WON | $601.19 | $1,961 | 109,468 EASY | 498,912.53 WON | -0.1% |
| EASY/XBTC | $529.97 | $5,297 | 251,798 EASY | 0.01 XBTC | +0.2% |
| EASY/MEME | $481.61 | $1,719 | 41,223 EASY | 234,978,390,418.57 MEME | +3.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,763 XMD | 3,162,188 EASY | $71,412 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,278 XUSDC | 3,134,770 EASY | $70,436 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,366 XPYUSD | 3,136,308 EASY | $56,186 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,437 XPAX | 3,137,149 EASY | $56,201 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,072 XUSDT | 3,146,225 EASY | $70,435 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,086,946 | (snapshot) | (snapshot) |
| **Swap TVL** | $947,347 | - | - |
| **Swap volume** | $30,211 | $262,672 | $1,572,859 |
| **Spot volume** | $69.20 | $1,854 | $11,851 |
| **Swap fees** | $143.52 | $1,427 | $8,558 |
| **DAU (avg)** | ≈411 | ≈404 | ≈413 |
| **Liquidity pools** | 11,739 | - | - |
| **Spot pairs** | 1,675 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **861.58 EASY** |
| Approx. USD | **≈$15.43** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
