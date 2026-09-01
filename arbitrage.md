# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-01 17:04 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999932 | 0.999302 | 0.967552 | 1.000344 |
| **XUSDC** | 1.000068 | 1.000000 | 0.999370 | 0.967618 | 1.000412 |
| **XPYUSD** | 1.000699 | 1.000631 | 1.000000 | 0.968229 | 1.001043 |
| **XPAX** | 1.033536 | 1.033466 | 1.032814 | 1.000000 | 1.033891 |
| **XUSDT** | 0.999656 | 0.999588 | 0.998958 | 0.967220 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.01 | -0.07 | -3.24 | +0.03 |
| **XUSDC** | +0.01 | +0.00 | -0.06 | -3.24 | +0.04 |
| **XPYUSD** | +0.07 | +0.06 | +0.00 | -3.18 | +0.10 |
| **XPAX** | +3.35 | +3.35 | +3.28 | +0.00 | +3.39 |
| **XUSDT** | -0.03 | -0.04 | -0.10 | -3.28 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.033891** (+3.39% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.033536** (+3.35% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.033466** (+3.35% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.032814** (+3.28% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.001043** (+0.10% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.967220** (-3.28% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.967552** (-3.24% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.967618** (-3.24% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.968229** (-3.18% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.998958** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.9373 | $16,086 | $3,181 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.9409 | $15,819 | $3,134 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.9743 | $15,854 | $208 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7126 | $15,417 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.9191 | $15,735 | $660 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9922 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0095 |
| XPAX | $1.0408 |
| XUSDT | $1.0000 |
