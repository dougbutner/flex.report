# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-25 13:42 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000782 | 0.982839 | 0.973462 | 1.003132 |
| **XUSDC** | 0.999219 | 1.000000 | 0.982071 | 0.972702 | 1.002349 |
| **XPYUSD** | 1.017461 | 1.018256 | 1.000000 | 0.990459 | 1.020648 |
| **XPAX** | 1.027262 | 1.028064 | 1.009632 | 1.000000 | 1.030479 |
| **XUSDT** | 0.996878 | 0.997657 | 0.979770 | 0.970423 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.08 | -1.72 | -2.65 | +0.31 |
| **XUSDC** | -0.08 | +0.00 | -1.79 | -2.73 | +0.23 |
| **XPYUSD** | +1.75 | +1.83 | +0.00 | -0.95 | +2.06 |
| **XPAX** | +2.73 | +2.81 | +0.96 | +0.00 | +3.05 |
| **XUSDT** | -0.31 | -0.23 | -2.02 | -2.96 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.030479** (+3.05% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.028064** (+2.81% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.027262** (+2.73% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.020648** (+2.06% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.018256** (+1.83% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.970423** (-2.96% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.972702** (-2.73% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.973462** (-2.65% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.979770** (-2.02% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.982071** (-1.79% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.2619 | $15,865 | $2,796 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.2203 | $16,878 | $2,494 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.1919 | $15,239 | $145 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7139 | $16,002 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.0956 | $15,434 | $1,264 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9894 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0124 |
| XPAX | $1.0384 |
| XUSDT | $0.9869 |
