# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-18 16:50 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999121 | 0.998999 | 0.983087 | 0.997748 |
| **XUSDC** | 1.000880 | 1.000000 | 0.999878 | 0.983953 | 0.998626 |
| **XPYUSD** | 1.001002 | 1.000122 | 1.000000 | 0.984073 | 0.998748 |
| **XPAX** | 1.017204 | 1.016309 | 1.016185 | 1.000000 | 1.014913 |
| **XUSDT** | 1.002257 | 1.001376 | 1.001253 | 0.985306 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.09 | -0.10 | -1.69 | -0.23 |
| **XUSDC** | +0.09 | +0.00 | -0.01 | -1.60 | -0.14 |
| **XPYUSD** | +0.10 | +0.01 | +0.00 | -1.59 | -0.13 |
| **XPAX** | +1.72 | +1.63 | +1.62 | +0.00 | +1.49 |
| **XUSDT** | +0.23 | +0.14 | +0.13 | -1.47 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.017204** (+1.72% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.016309** (+1.63% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.016185** (+1.62% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.014913** (+1.49% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.002257** (+0.23% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.983087** (-1.69% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.983953** (-1.60% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.984073** (-1.59% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.985306** (-1.47% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.997748** (-0.23% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.7676 | $14,900 | $4,601 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.8158 | $14,728 | $4,718 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.8225 | $14,872 | $337 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7098 | $14,375 | $51 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.8912 | $14,444 | $2,226 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9782 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0101 |
| XPAX | $1.0052 |
| XUSDT | $0.9833 |
