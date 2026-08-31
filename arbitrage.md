# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-31 19:19 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000638 | 0.991984 | 0.954463 | 1.000753 |
| **XUSDC** | 0.999362 | 1.000000 | 0.991351 | 0.953854 | 1.000115 |
| **XPYUSD** | 1.008081 | 1.008724 | 1.000000 | 0.962176 | 1.008840 |
| **XPAX** | 1.047709 | 1.048378 | 1.039311 | 1.000000 | 1.048498 |
| **XUSDT** | 0.999247 | 0.999885 | 0.991237 | 0.953745 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.06 | -0.80 | -4.55 | +0.08 |
| **XUSDC** | -0.06 | +0.00 | -0.86 | -4.61 | +0.01 |
| **XPYUSD** | +0.81 | +0.87 | +0.00 | -3.78 | +0.88 |
| **XPAX** | +4.77 | +4.84 | +3.93 | +0.00 | +4.85 |
| **XUSDT** | -0.08 | -0.01 | -0.88 | -4.63 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.048498** (+4.85% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.048378** (+4.84% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.047709** (+4.77% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.039311** (+3.93% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.008840** (+0.88% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.953745** (-4.63% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.953854** (-4.61% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.954463** (-4.55% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.962176** (-3.78% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.991237** (-0.88% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.2203 | $16,402 | $6,579 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.1870 | $16,142 | $7,929 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.6423 | $16,057 | $40 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7117 | $15,417 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.1810 | $16,130 | $1,798 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9873 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0107 |
| XPAX | $1.0408 |
| XUSDT | $0.9992 |
