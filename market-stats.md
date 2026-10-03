# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-03 16:53 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,092** |
| **EASY price** | **$0.0184** (≈7.71 XPR) |
| **EASY price in XUSDC** | **0.018475 XUSDC** |
| **Total EASY pools TVL** | **$421,860** |
| **Total USD backing (stables)** | **$76,255** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,501.50 EASY** (≈$27.69) in the reflection pool |
| **7d volume** | **$72,520** |
| **30d volume** | **$434,159** |
| **Flexers (holders on contract)** | **1,005** |
| **Market cap (fully circulating)** | **$387,280** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.44%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,092 | $28,109 | **24.4%** |
| 7d | $72,520 | $213,592 | **25.4%** |
| 30d | $434,159 | $1,411,224 | **23.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,722 | $72,043 | 3,090,306 EASY | 15,086.63 XUSDC | -0.1% |
| EASY/XMD | $1,518 | $72,903 | 3,115,705 EASY | 15,577.24 XMD | -0.1% |
| EASY/XXRP | $1,497 | $20,259 | 352,574 EASY | 9,300.14 XXRP | +1.0% |
| EASY/XPR | $1,051 | $26,048 | 234,871 EASY | 9,087,616.43 XPR | +0.4% |
| EASY/XUSDT | $714.98 | $72,043 | 3,098,432 EASY | 14,936.44 XUSDT | -0.4% |
| EASY/XPYUSD | $468.77 | $56,965 | 3,090,766 EASY | 15,077.66 XPYUSD | -0.1% |
| EASY/METAL | $319.88 | $3,902 | 101,055 EASY | 16,528.67 METAL | -0.8% |
| EASY/XXLM | $294.54 | $1,779 | 86,291 EASY | 881.22 XXLM | +1.9% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,547 XMD | 3,115,705 EASY | $72,903 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,087 XUSDC | 3,090,306 EASY | $72,043 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,140 XPYUSD | 3,090,766 EASY | $56,965 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,733 XPAX | 3,136,330 EASY | $57,805 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,936 XUSDT | 3,098,432 EASY | $72,043 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,189,372 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,037,924 | - | - |
| **Swap volume** | $37,201 | $286,111 | $1,845,383 |
| **Spot volume** | $555.19 | $4,143 | $13,054 |
| **Swap fees** | $195.71 | $1,624 | $9,620 |
| **DAU (avg)** | ≈435 | ≈416 | ≈421 |
| **Liquidity pools** | 11,668 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,501.50 EASY** |
| Approx. USD | **≈$27.69** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
