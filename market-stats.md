# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-18 13:35 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,210** |
| **EASY price** | **$0.0169** (≈6.74 XPR) |
| **EASY price in XUSDC** | **0.016949 XUSDC** |
| **Total EASY pools TVL** | **$2,086,214** |
| **Total USD backing (stables)** | **$64,877** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **874.74 EASY** (≈$14.78) in the reflection pool |
| **7d volume** | **$59,191** |
| **30d volume** | **$350,198** |
| **Flexers (holders on contract)** | **942** |
| **Market cap (fully circulating)** | **$354,798** |
| **Share of Alcor Proton swap volume (24h)** | **≈36.38%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,210 | $16,105 | **36.4%** |
| 7d | $59,191 | $141,371 | **29.5%** |
| 30d | $350,198 | $737,702 | **32.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,664 | $67,191 | 3,226,549 EASY | 12,677.95 XUSDC | -0.2% |
| EASY/LOAN | $1,880 | $3,593 | 2,461 EASY | 9,160,666.52 LOAN | +0.6% |
| EASY/XMD | $1,037 | $67,113 | 3,226,742 EASY | 12,677.95 XMD | -0.2% |
| EASY/XPR | $964.70 | $33,750 | 821,642 EASY | 7,923,971.87 XPR | -0.1% |
| EASY/XUSDT | $945.33 | $67,219 | 3,229,758 EASY | 12,621.81 XUSDT | -0.2% |
| EASY/METAL | $233.38 | $2,697 | 110,495 EASY | 7,938.91 METAL | -1.1% |
| EASY/XPYUSD | $125.57 | $54,500 | 3,225,799 EASY | 12,688.15 XPYUSD | +0.3% |
| EASY/XXRP | $82.38 | $14,434 | 196,744 EASY | 11,213.35 XXRP | -0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,597 XMD | 3,226,742 EASY | $67,113 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,678 XUSDC | 3,226,549 EASY | $67,191 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,724 XPYUSD | 3,225,799 EASY | $54,500 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,916 XPAX | 3,290,881 EASY | $55,600 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,652 XUSDT | 3,229,758 EASY | $67,219 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $2,735,799 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,595,917 | - | - |
| **Swap volume** | $25,314 | $200,562 | $1,087,900 |
| **Spot volume** | $38.43 | $1,674 | $25,384 |
| **Swap fees** | $122.50 | $982.98 | $5,638 |
| **DAU (avg)** | ≈69 | ≈74 | ≈78 |
| **Liquidity pools** | 11,358 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **874.74 EASY** |
| Approx. USD | **≈$14.78** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
