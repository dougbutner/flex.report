# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-16 17:06 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$4,814** |
| **EASY price** | **$0.0179** (≈8.05 XPR) |
| **EASY price in XUSDC** | **0.017952 XUSDC** |
| **Total EASY pools TVL** | **$394,373** |
| **Total USD backing (stables)** | **$71,961** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,325.20 EASY** (≈$23.67) in the reflection pool |
| **7d volume** | **$48,839** |
| **30d volume** | **$367,961** |
| **Flexers (holders on contract)** | **1,873** |
| **Market cap (fully circulating)** | **$375,062** |
| **Share of Alcor Proton swap volume (24h)** | **≈24.89%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $4,814 | $14,531 | **24.9%** |
| 7d | $48,839 | $172,168 | **22.1%** |
| 30d | $367,961 | $1,143,681 | **24.3%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $1,917 | $70,264 | 3,134,967 EASY | 14,273.28 XUSDC | -0.0% |
| EASY/XUSDT | $594.36 | $70,263 | 3,143,028 EASY | 14,128.51 XUSDT | +0.2% |
| EASY/XMD | $535.16 | $70,975 | 3,160,326 EASY | 14,764.43 XMD | +0.1% |
| EASY/XPR | $408.44 | $23,464 | 530,997 EASY | 6,308,070.72 XPR | -0.1% |
| EASY/XXRP | $387.64 | $18,490 | 283,423 EASY | 10,148.99 XXRP | -0.5% |
| EASY/XXLM | $242.69 | $1,674 | 49,444 EASY | 4,344.08 XXLM | -0.5% |
| EASY/XSOL | $185.11 | $907.88 | 42,105 EASY | 1.49 XSOL | +1.5% |
| EASY/XPYUSD | $146.95 | $55,973 | 3,133,978 EASY | 14,290.53 XPYUSD | +0.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $14,540 XMD | 3,160,326 EASY | $70,975 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,273 XUSDC | 3,134,967 EASY | $70,264 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,406 XPYUSD | 3,133,978 EASY | $55,973 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,436 XPAX | 3,137,228 EASY | $56,031 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,129 XUSDT | 3,143,028 EASY | $70,263 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,082,916 | (snapshot) | (snapshot) |
| **Swap TVL** | $946,204 | - | - |
| **Swap volume** | $19,345 | $221,007 | $1,511,642 |
| **Spot volume** | $214.54 | $1,960 | $11,979 |
| **Swap fees** | $86.57 | $1,170 | $8,223 |
| **DAU (avg)** | ≈409 | ≈406 | ≈412 |
| **Liquidity pools** | 11,767 | - | - |
| **Spot pairs** | 1,675 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,325.20 EASY** |
| Approx. USD | **≈$23.67** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
