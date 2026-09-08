# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-08 16:57 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999120 | 0.999070 | 0.956337 | 0.997465 |
| **XUSDC** | 1.000881 | 1.000000 | 0.999950 | 0.957179 | 0.998344 |
| **XPYUSD** | 1.000931 | 1.000050 | 1.000000 | 0.957227 | 0.998393 |
| **XPAX** | 1.045657 | 1.044736 | 1.044684 | 1.000000 | 1.043006 |
| **XUSDT** | 1.002542 | 1.001659 | 1.001609 | 0.958767 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.09 | -0.09 | -4.37 | -0.25 |
| **XUSDC** | +0.09 | +0.00 | -0.00 | -4.28 | -0.17 |
| **XPYUSD** | +0.09 | +0.00 | +0.00 | -4.28 | -0.16 |
| **XPAX** | +4.57 | +4.47 | +4.47 | +0.00 | +4.30 |
| **XUSDT** | +0.25 | +0.17 | +0.16 | -4.12 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.045657** (+4.57% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.044736** (+4.47% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.044684** (+4.47% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.043006** (+4.30% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.002542** (+0.25% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.956337** (-4.37% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.957179** (-4.28% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.957227** (-4.28% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.958767** (-4.12% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.997465** (-0.25% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.3297 | $17,532 | $5,192 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.3758 | $16,237 | $3,074 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.3784 | $16,149 | $228 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7189 | $15,413 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.4627 | $16,003 | $423 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9998 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0072 |
| XPAX | $1.0408 |
| XUSDT | $1.0011 |
