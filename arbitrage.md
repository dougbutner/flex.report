# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-11 16:50 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000350 | 0.995424 | 0.967627 | 1.001076 |
| **XUSDC** | 0.999651 | 1.000000 | 0.995076 | 0.967289 | 1.000726 |
| **XPYUSD** | 1.004597 | 1.004948 | 1.000000 | 0.972075 | 1.005677 |
| **XPAX** | 1.033456 | 1.033817 | 1.028727 | 1.000000 | 1.034568 |
| **XUSDT** | 0.998925 | 0.999275 | 0.994355 | 0.966587 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.03 | -0.46 | -3.24 | +0.11 |
| **XUSDC** | -0.03 | +0.00 | -0.49 | -3.27 | +0.07 |
| **XPYUSD** | +0.46 | +0.49 | +0.00 | -2.79 | +0.57 |
| **XPAX** | +3.35 | +3.38 | +2.87 | +0.00 | +3.46 |
| **XUSDT** | -0.11 | -0.07 | -0.56 | -3.34 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.034568** (+3.46% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.033817** (+3.38% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.033456** (+3.35% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.028727** (+2.87% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.005677** (+0.57% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.966587** (-3.34% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.967289** (-3.27% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.967627** (-3.24% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.972075** (-2.79% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.994355** (-0.56% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.9502 | $16,125 | $3,882 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.9317 | $15,729 | $2,384 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 53.1936 | $15,689 | $261 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7217 | $15,324 | $1 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.8933 | $15,628 | $764 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9950 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0066 |
| XPAX | $1.0349 |
| XUSDT | $0.9923 |
