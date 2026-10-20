# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-20 17:39 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999753 | 0.997763 | 0.998475 | 0.985466 |
| **XUSDC** | 1.000247 | 1.000000 | 0.998009 | 0.998721 | 0.985709 |
| **XPYUSD** | 1.002242 | 1.001995 | 1.000000 | 1.000714 | 0.987676 |
| **XPAX** | 1.001527 | 1.001280 | 0.999287 | 1.000000 | 0.986972 |
| **XUSDT** | 1.014748 | 1.014498 | 1.012478 | 1.013200 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -0.22 | -0.15 | -1.45 |
| **XUSDC** | +0.02 | +0.00 | -0.20 | -0.13 | -1.43 |
| **XPYUSD** | +0.22 | +0.20 | +0.00 | +0.07 | -1.23 |
| **XPAX** | +0.15 | +0.13 | -0.07 | +0.00 | -1.30 |
| **XUSDT** | +1.47 | +1.45 | +1.25 | +1.32 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.014748** (+1.47% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.014498** (+1.45% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.013200** (+1.32% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.012478** (+1.25% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.002242** (+0.22% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.985466** (-1.45% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.985709** (-1.43% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.986972** (-1.30% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.987676** (-1.23% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.997763** (-0.22% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 56.3741 | $14,349 | $1,375 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 56.3880 | $13,932 | $888 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.5005 | $13,783 | $358 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.4602 | $13,826 | $130 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 57.2055 | $13,529 | $265 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9957 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9934 |
| XPAX | $0.9928 |
| XUSDT | $1.0000 |
