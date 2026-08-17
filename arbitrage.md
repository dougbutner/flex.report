# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-17 13:33 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999477 | 0.989052 | 0.977991 | 0.996443 |
| **XUSDC** | 1.000523 | 1.000000 | 0.989569 | 0.978503 | 0.996964 |
| **XPYUSD** | 1.011069 | 1.010541 | 1.000000 | 0.988817 | 1.007473 |
| **XPAX** | 1.022504 | 1.021970 | 1.011310 | 1.000000 | 1.018867 |
| **XUSDT** | 1.003569 | 1.003045 | 0.992583 | 0.981482 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -1.09 | -2.20 | -0.36 |
| **XUSDC** | +0.05 | +0.00 | -1.04 | -2.15 | -0.30 |
| **XPYUSD** | +1.11 | +1.05 | +0.00 | -1.12 | +0.75 |
| **XPAX** | +2.25 | +2.20 | +1.13 | +0.00 | +1.89 |
| **XUSDT** | +0.36 | +0.30 | -0.74 | -1.85 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.022504** (+2.25% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.021970** (+2.20% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.018867** (+1.89% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.011310** (+1.13% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.011069** (+1.11% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.977991** (-2.20% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.978503** (-2.15% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.981482** (-1.85% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.988817** (-1.12% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.989052** (-1.09% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 58.7234 | $12,701 | $3,306 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 58.7541 | $15,830 | $1,796 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.3734 | $12,539 | $124 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0449 | $12,849 | $4 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 58.9330 | $12,735 | $1,001 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9917 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0027 |
| XPAX | $1.0038 |
| XUSDT | $1.0021 |
