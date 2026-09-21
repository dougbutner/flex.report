# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-21 18:24 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000179 | 0.954964 | 0.955595 | 0.999238 |
| **XUSDC** | 0.999821 | 1.000000 | 0.954794 | 0.955425 | 0.999059 |
| **XPYUSD** | 1.047159 | 1.047346 | 1.000000 | 1.000661 | 1.046361 |
| **XPAX** | 1.046468 | 1.046655 | 0.999340 | 1.000000 | 1.045670 |
| **XUSDT** | 1.000763 | 1.000942 | 0.955693 | 0.956325 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.02 | -4.50 | -4.44 | -0.08 |
| **XUSDC** | -0.02 | +0.00 | -4.52 | -4.46 | -0.09 |
| **XPYUSD** | +4.72 | +4.73 | +0.00 | +0.07 | +4.64 |
| **XPAX** | +4.65 | +4.67 | -0.07 | +0.00 | +4.57 |
| **XUSDT** | +0.08 | +0.09 | -4.43 | -4.37 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XUSDC**: **1.047346** (+4.73% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.047159** (+4.72% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.046655** (+4.67% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.046468** (+4.65% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.046361** (+4.64% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.954794** (-4.52% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.954964** (-4.50% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.955425** (-4.46% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.955595** (-4.44% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.955693** (-4.43% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.2152 | $15,999 | $7,469 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.2057 | $15,580 | $4,516 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.7248 | $14,810 | $126 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6880 | $14,870 | $8 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.2558 | $15,419 | $1,807 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9961 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0384 |
| XPAX | $1.0390 |
| XUSDT | $0.9914 |
