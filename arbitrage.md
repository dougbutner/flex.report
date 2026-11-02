# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-11-02 22:02 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000914 | 0.998921 | 0.995507 | 0.998394 |
| **XUSDC** | 0.999086 | 1.000000 | 0.998009 | 0.994597 | 0.997482 |
| **XPYUSD** | 1.001080 | 1.001995 | 1.000000 | 0.996582 | 0.999472 |
| **XPAX** | 1.004514 | 1.005432 | 1.003430 | 1.000000 | 1.002900 |
| **XUSDT** | 1.001609 | 1.002524 | 1.000528 | 0.997108 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.09 | -0.11 | -0.45 | -0.16 |
| **XUSDC** | -0.09 | +0.00 | -0.20 | -0.54 | -0.25 |
| **XPYUSD** | +0.11 | +0.20 | +0.00 | -0.34 | -0.05 |
| **XPAX** | +0.45 | +0.54 | +0.34 | +0.00 | +0.29 |
| **XUSDT** | +0.16 | +0.25 | +0.05 | -0.29 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.005432** (+0.54% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.004514** (+0.45% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.003430** (+0.34% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.002900** (+0.29% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.002524** (+0.25% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.994597** (-0.54% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.995507** (-0.45% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.996582** (-0.34% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.997108** (-0.29% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.997482** (-0.25% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.5281 | $517 | $191 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.4792 | $15,432 | $1,443 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.5859 | $15,499 | $367 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 53.7697 | $15,546 | $3 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.6142 | $15,360 | $588 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0005 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0080 |
| XPAX | $1.0156 |
| XUSDT | $1.0000 |
