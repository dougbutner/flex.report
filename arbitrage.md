# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-21 13:38 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999623 | 0.877259 | 0.848174 | 0.996246 |
| **XUSDC** | 1.000377 | 1.000000 | 0.877589 | 0.848494 | 0.996622 |
| **XPYUSD** | 1.139915 | 1.139485 | 1.000000 | 0.966846 | 1.135636 |
| **XPAX** | 1.179004 | 1.178559 | 1.034291 | 1.000000 | 1.174578 |
| **XUSDT** | 1.003768 | 1.003390 | 0.880564 | 0.851370 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.04 | -12.27 | -15.18 | -0.38 |
| **XUSDC** | +0.04 | +0.00 | -12.24 | -15.15 | -0.34 |
| **XPYUSD** | +13.99 | +13.95 | +0.00 | -3.32 | +13.56 |
| **XPAX** | +17.90 | +17.86 | +3.43 | +0.00 | +17.46 |
| **XUSDT** | +0.38 | +0.34 | -11.94 | -14.86 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.179004** (+17.90% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.178559** (+17.86% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.174578** (+17.46% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.139915** (+13.99% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.139485** (+13.95% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.848174** (-15.18% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.848494** (-15.15% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.851370** (-14.86% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.877259** (-12.27% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.877589** (-12.24% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 50.9017 | $17,194 | $14,472 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 50.9209 | $16,862 | $14,219 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 58.0236 | $14,886 | $178 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.0133 | $14,912 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 51.0935 | $16,811 | $3,168 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9899 |
| XUSDC | $1.0000 |
| XPYUSD | $1.1332 |
| XPAX | $1.1636 |
| XUSDT | $1.0031 |
