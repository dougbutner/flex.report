# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-24 16:23 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$21,900** |
| **EASY price** | **$0.0180** (≈9.72 XPR) |
| **EASY price in XUSDC** | **0.018049 XUSDC** |
| **Total EASY pools TVL** | **$406,680** |
| **Total USD backing (stables)** | **$72,224** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **946.56 EASY** (≈$17.01) in the reflection pool |
| **7d volume** | **$94,865** |
| **30d volume** | **$490,032** |
| **Flexers (holders on contract)** | **6,053** |
| **Market cap (fully circulating)** | **$377,404** |
| **Share of Alcor Proton swap volume (24h)** | **≈50.3%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $21,900 | $21,634 | **50.3%** |
| 7d | $94,865 | $161,615 | **37.0%** |
| 30d | $490,032 | $928,944 | **34.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $8,262 | $70,626 | 3,126,809 EASY | 14,431.99 XUSDC | -1.1% |
| EASY/XPR | $4,766 | $29,229 | 406,439 EASY | 11,852,896.44 XPR | -0.4% |
| EASY/XMD | $3,167 | $71,576 | 3,153,137 EASY | 14,902.28 XMD | -1.1% |
| EASY/XUSDT | $1,976 | $70,616 | 3,133,340 EASY | 14,305.26 XUSDT | -0.4% |
| EASY/XXRP | $1,822 | $23,894 | 505,353 EASY | 11,795.51 XXRP | +3.4% |
| EASY/XXLM | $671.04 | $1,593 | 18,706 EASY | 7,500.81 XXLM | +5.2% |
| EASY/XBTC | $489.85 | $6,458 | 287,500 EASY | 0.02 XBTC | +1.1% |
| EASY/XDOGE | $260.81 | $1,321 | 8,664 EASY | 15,543.91 XDOGE | +4.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,909 XMD | 3,153,137 EASY | $71,576 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,432 XUSDC | 3,126,809 EASY | $70,626 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,051 XPYUSD | 3,170,282 EASY | $56,975 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,332 XPAX | 3,156,942 EASY | $56,735 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,305 XUSDT | 3,133,340 EASY | $70,616 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $972,990 | (snapshot) | (snapshot) |
| **Swap TVL** | $864,742 | - | - |
| **Swap volume** | $43,534 | $256,480 | $1,418,976 |
| **Spot volume** | $103.42 | $2,200 | $11,132 |
| **Swap fees** | $182.65 | $1,146 | $7,391 |
| **DAU (avg)** | ≈396 | ≈382 | ≈405 |
| **Liquidity pools** | 11,805 | - | - |
| **Spot pairs** | 1,678 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **946.56 EASY** |
| Approx. USD | **≈$17.01** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
