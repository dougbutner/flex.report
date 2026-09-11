# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-11 16:50 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$16,689** |
| **EASY price** | **$0.0186** (≈6.71 XPR) |
| **EASY price in XUSDC** | **0.018892 XUSDC** |
| **Total EASY pools TVL** | **$2,312,924** |
| **Total USD backing (stables)** | **$79,832** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,295.47 EASY** (≈$24.10) in the reflection pool |
| **7d volume** | **$78,893** |
| **30d volume** | **$556,052** |
| **Flexers (holders on contract)** | **964** |
| **Market cap (fully circulating)** | **$390,719** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.99%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $16,689 | $38,957 | **30.0%** |
| 7d | $78,893 | $243,888 | **24.4%** |
| 30d | $556,052 | $1,057,477 | **34.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $3,882 | $73,430 | 3,082,086 EASY | 16,206.65 XMD | +0.2% |
| EASY/GEASY | $2,426 | - | 263,150 EASY | 267,113,913.98 GEASY | +59.8% |
| EASY/XUSDC | $2,384 | $72,569 | 3,055,950 EASY | 15,728.90 XUSDC | +0.1% |
| EASY/XPR | $2,058 | $43,133 | 498,932 EASY | 12,216,133.61 XPR | -0.3% |
| EASY/XXRP | $1,773 | $15,073 | 404,945 EASY | 5,460.13 XXRP | -0.7% |
| EASY/XUSDT | $763.91 | $72,426 | 3,054,825 EASY | 15,749.57 XUSDT | +0.2% |
| EASY/XPR | $734.28 | $890.84 | 40,661 EASY | 48,559.63 XPR | -0.4% |
| EASY/METAL | $576.79 | $7,881 | 39,268 EASY | 53,881.81 METAL | -2.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,110 XMD | 3,082,086 EASY | $73,430 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,729 XUSDC | 3,055,950 EASY | $72,569 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,689 XPYUSD | 3,063,487 EASY | $56,980 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,324 XPAX | 3,108,914 EASY | $57,825 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,612 XUSDT | 3,054,825 EASY | $72,426 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,095,467 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,930,979 | - | - |
| **Swap volume** | $55,646 | $322,781 | $1,613,529 |
| **Spot volume** | $147.45 | $2,320 | $7,895 |
| **Swap fees** | $289.38 | $1,584 | $8,644 |
| **DAU (avg)** | ≈78 | ≈75 | ≈75 |
| **Liquidity pools** | 11,534 | - | - |
| **Spot pairs** | 1,667 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,295.47 EASY** |
| Approx. USD | **≈$24.10** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
