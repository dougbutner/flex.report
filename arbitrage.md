# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-20 16:38 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999319 | 0.994070 | 0.980367 | 0.996349 |
| **XUSDC** | 1.000681 | 1.000000 | 0.994747 | 0.981035 | 0.997028 |
| **XPYUSD** | 1.005965 | 1.005281 | 1.000000 | 0.986216 | 1.002293 |
| **XPAX** | 1.020026 | 1.019332 | 1.013977 | 1.000000 | 1.016302 |
| **XUSDT** | 1.003664 | 1.002981 | 0.997712 | 0.983959 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.07 | -0.59 | -1.96 | -0.37 |
| **XUSDC** | +0.07 | +0.00 | -0.53 | -1.90 | -0.30 |
| **XPYUSD** | +0.60 | +0.53 | +0.00 | -1.38 | +0.23 |
| **XPAX** | +2.00 | +1.93 | +1.40 | +0.00 | +1.63 |
| **XUSDT** | +0.37 | +0.30 | -0.23 | -1.60 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.020026** (+2.00% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.019332** (+1.93% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.016302** (+1.63% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.013977** (+1.40% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.005965** (+0.60% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.980367** (-1.96% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.981035** (-1.90% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.983959** (-1.60% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.986216** (-1.38% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.994070** (-0.59% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.6143 | $14,963 | $9,695 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.6515 | $14,812 | $5,370 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.9401 | $14,583 | $849 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7080 | $14,210 | $4 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.8144 | $14,523 | $1,980 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9772 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9946 |
| XPAX | $0.9936 |
| XUSDT | $0.9861 |
