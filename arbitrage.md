# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-08 19:05 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999585 | 0.999482 | 0.997310 | 0.989070 |
| **XUSDC** | 1.000416 | 1.000000 | 0.999897 | 0.997725 | 0.989481 |
| **XPYUSD** | 1.000518 | 1.000103 | 1.000000 | 0.997827 | 0.989582 |
| **XPAX** | 1.002697 | 1.002281 | 1.002178 | 1.000000 | 0.991737 |
| **XUSDT** | 1.011051 | 1.010631 | 1.010528 | 1.008332 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.04 | -0.05 | -0.27 | -1.09 |
| **XUSDC** | +0.04 | +0.00 | -0.01 | -0.23 | -1.05 |
| **XPYUSD** | +0.05 | +0.01 | +0.00 | -0.22 | -1.04 |
| **XPAX** | +0.27 | +0.23 | +0.22 | +0.00 | -0.83 |
| **XUSDT** | +1.11 | +1.06 | +1.05 | +0.83 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.011051** (+1.11% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.010631** (+1.06% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.010528** (+1.05% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.008332** (+0.83% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.002697** (+0.27% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.989070** (-1.09% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.989481** (-1.05% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.989582** (-1.04% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.991737** (-0.83% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.997310** (-0.27% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.5775 | $14,719 | $2,563 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.6006 | $14,326 | $3,325 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.6063 | $14,422 | $576 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7274 | $14,458 | $8 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.1917 | $14,028 | $1,084 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9936 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0070 |
| XPAX | $1.0116 |
| XUSDT | $1.0000 |
