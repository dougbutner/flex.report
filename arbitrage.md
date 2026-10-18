# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-10-18 16:15 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999860 | 1.000016 | 1.000657 | 0.990328 |
| **XUSDC** | 1.000140 | 1.000000 | 1.000156 | 1.000796 | 0.990466 |
| **XPYUSD** | 0.999984 | 0.999844 | 1.000000 | 1.000641 | 0.990312 |
| **XPAX** | 0.999344 | 0.999204 | 0.999360 | 1.000000 | 0.989678 |
| **XUSDT** | 1.009767 | 1.009626 | 1.009783 | 1.010430 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.01 | +0.00 | +0.07 | -0.97 |
| **XUSDC** | +0.01 | +0.00 | +0.02 | +0.08 | -0.95 |
| **XPYUSD** | -0.00 | -0.02 | +0.00 | +0.06 | -0.97 |
| **XPAX** | -0.07 | -0.08 | -0.06 | +0.00 | -1.03 |
| **XUSDT** | +0.98 | +0.96 | +0.98 | +1.04 | +0.00 |

## Standout legs (this snapshot)

- Sell **XUSDT** → buy **XPAX**: **1.010430** (+1.04% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.009783** (+0.98% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.009767** (+0.98% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **1.009626** (+0.96% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **1.000796** (+0.08% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.989678** (-1.03% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.990312** (-0.97% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.990328** (-0.97% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **0.990466** (-0.95% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **0.999204** (-0.08% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 56.5384 | $14,118 | $2,983 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 56.5463 | $13,853 | $2,208 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.5375 | $13,782 | $398 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.5013 | $13,786 | $348 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 57.0906 | $13,585 | $789 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9853 |
| XUSDC | $1.0000 |
| XPYUSD | $0.9946 |
| XPAX | $0.9914 |
| XUSDT | $1.0000 |
