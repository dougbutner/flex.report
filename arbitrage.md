# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-12 20:34 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.001093 | 0.975116 | 1.001022 | 0.997635 |
| **XUSDC** | 0.998908 | 1.000000 | 0.974052 | 0.999929 | 0.996545 |
| **XPYUSD** | 1.025519 | 1.026640 | 1.000000 | 1.026567 | 1.023093 |
| **XPAX** | 0.998979 | 1.000071 | 0.974121 | 1.000000 | 0.996616 |
| **XUSDT** | 1.002371 | 1.003467 | 0.977428 | 1.003395 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.11 | -2.49 | +0.10 | -0.24 |
| **XUSDC** | -0.11 | +0.00 | -2.59 | -0.01 | -0.35 |
| **XPYUSD** | +2.55 | +2.66 | +0.00 | +2.66 | +2.31 |
| **XPAX** | -0.10 | +0.01 | -2.59 | +0.00 | -0.34 |
| **XUSDT** | +0.24 | +0.35 | -2.26 | +0.34 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XUSDC**: **1.026640** (+2.66% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **1.026567** (+2.66% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.025519** (+2.55% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.023093** (+2.31% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.003467** (+0.35% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.974052** (-2.59% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **0.974121** (-2.59% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.975116** (-2.49% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.977428** (-2.26% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.996545** (-0.35% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.0422 | $510 | $94 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.9821 | $14,642 | $3,410 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.4468 | $14,239 | $101 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.9860 | $14,775 | $923 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.1727 | $14,543 | $1,239 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0000 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0243 |
| XPAX | $1.0071 |
| XUSDT | $1.0000 |
