#!/usr/bin/env python3
"""Stablecoin cross-rates on XPR Alcor for arb sharing. Writes arbitrage.md + JSON + heatmap."""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ASSETS = ROOT / "assets"
UA = {"User-Agent": "Mozilla/5.0 (flex.report update-stats)"}

# User set: XMD, XUSDC, XPYUSD, XPAX, XUSDT (XUSDX → XUSDT)
STABLES = [
    ("XMD", "xmd.token", "xmd-xmd.token"),
    ("XUSDC", "xtokens", "xusdc-xtokens"),
    ("XPYUSD", "xtokens", "xpyusd-xtokens"),
    ("XPAX", "xtokens", "xpax-xtokens"),
    ("XUSDT", "xtokens", "xusdt-xtokens"),
]
SYMBOLS = [s[0] for s in STABLES]


def get(url: str):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def pick_easy_stable_pools(pools: list) -> dict:
    """Best EASY↔stable pool per stable by TVL. Returns easy_per_stable (priceB when EASY is tokenA)."""
    best = {}
    for p in pools:
        a, b = p.get("tokenA", {}), p.get("tokenB", {})
        sa, sb, ca, cb = a.get("symbol"), b.get("symbol"), a.get("contract"), b.get("contract")
        easy_a = sa == "EASY" and ca == "mon3y"
        easy_b = sb == "EASY" and cb == "mon3y"
        if not (easy_a or easy_b):
            continue
        if easy_a:
            stable_sym, stable_con = sb, cb
            # 1 stable = priceB EASY when tokenA=EASY, tokenB=stable
            easy_per_stable = float(p.get("priceB") or 0)
            stable_per_easy = float(p.get("priceA") or 0)
        else:
            stable_sym, stable_con = sa, ca
            easy_per_stable = float(p.get("priceA") or 0)
            stable_per_easy = float(p.get("priceB") or 0)
        meta = next((s for s in STABLES if s[0] == stable_sym and s[1] == stable_con), None)
        if not meta or easy_per_stable <= 0:
            continue
        tvl = float(p.get("tvlUSD") or 0)
        prev = best.get(stable_sym)
        if prev is None or tvl > prev["tvl"]:
            best[stable_sym] = {
                "pool_id": p.get("id"),
                "tvl": tvl,
                "vol24": float(p.get("volumeUSD24") or 0),
                "easy_per_stable": easy_per_stable,
                "stable_per_easy": stable_per_easy,
                "fee": p.get("fee"),
            }
    return best


def pick_direct_pools(pools: list) -> dict:
    """Best direct A/B pool for each unordered pair, keyed (sell, buy) → how many buy per 1 sell."""
    best = {}  # frozenset → pool info with oriented rates

    def match(sym, con):
        return next((s[0] for s in STABLES if s[0] == sym and s[1] == con), None)

    for p in pools:
        a, b = p.get("tokenA", {}), p.get("tokenB", {})
        sa, sb = match(a.get("symbol"), a.get("contract")), match(b.get("symbol"), b.get("contract"))
        if not sa or not sb or sa == sb:
            continue
        tvl = float(p.get("tvlUSD") or 0)
        key = frozenset((sa, sb))
        prev = best.get(key)
        if prev is not None and tvl <= prev["tvl"]:
            continue
        # priceA ≈ tokenA in tokenB terms when paired like EASY pattern: 1 B = priceA of A? 
        # For XUSDC/XUSDT pool 0: priceA 1.00001, priceB 0.999991 → 1/1.00001≈0.99999≈priceB
        # tokenA=XUSDC, tokenB=XUSDT: priceA = USDC per ? Actually priceA is USD-ish of A, priceB of B in A.
        # Safer: use quantity ratio if present
        qa, qb = float(a.get("quantity") or 0), float(b.get("quantity") or 0)
        price_a, price_b = float(p.get("priceA") or 0), float(p.get("priceB") or 0)
        # From EASY pattern: priceB = amount of A per 1 B, priceA = amount of B per 1 A
        # For stables both ~$1: priceA ≈ B per A, priceB ≈ A per B
        a_per_b = price_b if price_b > 0 else (qa / qb if qb else 0)
        b_per_a = price_a if price_a > 0 else (qb / qa if qa else 0)
        # If inverted (both near 1), check consistency
        if a_per_b > 0 and b_per_a > 0 and abs(a_per_b * b_per_a - 1) > 0.05:
            # try swap interpretation
            if abs(price_a * price_b - 1) < 0.05:
                b_per_a, a_per_b = price_a, price_b
        best[key] = {
            "pool_id": p.get("id"),
            "tvl": tvl,
            "vol24": float(p.get("volumeUSD24") or 0),
            "a": sa,
            "b": sb,
            "b_per_a": b_per_a,  # sell A get B
            "a_per_b": a_per_b,  # sell B get A
        }
    # expand to oriented dict
    out = {}
    for info in best.values():
        out[(info["a"], info["b"])] = {
            "pool_id": info["pool_id"],
            "tvl": info["tvl"],
            "vol24": info["vol24"],
            "rate": info["b_per_a"],
        }
        out[(info["b"], info["a"])] = {
            "pool_id": info["pool_id"],
            "tvl": info["tvl"],
            "vol24": info["vol24"],
            "rate": info["a_per_b"],
        }
    return out


def build_via_easy_matrix(easy_pools: dict) -> list[list[float | None]]:
    n = len(SYMBOLS)
    m = [[None] * n for _ in range(n)]
    for i, sell in enumerate(SYMBOLS):
        for j, buy in enumerate(SYMBOLS):
            if i == j:
                m[i][j] = 1.0
                continue
            if sell not in easy_pools or buy not in easy_pools:
                m[i][j] = None
                continue
            # 1 sell → easy_per_sell EASY → / easy_per_buy of buy
            m[i][j] = easy_pools[sell]["easy_per_stable"] / easy_pools[buy]["easy_per_stable"]
    return m


def fmt_rate(x: float | None) -> str:
    if x is None:
        return "—"
    return f"{x:.6f}"


def fmt_bps(x: float | None) -> str:
    if x is None:
        return "—"
    bps = (x - 1.0) * 10_000
    sign = "+" if bps >= 0 else ""
    return f"{sign}{bps:.1f}"


def write_heatmap(matrix: list[list[float | None]], updated: str) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    ASSETS.mkdir(exist_ok=True)
    data = np.array(
        [[(v - 1.0) * 10_000 if v is not None else np.nan for v in row] for row in matrix],
        dtype=float,
    )
    fig, ax = plt.subplots(figsize=(8.5, 7), dpi=150)
    fig.patch.set_facecolor("#1a1a1c")
    ax.set_facecolor("#212121")
    im = ax.imshow(data, cmap="RdYlGn", vmin=-150, vmax=150)
    ax.set_xticks(range(len(SYMBOLS)))
    ax.set_yticks(range(len(SYMBOLS)))
    ax.set_xticklabels(SYMBOLS, color="#f2f2f2")
    ax.set_yticklabels(SYMBOLS, color="#f2f2f2")
    ax.set_xlabel("Buy →", color="#9a9a9a")
    ax.set_ylabel("Sell ↓", color="#9a9a9a")
    ax.set_title("Cross-rate vs 1.000 (bps) via EASY pools", color="#f2f2f2", loc="left")
    for i in range(len(SYMBOLS)):
        for j in range(len(SYMBOLS)):
            v = matrix[i][j]
            if v is None:
                continue
            ax.text(j, i, f"{(v-1)*10000:+.0f}" if i != j else "0", ha="center", va="center", color="#111", fontsize=9)
    cbar = fig.colorbar(im, ax=ax, fraction=0.046)
    cbar.set_label("bps vs peg parity", color="#9a9a9a")
    cbar.ax.yaxis.set_tick_params(color="#9a9a9a")
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color="#9a9a9a")
    fig.text(0.99, 0.02, f"Alcor Proton · {updated}", ha="right", color="#9a9a9a", fontsize=8)
    fig.tight_layout()
    fig.savefig(ASSETS / "arbitrage-heatmap.png", facecolor="#1a1a1c", bbox_inches="tight")
    plt.close()


def write_markdown(payload: dict) -> None:
    e = payload["via_easy"]
    updated = payload["updated"]
    header = "| Sell ↓ \\ Buy → | " + " | ".join(SYMBOLS) + " |"
    sep = "| --- | " + " | ".join(["---:"] * len(SYMBOLS)) + " |"
    rate_rows = []
    bps_rows = []
    for i, sell in enumerate(SYMBOLS):
        rate_rows.append(
            f"| **{sell}** | " + " | ".join(fmt_rate(e["matrix"][i][j]) for j in range(len(SYMBOLS))) + " |"
        )
        bps_rows.append(
            f"| **{sell}** | " + " | ".join(fmt_bps(e["matrix"][i][j]) for j in range(len(SYMBOLS))) + " |"
        )

    pool_lines = []
    for sym in SYMBOLS:
        p = e["pools"].get(sym)
        if not p:
            pool_lines.append(f"| {sym} | — | — | — | — |")
            continue
        pool_lines.append(
            f"| {sym} | [{p['pool_id']}](https://proton.alcor.exchange/analytics/pools/{p['pool_id']}) | "
            f"{p['easy_per_stable']:.4f} | ${p['tvl']:,.0f} | ${p['vol24']:,.0f} |"
        )

    # top edges
    edges = []
    for i, sell in enumerate(SYMBOLS):
        for j, buy in enumerate(SYMBOLS):
            if i == j:
                continue
            r = e["matrix"][i][j]
            if r is None:
                continue
            edges.append((r - 1.0, sell, buy, r))
    edges.sort(reverse=True)
    top = edges[:5]
    bottom = list(reversed(edges[-5:])) if len(edges) >= 5 else []
    opp_lines = []
    for bps, sell, buy, r in top:
        if bps <= 0:
            continue
        opp_lines.append(f"- Sell **{sell}** → buy **{buy}**: **{r:.6f}** ({bps*10000:+.1f} bps) via EASY")
    for bps, sell, buy, r in bottom:
        if bps >= 0:
            continue
        opp_lines.append(f"- Sell **{sell}** → buy **{buy}**: **{r:.6f}** ({bps*10000:+.1f} bps) via EASY")
    if not opp_lines:
        opp_lines = ["- No material dislocation vs 1:1 in this snapshot."]

    # direct highlights
    direct_lines = []
    for (sell, buy), info in sorted(payload["direct"].items(), key=lambda x: -x[1]["tvl"]):
        if sell >= buy:  # list each pool once by alphabetical sell<buy orientation in display
            continue
        other = payload["direct"].get((buy, sell))
        direct_lines.append(
            f"| {sell}/{buy} | {info['pool_id']} | ${info['tvl']:,.2f} | "
            f"{info['rate']:.6f} {buy} per {sell} | "
            f"{(other or {}).get('rate', float('nan')):.6f} {sell} per {buy} |"
        )
    if not direct_lines:
        direct_lines = ["| — | — | — | — | — |"]

    usd_cells = " | ".join(f"${payload['token_usd'][s]:.4f}" for s in SYMBOLS)

    md = f"""# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **{updated}** · Primary path: deepest **EASY**↔stable pools · Also listed: direct stable↔stable pools*

## How to read

- Rows = **sell** this coin. Columns = **buy** that coin.
- Cell = how many **buy** tokens you get per **1.0 sell** token (implied), routing **sell → EASY → buy**.
- **bps** = distance from 1.0000 (parity). Green opportunity when you receive more than 1.0 of a same-peg asset after fees/slippage — always simulate on [Alcor Swap](https://proton.alcor.exchange/swap) before sizing.

Fees, hop slippage, and pool depth can erase small edges. EASY transfer tax (2%) applies when EASY moves to non-exempt accounts — prefer routing that stays inside `swap.alcor` memos when possible.

## Implied rates via EASY (amount of Buy per 1 Sell)

{header}
{sep}
{chr(10).join(rate_rows)}

### Same matrix in basis points vs 1.000

{header}
{sep}
{chr(10).join(bps_rows)}

![Cross-rate heatmap (bps)](assets/arbitrage-heatmap.png)

## Standout legs (this snapshot)

{chr(10).join(opp_lines)}

## EASY pool anchors

| Stable | Pool | EASY per 1 stable | TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
{chr(10).join(pool_lines)}

### Alcor mark prices

| | {' | '.join(SYMBOLS)} |
| --- | {' | '.join(['---:'] * len(SYMBOLS))} |
| `usd_price` | {usd_cells} |

## Direct stable↔stable pools (best TVL each pair)

| Pair | Pool | TVL | Rate | Inverse |
| --- | --- | ---: | --- | --- |
{chr(10).join(direct_lines)}

Many direct books are thin — the EASY matrix is usually the practical arb surface (and why EASY volume dominates Alcor).

## Share / refresh

Copy the dated tables above into Telegram or Club notes. Say **update stats** in Cursor to refresh this page with a new timestamp.
"""
    (ROOT / "arbitrage.md").write_text(md)


def main() -> None:
    pools = get("https://proton.alcor.exchange/api/v2/swap/pools")
    easy_pools = pick_easy_stable_pools(pools)
    direct = pick_direct_pools(pools)
    matrix = build_via_easy_matrix(easy_pools)
    token_usd = {}
    for sym, _con, tid in STABLES:
        tok = get(f"https://proton.alcor.exchange/api/v2/tokens/{tid}")
        token_usd[sym] = float(tok.get("usd_price") or 0)

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    payload = {
        "updated": updated,
        "symbols": SYMBOLS,
        "token_usd": token_usd,
        "via_easy": {"pools": easy_pools, "matrix": matrix},
        "direct": {f"{a}->{b}": v for (a, b), v in direct.items()},
    }
    # JSON-serializable direct keys already strings
    (ROOT / "arbitrage.json").write_text(json.dumps(payload, indent=2) + "\n")
    write_heatmap(matrix, updated)
    write_markdown(
        {
            "updated": updated,
            "token_usd": token_usd,
            "via_easy": {"pools": easy_pools, "matrix": matrix},
            "direct": direct,
        }
    )
    print(f"updated {updated}")
    for i, s in enumerate(SYMBOLS):
        row = " ".join(fmt_rate(matrix[i][j]) for j in range(len(SYMBOLS)))
        print(s, row)


if __name__ == "__main__":
    main()
