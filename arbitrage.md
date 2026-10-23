# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-23 17:38 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000442 | 0.968913 | 0.971115 | 0.989522 |
| **XUSDC** | 0.999558 | 1.000000 | 0.968485 | 0.970686 | 0.989085 |
| **XPYUSD** | 1.032084 | 1.032540 | 1.000000 | 1.002272 | 1.021270 |
| **XPAX** | 1.029744 | 1.030199 | 0.997733 | 1.000000 | 1.018954 |
| **XUSDT** | 1.010589 | 1.011035 | 0.979173 | 0.981398 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.04 | -3.11 | -2.89 | -1.05 |
| **XUSDC** | -0.04 | +0.00 | -3.15 | -2.93 | -1.09 |
| **XPYUSD** | +3.21 | +3.25 | +0.00 | +0.23 | +2.13 |
| **XPAX** | +2.97 | +3.02 | -0.23 | +0.00 | +1.90 |
| **XUSDT** | +1.06 | +1.10 | -2.08 | -1.86 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPYUSD** → buy **XUSDC**: **1.032540** (+3.25% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.032084** (+3.21% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.030199** (+3.02% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.029744** (+2.97% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.021270** (+2.13% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.968485** (-3.15% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.968913** (-3.11% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.970686** (-2.93% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.971115** (-2.89% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.979173** (-2.08% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.7845 | $15,194 | $1,610 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.7603 | $14,760 | $3,750 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.5422 | $14,169 | $55 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.4140 | $14,345 | $3 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.3646 | $14,447 | $1,257 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9979 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0227 |
| XPAX | $1.0284 |
| XUSDT | $1.0000 |
