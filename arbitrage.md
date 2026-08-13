# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-13 14:17 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000005 | 1.000979 | 0.999785 | 0.998475 |
| **XUSDC** | 0.999995 | 1.000000 | 1.000974 | 0.999780 | 0.998470 |
| **XPYUSD** | 0.999022 | 0.999027 | 1.000000 | 0.998808 | 0.997499 |
| **XPAX** | 1.000215 | 1.000220 | 1.001194 | 1.000000 | 0.998690 |
| **XUSDT** | 1.001527 | 1.001532 | 1.002507 | 1.001312 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.00 | +0.10 | -0.02 | -0.15 |
| **XUSDC** | -0.00 | +0.00 | +0.10 | -0.02 | -0.15 |
| **XPYUSD** | -0.10 | -0.10 | +0.00 | -0.12 | -0.25 |
| **XPAX** | +0.02 | +0.02 | +0.12 | +0.00 | -0.13 |
| **XUSDT** | +0.15 | +0.15 | +0.25 | +0.13 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPYUSD**: **1.002507** (+0.25% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.001532** (+0.15% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.001527** (+0.15% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.001312** (+0.13% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.001194** (+0.12% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.997499** (-0.25% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.998470** (-0.15% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.998475** (-0.15% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.998690** (-0.13% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.998808** (-0.12% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 60.0477 | $12,168 | $835 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 60.0474 | $12,253 | $979 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.9890 | $12,283 | $104 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0606 | $12,703 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.1394 | $12,177 | $179 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9975 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0048 |
| XPAX | $0.9930 |
| XUSDT | $1.0016 |
