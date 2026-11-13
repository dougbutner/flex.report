# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-13 20:10 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000709 | 0.981922 | 1.000237 | 0.991757 |
| **XUSDC** | 0.999291 | 1.000000 | 0.981226 | 0.999528 | 0.991055 |
| **XPYUSD** | 1.018411 | 1.019133 | 1.000000 | 1.018652 | 1.010017 |
| **XPAX** | 0.999763 | 1.000472 | 0.981689 | 1.000000 | 0.991523 |
| **XUSDT** | 1.008311 | 1.009026 | 0.990083 | 1.008550 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | -1.81 | +0.02 | -0.82 |
| **XUSDC** | -0.07 | +0.00 | -1.88 | -0.05 | -0.89 |
| **XPYUSD** | +1.84 | +1.91 | +0.00 | +1.87 | +1.00 |
| **XPAX** | -0.02 | +0.05 | -1.83 | +0.00 | -0.85 |
| **XUSDT** | +0.83 | +0.90 | -0.99 | +0.85 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XUSDC**: **1.019133** (+1.91% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **1.018652** (+1.87% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.018411** (+1.84% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.010017** (+1.00% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.009026** (+0.90% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.981226** (-1.88% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **0.981689** (-1.83% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.981922** (-1.81% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.990083** (-0.99% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.991055** (-0.89% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.8906 | $497 | $301 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.8517 | $14,709 | $4,131 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.9012 | $14,412 | $140 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.8776 | $14,771 | $960 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.3468 | $14,454 | $1,743 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9731 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0169 |
| XPAX | $1.0030 |
| XUSDT | $1.0000 |
