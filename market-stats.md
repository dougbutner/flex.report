# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-12 20:34 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$12,988** |
| **EASY price** | **$0.0181** (≈9.99 XPR) |
| **EASY price in XUSDC** | **0.018188 XUSDC** |
| **Total EASY pools TVL** | **$376,832** |
| **Total USD backing (stables)** | **$58,870** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **946.52 EASY** (≈$17.16) in the reflection pool |
| **7d volume** | **$62,920** |
| **30d volume** | **$483,701** |
| **Flexers (holders on contract)** | **6,067** |
| **Market cap (fully circulating)** | **$380,623** |
| **Share of Alcor Proton swap volume (24h)** | **≈26.9%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $12,988 | $35,299 | **26.9%** |
| 7d | $62,920 | $208,940 | **23.1%** |
| 30d | $483,701 | $889,341 | **35.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $4,381 | $16,114 | 593,122 EASY | 2,956,736.83 XPR | +8.6% |
| EASY/XUSDC | $3,410 | $71,093 | 3,114,593 EASY | 14,641.75 XUSDC | +2.3% |
| EASY/XUSDT | $1,239 | $71,093 | 3,119,978 EASY | 14,543.46 XUSDT | +2.2% |
| EASY/XBTC | $1,233 | $6,583 | 176,757 EASY | 0.05 XBTC | +4.6% |
| EASY/XXRP | $925.73 | $20,374 | 86,656 EASY | 18,709.79 XXRP | +5.9% |
| EASY/XPAX | $922.51 | $56,485 | 3,116,421 EASY | 14,670.95 XPAX | +2.4% |
| EASY/XXLM | $463.61 | $3,826 | 6,244 EASY | 26,081.53 XXLM | +3.9% |
| EASY/XPYUSD | $100.76 | $57,199 | 3,155,807 EASY | 13,901.11 XPYUSD | +0.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $510.38 XMD | 2,157,324 EASY | $39,612 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,642 XUSDC | 3,114,593 EASY | $71,093 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,239 XPYUSD | 3,155,807 EASY | $57,199 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,775 XPAX | 3,116,421 EASY | $56,485 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,543 XUSDT | 3,119,978 EASY | $71,093 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $886,511 | (snapshot) | (snapshot) |
| **Swap TVL** | $787,772 | - | - |
| **Swap volume** | $48,287 | $271,861 | $1,373,042 |
| **Spot volume** | $35.80 | $677.38 | $4,832 |
| **Swap fees** | $318.50 | $1,613 | $7,232 |
| **DAU (avg)** | ≈368 | ≈363 | ≈371 |
| **Liquidity pools** | 11,851 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **946.52 EASY** |
| Approx. USD | **≈$17.16** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
