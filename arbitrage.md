# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-05 15:09 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000041 | 0.995013 | 0.979250 | 0.980784 |
| **XUSDC** | 0.999959 | 1.000000 | 0.994972 | 0.979210 | 0.980744 |
| **XPYUSD** | 1.005012 | 1.005053 | 1.000000 | 0.984158 | 0.985699 |
| **XPAX** | 1.021190 | 1.021232 | 1.016097 | 1.000000 | 1.001567 |
| **XUSDT** | 1.019593 | 1.019634 | 1.014508 | 0.998436 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.00 | -0.50 | -2.08 | -1.92 |
| **XUSDC** | -0.00 | +0.00 | -0.50 | -2.08 | -1.93 |
| **XPYUSD** | +0.50 | +0.51 | +0.00 | -1.58 | -1.43 |
| **XPAX** | +2.12 | +2.12 | +1.61 | +0.00 | +0.16 |
| **XUSDT** | +1.96 | +1.96 | +1.45 | -0.16 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.021232** (+2.12% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.021190** (+2.12% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.019634** (+1.96% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.019593** (+1.96% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.016097** (+1.61% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.979210** (-2.08% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.979250** (-2.08% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.980744** (-1.93% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.980784** (-1.92% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.984158** (-1.58% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 59.0368 | $12,548 | $1,454 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 59.0344 | $12,662 | $2,106 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 59.3327 | $12,656 | $4 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.2878 | $13,001 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.1935 | $12,388 | $1,280 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9911 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0106 |
| XPAX | $1.0245 |
| XUSDT | $1.0211 |
