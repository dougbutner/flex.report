# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-14 17:41 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000530 | 0.995924 | 0.993196 | 0.994767 |
| **XUSDC** | 0.999471 | 1.000000 | 0.995396 | 0.992670 | 0.994241 |
| **XPYUSD** | 1.004093 | 1.004625 | 1.000000 | 0.997261 | 0.998839 |
| **XPAX** | 1.006851 | 1.007384 | 1.002746 | 1.000000 | 1.001582 |
| **XUSDT** | 1.005260 | 1.005793 | 1.001163 | 0.998421 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.05 | -0.41 | -0.68 | -0.52 |
| **XUSDC** | -0.05 | +0.00 | -0.46 | -0.73 | -0.58 |
| **XPYUSD** | +0.41 | +0.46 | +0.00 | -0.27 | -0.12 |
| **XPAX** | +0.69 | +0.74 | +0.27 | +0.00 | +0.16 |
| **XUSDT** | +0.53 | +0.58 | +0.12 | -0.16 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.007384** (+0.74% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.006851** (+0.69% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.005793** (+0.58% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.005260** (+0.53% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.004625** (+0.46% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.992670** (-0.73% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.993196** (-0.68% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.994241** (-0.58% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.994767** (-0.52% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.995396** (-0.46% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.3389 | $14,726 | $1,176 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.3096 | $14,473 | $1,737 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.5654 | $14,462 | $96 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7180 | $14,461 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.6300 | $14,310 | $686 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9860 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0083 |
| XPAX | $1.0115 |
| XUSDT | $1.0000 |
