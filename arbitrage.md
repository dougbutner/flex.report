# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-21 17:48 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999816 | 0.953018 | 0.955214 | 0.955763 |
| **XUSDC** | 1.000184 | 1.000000 | 0.953193 | 0.955390 | 0.955939 |
| **XPYUSD** | 1.049299 | 1.049106 | 1.000000 | 1.002305 | 1.002881 |
| **XPAX** | 1.046886 | 1.046693 | 0.997700 | 1.000000 | 1.000575 |
| **XUSDT** | 1.046284 | 1.046092 | 0.997127 | 0.999426 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -4.70 | -4.48 | -4.42 |
| **XUSDC** | +0.02 | +0.00 | -4.68 | -4.46 | -4.41 |
| **XPYUSD** | +4.93 | +4.91 | +0.00 | +0.23 | +0.29 |
| **XPAX** | +4.69 | +4.67 | -0.23 | +0.00 | +0.06 |
| **XUSDT** | +4.63 | +4.61 | -0.29 | -0.06 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XMD**: **1.049299** (+4.93% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.049106** (+4.91% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.046886** (+4.69% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.046693** (+4.67% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.046284** (+4.63% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.953018** (-4.70% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.953193** (-4.68% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.955214** (-4.48% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.955390** (-4.46% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.955763** (-4.42% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.8758 | $15,415 | $3,697 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.8857 | $15,218 | $4,907 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.5318 | $14,680 | $266 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.4018 | $14,506 | $16 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.3694 | $13,940 | $1,740 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9814 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0592 |
| XPAX | $1.0395 |
| XUSDT | $1.0000 |
