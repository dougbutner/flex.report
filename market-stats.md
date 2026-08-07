# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-07 14:06 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$18,458** |
| **EASY price** | **$0.0167** (≈6.51 XPR) |
| **EASY price in XUSDC** | **0.016968 XUSDC** |
| **Total EASY pools TVL** | **$389,284** |
| **Total USD backing (stables)** | **$63,619** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **783.80 EASY** (≈$13.10) in the reflection pool |
| **7d volume** | **$76,878** |
| **30d volume** | **$393,175** |
| **Flexers (holders on contract)** | **935** |
| **Market cap (fully circulating)** | **$350,880** |
| **Share of Alcor Proton swap volume (24h)** | **≈37.73%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $18,458 | $30,467 | **37.7%** |
| 7d | $76,878 | $212,666 | **26.6%** |
| 30d | $393,175 | $939,201 | **29.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $5,865 | $66,446 | 3,225,365 EASY | 12,700.84 XMD | +0.1% |
| EASY/XUSDC | $3,367 | $66,588 | 3,224,629 EASY | 12,708.82 XUSDC | +0.1% |
| EASY/XXRP | $1,926 | $19,974 | 202,484 EASY | 16,124.53 XXRP | +0.7% |
| EASY/XPR | $1,899 | $24,769 | 590,917 EASY | 5,760,597.85 XPR | +0.5% |
| EASY/METAL | $1,888 | $4,494 | 108,205 EASY | 26,730.47 METAL | -0.6% |
| EASY/XUSDT | $1,173 | $66,873 | 3,230,541 EASY | 12,607.96 XUSDT | +0.3% |
| EASY/XMT | $869.71 | $3,246 | 33,030 EASY | 13,143.96 XMT | +0.7% |
| EASY/XPYUSD | $586.89 | $54,128 | 3,224,968 EASY | 12,702.26 XPYUSD | +0.3% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,555 XMD | 3,225,365 EASY | $66,446 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,709 XUSDC | 3,224,629 EASY | $66,588 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,801 XPYUSD | 3,224,968 EASY | $54,128 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,863 XPAX | 3,291,191 EASY | $55,240 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,651 XUSDT | 3,230,541 EASY | $66,873 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,079,002 | (snapshot) | (snapshot) |
| **Swap TVL** | $940,574 | - | - |
| **Swap volume** | $48,925 | $289,544 | $1,332,376 |
| **Spot volume** | $178.03 | $6,045 | $51,835 |
| **Swap fees** | $226.33 | $1,716 | $6,987 |
| **DAU (avg)** | ≈78 | ≈78 | ≈79 |
| **Liquidity pools** | 11,249 | - | - |
| **Spot pairs** | 1,644 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **783.80 EASY** |
| Approx. USD | **≈$13.10** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
