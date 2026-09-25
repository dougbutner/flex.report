# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-25 17:39 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000665 | 0.974514 | 0.957063 | 1.002977 |
| **XUSDC** | 0.999336 | 1.000000 | 0.973866 | 0.956427 | 1.002311 |
| **XPYUSD** | 1.026153 | 1.026835 | 1.000000 | 0.982093 | 1.029208 |
| **XPAX** | 1.044864 | 1.045558 | 1.018234 | 1.000000 | 1.047975 |
| **XUSDT** | 0.997031 | 0.997694 | 0.971621 | 0.954221 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | -2.55 | -4.29 | +0.30 |
| **XUSDC** | -0.07 | +0.00 | -2.61 | -4.36 | +0.23 |
| **XPYUSD** | +2.62 | +2.68 | +0.00 | -1.79 | +2.92 |
| **XPAX** | +4.49 | +4.56 | +1.82 | +0.00 | +4.80 |
| **XUSDT** | -0.30 | -0.23 | -2.84 | -4.58 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.047975** (+4.80% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.045558** (+4.56% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.044864** (+4.49% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.029208** (+2.92% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.026835** (+2.68% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.954221** (-4.58% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.956427** (-4.36% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.957063** (-4.29% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.971621** (-2.84% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.973866** (-2.61% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.2902 | $15,837 | $2,989 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.2548 | $15,554 | $3,124 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.6839 | $15,069 | $185 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6810 | $14,806 | $5 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.1320 | $15,373 | $1,332 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9885 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0185 |
| XPAX | $1.0343 |
| XUSDT | $0.9842 |
