# Market Stats

Live pulse of EASY on XPR Alcor: liquidity, volume, and pending holder rewards.

*Last updated: 2026-07-25 21:32 UTC · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **$4,124** |
| **EASY price** | **$0.0163** (~6.46 XPR) |
| **EASY price in XUSDC** | **0.016638 XUSDC** |
| **Total USD backing** | **$59,376** (XMD + XUSDC + XPYUSD + XPAX + XUSDT in EASY pools) |
| **Pending holder rewards** | **1,322.43 EASY** (~$21.52) in the reflection pool |
| **7d volume** | **$108,623** |
| **30d volume** | **$388,939** |
| **Flexers (holders on contract)** | **892** |
| **Market cap (fully circulating)** | **$341,699** |
| **Share of Alcor Proton swap volume (24h)** | **~16.6%** |

USDC-style rewards dashboards inspired this layout: **liquidity**, **pending rewards**, and **volume that feeds holders**.

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | $4,124 | $20,715 | **16.6%** |
| 7d | $108,623 | $161,423 | **40.2%** |
| 30d | $388,939 | $948,630 | **29.1%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | 24h Δ |
| --- | ---: | ---: | ---: |
| EASY/XMD | $1,030 | $65,033 | +0.4% |
| EASY/XUSDC | $977.59 | $65,154 | +0.3% |
| EASY/XPR | $873.29 | $23,540 | +0.1% |
| EASY/XSOL | $234.85 | - | +1.6% |
| EASY/METAL | $208.18 | $8,917 | +0.1% |
| EASY/XUSDT | $197.05 | $64,923 | +0.2% |
| EASY/XXRP | $179.10 | $13,921 | -0.0% |
| EASY/XHBAR | $109.28 | $568.98 | +0.3% |

Trade: [alcor.exchange/v/xpr/swap](https://alcor.exchange/v/xpr/swap) · Analytics: [EASY token](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | $1,012,793 | (snapshot) | (snapshot) |
| **Swap TVL** | $891,085 | - | - |
| **Swap volume** | $24,839 | $270,046 | $1,337,569 |
| **Spot volume** | $2,697 | $16,674 | $42,738 |
| **Swap fees** | $131.23 | $1,353 | $7,300 |
| **DAU (avg)** | ~78 | ~80 | ~77 |
| **Liquidity pools** | 11,142 | - | - |
| **Spot pairs** | 1,602 | - | - |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **1,322.43 EASY** |
| Approx. USD | **~$21.52** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track a real bag over time on [Success in Community](our-story/success-in-community.md) (`thelake`).
