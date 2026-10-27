# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-27 18:29 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$7,667** |
| **EASY price** | **$0.0196** (≈10.61 XPR) |
| **EASY price in XUSDC** | **0.019724 XUSDC** |
| **Total EASY pools TVL** | **$382,406** |
| **Total USD backing (stables)** | **$65,944** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **977.40 EASY** (≈$19.16) in the reflection pool |
| **7d volume** | **$143,156** |
| **30d volume** | **$531,766** |
| **Flexers (holders on contract)** | **6,059** |
| **Market cap (fully circulating)** | **$411,675** |
| **Share of Alcor Proton swap volume (24h)** | **≈18.5%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $7,667 | $33,776 | **18.5%** |
| 7d | $143,156 | $251,530 | **36.3%** |
| 30d | $531,766 | $988,175 | **35.0%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $3,682 | $75,616 | 2,990,769 EASY | 16,986.56 XUSDC | -0.5% |
| EASY/XXRP | $1,313 | $17,272 | 350,686 EASY | 7,986.67 XXRP | -1.5% |
| EASY/XUSDT | $1,048 | $75,616 | 3,002,491 EASY | 16,756.01 XUSDT | -0.5% |
| EASY/XPYUSD | $644.20 | $60,361 | 3,079,084 EASY | 15,294.22 XPYUSD | +3.9% |
| EASY/XPR | $546.74 | $16,180 | 380,431 EASY | 4,721,309.49 XPR | +1.1% |
| EASY/XPAX | $140.24 | $61,368 | 3,130,433 EASY | 14,416.85 XPAX | +0.9% |
| EASY/XBTC | $84.36 | $6,636 | 176,867 EASY | 0.04 XBTC | -0.3% |
| EASY/XMD | $59.52 | $42,738 | 2,154,613 EASY | 499.60 XMD | -0.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $499.78 XMD | 2,154,613 EASY | $42,738 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,987 XUSDC | 2,990,769 EASY | $75,616 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,132 XPYUSD | 3,079,084 EASY | $60,361 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,005 XPAX | 3,130,433 EASY | $61,368 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,756 XUSDT | 3,002,491 EASY | $75,616 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $950,019 | (snapshot) | (snapshot) |
| **Swap TVL** | $847,575 | - | - |
| **Swap volume** | $41,443 | $394,685 | $1,519,941 |
| **Spot volume** | $14.09 | $2,235 | $10,839 |
| **Swap fees** | $234.58 | $1,809 | $7,919 |
| **DAU (avg)** | ≈381 | ≈386 | ≈403 |
| **Liquidity pools** | 11,818 | - | - |
| **Spot pairs** | 1,678 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **977.40 EASY** |
| Approx. USD | **≈$19.16** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
