# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-11 17:51 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999406 | 0.999453 | 0.978067 | 0.997476 |
| **XUSDC** | 1.000595 | 1.000000 | 1.000048 | 0.978648 | 0.998069 |
| **XPYUSD** | 1.000547 | 0.999952 | 1.000000 | 0.978602 | 0.998021 |
| **XPAX** | 1.022425 | 1.021818 | 1.021866 | 1.000000 | 1.019844 |
| **XUSDT** | 1.002531 | 1.001935 | 1.001983 | 0.980542 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.06 | -0.05 | -2.19 | -0.25 |
| **XUSDC** | +0.06 | +0.00 | +0.00 | -2.14 | -0.19 |
| **XPYUSD** | +0.05 | -0.00 | +0.00 | -2.14 | -0.20 |
| **XPAX** | +2.24 | +2.18 | +2.19 | +0.00 | +1.98 |
| **XUSDT** | +0.25 | +0.19 | +0.20 | -1.95 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.022425** (+2.24% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.021866** (+2.19% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.021818** (+2.18% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.019844** (+1.98% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.002531** (+0.25% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.978067** (-2.19% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.978602** (-2.14% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.978648** (-2.14% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.980542** (-1.95% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.997476** (-0.25% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.4877 | $15,147 | $872 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.5201 | $14,881 | $982 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.5175 | $14,805 | $144 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7096 | $14,546 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.6256 | $14,826 | $522 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9850 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9948 |
| XPAX | $1.0171 |
| XUSDT | $1.0000 |
