# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-22 17:27 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999102 | 0.948912 | 0.950663 | 1.009986 |
| **XUSDC** | 1.000899 | 1.000000 | 0.949765 | 0.951518 | 1.010894 |
| **XPYUSD** | 1.053839 | 1.052892 | 1.000000 | 1.001846 | 1.064362 |
| **XPAX** | 1.051897 | 1.050952 | 0.998157 | 1.000000 | 1.062401 |
| **XUSDT** | 0.990113 | 0.989223 | 0.939530 | 0.941264 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.09 | -5.11 | -4.93 | +1.00 |
| **XUSDC** | +0.09 | +0.00 | -5.02 | -4.85 | +1.09 |
| **XPYUSD** | +5.38 | +5.29 | +0.00 | +0.18 | +6.44 |
| **XPAX** | +5.19 | +5.10 | -0.18 | +0.00 | +6.24 |
| **XUSDT** | -0.99 | -1.08 | -6.05 | -5.87 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XUSDT**: **1.064362** (+6.44% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.062401** (+6.24% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.053839** (+5.38% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.052892** (+5.29% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.051897** (+5.19% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.939530** (-6.05% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.941264** (-5.87% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.948912** (-5.11% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.949765** (-5.02% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.950663** (-4.93% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.9376 | $16,213 | $2,885 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.9852 | $15,700 | $3,815 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.7877 | $14,869 | $19 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6849 | $14,898 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.4142 | $15,766 | $2,581 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0000 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0448 |
| XPAX | $1.0408 |
| XUSDT | $0.9845 |
