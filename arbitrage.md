# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-28 18:35 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999766 | 0.954843 | 0.948604 | 0.998516 |
| **XUSDC** | 1.000234 | 1.000000 | 0.955067 | 0.948826 | 0.998750 |
| **XPYUSD** | 1.047292 | 1.047047 | 1.000000 | 0.993465 | 1.045739 |
| **XPAX** | 1.054181 | 1.053934 | 1.006578 | 1.000000 | 1.052617 |
| **XUSDT** | 1.001486 | 1.001251 | 0.956262 | 0.950013 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -4.52 | -5.14 | -0.15 |
| **XUSDC** | +0.02 | +0.00 | -4.49 | -5.12 | -0.12 |
| **XPYUSD** | +4.73 | +4.70 | +0.00 | -0.65 | +4.57 |
| **XPAX** | +5.42 | +5.39 | +0.66 | +0.00 | +5.26 |
| **XUSDT** | +0.15 | +0.13 | -4.37 | -5.00 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.054181** (+5.42% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.053934** (+5.39% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.052617** (+5.26% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.047292** (+4.73% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.047047** (+4.70% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.948604** (-5.14% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.948826** (-5.12% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.950013** (-5.00% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.954843** (-4.52% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.955067** (-4.49% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 51.6914 | $534 | $84 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 51.7035 | $16,412 | $6,858 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.1360 | $15,623 | $945 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.4921 | $15,536 | $280 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 51.7682 | $16,374 | $2,516 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9980 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0358 |
| XPAX | $1.0408 |
| XUSDT | $1.0000 |
