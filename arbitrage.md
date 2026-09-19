# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-19 16:10 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999568 | 1.000513 | 0.983466 | 0.989440 |
| **XUSDC** | 1.000433 | 1.000000 | 1.000946 | 0.983891 | 0.989868 |
| **XPYUSD** | 0.999487 | 0.999055 | 1.000000 | 0.982961 | 0.988932 |
| **XPAX** | 1.016812 | 1.016373 | 1.017334 | 1.000000 | 1.006075 |
| **XUSDT** | 1.010673 | 1.010236 | 1.011192 | 0.993962 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.04 | +0.05 | -1.65 | -1.06 |
| **XUSDC** | +0.04 | +0.00 | +0.09 | -1.61 | -1.01 |
| **XPYUSD** | -0.05 | -0.09 | +0.00 | -1.70 | -1.11 |
| **XPAX** | +1.68 | +1.64 | +1.73 | +0.00 | +0.61 |
| **XUSDT** | +1.07 | +1.02 | +1.12 | -0.60 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XPYUSD**: **1.017334** (+1.73% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.016812** (+1.68% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.016373** (+1.64% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.011192** (+1.12% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.010673** (+1.07% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.982961** (-1.70% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.983466** (-1.65% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.983891** (-1.61% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.988932** (-1.11% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.989440** (-1.06% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.7750 | $15,083 | $6,103 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.7987 | $14,738 | $2,577 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.7469 | $14,896 | $655 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6959 | $14,521 | $4 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.3596 | $14,582 | $1,176 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9903 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0090 |
| XPAX | $1.0148 |
| XUSDT | $1.0092 |
