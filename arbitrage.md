# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-29 16:55 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000530 | 1.000160 | 0.973609 | 1.000302 |
| **XUSDC** | 0.999471 | 1.000000 | 0.999630 | 0.973094 | 0.999773 |
| **XPYUSD** | 0.999840 | 1.000370 | 1.000000 | 0.973454 | 1.000143 |
| **XPAX** | 1.027106 | 1.027650 | 1.027270 | 1.000000 | 1.027417 |
| **XUSDT** | 0.999698 | 1.000227 | 0.999857 | 0.973315 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.05 | +0.02 | -2.64 | +0.03 |
| **XUSDC** | -0.05 | +0.00 | -0.04 | -2.69 | -0.02 |
| **XPYUSD** | -0.02 | +0.04 | +0.00 | -2.65 | +0.01 |
| **XPAX** | +2.71 | +2.77 | +2.73 | +0.00 | +2.74 |
| **XUSDT** | -0.03 | +0.02 | -0.01 | -2.67 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.027650** (+2.77% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.027417** (+2.74% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.027270** (+2.73% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.027106** (+2.71% vs parity) via EASY
- Sell **XMD** → buy **XUSDC**: **1.000530** (+0.05% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.973094** (-2.69% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.973315** (-2.67% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.973454** (-2.65% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.973609** (-2.64% vs parity) via EASY
- Sell **XUSDC** → buy **XMD**: **0.999471** (-0.05% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.2684 | $15,889 | $2,114 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.2402 | $16,994 | $2,601 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.2599 | $15,686 | $245 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7123 | $15,337 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.2523 | $15,496 | $443 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9910 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0087 |
| XPAX | $1.0354 |
| XUSDT | $0.9962 |
