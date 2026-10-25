# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-25 16:55 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000163 | 0.888928 | 0.886283 | 0.936633 |
| **XUSDC** | 0.999837 | 1.000000 | 0.888783 | 0.886139 | 0.936480 |
| **XPYUSD** | 1.124950 | 1.125134 | 1.000000 | 0.997024 | 1.053665 |
| **XPAX** | 1.128308 | 1.128492 | 1.002985 | 1.000000 | 1.056810 |
| **XUSDT** | 1.067654 | 1.067829 | 0.949068 | 0.946244 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.02 | -11.11 | -11.37 | -6.34 |
| **XUSDC** | -0.02 | +0.00 | -11.12 | -11.39 | -6.35 |
| **XPYUSD** | +12.50 | +12.51 | +0.00 | -0.30 | +5.37 |
| **XPAX** | +12.83 | +12.85 | +0.30 | +0.00 | +5.68 |
| **XUSDT** | +6.77 | +6.78 | -5.09 | -5.38 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.128492** (+12.85% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.128308** (+12.83% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.125134** (+12.51% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.124950** (+12.50% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.067829** (+6.78% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.886139** (-11.39% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.886283** (-11.37% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.888783** (-11.12% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.888928** (-11.11% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.936480** (-6.35% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 49.6214 | $506 | $13,090 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 49.6133 | $17,631 | $20,074 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.8216 | $16,003 | $386 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.9882 | $14,739 | $123 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.9785 | $15,703 | $2,365 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9998 |
| XUSDC | $1.0000 |
| XPYUSD | $1.1259 |
| XPAX | $1.0408 |
| XUSDT | $1.0000 |
