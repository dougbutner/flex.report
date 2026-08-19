# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-19 13:38 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000558 | 0.984807 | 0.962675 | 1.000644 |
| **XUSDC** | 0.999443 | 1.000000 | 0.984258 | 0.962139 | 1.000087 |
| **XPYUSD** | 1.015427 | 1.015993 | 1.000000 | 0.977527 | 1.016081 |
| **XPAX** | 1.038772 | 1.039351 | 1.022990 | 1.000000 | 1.039441 |
| **XUSDT** | 0.999356 | 0.999913 | 0.984173 | 0.962056 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.06 | -1.52 | -3.73 | +0.06 |
| **XUSDC** | -0.06 | +0.00 | -1.57 | -3.79 | +0.01 |
| **XPYUSD** | +1.54 | +1.60 | +0.00 | -2.25 | +1.61 |
| **XPAX** | +3.88 | +3.94 | +2.30 | +0.00 | +3.94 |
| **XUSDT** | -0.06 | -0.01 | -1.58 | -3.79 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.039441** (+3.94% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.039351** (+3.94% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.038772** (+3.88% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.022990** (+2.30% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.016081** (+1.61% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.962056** (-3.79% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.962139** (-3.79% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.962675** (-3.73% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.977527** (-2.25% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.984173** (-1.58% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 57.7870 | $13,216 | $2,407 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 57.7548 | $13,266 | $2,418 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 58.6785 | $12,933 | $130 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0275 | $13,314 | $3 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 57.7498 | $13,279 | $1,093 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9971 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0083 |
| XPAX | $1.0395 |
| XUSDT | $1.0009 |
