# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-18 16:15 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$13,353** |
| **EASY price** | **$0.0175** (≈9.02 XPR) |
| **EASY price in XUSDC** | **0.017685 XUSDC** |
| **Total EASY pools TVL** | **$391,077** |
| **Total USD backing (stables)** | **$69,229** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,590.90 EASY** (≈$27.87) in the reflection pool |
| **7d volume** | **$215,251** |
| **30d volume** | **$521,153** |
| **Flexers (holders on contract)** | **6,043** |
| **Market cap (fully circulating)** | **$367,836** |
| **Share of Alcor Proton swap volume (24h)** | **≈35.52%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $13,353 | $24,239 | **35.5%** |
| 7d | $215,251 | $289,619 | **42.6%** |
| 30d | $521,153 | $1,248,469 | **29.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $4,048 | $31,303 | 699,801 EASY | 9,812,356.14 XPR | +1.5% |
| EASY/XMD | $2,983 | $69,884 | 3,184,855 EASY | 14,328.81 XMD | +1.3% |
| EASY/XUSDC | $2,208 | $69,179 | 3,158,616 EASY | 13,852.64 XUSDC | +1.4% |
| EASY/XXLM | $1,066 | $1,612 | 38,794 EASY | 5,397.34 XXLM | +1.2% |
| EASY/XUSDT | $788.64 | $69,177 | 3,173,769 EASY | 13,585.11 XUSDT | +0.7% |
| EASY/VIBRR | $486.56 | $76.12 | 4,346 EASY | 12,227,999.68 VIBRR | -95.0% |
| EASY/METAL | $436.72 | $2,760 | 46,300 EASY | 18,207.30 METAL | +1.8% |
| EASY/XPYUSD | $397.85 | $55,322 | 3,158,347 EASY | 13,856.54 XPYUSD | +1.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,098 XMD | 3,184,855 EASY | $69,884 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,853 XUSDC | 3,158,616 EASY | $69,179 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,782 XPYUSD | 3,158,347 EASY | $55,322 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,786 XPAX | 3,159,087 EASY | $55,335 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,585 XUSDT | 3,173,769 EASY | $69,177 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $988,469 | (snapshot) | (snapshot) |
| **Swap TVL** | $870,760 | - | - |
| **Swap volume** | $37,592 | $504,870 | $1,769,622 |
| **Spot volume** | $105.48 | $2,093 | $11,802 |
| **Swap fees** | $205.83 | $2,695 | $9,617 |
| **DAU (avg)** | ≈427 | ≈407 | ≈413 |
| **Liquidity pools** | 11,784 | - | - |
| **Spot pairs** | 1,675 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,590.90 EASY** |
| Approx. USD | **≈$27.87** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
