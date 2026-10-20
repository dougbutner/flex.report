# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-20 17:39 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,814** |
| **EASY price** | **$0.0175** (≈9.04 XPR) |
| **EASY price in XUSDC** | **0.017734 XUSDC** |
| **Total EASY pools TVL** | **$391,206** |
| **Total USD backing (stables)** | **$69,543** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,043.89 EASY** (≈$18.25) in the reflection pool |
| **7d volume** | **$208,885** |
| **30d volume** | **$482,412** |
| **Flexers (holders on contract)** | **6,047** |
| **Market cap (fully circulating)** | **$367,097** |
| **Share of Alcor Proton swap volume (24h)** | **≈32.52%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,814 | $14,140 | **32.5%** |
| 7d | $208,885 | $252,831 | **45.2%** |
| 30d | $482,412 | $949,451 | **33.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XXRP | $1,702 | $18,010 | 349,166 EASY | 9,257.11 XXRP | -0.4% |
| EASY/XMD | $1,375 | $69,943 | 3,180,256 EASY | 14,411.50 XMD | +0.3% |
| EASY/XPR | $1,026 | $31,219 | 610,121 EASY | 10,627,229.58 XPR | -0.4% |
| EASY/XUSDC | $888.33 | $69,070 | 3,154,222 EASY | 13,931.59 XUSDC | +0.3% |
| EASY/METAL | $644.31 | $2,764 | 37,881 EASY | 19,649.91 METAL | +0.8% |
| EASY/XPYUSD | $357.79 | $55,193 | 3,157,329 EASY | 13,875.13 XPYUSD | +0.0% |
| EASY/XUSDT | $265.29 | $69,065 | 3,176,972 EASY | 13,529.35 XUSDT | +0.0% |
| EASY/XDOGE | $160.83 | $1,429 | 42,419 EASY | 8,552.45 XDOGE | -2.4% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,349 XMD | 3,180,256 EASY | $69,943 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,932 XUSDC | 3,154,222 EASY | $69,070 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,783 XPYUSD | 3,157,329 EASY | $55,193 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,826 XPAX | 3,157,947 EASY | $55,203 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,529 XUSDT | 3,176,972 EASY | $69,065 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $989,499 | (snapshot) | (snapshot) |
| **Swap TVL** | $872,183 | - | - |
| **Swap volume** | $20,954 | $461,716 | $1,431,863 |
| **Spot volume** | $92.77 | $1,017 | $9,521 |
| **Swap fees** | $117.36 | $2,423 | $7,636 |
| **DAU (avg)** | ≈369 | ≈400 | ≈410 |
| **Liquidity pools** | 11,786 | - | - |
| **Spot pairs** | 1,676 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,043.89 EASY** |
| Approx. USD | **≈$18.25** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
