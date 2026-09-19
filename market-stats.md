# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-09-19 16:10 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$16,416** |
| **EASY price** | **$0.0180** (≈7.05 XPR) |
| **EASY price in XUSDC** | **0.018249 XUSDC** |
| **Total EASY pools TVL** | **$420,942** |
| **Total USD backing (stables)** | **$74,558** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **2,723.21 EASY** (≈$49.03) in the reflection pool |
| **7d volume** | **$146,103** |
| **30d volume** | **$601,159** |
| **Flexers (holders on contract)** | **977** |
| **Market cap (fully circulating)** | **$378,080** |
| **Share of Alcor Proton swap volume (24h)** | **≈36.2%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $16,416 | $28,928 | **36.2%** |
| 7d | $146,103 | $408,811 | **26.3%** |
| 30d | $601,159 | $1,311,007 | **31.4%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $6,103 | $71,522 | 3,134,850 EASY | 15,230.13 XMD | -0.1% |
| EASY/XXRP | $2,882 | $15,972 | 442,514 EASY | 6,155.03 XXRP | +1.0% |
| EASY/XUSDC | $2,577 | $70,720 | 3,109,466 EASY | 14,737.92 XUSDC | -0.1% |
| EASY/XUSDT | $1,176 | $70,849 | 3,125,299 EASY | 14,448.54 XUSDT | -0.5% |
| EASY/XPR | $959.60 | $21,491 | 211,823 EASY | 6,926,437.84 XPR | +0.7% |
| EASY/XXLM | $765.22 | $3,985 | 174,068 EASY | 4,540.21 XXLM | -0.7% |
| EASY/XPYUSD | $655.10 | $55,859 | 3,107,918 EASY | 14,763.29 XPYUSD | +1.0% |
| EASY/XSOL | $449.54 | $961.56 | 18,057 EASY | 5.74 XSOL | -0.3% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $15,083 XMD | 3,134,850 EASY | $71,522 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $14,738 XUSDC | 3,109,466 EASY | $70,720 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $14,896 XPYUSD | 3,107,918 EASY | $55,859 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,521 XPAX | 3,136,475 EASY | $56,372 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $14,582 XUSDT | 3,125,299 EASY | $70,849 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,180,829 | (snapshot) | (snapshot) |
| **Swap TVL** | $1,024,191 | - | - |
| **Swap volume** | $45,344 | $554,915 | $1,912,166 |
| **Spot volume** | $85.96 | $2,592 | $9,324 |
| **Swap fees** | $202.83 | $2,714 | $9,995 |
| **DAU (avg)** | ≈66 | ≈75 | ≈76 |
| **Liquidity pools** | 11,590 | - | - |
| **Spot pairs** | 1,669 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **2,723.21 EASY** |
| Approx. USD | **≈$49.03** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
