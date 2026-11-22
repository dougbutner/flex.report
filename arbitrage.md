# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-22 20:03 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000209 | 0.988581 | 0.985556 | 0.982418 |
| **XUSDC** | 0.999791 | 1.000000 | 0.988375 | 0.985351 | 0.982213 |
| **XPYUSD** | 1.011550 | 1.011762 | 1.000000 | 0.996940 | 0.993766 |
| **XPAX** | 1.014656 | 1.014867 | 1.003070 | 1.000000 | 0.996816 |
| **XUSDT** | 1.017896 | 1.018109 | 1.006273 | 1.003194 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.02 | -1.14 | -1.44 | -1.76 |
| **XUSDC** | -0.02 | +0.00 | -1.16 | -1.46 | -1.78 |
| **XPYUSD** | +1.16 | +1.18 | +0.00 | -0.31 | -0.62 |
| **XPAX** | +1.47 | +1.49 | +0.31 | +0.00 | -0.32 |
| **XUSDT** | +1.79 | +1.81 | +0.63 | +0.32 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XUSDC**: **1.018109** (+1.81% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.017896** (+1.79% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.014867** (+1.49% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.014656** (+1.47% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.011762** (+1.18% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.982213** (-1.78% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.982418** (-1.76% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.985351** (-1.46% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.985556** (-1.44% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.988375** (-1.16% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 58.9672 | $476 | $104 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 58.9549 | $12,700 | $1,854 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.6483 | $12,553 | $287 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 59.8314 | $12,563 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.0225 | $12,210 | $860 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9643 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0138 |
| XPAX | $1.0191 |
| XUSDT | $1.0000 |
