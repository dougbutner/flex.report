# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-06 15:55 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999828 | 0.999851 | 0.957171 | 0.999651 |
| **XUSDC** | 1.000172 | 1.000000 | 1.000023 | 0.957336 | 0.999822 |
| **XPYUSD** | 1.000149 | 0.999977 | 1.000000 | 0.957314 | 0.999800 |
| **XPAX** | 1.044745 | 1.044566 | 1.044590 | 1.000000 | 1.044380 |
| **XUSDT** | 1.000349 | 1.000178 | 1.000200 | 0.957506 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.02 | -0.01 | -4.28 | -0.03 |
| **XUSDC** | +0.02 | +0.00 | +0.00 | -4.27 | -0.02 |
| **XPYUSD** | +0.01 | -0.00 | +0.00 | -4.27 | -0.02 |
| **XPAX** | +4.47 | +4.46 | +4.46 | +0.00 | +4.44 |
| **XUSDT** | +0.03 | +0.02 | +0.02 | -4.25 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.044745** (+4.47% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.044590** (+4.46% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.044566** (+4.46% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.044380** (+4.44% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.000349** (+0.03% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.957171** (-4.28% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.957314** (-4.27% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.957336** (-4.27% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.957506** (-4.25% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.999651** (-0.03% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.3742 | $16,355 | $1,827 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.3832 | $16,030 | $1,600 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.3820 | $16,158 | $280 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7177 | $15,411 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.3925 | $16,046 | $851 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9897 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0079 |
| XPAX | $1.0406 |
| XUSDT | $1.0013 |
