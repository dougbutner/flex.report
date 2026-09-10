# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-10 16:47 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000878 | 1.000998 | 0.971345 | 1.001145 |
| **XUSDC** | 0.999123 | 1.000000 | 1.000121 | 0.970493 | 1.000267 |
| **XPYUSD** | 0.999003 | 0.999879 | 1.000000 | 0.970376 | 1.000147 |
| **XPAX** | 1.029501 | 1.030404 | 1.030528 | 1.000000 | 1.030680 |
| **XUSDT** | 0.998856 | 0.999733 | 0.999853 | 0.970234 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.09 | +0.10 | -2.87 | +0.11 |
| **XUSDC** | -0.09 | +0.00 | +0.01 | -2.95 | +0.03 |
| **XPYUSD** | -0.10 | -0.01 | +0.00 | -2.96 | +0.01 |
| **XPAX** | +2.95 | +3.04 | +3.05 | +0.00 | +3.07 |
| **XUSDT** | -0.11 | -0.03 | -0.01 | -2.98 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.030680** (+3.07% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.030528** (+3.05% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.030404** (+3.04% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.029501** (+2.95% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.001145** (+0.11% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.970234** (-2.98% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.970376** (-2.96% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.970493** (-2.95% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.971345** (-2.87% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.998856** (-0.11% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.1516 | $15,788 | $2,706 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.1050 | $15,916 | $3,747 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.0986 | $15,742 | $187 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7196 | $15,412 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.0908 | $15,427 | $523 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9809 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0067 |
| XPAX | $1.0408 |
| XUSDT | $0.9863 |
