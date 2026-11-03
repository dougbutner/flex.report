# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-03 19:54 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,366** |
| **EASY price** | **$0.0188** (≈10.00 XPR) |
| **EASY price in XUSDC** | **0.018923 XUSDC** |
| **Total EASY pools TVL** | **$367,966** |
| **Total USD backing (stables)** | **$63,091** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **942.26 EASY** (≈$17.67) in the reflection pool |
| **7d volume** | **$54,522** |
| **30d volume** | **$519,530** |
| **Flexers (holders on contract)** | **6,061** |
| **Market cap (fully circulating)** | **$393,880** |
| **Share of Alcor Proton swap volume (24h)** | **≈23.59%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,366 | $20,623 | **23.6%** |
| 7d | $54,522 | $138,804 | **28.2%** |
| 30d | $519,530 | $916,416 | **36.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,576 | $73,047 | 3,053,474 EASY | 15,775.10 XUSDC | +0.7% |
| EASY/XUSDT | $1,298 | $73,045 | 3,066,997 EASY | 15,520.15 XUSDT | +0.0% |
| EASY/XXRP | $895.14 | $18,851 | 412,828 EASY | 8,815.96 XXRP | -0.7% |
| EASY/XBTC | $476.48 | $6,991 | 230,239 EASY | 0.03 XBTC | -0.3% |
| EASY/XPR | $400.83 | $12,481 | 392,562 EASY | 2,737,428.91 XPR | +0.4% |
| EASY/XPYUSD | $294.13 | $57,601 | 3,071,031 EASY | 15,444.44 XPYUSD | +1.5% |
| EASY/XMD | $223.46 | $40,973 | 2,156,755 EASY | 520.51 XMD | +0.6% |
| EASY/XMD | $56.85 | $5,706 | 303,697 EASY | 9.65 XMD | -1.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $520.76 XMD | 2,156,755 EASY | $40,973 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,775 XUSDC | 3,053,474 EASY | $73,047 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,475 XPYUSD | 3,071,031 EASY | $57,601 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,515 XPAX | 3,081,817 EASY | $57,803 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,520 XUSDT | 3,066,997 EASY | $73,045 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $925,172 | (snapshot) | (snapshot) |
| **Swap TVL** | $822,574 | - | - |
| **Swap volume** | $26,989 | $193,326 | $1,435,946 |
| **Spot volume** | $66.89 | $748.96 | $7,337 |
| **Swap fees** | $158.60 | $1,099 | $7,446 |
| **DAU (avg)** | ≈344 | ≈348 | ≈387 |
| **Liquidity pools** | 11,830 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **942.26 EASY** |
| Approx. USD | **≈$17.67** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
