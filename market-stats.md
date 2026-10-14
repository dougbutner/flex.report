# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-14 17:41 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,125** |
| **EASY price** | **$0.0180** (≈8.06 XPR) |
| **EASY price in XUSDC** | **0.018080 XUSDC** |
| **Total EASY pools TVL** | **$391,877** |
| **Total USD backing (stables)** | **$72,623** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,677.31 EASY** (≈$30.15) in the reflection pool |
| **7d volume** | **$58,002** |
| **30d volume** | **$396,510** |
| **Flexers (holders on contract)** | **1,020** |
| **Market cap (fully circulating)** | **$377,494** |
| **Share of Alcor Proton swap volume (24h)** | **≈16.06%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,125 | $32,016 | **16.1%** |
| 7d | $58,002 | $213,958 | **21.3%** |
| 30d | $396,510 | $1,212,797 | **24.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,736 | $70,627 | 3,123,849 EASY | 14,473.29 XUSDC | -0.4% |
| EASY/XMD | $1,176 | $71,372 | 3,150,837 EASY | 14,935.33 XMD | -0.5% |
| EASY/XPR | $1,024 | $23,629 | 558,477 EASY | 6,087,399.99 XPR | +0.3% |
| EASY/XUSDT | $686.05 | $70,627 | 3,132,883 EASY | 14,310.23 XUSDT | +0.1% |
| EASY/XXRP | $613.32 | $14,778 | 285,405 EASY | 7,238.04 XXRP | +0.6% |
| EASY/XXLM | $262.01 | $1,684 | 48,476 EASY | 4,437.42 XXLM | +2.1% |
| EASY/XDOGE | $134.95 | $1,457 | 41,570 EASY | 8,717.49 XDOGE | +1.1% |
| EASY/METAL | $119.88 | $2,918 | 74,430 EASY | 13,621.32 METAL | +0.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,726 XMD | 3,150,837 EASY | $71,372 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,473 XUSDC | 3,123,849 EASY | $70,627 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,462 XPYUSD | 3,131,061 EASY | $56,284 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,461 XPAX | 3,137,099 EASY | $56,392 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,310 XUSDT | 3,132,883 EASY | $70,627 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,102,517 | (snapshot) | (snapshot) |
| **Swap TVL** | $963,681 | - | - |
| **Swap volume** | $38,141 | $271,960 | $1,609,308 |
| **Spot volume** | $202.51 | $1,862 | $11,840 |
| **Swap fees** | $204.69 | $1,543 | $8,752 |
| **DAU (avg)** | ≈400 | ≈403 | ≈414 |
| **Liquidity pools** | 11,733 | - | - |
| **Spot pairs** | 1,674 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,677.31 EASY** |
| Approx. USD | **≈$30.15** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
