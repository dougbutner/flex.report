# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-29 18:23 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000516 | 1.000531 | 0.975409 | 1.001344 |
| **XUSDC** | 0.999484 | 1.000000 | 1.000015 | 0.974906 | 1.000828 |
| **XPYUSD** | 0.999470 | 0.999985 | 1.000000 | 0.974892 | 1.000813 |
| **XPAX** | 1.025211 | 1.025740 | 1.025755 | 1.000000 | 1.026589 |
| **XUSDT** | 0.998658 | 0.999173 | 0.999188 | 0.974100 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.05 | +0.05 | -2.46 | +0.13 |
| **XUSDC** | -0.05 | +0.00 | +0.00 | -2.51 | +0.08 |
| **XPYUSD** | -0.05 | -0.00 | +0.00 | -2.51 | +0.08 |
| **XPAX** | +2.52 | +2.57 | +2.58 | +0.00 | +2.66 |
| **XUSDT** | -0.13 | -0.08 | -0.08 | -2.59 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.026589** (+2.66% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.025755** (+2.58% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.025740** (+2.57% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.025211** (+2.52% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.001344** (+0.13% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.974100** (-2.59% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.974892** (-2.51% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.974906** (-2.51% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.975409** (-2.46% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.998658** (-0.13% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.3131 | $15,462 | $2,645 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.2851 | $15,188 | $2,601 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.2843 | $15,058 | $598 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6824 | $14,730 | $5 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.2402 | $14,959 | $693 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9994 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0036 |
| XPAX | $1.0290 |
| XUSDT | $0.9954 |
