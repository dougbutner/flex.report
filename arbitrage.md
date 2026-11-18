# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-18 21:01 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000154 | 0.999845 | 1.008459 | 0.995966 |
| **XUSDC** | 0.999846 | 1.000000 | 0.999691 | 1.008304 | 0.995813 |
| **XPYUSD** | 1.000155 | 1.000309 | 1.000000 | 1.008616 | 0.996121 |
| **XPAX** | 0.991612 | 0.991764 | 0.991457 | 1.000000 | 0.987612 |
| **XUSDT** | 1.004050 | 1.004204 | 1.003894 | 1.012544 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.02 | -0.02 | +0.85 | -0.40 |
| **XUSDC** | -0.02 | +0.00 | -0.03 | +0.83 | -0.42 |
| **XPYUSD** | +0.02 | +0.03 | +0.00 | +0.86 | -0.39 |
| **XPAX** | -0.84 | -0.82 | -0.85 | +0.00 | -1.24 |
| **XUSDT** | +0.40 | +0.42 | +0.39 | +1.25 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPAX**: **1.012544** (+1.25% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **1.008616** (+0.86% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.008459** (+0.85% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **1.008304** (+0.83% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.004204** (+0.42% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.987612** (-1.24% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **0.991457** (-0.85% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.991612** (-0.84% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **0.991764** (-0.82% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.995813** (-0.42% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 58.5446 | $528 | $355 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 58.5356 | $12,895 | $4,626 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 58.5537 | $12,874 | $124 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 58.0535 | $13,146 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 58.7817 | $12,779 | $2,234 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9772 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9991 |
| XPAX | $0.9995 |
| XUSDT | $1.0000 |
