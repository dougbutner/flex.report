# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-26 16:50 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999118 | 0.973991 | 0.959931 | 1.002895 |
| **XUSDC** | 1.000883 | 1.000000 | 0.974851 | 0.960778 | 1.003781 |
| **XPYUSD** | 1.026703 | 1.025798 | 1.000000 | 0.985564 | 1.029676 |
| **XPAX** | 1.041742 | 1.040823 | 1.014647 | 1.000000 | 1.044758 |
| **XUSDT** | 0.997113 | 0.996233 | 0.971179 | 0.957160 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.09 | -2.60 | -4.01 | +0.29 |
| **XUSDC** | +0.09 | +0.00 | -2.51 | -3.92 | +0.38 |
| **XPYUSD** | +2.67 | +2.58 | +0.00 | -1.44 | +2.97 |
| **XPAX** | +4.17 | +4.08 | +1.46 | +0.00 | +4.48 |
| **XUSDT** | -0.29 | -0.38 | -2.88 | -4.28 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.044758** (+4.48% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.041742** (+4.17% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.040823** (+4.08% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.029676** (+2.97% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **1.026703** (+2.67% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.957160** (-4.28% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.959931** (-4.01% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.960778** (-3.92% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.971179** (-2.88% vs parity) via EASY
- Sell **XMD** → buy **XPYUSD**: **0.973991** (-2.60% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 53.4500 | $15,866 | $2,015 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 53.4972 | $15,423 | $1,096 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.8773 | $15,138 | $83 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 55.6811 | $14,933 | $0 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 53.2957 | $15,402 | $354 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9957 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0301 |
| XPAX | $1.0431 |
| XUSDT | $0.9917 |
