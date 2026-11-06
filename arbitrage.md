# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-06 19:46 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000028 | 0.998999 | 0.999666 | 0.995803 |
| **XUSDC** | 0.999972 | 1.000000 | 0.998971 | 0.999638 | 0.995775 |
| **XPYUSD** | 1.001002 | 1.001030 | 1.000000 | 1.000668 | 0.996800 |
| **XPAX** | 1.000334 | 1.000362 | 0.999333 | 1.000000 | 0.996135 |
| **XUSDT** | 1.004215 | 1.004243 | 1.003210 | 1.003880 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.00 | -0.10 | -0.03 | -0.42 |
| **XUSDC** | -0.00 | +0.00 | -0.10 | -0.04 | -0.42 |
| **XPYUSD** | +0.10 | +0.10 | +0.00 | +0.07 | -0.32 |
| **XPAX** | +0.03 | +0.04 | -0.07 | +0.00 | -0.39 |
| **XUSDT** | +0.42 | +0.42 | +0.32 | +0.39 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XUSDC**: **1.004243** (+0.42% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.004215** (+0.42% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.003880** (+0.39% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.003210** (+0.32% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.001030** (+0.10% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.995775** (-0.42% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.995803** (-0.42% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.996135** (-0.39% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.996800** (-0.32% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.998971** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.9022 | $516 | $133 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.9007 | $15,207 | $3,215 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.9562 | $15,155 | $335 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 53.9202 | $15,365 | $270 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.1294 | $15,086 | $659 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0004 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9985 |
| XPAX | $1.0090 |
| XUSDT | $1.0000 |
