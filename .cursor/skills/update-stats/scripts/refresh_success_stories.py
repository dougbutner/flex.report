#!/usr/bin/env python3
"""Refresh thelake case study + vs-blue-chip table on Success Stories.

Writes our-story/success-stories.md, our-story/success-stories.json, and charts.
"""
from __future__ import annotations

import json
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STORY = ROOT / "our-story"
ASSETS = STORY / "assets"
UA = {"User-Agent": "Mozilla/5.0 (flex.report update-stats)"}

LAKE = "thelake"
KIN = "kinship1"
START = date(2025, 12, 22)
HYPERION = [
    "https://proton.eosusa.io",
    "https://eos.greymass.com",
]
RPC = [
    "https://api.protonnz.com",
    "https://proton.greymass.com",
]

# Spot blue chips: Binance USDT pairs (day-one close vs now).
SPOT = [
    {"id": "btc", "name": "Bitcoin", "symbol": "BTC", "binance": "BTCUSDT", "kind": "blue chip"},
    {"id": "eth", "name": "Ethereum", "symbol": "ETH", "binance": "ETHUSDT", "kind": "blue chip"},
    {"id": "xrp", "name": "XRP", "symbol": "XRP", "binance": "XRPUSDT", "kind": "blue chip"},
    {"id": "sol", "name": "Solana", "symbol": "SOL", "binance": "SOLUSDT", "kind": "blue chip"},
    {"id": "bnb", "name": "BNB", "symbol": "BNB", "binance": "BNBUSDT", "kind": "blue chip"},
    {"id": "ada", "name": "Cardano", "symbol": "ADA", "binance": "ADAUSDT", "kind": "blue chip"},
    {"id": "dot", "name": "Polkadot", "symbol": "DOT", "binance": "DOTUSDT", "kind": "blue chip"},
    {"id": "usdc", "name": "USDC (idle)", "symbol": "USDC", "binance": "USDCUSDT", "kind": "stable"},
]

# Supplied / savings USDC: DefiLlama daily APY compounded from day one.
# Largest popular USDC venues (Aave V3 ETH, Compound III ETH, Morpho Steakhouse Base,
# Spark Savings ETH). Idle USDC is the spot row above.
YIELD_USDC = [
    {
        "id": "aave-usdc",
        "name": "Aave USDC",
        "symbol": "aUSDC",
        "kind": "staked USDC",
        "note": "Aave V3 Ethereum supply",
        "pool": "aa70268e-4b52-42bf-a116-608b370f9501",
    },
    {
        "id": "comp-usdc",
        "name": "Compound USDC",
        "symbol": "cUSDC",
        "kind": "staked USDC",
        "note": "Compound III Ethereum",
        "pool": "7da72d09-56ca-4ec5-a45f-59114353e487",
    },
    {
        "id": "morpho-usdc",
        "name": "Morpho USDC",
        "symbol": "steakUSDC",
        "kind": "staked USDC",
        "note": "Morpho Steakhouse USDC on Base",
        "pool": "ba68527f-8ec2-4c55-827a-8f4673ae047c",
    },
    {
        "id": "spark-usdc",
        "name": "Spark USDC",
        "symbol": "sUSDC",
        "kind": "staked USDC",
        "note": "Spark Savings Ethereum",
        "pool": "c5c74dd1-995c-4445-9d84-3e710bad7d52",
    },
]


def get(url: str, timeout: int = 90):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def post(url: str, body: dict, timeout: int = 60):
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={**UA, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def money(n: float) -> str:
    if abs(n) >= 1000:
        return f"${n:,.0f}"
    return f"${n:,.2f}"


def pct(n: float, digits: int = 1) -> str:
    if abs(n) < 0.5 * (10 ** (-digits - 2)):
        return f"{0:.{digits}f}%"
    sign = "+" if n >= 0 else ""
    return f"{sign}{n * 100:.{digits}f}%"


def annualized(total_return: float, days: float) -> float:
    if days <= 0 or total_return <= -0.999:
        return 0.0
    return (1.0 + total_return) ** (365.25 / days) - 1.0


def qty_from(data: dict) -> float:
    raw = data.get("quantity")
    if raw:
        return float(str(raw).split()[0])
    return float(data.get("amount") or 0)


def parse_day(ts: str) -> date:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).date()


def easy_usd_on(day: date) -> float:
    charts = get(
        "https://proton.alcor.exchange/api/v2/swap/charts?tokenA=easy-mon3y&tokenB=xusdc-xtokens"
    )
    by_day = {}
    for c in charts:
        d = str(c.get("_id") or "")[:10]
        ra = float(c.get("reserveA") or 0)
        ua = float(c.get("usdReserveA") or 0)
        if d and ra > 0:
            by_day[d] = ua / ra
    key = day.isoformat()
    if key in by_day:
        return by_day[key]
    # nearest previous day
    prev = [k for k in by_day if k <= key]
    if not prev:
        raise SystemExit(f"no Alcor EASY chart price on or before {key}")
    return by_day[max(prev)]


def easy_usd_now() -> float:
    tok = get("https://proton.alcor.exchange/api/v2/tokens/easy-mon3y")
    return float(tok.get("usd_price") or 0)


def history_actions(account: str) -> list:
    last_err = None
    for host in HYPERION:
        acts: list = []
        skip = 0
        try:
            while True:
                url = (
                    f"{host}/v2/history/get_actions?account={account}"
                    f"&filter=mon3y:transfer&sort=asc&limit=1000&skip={skip}"
                )
                h = get(url, timeout=120)
                page = h.get("actions") or []
                acts.extend(page)
                total = h.get("total")
                if isinstance(total, dict):
                    total = total.get("value")
                if not page or len(page) < 1000:
                    break
                if total is not None and len(acts) >= int(total):
                    break
                skip += 1000
                if skip > 50000:
                    break
            return acts
        except Exception as e:
            last_err = e
            continue
    raise SystemExit(f"history failed for {account}: {last_err}")


def currency_balance(account: str) -> float:
    last_err = None
    for host in RPC:
        try:
            rows = post(
                f"{host}/v1/chain/get_currency_balance",
                {"account": account, "code": "mon3y", "symbol": "EASY"},
            )
            if not rows:
                return 0.0
            return float(str(rows[0]).split()[0])
        except Exception as e:
            last_err = e
            continue
    raise SystemExit(f"balance failed for {account}: {last_err}")


def summarize_account(account: str, welcome_from: tuple[str, ...] = ("nyra", "reflections")) -> dict:
    acts = history_actions(account)
    in_from: dict[str, float] = defaultdict(float)
    n_from: dict[str, int] = defaultdict(int)
    monthly: dict[str, float] = defaultdict(float)
    cumulative = []
    run = 0.0
    first_ts = last_refl = None
    for a in acts:
        data = a.get("act", {}).get("data") or {}
        if data.get("to") != account:
            continue
        q = qty_from(data)
        frm = data.get("from") or ""
        ts = a.get("@timestamp") or a.get("timestamp") or ""
        in_from[frm] += q
        n_from[frm] += 1
        if first_ts is None:
            first_ts = ts
        if frm == "mon3y":
            last_refl = ts
            run += q
            cumulative.append({"ts": ts, "cum": run, "amt": q})
            if ts:
                monthly[ts[:7]] += q
    day_one = sum(in_from[f] for f in welcome_from)
    reflections = in_from.get("mon3y", 0.0)
    invite = in_from.get("invite.mon3y", 0.0)
    return {
        "account": account,
        "first_ts": first_ts,
        "last_refl_ts": last_refl,
        "in_from": dict(in_from),
        "n_from": dict(n_from),
        "day_one_easy": round(day_one, 6),
        "reflections_easy": round(reflections, 6),
        "reflection_payments": int(n_from.get("mon3y", 0)),
        "invite_easy": round(invite, 6),
        "balance_easy": round(currency_balance(account), 6),
        "monthly": dict(sorted(monthly.items())),
        "cumulative": cumulative,
    }


def binance_start_and_now() -> dict[str, dict]:
    start_ms = int(datetime(START.year, START.month, START.day, tzinfo=timezone.utc).timestamp() * 1000)
    symbols = [s["binance"] for s in SPOT]
    now_rows = get(
        "https://api.binance.com/api/v3/ticker/price?symbols=" + json.dumps(symbols).replace(" ", "")
    )
    now = {r["symbol"]: float(r["price"]) for r in now_rows}
    out = {}
    for s in SPOT:
        klines = get(
            f"https://api.binance.com/api/v3/klines?symbol={s['binance']}"
            f"&interval=1d&startTime={start_ms}&limit=1"
        )
        if not klines:
            raise SystemExit(f"no Binance kline for {s['binance']} on {START}")
        close = float(klines[0][4])
        px_now = now[s["binance"]]
        out[s["id"]] = {
            **s,
            "start": close,
            "now": px_now,
            "factor": px_now / close if close else 1.0,
        }
    return out


def llama_compound(pool: str, start: date) -> dict:
    ch = get(f"https://yields.llama.fi/chart/{pool}", timeout=120)
    data = ch.get("data") or []
    factor = 1.0
    n = 0
    last_apy = 0.0
    for pt in data:
        ts = pt.get("timestamp")
        if isinstance(ts, (int, float)):
            d = datetime.fromtimestamp(ts, tz=timezone.utc).date()
        else:
            d = datetime.fromisoformat(str(ts).replace("Z", "+00:00")).date()
        if d < start:
            continue
        apy = float(pt.get("apy") or 0) / 100.0
        last_apy = apy
        factor *= 1.0 + apy / 365.0
        n += 1
    if n == 0:
        raise SystemExit(f"no DefiLlama APY points for {pool} after {start}")
    return {"factor": factor, "days": n, "last_apy": last_apy}


def build_payload() -> dict:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lake = summarize_account(LAKE)
    kin = summarize_account(KIN, welcome_from=("reflections",))
    px_start = easy_usd_on(START)
    px_now = easy_usd_now()
    today = datetime.now(timezone.utc).date()
    days = max((today - START).days, 1)

    day_one = lake["day_one_easy"]
    refl = lake["reflections_easy"]
    held = day_one + refl  # exclude later invite bonus from the $100 story
    start_usd = day_one * px_start
    now_usd = held * px_now
    refl_usd = refl * px_now
    qty_gain = refl / day_one if day_one else 0.0
    usd_gain = now_usd / start_usd - 1.0 if start_usd else 0.0
    qty_apy = annualized(qty_gain, days)
    usd_apy = annualized(usd_gain, days)

    lake.update(
        {
            "price_start": round(px_start, 6),
            "price_now": round(px_now, 6),
            "start_usd": round(start_usd, 2),
            "now_usd": round(now_usd, 2),
            "reflections_usd": round(refl_usd, 2),
            "qty_gain": round(qty_gain, 6),
            "usd_gain": round(usd_gain, 6),
            "qty_apy": round(qty_apy, 6),
            "usd_apy": round(usd_apy, 6),
            "days": days,
            "held_easy": round(held, 6),
        }
    )

    kin_days = 1
    if kin.get("first_ts"):
        kin_days = max((today - parse_day(kin["first_ts"])).days, 1)
    kin_qty = kin["reflections_easy"] / kin["day_one_easy"] if kin["day_one_easy"] else 0
    kin.update(
        {
            "price_now": round(px_now, 6),
            "reflections_usd": round(kin["reflections_easy"] * px_now, 2),
            "balance_usd": round(kin["balance_easy"] * px_now, 2),
            "qty_gain": round(kin_qty, 6),
            "qty_apy": round(annualized(kin_qty, kin_days), 6),
            "days": kin_days,
        }
    )

    spots = binance_start_and_now()
    benches = []
    benches.append(
        {
            "id": "easy",
            "name": "EASY (thelake)",
            "symbol": "EASY",
            "kind": "Flex token",
            "note": "Hold + reflections",
            "start_usd": round(start_usd, 2),
            "now_usd": round(now_usd, 2),
            "usd_gain": round(usd_gain, 6),
            "usd_apy": round(usd_apy, 6),
        }
    )
    for s in SPOT:
        row = spots[s["id"]]
        val = start_usd * row["factor"]
        gain = row["factor"] - 1.0
        benches.append(
            {
                "id": s["id"],
                "name": s["name"],
                "symbol": s["symbol"],
                "kind": s["kind"],
                "note": f"Buy and hold from {START.isoformat()}",
                "start": row["start"],
                "now": row["now"],
                "start_usd": round(start_usd, 2),
                "now_usd": round(val, 2),
                "usd_gain": round(gain, 6),
                "usd_apy": round(annualized(gain, days), 6),
            }
        )
    for y in YIELD_USDC:
        ll = llama_compound(y["pool"], START)
        val = start_usd * ll["factor"]
        gain = ll["factor"] - 1.0
        benches.append(
            {
                "id": y["id"],
                "name": y["name"],
                "symbol": y["symbol"],
                "kind": y["kind"],
                "note": y["note"],
                "pool": y["pool"],
                "last_apy": round(ll["last_apy"], 6),
                "start_usd": round(start_usd, 2),
                "now_usd": round(val, 2),
                "usd_gain": round(gain, 6),
                "usd_apy": round(annualized(gain, days), 6),
            }
        )

    ranked = sorted(benches, key=lambda r: r["usd_gain"], reverse=True)
    return {
        "updated": updated,
        "start": START.isoformat(),
        "thelake": lake,
        "kinship1": kin,
        "benchmarks": ranked,
    }


def write_charts(data: dict) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ASSETS.mkdir(parents=True, exist_ok=True)
    BG, CARD, GREEN, MUTED, WHITE, GOLD = (
        "#1a1a1c",
        "#212121",
        "#66c167",
        "#9a9a9a",
        "#f2f2f2",
        "#f5ba20",
    )
    lake = data["thelake"]
    updated = data["updated"]

    # Scoreboard / hero
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100)
    fig.patch.set_facecolor("#000000")
    ax.set_facecolor("#000000")
    ax.axis("off")
    ax.text(0.04, 0.88, "THELAKE", color=GOLD, fontsize=42, fontweight="bold", transform=ax.transAxes)
    ax.text(
        0.04,
        0.78,
        "Case study · hold EASY, collect reflections",
        color="#d4b84a",
        fontsize=14,
        transform=ax.transAxes,
    )
    ax.text(
        0.04,
        0.58,
        pct(lake["usd_gain"]),
        color=GOLD,
        fontsize=48,
        fontweight="bold",
        transform=ax.transAxes,
    )
    ax.text(0.04, 0.50, "USD bag vs day-one dollars", color="#d4b84a", fontsize=13, transform=ax.transAxes)
    lines = [
        f"{pct(lake['qty_gain'])} EASY from reflections · {pct(lake['qty_apy'])} APY (qty)",
        f"{lake['reflections_easy']:,.2f} EASY earned · {lake['reflection_payments']} payments · {money(lake['reflections_usd'])}",
        f"Day-one {lake['day_one_easy']:,.2f} EASY ({money(lake['start_usd'])} at ${lake['price_start']:.4f})",
        f"Comparable bag {lake['held_easy']:,.2f} EASY ({money(lake['now_usd'])} at ${lake['price_now']:.4f})",
        f"{data['start']} to {updated[:10]} · {lake['days']} days · USD APY {pct(lake['usd_apy'])}",
    ]
    y = 0.40
    for line in lines:
        ax.text(0.04, y, line, color=GOLD, fontsize=12, transform=ax.transAxes)
        y -= 0.07
    fig.savefig(ASSETS / "reflections-lake.png", facecolor="#000000", bbox_inches="tight")
    plt.close()

    # Receipts
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(CARD)
    ax.axis("off")
    ax.set_title("thelake · reflections receipts", color=WHITE, loc="left", fontsize=14, pad=12)
    rows = [
        ("Day-one stack (nyra + welcome)", f"{lake['day_one_easy']:,.2f} EASY"),
        ("Day-one USD (then EASY price)", money(lake["start_usd"])),
        ("Reflections earned (mon3y)", f"{lake['reflections_easy']:,.2f} EASY"),
        ("Reflection payments", f"{lake['reflection_payments']}"),
        ("Invite program inflows", f"{lake['invite_easy']:,.2f} EASY"),
        ("Wallet now", f"{lake['balance_easy']:,.2f} EASY"),
        ("Comparable bag (day one + reflections)", f"{lake['held_easy']:,.2f} EASY"),
        ("USD value of comparable bag", money(lake["now_usd"])),
        ("Growth from reflections (EASY qty)", pct(lake["qty_gain"])),
        ("USD bag vs day-one dollars", pct(lake["usd_gain"])),
    ]
    y = 0.88
    for lab, val in rows:
        ax.text(0.04, y, lab, color=MUTED, fontsize=10, transform=ax.transAxes)
        ax.text(0.96, y, val, color=GREEN, fontsize=10, ha="right", fontweight="bold", transform=ax.transAxes)
        y -= 0.08
    fig.text(
        0.01,
        0.02,
        f"Explorer: explorer.xprnetwork.org/account/thelake · {updated}",
        color=MUTED,
        fontsize=7,
    )
    fig.savefig(ASSETS / "thelake-reflections-summary.png", facecolor=BG, bbox_inches="tight")
    plt.close()

    # Cumulative
    cum = lake["cumulative"]
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(CARD)
    if cum:
        xs = [datetime.fromisoformat(p["ts"].replace("Z", "+00:00")) for p in cum]
        ys = [p["cum"] for p in cum]
        ax.plot(xs, ys, color=GREEN, linewidth=2)
        ax.fill_between(xs, ys, color=GREEN, alpha=0.15)
    ax.set_title("thelake · cumulative reflections (EASY)", color=WHITE, loc="left")
    ax.tick_params(colors=MUTED)
    for s in ax.spines.values():
        s.set_color("#3f3f3f")
    ax.set_ylabel("EASY", color=MUTED)
    ax.grid(True, color="#2c2c2c", axis="y")
    fig.text(0.99, 0.02, f"Inbound mon3y → thelake · {updated}", ha="right", color=MUTED, fontsize=7)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(ASSETS / "thelake-reflections-cumulative.png", facecolor=BG, bbox_inches="tight")
    plt.close()

    # Monthly
    months = list(lake["monthly"].items())
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(CARD)
    ax.bar([m[0] for m in months], [m[1] for m in months], color=GREEN)
    ax.set_title("thelake · reflections by month (EASY)", color=WHITE, loc="left")
    ax.tick_params(colors=MUTED)
    plt.setp(ax.get_xticklabels(), rotation=40, ha="right")
    for s in ax.spines.values():
        s.set_color("#3f3f3f")
    ax.set_ylabel("EASY", color=MUTED)
    ax.grid(True, color="#2c2c2c", axis="y")
    fig.text(0.99, 0.02, f"Source: Hyperion mon3y:transfer · {updated}", ha="right", color=MUTED, fontsize=7)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(ASSETS / "thelake-reflections-monthly.png", facecolor=BG, bbox_inches="tight")
    plt.close()

    # Vs blue chips
    rows = list(reversed(data["benchmarks"]))
    colors = [GOLD if r["id"] == "easy" else (GREEN if r["usd_gain"] >= 0 else "#6b8cae") for r in rows]
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(CARD)
    ax.barh([r["name"] for r in rows], [r["usd_gain"] * 100 for r in rows], color=colors)
    ax.axvline(0, color="#3f3f3f", linewidth=1)
    ax.set_title(
        f"Same {money(lake['start_usd'])} on {data['start']}: USD change through {updated[:10]}",
        color=WHITE,
        loc="left",
        fontsize=11,
    )
    ax.tick_params(colors=MUTED)
    for s in ax.spines.values():
        s.set_color("#3f3f3f")
    ax.set_xlabel("USD return %", color=MUTED)
    ax.grid(True, color="#2c2c2c", axis="x")
    fig.text(
        0.99,
        0.01,
        "EASY = thelake day-one bag + reflections · coins = Binance close · USDC yield = DefiLlama APY compounded",
        ha="right",
        color=MUTED,
        fontsize=6.5,
    )
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(ASSETS / "thelake-vs-bluechips.png", facecolor=BG, bbox_inches="tight")
    plt.close()


def write_markdown(data: dict) -> None:
    lake = data["thelake"]
    kin = data["kinship1"]
    rows = []
    for i, r in enumerate(data["benchmarks"], 1):
        mark = "**" if r["id"] == "easy" else ""
        rows.append(
            f"| {i} | {mark}{r['name']}{mark} | {r['kind']} | {money(r['now_usd'])} | "
            f"{mark}{pct(r['usd_gain'])}{mark} | {pct(r['usd_apy'])} |"
        )
    bench = "\n".join(rows)
    first = (lake.get("first_ts") or "")[:10] or data["start"]
    last = (lake.get("last_refl_ts") or "")[:10]
    kin_first = (kin.get("first_ts") or "")[:10]

    md = f"""# Success Stories

Pics or it didn’t happen.

![thelake reflections case study](assets/reflections-lake.png)

*Last updated: {data['updated']} · thelake is a live on-chain bag, not a backtest.*

## Case study: `thelake`

On **December 22, 2025**, XPR account [`thelake`](https://explorer.xprnetwork.org/account/thelake) bought into EASY. That is the original playbook example: put in about **$100** of EASY and leave it.

**Day-one stack:** {lake['day_one_easy']:,.2f} EASY  
({lake['in_from'].get('nyra', 0):,.2f} from the funding transfer + {lake['in_from'].get('reflections', 0):,.2f} welcome)

At the **then** EASY mark (**${lake['price_start']:.4f}** on the Alcor EASY/XUSDC pool), that stack was **{money(lake['start_usd'])}**: the ~$100 entry the playbook talks about.

**Reflections earned since then:** **{lake['reflections_easy']:,.2f} EASY** across **{lake['reflection_payments']}** on-chain payments from `mon3y` (through {last or 'today'}).

That is **{pct(lake['qty_gain'])} more EASY** from reflections alone (about **{pct(lake['qty_apy'])} APY** on quantity over {lake['days']} days), without selling. A later invite bonus of **{lake['invite_easy']:,.2f} EASY** sits in the wallet too. The comparison below ignores that bonus so the story stays “the original ~$100 bag.”

USD is a different lens. EASY itself moved from **${lake['price_start']:.4f}** to **${lake['price_now']:.4f}**. The comparable bag (day one + reflections) is **{lake['held_easy']:,.2f} EASY**, about **{money(lake['now_usd'])}** now: **{pct(lake['usd_gain'])}** vs those day-one dollars (**{pct(lake['usd_apy'])} APY** in USD).

| | |
| --- | --- |
| Account created | {first} |
| Day-one stack | {lake['day_one_easy']:,.2f} EASY (**{money(lake['start_usd'])}** at ${lake['price_start']:.4f}) |
| Reflections (mon3y → thelake) | **{lake['reflections_easy']:,.2f} EASY** (≈**{money(lake['reflections_usd'])}** at today’s mark) |
| Reflection gain (EASY qty) | **{pct(lake['qty_gain'])} EASY** · **{pct(lake['qty_apy'])} APY** |
| USD bag vs day-one dollars | **{pct(lake['usd_gain'])}** · **{pct(lake['usd_apy'])} APY** |
| Reflection payments | {lake['reflection_payments']} |
| Comparable bag | **{lake['held_easy']:,.2f} EASY** (≈**{money(lake['now_usd'])}**) |
| Wallet now | **{lake['balance_easy']:,.2f} EASY** (includes {lake['invite_easy']:,.2f} invite EASY) |
| Explorer | [thelake](https://explorer.xprnetwork.org/account/thelake) |

![thelake reflections summary](assets/thelake-reflections-summary.png)

![thelake cumulative reflections](assets/thelake-reflections-cumulative.png)

![thelake monthly reflections](assets/thelake-reflections-monthly.png)

You can verify any payment on the explorer: transfers from `mon3y` with memos like “Take it EASY 🍹 Reflect & Collect ❇️” / “Be EASY 🍹 flex.town 🏘”.

## Same dollars, other bags

What if that **{money(lake['start_usd'])}** had bought a major coin on **{data['start']}** instead, or sat in USDC / supplied USDC?

Buy-and-hold, no leverage, no trading. Coin marks are Binance USDT daily close vs now. Idle USDC is the USDC/USDT pair. “Staked USDC” rows compound DefiLlama daily supply APY on the named venue (Aave V3 Ethereum, Compound III Ethereum, Morpho Steakhouse USDC on Base, Spark Savings Ethereum). EASY is thelake’s day-one stack plus reflections, marked in USD.

![thelake vs blue chips](assets/thelake-vs-bluechips.png)

| Rank | Bag | Kind | Value now | USD change | USD APY |
| ---: | --- | --- | ---: | ---: | ---: |
{bench}

The twelve comparison bags: Bitcoin, Ethereum, XRP, Solana, BNB, Cardano, Polkadot, idle USDC, plus four large USDC supply/savings venues. This is not advice, and a different window can reverse the ranking.

## `kinship1`

[`kinship1`](https://explorer.xprnetwork.org/account/kinship1) got **{kin['day_one_easy']:,.2f} EASY** from `reflections` on **{kin_first}** (“When things seem hard, Take it EASY”). Since then it has taken **{kin['reflections_easy']:,.2f} EASY** in reflections across **{kin['reflection_payments']}** payments (≈**{money(kin['reflections_usd'])}** at ${kin['price_now']:.4f}), a **{pct(kin['qty_gain'])}** gain in EASY (≈**{pct(kin['qty_apy'])} APY** over {kin['days']} days). Balance now: **{kin['balance_easy']:,.2f} EASY** (≈**{money(kin['balance_usd'])}**).

## EASY price (recent)

From the Alcor EASY/XUSDC pool: price stepped up from ≈$0.01 at launch into the mid-teens of cents.

![EASY price chart on Alcor](assets/easy-price-chart.png)

Live analytics: [alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y)

## Volume

Daily volume across the main stable pools (XUSDC + XMD + XUSDT). Quiet at first, then the bots found the rails.

![EASY daily volume chart](assets/easy-volume-chart.png)

Where that volume sits today (top EASY pools by 24h USD):

![Top EASY pools by 24h volume](assets/easy-top-pools-volume.png)

Volume followed. See [Unintended Consequences](unintended-consequences.md) for how EASY became #1 on Alcor.

## Farms

Extensive rewards pools for [Alcor Farms (XPR)](https://alcor.exchange/v/xpr/analytics?tab=farms).

This is just what happens if you **buy and hold**. There are also other ways to earn with EASY, including the [Welcome Program](../maximizing-your-easy.md#welcome-program) and [providing liquidity](../maximizing-your-easy.md#provide-liquidity) against other coins.
"""
    (STORY / "success-stories.md").write_text(md)


def jsonable(data: dict) -> dict:
    out = json.loads(json.dumps(data))
    for key in ("thelake", "kinship1"):
        out.get(key, {}).pop("cumulative", None)
    return out


def main() -> None:
    data = build_payload()
    (STORY / "success-stories.json").write_text(json.dumps(jsonable(data), indent=2) + "\n")
    write_charts(data)
    write_markdown(data)
    lake = data["thelake"]
    top = data["benchmarks"][0]
    print(f"updated {data['updated']}")
    print(
        f"thelake {lake['held_easy']:.2f} EASY · USD {pct(lake['usd_gain'])} · "
        f"qty {pct(lake['qty_gain'])} · vs winner {top['name']} {pct(top['usd_gain'])}"
    )


if __name__ == "__main__":
    main()
