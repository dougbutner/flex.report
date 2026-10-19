# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-19 18:55 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999813 | 1.000504 | 1.000444 | 0.988570 |
| **XUSDC** | 1.000187 | 1.000000 | 1.000692 | 1.000632 | 0.988755 |
| **XPYUSD** | 0.999496 | 0.999309 | 1.000000 | 0.999940 | 0.988072 |
| **XPAX** | 0.999556 | 0.999369 | 1.000060 | 1.000000 | 0.988131 |
| **XUSDT** | 1.011562 | 1.011373 | 1.012072 | 1.012011 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | +0.05 | +0.04 | -1.14 |
| **XUSDC** | +0.02 | +0.00 | +0.07 | +0.06 | -1.12 |
| **XPYUSD** | -0.05 | -0.07 | +0.00 | -0.01 | -1.19 |
| **XPAX** | -0.04 | -0.06 | +0.01 | +0.00 | -1.19 |
| **XUSDT** | +1.16 | +1.14 | +1.21 | +1.20 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPYUSD**: **1.012072** (+1.21% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.012011** (+1.20% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.011562** (+1.16% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.011373** (+1.14% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **1.000692** (+0.07% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.988072** (-1.19% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.988131** (-1.19% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.988570** (-1.14% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.988755** (-1.12% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **0.999309** (-0.07% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 56.5548 | $14,197 | $1,022 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 56.5654 | $13,844 | $1,324 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.5263 | $13,794 | $210 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.5297 | $13,859 | $198 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 57.2087 | $13,528 | $264 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9914 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9951 |
| XPAX | $0.9977 |
| XUSDT | $1.0000 |
