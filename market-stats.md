# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-22 20:03 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$4,971** |
| **EASY price** | **$0.0167** (≈10.88 XPR) |
| **EASY price in XUSDC** | **0.016962 XUSDC** |
| **Total EASY pools TVL** | **$349,971** |
| **Total USD backing (stables)** | **$50,629** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **994.96 EASY** (≈$16.58) in the reflection pool |
| **7d volume** | **$74,944** |
| **30d volume** | **$345,651** |
| **Flexers (holders on contract)** | **6,072** |
| **Market cap (fully circulating)** | **$349,868** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.58%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $4,971 | $15,255 | **24.6%** |
| 7d | $74,944 | $179,627 | **29.4%** |
| 30d | $345,651 | $830,761 | **29.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,854 | $66,434 | 3,225,269 EASY | 12,699.97 XUSDC | -0.4% |
| EASY/XUSDT | $860.45 | $66,428 | 3,254,300 EASY | 12,210.33 XUSDT | +0.5% |
| EASY/XPR | $668.35 | $9,378 | 119,115 EASY | 4,827,628.63 XPR | +0.6% |
| EASY/XXRP | $394.47 | $14,786 | 94,230 EASY | 14,538.15 XXRP | -0.3% |
| EASY/XBTC | $291.34 | $5,791 | 74,002 EASY | 0.08 XBTC | -1.6% |
| EASY/XPYUSD | $286.93 | $54,050 | 3,244,246 EASY | 12,381.96 XPYUSD | +1.6% |
| EASY/XSOL | $163.69 | $2,378 | 73,999 EASY | 16.60 XSOL | +0.0% |
| EASY/XXLM | $109.57 | $3,317 | 18,641 EASY | 23,934.64 XXLM | -0.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $476.24 XMD | 2,158,834 EASY | $36,443 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,700 XUSDC | 3,225,269 EASY | $66,434 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,553 XPYUSD | 3,244,246 EASY | $54,050 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,563 XPAX | 3,250,995 EASY | $54,163 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,210 XUSDT | 3,254,300 EASY | $66,428 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $840,522 | (snapshot) | (snapshot) |
| **Swap TVL** | $746,864 | - | - |
| **Swap volume** | $20,227 | $254,571 | $1,176,411 |
| **Spot volume** | $223.02 | $1,031 | $4,634 |
| **Swap fees** | $87.40 | $1,238 | $6,331 |
| **DAU (avg)** | ≈402 | ≈386 | ≈369 |
| **Liquidity pools** | 11,993 | - | - |
| **Spot pairs** | 1,682 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **994.96 EASY** |
| Approx. USD | **≈$16.58** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
