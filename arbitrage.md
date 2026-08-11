# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-11 14:14 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999880 | 0.996009 | 0.996259 | 0.997225 |
| **XUSDC** | 1.000120 | 1.000000 | 0.996129 | 0.996379 | 0.997345 |
| **XPYUSD** | 1.004007 | 1.003887 | 1.000000 | 1.000251 | 1.001222 |
| **XPAX** | 1.003755 | 1.003634 | 0.999749 | 1.000000 | 1.000970 |
| **XUSDT** | 1.002782 | 1.002662 | 0.998780 | 0.999031 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.01 | -0.40 | -0.37 | -0.28 |
| **XUSDC** | +0.01 | +0.00 | -0.39 | -0.36 | -0.27 |
| **XPYUSD** | +0.40 | +0.39 | +0.00 | +0.03 | +0.12 |
| **XPAX** | +0.38 | +0.36 | -0.03 | +0.00 | +0.10 |
| **XUSDT** | +0.28 | +0.27 | -0.12 | -0.10 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XMD**: **1.004007** (+0.40% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.003887** (+0.39% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.003755** (+0.38% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.003634** (+0.36% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.002782** (+0.28% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.996009** (-0.40% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.996129** (-0.39% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.996259** (-0.37% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.996379** (-0.36% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.997225** (-0.28% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.8404 | $12,138 | $2,073 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.8476 | $12,615 | $2,385 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 60.0802 | $12,253 | $260 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0651 | $12,735 | $3 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.0069 | $12,241 | $647 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9874 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0057 |
| XPAX | $0.9956 |
| XUSDT | $1.0020 |
