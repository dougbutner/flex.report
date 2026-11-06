# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-06 19:46 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$9,209** |
| **EASY price** | **$0.0185** (≈10.27 XPR) |
| **EASY price in XUSDC** | **0.018553 XUSDC** |
| **Total EASY pools TVL** | **$360,702** |
| **Total USD backing (stables)** | **$61,588** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,256.56 EASY** (≈$23.21) in the reflection pool |
| **7d volume** | **$40,420** |
| **30d volume** | **$480,400** |
| **Flexers (holders on contract)** | **6,062** |
| **Market cap (fully circulating)** | **$387,960** |
| **Share of Alcor Proton swap volume (24h)** | **≈28.77%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $9,209 | $22,800 | **28.8%** |
| 7d | $40,420 | $134,107 | **23.2%** |
| 30d | $480,400 | $885,914 | **35.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,215 | $72,178 | 3,083,804 EASY | 15,207.33 XUSDC | -1.3% |
| EASY/XXRP | $2,918 | $17,816 | 359,655 EASY | 9,200.36 XXRP | +2.1% |
| EASY/XPR | $731.19 | $12,148 | 346,930 EASY | 3,203,078.40 XPR | -1.8% |
| EASY/XUSDT | $659.19 | $72,177 | 3,090,321 EASY | 15,085.92 XUSDT | -0.6% |
| EASY/XXLM | $454.52 | $2,148 | 22,285 EASY | 11,334.57 XXLM | -3.4% |
| EASY/XPYUSD | $335.03 | $57,000 | 3,085,375 EASY | 15,177.49 XPYUSD | -1.0% |
| EASY/USDC | $310.13 | $4.29 | 200,263 EASY | 2.15 USDC | -0.7% |
| EASY/XPAX | $270.26 | $57,013 | 3,086,056 EASY | 15,228.29 XPAX | -1.0% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $515.75 XMD | 2,157,027 EASY | $40,365 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,207 XUSDC | 3,083,804 EASY | $72,178 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,155 XPYUSD | 3,085,375 EASY | $57,000 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,365 XPAX | 3,086,056 EASY | $57,013 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,086 XUSDT | 3,090,321 EASY | $72,177 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $905,474 | (snapshot) | (snapshot) |
| **Swap TVL** | $805,352 | - | - |
| **Swap volume** | $32,010 | $174,527 | $1,366,313 |
| **Spot volume** | $81.75 | $561.93 | $5,892 |
| **Swap fees** | $212.06 | $1,010 | $7,163 |
| **DAU (avg)** | ≈348 | ≈346 | ≈379 |
| **Liquidity pools** | 11,835 | - | - |
| **Spot pairs** | 1,679 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,256.56 EASY** |
| Approx. USD | **≈$23.21** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
