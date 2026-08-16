# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-16 13:24 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000010 | 0.999831 | 0.991933 | 0.998554 |
| **XUSDC** | 0.999990 | 1.000000 | 0.999820 | 0.991923 | 0.998543 |
| **XPYUSD** | 1.000170 | 1.000180 | 1.000000 | 0.992101 | 0.998723 |
| **XPAX** | 1.008132 | 1.008142 | 1.007961 | 1.000000 | 1.006674 |
| **XUSDT** | 1.001449 | 1.001459 | 1.001279 | 0.993370 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.00 | -0.02 | -0.81 | -0.14 |
| **XUSDC** | -0.00 | +0.00 | -0.02 | -0.81 | -0.15 |
| **XPYUSD** | +0.02 | +0.02 | +0.00 | -0.79 | -0.13 |
| **XPAX** | +0.81 | +0.81 | +0.80 | +0.00 | +0.67 |
| **XUSDT** | +0.14 | +0.15 | +0.13 | -0.66 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.008142** (+0.81% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.008132** (+0.81% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.007961** (+0.80% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.006674** (+0.67% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.001459** (+0.15% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.991923** (-0.81% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.991933** (-0.81% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.992101** (-0.79% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.993370** (-0.66% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.998543** (-0.15% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.5770 | $12,317 | $2,282 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.5764 | $15,451 | $1,847 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.5871 | $12,442 | $220 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0615 | $12,765 | $92 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 59.6633 | $12,386 | $893 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9923 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0028 |
| XPAX | $0.9978 |
| XUSDT | $1.0010 |
