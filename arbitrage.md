# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-05 15:43 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999761 | 0.999563 | 0.965142 | 1.000597 |
| **XUSDC** | 1.000239 | 1.000000 | 0.999801 | 0.965372 | 1.000836 |
| **XPYUSD** | 1.000437 | 1.000199 | 1.000000 | 0.965564 | 1.001035 |
| **XPAX** | 1.036117 | 1.035870 | 1.035664 | 1.000000 | 1.036736 |
| **XUSDT** | 0.999404 | 0.999165 | 0.998967 | 0.964566 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -0.04 | -3.49 | +0.06 |
| **XUSDC** | +0.02 | +0.00 | -0.02 | -3.46 | +0.08 |
| **XPYUSD** | +0.04 | +0.02 | +0.00 | -3.44 | +0.10 |
| **XPAX** | +3.61 | +3.59 | +3.57 | +0.00 | +3.67 |
| **XUSDT** | -0.06 | -0.08 | -0.10 | -3.54 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.036736** (+3.67% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.036117** (+3.61% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.035870** (+3.59% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.035664** (+3.57% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.001035** (+0.10% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.964566** (-3.54% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.965142** (-3.49% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.965372** (-3.46% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.965564** (-3.44% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.998967** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.8086 | $16,178 | $1,267 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.8212 | $16,045 | $1,468 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.8317 | $15,917 | $71 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7159 | $15,293 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.7771 | $15,677 | $215 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9934 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0085 |
| XPAX | $1.0326 |
| XUSDT | $0.9914 |
