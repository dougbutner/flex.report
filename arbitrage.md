# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-07-25 08:52 UTC** · Primary path: deepest **EASY**↔stable pools*

## How to read

- Rows = **sell** this coin. Columns = **buy** that coin.
- Cell = how many **buy** tokens you get per **1.0 sell** token (implied), routing **sell → EASY → buy**.
- **bps** = distance from 1.0000 (parity). Green opportunity when you receive more than 1.0 of a same-peg asset after fees/slippage — always simulate on [Alcor Swap](https://proton.alcor.exchange/swap) before sizing.

Fees, hop slippage, and pool depth can erase small edges. EASY transfer tax (2%) applies when EASY moves to non-exempt accounts — prefer routing that stays inside `swap.alcor` memos when possible.

## Implied rates via EASY (amount of Buy per 1 Sell)

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | 1.000000 | 1.000906 | 0.968272 | 0.940640 | 1.001224 |
| **XUSDC** | 0.999095 | 1.000000 | 0.967396 | 0.939788 | 1.000317 |
| **XPYUSD** | 1.032768 | 1.033703 | 1.000000 | 0.971462 | 1.034032 |
| **XPAX** | 1.063106 | 1.064069 | 1.029376 | 1.000000 | 1.064407 |
| **XUSDT** | 0.998778 | 0.999683 | 0.967088 | 0.939490 | 1.000000 |

### Same matrix in basis points vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.0 | +9.1 | -317.3 | -593.6 | +12.2 |
| **XUSDC** | -9.0 | +0.0 | -326.0 | -602.1 | +3.2 |
| **XPYUSD** | +327.7 | +337.0 | +0.0 | -285.4 | +340.3 |
| **XPAX** | +631.1 | +640.7 | +293.8 | +0.0 | +644.1 |
| **XUSDT** | -12.2 | -3.2 | -329.1 | -605.1 | +0.0 |

![Cross-rate heatmap (bps)](assets/arbitrage-heatmap.png)

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.064407** (+644.1 bps) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.064069** (+640.7 bps) via EASY
- Sell **XPAX** → buy **XMD**: **1.063106** (+631.1 bps) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.034032** (+340.3 bps) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.033703** (+337.0 bps) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.939490** (-605.1 bps) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.939788** (-602.1 bps) via EASY
- Sell **XMD** → buy **XPAX**: **0.940640** (-593.6 bps) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.967088** (-329.1 bps) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.967396** (-326.0 bps) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://proton.alcor.exchange/analytics/pools/4067) | 60.5532 | $11,932 | $6,633 |
| XUSDC | [4065](https://proton.alcor.exchange/analytics/pools/4065) | 60.4984 | $11,996 | $2,807 |
| XPYUSD | [4068](https://proton.alcor.exchange/analytics/pools/4068) | 62.5374 | $11,450 | $50 |
| XPAX | [4070](https://proton.alcor.exchange/analytics/pools/4070) | 64.3745 | $11,499 | $1 |
| XUSDT | [4066](https://proton.alcor.exchange/analytics/pools/4066) | 60.4792 | $11,784 | $1,270 |

### Alcor mark prices

| | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| `usd_price` | $0.9811 | $1.0000 | $1.0308 | $1.0444 | $0.9816 |

## Share / refresh

Copy the dated tables above into Telegram or Club notes. Say **update stats** in Cursor to refresh this page with a new timestamp.
