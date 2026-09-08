# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-08 16:57 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$16,935** |
| **EASY price** | **$0.0188** (≈6.64 XPR) |
| **EASY price in XUSDC** | **0.019093 XUSDC** |
| **Total EASY pools TVL** | **$2,314,109** |
| **Total USD backing (stables)** | **$82,811** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **3,279.94 EASY** (≈$61.67) in the reflection pool |
| **7d volume** | **$96,652** |
| **30d volume** | **$544,341** |
| **Flexers (holders on contract)** | **958** |
| **Market cap (fully circulating)** | **$394,876** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.38%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $16,935 | $40,706 | **29.4%** |
| 7d | $96,652 | $285,285 | **25.3%** |
| 30d | $544,341 | $1,039,358 | **34.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $5,192 | $74,661 | 3,063,923 EASY | 17,535.20 XMD | +0.1% |
| EASY/XXRP | $3,241 | $15,254 | 427,640 EASY | 5,147.14 XXRP | -0.3% |
| EASY/XUSDC | $3,074 | $73,158 | 3,039,830 EASY | 16,237.33 XUSDC | +0.2% |
| EASY/METAL | $2,013 | $8,019 | 38,293 EASY | 56,944.18 METAL | -0.1% |
| EASY/XPR | $1,185 | $42,743 | 677,475 EASY | 10,666,182.38 XPR | +0.0% |
| EASY/XBTC | $482.48 | $6,604 | 239,020 EASY | 0.03 XBTC | +0.4% |
| EASY/XUSDT | $422.79 | $72,971 | 3,042,350 EASY | 15,986.06 XUSDT | +0.1% |
| EASY/XXLM | $398.93 | $4,100 | 141,049 EASY | 7,713.76 XXLM | -0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $17,532 XMD | 3,063,923 EASY | $74,661 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,237 XUSDC | 3,039,830 EASY | $73,158 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,149 XPYUSD | 3,039,904 EASY | $56,922 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,413 XPAX | 3,108,834 EASY | $58,213 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,003 XUSDT | 3,042,350 EASY | $72,971 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,132,430 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,966,749 | - | - |
| **Swap volume** | $57,641 | $381,937 | $1,583,699 |
| **Spot volume** | $136.06 | $2,460 | $9,256 |
| **Swap fees** | $309.64 | $2,033 | $8,532 |
| **DAU (avg)** | ≈77 | ≈74 | ≈76 |
| **Liquidity pools** | 11,499 | - | - |
| **Spot pairs** | 1,667 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **3,279.94 EASY** |
| Approx. USD | **≈$61.67** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
