# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-07 19:08 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$40,246** |
| **EASY price** | **$0.0182** (≈8.02 XPR) |
| **EASY price in XUSDC** | **0.018316 XUSDC** |
| **Total EASY pools TVL** | **$425,136** |
| **Total USD backing (stables)** | **$74,467** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,133.48 EASY** (≈$20.67) in the reflection pool |
| **7d volume** | **$98,262** |
| **30d volume** | **$455,949** |
| **Flexers (holders on contract)** | **1,014** |
| **Market cap (fully circulating)** | **$382,990** |
| **Share of Alcor Proton swap volume (24h)** | **≈47.96%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $40,246 | $43,665 | **48.0%** |
| 7d | $98,262 | $220,484 | **30.8%** |
| 30d | $455,949 | $1,389,352 | **24.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $13,305 | $24,065 | 518,376 EASY | 6,418,471.61 XPR | -0.4% |
| EASY/XUSDC | $8,911 | $71,472 | 3,103,704 EASY | 14,840.84 XUSDC | -0.6% |
| EASY/XUSDT | $8,255 | $71,472 | 3,124,142 EASY | 14,467.94 XUSDT | -1.2% |
| EASY/XMD | $4,473 | $72,252 | 3,128,342 EASY | 15,344.99 XMD | -0.5% |
| EASY/XXRP | $1,774 | $19,652 | 312,140 EASY | 9,795.34 XXRP | +2.0% |
| EASY/XBTC | $1,111 | $3,630 | 159,197 EASY | 0.01 XBTC | +0.9% |
| EASY/XXLM | $701.18 | $1,762 | 68,807 EASY | 2,528.57 XXLM | +2.6% |
| EASY/METAL | $576.57 | $14,666 | 32,720 EASY | 119,633.75 METAL | +0.8% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,165 XMD | 3,128,342 EASY | $72,252 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,841 XUSDC | 3,103,704 EASY | $71,472 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,890 XPYUSD | 3,102,141 EASY | $56,603 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,717 XPAX | 3,136,465 EASY | $57,229 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,468 XUSDT | 3,124,142 EASY | $71,472 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,148,581 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,002,309 | - | - |
| **Swap volume** | $83,911 | $318,747 | $1,845,301 |
| **Spot volume** | $537.31 | $3,416 | $12,842 |
| **Swap fees** | $452.74 | $1,690 | $9,675 |
| **DAU (avg)** | ≈423 | ≈424 | ≈420 |
| **Liquidity pools** | 11,678 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,133.48 EASY** |
| Approx. USD | **≈$20.67** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
