# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-30 18:13 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999700 | 0.999595 | 0.971040 | 1.000583 |
| **XUSDC** | 1.000300 | 1.000000 | 0.999895 | 0.971331 | 1.000883 |
| **XPYUSD** | 1.000405 | 1.000105 | 1.000000 | 0.971434 | 1.000988 |
| **XPAX** | 1.029823 | 1.029515 | 1.029406 | 1.000000 | 1.030424 |
| **XUSDT** | 0.999417 | 0.999118 | 0.999013 | 0.970475 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.03 | -0.04 | -2.90 | +0.06 |
| **XUSDC** | +0.03 | +0.00 | -0.01 | -2.87 | +0.09 |
| **XPYUSD** | +0.04 | +0.01 | +0.00 | -2.86 | +0.10 |
| **XPAX** | +2.98 | +2.95 | +2.94 | +0.00 | +3.04 |
| **XUSDT** | -0.06 | -0.09 | -0.10 | -2.95 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.030424** (+3.04% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.029823** (+2.98% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.029515** (+2.95% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.029406** (+2.94% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.000988** (+0.10% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.970475** (-2.95% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.971040** (-2.90% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.971331** (-2.87% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.971434** (-2.86% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.999013** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.0717 | $15,533 | $1,905 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.0879 | $15,293 | $2,507 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.0936 | $15,150 | $356 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6843 | $14,615 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.0402 | $15,108 | $406 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9957 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0030 |
| XPAX | $1.0210 |
| XUSDT | $0.9983 |
