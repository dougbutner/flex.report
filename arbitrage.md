# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-08 13:39 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999481 | 0.999555 | 0.987081 | 0.988457 |
| **XUSDC** | 1.000520 | 1.000000 | 1.000074 | 0.987594 | 0.988971 |
| **XPYUSD** | 1.000445 | 0.999926 | 1.000000 | 0.987521 | 0.988898 |
| **XPAX** | 1.013088 | 1.012562 | 1.012637 | 1.000000 | 1.001394 |
| **XUSDT** | 1.011677 | 1.011152 | 1.011227 | 0.998608 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -0.04 | -1.29 | -1.15 |
| **XUSDC** | +0.05 | +0.00 | +0.01 | -1.24 | -1.10 |
| **XPYUSD** | +0.04 | -0.01 | +0.00 | -1.25 | -1.11 |
| **XPAX** | +1.31 | +1.26 | +1.26 | +0.00 | +0.14 |
| **XUSDT** | +1.17 | +1.12 | +1.12 | -0.14 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.013088** (+1.31% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.012637** (+1.26% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.012562** (+1.26% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.011677** (+1.17% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.011227** (+1.12% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.987081** (-1.29% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.987521** (-1.25% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.987594** (-1.24% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.988457** (-1.15% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.988898** (-1.11% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.2773 | $12,500 | $2,598 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.3081 | $12,535 | $1,695 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.3037 | $12,636 | $168 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0531 | $12,863 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 59.9695 | $12,362 | $1,302 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9960 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0079 |
| XPAX | $1.0051 |
| XUSDT | $1.0105 |
