# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-28 22:49 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000735 | 1.000765 | 0.973278 | 1.002227 |
| **XUSDC** | 0.999266 | 1.000000 | 1.000030 | 0.972563 | 1.001491 |
| **XPYUSD** | 0.999236 | 0.999970 | 1.000000 | 0.972534 | 1.001461 |
| **XPAX** | 1.027456 | 1.028211 | 1.028242 | 1.000000 | 1.029744 |
| **XUSDT** | 0.997778 | 0.998512 | 0.998542 | 0.971115 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | +0.08 | -2.67 | +0.22 |
| **XUSDC** | -0.07 | +0.00 | +0.00 | -2.74 | +0.15 |
| **XPYUSD** | -0.08 | -0.00 | +0.00 | -2.75 | +0.15 |
| **XPAX** | +2.75 | +2.82 | +2.82 | +0.00 | +2.97 |
| **XUSDT** | -0.22 | -0.15 | -0.15 | -2.89 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.029744** (+2.97% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.028242** (+2.82% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.028211** (+2.82% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.027456** (+2.75% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.002227** (+0.22% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.971115** (-2.89% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.972534** (-2.75% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.972563** (-2.74% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.973278** (-2.67% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.997778** (-0.22% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.2488 | $15,958 | $4,992 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.2097 | $17,041 | $5,409 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.2081 | $15,714 | $631 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7108 | $15,384 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.1305 | $15,629 | $1,812 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9947 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0087 |
| XPAX | $1.0386 |
| XUSDT | $1.0005 |
