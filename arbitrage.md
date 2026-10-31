# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-31 17:27 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000733 | 0.983604 | 0.982037 | 0.998647 |
| **XUSDC** | 0.999267 | 1.000000 | 0.982884 | 0.981318 | 0.997915 |
| **XPYUSD** | 1.016669 | 1.017415 | 1.000000 | 0.998407 | 1.015293 |
| **XPAX** | 1.018291 | 1.019038 | 1.001596 | 1.000000 | 1.016913 |
| **XUSDT** | 1.001355 | 1.002089 | 0.984937 | 0.983368 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | -1.64 | -1.80 | -0.14 |
| **XUSDC** | -0.07 | +0.00 | -1.71 | -1.87 | -0.21 |
| **XPYUSD** | +1.67 | +1.74 | +0.00 | -0.16 | +1.53 |
| **XPAX** | +1.83 | +1.90 | +0.16 | +0.00 | +1.69 |
| **XUSDT** | +0.14 | +0.21 | -1.51 | -1.66 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.019038** (+1.90% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.018291** (+1.83% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.017415** (+1.74% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.016913** (+1.69% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.016669** (+1.67% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.981318** (-1.87% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.982037** (-1.80% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.982884** (-1.71% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.983368** (-1.66% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.983604** (-1.64% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.0751 | $527 | $36 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.0362 | $15,672 | $2,568 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.9598 | $15,321 | $5 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.0459 | $15,465 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.1470 | $15,611 | $540 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9948 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0096 |
| XPAX | $1.0200 |
| XUSDT | $1.0000 |
