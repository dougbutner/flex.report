# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-26 18:57 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000759 | 0.904119 | 0.901568 | 0.992717 |
| **XUSDC** | 0.999241 | 1.000000 | 0.903433 | 0.900884 | 0.991964 |
| **XPYUSD** | 1.106049 | 1.106889 | 1.000000 | 0.997178 | 1.097994 |
| **XPAX** | 1.109179 | 1.110021 | 1.002830 | 1.000000 | 1.101101 |
| **XUSDT** | 1.007336 | 1.008101 | 0.910752 | 0.908182 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.08 | -9.59 | -9.84 | -0.73 |
| **XUSDC** | -0.08 | +0.00 | -9.66 | -9.91 | -0.80 |
| **XPYUSD** | +10.60 | +10.69 | +0.00 | -0.28 | +9.80 |
| **XPAX** | +10.92 | +11.00 | +0.28 | +0.00 | +10.11 |
| **XUSDT** | +0.73 | +0.81 | -8.92 | -9.18 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDC**: **1.110021** (+11.00% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.109179** (+10.92% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.106889** (+10.69% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.106049** (+10.60% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.101101** (+10.11% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.900884** (-9.91% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.901568** (-9.84% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.903433** (-9.66% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.904119** (-9.59% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.908182** (-9.18% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 50.4749 | $501 | $655 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 50.4366 | $17,140 | $4,109 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 55.8277 | $15,644 | $7 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.9857 | $14,740 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 50.8452 | $16,902 | $1,975 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $1.0004 |
| XUSDC | $1.0000 |
| XPYUSD | $1.1009 |
| XPAX | $1.0408 |
| XUSDT | $1.0000 |
