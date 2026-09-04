# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-04 16:40 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000900 | 1.000355 | 0.967409 | 1.000285 |
| **XUSDC** | 0.999101 | 1.000000 | 0.999456 | 0.966539 | 0.999386 |
| **XPYUSD** | 0.999645 | 1.000545 | 1.000000 | 0.967066 | 0.999930 |
| **XPAX** | 1.033689 | 1.034619 | 1.034056 | 1.000000 | 1.033984 |
| **XUSDT** | 0.999715 | 1.000615 | 1.000070 | 0.967133 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.09 | +0.04 | -3.26 | +0.03 |
| **XUSDC** | -0.09 | +0.00 | -0.05 | -3.35 | -0.06 |
| **XPYUSD** | -0.04 | +0.05 | +0.00 | -3.29 | -0.01 |
| **XPAX** | +3.37 | +3.46 | +3.41 | +0.00 | +3.40 |
| **XUSDT** | -0.03 | +0.06 | +0.01 | -3.29 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.034619** (+3.46% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.034056** (+3.41% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.033984** (+3.40% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.033689** (+3.37% vs parity) via EASY
- Sell **XMD** → buy **XUSDC**: **1.000900** (+0.09% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.966539** (-3.35% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.967066** (-3.29% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.967133** (-3.29% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.967409** (-3.26% vs parity) via EASY
- Sell **XUSDC** → buy **XMD**: **0.999101** (-0.09% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.9316 | $16,275 | $3,189 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.8840 | $15,755 | $2,592 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.9128 | $15,873 | $438 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7148 | $15,354 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.9165 | $15,743 | $792 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0036 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0085 |
| XPAX | $1.0366 |
| XUSDT | $1.0004 |
