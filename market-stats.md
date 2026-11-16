# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-11-16 22:40 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,861** |
| **EASY price** | **$0.0171** (≈10.65 XPR) |
| **EASY price in XUSDC** | **0.017263 XUSDC** |
| **Total EASY pools TVL** | **$346,377** |
| **Total USD backing (stables)** | **$53,250** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **949.08 EASY** (≈$16.25) in the reflection pool |
| **7d volume** | **$81,020** |
| **30d volume** | **$347,658** |
| **Flexers (holders on contract)** | **6,072** |
| **Market cap (fully circulating)** | **$359,505** |
| **Share of Alcor Proton swap volume (24h)** | **≈35.11%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,861 | $12,683 | **35.1%** |
| 7d | $81,020 | $198,177 | **29.0%** |
| 30d | $347,658 | $802,508 | **30.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XPR | $2,478 | $9,904 | 180,451 EASY | 4,239,778.71 XPR | -6.9% |
| EASY/XUSDC | $1,899 | $67,912 | 3,196,933 EASY | 13,182.35 XUSDC | -1.7% |
| EASY/XUSDT | $805.77 | $67,910 | 3,210,347 EASY | 12,951.46 XUSDT | -2.4% |
| EASY/XXRP | $400.83 | $11,877 | 99,305 EASY | 11,033.07 XXRP | -1.6% |
| EASY/XPYUSD | $344.10 | $54,732 | 3,197,114 EASY | 13,178.98 XPYUSD | -1.7% |
| EASY/XPAX | $260.28 | $54,637 | 3,191,541 EASY | 13,336.63 XPAX | -1.3% |
| EASY/XBTC | $245.67 | $6,041 | 106,428 EASY | 0.07 XBTC | -1.3% |
| EASY/XXLM | $139.95 | $3,479 | 31,207 EASY | 22,311.15 XXLM | +1.1% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $479.04 XMD | 2,158,065 EASY | $37,424 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $13,182 XUSDC | 3,196,933 EASY | $67,912 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $13,158 XPYUSD | 3,197,114 EASY | $54,732 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,392 XPAX | 3,191,541 EASY | $54,637 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,951 XUSDT | 3,210,347 EASY | $67,910 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $833,565 | (snapshot) | (snapshot) |
| **Swap TVL** | $741,552 | - | - |
| **Swap volume** | $19,544 | $279,197 | $1,150,166 |
| **Spot volume** | $120.76 | $2,162 | $5,849 |
| **Swap fees** | $99.46 | $1,620 | $6,129 |
| **DAU (avg)** | ≈370 | ≈379 | ≈367 |
| **Liquidity pools** | 11,858 | - | - |
| **Spot pairs** | 1,681 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **949.08 EASY** |
| Approx. USD | **≈$16.25** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
