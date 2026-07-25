# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-07-25 09:00 UTC** · Primary path: deepest **EASY**↔stable pools*

## Cross-rate heatmap (bps)

![Cross-rate heatmap (bps)](assets/arbitrage-heatmap.png)

## How to read

- Rows = **sell** this coin. Columns = **buy** that coin.
- Cell = how many **buy** tokens you get per **1.0 sell** token (implied), routing **sell → EASY → buy**.
- **bps** = distance from 1.0000 (parity). Green opportunity when you receive more than 1.0 of a same-peg asset after fees/slippage — always simulate on [Alcor Swap](https://proton.alcor.exchange/swap) before sizing.

Fees, hop slippage, and pool depth can erase small edges. EASY transfer tax (2%) applies when EASY moves to non-exempt accounts — prefer routing that stays inside `swap.alcor` memos when possible.

## Implied rates via EASY (amount of Buy per 1 Sell)

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | 1.000000 | 1.000687 | 0.968272 | 0.940640 | 1.001215 |
| **XUSDC** | 0.999313 | 1.000000 | 0.967607 | 0.939993 | 1.000527 |
| **XPYUSD** | 1.032768 | 1.033478 | 1.000000 | 0.971462 | 1.034023 |
| **XPAX** | 1.063106 | 1.063837 | 1.029376 | 1.000000 | 1.064398 |
| **XUSDT** | 0.998786 | 0.999473 | 0.967096 | 0.939498 | 1.000000 |

### Same matrix in basis points vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.0 | +6.9 | -317.3 | -593.6 | +12.2 |
| **XUSDC** | -6.9 | +0.0 | -323.9 | -600.1 | +5.3 |
| **XPYUSD** | +327.7 | +334.8 | +0.0 | -285.4 | +340.2 |
| **XPAX** | +631.1 | +638.4 | +293.8 | +0.0 | +644.0 |
| **XUSDT** | -12.1 | -5.3 | -329.0 | -605.0 | +0.0 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.064398** (+644.0 bps) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.063837** (+638.4 bps) via EASY
- Sell **XPAX** → buy **XMD**: **1.063106** (+631.1 bps) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.034023** (+340.2 bps) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **1.033478** (+334.8 bps) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.939498** (-605.0 bps) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.939993** (-600.1 bps) via EASY
- Sell **XMD** → buy **XPAX**: **0.940640** (-593.6 bps) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.967096** (-329.0 bps) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **0.967607** (-323.9 bps) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://proton.alcor.exchange/analytics/pools/4067) | 60.5532 | $11,942 | $6,633 |
| XUSDC | [4065](https://proton.alcor.exchange/analytics/pools/4065) | 60.5116 | $11,990 | $2,812 |
| XPYUSD | [4068](https://proton.alcor.exchange/analytics/pools/4068) | 62.5374 | $11,450 | $50 |
| XPAX | [4070](https://proton.alcor.exchange/analytics/pools/4070) | 64.3745 | $11,509 | $1 |
| XUSDT | [4066](https://proton.alcor.exchange/analytics/pools/4066) | 60.4797 | $11,793 | $1,270 |

### Alcor mark prices

| | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| `usd_price` | $0.9819 | $1.0000 | $1.0308 | $1.0453 | $0.9824 |

## Share / refresh

Copy the dated tables above into Telegram or Club notes. Say **update stats** in Cursor to refresh this page with a new timestamp.
