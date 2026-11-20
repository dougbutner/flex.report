# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-20 20:51 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$18,139** |
| **EASY price** | **$0.0164** (≈11.01 XPR) |
| **EASY price in XUSDC** | **0.016674 XUSDC** |
| **Total EASY pools TVL** | **$341,339** |
| **Total USD backing (stables)** | **$49,358** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,172.98 EASY** (≈$19.29) in the reflection pool |
| **7d volume** | **$85,980** |
| **30d volume** | **$353,768** |
| **Flexers (holders on contract)** | **6,072** |
| **Market cap (fully circulating)** | **$345,309** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.04%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $18,139 | $44,322 | **29.0%** |
| 7d | $85,980 | $176,481 | **32.8%** |
| 30d | $353,768 | $827,089 | **30.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $6,385 | $65,721 | 3,252,968 EASY | 12,231.50 XUSDC | -2.7% |
| EASY/XPR | $2,796 | $9,158 | 110,377 EASY | 4,917,038.15 XPR | -1.0% |
| EASY/METAL | $2,164 | $3,833 | 215,097 EASY | 3,159.25 METAL | -0.8% |
| EASY/XUSDT | $1,712 | $65,718 | 3,275,703 EASY | 11,854.97 XUSDT | -2.8% |
| EASY/XXRP | $1,646 | $14,257 | 76,874 EASY | 14,851.40 XXRP | +6.4% |
| EASY/USDC | $711.97 | $7,611 | 442,593 EASY | 333.11 USDC | +1.9% |
| EASY/XMD | $589.00 | $36,026 | 2,160,252 EASY | 514.29 XMD | -2.8% |
| EASY/XXLM | $526.31 | $3,210 | 10,001 EASY | 25,068.56 XXLM | +6.9% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $504.13 XMD | 2,160,252 EASY | $36,026 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,232 XUSDC | 3,252,968 EASY | $65,721 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,219 XPYUSD | 3,252,827 EASY | $53,487 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,537 XPAX | 3,236,681 EASY | $53,222 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $11,855 XUSDT | 3,275,703 EASY | $65,718 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $821,990 | (snapshot) | (snapshot) |
| **Swap TVL** | $730,352 | - | - |
| **Swap volume** | $62,461 | $262,461 | $1,180,858 |
| **Spot volume** | $34.51 | $1,378 | $5,976 |
| **Swap fees** | $289.36 | $1,345 | $6,327 |
| **DAU (avg)** | ≈399 | ≈373 | ≈366 |
| **Liquidity pools** | 11,917 | - | - |
| **Spot pairs** | 1,681 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,172.98 EASY** |
| Approx. USD | **≈$19.29** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
