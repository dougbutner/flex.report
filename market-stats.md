# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-17 17:22 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,857** |
| **EASY price** | **$0.0176** (≈7.13 XPR) |
| **EASY price in XUSDC** | **0.017903 XUSDC** |
| **Total EASY pools TVL** | **$389,773** |
| **Total USD backing (stables)** | **$72,032** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,747.04 EASY** (≈$30.83) in the reflection pool |
| **7d volume** | **$136,479** |
| **30d volume** | **$622,847** |
| **Flexers (holders on contract)** | **973** |
| **Market cap (fully circulating)** | **$370,629** |
| **Share of Alcor Proton swap volume (24h)** | **≈21.9%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,857 | $20,885 | **21.9%** |
| 7d | $136,479 | $418,159 | **24.6%** |
| 30d | $622,847 | $1,323,379 | **32.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $1,592 | $70,345 | 3,164,782 EASY | 14,684.07 XMD | +0.3% |
| EASY/XUSDC | $1,256 | $69,601 | 3,139,285 EASY | 14,195.44 XUSDC | +0.3% |
| EASY/XXRP | $719.25 | $15,028 | 410,442 EASY | 6,107.29 XXRP | -0.5% |
| EASY/XUSDT | $572.74 | $69,347 | 3,139,732 EASY | 14,187.35 XUSDT | +0.2% |
| EASY/XXLM | $555.61 | $3,888 | 159,216 EASY | 5,937.43 XXLM | -1.6% |
| EASY/XPR | $495.10 | $20,966 | 189,551 EASY | 7,114,107.24 XPR | -0.5% |
| EASY/XPAX | $133.76 | $55,446 | 3,141,575 EASY | 14,216.69 XPAX | +0.3% |
| EASY/XPYUSD | $118.44 | $55,418 | 3,140,002 EASY | 14,182.50 XPYUSD | +0.3% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,489 XMD | 3,164,782 EASY | $70,345 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,195 XUSDC | 3,139,285 EASY | $69,601 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,228 XPYUSD | 3,140,002 EASY | $55,418 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,948 XPAX | 3,141,575 EASY | $55,446 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,934 XUSDT | 3,139,732 EASY | $69,347 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,120,266 | (snapshot) | (snapshot) |
| **Swap TVL** | $971,808 | - | - |
| **Swap volume** | $26,742 | $554,638 | $1,946,226 |
| **Spot volume** | $69.15 | $2,556 | $9,065 |
| **Swap fees** | $147.54 | $2,755 | $10,301 |
| **DAU (avg)** | ≈71 | ≈76 | ≈76 |
| **Liquidity pools** | 11,574 | - | - |
| **Spot pairs** | 1,668 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,747.04 EASY** |
| Approx. USD | **≈$30.83** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
