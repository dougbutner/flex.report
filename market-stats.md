# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-19 18:55 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$5,924** |
| **EASY price** | **$0.0175** (≈8.99 XPR) |
| **EASY price in XUSDC** | **0.017679 XUSDC** |
| **Total EASY pools TVL** | **$392,004** |
| **Total USD backing (stables)** | **$69,347** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **991.33 EASY** (≈$17.39) in the reflection pool |
| **7d volume** | **$212,896** |
| **30d volume** | **$507,113** |
| **Flexers (holders on contract)** | **6,045** |
| **Market cap (fully circulating)** | **$368,414** |
| **Share of Alcor Proton swap volume (24h)** | **≈39.28%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $5,924 | $9,159 | **39.3%** |
| 7d | $212,896 | $272,445 | **43.9%** |
| 30d | $507,113 | $1,168,009 | **30.3%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XXRP | $1,352 | $18,134 | 324,702 EASY | 9,592.68 XXRP | -1.7% |
| EASY/XUSDC | $1,324 | $69,203 | 3,159,171 EASY | 13,843.53 XUSDC | +0.1% |
| EASY/XPR | $1,075 | $31,385 | 637,198 EASY | 10,370,926.71 XPR | -0.8% |
| EASY/XMD | $1,022 | $69,999 | 3,185,333 EASY | 14,320.88 XMD | +0.1% |
| EASY/XUSDT | $264.31 | $69,201 | 3,177,055 EASY | 13,527.76 XUSDT | -0.1% |
| EASY/XPYUSD | $210.04 | $55,340 | 3,158,041 EASY | 13,862.18 XPYUSD | +0.1% |
| EASY/XPAX | $198.37 | $55,372 | 3,159,887 EASY | 13,891.45 XPAX | +0.0% |
| EASY/METAL | $156.25 | $2,786 | 41,810 EASY | 18,949.77 METAL | +0.6% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,197 XMD | 3,185,333 EASY | $69,999 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,844 XUSDC | 3,159,171 EASY | $69,203 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,794 XPYUSD | 3,158,041 EASY | $55,340 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,859 XPAX | 3,159,887 EASY | $55,372 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $13,528 XUSDT | 3,177,055 EASY | $69,201 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $993,931 | (snapshot) | (snapshot) |
| **Swap TVL** | $875,661 | - | - |
| **Swap volume** | $15,083 | $485,342 | $1,675,122 |
| **Spot volume** | $22.10 | $1,660 | $11,621 |
| **Swap fees** | $80.48 | $2,581 | $9,105 |
| **DAU (avg)** | ≈371 | ≈404 | ≈411 |
| **Liquidity pools** | 11,785 | - | - |
| **Spot pairs** | 1,676 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **991.33 EASY** |
| Approx. USD | **≈$17.39** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
