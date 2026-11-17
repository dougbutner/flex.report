# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-17 21:28 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000597 | 1.000869 | 1.005644 | 0.999088 |
| **XUSDC** | 0.999404 | 1.000000 | 1.000273 | 1.005044 | 0.998492 |
| **XPYUSD** | 0.999131 | 0.999727 | 1.000000 | 1.004770 | 0.998220 |
| **XPAX** | 0.994388 | 0.994981 | 0.995252 | 1.000000 | 0.993481 |
| **XUSDT** | 1.000913 | 1.001510 | 1.001783 | 1.006562 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.06 | +0.09 | +0.56 | -0.09 |
| **XUSDC** | -0.06 | +0.00 | +0.03 | +0.50 | -0.15 |
| **XPYUSD** | -0.09 | -0.03 | +0.00 | +0.48 | -0.18 |
| **XPAX** | -0.56 | -0.50 | -0.47 | +0.00 | -0.65 |
| **XUSDT** | +0.09 | +0.15 | +0.18 | +0.66 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPAX**: **1.006562** (+0.66% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.005644** (+0.56% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **1.005044** (+0.50% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **1.004770** (+0.48% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.001783** (+0.18% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.993481** (-0.65% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.994388** (-0.56% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **0.994981** (-0.50% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **0.995252** (-0.47% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.998220** (-0.18% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 58.3724 | $527 | $35 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 58.3376 | $12,987 | $1,652 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 58.3217 | $12,991 | $219 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 58.0448 | $13,208 | $119 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 58.4257 | $12,946 | $396 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9695 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9997 |
| XPAX | $1.0039 |
| XUSDT | $1.0000 |
