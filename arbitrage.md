# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-02 18:08 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000272 | 1.000142 | 0.971465 | 1.001420 |
| **XUSDC** | 0.999728 | 1.000000 | 0.999871 | 0.971201 | 1.001148 |
| **XPYUSD** | 0.999858 | 1.000129 | 1.000000 | 0.971327 | 1.001277 |
| **XPAX** | 1.029373 | 1.029653 | 1.029520 | 1.000000 | 1.030835 |
| **XUSDT** | 0.998582 | 0.998854 | 0.998724 | 0.970088 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.03 | +0.01 | -2.85 | +0.14 |
| **XUSDC** | -0.03 | +0.00 | -0.01 | -2.88 | +0.11 |
| **XPYUSD** | -0.01 | +0.01 | +0.00 | -2.87 | +0.13 |
| **XPAX** | +2.94 | +2.97 | +2.95 | +0.00 | +3.08 |
| **XUSDT** | -0.14 | -0.11 | -0.13 | -2.99 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.030835** (+3.08% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.029653** (+2.97% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.029520** (+2.95% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.029373** (+2.94% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.001420** (+0.14% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.970088** (-2.99% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.971201** (-2.88% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.971327** (-2.87% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.971465** (-2.85% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.998582** (-0.14% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.1002 | $15,568 | $2,205 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.0855 | $15,109 | $3,658 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.0925 | $15,229 | $679 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6893 | $14,763 | $4 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.0235 | $15,142 | $824 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9990 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0082 |
| XPAX | $1.0316 |
| XUSDT | $1.0000 |
