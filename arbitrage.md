# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-06 18:42 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999857 | 0.999437 | 0.968611 | 0.999070 |
| **XUSDC** | 1.000143 | 1.000000 | 0.999579 | 0.968749 | 0.999213 |
| **XPYUSD** | 1.000564 | 1.000421 | 1.000000 | 0.969156 | 0.999633 |
| **XPAX** | 1.032407 | 1.032259 | 1.031825 | 1.000000 | 1.031447 |
| **XUSDT** | 1.000931 | 1.000788 | 1.000367 | 0.969512 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.01 | -0.06 | -3.14 | -0.09 |
| **XUSDC** | +0.01 | +0.00 | -0.04 | -3.13 | -0.08 |
| **XPYUSD** | +0.06 | +0.04 | +0.00 | -3.08 | -0.04 |
| **XPAX** | +3.24 | +3.23 | +3.18 | +0.00 | +3.14 |
| **XUSDT** | +0.09 | +0.08 | +0.04 | -3.05 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.032407** (+3.24% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.032259** (+3.23% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.031825** (+3.18% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.031447** (+3.14% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.000931** (+0.09% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.968611** (-3.14% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.968749** (-3.13% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.969156** (-3.08% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.969512** (-3.05% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.999070** (-0.09% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.9458 | $15,594 | $1,624 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.9535 | $15,183 | $2,263 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.9762 | $15,198 | $237 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6940 | $14,760 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.9960 | $15,156 | $1,017 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9954 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0021 |
| XPAX | $1.0315 |
| XUSDT | $1.0000 |
