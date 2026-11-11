# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-11 19:56 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.001000 | 0.993594 | 1.001284 | 1.000128 |
| **XUSDC** | 0.999001 | 1.000000 | 0.992602 | 1.000284 | 0.999129 |
| **XPYUSD** | 1.006447 | 1.007453 | 1.000000 | 1.007740 | 1.006576 |
| **XPAX** | 0.998717 | 0.999716 | 0.992320 | 1.000000 | 0.998845 |
| **XUSDT** | 0.999872 | 1.000872 | 0.993467 | 1.001156 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.10 | -0.64 | +0.13 | +0.01 |
| **XUSDC** | -0.10 | +0.00 | -0.74 | +0.03 | -0.09 |
| **XPYUSD** | +0.64 | +0.75 | +0.00 | +0.77 | +0.66 |
| **XPAX** | -0.13 | -0.03 | -0.77 | +0.00 | -0.12 |
| **XUSDT** | -0.01 | +0.09 | -0.65 | +0.12 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XPAX**: **1.007740** (+0.77% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.007453** (+0.75% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.006576** (+0.66% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.006447** (+0.64% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.001284** (+0.13% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **0.992320** (-0.77% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.992602** (-0.74% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.993467** (-0.65% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.993594** (-0.64% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.998717** (-0.13% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 56.3675 | $503 | $49 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 56.3112 | $13,969 | $1,464 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.7309 | $13,864 | $11 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.2952 | $14,107 | $476 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.3603 | $13,944 | $809 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9968 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0075 |
| XPAX | $1.0071 |
| XUSDT | $1.0000 |
