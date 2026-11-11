# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-11 19:56 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,094** |
| **EASY price** | **$0.0177** (≈10.62 XPR) |
| **EASY price in XUSDC** | **0.017758 XUSDC** |
| **Total EASY pools TVL** | **$367,199** |
| **Total USD backing (stables)** | **$56,513** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **965.13 EASY** (≈$17.13) in the reflection pool |
| **7d volume** | **$56,709** |
| **30d volume** | **$481,467** |
| **Flexers (holders on contract)** | **6,067** |
| **Market cap (fully circulating)** | **$372,672** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.94%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,094 | $18,341 | **24.9%** |
| 7d | $56,709 | $186,987 | **23.3%** |
| 30d | $481,467 | $884,028 | **35.3%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $2,020 | $15,425 | 369,078 EASY | 5,309,831.75 XPR | +0.2% |
| EASY/XUSDC | $1,464 | $69,905 | 3,152,016 EASY | 13,968.58 XUSDC | +0.6% |
| EASY/XUSDT | $809.02 | $69,905 | 3,153,389 EASY | 13,944.06 XUSDT | +0.4% |
| EASY/XXRP | $625.58 | $17,903 | 116,849 EASY | 15,010.94 XXRP | -0.3% |
| EASY/XPAX | $475.61 | $55,960 | 3,153,314 EASY | 14,007.47 XPAX | +0.6% |
| EASY/XXLM | $284.50 | $2,054 | 22,731 EASY | 11,176.90 XXLM | -2.5% |
| EASY/XBTC | $150.24 | $6,640 | 242,958 EASY | 0.03 XBTC | +0.6% |
| EASY/METAL | $95.01 | $5,539 | 306,496 EASY | 979.93 METAL | -0.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $502.77 XMD | 2,157,656 EASY | $38,793 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,969 XUSDC | 3,152,016 EASY | $69,905 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,864 XPYUSD | 3,163,744 EASY | $56,145 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,107 XPAX | 3,153,314 EASY | $55,960 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,944 XUSDT | 3,153,389 EASY | $69,905 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $866,466 | (snapshot) | (snapshot) |
| **Swap TVL** | $773,593 | - | - |
| **Swap volume** | $24,435 | $243,696 | $1,365,495 |
| **Spot volume** | $116.73 | $691.40 | $5,402 |
| **Swap fees** | $168.73 | $1,416 | $7,167 |
| **DAU (avg)** | ≈386 | ≈358 | ≈373 |
| **Liquidity pools** | 11,849 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **965.13 EASY** |
| Approx. USD | **≈$17.13** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
