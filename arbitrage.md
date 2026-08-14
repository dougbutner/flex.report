# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-14 14:09 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000364 | 1.000952 | 1.000942 | 1.000323 |
| **XUSDC** | 0.999636 | 1.000000 | 1.000587 | 1.000577 | 0.999958 |
| **XPYUSD** | 0.999049 | 0.999413 | 1.000000 | 0.999990 | 0.999372 |
| **XPAX** | 0.999059 | 0.999423 | 1.000010 | 1.000000 | 0.999381 |
| **XUSDT** | 0.999678 | 1.000042 | 1.000629 | 1.000619 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.04 | +0.10 | +0.09 | +0.03 |
| **XUSDC** | -0.04 | +0.00 | +0.06 | +0.06 | -0.00 |
| **XPYUSD** | -0.10 | -0.06 | +0.00 | -0.00 | -0.06 |
| **XPAX** | -0.09 | -0.06 | +0.00 | +0.00 | -0.06 |
| **XUSDT** | -0.03 | +0.00 | +0.06 | +0.06 | +0.00 |

## Standout legs (this snapshot)

- Sell **XMD** → buy **XPYUSD**: **1.000952** (+0.10% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.000942** (+0.09% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **1.000629** (+0.06% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **1.000619** (+0.06% vs parity) via EASY
- Sell **XUSDC** → buy **XPYUSD**: **1.000587** (+0.06% vs parity) via EASY
- Sell **XPYUSD** → buy **XMD**: **0.999049** (-0.10% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.999059** (-0.09% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **0.999372** (-0.06% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **0.999381** (-0.06% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDC**: **0.999413** (-0.06% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 60.1626 | $11,960 | $1,812 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 60.1407 | $15,596 | $2,188 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 60.1054 | $12,228 | $241 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 60.1060 | $12,576 | $171 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 60.1432 | $12,160 | $404 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9846 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0046 |
| XPAX | $0.9846 |
| XUSDT | $1.0004 |
