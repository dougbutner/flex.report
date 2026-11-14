# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-14 18:36 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000942 | 1.000844 | 1.000724 | 0.992182 |
| **XUSDC** | 0.999059 | 1.000000 | 0.999902 | 0.999782 | 0.991248 |
| **XPYUSD** | 0.999156 | 1.000098 | 1.000000 | 0.999879 | 0.991345 |
| **XPAX** | 0.999277 | 1.000218 | 1.000121 | 1.000000 | 0.991464 |
| **XUSDT** | 1.007880 | 1.008829 | 1.008731 | 1.008609 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.09 | +0.08 | +0.07 | -0.78 |
| **XUSDC** | -0.09 | +0.00 | -0.01 | -0.02 | -0.88 |
| **XPYUSD** | -0.08 | +0.01 | +0.00 | -0.01 | -0.87 |
| **XPAX** | -0.07 | +0.02 | +0.01 | +0.00 | -0.85 |
| **XUSDT** | +0.79 | +0.88 | +0.87 | +0.86 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XUSDC**: **1.008829** (+0.88% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.008731** (+0.87% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.008609** (+0.86% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.007880** (+0.79% vs parity) via EASY
- Sell **XMD** → buy **XUSDC**: **1.000942** (+0.09% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.991248** (-0.88% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.991345** (-0.87% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.991464** (-0.85% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.992182** (-0.78% vs parity) via EASY
- Sell **XUSDC** → buy **XMD**: **0.999059** (-0.09% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 56.4215 | $498 | $78 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 56.3684 | $13,940 | $2,544 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.3739 | $13,938 | $137 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.3807 | $14,007 | $442 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.8661 | $13,695 | $1,133 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9868 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0001 |
| XPAX | $1.0030 |
| XUSDT | $1.0000 |
