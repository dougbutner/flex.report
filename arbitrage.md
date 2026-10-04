# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-04 17:12 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999444 | 0.999389 | 0.971768 | 0.991879 |
| **XUSDC** | 1.000556 | 1.000000 | 0.999945 | 0.972308 | 0.992431 |
| **XPYUSD** | 1.000612 | 1.000055 | 1.000000 | 0.972362 | 0.992486 |
| **XPAX** | 1.029052 | 1.028480 | 1.028423 | 1.000000 | 1.020695 |
| **XUSDT** | 1.008187 | 1.007627 | 1.007571 | 0.979724 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.06 | -0.06 | -2.82 | -0.81 |
| **XUSDC** | +0.06 | +0.00 | -0.01 | -2.77 | -0.76 |
| **XPYUSD** | +0.06 | +0.01 | +0.00 | -2.76 | -0.75 |
| **XPAX** | +2.91 | +2.85 | +2.84 | +0.00 | +2.07 |
| **XUSDT** | +0.82 | +0.76 | +0.76 | -2.03 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.029052** (+2.91% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.028480** (+2.85% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.028423** (+2.84% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.020695** (+2.07% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.008187** (+0.82% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.971768** (-2.82% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.972308** (-2.77% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.972362** (-2.76% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.979724** (-2.03% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.991879** (-0.81% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.1195 | $15,621 | $1,437 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.1496 | $15,076 | $1,040 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.1526 | $15,105 | $183 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6918 | $14,733 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.5626 | $14,859 | $430 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0030 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0021 |
| XPAX | $1.0295 |
| XUSDT | $1.0000 |
