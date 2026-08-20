# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-20 13:39 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$41,253** |
| **EASY price** | **$0.0189** (≈6.54 XPR) |
| **EASY price in XUSDC** | **0.018943 XUSDC** |
| **Total EASY pools TVL** | **$2,319,390** |
| **Total USD backing (stables)** | **$79,761** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,040.51 EASY** (≈$19.62) in the reflection pool |
| **7d volume** | **$99,438** |
| **30d volume** | **$362,359** |
| **Flexers (holders on contract)** | **944** |
| **Market cap (fully circulating)** | **$396,056** |
| **Share of Alcor Proton swap volume (24h)** | **≈46.32%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $41,253 | $47,815 | **46.3%** |
| 7d | $99,438 | $167,122 | **37.3%** |
| 30d | $362,359 | $755,081 | **32.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $12,097 | $73,416 | 3,051,106 EASY | 15,824.82 XMD | +4.6% |
| EASY/XUSDC | $8,220 | $73,419 | 3,051,814 EASY | 15,806.68 XUSDC | +4.6% |
| EASY/XXRP | $6,240 | $12,898 | 318,729 EASY | 5,879.94 XXRP | -2.4% |
| EASY/XPR | $5,352 | $37,574 | 1,085,921 EASY | 5,919,795.62 XPR | +0.9% |
| EASY/XUSDT | $2,870 | $73,486 | 3,059,951 EASY | 15,652.54 XUSDT | +4.3% |
| EASY/XUSDC | $1,968 | $4,111 | 51,547 EASY | 3,138.28 XUSDC | +4.4% |
| EASY/XMT | $1,472 | $603.76 | 8,425 EASY | 2,193.10 XMT | +0.5% |
| EASY/XMD | $590.54 | $969.83 | 16,762 EASY | 653.70 XMD | +4.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,802 XMD | 3,051,106 EASY | $73,416 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,807 XUSDC | 3,051,814 EASY | $73,419 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,128 XPYUSD | 3,215,769 EASY | $60,707 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,513 XPAX | 3,290,088 EASY | $62,110 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,720 XUSDT | 3,059,951 EASY | $73,486 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,076,279 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,919,789 | - | - |
| **Swap volume** | $89,069 | $266,560 | $1,117,440 |
| **Spot volume** | $268.05 | $1,104 | $19,979 |
| **Swap fees** | $511.94 | $1,369 | $5,845 |
| **DAU (avg)** | ≈78 | ≈74 | ≈77 |
| **Liquidity pools** | 11,388 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,040.51 EASY** |
| Approx. USD | **≈$19.62** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
