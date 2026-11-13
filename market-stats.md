# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-13 20:10 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$14,681** |
| **EASY price** | **$0.0181** (≈9.54 XPR) |
| **EASY price in XUSDC** | **0.018231 XUSDC** |
| **Total EASY pools TVL** | **$372,993** |
| **Total USD backing (stables)** | **$59,032** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **932.93 EASY** (≈$16.86) in the reflection pool |
| **7d volume** | **$69,714** |
| **30d volume** | **$491,794** |
| **Flexers (holders on contract)** | **6,072** |
| **Market cap (fully circulating)** | **$379,426** |
| **Share of Alcor Proton swap volume (24h)** | **≈22.42%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $14,681 | $50,801 | **22.4%** |
| 7d | $69,714 | $240,316 | **22.5%** |
| 30d | $491,794 | $911,295 | **35.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $4,131 | $70,916 | 3,110,893 EASY | 14,708.68 XUSDC | +0.2% |
| EASY/XPR | $3,758 | $16,122 | 690,350 EASY | 1,926,533.28 XPR | +3.8% |
| EASY/XUSDT | $1,743 | $70,915 | 3,124,901 EASY | 14,454.23 XUSDT | -0.3% |
| EASY/XXRP | $1,668 | $18,235 | 84,269 EASY | 16,643.00 XXRP | +0.3% |
| EASY/XBTC | $996.69 | $6,451 | 124,295 EASY | 0.06 XBTC | +3.8% |
| EASY/XPAX | $959.87 | $56,252 | 3,113,348 EASY | 14,726.60 XPAX | +0.2% |
| EASY/XXLM | $469.12 | $3,901 | 6,606 EASY | 26,027.26 XXLM | -0.4% |
| EASY/XMD | $300.97 | $39,476 | 2,157,290 EASY | 511.14 XMD | +0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $498.46 XMD | 2,157,290 EASY | $39,476 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,709 XUSDC | 3,110,893 EASY | $70,916 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,412 XPYUSD | 3,140,514 EASY | $56,742 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,771 XPAX | 3,113,348 EASY | $56,252 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,454 XUSDT | 3,124,901 EASY | $70,915 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $895,793 | (snapshot) | (snapshot) |
| **Swap TVL** | $795,020 | - | - |
| **Swap volume** | $65,482 | $310,030 | $1,403,089 |
| **Spot volume** | $815.47 | $1,412 | $5,393 |
| **Swap fees** | $379.77 | $1,812 | $7,434 |
| **DAU (avg)** | ≈390 | ≈369 | ≈371 |
| **Liquidity pools** | 11,851 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **932.93 EASY** |
| Approx. USD | **≈$16.86** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
