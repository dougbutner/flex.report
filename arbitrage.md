# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-18 13:35 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999981 | 1.000400 | 0.982670 | 0.997964 |
| **XUSDC** | 1.000019 | 1.000000 | 1.000419 | 0.982689 | 0.997982 |
| **XPYUSD** | 0.999600 | 0.999581 | 1.000000 | 0.982277 | 0.997564 |
| **XPAX** | 1.017635 | 1.017616 | 1.018043 | 1.000000 | 1.015563 |
| **XUSDT** | 1.002041 | 1.002022 | 1.002442 | 0.984676 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.00 | +0.04 | -1.73 | -0.20 |
| **XUSDC** | +0.00 | +0.00 | +0.04 | -1.73 | -0.20 |
| **XPYUSD** | -0.04 | -0.04 | +0.00 | -1.77 | -0.24 |
| **XPAX** | +1.76 | +1.76 | +1.80 | +0.00 | +1.56 |
| **XUSDT** | +0.20 | +0.20 | +0.24 | -1.53 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XPYUSD**: **1.018043** (+1.80% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.017635** (+1.76% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.017616** (+1.76% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.015563** (+1.56% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.002442** (+0.24% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.982277** (-1.77% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.982670** (-1.73% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.982689** (-1.73% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.984676** (-1.53% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.997564** (-0.24% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.0009 | $12,597 | $1,037 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.0020 | $12,678 | $3,664 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 58.9773 | $12,724 | $126 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0414 | $12,916 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 59.1213 | $12,652 | $945 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9936 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0028 |
| XPAX | $1.0089 |
| XUSDT | $1.0024 |
