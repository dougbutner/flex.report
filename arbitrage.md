# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-28 19:55 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999517 | 1.000324 | 0.970897 | 0.998749 |
| **XUSDC** | 1.000483 | 1.000000 | 1.000807 | 0.971366 | 0.999231 |
| **XPYUSD** | 0.999676 | 0.999194 | 1.000000 | 0.970583 | 0.998426 |
| **XPAX** | 1.029975 | 1.029478 | 1.030308 | 1.000000 | 1.028687 |
| **XUSDT** | 1.001252 | 1.000769 | 1.001577 | 0.972113 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | +0.03 | -2.91 | -0.13 |
| **XUSDC** | +0.05 | +0.00 | +0.08 | -2.86 | -0.08 |
| **XPYUSD** | -0.03 | -0.08 | +0.00 | -2.94 | -0.16 |
| **XPAX** | +3.00 | +2.95 | +3.03 | +0.00 | +2.87 |
| **XUSDT** | +0.13 | +0.08 | +0.16 | -2.79 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XPYUSD**: **1.030308** (+3.03% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.029975** (+3.00% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.029478** (+2.95% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.028687** (+2.87% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.001577** (+0.16% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.970583** (-2.94% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.970897** (-2.91% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.971366** (-2.86% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.972113** (-2.79% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.998426** (-0.16% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.0585 | $15,395 | $1,884 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.0846 | $15,110 | $1,310 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.0410 | $15,267 | $179 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6789 | $14,516 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.1262 | $14,986 | $309 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9865 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0089 |
| XPAX | $1.0139 |
| XUSDT | $0.9933 |
