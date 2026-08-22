# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-22 13:25 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999366 | 0.957166 | 0.888096 | 0.982481 |
| **XUSDC** | 1.000634 | 1.000000 | 0.957772 | 0.888659 | 0.983103 |
| **XPYUSD** | 1.044751 | 1.044089 | 1.000000 | 0.927839 | 1.026448 |
| **XPAX** | 1.126005 | 1.125291 | 1.077773 | 1.000000 | 1.106278 |
| **XUSDT** | 1.017832 | 1.017187 | 0.974234 | 0.903932 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.06 | -4.28 | -11.19 | -1.75 |
| **XUSDC** | +0.06 | +0.00 | -4.22 | -11.13 | -1.69 |
| **XPYUSD** | +4.48 | +4.41 | +0.00 | -7.22 | +2.64 |
| **XPAX** | +12.60 | +12.53 | +7.78 | +0.00 | +10.63 |
| **XUSDT** | +1.78 | +1.72 | -2.58 | -9.61 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.126005** (+12.60% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.125291** (+12.53% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.106278** (+10.63% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.077773** (+7.78% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.044751** (+4.48% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.888096** (-11.19% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.888659** (-11.13% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.903932** (-9.61% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.927839** (-7.22% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.957166** (-4.28% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.3671 | $16,313 | $11,449 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.4003 | $17,685 | $14,443 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.7106 | $15,601 | $965 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 58.9656 | $15,041 | $275 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.3009 | $15,782 | $5,472 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9869 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0554 |
| XPAX | $1.1309 |
| XUSDT | $1.0163 |
