# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-10 17:33 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999718 | 0.999519 | 0.972893 | 0.991728 |
| **XUSDC** | 1.000282 | 1.000000 | 0.999801 | 0.973168 | 0.992008 |
| **XPYUSD** | 1.000482 | 1.000199 | 1.000000 | 0.973362 | 0.992205 |
| **XPAX** | 1.027862 | 1.027572 | 1.027367 | 1.000000 | 1.019359 |
| **XUSDT** | 1.008341 | 1.008057 | 1.007856 | 0.981009 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.03 | -0.05 | -2.71 | -0.83 |
| **XUSDC** | +0.03 | +0.00 | -0.02 | -2.68 | -0.80 |
| **XPYUSD** | +0.05 | +0.02 | +0.00 | -2.66 | -0.78 |
| **XPAX** | +2.79 | +2.76 | +2.74 | +0.00 | +1.94 |
| **XUSDT** | +0.83 | +0.81 | +0.79 | -1.90 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.027862** (+2.79% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.027572** (+2.76% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.027367** (+2.74% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.019359** (+1.94% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.008341** (+0.83% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.972893** (-2.71% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.973168** (-2.68% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.973362** (-2.66% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.981009** (-1.90% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.991728** (-0.83% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.1997 | $15,417 | $682 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.2150 | $15,043 | $1,926 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.2258 | $14,951 | $204 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7098 | $14,553 | $5 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.6518 | $14,813 | $624 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9926 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9944 |
| XPAX | $1.0176 |
| XUSDT | $1.0000 |
