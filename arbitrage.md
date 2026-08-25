# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-25 05:05 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999670 | 0.978729 | 0.969858 | 0.998867 |
| **XUSDC** | 1.000330 | 1.000000 | 0.979052 | 0.970178 | 0.999196 |
| **XPYUSD** | 1.021733 | 1.021396 | 1.000000 | 0.990936 | 1.020575 |
| **XPAX** | 1.031079 | 1.030739 | 1.009147 | 1.000000 | 1.029911 |
| **XUSDT** | 1.001134 | 1.000804 | 0.979839 | 0.970958 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.03 | -2.13 | -3.01 | -0.11 |
| **XUSDC** | +0.03 | +0.00 | -2.09 | -2.98 | -0.08 |
| **XPYUSD** | +2.17 | +2.14 | +0.00 | -0.91 | +2.06 |
| **XPAX** | +3.11 | +3.07 | +0.91 | +0.00 | +2.99 |
| **XUSDT** | +0.11 | +0.08 | -2.02 | -2.90 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.031079** (+3.11% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.030739** (+3.07% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.029911** (+2.99% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.021733** (+2.17% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.021396** (+2.14% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.969858** (-3.01% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.970178** (-2.98% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.970958** (-2.90% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.978729** (-2.13% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.979052** (-2.09% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.0714 | $16,042 | $2,916 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.0889 | $17,082 | $2,963 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.2248 | $15,195 | $143 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7208 | $15,998 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.1316 | $15,617 | $290 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9940 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0106 |
| XPAX | $1.0384 |
| XUSDT | $0.9999 |
