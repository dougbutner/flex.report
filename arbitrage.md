# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-07-28 16:59 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999526 | 0.975312 | 0.945984 | 1.000276 |
| **XUSDC** | 1.000475 | 1.000000 | 0.975775 | 0.946433 | 1.000751 |
| **XPYUSD** | 1.025313 | 1.024827 | 1.000000 | 0.969930 | 1.025596 |
| **XPAX** | 1.057100 | 1.056599 | 1.031003 | 1.000000 | 1.057392 |
| **XUSDT** | 0.999724 | 0.999250 | 0.975043 | 0.945723 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -2.47 | -5.40 | +0.03 |
| **XUSDC** | +0.05 | +0.00 | -2.42 | -5.36 | +0.08 |
| **XPYUSD** | +2.53 | +2.48 | +0.00 | -3.01 | +2.56 |
| **XPAX** | +5.71 | +5.66 | +3.10 | +0.00 | +5.74 |
| **XUSDT** | -0.03 | -0.08 | -2.50 | -5.43 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.057392** (+5.74% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.057100** (+5.71% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.056599** (+5.66% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.031003** (+3.10% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.025596** (+2.56% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.945723** (-5.43% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.945984** (-5.40% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.946433** (-5.36% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.969930** (-3.01% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.975043** (-2.50% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 60.9014 | $11,765 | $5,360 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 60.9303 | $11,806 | $7,149 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 62.4430 | $11,381 | $36 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 64.3789 | $11,462 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.8846 | $11,588 | $1,930 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9798 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0209 |
| XPAX | $1.0411 |
| XUSDT | $0.9800 |
