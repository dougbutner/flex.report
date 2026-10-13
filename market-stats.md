# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-13 19:40 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,651** |
| **EASY price** | **$0.0180** (≈8.02 XPR) |
| **EASY price in XUSDC** | **0.018211 XUSDC** |
| **Total EASY pools TVL** | **$393,293** |
| **Total USD backing (stables)** | **$72,795** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **906.42 EASY** (≈$16.35) in the reflection pool |
| **7d volume** | **$91,553** |
| **30d volume** | **$401,717** |
| **Flexers (holders on contract)** | **1,019** |
| **Market cap (fully circulating)** | **$378,727** |
| **Share of Alcor Proton swap volume (24h)** | **≈25.13%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,651 | $31,725 | **25.1%** |
| 7d | $91,553 | $225,746 | **28.9%** |
| 30d | $401,717 | $1,239,641 | **24.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,386 | $70,796 | 3,112,628 EASY | 14,677.07 XUSDC | +0.3% |
| EASY/XXRP | $1,829 | $15,102 | 319,008 EASY | 6,793.73 XXRP | +0.5% |
| EASY/XMD | $1,826 | $71,468 | 3,137,876 EASY | 15,170.59 XMD | +0.3% |
| EASY/XPR | $1,753 | $23,769 | 518,763 EASY | 6,410,287.79 XPR | +0.2% |
| EASY/XUSDT | $798.98 | $70,798 | 3,136,325 EASY | 14,248.50 XUSDT | -0.1% |
| EASY/XDOGE | $382.88 | $1,481 | 47,897 EASY | 7,370.85 XDOGE | +0.3% |
| EASY/XPYUSD | $364.77 | $56,394 | 3,127,730 EASY | 14,403.01 XPYUSD | -0.2% |
| EASY/METAL | $327.39 | $2,971 | 76,322 EASY | 13,499.32 METAL | -0.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,899 XMD | 3,137,876 EASY | $71,468 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,677 XUSDC | 3,112,628 EASY | $70,796 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,345 XPYUSD | 3,127,730 EASY | $56,394 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,448 XPAX | 3,137,107 EASY | $56,563 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,248 XUSDT | 3,136,325 EASY | $70,798 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,105,061 | (snapshot) | (snapshot) |
| **Swap TVL** | $964,641 | - | - |
| **Swap volume** | $42,375 | $317,299 | $1,641,358 |
| **Spot volume** | $654.44 | $2,198 | $11,770 |
| **Swap fees** | $262.84 | $1,788 | $8,891 |
| **DAU (avg)** | ≈404 | ≈406 | ≈416 |
| **Liquidity pools** | 11,719 | - | - |
| **Spot pairs** | 1,674 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **906.42 EASY** |
| Approx. USD | **≈$16.35** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
