# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-28 22:49 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$22,371** |
| **EASY price** | **$0.0187** (≈6.48 XPR) |
| **EASY price in XUSDC** | **0.018794 XUSDC** |
| **Total EASY pools TVL** | **$436,255** |
| **Total USD backing (stables)** | **$82,595** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,121.57 EASY** (≈$20.96) in the reflection pool |
| **7d volume** | **$199,464** |
| **30d volume** | **$510,600** |
| **Flexers (holders on contract)** | **952** |
| **Market cap (fully circulating)** | **$392,374** |
| **Share of Alcor Proton swap volume (24h)** | **≈35.89%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $22,371 | $39,966 | **35.9%** |
| 7d | $199,464 | $261,688 | **43.2%** |
| 30d | $510,600 | $928,434 | **35.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $5,409 | $74,313 | 3,068,123 EASY | 17,040.85 XUSDC | -1.5% |
| EASY/XMD | $4,992 | $73,666 | 3,090,798 EASY | 16,043.10 XMD | -1.5% |
| EASY/XPR | $3,928 | $49,071 | 1,097,557 EASY | 9,920,170.35 XPR | -0.1% |
| EASY/XUSDT | $1,812 | $72,765 | 3,061,699 EASY | 15,620.46 XUSDT | -1.4% |
| EASY/XHBAR | $1,029 | $673.32 | 17,288 EASY | 4,643.58 XHBAR | +1.1% |
| EASY/XXRP | $895.02 | $15,218 | 392,713 EASY | 5,768.34 XXRP | +1.3% |
| EASY/XUSDC | $759.42 | $5,931 | 190,303 EASY | 2,378.89 XUSDC | -0.8% |
| EASY/METAL | $690.49 | $3,220 | 114,019 EASY | 8,821.68 METAL | +1.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,958 XMD | 3,090,798 EASY | $73,666 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,041 XUSDC | 3,068,123 EASY | $74,313 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,714 XPYUSD | 3,063,905 EASY | $57,193 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,384 XPAX | 3,108,604 EASY | $58,027 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,629 XUSDT | 3,061,699 EASY | $72,765 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,175,602 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,019,086 | - | - |
| **Swap volume** | $62,337 | $461,153 | $1,439,034 |
| **Spot volume** | $53.67 | $933.09 | $13,313 |
| **Swap fees** | $307.03 | $2,500 | $7,878 |
| **DAU (avg)** | ≈71 | ≈76 | ≈77 |
| **Liquidity pools** | 11,452 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,121.57 EASY** |
| Approx. USD | **≈$20.96** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
