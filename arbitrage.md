# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-12 14:16 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999859 | 0.994602 | 0.994126 | 0.994794 |
| **XUSDC** | 1.000141 | 1.000000 | 0.994742 | 0.994266 | 0.994934 |
| **XPYUSD** | 1.005428 | 1.005286 | 1.000000 | 0.999522 | 1.000193 |
| **XPAX** | 1.005908 | 1.005767 | 1.000478 | 1.000000 | 1.000671 |
| **XUSDT** | 1.005233 | 1.005092 | 0.999807 | 0.999329 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.01 | -0.54 | -0.59 | -0.52 |
| **XUSDC** | +0.01 | +0.00 | -0.53 | -0.57 | -0.51 |
| **XPYUSD** | +0.54 | +0.53 | +0.00 | -0.05 | +0.02 |
| **XPAX** | +0.59 | +0.58 | +0.05 | +0.00 | +0.07 |
| **XUSDT** | +0.52 | +0.51 | -0.02 | -0.07 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.005908** (+0.59% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.005767** (+0.58% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.005428** (+0.54% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.005286** (+0.53% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.005233** (+0.52% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.994126** (-0.59% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.994266** (-0.57% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.994602** (-0.54% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.994742** (-0.53% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.994794** (-0.52% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.7122 | $12,213 | $1,746 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.7206 | $12,673 | $1,575 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 60.0363 | $12,273 | $41 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0650 | $12,809 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.0247 | $12,270 | $551 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9889 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0057 |
| XPAX | $1.0014 |
| XUSDT | $1.0050 |
