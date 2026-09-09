# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-09 16:57 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000723 | 1.000883 | 0.958645 | 1.000441 |
| **XUSDC** | 0.999277 | 1.000000 | 1.000160 | 0.957953 | 0.999718 |
| **XPYUSD** | 0.999117 | 0.999840 | 1.000000 | 0.957799 | 0.999558 |
| **XPAX** | 1.043139 | 1.043893 | 1.044060 | 1.000000 | 1.043598 |
| **XUSDT** | 0.999560 | 1.000282 | 1.000443 | 0.958223 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | +0.09 | -4.14 | +0.04 |
| **XUSDC** | -0.07 | +0.00 | +0.02 | -4.20 | -0.03 |
| **XPYUSD** | -0.09 | -0.02 | +0.00 | -4.22 | -0.04 |
| **XPAX** | +4.31 | +4.39 | +4.41 | +0.00 | +4.36 |
| **XUSDT** | -0.04 | +0.03 | +0.04 | -4.18 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XPYUSD**: **1.044060** (+4.41% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.043893** (+4.39% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.043598** (+4.36% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.043139** (+4.31% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **1.000883** (+0.09% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.957799** (-4.22% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.957953** (-4.20% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.958223** (-4.18% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.958645** (-4.14% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **0.999117** (-0.09% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.4564 | $16,469 | $2,603 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.4185 | $17,649 | $1,563 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.4101 | $16,123 | $680 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7193 | $15,413 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.4333 | $15,979 | $397 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9994 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0067 |
| XPAX | $1.0408 |
| XUSDT | $0.9986 |
