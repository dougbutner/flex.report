# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-09 18:35 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999967 | 1.000476 | 0.980184 | 0.992067 |
| **XUSDC** | 1.000033 | 1.000000 | 1.000509 | 0.980217 | 0.992100 |
| **XPYUSD** | 0.999524 | 0.999491 | 1.000000 | 0.979718 | 0.991595 |
| **XPAX** | 1.020216 | 1.020183 | 1.020702 | 1.000000 | 1.012123 |
| **XUSDT** | 1.007996 | 1.007963 | 1.008476 | 0.988022 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.00 | +0.05 | -1.98 | -0.79 |
| **XUSDC** | +0.00 | +0.00 | +0.05 | -1.98 | -0.79 |
| **XPYUSD** | -0.05 | -0.05 | +0.00 | -2.03 | -0.84 |
| **XPAX** | +2.02 | +2.02 | +2.07 | +0.00 | +1.21 |
| **XUSDT** | +0.80 | +0.80 | +0.85 | -1.20 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XPYUSD**: **1.020702** (+2.07% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.020216** (+2.02% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.020183** (+2.02% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.012123** (+1.21% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.008476** (+0.85% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.979718** (-2.03% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.980184** (-1.98% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.980217** (-1.98% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.988022** (-1.20% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.991595** (-0.84% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.6245 | $15,013 | $1,854 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.6263 | $14,828 | $2,949 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.5985 | $14,939 | $407 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7288 | $14,454 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.0613 | $14,601 | $994 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9807 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0067 |
| XPAX | $1.0113 |
| XUSDT | $1.0000 |
