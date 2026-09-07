# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-07 18:00 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000946 | 1.000919 | 0.961416 | 1.001003 |
| **XUSDC** | 0.999055 | 1.000000 | 0.999973 | 0.960507 | 1.000057 |
| **XPYUSD** | 0.999082 | 1.000027 | 1.000000 | 0.960533 | 1.000084 |
| **XPAX** | 1.040133 | 1.041116 | 1.041089 | 1.000000 | 1.041176 |
| **XUSDT** | 0.998998 | 0.999943 | 0.999916 | 0.960452 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.09 | +0.09 | -3.86 | +0.10 |
| **XUSDC** | -0.09 | +0.00 | -0.00 | -3.95 | +0.01 |
| **XPYUSD** | -0.09 | +0.00 | +0.00 | -3.95 | +0.01 |
| **XPAX** | +4.01 | +4.11 | +4.11 | +0.00 | +4.12 |
| **XUSDT** | -0.10 | -0.01 | -0.01 | -3.95 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.041176** (+4.12% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.041116** (+4.11% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.041089** (+4.11% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.040133** (+4.01% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.001003** (+0.10% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.960452** (-3.95% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.960507** (-3.95% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.960533** (-3.95% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.961416** (-3.86% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.998998** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.6077 | $16,392 | $2,575 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.5580 | $17,604 | $1,872 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.5594 | $16,052 | $232 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7190 | $15,413 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.5550 | $15,803 | $317 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9998 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0075 |
| XPAX | $1.0408 |
| XUSDT | $0.9917 |
