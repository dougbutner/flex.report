# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-26 16:49 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,809** |
| **EASY price** | **$0.0187** (≈7.49 XPR) |
| **EASY price in XUSDC** | **0.018693 XUSDC** |
| **Total EASY pools TVL** | **$460,298** |
| **Total USD backing (stables)** | **$77,756** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **786.30 EASY** (≈$14.71) in the reflection pool |
| **7d volume** | **$115,001** |
| **30d volume** | **$489,372** |
| **Flexers (holders on contract)** | **986** |
| **Market cap (fully circulating)** | **$392,841** |
| **Share of Alcor Proton swap volume (24h)** | **≈27.91%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,809 | $17,589 | **27.9%** |
| 7d | $115,001 | $423,776 | **21.3%** |
| 30d | $489,372 | $1,488,790 | **24.7%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $2,015 | $73,794 | 3,096,623 EASY | 15,934.07 XMD | -0.2% |
| EASY/XXRP | $1,254 | $20,171 | 461,278 EASY | 7,446.19 XXRP | +0.8% |
| EASY/XUSDC | $1,096 | $72,895 | 3,072,259 EASY | 15,423.35 XUSDC | -0.3% |
| EASY/METAL | $738.46 | $3,301 | 91,865 EASY | 12,103.00 METAL | -1.1% |
| EASY/XPR | $641.75 | $41,796 | 380,239 EASY | 13,893,839.93 XPR | +0.0% |
| EASY/XXLM | $365.28 | $1,808 | 90,850 EASY | 501.88 XXLM | -0.2% |
| EASY/XUSDT | $353.97 | $72,765 | 3,066,434 EASY | 15,531.22 XUSDT | -0.2% |
| EASY/VIBRR | $165.34 | $1,815 | 84,615 EASY | 1,106,608.68 VIBRR | -1.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,866 XMD | 3,096,623 EASY | $73,794 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,423 XUSDC | 3,072,259 EASY | $72,895 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,138 XPYUSD | 3,111,612 EASY | $58,208 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,933 XPAX | 3,136,061 EASY | $73,598 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,402 XUSDT | 3,066,434 EASY | $72,765 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,269,336 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,109,843 | - | - |
| **Swap volume** | $24,398 | $538,777 | $1,978,162 |
| **Spot volume** | $163.35 | $3,045 | $11,449 |
| **Swap fees** | $113.01 | $2,954 | $10,289 |
| **DAU (avg)** | ≈429 | ≈417 | ≈421 |
| **Liquidity pools** | 11,632 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **786.30 EASY** |
| Approx. USD | **≈$14.71** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
