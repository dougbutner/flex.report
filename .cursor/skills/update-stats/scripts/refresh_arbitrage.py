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


def pick_easy_stable_pools(pools: list, token_usd: dict) -> dict:
    """Best EASY↔stable pool per stable by Stable TVL (non-EASY side USD)."""
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
            easy_per_stable = float(p.get("priceB") or 0)
            stable_per_easy = float(p.get("priceA") or 0)
            stable_qty = float(b.get("quantity") or 0)
        else:
            stable_sym, stable_con = sa, ca
            easy_per_stable = float(p.get("priceA") or 0)
            stable_per_easy = float(p.get("priceB") or 0)
            stable_qty = float(a.get("quantity") or 0)
        meta = next((s for s in STABLES if s[0] == stable_sym and s[1] == stable_con), None)
        if not meta or easy_per_stable <= 0:
            continue
        # Stable TVL = USD value of the non-EASY side only
        stable_tvl = stable_qty * float(token_usd.get(stable_sym) or 1.0)
        prev = best.get(stable_sym)
        if prev is None or stable_tvl > prev["stable_tvl"]:
            best[stable_sym] = {
                "pool_id": p.get("id"),
                "stable_tvl": stable_tvl,
                "stable_qty": stable_qty,
                "vol24": float(p.get("volumeUSD24") or 0),
                "easy_per_stable": easy_per_stable,
                "stable_per_easy": stable_per_easy,
                "fee": p.get("fee"),
            }
    return best


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
        return "-"
    return f"{x:.6f}"


def fmt_pct(x: float | None) -> str:
    if x is None:
        return "-"
    pct = (x - 1.0) * 100
    sign = "+" if pct >= 0 else ""
    return f"{sign}{pct:.2f}"


def write_heatmap(matrix: list[list[float | None]], updated: str) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import colors as mcolors

    ASSETS.mkdir(exist_ok=True)
    data = np.array(
        [[(v - 1.0) * 100 if v is not None else np.nan for v in row] for row in matrix],
        dtype=float,
    )
    fig, ax = plt.subplots(figsize=(8.5, 7), dpi=150)
    fig.patch.set_facecolor("#1a1a1c")
    ax.set_facecolor("#212121")
    # Symmetric scale in percent (not basis points)
    lim = float(np.nanmax(np.abs(data))) if np.isfinite(data).any() else 8.0
    lim = max(lim, 1.0)
    im = ax.imshow(data, cmap="RdYlGn", vmin=-lim, vmax=lim)
    ax.set_xticks(range(len(SYMBOLS)))
    ax.set_yticks(range(len(SYMBOLS)))
    ax.set_xticklabels(SYMBOLS, color="#f2f2f2")
    ax.set_yticklabels(SYMBOLS, color="#f2f2f2")
    ax.set_xlabel("Buy →", color="#9a9a9a")
    ax.set_ylabel("Sell ↓", color="#9a9a9a")
    ax.set_title("Cross-rate vs 1.000 (+/- percent) via EASY pools", color="#f2f2f2", loc="left")
    norm = mcolors.Normalize(vmin=-lim, vmax=lim)
    cmap = plt.get_cmap("RdYlGn")
    for i in range(len(SYMBOLS)):
        for j in range(len(SYMBOLS)):
            v = matrix[i][j]
            if v is None:
                continue
            pct = (v - 1.0) * 100
            # No % sign in cells; label/colorbar carry the unit
            label = "0" if i == j else f"{pct:+.1f}"
            rgba = cmap(norm(pct if i != j else 0.0))
            # Relative luminance → dark text on light cells, light text on dark
            lum = 0.299 * rgba[0] + 0.587 * rgba[1] + 0.114 * rgba[2]
            text_color = "#111111" if lum > 0.55 else "#f7f7f7"
            ax.text(j, i, label, ha="center", va="center", color=text_color, fontsize=10, fontweight="bold")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046)
    cbar.set_label("+/- percent vs peg parity", color="#9a9a9a")
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
    pct_rows = []
    for i, sell in enumerate(SYMBOLS):
        rate_rows.append(
            f"| **{sell}** | " + " | ".join(fmt_rate(e["matrix"][i][j]) for j in range(len(SYMBOLS))) + " |"
        )
        pct_rows.append(
            f"| **{sell}** | " + " | ".join(fmt_pct(e["matrix"][i][j]) for j in range(len(SYMBOLS))) + " |"
        )

    pool_lines = []
    for sym in SYMBOLS:
        p = e["pools"].get(sym)
        if not p:
            pool_lines.append(f"| {sym} | - | - | - | - |")
            continue
        pool_lines.append(
            f"| {sym} | [{p['pool_id']}](https://alcor.exchange/v/xpr/analytics/pools/{p['pool_id']}) | "
            f"{p['easy_per_stable']:.4f} | ${p['stable_tvl']:,.0f} | ${p['vol24']:,.0f} |"
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
    for delta, sell, buy, r in top:
        if delta <= 0:
            continue
        opp_lines.append(f"- Sell **{sell}** → buy **{buy}**: **{r:.6f}** ({delta*100:+.2f}% vs parity) via EASY")
    for delta, sell, buy, r in bottom:
        if delta >= 0:
            continue
        opp_lines.append(f"- Sell **{sell}** → buy **{buy}**: **{r:.6f}** ({delta*100:+.2f}% vs parity) via EASY")
    if not opp_lines:
        opp_lines = ["- No material dislocation vs 1:1 in this snapshot."]

    mark_lines = [
        f"| {s} | ${payload['token_usd'][s]:.4f} |" for s in SYMBOLS
    ]

    md = f"""# Stablecoin Arbitrage (XPR)

Dated cross-rates for selling each of **XMD · XUSDC · XPYUSD · XPAX · XUSDT** into the others on Alcor (XPR Network).

*Snapshot: **{updated}** · Primary path: deepest **EASY**↔stable pools*

## Cross-rate heatmap (+/- percent)

![Cross-rate heatmap (+/- percent vs parity)](assets/arbitrage-heatmap.png)

## How to read

```mermaid
flowchart LR
  Sell[Sell stable] --> Easy[EASY pool]
  Easy --> Buy[Buy stable]
```

- Rows = **sell** this coin. Columns = **buy** that coin.
- Cell = how many **buy** tokens you get per **1.0 sell** token (implied), routing **sell → EASY → buy**.
- Heatmap / percent table = distance from 1.0000 (parity) as **+/- percent** (green when you receive more than 1.0 of a same-peg asset after fees/slippage). Always simulate on [Alcor Swap](https://alcor.exchange/v/xpr/swap) before sizing.

Fees, hop slippage, and pool depth can erase small edges. EASY transfer tax (2%) applies when EASY moves to non-exempt accounts. Prefer routing that stays inside `swap.alcor` memos when possible.

## Implied rates via EASY (amount of Buy per 1 Sell)

{header}
{sep}
{chr(10).join(rate_rows)}

### Same matrix as +/- percent vs 1.000

{header}
{sep}
{chr(10).join(pct_rows)}

## Standout legs (this snapshot)

{chr(10).join(opp_lines)}

## EASY pool anchors

**Stable TVL** = USD value of the non-EASY side only (XMD / XUSDC / XPYUSD / XPAX / XUSDT depth in that pool).

| Stable | Pool | EASY per 1 stable | Stable TVL | 24h vol |
| --- | --- | ---: | ---: | ---: |
{chr(10).join(pool_lines)}

### Alcor mark prices

| Stable | usd_price |
| --- | ---: |
{chr(10).join(mark_lines)}
"""
    (ROOT / "arbitrage.md").write_text(md)


def main() -> None:
    pools = get("https://proton.alcor.exchange/api/v2/swap/pools")
    token_usd = {}
    for sym, _con, tid in STABLES:
        tok = get(f"https://proton.alcor.exchange/api/v2/tokens/{tid}")
        token_usd[sym] = float(tok.get("usd_price") or 0)

    easy_pools = pick_easy_stable_pools(pools, token_usd)
    matrix = build_via_easy_matrix(easy_pools)

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    payload = {
        "updated": updated,
        "symbols": SYMBOLS,
        "token_usd": token_usd,
        "via_easy": {"pools": easy_pools, "matrix": matrix},
    }
    (ROOT / "arbitrage.json").write_text(json.dumps(payload, indent=2) + "\n")
    write_heatmap(matrix, updated)
    write_markdown(
        {
            "updated": updated,
            "token_usd": token_usd,
            "via_easy": {"pools": easy_pools, "matrix": matrix},
        }
    )
    print(f"updated {updated}")
    for i, s in enumerate(SYMBOLS):
        row = " ".join(fmt_rate(matrix[i][j]) for j in range(len(SYMBOLS)))
        print(s, row)


if __name__ == "__main__":
    main()
