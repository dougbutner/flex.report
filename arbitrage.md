# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-08 18:10 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000410 | 1.000423 | 1.000798 | 0.988633 |
| **XUSDC** | 0.999590 | 1.000000 | 1.000013 | 1.000388 | 0.988228 |
| **XPYUSD** | 0.999578 | 0.999987 | 1.000000 | 1.000375 | 0.988215 |
| **XPAX** | 0.999203 | 0.999612 | 0.999625 | 1.000000 | 0.987845 |
| **XUSDT** | 1.011498 | 1.011912 | 1.011925 | 1.012305 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.04 | +0.04 | +0.08 | -1.14 |
| **XUSDC** | -0.04 | +0.00 | +0.00 | +0.04 | -1.18 |
| **XPYUSD** | -0.04 | -0.00 | +0.00 | +0.04 | -1.18 |
| **XPAX** | -0.08 | -0.04 | -0.04 | +0.00 | -1.22 |
| **XUSDT** | +1.15 | +1.19 | +1.19 | +1.23 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPAX**: **1.012305** (+1.23% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.011925** (+1.19% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.011912** (+1.19% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.011498** (+1.15% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.000798** (+0.08% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.987845** (-1.22% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.988215** (-1.18% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.988228** (-1.18% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.988633** (-1.14% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.999203** (-0.08% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.9238 | $511 | $30 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.9013 | $14,683 | $521 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.9006 | $14,812 | $104 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.8800 | $14,854 | $130 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.5553 | $14,348 | $127 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0004 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0088 |
| XPAX | $1.0087 |
| XUSDT | $1.0000 |
