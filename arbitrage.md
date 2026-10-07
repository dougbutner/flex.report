# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-07 19:09 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999152 | 1.000141 | 0.979460 | 0.986108 |
| **XUSDC** | 1.000849 | 1.000000 | 1.000990 | 0.980291 | 0.986945 |
| **XPYUSD** | 0.999859 | 0.999011 | 1.000000 | 0.979321 | 0.985969 |
| **XPAX** | 1.020971 | 1.020105 | 1.021115 | 1.000000 | 1.006788 |
| **XUSDT** | 1.014088 | 1.013228 | 1.014231 | 0.993258 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.08 | +0.01 | -2.05 | -1.39 |
| **XUSDC** | +0.08 | +0.00 | +0.10 | -1.97 | -1.31 |
| **XPYUSD** | -0.01 | -0.10 | +0.00 | -2.07 | -1.40 |
| **XPAX** | +2.10 | +2.01 | +2.11 | +0.00 | +0.68 |
| **XUSDT** | +1.41 | +1.32 | +1.42 | -0.67 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XPYUSD**: **1.021115** (+2.11% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.020971** (+2.10% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.020105** (+2.01% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.014231** (+1.42% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.014088** (+1.41% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.979321** (-2.07% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.979460** (-2.05% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.980291** (-1.97% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.985969** (-1.40% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.986108** (-1.39% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.5515 | $15,165 | $4,473 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.5978 | $14,841 | $8,911 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.5438 | $14,890 | $166 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6955 | $14,717 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.3200 | $14,468 | $8,255 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9882 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0014 |
| XPAX | $1.0286 |
| XUSDT | $1.0000 |
