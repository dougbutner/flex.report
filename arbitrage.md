# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-01 18:38 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999927 | 1.000411 | 0.978019 | 1.001565 |
| **XUSDC** | 1.000073 | 1.000000 | 1.000485 | 0.978091 | 1.001639 |
| **XPYUSD** | 0.999589 | 0.999515 | 1.000000 | 0.977617 | 1.001153 |
| **XPAX** | 1.022475 | 1.022400 | 1.022896 | 1.000000 | 1.024075 |
| **XUSDT** | 0.998437 | 0.998364 | 0.998848 | 0.976491 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.01 | +0.04 | -2.20 | +0.16 |
| **XUSDC** | +0.01 | +0.00 | +0.05 | -2.19 | +0.16 |
| **XPYUSD** | -0.04 | -0.05 | +0.00 | -2.24 | +0.12 |
| **XPAX** | +2.25 | +2.24 | +2.29 | +0.00 | +2.41 |
| **XUSDT** | -0.16 | -0.16 | -0.12 | -2.35 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.024075** (+2.41% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.022896** (+2.29% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.022475** (+2.25% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.022400** (+2.24% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **1.001639** (+0.16% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.976491** (-2.35% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.977617** (-2.24% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.978019** (-2.20% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.978091** (-2.19% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **0.998364** (-0.16% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.4605 | $15,298 | $2,045 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.4645 | $14,912 | $1,527 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.4381 | $14,950 | $210 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6845 | $14,530 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.3754 | $14,936 | $521 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9938 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0018 |
| XPAX | $1.0151 |
| XUSDT | $0.9986 |
