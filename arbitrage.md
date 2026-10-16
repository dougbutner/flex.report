# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-16 17:06 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999442 | 1.000066 | 0.999101 | 0.994317 |
| **XUSDC** | 1.000559 | 1.000000 | 1.000625 | 0.999659 | 0.994872 |
| **XPYUSD** | 0.999934 | 0.999375 | 1.000000 | 0.999035 | 0.994251 |
| **XPAX** | 1.000900 | 1.000341 | 1.000966 | 1.000000 | 0.995212 |
| **XUSDT** | 1.005716 | 1.005154 | 1.005782 | 1.004811 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.06 | +0.01 | -0.09 | -0.57 |
| **XUSDC** | +0.06 | +0.00 | +0.06 | -0.03 | -0.51 |
| **XPYUSD** | -0.01 | -0.06 | +0.00 | -0.10 | -0.57 |
| **XPAX** | +0.09 | +0.03 | +0.10 | +0.00 | -0.48 |
| **XUSDT** | +0.57 | +0.52 | +0.58 | +0.48 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPYUSD**: **1.005782** (+0.58% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.005716** (+0.57% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.005154** (+0.52% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.004811** (+0.48% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.000966** (+0.10% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.994251** (-0.57% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.994317** (-0.57% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.994872** (-0.51% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.995212** (-0.48% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.999035** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.6725 | $14,540 | $535 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.7036 | $14,273 | $1,917 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.6688 | $14,406 | $147 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7226 | $14,436 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.9907 | $14,129 | $594 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9848 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0081 |
| XPAX | $1.0099 |
| XUSDT | $1.0000 |
