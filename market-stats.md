# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-30 18:20 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$12,144** |
| **EASY price** | **$0.0187** (≈10.21 XPR) |
| **EASY price in XUSDC** | **0.018761 XUSDC** |
| **Total EASY pools TVL** | **$368,467** |
| **Total USD backing (stables)** | **$62,620** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **2,056.37 EASY** (≈$38.53) in the reflection pool |
| **7d volume** | **$131,326** |
| **30d volume** | **$537,544** |
| **Flexers (holders on contract)** | **6,060** |
| **Market cap (fully circulating)** | **$393,506** |
| **Share of Alcor Proton swap volume (24h)** | **≈25.99%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $12,144 | $34,581 | **26.0%** |
| 7d | $131,326 | $223,014 | **37.1%** |
| 30d | $537,544 | $971,149 | **35.6%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $5,016 | $72,991 | 3,066,651 EASY | 15,526.87 XUSDC | -2.2% |
| EASY/XXRP | $2,136 | $19,417 | 384,104 EASY | 9,834.27 XXRP | +1.7% |
| EASY/XUSDT | $1,492 | $72,991 | 3,068,458 EASY | 15,492.70 XUSDT | -2.1% |
| EASY/XPR | $1,300 | $13,952 | 387,266 EASY | 3,649,547.99 XPR | +0.1% |
| EASY/XBTC | $924.29 | $6,406 | 207,186 EASY | 0.03 XBTC | +0.6% |
| EASY/XDOGE | $275.69 | $1,325 | 463 EASY | 17,521.91 XDOGE | +3.0% |
| EASY/USDT | $189.16 | $0.00 | 304,210 EASY | 0.00 USDT | -0.1% |
| EASY/XPYUSD | $184.68 | $57,808 | 3,084,986 EASY | 15,184.53 XPYUSD | -0.7% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $529.37 XMD | 2,157,440 EASY | $40,956 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $15,527 XUSDC | 3,066,651 EASY | $72,991 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,331 XPYUSD | 3,084,986 EASY | $57,808 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $15,466 XPAX | 3,089,660 EASY | $57,895 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $15,493 XUSDT | 3,068,458 EASY | $72,991 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $935,163 | (snapshot) | (snapshot) |
| **Swap TVL** | $834,397 | - | - |
| **Swap volume** | $46,726 | $354,340 | $1,508,694 |
| **Spot volume** | $363.82 | $777.75 | $8,743 |
| **Swap fees** | $303.31 | $1,827 | $7,844 |
| **DAU (avg)** | ≈345 | ≈375 | ≈397 |
| **Liquidity pools** | 11,826 | - | - |
| **Spot pairs** | 1,678 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **2,056.37 EASY** |
| Approx. USD | **≈$38.53** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
