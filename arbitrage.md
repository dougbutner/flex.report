# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **2026-08-26 13:46 UTC** · Primary path: deepest **EASY**↔stable pools*

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
| **XMD** | 1.000000 | 1.000667 | 1.000760 | 0.998330 | 1.001984 |
| **XUSDC** | 0.999334 | 1.000000 | 1.000093 | 0.997665 | 1.001317 |
| **XPYUSD** | 0.999241 | 0.999907 | 1.000000 | 0.997572 | 1.001223 |
| **XPAX** | 1.001673 | 1.002340 | 1.002434 | 1.000000 | 1.003660 |
| **XUSDT** | 0.998020 | 0.998685 | 0.998778 | 0.996353 | 1.000000 |

### Same matrix as +/- percent vs 1.000

| Sell ↓ \ Buy → | XMD | XUSDC | XPYUSD | XPAX | XUSDT |
| --- | ---: | ---: | ---: | ---: | ---: |
| **XMD** | +0.00 | +0.07 | +0.08 | -0.17 | +0.20 |
| **XUSDC** | -0.07 | +0.00 | +0.01 | -0.23 | +0.13 |
| **XPYUSD** | -0.08 | -0.01 | +0.00 | -0.24 | +0.12 |
| **XPAX** | +0.17 | +0.23 | +0.24 | +0.00 | +0.37 |
| **XUSDT** | -0.20 | -0.13 | -0.12 | -0.36 | +0.00 |

## Standout legs (this snapshot)

- Sell **XPAX** → buy **XUSDT**: **1.003660** (+0.37% vs parity) via EASY
- Sell **XPAX** → buy **XPYUSD**: **1.002434** (+0.24% vs parity) via EASY
- Sell **XPAX** → buy **XUSDC**: **1.002340** (+0.23% vs parity) via EASY
- Sell **XMD** → buy **XUSDT**: **1.001984** (+0.20% vs parity) via EASY
- Sell **XPAX** → buy **XMD**: **1.001673** (+0.17% vs parity) via EASY
- Sell **XUSDT** → buy **XPAX**: **0.996353** (-0.36% vs parity) via EASY
- Sell **XPYUSD** → buy **XPAX**: **0.997572** (-0.24% vs parity) via EASY
- Sell **XUSDC** → buy **XPAX**: **0.997665** (-0.23% vs parity) via EASY
- Sell **XUSDT** → buy **XMD**: **0.998020** (-0.20% vs parity) via EASY
- Sell **XMD** → buy **XPAX**: **0.998330** (-0.17% vs parity) via EASY

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
| XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) | 54.6433 | $15,190 | $3,094 |
| XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) | 54.6069 | $17,172 | $4,456 |
| XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) | 54.6018 | $14,987 | $107 |
| XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) | 54.7347 | $15,597 | $6 |
| XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) | 54.5351 | $14,744 | $866 |

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
| XMD | $0.9931 |
| XUSDC | $1.0000 |
| XPYUSD | $1.0101 |
| XPAX | $1.0129 |
| XUSDT | $0.9914 |
