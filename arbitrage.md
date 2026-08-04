# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-04 15:17 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999459 | 0.994172 | 0.978174 | 0.993797 |
| **XUSDC** | 1.000541 | 1.000000 | 0.994710 | 0.978703 | 0.994334 |
| **XPYUSD** | 1.005862 | 1.005318 | 1.000000 | 0.983908 | 0.999623 |
| **XPAX** | 1.022313 | 1.021760 | 1.016355 | 1.000000 | 1.015971 |
| **XUSDT** | 1.006242 | 1.005698 | 1.000378 | 0.984280 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -0.58 | -2.18 | -0.62 |
| **XUSDC** | +0.05 | +0.00 | -0.53 | -2.13 | -0.57 |
| **XPYUSD** | +0.59 | +0.53 | +0.00 | -1.61 | -0.04 |
| **XPAX** | +2.23 | +2.18 | +1.64 | +0.00 | +1.60 |
| **XUSDT** | +0.62 | +0.57 | +0.04 | -1.57 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.022313** (+2.23% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.021760** (+2.18% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.016355** (+1.64% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.015971** (+1.60% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.006242** (+0.62% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.978174** (-2.18% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.978703** (-2.13% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.983908** (-1.61% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.984280** (-1.57% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.993797** (-0.62% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 58.9701 | $12,499 | $1,670 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.0020 | $12,677 | $1,559 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.3158 | $12,659 | $133 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.2859 | $13,002 | $3 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 59.3382 | $12,407 | $437 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9848 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0102 |
| XPAX | $1.0245 |
| XUSDT | $0.9908 |
