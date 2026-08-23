---
name: update-stats
description: >-
  Refresh Flex Report market stats, stablecoin arbitrage matrices, and thelake
  success-story numbers from XPR Alcor APIs, on-chain mon3y tables, Binance,
  and DefiLlama. Use when the user says "update stats", "refresh stats",
  "update market stats", "update arbitrage", or asks to pull latest EASY/Alcor
  volume, TVL, price, reflection pool, XMD/XUSDC/XPYUSD/XPAX/XUSDT cross-rates,
  or thelake case-study charts into the docs.
---

# Update Stats

## When

User says **update stats** (or refresh/update market stats / arbitrage).

## Do this

1. From the repo root, run all three refresh scripts:

```bash
python3 .cursor/skills/update-stats/scripts/refresh_market_stats.py
python3 .cursor/skills/update-stats/scripts/refresh_arbitrage.py
python3 .cursor/skills/update-stats/scripts/refresh_success_stories.py
```

Requires network. Needs `matplotlib` for chart PNGs (`pip install -r .cursor/skills/update-stats/requirements.txt` if missing).

GitHub Actions runs the same three scripts daily around **9 AM Eastern** (`.github/workflows/update-stats.yml`; cron `0 13 * * *` UTC) and commits updated files to `main`. Manual run: Actions → Update stats → Run workflow.

2. Confirm these files changed:

**Market stats**
- `market-stats.md`
- `market-stats.json`
- `assets/market-easy-pools-24h.png`
- `assets/market-easy-share.png` (EASY share donut + same-window EASY vs rest of Alcor)
- `tokenomics.md` live Flex family tables (supply / fees / major-token USD backing)
- `tokens/won/won-featured.png` (random WON art for onboarding each refresh)

**Arbitrage**
- `arbitrage.md`
- `arbitrage.json`
- `assets/arbitrage-heatmap.png`

**Success stories (thelake)**
- `our-story/success-stories.md`
- `our-story/success-stories.json`
- `our-story/assets/reflections-lake.png`
- `our-story/assets/thelake-reflections-summary.png`
- `our-story/assets/thelake-reflections-cumulative.png`
- `our-story/assets/thelake-reflections-monthly.png`
- `our-story/assets/thelake-vs-bluechips.png`

3. Do **not** rewrite founder/legal content. Do not put `montauk` back on Success Stories.

4. Brief the user with: EASY price, 24h EASY volume, Alcor Proton swap 1D volume, reflection pool, top arb +/- % (best sell→buy leg), thelake USD bag vs day-one dollars, updated timestamp.

## Alcor links in generated markdown

**UI links must use the v2 XPR UI** (see `.cursor/rules/alcor-v2-links.mdc`):

- Swap: `https://alcor.exchange/v/xpr/swap`
- Analytics / token / pool / farms: `https://alcor.exchange/v/xpr/analytics…`
- Never emit legacy `https://proton.alcor.exchange/…` UI URLs in markdown.

**API fetches** still use `https://proton.alcor.exchange/api/v2/…`.

## Data sources (Alcor / XPR)

Base URL for XPR (Proton) chain: `https://proton.alcor.exchange/api/v2/`

Docs: https://api.alcor.exchange/ and https://docs.alcor.exchange/developers-api/api

| What | Endpoint | Notes |
| --- | --- | --- |
| Exchange TVL / volume | `GET .../analytics/global?resolution=1D` and `?resolution=1M` | Resolutions: `1D`, `1W`, `1M`. API host is **proton.alcor.exchange**; user-facing docs use **alcor.exchange/v/xpr/…**. |
| Token price | `GET .../tokens/easy-mon3y` | `usd_price`, `system_price` (XPR) |
| Pool volumes / TVL | `GET .../swap/pools` | Sum pools where `tokenA` or `tokenB` is EASY@`mon3y`. Fields: `volumeUSD24`, `volumeUSDWeek`, `volumeUSDMonth`, `tvlUSD`, `change24` |
| Daily pool charts | `GET .../swap/charts?tokenA=easy-mon3y&tokenB=xusdc-xtokens` | Optional; used for longer price/volume series |
| Reflection pool | RPC `get_table_rows` `code=mon3y` `scope=EASY` `table=stat` | `reflection_pool` asset |
| Flexer count | RPC page `flexers` table `code=mon3y` `scope=mon3y` | Count rows |
| Stable arb matrix | Same `.../swap/pools` | Stables: XMD@`xmd.token`, XUSDC/XPYUSD/XPAX/XUSDT@`xtokens`. Prefer deepest EASY↔stable pool per asset by **Stable TVL** (USD value of non-EASY quantity). Cross rate sell→buy = easy_per_sell / easy_per_buy. Do **not** include direct stable↔stable pools section. |

RPC: `https://api.protonnz.com/v1/chain/...` (fallback `https://proton.greymass.com`).

## EASY volume definition

**EASY 24h/7d/30d volume** = sum of Alcor AMM `volumeUSD*` across all pools containing `EASY` / `mon3y`.

**Share of Alcor** = EASY 24h volume / `swapTradingVolume` from `analytics/global?resolution=1D`.

Do not use spot `markets` volume for EASY: liquidity is almost entirely AMM/swap.

## Arbitrage page rules

Keep `arbitrage.md` structure:

1. Dated snapshot header (UTC)
2. Cross-rate heatmap (+/- percent) at the top
3. How to read (sell rows / buy cols)
4. 5×5 rate matrix via EASY
5. Same matrix as +/- percent vs 1.0
6. Standout legs
7. EASY pool anchors with **Stable TVL** (non-EASY side only) + Alcor `usd_price` row

Do not include a direct stable↔stable pools section.

Coins (fixed order): **XMD, XUSDC, XPYUSD, XPAX, XUSDT** (treat “XUSDX” as XUSDT).

Keep `market-stats.md` at-a-glance order: **24h volume** first, then EASY price, EASY price in XUSDC, **Total EASY pools TVL**, **Total USD backing** (sum of XMD+XUSDC+XPYUSD+XPAX+XUSDT sides in EASY pools: not Alcor `tvlUSD`), then rewards / 7d / 30d / flexers / mcap / share. Top pools table includes **TVL + EASY qty + other side**. Add **Stable backing** table (deepest pool each) with stable side USD, EASY in pool, and pool TVL.

## Page layout rules (ime.money-inspired)

Keep `market-stats.md` structure:

1. At a glance: price, liquidity (TVL), pending holder rewards, 24h/7d/30d volume, flexers, mcap, Alcor share
2. Volume tables + charts
3. Top pools table
4. Alcor Proton exchange-wide 1D / 1M
5. Holder rewards + supply

Do not invent APY unless computed from a documented formula. Prefer raw on-chain + Alcor figures.

## Success stories (thelake): always refresh

`refresh_success_stories.py` is part of the daily job.

- History: `https://proton.eosusa.io/v2/history/get_actions?account=thelake&filter=mon3y:transfer&sort=asc`
- Reflections = inbound transfers `from=mon3y`
- Day-one stack = inbound from `nyra` + `reflections` welcome
- Day-one USD = day-one EASY × Alcor EASY/XUSDC USD mark on **2025-12-22** (not today’s price)
- Comparable bag = day-one + reflections (exclude later `invite.mon3y` from the vs-coins table)
- Blue chips: Binance USDT daily close on 2025-12-22 vs last price (BTC, ETH, XRP, SOL, BNB, ADA, DOT, USDC)
- Staked USDC: compound DefiLlama daily `apy` from day one (Aave V3 ETH USDC, Compound III ETH USDC, Morpho Steakhouse USDC Base, Spark Savings ETH USDC)
- Do not include `montauk`

## Not published

This skill lives under `.cursor/skills/`: **not** linked in `SUMMARY.md`. Do not add it to GitBook navigation.
