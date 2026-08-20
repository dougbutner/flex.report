# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-20 13:39 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999528 | 0.900239 | 0.879220 | 0.994215 |
| **XUSDC** | 1.000472 | 1.000000 | 0.900664 | 0.879635 | 0.994684 |
| **XPYUSD** | 1.110816 | 1.110292 | 1.000000 | 0.976652 | 1.104390 |
| **XPAX** | 1.137372 | 1.136835 | 1.023907 | 1.000000 | 1.130792 |
| **XUSDT** | 1.005818 | 1.005344 | 0.905477 | 0.884336 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -9.98 | -12.08 | -0.58 |
| **XUSDC** | +0.05 | +0.00 | -9.93 | -12.04 | -0.53 |
| **XPYUSD** | +11.08 | +11.03 | +0.00 | -2.33 | +10.44 |
| **XPAX** | +13.74 | +13.68 | +2.39 | +0.00 | +13.08 |
| **XUSDT** | +0.58 | +0.53 | -9.45 | -11.57 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.137372** (+13.74% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.136835** (+13.68% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.130792** (+13.08% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.110816** (+11.08% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.110292** (+11.03% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.879220** (-12.08% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.879635** (-12.04% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.884336** (-11.57% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.900239** (-9.98% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.900664** (-9.93% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.7642 | $15,802 | $12,097 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.7891 | $15,807 | $8,220 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 58.6113 | $14,128 | $37 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0125 | $14,513 | $5 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.0712 | $15,720 | $2,870 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9986 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0987 |
| XPAX | $1.1324 |
| XUSDT | $1.0043 |
