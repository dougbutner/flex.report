# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-06 15:07 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,896** |
| **EASY price** | **$0.0167** (≈6.58 XPR) |
| **EASY price in XUSDC** | **0.016945 XUSDC** |
| **Total EASY pools TVL** | **$402,177** |
| **Total USD backing (stables)** | **$63,568** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **855.34 EASY** (≈$14.26) in the reflection pool |
| **7d volume** | **$65,497** |
| **30d volume** | **$381,305** |
| **Flexers (holders on contract)** | **933** |
| **Market cap (fully circulating)** | **$350,036** |
| **Share of Alcor Proton swap volume (24h)** | **≈33.48%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,896 | $21,654 | **33.5%** |
| 7d | $65,497 | $205,389 | **24.2%** |
| 30d | $381,305 | $921,227 | **29.3%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,004 | $66,458 | 3,226,826 EASY | 12,671.86 XUSDC | +0.0% |
| EASY/XMD | $2,733 | $66,666 | 3,228,482 EASY | 12,648.17 XMD | -0.0% |
| EASY/XPR | $1,735 | $24,563 | 485,254 EASY | 6,452,145.88 XPR | -0.1% |
| EASY/XUSDT | $881.63 | $66,912 | 3,241,844 EASY | 12,455.03 XUSDT | +0.6% |
| EASY/XXRP | $697.14 | $19,647 | 318,802 EASY | 13,780.30 XXRP | +0.2% |
| EASY/XMT | $479.91 | $3,286 | 40,642 EASY | 12,542.74 XMT | -1.7% |
| EASY/XPYUSD | $371.50 | $54,241 | 3,235,818 EASY | 12,519.01 XPYUSD | +0.0% |
| EASY/METAL | $268.37 | $4,460 | 64,174 EASY | 33,985.69 METAL | -0.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,477 XMD | 3,228,482 EASY | $66,666 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,672 XUSDC | 3,226,826 EASY | $66,458 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,644 XPYUSD | 3,235,818 EASY | $54,241 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,007 XPAX | 3,297,612 EASY | $68,284 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,570 XUSDT | 3,241,844 EASY | $66,912 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,093,908 | (snapshot) | (snapshot) |
| **Swap TVL** | $954,193 | - | - |
| **Swap volume** | $32,551 | $270,885 | $1,302,532 |
| **Spot volume** | $151.73 | $5,985 | $51,874 |
| **Swap fees** | $147.60 | $1,639 | $6,862 |
| **DAU (avg)** | ≈77 | ≈78 | ≈79 |
| **Liquidity pools** | 11,237 | - | - |
| **Spot pairs** | 1,643 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **855.34 EASY** |
| Approx. USD | **≈$14.26** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
