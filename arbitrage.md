# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-17 17:23 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999508 | 0.999052 | 0.999159 | 0.999223 |
| **XUSDC** | 1.000493 | 1.000000 | 0.999544 | 0.999651 | 0.999715 |
| **XPYUSD** | 1.000949 | 1.000457 | 1.000000 | 1.000107 | 1.000172 |
| **XPAX** | 1.000842 | 1.000349 | 0.999893 | 1.000000 | 1.000064 |
| **XUSDT** | 1.000777 | 1.000285 | 0.999828 | 0.999936 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -0.09 | -0.08 | -0.08 |
| **XUSDC** | +0.05 | +0.00 | -0.05 | -0.03 | -0.03 |
| **XPYUSD** | +0.09 | +0.05 | +0.00 | +0.01 | +0.02 |
| **XPAX** | +0.08 | +0.03 | -0.01 | +0.00 | +0.01 |
| **XUSDT** | +0.08 | +0.03 | -0.02 | -0.01 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XMD**: **1.000949** (+0.09% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.000842** (+0.08% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.000777** (+0.08% vs parity) via EASY
- Sell **XUSDC** → buy **XMD**: **1.000493** (+0.05% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.000457** (+0.05% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.999052** (-0.09% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.999159** (-0.08% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.999223** (-0.08% vs parity) via EASY
- Sell **XMD** → buy **XUSDC**: **0.999508** (-0.05% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.999544** (-0.05% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.8300 | $14,489 | $1,592 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.8575 | $14,195 | $1,256 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.8830 | $14,228 | $118 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.8770 | $13,948 | $134 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.8734 | $13,934 | $573 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9867 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0032 |
| XPAX | $0.9811 |
| XUSDT | $0.9822 |
