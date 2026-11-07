# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-07 17:54 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999576 | 0.999446 | 0.999662 | 0.984539 |
| **XUSDC** | 1.000424 | 1.000000 | 0.999870 | 1.000086 | 0.984956 |
| **XPYUSD** | 1.000554 | 1.000130 | 1.000000 | 1.000216 | 0.985084 |
| **XPAX** | 1.000338 | 0.999914 | 0.999784 | 1.000000 | 0.984871 |
| **XUSDT** | 1.015704 | 1.015274 | 1.015142 | 1.015361 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.04 | -0.06 | -0.03 | -1.55 |
| **XUSDC** | +0.04 | +0.00 | -0.01 | +0.01 | -1.50 |
| **XPYUSD** | +0.06 | +0.01 | +0.00 | +0.02 | -1.49 |
| **XPAX** | +0.03 | -0.01 | -0.02 | +0.00 | -1.51 |
| **XUSDT** | +1.57 | +1.53 | +1.51 | +1.54 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.015704** (+1.57% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.015361** (+1.54% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.015274** (+1.53% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.015142** (+1.51% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.000554** (+0.06% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.984539** (-1.55% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.984871** (-1.51% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.984956** (-1.50% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.985084** (-1.49% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.999446** (-0.06% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.4885 | $513 | $31 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.5116 | $14,885 | $2,445 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.5187 | $15,015 | $268 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.5069 | $15,052 | $319 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.3442 | $14,456 | $845 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0005 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0090 |
| XPAX | $1.0089 |
| XUSDT | $1.0000 |
