# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-12 14:15 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,204** |
| **EASY price** | **$0.0166** (≈6.65 XPR) |
| **EASY price in XUSDC** | **0.016745 XUSDC** |
| **Total EASY pools TVL** | **$387,849** |
| **Total USD backing (stables)** | **$62,262** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **685.34 EASY** (≈$11.39) in the reflection pool |
| **7d volume** | **$73,394** |
| **30d volume** | **$391,700** |
| **Flexers (holders on contract)** | **940** |
| **Market cap (fully circulating)** | **$349,102** |
| **Share of Alcor Proton swap volume (24h)** | **≈19.32%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,204 | $25,909 | **19.3%** |
| 7d | $73,394 | $186,029 | **28.3%** |
| 30d | $391,700 | $795,930 | **33.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $1,746 | $66,175 | 3,246,102 EASY | 12,350.44 XMD | +0.1% |
| EASY/XUSDC | $1,575 | $66,636 | 3,246,075 EASY | 12,673.48 XUSDC | +0.1% |
| EASY/XXRP | $747.50 | $25,698 | 387,805 EASY | 19,073.84 XXRP | +0.1% |
| EASY/XUSDT | $550.76 | $66,478 | 3,254,328 EASY | 12,208.55 XUSDT | -0.0% |
| EASY/METAL | $383.83 | $2,065 | 59,579 EASY | 10,743.42 METAL | +0.1% |
| EASY/XDOGE | $323.68 | $351.36 | 18,092 EASY | 702.84 XDOGE | -1.4% |
| EASY/XMT | $189.16 | $3,251 | 40,494 EASY | 12,543.54 XMT | +0.4% |
| EASY/XXLM | $163.86 | $786.43 | 5,122 EASY | 4,359.98 XXLM | +0.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,213 XMD | 3,246,102 EASY | $66,175 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,673 XUSDC | 3,246,075 EASY | $66,636 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,273 XPYUSD | 3,254,644 EASY | $54,215 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,809 XPAX | 3,291,527 EASY | $54,829 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,270 XUSDT | 3,254,328 EASY | $66,478 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,084,430 | (snapshot) | (snapshot) |
| **Swap TVL** | $934,411 | - | - |
| **Swap volume** | $32,113 | $259,424 | $1,187,630 |
| **Spot volume** | $366.29 | $3,647 | $33,418 |
| **Swap fees** | $158.27 | $1,279 | $6,222 |
| **DAU (avg)** | ≈77 | ≈79 | ≈79 |
| **Liquidity pools** | 11,300 | - | - |
| **Spot pairs** | 1,655 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **685.34 EASY** |
| Approx. USD | **≈$11.39** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
