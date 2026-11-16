# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-16 22:40 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000785 | 1.000670 | 1.005277 | 0.992438 |
| **XUSDC** | 0.999215 | 1.000000 | 0.999884 | 1.004488 | 0.991659 |
| **XPYUSD** | 0.999331 | 1.000116 | 1.000000 | 1.004604 | 0.991774 |
| **XPAX** | 0.994751 | 0.995532 | 0.995417 | 1.000000 | 0.987229 |
| **XUSDT** | 1.007619 | 1.008411 | 1.008294 | 1.012936 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.08 | +0.07 | +0.53 | -0.76 |
| **XUSDC** | -0.08 | +0.00 | -0.01 | +0.45 | -0.83 |
| **XPYUSD** | -0.07 | +0.01 | +0.00 | +0.46 | -0.82 |
| **XPAX** | -0.52 | -0.45 | -0.46 | +0.00 | -1.28 |
| **XUSDT** | +0.76 | +0.84 | +0.83 | +1.29 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPAX**: **1.012936** (+1.29% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.008411** (+0.84% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.008294** (+0.83% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.007619** (+0.76% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.005277** (+0.53% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.987229** (-1.28% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.991659** (-0.83% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.991774** (-0.82% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.992438** (-0.76% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.994751** (-0.52% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 57.9719 | $479 | $62 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 57.9264 | $13,182 | $1,899 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 57.9331 | $13,158 | $344 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 57.6676 | $13,392 | $260 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 58.4136 | $12,951 | $806 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9626 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9984 |
| XPAX | $1.0041 |
| XUSDT | $1.0000 |
