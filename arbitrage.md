# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-29 18:44 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999653 | 0.972418 | 0.963563 | 0.997237 |
| **XUSDC** | 1.000348 | 1.000000 | 0.972756 | 0.963898 | 0.997584 |
| **XPYUSD** | 1.028364 | 1.028007 | 1.000000 | 0.990894 | 1.025523 |
| **XPAX** | 1.037815 | 1.037454 | 1.009190 | 1.000000 | 1.034947 |
| **XUSDT** | 1.002771 | 1.002422 | 0.975112 | 0.966233 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.03 | -2.76 | -3.64 | -0.28 |
| **XUSDC** | +0.03 | +0.00 | -2.72 | -3.61 | -0.24 |
| **XPYUSD** | +2.84 | +2.80 | +0.00 | -0.91 | +2.55 |
| **XPAX** | +3.78 | +3.75 | +0.92 | +0.00 | +3.49 |
| **XUSDT** | +0.28 | +0.24 | -2.49 | -3.38 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.037815** (+3.78% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.037454** (+3.75% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.034947** (+3.49% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.028364** (+2.84% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.028007** (+2.80% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.963563** (-3.64% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.963898** (-3.61% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.966233** (-3.38% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.972418** (-2.76% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.972756** (-2.72% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.0829 | $557 | $262 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.1010 | $16,188 | $3,912 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.5602 | $15,821 | $312 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.0524 | $15,717 | $124 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.2272 | $16,117 | $935 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9901 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0281 |
| XPAX | $1.0369 |
| XUSDT | $1.0000 |
