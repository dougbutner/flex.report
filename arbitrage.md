# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-12 21:29 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000022 | 1.000100 | 0.990949 | 0.987620 |
| **XUSDC** | 0.999978 | 1.000000 | 1.000078 | 0.990928 | 0.987599 |
| **XPYUSD** | 0.999900 | 0.999922 | 1.000000 | 0.990851 | 0.987522 |
| **XPAX** | 1.009133 | 1.009155 | 1.009234 | 1.000000 | 0.996640 |
| **XUSDT** | 1.012535 | 1.012557 | 1.012636 | 1.003371 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.00 | +0.01 | -0.91 | -1.24 |
| **XUSDC** | -0.00 | +0.00 | +0.01 | -0.91 | -1.24 |
| **XPYUSD** | -0.01 | -0.01 | +0.00 | -0.91 | -1.25 |
| **XPAX** | +0.91 | +0.92 | +0.92 | +0.00 | -0.34 |
| **XUSDT** | +1.25 | +1.26 | +1.26 | +0.34 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPYUSD**: **1.012636** (+1.26% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.012557** (+1.26% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.012535** (+1.25% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.009234** (+0.92% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.009155** (+0.92% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.987522** (-1.25% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.987599** (-1.24% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.987620** (-1.24% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.990851** (-0.91% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.990928** (-0.91% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 55.2049 | $15,025 | $1,110 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 55.2037 | $14,528 | $2,507 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.1994 | $14,580 | $212 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.7091 | $14,448 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 55.8969 | $14,176 | $1,051 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0013 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0035 |
| XPAX | $1.0103 |
| XUSDT | $1.0000 |
