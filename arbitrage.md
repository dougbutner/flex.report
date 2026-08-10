# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-10 14:15 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000224 | 0.999293 | 0.990454 | 0.981583 |
| **XUSDC** | 0.999776 | 1.000000 | 0.999069 | 0.990232 | 0.981364 |
| **XPYUSD** | 1.000708 | 1.000932 | 1.000000 | 0.991155 | 0.982278 |
| **XPAX** | 1.009638 | 1.009864 | 1.008924 | 1.000000 | 0.991044 |
| **XUSDT** | 1.018762 | 1.018990 | 1.018042 | 1.009037 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.02 | -0.07 | -0.95 | -1.84 |
| **XUSDC** | -0.02 | +0.00 | -0.09 | -0.98 | -1.86 |
| **XPYUSD** | +0.07 | +0.09 | +0.00 | -0.88 | -1.77 |
| **XPAX** | +0.96 | +0.99 | +0.89 | +0.00 | -0.90 |
| **XUSDT** | +1.88 | +1.90 | +1.80 | +0.90 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XUSDC**: **1.018990** (+1.90% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.018762** (+1.88% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.018042** (+1.80% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.009864** (+0.99% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.009638** (+0.96% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.981364** (-1.86% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.981583** (-1.84% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.982278** (-1.77% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.990232** (-0.98% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.990454** (-0.95% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.4813 | $12,210 | $2,229 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.4680 | $12,462 | $2,852 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.5234 | $12,505 | $320 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0546 | $12,653 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.5973 | $12,190 | $1,425 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9803 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0055 |
| XPAX | $0.9888 |
| XUSDT | $1.0199 |
