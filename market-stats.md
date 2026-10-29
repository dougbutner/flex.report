# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-29 18:44 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,324** |
| **EASY price** | **$0.0191** (≈10.22 XPR) |
| **EASY price in XUSDC** | **0.019193 XUSDC** |
| **Total EASY pools TVL** | **$375,689** |
| **Total USD backing (stables)** | **$64,802** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,428.09 EASY** (≈$27.34) in the reflection pool |
| **7d volume** | **$129,314** |
| **30d volume** | **$534,463** |
| **Flexers (holders on contract)** | **6,060** |
| **Market cap (fully circulating)** | **$402,090** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.88%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,324 | $25,132 | **24.9%** |
| 7d | $129,314 | $225,084 | **36.5%** |
| 30d | $534,463 | $965,520 | **35.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,912 | $74,240 | 3,031,894 EASY | 16,188.06 XUSDC | -0.8% |
| EASY/XPR | $952.69 | $14,223 | 385,054 EASY | 3,673,144.23 XPR | -0.8% |
| EASY/XUSDT | $934.64 | $74,238 | 3,035,528 EASY | 16,116.84 XUSDT | -0.9% |
| EASY/XXRP | $823.40 | $20,112 | 429,008 EASY | 9,171.45 XXRP | +0.2% |
| EASY/XDOGE | $341.67 | $1,403 | 10,178 EASY | 15,210.06 XDOGE | -2.8% |
| EASY/XPYUSD | $311.55 | $58,859 | 3,074,027 EASY | 15,388.72 XPYUSD | +1.1% |
| EASY/XBTC | $305.10 | $6,804 | 226,655 EASY | 0.03 XBTC | -1.2% |
| EASY/XMD | $262.44 | $41,884 | 2,158,535 EASY | 562.31 XMD | -0.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $556.76 XMD | 2,158,535 EASY | $41,884 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,188 XUSDC | 3,031,894 EASY | $74,240 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,821 XPYUSD | 3,074,027 EASY | $58,859 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,717 XPAX | 3,089,836 EASY | $59,161 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,117 XUSDT | 3,035,528 EASY | $74,238 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $943,787 | (snapshot) | (snapshot) |
| **Swap TVL** | $841,138 | - | - |
| **Swap volume** | $33,456 | $354,397 | $1,499,983 |
| **Spot volume** | $24.48 | $605.43 | $9,763 |
| **Swap fees** | $193.04 | $1,681 | $7,747 |
| **DAU (avg)** | ≈356 | ≈382 | ≈398 |
| **Liquidity pools** | 11,819 | - | - |
| **Spot pairs** | 1,678 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,428.09 EASY** |
| Approx. USD | **≈$27.34** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
