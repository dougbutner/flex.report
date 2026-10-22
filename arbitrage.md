# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-22 17:45 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999846 | 0.974264 | 0.977404 | 0.973772 |
| **XUSDC** | 1.000154 | 1.000000 | 0.974415 | 0.977555 | 0.973922 |
| **XPYUSD** | 1.026415 | 1.026257 | 1.000000 | 1.003223 | 0.999495 |
| **XPAX** | 1.023118 | 1.022960 | 0.996787 | 1.000000 | 0.996284 |
| **XUSDT** | 1.026934 | 1.026776 | 1.000505 | 1.003730 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -2.57 | -2.26 | -2.62 |
| **XUSDC** | +0.02 | +0.00 | -2.56 | -2.24 | -2.61 |
| **XPYUSD** | +2.64 | +2.63 | +0.00 | +0.32 | -0.05 |
| **XPAX** | +2.31 | +2.30 | -0.32 | +0.00 | -0.37 |
| **XUSDT** | +2.69 | +2.68 | +0.05 | +0.37 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.026934** (+2.69% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.026776** (+2.68% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.026415** (+2.64% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.026257** (+2.63% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.023118** (+2.31% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.973772** (-2.62% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.973922** (-2.61% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.974264** (-2.57% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.974415** (-2.56% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.977404** (-2.26% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.1344 | $15,051 | $2,796 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.1429 | $14,562 | $3,263 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.5908 | $14,280 | $18 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.4090 | $14,436 | $3 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.6194 | $13,817 | $252 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0005 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0325 |
| XPAX | $1.0348 |
| XUSDT | $1.0000 |
