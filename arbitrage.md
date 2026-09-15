# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-15 17:24 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000139 | 0.999419 | 0.995036 | 1.007246 |
| **XUSDC** | 0.999861 | 1.000000 | 0.999280 | 0.994898 | 1.007106 |
| **XPYUSD** | 1.000582 | 1.000720 | 1.000000 | 0.995614 | 1.007832 |
| **XPAX** | 1.004989 | 1.005128 | 1.004405 | 1.000000 | 1.012271 |
| **XUSDT** | 0.992806 | 0.992944 | 0.992229 | 0.987878 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.01 | -0.06 | -0.50 | +0.72 |
| **XUSDC** | -0.01 | +0.00 | -0.07 | -0.51 | +0.71 |
| **XPYUSD** | +0.06 | +0.07 | +0.00 | -0.44 | +0.78 |
| **XPAX** | +0.50 | +0.51 | +0.44 | +0.00 | +1.23 |
| **XUSDT** | -0.72 | -0.71 | -0.78 | -1.21 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.012271** (+1.23% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.007832** (+0.78% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.007246** (+0.72% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **1.007106** (+0.71% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.005128** (+0.51% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.987878** (-1.21% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.992229** (-0.78% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.992806** (-0.72% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **0.992944** (-0.71% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.994898** (-0.51% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.8390 | $15,090 | $5,054 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.8314 | $14,719 | $2,353 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.8709 | $14,746 | $325 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.1126 | $14,561 | $4 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.4445 | $14,773 | $1,490 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9931 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0032 |
| XPAX | $0.9970 |
| XUSDT | $0.9901 |
