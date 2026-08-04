# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-08-04 15:17 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$6,945** |
| **EASY price** | **$0.0168** (≈6.53 XPR) |
| **EASY price in XUSDC** | **0.016949 XUSDC** |
| **Total EASY pools TVL** | **$398,844** |
| **Total USD backing (stables)** | **$64,234** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **811.03 EASY** (≈$13.60) in the reflection pool |
| **7d volume** | **$78,173** |
| **30d volume** | **$380,995** |
| **Flexers (holders on contract)** | **906** |
| **Market cap (fully circulating)** | **$352,073** |
| **Share of Alcor Proton swap volume (24h)** | **≈41.41%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $6,945 | $9,827 | **41.4%** |
| 7d | $78,173 | $211,678 | **27.0%** |
| 30d | $380,995 | $927,990 | **29.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XMD | $1,670 | $66,623 | 3,225,862 EASY | 12,691.55 XMD | -0.1% |
| EASY/XUSDC | $1,559 | $66,804 | 3,226,479 EASY | 12,676.77 XUSDC | -0.1% |
| EASY/XPR | $808.09 | $23,324 | 513,219 EASY | 5,731,644.31 XPR | -0.2% |
| EASY/XMT | $746.02 | $3,049 | 19,962 EASY | 13,386.98 XMT | -0.1% |
| EASY/XXRP | $743.45 | $20,643 | 357,610 EASY | 13,854.50 XXRP | -0.1% |
| EASY/XUSDT | $436.66 | $66,695 | 3,235,656 EASY | 12,521.39 XUSDT | -0.4% |
| EASY/XSOL | $262.05 | - | 1,423 EASY | 8.84 XSOL | -0.1% |
| EASY/XPYUSD | $133.47 | $54,271 | 3,235,045 EASY | 12,531.68 XPYUSD | +0.5% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $12,499 XMD | 3,225,862 EASY | $66,623 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $12,677 XUSDC | 3,226,479 EASY | $66,804 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $12,659 XPYUSD | 3,235,045 EASY | $54,271 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $13,002 XPAX | 3,297,578 EASY | $68,321 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $12,407 XUSDT | 3,235,656 EASY | $66,695 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,088,888 | (snapshot) | (snapshot) |
| **Swap TVL** | $948,232 | - | - |
| **Swap volume** | $16,771 | $289,851 | $1,308,984 |
| **Spot volume** | $380.52 | $8,638 | $51,915 |
| **Swap fees** | $80.33 | $1,698 | $6,998 |
| **DAU (avg)** | ≈75 | ≈78 | ≈78 |
| **Liquidity pools** | 11,221 | - | - |
| **Spot pairs** | 1,620 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **811.03 EASY** |
| Approx. USD | **≈$13.60** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
