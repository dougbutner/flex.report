# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-31 19:19 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$30,517** |
| **EASY price** | **$0.0189** (≈6.37 XPR) |
| **EASY price in XUSDC** | **0.019162 XUSDC** |
| **Total EASY pools TVL** | **$439,284** |
| **Total USD backing (stables)** | **$81,932** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **1,103.15 EASY** (≈$20.82) in the reflection pool |
| **7d volume** | **$152,066** |
| **30d volume** | **$520,165** |
| **Flexers (holders on contract)** | **954** |
| **Market cap (fully circulating)** | **$396,370** |
| **Share of Alcor Proton swap volume (24h)** | **≈30.68%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $30,517 | $68,939 | **30.7%** |
| 7d | $152,066 | $265,220 | **36.4%** |
| 30d | $520,165 | $906,709 | **36.5%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $7,929 | $73,416 | 3,034,459 EASY | 16,141.52 XUSDC | -0.1% |
| EASY/XPR | $6,753 | $48,020 | 1,142,880 EASY | 8,924,038.82 XPR | +0.8% |
| EASY/XMD | $6,579 | $74,162 | 3,060,802 EASY | 16,613.10 XMD | -0.2% |
| EASY/XXRP | $2,266 | $14,821 | 351,815 EASY | 6,000.23 XXRP | +2.0% |
| EASY/XUSDT | $1,798 | $73,399 | 3,034,192 EASY | 16,143.06 XUSDT | -0.0% |
| EASY/XHBAR | $1,351 | $659.42 | 4,365 EASY | 7,925.07 XHBAR | +1.5% |
| EASY/XBTC | $1,289 | $6,736 | 195,415 EASY | 0.04 XBTC | +0.8% |
| EASY/XUSDC | $709.30 | $4,024 | 146,572 EASY | 1,257.39 XUSDC | +0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $16,390 XMD | 3,060,802 EASY | $74,162 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $16,142 XUSDC | 3,034,459 EASY | $73,416 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $16,058 XPYUSD | 3,047,556 EASY | $57,522 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,417 XPAX | 3,108,629 EASY | $58,675 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,130 XUSDT | 3,034,192 EASY | $73,399 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,228,312 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,056,791 | - | - |
| **Swap volume** | $99,457 | $417,285 | $1,426,874 |
| **Spot volume** | $449.96 | $1,711 | $8,699 |
| **Swap fees** | $511.10 | $2,294 | $7,612 |
| **DAU (avg)** | ≈85 | ≈77 | ≈77 |
| **Liquidity pools** | 11,466 | - | - |
| **Spot pairs** | 1,658 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,103.15 EASY** |
| Approx. USD | **≈$20.82** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
