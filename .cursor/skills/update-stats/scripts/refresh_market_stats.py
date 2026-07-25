#!/usr/bin/env python3
"""Fetch Alcor Proton + mon3y stats; write market-stats.json, charts, and market-stats.md."""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # flex.report/
ASSETS = ROOT / "assets"
UA = {"User-Agent": "Mozilla/5.0 (flex.report update-stats)"}


def get(url: str):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def post(url: str, body: dict):
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={**UA, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def money(n: float) -> str:
    if abs(n) >= 1_000_000:
        return f"${n:,.0f}" if n >= 100_000 else f"${n:,.2f}"
    if abs(n) >= 1000:
        return f"${n:,.0f}"
    return f"${n:,.2f}"


def fetch_stats() -> dict:
    global_1d = get("https://proton.alcor.exchange/api/v2/analytics/global?resolution=1D")
    global_1w = get("https://proton.alcor.exchange/api/v2/analytics/global?resolution=1W")
    global_1m = get("https://proton.alcor.exchange/api/v2/analytics/global?resolution=1M")
    tok = get("https://proton.alcor.exchange/api/v2/tokens/easy-mon3y")
    pools = get("https://proton.alcor.exchange/api/v2/swap/pools")

    # USD marks for the five backing stables
    stable_meta = {
        "XMD": ("xmd.token", "xmd-xmd.token"),
        "XUSDC": ("xtokens", "xusdc-xtokens"),
        "XPYUSD": ("xtokens", "xpyusd-xtokens"),
        "XPAX": ("xtokens", "xpax-xtokens"),
        "XUSDT": ("xtokens", "xusdt-xtokens"),
    }
    stable_usd = {}
    for sym, (_con, tid) in stable_meta.items():
        t = get(f"https://proton.alcor.exchange/api/v2/tokens/{tid}")
        stable_usd[sym] = float(t.get("usd_price") or 1.0)

    easy = []
    backing = 0.0
    backing_by_stable = {s: 0.0 for s in stable_meta}
    price_xusdc = None  # (price, pool_tvl_for_pick)

    for p in pools:
        a, b = p.get("tokenA", {}), p.get("tokenB", {})
        easy_a = a.get("symbol") == "EASY" and a.get("contract") == "mon3y"
        easy_b = b.get("symbol") == "EASY" and b.get("contract") == "mon3y"
        if not (easy_a or easy_b):
            continue
        other = b if easy_a else a
        easy.append(
            {
                "id": p.get("id"),
                "pair": f"EASY/{other.get('symbol')}",
                "vol24": float(p.get("volumeUSD24") or 0),
                "vol7": float(p.get("volumeUSDWeek") or 0),
                "vol30": float(p.get("volumeUSDMonth") or 0),
                "tvl": float(p.get("tvlUSD") or 0),
                "change24": float(p.get("change24") or 0),
            }
        )
        # Total USD backing = sum of non-EASY (stable) side across the 5 stables
        osym, ocon = other.get("symbol"), other.get("contract")
        meta = stable_meta.get(osym)
        if meta and meta[0] == ocon:
            qty = float(other.get("quantity") or 0)
            side_usd = qty * stable_usd[osym]
            backing += side_usd
            backing_by_stable[osym] += side_usd

        # EASY price in XUSDC from deepest EASY/XUSDC pool
        if osym == "XUSDC" and ocon == "xtokens":
            cand = float(p.get("priceA") if easy_a else p.get("priceB") or 0)
            pool_tvl = float(p.get("tvlUSD") or 0)
            if cand > 0 and (price_xusdc is None or pool_tvl > price_xusdc[1]):
                price_xusdc = (cand, pool_tvl)

    easy.sort(key=lambda x: -x["vol24"])

    vol24 = sum(x["vol24"] for x in easy)
    vol7 = sum(x["vol7"] for x in easy)
    vol30 = sum(x["vol30"] for x in easy)
    px = float(tok["usd_price"])

    stat = post(
        "https://api.protonnz.com/v1/chain/get_table_rows",
        {"code": "mon3y", "scope": "EASY", "table": "stat", "json": True, "limit": 1},
    )["rows"][0]
    refl_pool = float(stat["reflection_pool"].split()[0])
    supply = float(stat["supply"].split()[0])

    holders = 0
    lb = None
    while True:
        body = {"code": "mon3y", "scope": "mon3y", "table": "flexers", "json": True, "limit": 1000}
        if lb:
            body["lower_bound"] = lb
        rows = post("https://api.protonnz.com/v1/chain/get_table_rows", body)
        batch = rows.get("rows") or []
        holders += len(batch)
        if not rows.get("more") or not batch:
            break
        lb = rows.get("next_key")
        if holders > 10000:
            break

    price_xusdc_val = round(price_xusdc[0], 6) if price_xusdc and price_xusdc[0] else round(px, 6)

    alcor_swap_1d = float(global_1d["swapTradingVolume"])
    alcor_swap_1w = float(global_1w["swapTradingVolume"])
    alcor_swap_1m = float(global_1m["swapTradingVolume"])
    share_1d = 100 * vol24 / alcor_swap_1d if alcor_swap_1d else 0
    share_1w = 100 * vol7 / alcor_swap_1w if alcor_swap_1w else 0
    share_1m = 100 * vol30 / alcor_swap_1m if alcor_swap_1m else 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    return {
        "updated": now,
        "easy": {
            "price_usd": round(px, 6),
            "price_xusdc": price_xusdc_val,
            "price_xpr": round(float(tok["system_price"]), 4),
            "usd_backing": round(backing, 2),
            "usd_backing_by_stable": {k: round(v, 2) for k, v in backing_by_stable.items()},
            "volume_usd_24h": round(vol24, 2),
            "volume_usd_7d": round(vol7, 2),
            "volume_usd_30d": round(vol30, 2),
            "pools": len(easy),
            "supply": supply,
            "max_supply": 21_000_000,
            "reflection_pool_easy": round(refl_pool, 6),
            "reflection_pool_usd": round(refl_pool * px, 2),
            "flexers": holders,
            "mcap_usd": round(supply * px, 2),
            "share_of_alcor_swap_24h_pct": round(share_1d, 2),
            "share_of_alcor_swap_7d_pct": round(share_1w, 2),
            "share_of_alcor_swap_30d_pct": round(share_1m, 2),
            "top_pools": easy[:10],
        },
        "alcor_proton": {
            "tvl_usd": round(float(global_1d["totalValueLocked"]), 2),
            "swap_tvl_usd": round(float(global_1d["swapValueLocked"]), 2),
            "volume_usd_1d": round(float(global_1d["totalTradingVolume"]), 2),
            "swap_volume_usd_1d": round(alcor_swap_1d, 2),
            "spot_volume_usd_1d": round(float(global_1d["spotTradingVolume"]), 2),
            "volume_usd_1w": round(float(global_1w["totalTradingVolume"]), 2),
            "swap_volume_usd_1w": round(alcor_swap_1w, 2),
            "spot_volume_usd_1w": round(float(global_1w["spotTradingVolume"]), 2),
            "volume_usd_1m": round(float(global_1m["totalTradingVolume"]), 2),
            "swap_volume_usd_1m": round(alcor_swap_1m, 2),
            "spot_volume_usd_1m": round(float(global_1m["spotTradingVolume"]), 2),
            "swap_fees_1d": round(float(global_1d["swapFees"]), 2),
            "swap_fees_1w": round(float(global_1w["swapFees"]), 2),
            "swap_fees_1m": round(float(global_1m["swapFees"]), 2),
            "dau_1d": round(float(global_1d["dailyActiveUsers"]), 1),
            "dau_1w": round(float(global_1w["dailyActiveUsers"]), 1),
            "dau_1m": round(float(global_1m["dailyActiveUsers"]), 1),
            "pools": global_1d["totalLiquidityPools"],
            "spot_pairs": global_1d["totalSpotPairs"],
            "rest_swap_1d": round(max(alcor_swap_1d - vol24, 0), 2),
            "rest_swap_1w": round(max(alcor_swap_1w - vol7, 0), 2),
            "rest_swap_1m": round(max(alcor_swap_1m - vol30, 0), 2),
        },
    }


def write_charts(stats: dict) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    ASSETS.mkdir(exist_ok=True)
    BG, CARD, GREEN, MUTED, WHITE, BLUE = (
        "#1a1a1c",
        "#212121",
        "#66c167",
        "#9a9a9a",
        "#f2f2f2",
        "#3d8bfd",
    )
    e, a = stats["easy"], stats["alcor_proton"]
    top = list(reversed(e["top_pools"][:8]))

    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    ax.set_facecolor(CARD)
    fig.patch.set_facecolor(BG)
    ax.barh([p["pair"] for p in top], [p["vol24"] for p in top], color=GREEN)
    ax.set_title(
        f"EASY pool volume (24h) · {money(e['volume_usd_24h'])} total",
        color=WHITE,
        loc="left",
    )
    ax.tick_params(colors=MUTED)
    for s in ax.spines.values():
        s.set_color("#3f3f3f")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.grid(True, color="#2c2c2c", axis="x")
    fig.text(0.99, 0.02, f"Source: proton.alcor.exchange · {stats['updated']}", ha="right", color=MUTED, fontsize=8)
    fig.tight_layout()
    fig.savefig(ASSETS / "market-easy-pools-24h.png", facecolor=BG, bbox_inches="tight")
    plt.close()

    # Meaningful context: EASY share of Alcor (donut) + same-window EASY vs rest (grouped bars)
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=150, gridspec_kw={"width_ratios": [1, 1.25]})
    fig.patch.set_facecolor(BG)
    for ax in (ax0, ax1):
        ax.set_facecolor(CARD)

    easy_24 = e["volume_usd_24h"]
    rest_24 = a["rest_swap_1d"]
    share = e["share_of_alcor_swap_24h_pct"]
    wedges, texts, autotexts = ax0.pie(
        [easy_24, rest_24],
        labels=["EASY pools", "Rest of Alcor swap"],
        colors=[GREEN, BLUE],
        autopct=lambda p: f"{p:.0f}%",
        startangle=90,
        textprops={"color": WHITE, "fontsize": 9},
        wedgeprops={"width": 0.42, "edgecolor": BG},
    )
    for t in autotexts:
        t.set_color("#111")
        t.set_fontweight("bold")
    ax0.set_title(f"Alcor Proton swap · 24h\nEASY share {share:.1f}%", color=WHITE, fontsize=11, loc="left")

    windows = ["24h", "7d", "30d"]
    easy_vals = [e["volume_usd_24h"], e["volume_usd_7d"], e["volume_usd_30d"]]
    rest_vals = [a["rest_swap_1d"], a["rest_swap_1w"], a["rest_swap_1m"]]
    shares = [
        e["share_of_alcor_swap_24h_pct"],
        e["share_of_alcor_swap_7d_pct"],
        e["share_of_alcor_swap_30d_pct"],
    ]
    x = np.arange(len(windows))
    w = 0.36
    ax1.bar(x - w / 2, easy_vals, w, label="EASY pools", color=GREEN)
    ax1.bar(x + w / 2, rest_vals, w, label="Rest of Alcor swap", color=BLUE)
    ax1.set_xticks(x)
    ax1.set_xticklabels([f"{w}\n({s:.0f}% EASY)" for w, s in zip(windows, shares)], color=MUTED)
    ax1.set_ylabel("USD volume", color=MUTED)
    ax1.tick_params(colors=MUTED)
    for s in ax1.spines.values():
        s.set_color("#3f3f3f")
    ax1.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"${v/1000:.0f}k" if v < 1e6 else f"${v/1e6:.2f}M")
    )
    ax1.grid(True, color="#2c2c2c", axis="y")
    ax1.legend(facecolor=CARD, edgecolor="#3f3f3f", labelcolor=WHITE, fontsize=8)
    ax1.set_title("Same-window: EASY vs rest of Alcor", color=WHITE, fontsize=11, loc="left")

    fig.text(
        0.99,
        0.02,
        f"EASY = sum volumeUSD* on EASY@mon3y pools · Alcor = analytics/global · {stats['updated']}",
        ha="right",
        color=MUTED,
        fontsize=7,
    )
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(ASSETS / "market-easy-share.png", facecolor=BG, bbox_inches="tight")
    # keep old filename as alias for any cached links
    fig.savefig(ASSETS / "market-volume-context.png", facecolor=BG, bbox_inches="tight")
    plt.close()


def write_markdown(stats: dict) -> None:
    e, a = stats["easy"], stats["alcor_proton"]
    rows = []
    for p in e["top_pools"][:8]:
        tvl = money(p["tvl"]) if p["tvl"] else "—"
        sign = "+" if p["change24"] >= 0 else ""
        rows.append(
            f"| {p['pair']} | {money(p['vol24'])} | {tvl} | {sign}{p['change24']:.1f}% |"
        )
    pool_table = "\n".join(rows)

    md = f"""# Market Stats

Live pulse of EASY on XPR Alcor — liquidity, volume, and pending holder rewards.

*Last updated: {stats['updated']} · Sources: [Alcor API](https://api.alcor.exchange/) (`proton.alcor.exchange/api/v2`) + `mon3y` chain tables*

## At a glance

| | |
| --- | --- |
| **24h volume (all EASY pools)** | **{money(e['volume_usd_24h'])}** |
| **EASY price** | **${e['price_usd']:.4f}** (~{e['price_xpr']:.2f} XPR) |
| **EASY price in XUSDC** | **{e.get('price_xusdc', e['price_usd']):.6f} XUSDC** |
| **Total USD backing** | **{money(e.get('usd_backing', 0))}** (XMD + XUSDC + XPYUSD + XPAX + XUSDT in EASY pools) |
| **Pending holder rewards** | **{e['reflection_pool_easy']:,.2f} EASY** (~{money(e['reflection_pool_usd'])}) in the reflection pool |
| **7d volume** | **{money(e['volume_usd_7d'])}** |
| **30d volume** | **{money(e['volume_usd_30d'])}** |
| **Flexers (holders on contract)** | **{e['flexers']:,}** |
| **Market cap (fully circulating)** | **{money(e['mcap_usd'])}** |
| **Share of Alcor Proton swap volume (24h)** | **~{e['share_of_alcor_swap_24h_pct']}%** |

USDC-style rewards dashboards inspired this layout: **liquidity**, **pending rewards**, and **volume that feeds holders**.

## Volume

EASY pool volume is the sum of `volumeUSD24` / `volumeUSDWeek` / `volumeUSDMonth` across every Alcor swap pool where one side is `EASY@mon3y`.

**Share** = EASY volume ÷ Alcor Proton **swap** volume for the **same window** (`analytics/global` resolutions `1D` / `1W` / `1M`). That answers: *how much of Alcor’s swap tape is EASY?*

| Window | EASY pools | Rest of Alcor swap | EASY share |
| --- | ---: | ---: | ---: |
| 24h | {money(e['volume_usd_24h'])} | {money(a['rest_swap_1d'])} | **{e['share_of_alcor_swap_24h_pct']:.1f}%** |
| 7d | {money(e['volume_usd_7d'])} | {money(a['rest_swap_1w'])} | **{e.get('share_of_alcor_swap_7d_pct', 0):.1f}%** |
| 30d | {money(e['volume_usd_30d'])} | {money(a['rest_swap_1m'])} | **{e.get('share_of_alcor_swap_30d_pct', 0):.1f}%** |

![EASY share of Alcor Proton swap volume](assets/market-easy-share.png)

![Top EASY pools by 24h volume](assets/market-easy-pools-24h.png)

### Top EASY pools (24h)

| Pool | 24h volume | TVL | 24h Δ |
| --- | ---: | ---: | ---: |
{pool_table}

Trade: [proton.alcor.exchange](https://proton.alcor.exchange) · Analytics: [EASY token](https://proton.alcor.exchange/analytics/tokens/EASY-mon3y)

## Alcor Proton (exchange-wide)

| | 1D | 1W | 1M |
| --- | ---: | ---: | ---: |
| **TVL** | {money(a['tvl_usd'])} | (snapshot) | (snapshot) |
| **Swap TVL** | {money(a['swap_tvl_usd'])} | — | — |
| **Swap volume** | {money(a['swap_volume_usd_1d'])} | {money(a.get('swap_volume_usd_1w', 0))} | {money(a['swap_volume_usd_1m'])} |
| **Spot volume** | {money(a['spot_volume_usd_1d'])} | {money(a.get('spot_volume_usd_1w', 0))} | {money(a['spot_volume_usd_1m'])} |
| **Swap fees** | {money(a['swap_fees_1d'])} | {money(a.get('swap_fees_1w', 0))} | {money(a['swap_fees_1m'])} |
| **DAU (avg)** | ~{a['dau_1d']:.0f} | ~{a.get('dau_1w', a['dau_1d']):.0f} | ~{a['dau_1m']:.0f} |
| **Liquidity pools** | {a['pools']:,} | — | — |
| **Spot pairs** | {a['spot_pairs']:,} | — | — |

## Holder rewards (on-chain)

| | |
| --- | --- |
| Reflection pool (`mon3y` / EASY `stat`) | **{e['reflection_pool_easy']:,.2f} EASY** |
| Approx. USD | **~{money(e['reflection_pool_usd'])}** |
| How it fills | 2% transfer tax into the pool |
| How it pays | Anyone calls `distribute` → splash to flexers |

Track a real bag over time on [Success in Community](our-story/success-in-community.md) (`thelake`).

## Supply

| | |
| --- | --- |
| Max / issued | {e['max_supply']:,.0f} EASY |
| Circulating in pools + wallets | {e['supply']:,.0f} (100% minted day one into liquidity) |

---

*Numbers drift every block. Say **update stats** in Cursor to refresh this page from Alcor + chain.*
"""
    (ROOT / "market-stats.md").write_text(md)


def main() -> None:
    stats = fetch_stats()
    (ROOT / "market-stats.json").write_text(json.dumps(stats, indent=2) + "\n")
    write_charts(stats)
    write_markdown(stats)
    print(f"updated {stats['updated']}")
    print(f"EASY 24h vol {stats['easy']['volume_usd_24h']} · Alcor swap 1D {stats['alcor_proton']['swap_volume_usd_1d']}")


if __name__ == "__main__":
    main()
