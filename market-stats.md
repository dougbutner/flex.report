# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-10 14:15 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,353** |
| **EASY price** | **$0.0165** (≈6.65 XPR) |
| **EASY price in XUSDC** | **0.016816 XUSDC** |
| **Total EASY pools TVL** | **$382,797** |
| **Total USD backing (stables)** | **$62,068** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **940.81 EASY** (≈$15.49) in the reflection pool |
| **7d volume** | **$72,179** |
| **30d volume** | **$396,788** |
| **Flexers (holders on contract)** | **937** |
| **Market cap (fully circulating)** | **$345,658** |
| **Share of Alcor Proton swap volume (24h)** | **≈38.3%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,353 | $15,064 | **38.3%** |
| 7d | $72,179 | $144,806 | **33.3%** |
| 30d | $396,788 | $791,701 | **33.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $2,852 | $65,779 | 3,239,203 EASY | 12,461.98 XUSDC | -0.4% |
| EASY/XMD | $2,229 | $65,541 | 3,239,817 EASY | 12,455.88 XMD | -0.4% |
| EASY/XPR | $1,455 | $24,902 | 430,773 EASY | 7,198,922.47 XPR | -0.4% |
| EASY/XUSDT | $1,425 | $66,011 | 3,269,821 EASY | 11,951.65 XUSDT | -0.3% |
| EASY/XXRP | $593.50 | $18,893 | 325,867 EASY | 13,338.57 XXRP | -0.2% |
| EASY/XPYUSD | $320.10 | $53,342 | 3,240,706 EASY | 12,436.42 XPYUSD | -0.4% |
| EASY/XMT | $109.53 | $3,288 | 49,551 EASY | 11,814.94 XMT | -0.6% |
| EASY/METAL | $88.90 | $3,549 | 74,626 EASY | 23,507.72 METAL | +0.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,214 XMD | 3,239,817 EASY | $65,541 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,462 XUSDC | 3,239,203 EASY | $65,779 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,505 XPYUSD | 3,240,706 EASY | $53,342 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $12,657 XPAX | 3,291,242 EASY | $54,174 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,190 XUSDT | 3,269,821 EASY | $66,011 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,069,211 | (snapshot) | (snapshot) |
| **Swap TVL** | $927,623 | - | - |
| **Swap volume** | $24,416 | $216,985 | $1,188,489 |
| **Spot volume** | $1,476 | $3,795 | $51,924 |
| **Swap fees** | $98.43 | $1,004 | $6,168 |
| **DAU (avg)** | ≈81 | ≈78 | ≈79 |
| **Liquidity pools** | 11,264 | - | - |
| **Spot pairs** | 1,653 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **940.81 EASY** |
| Approx. USD | **≈$15.49** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
