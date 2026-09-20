# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-20 16:38 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$32,283** |
| **EASY price** | **$0.0179** (≈7.15 XPR) |
| **EASY price in XUSDC** | **0.018298 XUSDC** |
| **Total EASY pools TVL** | **$413,886** |
| **Total USD backing (stables)** | **$73,703** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,295.17 EASY** (≈$23.14) in the reflection pool |
| **7d volume** | **$127,593** |
| **30d volume** | **$584,599** |
| **Flexers (holders on contract)** | **978** |
| **Market cap (fully circulating)** | **$375,136** |
| **Share of Alcor Proton swap volume (24h)** | **≈12.33%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $32,283 | $229,592 | **12.3%** |
| 7d | $127,593 | $534,268 | **19.3%** |
| 30d | $584,599 | $1,522,525 | **27.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $9,695 | $70,879 | 3,130,123 EASY | 15,311.88 XMD | -0.2% |
| EASY/XXRP | $7,528 | $16,090 | 460,925 EASY | 5,894.58 XXRP | +0.4% |
| EASY/XUSDC | $5,370 | $70,282 | 3,105,195 EASY | 14,812.45 XUSDC | -0.1% |
| EASY/XPR | $2,848 | $19,568 | 110,825 EASY | 7,038,744.81 XPR | -0.7% |
| EASY/XUSDT | $1,980 | $70,075 | 3,109,822 EASY | 14,727.85 XUSDT | +0.1% |
| EASY/XXLM | $1,419 | $3,968 | 171,298 EASY | 4,774.42 XXLM | +0.4% |
| EASY/METAL | $909.38 | $7,280 | 97,203 EASY | 43,456.15 METAL | +0.5% |
| EASY/XPYUSD | $849.05 | $55,616 | 3,113,387 EASY | 14,662.83 XPYUSD | -0.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,963 XMD | 3,130,123 EASY | $70,879 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,812 XUSDC | 3,105,195 EASY | $70,282 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,583 XPYUSD | 3,113,387 EASY | $55,616 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,210 XPAX | 3,136,818 EASY | $56,040 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,523 XUSDT | 3,109,822 EASY | $70,075 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,162,065 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,008,560 | - | - |
| **Swap volume** | $261,874 | $661,861 | $2,107,124 |
| **Spot volume** | $1,047 | $3,239 | $10,290 |
| **Swap fees** | $1,589 | $3,628 | $11,170 |
| **DAU (avg)** | ≈75 | ≈74 | ≈76 |
| **Liquidity pools** | 11,593 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,295.17 EASY** |
| Approx. USD | **≈$23.14** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
