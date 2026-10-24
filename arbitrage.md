# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-24 16:23 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000159 | 0.972750 | 0.982057 | 0.995838 |
| **XUSDC** | 0.999841 | 1.000000 | 0.972595 | 0.981901 | 0.995680 |
| **XPYUSD** | 1.028014 | 1.028177 | 1.000000 | 1.009569 | 1.023735 |
| **XPAX** | 1.018270 | 1.018432 | 0.990522 | 1.000000 | 1.014032 |
| **XUSDT** | 1.004180 | 1.004339 | 0.976815 | 0.986162 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.02 | -2.73 | -1.79 | -0.42 |
| **XUSDC** | -0.02 | +0.00 | -2.74 | -1.81 | -0.43 |
| **XPYUSD** | +2.80 | +2.82 | +0.00 | +0.96 | +2.37 |
| **XPAX** | +1.83 | +1.84 | -0.95 | +0.00 | +1.40 |
| **XUSDT** | +0.42 | +0.43 | -2.32 | -1.38 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XUSDC**: **1.028177** (+2.82% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.028014** (+2.80% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.023735** (+2.37% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.018432** (+1.84% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.018270** (+1.83% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.972595** (-2.74% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.972750** (-2.73% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.976815** (-2.32% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.981901** (-1.81% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.982057** (-1.79% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.4119 | $14,909 | $3,167 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.4031 | $14,432 | $8,262 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.9642 | $14,051 | $112 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.4243 | $14,332 | $11 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.6435 | $14,305 | $1,976 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0004 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0296 |
| XPAX | $1.0278 |
| XUSDT | $1.0000 |
