# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-30 17:05 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999510 | 0.999297 | 0.965956 | 0.998225 |
| **XUSDC** | 1.000490 | 1.000000 | 0.999786 | 0.966429 | 0.998714 |
| **XPYUSD** | 1.000704 | 1.000214 | 1.000000 | 0.966636 | 0.998927 |
| **XPAX** | 1.035244 | 1.034737 | 1.034516 | 1.000000 | 1.033406 |
| **XUSDT** | 1.001779 | 1.001288 | 1.001074 | 0.967674 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.05 | -0.07 | -3.40 | -0.18 |
| **XUSDC** | +0.05 | +0.00 | -0.02 | -3.36 | -0.13 |
| **XPYUSD** | +0.07 | +0.02 | +0.00 | -3.34 | -0.11 |
| **XPAX** | +3.52 | +3.47 | +3.45 | +0.00 | +3.34 |
| **XUSDT** | +0.18 | +0.13 | +0.11 | -3.23 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.035244** (+3.52% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.034737** (+3.47% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.034516** (+3.45% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.033406** (+3.34% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.001779** (+0.18% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.965956** (-3.40% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.966429** (-3.36% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.966636** (-3.34% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.967674** (-3.23% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.998225** (-0.18% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.8517 | $16,132 | $1,228 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.8776 | $16,497 | $965 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.8889 | $15,888 | $307 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7144 | $15,416 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.9457 | $15,726 | $171 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9921 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0087 |
| XPAX | $1.0408 |
| XUSDT | $1.0003 |
