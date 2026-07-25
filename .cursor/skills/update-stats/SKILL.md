---
name: update-stats
description: >-
  Refresh Flex Report market stats and stablecoin arbitrage matrices from XPR
  Alcor APIs and on-chain mon3y tables. Use when the user says "update stats",
  "refresh stats", "update market stats", "update arbitrage", or asks to pull
  latest EASY/Alcor volume, TVL, price, reflection pool, or XMD/XUSDC/XPYUSD/XPAX/XUSDT
  cross-rates into the docs.
---

# Update Stats

## When

User says **update stats** (or refresh/update market stats / arbitrage).

## Do this

1. From the repo root, run both refresh scripts:

```bash
python3 .cursor/skills/update-stats/scripts/refresh_market_stats.py
python3 .cursor/skills/update-stats/scripts/refresh_arbitrage.py
```

Requires network. Needs `matplotlib` for chart PNGs (`pip install matplotlib` if missing).

2. Confirm these files changed:

**Market stats**
- `market-stats.md`
- `market-stats.json`
- `assets/market-easy-pools-24h.png`
- `assets/market-easy-share.png` (EASY share donut + same-window EASY vs rest of Alcor)

**Arbitrage**
- `arbitrage.md`
- `arbitrage.json`
- `assets/arbitrage-heatmap.png`

3. Optionally refresh Success-in-Community Alcor charts if the user also asks for story/price charts (that is a separate path) (see below). Do **not** rewrite founder/legal content.

4. Brief the user with: EASY price, 24h EASY volume, Alcor Proton swap 1D volume, reflection pool, top arb +/- % (best sell→buy leg), updated timestamp.

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

Keep `market-stats.md` at-a-glance order: **24h volume** first, then EASY price, EASY price in XUSDC, **Total USD backing** (sum of XMD+XUSDC+XPYUSD+XPAX+XUSDT sides in EASY pools: not Alcor `tvlUSD`), then rewards / 7d / 30d / flexers / mcap / share. Do not show “Liquidity (EASY pools TVL)”.

## Page layout rules (ime.money-inspired)

Keep `market-stats.md` structure:

1. At a glance: price, liquidity (TVL), pending holder rewards, 24h/7d/30d volume, flexers, mcap, Alcor share
2. Volume tables + charts
3. Top pools table
4. Alcor Proton exchange-wide 1D / 1M
5. Holder rewards + supply

Do not invent APY unless computed from a documented formula. Prefer raw on-chain + Alcor figures.

## Optional: thelake / Success charts

Only if user asks to update reflection case-study charts:

- History: `https://proton.eosusa.io/v2/history/get_actions?account=thelake&filter=mon3y:transfer&sort=asc`
- Reflections = inbound transfers `from=mon3y`
- Day-one stack ≈ inbound from `nyra` + `reflections` welcome memos
- Regenerate PNGs under `our-story/assets/thelake-*.png` and update numbers in `our-story/success-in-community.md`

## Not published

This skill lives under `.cursor/skills/`: **not** linked in `SUMMARY.md`. Do not add it to GitBook navigation.
