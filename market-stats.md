# Market Stats

![Market Stats](assets/heroes/market-stats.png)

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-10-26 18:57 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$11,442** |
| **EASY price** | **$0.0198** (≈10.72 XPR) |
| **EASY price in XUSDC** | **0.019827 XUSDC** |
| **Total EASY pools TVL** | **$386,718** |
| **Total USD backing (stables)** | **$65,498** (XMD + XUSDC + XPYUSD + XPAX + XUSDT sides) |
| **Pending holder rewards** | **971.31 EASY** (≈$19.22) in the reflection pool |
| **7d volume** | **$142,302** |
| **30d volume** | **$535,330** |
| **Flexers (holders on contract)** | **6,056** |
| **Market cap (fully circulating)** | **$415,638** |
| **Share of Alcor Proton swap volume (24h)** | **≈29.16%** |

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $11,442 | $27,794 | **29.2%** |
| 7d | $142,302 | $230,525 | **38.2%** |
| 30d | $535,330 | $984,221 | **35.2%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | EASY in pool | Other side | 24h Δ |
| --- | ---: | ---: | ---: | ---: | ---: |
| EASY/XUSDC | $4,109 | $76,181 | 2,983,004 EASY | 17,140.00 XUSDC | -1.7% |
| EASY/XPR | $2,031 | $16,239 | 357,590 EASY | 4,964,000.02 XPR | +1.4% |
| EASY/XUSDT | $1,975 | $76,181 | 2,995,064 EASY | 16,901.64 XUSDT | +4.2% |
| EASY/XXRP | $1,720 | $17,200 | 322,638 EASY | 8,411.07 XXRP | -1.9% |
| EASY/XMD | $654.56 | $43,145 | 2,154,543 EASY | 500.96 XMD | -2.3% |
| EASY/XBTC | $293.62 | $6,687 | 173,377 EASY | 0.04 XBTC | -1.4% |
| EASY/METAL | $212.24 | $5,527 | 30,215 EASY | 48,409.77 METAL | -2.7% |
| EASY/XXLM | $105.77 | $620.83 | 10,132 EASY | 2,491.17 XXLM | -2.2% |

### Stable backing (deepest pool each)

| Pool | Stable side | EASY in pool | Pool TVL |
| --- | ---: | ---: | ---: |
| [EASY/XMD](https://alcor.exchange/v/xpr/analytics/pools/4067) | $501.17 XMD | 2,154,543 EASY | $43,145 |
| [EASY/XUSDC](https://alcor.exchange/v/xpr/analytics/pools/4065) | $17,140 XUSDC | 2,983,004 EASY | $76,181 |
| [EASY/XPYUSD](https://alcor.exchange/v/xpr/analytics/pools/4068) | $15,644 XPYUSD | 3,138,446 EASY | $62,117 |
| [EASY/XPAX](https://alcor.exchange/v/xpr/analytics/pools/4070) | $14,740 XPAX | 3,144,630 EASY | $62,239 |
| [EASY/XUSDT](https://alcor.exchange/v/xpr/analytics/pools/4066) | $16,902 XUSDT | 2,995,064 EASY | $76,181 |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $962,405 | (snapshot) | (snapshot) |
| **Swap TVL** | $856,458 | - | - |
| **Swap volume** | $39,236 | $372,827 | $1,519,551 |
| **Spot volume** | $30.18 | $2,314 | $10,887 |
| **Swap fees** | $208.29 | $1,682 | $7,905 |
| **DAU (avg)** | ≈396 | ≈385 | ≈404 |
| **Liquidity pools** | 11,812 | - | - |
| **Spot pairs** | 1,678 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **971.31 EASY** |
| Approx. USD | **≈$19.22** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track real bags over time on [Success Stories](our-story/success-stories.md).
