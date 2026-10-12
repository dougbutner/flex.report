# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-12 21:29 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,476** |
| **EASY price** | **$0.0181** (≈8.05 XPR) |
| **EASY price in XUSDC** | **0.018115 XUSDC** |
| **Total EASY pools TVL** | **$392,536** |
| **Total USD backing (stables)** | **$73,107** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,146.91 EASY** (≈$20.71) in the reflection pool |
| **7d volume** | **$89,273** |
| **30d volume** | **$412,132** |
| **Flexers (holders on contract)** | **1,018** |
| **Market cap (fully circulating)** | **$379,117** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.21%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,476 | $26,527 | **24.2%** |
| 7d | $89,273 | $211,877 | **29.6%** |
| 30d | $412,132 | $1,291,274 | **24.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,507 | $70,797 | 3,120,897 EASY | 14,528.08 XUSDC | -0.6% |
| EASY/XPR | $2,130 | $23,697 | 488,734 EASY | 6,649,775.70 XPR | -0.3% |
| EASY/XMD | $1,110 | $71,746 | 3,147,043 EASY | 15,004.73 XMD | -0.7% |
| EASY/XUSDT | $1,051 | $70,797 | 3,140,419 EASY | 14,175.73 XUSDT | -1.1% |
| EASY/METAL | $555.82 | $2,261 | 34,499 EASY | 13,883.04 METAL | +1.1% |
| EASY/XXRP | $452.23 | $15,120 | 360,697 EASY | 6,242.49 XXRP | +0.2% |
| EASY/XPYUSD | $212.19 | $56,266 | 3,120,741 EASY | 14,529.60 XPYUSD | -0.6% |
| EASY/XSOL | $138.07 | $973.01 | 14,871 EASY | 6.46 XSOL | +0.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,025 XMD | 3,147,043 EASY | $71,746 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,528 XUSDC | 3,120,897 EASY | $70,797 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,580 XPYUSD | 3,120,741 EASY | $56,266 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,448 XPAX | 3,136,848 EASY | $56,557 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,176 XUSDT | 3,140,419 EASY | $70,797 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,112,308 | (snapshot) | (snapshot) |
| **Swap TVL** | $971,580 | - | - |
| **Swap volume** | $35,003 | $301,150 | $1,703,406 |
| **Spot volume** | $785.85 | $2,343 | $12,626 |
| **Swap fees** | $190.13 | $1,635 | $9,141 |
| **DAU (avg)** | ≈393 | ≈406 | ≈417 |
| **Liquidity pools** | 11,707 | - | - |
| **Spot pairs** | 1,674 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,146.91 EASY** |
| Approx. USD | **≈$20.71** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
