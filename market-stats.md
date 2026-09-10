# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-10 16:47 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$11,699** |
| **EASY price** | **$0.0185** (≈6.67 XPR) |
| **EASY price in XUSDC** | **0.018831 XUSDC** |
| **Total EASY pools TVL** | **$2,294,802** |
| **Total USD backing (stables)** | **$79,748** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **968.42 EASY** (≈$17.90) in the reflection pool |
| **7d volume** | **$74,020** |
| **30d volume** | **$543,464** |
| **Flexers (holders on contract)** | **962** |
| **Market cap (fully circulating)** | **$388,235** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.96%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $11,699 | $30,141 | **28.0%** |
| 7d | $74,020 | $242,904 | **23.4%** |
| 30d | $543,464 | $1,037,115 | **34.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,747 | $73,669 | 3,124,233 EASY | 15,916.47 XUSDC | -0.6% |
| EASY/XMD | $2,706 | $72,867 | 3,087,895 EASY | 16,095.20 XMD | -0.7% |
| EASY/XXRP | $1,032 | $14,859 | 384,633 EASY | 5,732.58 XXRP | +1.3% |
| EASY/XPR | $770.65 | $885.61 | 46,103 EASY | 12,015.47 XPR | +0.1% |
| EASY/VIBRR | $548.87 | $1,622 | 68,878 EASY | 2,844,528.66 VIBRR | -6.3% |
| EASY/XUSDT | $523.05 | $72,000 | 3,060,518 EASY | 15,641.75 XUSDT | -0.5% |
| EASY/XPR | $463.38 | $43,034 | 607,089 EASY | 11,485,971.57 XPR | -0.0% |
| EASY/XXLM | $362.86 | $3,952 | 109,696 EASY | 10,937.41 XXLM | +1.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,788 XMD | 3,087,895 EASY | $72,867 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,916 XUSDC | 3,124,233 EASY | $73,669 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,742 XPYUSD | 3,060,742 EASY | $56,579 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,412 XPAX | 3,108,853 EASY | $57,474 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,427 XUSDT | 3,060,518 EASY | $72,000 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,067,278 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,904,179 | - | - |
| **Swap volume** | $41,840 | $316,924 | $1,580,579 |
| **Spot volume** | $305.02 | $2,605 | $8,181 |
| **Swap fees** | $172.94 | $1,530 | $8,451 |
| **DAU (avg)** | ≈75 | ≈74 | ≈75 |
| **Liquidity pools** | 11,525 | - | - |
| **Spot pairs** | 1,667 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **968.42 EASY** |
| Approx. USD | **≈$17.90** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
