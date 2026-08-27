# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-27 22:42 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$21,011** |
| **EASY price** | **$0.0193** (≈6.47 XPR) |
| **EASY price in XUSDC** | **0.019362 XUSDC** |
| **Total EASY pools TVL** | **$449,213** |
| **Total USD backing (stables)** | **$86,074** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **748.47 EASY** (≈$14.42) in the reflection pool |
| **7d volume** | **$223,501** |
| **30d volume** | **$496,349** |
| **Flexers (holders on contract)** | **952** |
| **Market cap (fully circulating)** | **$404,663** |
| **Share of Alcor Proton swap volume (24h)** | **≈32.89%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $21,011 | $42,875 | **32.9%** |
| 7d | $223,501 | $287,269 | **43.8%** |
| 30d | $496,349 | $902,723 | **35.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $5,473 | $50,586 | 1,125,480 EASY | 9,700,439.01 XPR | +0.8% |
| EASY/XUSDC | $4,113 | $76,149 | 3,018,631 EASY | 17,981.14 XUSDC | +1.8% |
| EASY/XMD | $3,877 | $75,490 | 3,043,458 EASY | 16,943.44 XMD | +1.8% |
| EASY/XXRP | $2,872 | $15,902 | 438,487 EASY | 5,150.35 XXRP | -0.3% |
| EASY/XUSDT | $1,266 | $74,605 | 3,017,921 EASY | 16,455.45 XUSDT | +1.9% |
| EASY/XBTC | $1,213 | $6,785 | 200,445 EASY | 0.04 XBTC | +1.2% |
| EASY/XDOGE | $773.42 | $1,170 | 26,677 EASY | 7,541.87 XDOGE | +0.2% |
| EASY/XUSDC | $520.78 | $5,747 | 148,033 EASY | 2,894.50 XUSDC | +1.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,844 XMD | 3,043,458 EASY | $75,490 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,981 XUSDC | 3,018,631 EASY | $76,149 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,623 XPYUSD | 3,100,151 EASY | $59,739 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,725 XPAX | 3,108,508 EASY | $59,900 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,451 XUSDT | 3,017,921 EASY | $74,605 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,205,008 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,045,631 | - | - |
| **Swap volume** | $63,886 | $510,770 | $1,399,071 |
| **Spot volume** | $209.74 | $1,079 | $14,256 |
| **Swap fees** | $398.32 | $2,841 | $7,656 |
| **DAU (avg)** | ≈73 | ≈78 | ≈77 |
| **Liquidity pools** | 11,448 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **748.47 EASY** |
| Approx. USD | **≈$14.42** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
