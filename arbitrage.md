# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-15 17:31 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000747 | 0.999747 | 1.000316 | 0.993466 |
| **XUSDC** | 0.999254 | 1.000000 | 0.999001 | 0.999569 | 0.992724 |
| **XPYUSD** | 1.000253 | 1.001000 | 1.000000 | 1.000569 | 0.993717 |
| **XPAX** | 0.999684 | 1.000431 | 0.999431 | 1.000000 | 0.993152 |
| **XUSDT** | 1.006577 | 1.007329 | 1.006323 | 1.006895 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | -0.03 | +0.03 | -0.65 |
| **XUSDC** | -0.07 | +0.00 | -0.10 | -0.04 | -0.73 |
| **XPYUSD** | +0.03 | +0.10 | +0.00 | +0.06 | -0.63 |
| **XPAX** | -0.03 | +0.04 | -0.06 | +0.00 | -0.68 |
| **XUSDT** | +0.66 | +0.73 | +0.63 | +0.69 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XUSDC**: **1.007329** (+0.73% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.006895** (+0.69% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.006577** (+0.66% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.006323** (+0.63% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.001000** (+0.10% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.992724** (-0.73% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.993152** (-0.68% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.993466** (-0.65% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.993717** (-0.63% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.999001** (-0.10% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.7373 | $14,770 | $1,445 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.6957 | $14,278 | $2,153 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.7514 | $14,366 | $227 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7197 | $14,437 | $28 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.1039 | $14,072 | $1,118 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0026 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0082 |
| XPAX | $1.0099 |
| XUSDT | $1.0000 |
