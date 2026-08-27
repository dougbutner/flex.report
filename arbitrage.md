# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-27 22:42 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999717 | 0.947851 | 0.943808 | 1.000186 |
| **XUSDC** | 1.000283 | 1.000000 | 0.948119 | 0.944075 | 1.000469 |
| **XPYUSD** | 1.055019 | 1.054720 | 1.000000 | 0.995736 | 1.055215 |
| **XPAX** | 1.059537 | 1.059238 | 1.004283 | 1.000000 | 1.059734 |
| **XUSDT** | 0.999814 | 0.999531 | 0.947674 | 0.943633 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.03 | -5.21 | -5.62 | +0.02 |
| **XUSDC** | +0.03 | +0.00 | -5.19 | -5.59 | +0.05 |
| **XPYUSD** | +5.50 | +5.47 | +0.00 | -0.43 | +5.52 |
| **XPAX** | +5.95 | +5.92 | +0.43 | +0.00 | +5.97 |
| **XUSDT** | -0.02 | -0.05 | -5.23 | -5.64 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.059734** (+5.97% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.059537** (+5.95% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.059238** (+5.92% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.055215** (+5.52% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.055019** (+5.50% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.943633** (-5.64% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.943808** (-5.62% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.944075** (-5.59% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.947674** (-5.23% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.947851** (-5.21% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 51.6334 | $16,844 | $3,877 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 51.6480 | $17,981 | $4,113 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.4742 | $15,623 | $109 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7075 | $15,725 | $5 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 51.6238 | $16,451 | $1,266 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9941 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0482 |
| XPAX | $1.0615 |
| XUSDT | $0.9997 |
