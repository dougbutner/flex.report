# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-27 17:22 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000695 | 1.000266 | 0.967057 | 1.002239 |
| **XUSDC** | 0.999305 | 1.000000 | 0.999571 | 0.966386 | 1.001543 |
| **XPYUSD** | 0.999734 | 1.000429 | 1.000000 | 0.966801 | 1.001973 |
| **XPAX** | 1.034065 | 1.034783 | 1.034339 | 1.000000 | 1.036380 |
| **XUSDT** | 0.997766 | 0.998459 | 0.998031 | 0.964897 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | +0.03 | -3.29 | +0.22 |
| **XUSDC** | -0.07 | +0.00 | -0.04 | -3.36 | +0.15 |
| **XPYUSD** | -0.03 | +0.04 | +0.00 | -3.32 | +0.20 |
| **XPAX** | +3.41 | +3.48 | +3.43 | +0.00 | +3.64 |
| **XUSDT** | -0.22 | -0.15 | -0.20 | -3.51 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.036380** (+3.64% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.034783** (+3.48% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.034339** (+3.43% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.034065** (+3.41% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.002239** (+0.22% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.964897** (-3.51% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.966386** (-3.36% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.966801** (-3.32% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.967057** (-3.29% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.997766** (-0.22% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.8446 | $15,697 | $2,340 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.8072 | $15,258 | $3,084 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.8303 | $15,393 | $482 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6788 | $14,831 | $2 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.7243 | $15,196 | $1,882 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9984 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0097 |
| XPAX | $1.0359 |
| XUSDT | $0.9931 |
