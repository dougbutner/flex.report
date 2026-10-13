# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-13 19:40 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999483 | 0.989857 | 0.985041 | 0.984440 |
| **XUSDC** | 1.000517 | 1.000000 | 0.990369 | 0.985551 | 0.984949 |
| **XPYUSD** | 1.010247 | 1.009724 | 1.000000 | 0.995134 | 0.994528 |
| **XPAX** | 1.015186 | 1.014661 | 1.004889 | 1.000000 | 0.999390 |
| **XUSDT** | 1.015806 | 1.015280 | 1.005503 | 1.000610 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -1.01 | -1.50 | -1.56 |
| **XUSDC** | +0.05 | +0.00 | -0.96 | -1.44 | -1.51 |
| **XPYUSD** | +1.02 | +0.97 | +0.00 | -0.49 | -0.55 |
| **XPAX** | +1.52 | +1.47 | +0.49 | +0.00 | -0.06 |
| **XUSDT** | +1.58 | +1.53 | +0.55 | +0.06 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.015806** (+1.58% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.015280** (+1.53% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.015186** (+1.52% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.014661** (+1.47% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.010247** (+1.02% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.984440** (-1.56% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.984949** (-1.51% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.985041** (-1.50% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.985551** (-1.44% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.989857** (-1.01% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.8848 | $14,899 | $1,826 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.9132 | $14,677 | $2,386 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.4472 | $14,345 | $365 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7183 | $14,448 | $83 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.7523 | $14,249 | $799 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9821 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9960 |
| XPAX | $1.0106 |
| XUSDT | $1.0000 |
