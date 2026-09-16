# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-09-16 17:23 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000461 | 1.000651 | 1.000780 | 1.001721 |
| **XUSDC** | 0.999539 | 1.000000 | 1.000190 | 1.000319 | 1.001260 |
| **XPYUSD** | 0.999349 | 0.999810 | 1.000000 | 1.000128 | 1.001069 |
| **XPAX** | 0.999221 | 0.999681 | 0.999872 | 1.000000 | 1.000941 |
| **XUSDT** | 0.998282 | 0.998742 | 0.998932 | 0.999060 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.05 | +0.07 | +0.08 | +0.17 |
| **XUSDC** | -0.05 | +0.00 | +0.02 | +0.03 | +0.13 |
| **XPYUSD** | -0.07 | -0.02 | +0.00 | +0.01 | +0.11 |
| **XPAX** | -0.08 | -0.03 | -0.01 | +0.00 | +0.09 |
| **XUSDT** | -0.17 | -0.13 | -0.11 | -0.09 | +0.00 |

## Standout legs (this snapshot)

- Sell **XMD** → buy **XUSDT**: **1.001721** (+0.17% vs parity) via EASY
- Sell **XUSDC** → buy **XUSDT**: **1.001260** (+0.13% vs parity) via EASY
- Sell **XPYUSD** → buy **XUSDT**: **1.001069** (+0.11% vs parity) via EASY
- Sell **XPAX** → buy **XUSDT**: **1.000941** (+0.09% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **1.000780** (+0.08% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.998282** (-0.17% vs parity) via EASY
- Sell **XUSDT** → buy **XUSDC**: **0.998742** (-0.13% vs parity) via EASY
- Sell **XUSDT** → buy **XPYUSD**: **0.998932** (-0.11% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.999060** (-0.09% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **0.999221** (-0.08% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 56.2189 | $13,837 | $9,049 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 56.1930 | $14,027 | $4,573 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 56.1823 | $14,077 | $593 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 56.1751 | $13,357 | $365 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 56.1223 | $13,438 | $1,580 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9551 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0032 |
| XPAX | $0.9495 |
| XUSDT | $0.9556 |
