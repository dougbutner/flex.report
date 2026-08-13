# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-13 14:17 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,318** |
| **EASY price** | **$0.0165** (≈6.67 XPR) |
| **EASY price in XUSDC** | **0.016654 XUSDC** |
| **Total EASY pools TVL** | **$385,788** |
| **Total USD backing (stables)** | **$61,606** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **700.62 EASY** (≈$11.58) in the reflection pool |
| **7d volume** | **$67,955** |
| **30d volume** | **$388,495** |
| **Flexers (holders on contract)** | **940** |
| **Market cap (fully circulating)** | **$346,978** |
| **Share of Alcor Proton swap volume (24h)** | **≈26.83%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,318 | $14,502 | **26.8%** |
| 7d | $67,955 | $177,479 | **27.7%** |
| 30d | $388,495 | $792,135 | **32.9%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $978.84 | $66,304 | 3,271,317 EASY | 12,252.56 XUSDC | -0.2% |
| EASY/XMD | $834.67 | $65,956 | 3,255,226 EASY | 12,198.50 XMD | -0.3% |
| EASY/XXRP | $677.81 | $25,444 | 345,445 EASY | 19,708.89 XXRP | +0.2% |
| EASY/XMT | $594.81 | $3,525 | 32,037 EASY | 15,077.72 XMT | +1.8% |
| EASY/METAL | $587.99 | $2,036 | 46,551 EASY | 12,872.27 METAL | +0.4% |
| EASY/XPR | $438.73 | $26,027 | 473,810 EASY | 7,341,133.04 XPR | -0.1% |
| EASY/XXLM | $262.03 | $770.66 | 153 EASY | 4,876.33 XXLM | +0.3% |
| EASY/XDOGE | $233.08 | $348.00 | 7,126 EASY | 3,286.44 XDOGE | +0.9% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,168 XMD | 3,255,226 EASY | $65,956 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,253 XUSDC | 3,271,317 EASY | $66,304 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,283 XPYUSD | 3,253,363 EASY | $53,756 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,703 XPAX | 3,291,406 EASY | $54,385 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,177 XUSDT | 3,257,441 EASY | $66,000 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,074,352 | (snapshot) | (snapshot) |
| **Swap TVL** | $924,928 | - | - |
| **Swap volume** | $19,820 | $245,435 | $1,180,629 |
| **Spot volume** | $439.31 | $3,967 | $33,834 |
| **Swap fees** | $112.26 | $1,241 | $6,191 |
| **DAU (avg)** | ≈76 | ≈79 | ≈79 |
| **Liquidity pools** | 11,315 | - | - |
| **Spot pairs** | 1,655 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **700.62 EASY** |
| Approx. USD | **≈$11.58** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
