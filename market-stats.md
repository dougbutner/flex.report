# Market Stats

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-07-25 09:19 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$15,503** |
| **EASY price** | **$0.0162** (~6.48 XPR) |
| **EASY price in XUSDC** | **0.016526 XUSDC** |
| **Total USD backing** | **$58,821** (XMD + XUSDC + XPYUSD + XPAX + XUSDT in EASY pools) |
| **Pending holder rewards** | **954.53 EASY** (~$15.50) in the reflection pool |
| **7d volume** | **$114,802** |
| **30d volume** | **$393,904** |
| **Flexers (holders on contract)** | **888** |
| **Market cap (fully circulating)** | **$340,940** |
| **Share of Alcor Proton swap volume (24h)** | **~33.53%** |

USDC-style rewards dashboards inspired this layout: **liquidity**, **pending rewards**, and **volume that feeds holders**.

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $15,503 | $30,739 | **33.5%** |
| 7d | $114,802 | $175,331 | **39.6%** |
| 30d | $393,904 | $972,530 | **28.8%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | 24h Δ |
| --- | ---: | ---: | ---: |
| EASY/XMD | $6,581 | $64,998 | -0.3% |
| EASY/XUSDC | $2,798 | $65,039 | -0.4% |
| EASY/XXRP | $2,089 | $13,875 | +0.7% |
| EASY/XUSDT | $1,270 | $64,814 | -0.3% |
| EASY/XPR | $1,012 | $23,447 | -0.2% |
| EASY/METAL | $547.72 | $8,858 | -0.2% |
| EASY/SNIPS | $494.73 | $5,256 | +0.5% |
| EASY/XSOL | $240.41 | - | +0.8% |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,000,924 | (snapshot) | (snapshot) |
| **Swap TVL** | $882,139 | - | - |
| **Swap volume** | $46,241 | $290,132 | $1,366,434 |
| **Spot volume** | $852.77 | $15,465 | $40,923 |
| **Swap fees** | $228.32 | $1,461 | $7,523 |
| **DAU (avg)** | ~78 | ~81 | ~77 |
| **Liquidity pools** | 11,124 | - | - |
| **Spot pairs** | 1,601 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **954.53 EASY** |
| Approx. USD | **~$15.50** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track a real bag over time on [Success in Community](our-story/success-in-community.md) (`thelake`).

## Supply

| | |
| --- | --- |
| Max / issued | 21,000,000 EASY |
| Circulating in pools + wallets | 21,000,000 (100% minted day one into liquidity) |

---

*Numbers drift every block. Say **update stats** in Cursor to refresh this page from Alcor + chain.*
