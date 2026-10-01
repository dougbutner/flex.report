# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-01 18:38 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,193** |
| **EASY price** | **$0.0182** (≈7.71 XPR) |
| **EASY price in XUSDC** | **0.018361 XUSDC** |
| **Total EASY pools TVL** | **$434,111** |
| **Total USD backing (stables)** | **$75,488** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **944.30 EASY** (≈$17.20) in the reflection pool |
| **7d volume** | **$68,988** |
| **30d volume** | **$453,080** |
| **Flexers (holders on contract)** | **1,005** |
| **Market cap (fully circulating)** | **$382,598** |
| **Share of Alcor Proton swap volume (24h)** | **≈20.06%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,193 | $32,646 | **20.1%** |
| 7d | $68,988 | $189,487 | **26.7%** |
| 30d | $453,080 | $1,425,063 | **24.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $2,045 | $72,247 | 3,125,812 EASY | 15,394.45 XMD | -0.3% |
| EASY/XUSDC | $1,527 | $71,390 | 3,099,974 EASY | 14,911.59 XUSDC | -0.4% |
| EASY/XPR | $1,410 | $26,903 | 262,537 EASY | 9,364,006.86 XPR | -0.1% |
| EASY/GEASY | $651.20 | $16,478 | 232,210 EASY | 276,976,542.28 GEASY | -3.5% |
| EASY/METAL | $597.75 | $3,822 | 82,759 EASY | 19,220.81 METAL | +1.4% |
| EASY/XUSDT | $521.07 | $71,367 | 3,097,363 EASY | 14,956.87 XUSDT | -0.3% |
| EASY/XXRP | $456.31 | $20,214 | 391,748 EASY | 8,814.37 XXRP | +0.3% |
| EASY/XPAXG | $222.36 | - | 9,336 EASY | 0.01 XPAXG | -9.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,298 XMD | 3,125,812 EASY | $72,247 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,912 XUSDC | 3,099,974 EASY | $71,390 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,950 XPYUSD | 3,099,161 EASY | $56,463 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,530 XPAX | 3,136,155 EASY | $71,667 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,936 XUSDT | 3,097,363 EASY | $71,367 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,188,583 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,042,153 | - | - |
| **Swap volume** | $40,839 | $258,475 | $1,878,143 |
| **Spot volume** | $661.96 | $3,722 | $12,484 |
| **Swap fees** | $193.27 | $1,366 | $9,796 |
| **DAU (avg)** | ≈422 | ≈410 | ≈419 |
| **Liquidity pools** | 11,652 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **944.30 EASY** |
| Approx. USD | **≈$17.20** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
