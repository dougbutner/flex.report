# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-21 13:38 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$51,316** |
| **EASY price** | **$0.0193** (≈6.52 XPR) |
| **EASY price in XUSDC** | **0.019638 XUSDC** |
| **Total EASY pools TVL** | **$2,380,973** |
| **Total USD backing (stables)** | **$82,978** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **765.02 EASY** (≈$14.79) in the reflection pool |
| **7d volume** | **$141,948** |
| **30d volume** | **$403,637** |
| **Flexers (holders on contract)** | **946** |
| **Market cap (fully circulating)** | **$405,901** |
| **Share of Alcor Proton swap volume (24h)** | **≈40.68%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $51,316 | $74,819 | **40.7%** |
| 7d | $141,948 | $218,950 | **39.3%** |
| 30d | $403,637 | $818,549 | **33.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $14,472 | $75,588 | 3,021,985 EASY | 17,369.88 XMD | +1.8% |
| EASY/XUSDC | $14,219 | $74,786 | 2,997,472 EASY | 16,861.93 XUSDC | +1.8% |
| EASY/XXRP | $9,545 | $12,456 | 336,618 EASY | 4,371.63 XXRP | -5.7% |
| EASY/XPR | $6,019 | $46,832 | 1,197,902 EASY | 7,994,874.48 XPR | +0.2% |
| EASY/XUSDT | $3,168 | $74,830 | 3,002,397 EASY | 16,759.38 XUSDT | +1.9% |
| EASY/XBTC | $1,084 | $3,724 | 111,212 EASY | 0.02 XBTC | -1.7% |
| EASY/XXLM | $478.45 | $1,137 | 20,233 EASY | 3,983.33 XXLM | -0.4% |
| EASY/XDOGE | $414.16 | $495.35 | 20,017 EASY | 1,338.98 XDOGE | -1.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $17,194 XMD | 3,021,985 EASY | $75,588 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,862 XUSDC | 2,997,472 EASY | $74,786 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,886 XPYUSD | 3,199,602 EASY | $61,830 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,912 XPAX | 3,290,110 EASY | $63,579 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,811 XUSDT | 3,002,397 EASY | $74,830 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,152,468 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,993,135 | - | - |
| **Swap volume** | $126,135 | $360,898 | $1,222,186 |
| **Spot volume** | $220.42 | $904.62 | $19,944 |
| **Swap fees** | $781.86 | $1,972 | $6,515 |
| **DAU (avg)** | ≈81 | ≈74 | ≈77 |
| **Liquidity pools** | 11,407 | - | - |
| **Spot pairs** | 1,656 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **765.02 EASY** |
| Approx. USD | **≈$14.79** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
