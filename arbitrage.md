# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-09 13:42 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999230 | 0.999575 | 0.983831 | 0.981020 |
| **XUSDC** | 1.000770 | 1.000000 | 1.000345 | 0.984589 | 0.981775 |
| **XPYUSD** | 1.000425 | 0.999655 | 1.000000 | 0.984249 | 0.981436 |
| **XPAX** | 1.016435 | 1.015653 | 1.016003 | 1.000000 | 0.997142 |
| **XUSDT** | 1.019348 | 1.018563 | 1.018915 | 1.002866 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.08 | -0.04 | -1.62 | -1.90 |
| **XUSDC** | +0.08 | +0.00 | +0.03 | -1.54 | -1.82 |
| **XPYUSD** | +0.04 | -0.03 | +0.00 | -1.58 | -1.86 |
| **XPAX** | +1.64 | +1.57 | +1.60 | +0.00 | -0.29 |
| **XUSDT** | +1.93 | +1.86 | +1.89 | +0.29 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.019348** (+1.93% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.018915** (+1.89% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.018563** (+1.86% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.016435** (+1.64% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.016003** (+1.60% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.981020** (-1.90% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.981436** (-1.86% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.981775** (-1.82% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.983831** (-1.62% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.984249** (-1.58% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.0824 | $12,500 | $2,193 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.1279 | $12,619 | $1,970 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.1075 | $12,719 | $158 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0534 | $12,798 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.2255 | $12,338 | $345 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9890 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0072 |
| XPAX | $1.0001 |
| XUSDT | $1.0182 |
