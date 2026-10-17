# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-17 16:03 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000124 | 0.999113 | 0.999142 | 0.996960 |
| **XUSDC** | 0.999876 | 1.000000 | 0.998989 | 0.999019 | 0.996836 |
| **XPYUSD** | 1.000888 | 1.001012 | 1.000000 | 1.000030 | 0.997845 |
| **XPAX** | 1.000858 | 1.000982 | 0.999970 | 1.000000 | 0.997816 |
| **XUSDT** | 1.003049 | 1.003174 | 1.002160 | 1.002189 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.01 | -0.09 | -0.09 | -0.30 |
| **XUSDC** | -0.01 | +0.00 | -0.10 | -0.10 | -0.32 |
| **XPYUSD** | +0.09 | +0.10 | +0.00 | +0.00 | -0.22 |
| **XPAX** | +0.09 | +0.10 | -0.00 | +0.00 | -0.22 |
| **XUSDT** | +0.30 | +0.32 | +0.22 | +0.22 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XUSDC**: **1.003174** (+0.32% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.003049** (+0.30% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.002189** (+0.22% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.002160** (+0.22% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.001012** (+0.10% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.996836** (-0.32% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.996960** (-0.30% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.997816** (-0.22% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.997845** (-0.22% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.998989** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 57.3225 | $14,052 | $31,679 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 57.3154 | $13,476 | $44,511 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 57.3734 | $13,496 | $1,806 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 57.3717 | $13,377 | $3,103 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 57.4973 | $13,388 | $8,462 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0079 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0036 |
| XPAX | $0.9924 |
| XUSDT | $1.0000 |
