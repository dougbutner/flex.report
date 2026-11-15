# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-15 19:12 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999803 | 0.998743 | 0.999129 | 0.998364 |
| **XUSDC** | 1.000197 | 1.000000 | 0.998939 | 0.999325 | 0.998560 |
| **XPYUSD** | 1.001259 | 1.001062 | 1.000000 | 1.000387 | 0.999621 |
| **XPAX** | 1.000872 | 1.000675 | 0.999614 | 1.000000 | 0.999235 |
| **XUSDT** | 1.001639 | 1.001442 | 1.000379 | 1.000766 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -0.13 | -0.09 | -0.16 |
| **XUSDC** | +0.02 | +0.00 | -0.11 | -0.07 | -0.14 |
| **XPYUSD** | +0.13 | +0.11 | +0.00 | +0.04 | -0.04 |
| **XPAX** | +0.09 | +0.07 | -0.04 | +0.00 | -0.08 |
| **XUSDT** | +0.16 | +0.14 | +0.04 | +0.08 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XMD**: **1.001639** (+0.16% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.001442** (+0.14% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.001259** (+0.13% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.001062** (+0.11% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.000872** (+0.09% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.998364** (-0.16% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.998560** (-0.14% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.998743** (-0.13% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.998939** (-0.11% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.999129** (-0.09% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 56.8689 | $489 | $288 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 56.8801 | $13,689 | $6,559 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.9405 | $13,662 | $576 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.9185 | $13,753 | $989 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.9621 | $13,648 | $3,056 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9744 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0003 |
| XPAX | $1.0039 |
| XUSDT | $1.0000 |
