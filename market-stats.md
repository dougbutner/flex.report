# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-16 17:23 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$25,149** |
| **EASY price** | **$0.0169** (≈7.06 XPR) |
| **EASY price in XUSDC** | **0.017796 XUSDC** |
| **Total EASY pools TVL** | **$373,822** |
| **Total USD backing (stables)** | **$69,986** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **738.04 EASY** (≈$12.50) in the reflection pool |
| **7d volume** | **$142,420** |
| **30d volume** | **$619,480** |
| **Flexers (holders on contract)** | **971** |
| **Market cap (fully circulating)** | **$355,739** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.95%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $25,149 | $58,827 | **29.9%** |
| 7d | $142,420 | $429,413 | **24.9%** |
| 30d | $619,480 | $1,316,277 | **32.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $9,049 | $67,635 | 3,175,794 EASY | 14,487.63 XMD | -1.2% |
| EASY/XUSDC | $4,573 | $67,367 | 3,148,712 EASY | 14,027.45 XUSDC | -1.2% |
| EASY/XXRP | $4,082 | $14,402 | 391,776 EASY | 6,375.17 XXRP | +3.3% |
| EASY/XPR | $1,692 | $19,991 | 191,799 EASY | 6,973,392.68 XPR | +0.5% |
| EASY/XUSDT | $1,580 | $66,743 | 3,146,721 EASY | 14,062.57 XUSDT | -1.5% |
| EASY/XPR | $1,086 | $0.00 | 0 EASY | 0.17 XPR | +1.0% |
| EASY/XXLM | $604.35 | $3,701 | 139,412 EASY | 7,880.54 XXLM | +3.0% |
| EASY/XPYUSD | $592.67 | $53,334 | 3,148,404 EASY | 14,032.59 XPYUSD | -1.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $13,837 XMD | 3,175,794 EASY | $67,635 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,027 XUSDC | 3,148,712 EASY | $67,366 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,077 XPYUSD | 3,148,404 EASY | $53,334 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,357 XPAX | 3,149,950 EASY | $53,360 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,438 XUSDT | 3,146,721 EASY | $66,743 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,079,480 | (snapshot) | (snapshot) |
| **Swap TVL** | $936,691 | - | - |
| **Swap volume** | $83,977 | $571,833 | $1,935,757 |
| **Spot volume** | $93.82 | $2,790 | $9,031 |
| **Swap fees** | $430.46 | $2,788 | $10,230 |
| **DAU (avg)** | ≈74 | ≈77 | ≈76 |
| **Liquidity pools** | 11,573 | - | - |
| **Spot pairs** | 1,668 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **738.04 EASY** |
| Approx. USD | **≈$12.50** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
