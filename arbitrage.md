# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-01 18:12 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.001017 | 0.982572 | 0.980806 | 0.999282 |
| **XUSDC** | 0.998984 | 1.000000 | 0.981574 | 0.979810 | 0.998268 |
| **XPYUSD** | 1.017737 | 1.018772 | 1.000000 | 0.998203 | 1.017007 |
| **XPAX** | 1.019569 | 1.020606 | 1.001800 | 1.000000 | 1.018838 |
| **XUSDT** | 1.000718 | 1.001735 | 0.983277 | 0.981511 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.10 | -1.74 | -1.92 | -0.07 |
| **XUSDC** | -0.10 | +0.00 | -1.84 | -2.02 | -0.17 |
| **XPYUSD** | +1.77 | +1.88 | +0.00 | -0.18 | +1.70 |
| **XPAX** | +1.96 | +2.06 | +0.18 | +0.00 | +1.88 |
| **XUSDT** | +0.07 | +0.17 | -1.67 | -1.85 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.020606** (+2.06% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.019569** (+1.96% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.018838** (+1.88% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.018772** (+1.88% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.017737** (+1.77% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.979810** (-2.02% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.980806** (-1.92% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.981511** (-1.85% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.981574** (-1.84% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.982572** (-1.74% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.7817 | $518 | $41 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.7281 | $15,840 | $1,672 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.7179 | $15,500 | $87 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 53.8146 | $15,591 | $63 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.8196 | $15,790 | $446 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9952 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0128 |
| XPAX | $1.0200 |
| XUSDT | $1.0000 |
