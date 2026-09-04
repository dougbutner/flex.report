# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-04 16:40 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$11,925** |
| **EASY price** | **$0.0190** (≈6.59 XPR) |
| **EASY price in XUSDC** | **0.018909 XUSDC** |
| **Total EASY pools TVL** | **$2,341,525** |
| **Total USD backing (stables)** | **$80,462** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **842.04 EASY** (≈$15.99) in the reflection pool |
| **7d volume** | **$120,194** |
| **30d volume** | **$551,112** |
| **Flexers (holders on contract)** | **956** |
| **Market cap (fully circulating)** | **$398,694** |
| **Share of Alcor Proton swap volume (24h)** | **≈23.95%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $11,925 | $37,863 | **23.9%** |
| 7d | $120,194 | $302,344 | **28.4%** |
| 30d | $551,112 | $998,853 | **35.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $3,189 | $74,709 | 3,081,533 EASY | 16,216.36 XMD | -0.5% |
| EASY/XUSDC | $2,592 | $73,693 | 3,054,575 EASY | 15,754.86 XUSDC | -0.5% |
| EASY/XPR | $2,386 | $39,898 | 501,566 EASY | 10,555,811.98 XPR | +0.0% |
| EASY/XXRP | $792.58 | $18,425 | 589,662 EASY | 5,172.04 XXRP | +1.1% |
| EASY/XUSDT | $791.52 | $73,698 | 3,055,499 EASY | 15,736.73 XUSDT | -0.4% |
| EASY/XPYUSD | $437.69 | $57,953 | 3,055,394 EASY | 15,738.77 XPYUSD | -0.5% |
| EASY/XBTC | $331.38 | $6,813 | 265,080 EASY | 0.02 XBTC | -0.1% |
| EASY/XDOGE | $328.68 | $1,469 | 34,852 EASY | 9,487.02 XDOGE | +1.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,275 XMD | 3,081,533 EASY | $74,709 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,755 XUSDC | 3,054,575 EASY | $73,693 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,873 XPYUSD | 3,055,394 EASY | $57,953 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,354 XPAX | 3,108,717 EASY | $58,965 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,743 XUSDT | 3,055,499 EASY | $73,698 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $3,124,997 | (snapshot) | (snapshot) |
| **Swap TVL** | $2,966,160 | - | - |
| **Swap volume** | $49,788 | $422,539 | $1,549,965 |
| **Spot volume** | $432.49 | $2,862 | $9,256 |
| **Swap fees** | $235.72 | $2,276 | $8,343 |
| **DAU (avg)** | ≈74 | ≈76 | ≈76 |
| **Liquidity pools** | 11,480 | - | - |
| **Spot pairs** | 1,664 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **842.04 EASY** |
| Approx. USD | **≈$15.99** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
