# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-12 15:56 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999844 | 0.999375 | 0.973327 | 0.998193 |
| **XUSDC** | 1.000156 | 1.000000 | 0.999531 | 0.973478 | 0.998349 |
| **XPYUSD** | 1.000625 | 1.000469 | 1.000000 | 0.973935 | 0.998817 |
| **XPAX** | 1.027404 | 1.027244 | 1.026763 | 1.000000 | 1.025548 |
| **XUSDT** | 1.001810 | 1.001654 | 1.001184 | 0.975088 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -0.06 | -2.67 | -0.18 |
| **XUSDC** | +0.02 | +0.00 | -0.05 | -2.65 | -0.17 |
| **XPYUSD** | +0.06 | +0.05 | +0.00 | -2.61 | -0.12 |
| **XPAX** | +2.74 | +2.72 | +2.68 | +0.00 | +2.55 |
| **XUSDT** | +0.18 | +0.17 | +0.12 | -2.49 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.027404** (+2.74% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.027244** (+2.72% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.026763** (+2.68% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.025548** (+2.55% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.001810** (+0.18% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.973327** (-2.67% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.973478** (-2.65% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.973935** (-2.61% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.975088** (-2.49% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.998193** (-0.18% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.2614 | $15,907 | $1,471 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.2697 | $15,545 | $1,927 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.2947 | $15,632 | $127 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7210 | $15,146 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.3578 | $15,393 | $600 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9920 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0065 |
| XPAX | $1.0228 |
| XUSDT | $0.9933 |
