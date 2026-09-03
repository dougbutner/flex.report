# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-03 16:47 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 0.999296 | 0.999002 | 0.956758 | 0.997538 |
| **XUSDC** | 1.000705 | 1.000000 | 0.999706 | 0.957432 | 0.998241 |
| **XPYUSD** | 1.000999 | 1.000294 | 1.000000 | 0.957713 | 0.998535 |
| **XPAX** | 1.045197 | 1.044461 | 1.044154 | 1.000000 | 1.042624 |
| **XUSDT** | 1.002468 | 1.001762 | 1.001467 | 0.959119 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | -0.07 | -0.10 | -4.32 | -0.25 |
| **XUSDC** | +0.07 | +0.00 | -0.03 | -4.26 | -0.18 |
| **XPYUSD** | +0.10 | +0.03 | +0.00 | -4.23 | -0.15 |
| **XPAX** | +4.52 | +4.45 | +4.42 | +0.00 | +4.26 |
| **XUSDT** | +0.25 | +0.18 | +0.15 | -4.09 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XMD**: **1.045197** (+4.52% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.044461** (+4.45% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.044154** (+4.42% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.042624** (+4.26% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **1.002468** (+0.25% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.956758** (-4.32% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.957432** (-4.26% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.957713** (-4.23% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.959119** (-4.09% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **0.997538** (-0.25% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 52.3510 | $16,470 | $5,264 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 52.3879 | $16,029 | $3,789 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 52.4033 | $16,156 | $587 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7171 | $15,316 | $4 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 52.4802 | $15,998 | $1,133 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9958 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0085 |
| XPAX | $1.0342 |
| XUSDT | $1.0013 |
