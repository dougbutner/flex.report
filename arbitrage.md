# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-27 18:29 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.001148 | 0.944561 | 0.914855 | 0.993348 |
| **XUSDC** | 0.998853 | 1.000000 | 0.943478 | 0.913806 | 0.992209 |
| **XPYUSD** | 1.058693 | 1.059908 | 1.000000 | 0.968550 | 1.051650 |
| **XPAX** | 1.093070 | 1.094325 | 1.032471 | 1.000000 | 1.085799 |
| **XUSDT** | 1.006697 | 1.007852 | 0.950886 | 0.920981 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.11 | -5.54 | -8.51 | -0.67 |
| **XUSDC** | -0.11 | +0.00 | -5.65 | -8.62 | -0.78 |
| **XPYUSD** | +5.87 | +5.99 | +0.00 | -3.15 | +5.17 |
| **XPAX** | +9.31 | +9.43 | +3.25 | +0.00 | +8.58 |
| **XUSDT** | +0.67 | +0.79 | -4.91 | -7.90 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.094325** (+9.43% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.093070** (+9.31% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.085799** (+8.58% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.059908** (+5.99% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.058693** (+5.87% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.913806** (-8.62% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.914855** (-8.51% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.920981** (-7.90% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.943478** (-5.65% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.944561** (-5.54% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 50.7575 | $500 | $60 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 50.6993 | $16,987 | $3,682 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.7366 | $16,132 | $644 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.4815 | $15,005 | $140 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 51.0974 | $16,756 | $1,048 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0004 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0548 |
| XPAX | $1.0408 |
| XUSDT | $1.0000 |
