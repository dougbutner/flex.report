# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-20 20:51 UTC** · Primary path: deepest **EASY**↔stable pools*

## Cross-rate heatmap (+/- percent)

![Cross-rate heatmap (+/- percent vs parity)](assets/arbitrage-heatmap.png)

## How to read

![Stablecoin arb path](assets/diagrams/arbitrage-path.png)

- Rows = **sell** this coin. Columns = **buy** that coin.
- Cell = how many **buy** tokens you get per **1.0 sell** token (implied), routing **sell → EASY → buy**.
- Heatmap / percent table = distance from 1.0000 (parity) as **+/- percent** (green when you receive more than 1.0 of a same-peg asset after fees/slippage). Always simulate on [Alcor Swap](https://alcor.exchange/v/xpr/swap) before sizing.

Fees, hop slippage, and pool depth can erase small edges. EASY transfer tax (2%) applies when EASY moves to non-exempt accounts. Prefer routing that stays inside `swap.alcor` memos when possible.

## Implied rates via EASY (amount of Buy per 1 Sell)

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | 1.000000 | 1.000719 | 1.000802 | 1.011929 | 0.986883 |
| **XUSDC** | 0.999282 | 1.000000 | 1.000083 | 1.011202 | 0.986174 |
| **XPYUSD** | 0.999199 | 0.999917 | 1.000000 | 1.011118 | 0.986092 |
| **XPAX** | 0.988212 | 0.988922 | 0.989004 | 1.000000 | 0.975250 |
| **XUSDT** | 1.013291 | 1.014019 | 1.014104 | 1.025379 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | +0.08 | +1.19 | -1.31 |
| **XUSDC** | -0.07 | +0.00 | +0.01 | +1.12 | -1.38 |
| **XPYUSD** | -0.08 | -0.01 | +0.00 | +1.11 | -1.39 |
| **XPAX** | -1.18 | -1.11 | -1.10 | +0.00 | -2.48 |
| **XUSDT** | +1.33 | +1.40 | +1.41 | +2.54 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPAX**: **1.025379** (+2.54% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.014104** (+1.41% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.014019** (+1.40% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.013291** (+1.33% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.011929** (+1.19% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.975250** (-2.48% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.986092** (-1.39% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.986174** (-1.38% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.986883** (-1.31% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.988212** (-1.18% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 60.0174 | $504 | $589 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.9743 | $12,232 | $6,391 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.9693 | $12,219 | $418 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 59.3099 | $12,537 | $258 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.8151 | $11,855 | $1,712 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9802 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9988 |
| XPAX | $0.9978 |
| XUSDT | $1.0000 |
