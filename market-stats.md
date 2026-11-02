# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-02 22:01 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$3,852** |
| **EASY price** | **$0.0187** (≈10.08 XPR) |
| **EASY price in XUSDC** | **0.018699 XUSDC** |
| **Total EASY pools TVL** | **$360,383** |
| **Total USD backing (stables)** | **$62,628** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **953.13 EASY** (≈$17.78) in the reflection pool |
| **7d volume** | **$56,895** |
| **30d volume** | **$520,200** |
| **Flexers (holders on contract)** | **6,061** |
| **Market cap (fully circulating)** | **$391,688** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.58%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $3,852 | $10,115 | **27.6%** |
| 7d | $56,895 | $155,583 | **26.8%** |
| 30d | $520,200 | $926,413 | **36.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,443 | $72,725 | 3,071,717 EASY | 15,432.23 XUSDC | -1.4% |
| EASY/XPR | $656.61 | $12,386 | 385,885 EASY | 2,803,967.96 XPR | -0.3% |
| EASY/XUSDT | $587.63 | $72,725 | 3,075,584 EASY | 15,359.63 XUSDT | -1.3% |
| EASY/XPYUSD | $367.34 | $57,350 | 3,074,760 EASY | 15,374.94 XPYUSD | +0.3% |
| EASY/XXRP | $366.48 | $18,631 | 393,167 EASY | 9,108.93 XXRP | +0.4% |
| EASY/XMD | $190.90 | $40,748 | 2,156,928 EASY | 517.24 XMD | -1.6% |
| EASY/XMD | $47.17 | $5,675 | 304,236 EASY | 0.00 XMD | -1.4% |
| EASY/XBTC | $47.11 | $6,987 | 229,120 EASY | 0.04 XBTC | -0.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $517.50 XMD | 2,156,928 EASY | $40,748 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,432 XUSDC | 3,071,717 EASY | $72,725 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,499 XPYUSD | 3,074,760 EASY | $57,350 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,546 XPAX | 3,081,743 EASY | $57,480 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,360 XUSDT | 3,075,584 EASY | $72,725 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $912,595 | (snapshot) | (snapshot) |
| **Swap TVL** | $811,466 | - | - |
| **Swap volume** | $13,968 | $212,478 | $1,446,613 |
| **Spot volume** | $44.54 | $719.45 | $7,412 |
| **Swap fees** | $76.96 | $1,204 | $7,489 |
| **DAU (avg)** | ≈330 | ≈352 | ≈388 |
| **Liquidity pools** | 11,828 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **953.13 EASY** |
| Approx. USD | **≈$17.78** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
