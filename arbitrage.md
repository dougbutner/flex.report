# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-07 14:06 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000295 | 1.000073 | 0.981658 | 0.996627 |
| **XUSDC** | 0.999705 | 1.000000 | 0.999778 | 0.981368 | 0.996333 |
| **XPYUSD** | 0.999927 | 1.000222 | 1.000000 | 0.981586 | 0.996555 |
| **XPAX** | 1.018685 | 1.018986 | 1.018759 | 1.000000 | 1.015249 |
| **XUSDT** | 1.003384 | 1.003680 | 1.003457 | 0.984980 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.03 | +0.01 | -1.83 | -0.34 |
| **XUSDC** | -0.03 | +0.00 | -0.02 | -1.86 | -0.37 |
| **XPYUSD** | -0.01 | +0.02 | +0.00 | -1.84 | -0.34 |
| **XPAX** | +1.87 | +1.90 | +1.88 | +0.00 | +1.52 |
| **XUSDT** | +0.34 | +0.37 | +0.35 | -1.50 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.018986** (+1.90% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.018759** (+1.88% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.018685** (+1.87% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.015249** (+1.52% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.003680** (+0.37% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.981368** (-1.86% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.981586** (-1.84% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.981658** (-1.83% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.984980** (-1.50% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.996333** (-0.37% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 58.9512 | $12,555 | $5,865 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 58.9338 | $12,709 | $3,367 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 58.9469 | $12,801 | $587 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0527 | $12,863 | $147 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 59.1507 | $12,651 | $1,173 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9885 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0078 |
| XPAX | $1.0052 |
| XUSDT | $1.0034 |
