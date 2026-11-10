# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-10 20:06 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$11,682** |
| **EASY price** | **$0.0177** (≈10.83 XPR) |
| **EASY price in XUSDC** | **0.017684 XUSDC** |
| **Total EASY pools TVL** | **$361,627** |
| **Total USD backing (stables)** | **$55,932** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **995.13 EASY** (≈$17.58) in the reflection pool |
| **7d volume** | **$58,239** |
| **30d volume** | **$483,623** |
| **Flexers (holders on contract)** | **6,066** |
| **Market cap (fully circulating)** | **$370,934** |
| **Share of Alcor Proton swap volume (24h)** | **≈33.44%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $11,682 | $23,253 | **33.4%** |
| 7d | $58,239 | $188,710 | **23.6%** |
| 30d | $483,623 | $892,459 | **35.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $4,809 | $69,594 | 3,158,682 EASY | 13,850.47 XUSDC | -1.1% |
| EASY/XXRP | $2,432 | $14,261 | 112,357 EASY | 11,825.72 XXRP | +1.8% |
| EASY/XUSDT | $1,586 | $69,594 | 3,160,474 EASY | 13,818.59 XUSDT | +1.8% |
| EASY/XPR | $736.58 | $15,153 | 363,338 EASY | 5,360,334.80 XPR | +0.5% |
| EASY/XPAX | $614.11 | $55,766 | 3,159,941 EASY | 13,890.01 XPAX | -1.1% |
| EASY/XXLM | $464.55 | $1,985 | 6,627 EASY | 13,233.74 XXLM | +1.1% |
| EASY/XPYUSD | $454.95 | $55,848 | 3,164,583 EASY | 13,746.05 XPYUSD | -1.4% |
| EASY/METAL | $128.89 | $5,507 | 308,231 EASY | 676.48 METAL | +1.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $503.58 XMD | 2,157,701 EASY | $38,582 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,850 XUSDC | 3,158,682 EASY | $69,594 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,640 XPYUSD | 3,164,583 EASY | $55,848 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,990 XPAX | 3,159,941 EASY | $55,766 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,819 XUSDT | 3,160,474 EASY | $69,594 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $854,254 | (snapshot) | (snapshot) |
| **Swap TVL** | $763,221 | - | - |
| **Swap volume** | $34,935 | $246,949 | $1,376,082 |
| **Spot volume** | $158.11 | $625.63 | $5,811 |
| **Swap fees** | $187.93 | $1,400 | $7,189 |
| **DAU (avg)** | ≈398 | ≈351 | ≈373 |
| **Liquidity pools** | 11,846 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **995.13 EASY** |
| Approx. USD | **≈$17.58** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
