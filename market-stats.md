# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-16 13:24 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$10,387** |
| **EASY price** | **$0.0167** (≈6.70 XPR) |
| **EASY price in XUSDC** | **0.016785 XUSDC** |
| **Total EASY pools TVL** | **$387,550** |
| **Total USD backing (stables)** | **$65,376** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **782.13 EASY** (≈$13.05) in the reflection pool |
| **7d volume** | **$58,823** |
| **30d volume** | **$356,021** |
| **Flexers (holders on contract)** | **941** |
| **Market cap (fully circulating)** | **$350,425** |
| **Share of Alcor Proton swap volume (24h)** | **≈36.57%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $10,387 | $18,019 | **36.6%** |
| 7d | $58,823 | $154,282 | **27.6%** |
| 30d | $356,021 | $767,145 | **31.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XXRP | $2,769 | $16,880 | 274,362 EASY | 12,365.83 XXRP | +0.6% |
| EASY/XMD | $2,282 | $66,424 | 3,242,467 EASY | 12,413.01 XMD | +0.7% |
| EASY/XUSDC | $1,847 | $69,553 | 3,242,191 EASY | 15,450.66 XUSDC | +0.7% |
| EASY/XPR | $1,768 | $33,659 | 863,312 EASY | 7,733,085.71 XPR | +0.1% |
| EASY/XUSDT | $893.43 | $66,527 | 3,244,546 EASY | 12,373.23 XUSDT | +1.5% |
| EASY/METAL | $268.22 | $2,042 | 41,499 EASY | 13,731.79 METAL | -1.2% |
| EASY/XPYUSD | $220.32 | $54,106 | 3,242,446 EASY | 12,407.52 XPYUSD | +0.7% |
| EASY/XPAX | $92.34 | $54,924 | 3,291,436 EASY | 12,793.15 XPAX | +0.3% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,317 XMD | 3,242,467 EASY | $66,424 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,451 XUSDC | 3,242,191 EASY | $69,553 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,442 XPYUSD | 3,242,446 EASY | $54,106 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,765 XPAX | 3,291,436 EASY | $54,924 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,386 XUSDT | 3,244,546 EASY | $66,527 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,069,919 | (snapshot) | (snapshot) |
| **Swap TVL** | $923,153 | - | - |
| **Swap volume** | $28,406 | $213,105 | $1,123,166 |
| **Spot volume** | $113.35 | $3,011 | $33,457 |
| **Swap fees** | $133.37 | $1,063 | $5,863 |
| **DAU (avg)** | ≈74 | ≈77 | ≈78 |
| **Liquidity pools** | 11,342 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **782.13 EASY** |
| Approx. USD | **≈$13.05** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
