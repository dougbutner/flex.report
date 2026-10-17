# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-17 16:03 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$163,289** |
| **EASY price** | **$0.0174** (≈8.98 XPR) |
| **EASY price in XUSDC** | **0.017447 XUSDC** |
| **Total EASY pools TVL** | **$391,733** |
| **Total USD backing (stables)** | **$67,890** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,088.20 EASY** (≈$18.99) in the reflection pool |
| **7d volume** | **$206,121** |
| **30d volume** | **$524,881** |
| **Flexers (holders on contract)** | **1,879** |
| **Market cap (fully circulating)** | **$366,393** |
| **Share of Alcor Proton swap volume (24h)** | **≈55.44%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $163,289 | $131,242 | **55.4%** |
| 7d | $206,121 | $285,749 | **41.9%** |
| 30d | $524,881 | $1,255,095 | **29.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $44,511 | $68,958 | 3,180,006 EASY | 13,475.80 XUSDC | -3.0% |
| EASY/XPR | $38,740 | $29,311 | 472,822 EASY | 10,838,059.77 XPR | -11.6% |
| EASY/XMD | $31,679 | $70,097 | 3,206,835 EASY | 13,941.22 XMD | -2.9% |
| EASY/VIBRR | $19,146 | - | 1,517 EASY | 19,936,689.01 VIBRR | +16429.2% |
| EASY/XUSDT | $8,462 | $68,955 | 3,185,051 EASY | 13,387.81 XUSDT | -2.6% |
| EASY/XXRP | $6,918 | $17,801 | 255,281 EASY | 10,548.51 XXRP | +5.4% |
| EASY/XPAX | $3,103 | $55,537 | 3,183,331 EASY | 13,479.20 XPAX | -2.9% |
| EASY/XXLM | $2,806 | $1,646 | 42,128 EASY | 5,060.07 XXLM | +1.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,052 XMD | 3,206,835 EASY | $70,097 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,476 XUSDC | 3,180,006 EASY | $68,958 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,496 XPYUSD | 3,181,614 EASY | $55,507 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,377 XPAX | 3,183,331 EASY | $55,537 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,388 XUSDT | 3,185,051 EASY | $68,955 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $984,105 | (snapshot) | (snapshot) |
| **Swap TVL** | $867,322 | - | - |
| **Swap volume** | $294,531 | $491,870 | $1,779,976 |
| **Spot volume** | $300.51 | $2,088 | $12,213 |
| **Swap fees** | $1,563 | $2,607 | $9,642 |
| **DAU (avg)** | ≈409 | ≈404 | ≈413 |
| **Liquidity pools** | 11,780 | - | - |
| **Spot pairs** | 1,675 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,088.20 EASY** |
| Approx. USD | **≈$18.99** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
