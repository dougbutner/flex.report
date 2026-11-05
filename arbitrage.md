# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-05 20:25 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999367 | 0.993133 | 0.994324 | 0.986473 |
| **XUSDC** | 1.000633 | 1.000000 | 0.993762 | 0.994954 | 0.987098 |
| **XPYUSD** | 1.006914 | 1.006277 | 1.000000 | 1.001199 | 0.993294 |
| **XPAX** | 1.005708 | 1.005072 | 0.998802 | 1.000000 | 0.992105 |
| **XUSDT** | 1.013712 | 1.013071 | 1.006751 | 1.007958 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.06 | -0.69 | -0.57 | -1.35 |
| **XUSDC** | +0.06 | +0.00 | -0.62 | -0.50 | -1.29 |
| **XPYUSD** | +0.69 | +0.63 | +0.00 | +0.12 | -0.67 |
| **XPAX** | +0.57 | +0.51 | -0.12 | +0.00 | -0.79 |
| **XUSDT** | +1.37 | +1.31 | +0.68 | +0.80 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.013712** (+1.37% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.013071** (+1.31% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.007958** (+0.80% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.006914** (+0.69% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.006751** (+0.68% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.986473** (-1.35% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.987098** (-1.29% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.992105** (-0.79% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.993133** (-0.69% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.993294** (-0.67% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.0629 | $520 | $88 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.0965 | $15,639 | $2,943 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.4298 | $15,691 | $3 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 53.3658 | $15,737 | $118 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.7905 | $15,266 | $811 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0004 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0150 |
| XPAX | $1.0136 |
| XUSDT | $1.0000 |
