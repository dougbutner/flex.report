# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-08 18:09 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$1,885** |
| **EASY price** | **$0.0180** (≈10.71 XPR) |
| **EASY price in XUSDC** | **0.018215 XUSDC** |
| **Total EASY pools TVL** | **$352,016** |
| **Total USD backing (stables)** | **$59,429** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,470.87 EASY** (≈$26.48) in the reflection pool |
| **7d volume** | **$40,169** |
| **30d volume** | **$466,110** |
| **Flexers (holders on contract)** | **6,063** |
| **Market cap (fully circulating)** | **$378,002** |
| **Share of Alcor Proton swap volume (24h)** | **≈22.09%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $1,885 | $6,646 | **22.1%** |
| 7d | $40,169 | $114,500 | **26.0%** |
| 30d | $466,110 | $827,838 | **36.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $516.04 | $70,705 | 3,112,303 EASY | 14,683.08 XUSDC | -0.7% |
| EASY/XPR | $513.74 | $12,069 | 363,636 EASY | 3,286,697.37 XPR | -1.4% |
| EASY/XXRP | $227.89 | $15,816 | 254,706 EASY | 9,945.61 XXRP | +0.3% |
| EASY/XUSDT | $122.23 | $70,713 | 3,130,782 EASY | 14,348.09 XUSDT | -0.3% |
| EASY/XPAX | $121.43 | $56,042 | 3,113,419 EASY | 14,725.39 XPAX | -0.5% |
| EASY/XXLM | $120.82 | $2,069 | 18,335 EASY | 11,819.06 XXLM | +0.3% |
| EASY/XPYUSD | $91.15 | $56,021 | 3,112,273 EASY | 14,683.26 XPYUSD | -0.6% |
| EASY/XBTC | $74.33 | $6,753 | 239,389 EASY | 0.03 XBTC | -0.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $510.97 XMD | 2,157,287 EASY | $39,342 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,683 XUSDC | 3,112,303 EASY | $70,705 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,812 XPYUSD | 3,112,273 EASY | $56,021 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,854 XPAX | 3,113,419 EASY | $56,042 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,348 XUSDT | 3,130,782 EASY | $70,713 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $869,872 | (snapshot) | (snapshot) |
| **Swap TVL** | $774,179 | - | - |
| **Swap volume** | $8,530 | $154,669 | $1,293,948 |
| **Spot volume** | $45.50 | $393.58 | $5,773 |
| **Swap fees** | $51.79 | $905.10 | $6,726 |
| **DAU (avg)** | ≈336 | ≈340 | ≈375 |
| **Liquidity pools** | 11,837 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,470.87 EASY** |
| Approx. USD | **≈$26.48** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
