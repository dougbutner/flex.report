# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-03 19:54 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000125 | 0.988723 | 0.982908 | 0.991327 |
| **XUSDC** | 0.999875 | 1.000000 | 0.988600 | 0.982785 | 0.991203 |
| **XPYUSD** | 1.011405 | 1.011531 | 1.000000 | 0.994118 | 1.002633 |
| **XPAX** | 1.017390 | 1.017517 | 1.005917 | 1.000000 | 1.008566 |
| **XUSDT** | 1.008749 | 1.008875 | 0.997374 | 0.991507 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.01 | -1.13 | -1.71 | -0.87 |
| **XUSDC** | -0.01 | +0.00 | -1.14 | -1.72 | -0.88 |
| **XPYUSD** | +1.14 | +1.15 | +0.00 | -0.59 | +0.26 |
| **XPAX** | +1.74 | +1.75 | +0.59 | +0.00 | +0.86 |
| **XUSDT** | +0.87 | +0.89 | -0.26 | -0.85 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.017517** (+1.75% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.017390** (+1.74% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.011531** (+1.15% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.011405** (+1.14% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.008875** (+0.89% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.982785** (-1.72% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.982908** (-1.71% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.988600** (-1.14% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.988723** (-1.13% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.991203** (-0.88% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.8532 | $521 | $223 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.8466 | $15,775 | $2,576 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.4560 | $15,475 | $294 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 53.7723 | $15,515 | $3 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.3156 | $15,520 | $1,298 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0005 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0020 |
| XPAX | $1.0136 |
| XUSDT | $1.0000 |
