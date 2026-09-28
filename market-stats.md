# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-28 19:55 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$8,955** |
| **EASY price** | **$0.0183** (≈7.55 XPR) |
| **EASY price in XUSDC** | **0.018490 XUSDC** |
| **Total EASY pools TVL** | **$442,366** |
| **Total USD backing (stables)** | **$76,224** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **669.50 EASY** (≈$12.28) in the reflection pool |
| **7d volume** | **$79,877** |
| **30d volume** | **$478,668** |
| **Flexers (holders on contract)** | **993** |
| **Market cap (fully circulating)** | **$385,163** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.02%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $8,955 | $21,898 | **29.0%** |
| 7d | $79,877 | $194,089 | **29.2%** |
| 30d | $478,668 | $1,469,010 | **24.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $2,083 | $29,871 | 304,641 EASY | 10,000,119.62 XPR | -0.6% |
| EASY/XMD | $1,884 | $72,512 | 3,114,156 EASY | 15,605.95 XMD | -0.2% |
| EASY/XXRP | $1,810 | $20,370 | 418,126 EASY | 8,493.25 XXRP | +0.3% |
| EASY/XUSDC | $1,310 | $71,766 | 3,089,049 EASY | 15,109.64 XUSDC | -0.2% |
| EASY/XXLM | $493.19 | $1,774 | 96,619 EASY | 8.70 XXLM | -3.0% |
| EASY/METAL | $425.20 | $5,063 | 139,237 EASY | 19,892.85 METAL | +0.8% |
| EASY/XUSDT | $309.47 | $71,664 | 3,090,233 EASY | 15,087.49 XUSDT | -0.4% |
| EASY/XDOGE | $193.05 | $1,476 | 74,404 EASY | 1,189.64 XDOGE | +1.3% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,395 XMD | 3,114,156 EASY | $72,512 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,110 XUSDC | 3,089,049 EASY | $71,766 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,267 XPYUSD | 3,087,798 EASY | $56,634 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,516 XPAX | 3,135,998 EASY | $72,033 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,986 XUSDT | 3,090,233 EASY | $71,664 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,224,910 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,072,823 | - | - |
| **Swap volume** | $30,854 | $273,966 | $1,947,678 |
| **Spot volume** | $1,090 | $1,773 | $12,160 |
| **Swap fees** | $196.36 | $1,396 | $10,160 |
| **DAU (avg)** | ≈406 | ≈415 | ≈422 |
| **Liquidity pools** | 11,635 | - | - |
| **Spot pairs** | 1,670 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **669.50 EASY** |
| Approx. USD | **≈$12.28** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
