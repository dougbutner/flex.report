# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-06 15:07 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000869 | 0.995300 | 0.979724 | 0.992290 |
| **XUSDC** | 0.999131 | 1.000000 | 0.994436 | 0.978873 | 0.991429 |
| **XPYUSD** | 1.004722 | 1.005595 | 1.000000 | 0.984350 | 0.996976 |
| **XPAX** | 1.020696 | 1.021583 | 1.015899 | 1.000000 | 1.012827 |
| **XUSDT** | 1.007769 | 1.008645 | 1.003033 | 0.987336 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.09 | -0.47 | -2.03 | -0.77 |
| **XUSDC** | -0.09 | +0.00 | -0.56 | -2.11 | -0.86 |
| **XPYUSD** | +0.47 | +0.56 | +0.00 | -1.57 | -0.30 |
| **XPAX** | +2.07 | +2.16 | +1.59 | +0.00 | +1.28 |
| **XUSDT** | +0.78 | +0.86 | +0.30 | -1.27 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.021583** (+2.16% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.020696** (+2.07% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.015899** (+1.59% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.012827** (+1.28% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.008645** (+0.86% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.978873** (-2.11% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.979724** (-2.03% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.984350** (-1.57% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.987336** (-1.27% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.991429** (-0.86% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.0648 | $12,477 | $2,733 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.0135 | $12,672 | $3,004 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.3437 | $12,644 | $371 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.2872 | $13,007 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 59.5237 | $12,570 | $882 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9865 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0100 |
| XPAX | $1.0249 |
| XUSDT | $1.0093 |
