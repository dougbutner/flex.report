# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-14 14:09 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,755** |
| **EASY price** | **$0.0164** (≈6.64 XPR) |
| **EASY price in XUSDC** | **0.016628 XUSDC** |
| **Total EASY pools TVL** | **$384,618** |
| **Total USD backing (stables)** | **$64,535** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **750.53 EASY** (≈$12.29) in the reflection pool |
| **7d volume** | **$58,288** |
| **30d volume** | **$359,909** |
| **Flexers (holders on contract)** | **940** |
| **Market cap (fully circulating)** | **$343,995** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.78%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,755 | $20,647 | **29.8%** |
| 7d | $58,288 | $169,482 | **25.6%** |
| 30d | $359,909 | $768,040 | **31.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,188 | $69,140 | 3,267,717 EASY | 15,596.47 XUSDC | -0.1% |
| EASY/XMD | $1,812 | $65,353 | 3,258,324 EASY | 12,146.50 XMD | -0.1% |
| EASY/XPR | $1,667 | $25,872 | 510,715 EASY | 7,094,901.69 XPR | +0.2% |
| EASY/XBTC | $461.74 | $2,694 | 8,528 EASY | 0.04 XBTC | +0.8% |
| EASY/XMT | $413.62 | $2,023 | 21,530 EASY | 8,845.75 XMT | +1.9% |
| EASY/XXLM | $406.82 | $772.26 | 1,002 EASY | 4,790.95 XXLM | -0.1% |
| EASY/XUSDT | $403.96 | $65,534 | 3,257,539 EASY | 12,155.09 XUSDT | +0.0% |
| EASY/METAL | $388.13 | $1,968 | 25,062 EASY | 16,531.01 METAL | +1.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $11,960 XMD | 3,258,324 EASY | $65,353 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,596 XUSDC | 3,267,717 EASY | $69,140 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,228 XPYUSD | 3,256,516 EASY | $53,360 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,576 XPAX | 3,292,650 EASY | $53,952 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,160 XUSDT | 3,257,539 EASY | $65,534 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,066,284 | (snapshot) | (snapshot) |
| **Swap TVL** | $918,676 | - | - |
| **Swap volume** | $29,403 | $227,770 | $1,127,950 |
| **Spot volume** | $413.79 | $4,191 | $33,703 |
| **Swap fees** | $163.27 | $1,191 | $5,959 |
| **DAU (avg)** | ≈77 | ≈79 | ≈79 |
| **Liquidity pools** | 11,322 | - | - |
| **Spot pairs** | 1,655 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **750.53 EASY** |
| Approx. USD | **≈$12.29** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
