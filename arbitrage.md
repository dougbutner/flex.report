# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-09 22:47 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.001204 | 0.995773 | 1.000355 | 0.963143 |
| **XUSDC** | 0.998797 | 1.000000 | 0.994575 | 0.999152 | 0.961985 |
| **XPYUSD** | 1.004245 | 1.005454 | 1.000000 | 1.004602 | 0.967232 |
| **XPAX** | 0.999645 | 1.000849 | 0.995420 | 1.000000 | 0.962801 |
| **XUSDT** | 1.038267 | 1.039518 | 1.033879 | 1.038636 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.12 | -0.42 | +0.04 | -3.69 |
| **XUSDC** | -0.12 | +0.00 | -0.54 | -0.08 | -3.80 |
| **XPYUSD** | +0.42 | +0.55 | +0.00 | +0.46 | -3.28 |
| **XPAX** | -0.04 | +0.08 | -0.46 | +0.00 | -3.72 |
| **XUSDT** | +3.83 | +3.95 | +3.39 | +3.86 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XUSDC**: **1.039518** (+3.95% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.038636** (+3.86% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.038267** (+3.83% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.033879** (+3.39% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.005454** (+0.55% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.961985** (-3.80% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.962801** (-3.72% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.963143** (-3.69% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.967232** (-3.28% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.994575** (-0.54% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.7839 | $507 | $117 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.7168 | $14,267 | $4,611 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.0207 | $14,180 | $450 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7641 | $14,378 | $621 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 57.9186 | $13,186 | $948 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0003 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0047 |
| XPAX | $1.0073 |
| XUSDT | $1.0000 |
