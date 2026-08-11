# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-11 14:13 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,449** |
| **EASY price** | **$0.0165** (≈6.65 XPR) |
| **EASY price in XUSDC** | **0.016709 XUSDC** |
| **Total EASY pools TVL** | **$386,563** |
| **Total USD backing (stables)** | **$62,010** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **883.26 EASY** (≈$14.59) in the reflection pool |
| **7d volume** | **$74,567** |
| **30d volume** | **$391,038** |
| **Flexers (holders on contract)** | **939** |
| **Market cap (fully circulating)** | **$346,786** |
| **Share of Alcor Proton swap volume (24h)** | **≈19.66%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,449 | $38,615 | **19.7%** |
| 7d | $74,567 | $171,027 | **30.4%** |
| 30d | $391,038 | $784,878 | **33.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,385 | $66,271 | 3,249,555 EASY | 12,615.27 XUSDC | -0.3% |
| EASY/XMD | $2,073 | $65,792 | 3,249,583 EASY | 12,292.17 XMD | -0.3% |
| EASY/XPR | $1,325 | $24,985 | 433,044 EASY | 7,184,336.98 XPR | +0.0% |
| EASY/XBTC | $1,167 | $2,774 | 29,111 EASY | 0.04 XBTC | +0.0% |
| EASY/XXRP | $653.06 | $22,723 | 326,134 EASY | 17,242.99 XXRP | +0.2% |
| EASY/XUSDT | $647.20 | $65,967 | 3,253,846 EASY | 12,216.57 XUSDT | +0.5% |
| EASY/XMT | $356.63 | $3,262 | 44,555 EASY | 12,213.84 XMT | +0.4% |
| EASY/XPYUSD | $260.06 | $53,759 | 3,255,833 EASY | 12,183.45 XPYUSD | -0.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,138 XMD | 3,249,583 EASY | $65,792 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,615 XUSDC | 3,249,555 EASY | $66,271 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,253 XPYUSD | 3,255,833 EASY | $53,759 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,735 XPAX | 3,291,530 EASY | $54,348 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,241 XUSDT | 3,253,846 EASY | $65,967 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,079,483 | (snapshot) | (snapshot) |
| **Swap TVL** | $934,420 | - | - |
| **Swap volume** | $48,064 | $245,594 | $1,175,916 |
| **Spot volume** | $79.88 | $3,494 | $33,336 |
| **Swap fees** | $277.31 | $1,187 | $6,161 |
| **DAU (avg)** | ≈79 | ≈79 | ≈79 |
| **Liquidity pools** | 11,268 | - | - |
| **Spot pairs** | 1,654 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **883.26 EASY** |
| Approx. USD | **≈$14.59** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
