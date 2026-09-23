# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-23 17:37 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999584 | 0.961385 | 0.962320 | 0.999306 |
| **XUSDC** | 1.000416 | 1.000000 | 0.961786 | 0.962720 | 0.999722 |
| **XPYUSD** | 1.040165 | 1.039733 | 1.000000 | 1.000972 | 1.039444 |
| **XPAX** | 1.039156 | 1.038724 | 0.999029 | 1.000000 | 1.038435 |
| **XUSDT** | 1.000694 | 1.000278 | 0.962053 | 0.962988 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.04 | -3.86 | -3.77 | -0.07 |
| **XUSDC** | +0.04 | +0.00 | -3.82 | -3.73 | -0.03 |
| **XPYUSD** | +4.02 | +3.97 | +0.00 | +0.10 | +3.94 |
| **XPAX** | +3.92 | +3.87 | -0.10 | +0.00 | +3.84 |
| **XUSDT** | +0.07 | +0.03 | -3.79 | -3.70 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XMD**: **1.040165** (+4.02% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.039733** (+3.97% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.039444** (+3.94% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.039156** (+3.92% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.038724** (+3.87% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.961385** (-3.86% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.961786** (-3.82% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.962053** (-3.79% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.962320** (-3.77% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.962720** (-3.73% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.5833 | $15,658 | $3,020 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.6056 | $15,366 | $2,216 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.7355 | $14,916 | $23 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6814 | $14,900 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.6205 | $15,271 | $1,304 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9871 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0463 |
| XPAX | $1.0408 |
| XUSDT | $0.9944 |
