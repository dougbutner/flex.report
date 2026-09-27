#!/usr/bin/env python3
"""Refresh kinship1 case study + $100 vs-blue-chip table on Success Stories.

Primary example is kinship1. Inbound transfers from the `reflections` account
are the seed, not yield. Yield is inbound from `mon3y` only. The comparison
table extrapolates that quantity gain onto a $100 buy on kinship1's first day.
More accounts can be appended to EXAMPLES later.

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
GIFT = "jolly.1won"
# Featured bag. Add more account names here when they are ready.
EXAMPLES = (KIN,)
COMPARE_USD = 100.0
START = date(2025, 12, 22)
HYPERION = [
    "https://proton.eu.eosamsterdam.net",
    "https://proton.eosusa.io",
]
RPC = [
    "https://api.protonnz.com",
    "https://proton.greymass.com",
]
# api.binance.com returns 451 from many US/cloud IPs (incl. GitHub Actions).
BINANCE = [
    "https://data-api.binance.vision",
    "https://api.binance.com",
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


def binance_get(path: str):
    last_err = None
    for host in BINANCE:
        try:
            return get(f"{host}{path}")
        except Exception as e:
            last_err = e
            continue
    raise SystemExit(f"Binance fetch failed for {path}: {last_err}")


def binance_start_and_now(start: date) -> dict[str, dict]:
    start_ms = int(datetime(start.year, start.month, start.day, tzinfo=timezone.utc).timestamp() * 1000)
    symbols = [s["binance"] for s in SPOT]
    now_rows = binance_get(
        "/api/v3/ticker/price?symbols=" + json.dumps(symbols).replace(" ", "")
    )
    now = {r["symbol"]: float(r["price"]) for r in now_rows}
    out = {}
    for s in SPOT:
        klines = binance_get(
            f"/api/v3/klines?symbol={s['binance']}&interval=1d&startTime={start_ms}&limit=1"
        )
        if not klines:
            raise SystemExit(f"no Binance kline for {s['binance']} on {start}")
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


def score_example(raw: dict, px_now: float, today: date) -> dict:
    """Seed is inbound from `reflections`. Yield is inbound from `mon3y` only."""
    kin_start = parse_day(raw["first_ts"]) if raw.get("first_ts") else START
    px_start = easy_usd_on(kin_start)
    days = max((today - kin_start).days, 1)
    seed = raw["day_one_easy"]
    refl = raw["reflections_easy"]
    qty_gain = refl / seed if seed else 0.0
    start_usd = COMPARE_USD
    easy_bought = start_usd / px_start if px_start else 0.0
    held = easy_bought * (1.0 + qty_gain)
    now_usd = held * px_now
    usd_gain = now_usd / start_usd - 1.0 if start_usd else 0.0
    raw.update(
        {
            "start": kin_start.isoformat(),
            "price_start": round(px_start, 6),
            "price_now": round(px_now, 6),
            "days": days,
            "qty_gain": round(qty_gain, 6),
            "qty_apy": round(annualized(qty_gain, days), 6),
            "reflections_usd": round(refl * px_now, 2),
            "balance_usd": round(raw["balance_easy"] * px_now, 2),
            "seed_usd_actual": round(seed * px_start, 2),
            "compare_usd": round(start_usd, 2),
            "easy_bought": round(easy_bought, 6),
            "held_easy": round(held, 6),
            "start_usd": round(start_usd, 2),
            "now_usd": round(now_usd, 2),
            "usd_gain": round(usd_gain, 6),
            "usd_apy": round(annualized(usd_gain, days), 6),
            "extrapolated_reflections_easy": round(held - easy_bought, 6),
        }
    )
    return raw


def token_balance(account: str, code: str, symbol: str) -> float:
    last_err = None
    for host in RPC:
        try:
            rows = post(
                f"{host}/v1/chain/get_currency_balance",
                {"account": account, "code": code, "symbol": symbol},
            )
            if not rows:
                return 0.0
            return float(str(rows[0]).split()[0])
        except Exception as e:
            last_err = e
            continue
    raise SystemExit(f"balance failed for {account} {symbol}: {last_err}")


def won_usd_on(day: date) -> float:
    charts = get(
        "https://proton.alcor.exchange/api/v2/swap/charts?tokenA=won-w3won&tokenB=easy-mon3y"
    )
    by_day = {}
    for c in charts:
        d = str(c.get("_id") or "")[:10]
        prices = []
        for qty_k, usd_k in (("reserveA", "usdReserveA"), ("reserveB", "usdReserveB")):
            qty = float(c.get(qty_k) or 0)
            usd = float(c.get(usd_k) or 0)
            if qty > 0:
                prices.append(usd / qty)
        won_px = [p for p in prices if p > 0.05]
        if d and won_px:
            by_day[d] = won_px[0]
    key = day.isoformat()
    if key in by_day:
        return by_day[key]
    prev = [k for k in by_day if k <= key]
    if not prev:
        raise SystemExit(f"no WON chart price on or before {key}")
    return by_day[max(prev)]


def won_usd_now() -> float:
    tok = get("https://proton.alcor.exchange/api/v2/tokens/won-w3won")
    return float(tok.get("usd_price") or 0)


def gift_story(px_easy_now: float) -> dict:
    """jolly.1won: Christmas gift of EASY + 1 WON transfers. Yield excludes the gift itself."""
    raw = summarize_account(GIFT, welcome_from=("printy",))
    gift_day = parse_day(raw["first_ts"]) if raw.get("first_ts") else date(2025, 12, 24)
    easy_seed = raw["in_from"].get("printy", 0.0)
    easy_refl = raw["in_from"].get("mon3y", 0.0)
    easy_won_flex = raw["in_from"].get("swap.alcor", 0.0)
    # WON gifts are separate transfers on w3won.
    won_acts = history_actions_code(GIFT, "w3won")
    won_in = 0.0
    won_n = 0
    for a in won_acts:
        data = a.get("act", {}).get("data") or {}
        if data.get("to") != GIFT:
            continue
        won_in += qty_from(data)
        won_n += 1
    won_now_qty = token_balance(GIFT, "w3won", "WON")
    px_easy_then = easy_usd_on(gift_day)
    px_won_then = won_usd_on(gift_day)
    px_won_now = won_usd_now()
    then_usd = easy_seed * px_easy_then + won_in * px_won_then
    now_usd = raw["balance_easy"] * px_easy_now + won_now_qty * px_won_now
    days = max((datetime.now(timezone.utc).date() - gift_day).days, 1)
    usd_gain = now_usd / then_usd - 1.0 if then_usd else 0.0
    qty_gain = raw["balance_easy"] / easy_seed - 1.0 if easy_seed else 0.0
    return {
        "account": GIFT,
        "day": gift_day.isoformat(),
        "days": days,
        "easy_seed": round(easy_seed, 6),
        "easy_refl": round(easy_refl, 6),
        "easy_won_flex": round(easy_won_flex, 6),
        "easy_now": round(raw["balance_easy"], 6),
        "won_in": round(won_in, 6),
        "won_n": won_n,
        "won_now": round(won_now_qty, 6),
        "px_easy_then": round(px_easy_then, 6),
        "px_easy_now": round(px_easy_now, 6),
        "px_won_then": round(px_won_then, 6),
        "px_won_now": round(px_won_now, 6),
        "then_usd": round(then_usd, 2),
        "now_usd": round(now_usd, 2),
        "usd_gain": round(usd_gain, 6),
        "usd_apy": round(annualized(usd_gain, days), 6),
        "qty_gain": round(qty_gain, 6),
    }


def history_actions_code(account: str, code: str) -> list:
    last_err = None
    for host in HYPERION:
        acts: list = []
        skip = 0
        try:
            while True:
                url = (
                    f"{host}/v2/history/get_actions?account={account}"
                    f"&filter={code}:transfer&sort=asc&limit=1000&skip={skip}"
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
    raise SystemExit(f"history failed for {account} {code}: {last_err}")


def build_payload() -> dict:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    px_now = easy_usd_now()
    today = datetime.now(timezone.utc).date()
    examples = []
    for name in EXAMPLES:
        raw = summarize_account(name, welcome_from=("reflections",))
        examples.append(score_example(raw, px_now, today))
    kin = examples[0]
    kin_start = date.fromisoformat(kin["start"])
    days = kin["days"]
    start_usd = kin["start_usd"]
    usd_gain = kin["usd_gain"]

    spots = binance_start_and_now(kin_start)
    benches = []
    benches.append(
        {
            "id": "easy",
            "name": f"EASY ({kin['account']})",
            "symbol": "EASY",
            "kind": "Flex token",
            "note": f"${COMPARE_USD:.0f} buy, kinship1 reflection rate",
            "start_usd": round(start_usd, 2),
            "now_usd": round(kin["now_usd"], 2),
            "usd_gain": round(usd_gain, 6),
            "usd_apy": round(kin["usd_apy"], 6),
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
                "note": f"Buy and hold from {kin_start.isoformat()}",
                "start": row["start"],
                "now": row["now"],
                "start_usd": round(start_usd, 2),
                "now_usd": round(val, 2),
                "usd_gain": round(gain, 6),
                "usd_apy": round(annualized(gain, days), 6),
            }
        )
    for y in YIELD_USDC:
        ll = llama_compound(y["pool"], kin_start)
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
        "start": kin_start.isoformat(),
        "compare_usd": COMPARE_USD,
        "examples": examples,
        "kinship1": kin,
        "gift": gift_story(px_now),
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
    lake = data["kinship1"]
    updated = data["updated"]

    # Scoreboard / hero
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100)
    fig.patch.set_facecolor("#000000")
    ax.set_facecolor("#000000")
    ax.axis("off")
    ax.text(0.04, 0.88, "KINSHIP1", color=GOLD, fontsize=42, fontweight="bold", transform=ax.transAxes)
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
        f"Seed {lake['day_one_easy']:,.2f} EASY from reflections ({money(lake['seed_usd_actual'])} then)",
        f"${lake['compare_usd']:.0f} extrapolated bag {lake['held_easy']:,.2f} EASY ({money(lake['now_usd'])} at ${lake['price_now']:.4f})",
        f"{data['start']} to {updated[:10]} · {lake['days']} days · USD APY {pct(lake['usd_apy'])}",
    ]
    y = 0.40
    for line in lines:
        ax.text(0.04, y, line, color=GOLD, fontsize=12, transform=ax.transAxes)
        y -= 0.07
    fig.savefig(ASSETS / "reflections-kinship.png", facecolor="#000000", bbox_inches="tight")
    plt.close()

    # Receipts
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(CARD)
    ax.axis("off")
    ax.set_title("kinship1 · reflections receipts", color=WHITE, loc="left", fontsize=14, pad=12)
    rows = [
        ("Seed (from reflections account)", f"{lake['day_one_easy']:,.2f} EASY"),
        ("Seed USD on that day", money(lake["seed_usd_actual"])),
        ("Reflections earned (mon3y only)", f"{lake['reflections_easy']:,.2f} EASY"),
        ("Reflection payments", f"{lake['reflection_payments']}"),
        ("Wallet now", f"{lake['balance_easy']:,.2f} EASY"),
        (f"${lake['compare_usd']:.0f} buy, same reflection rate", f"{lake['easy_bought']:,.2f} EASY"),
        ("Extrapolated bag", f"{lake['held_easy']:,.2f} EASY"),
        ("USD value of $100 bag now", money(lake["now_usd"])),
        ("Growth from reflections (EASY qty)", pct(lake["qty_gain"])),
        ("USD bag vs the $100", pct(lake["usd_gain"])),
    ]
    y = 0.88
    for lab, val in rows:
        ax.text(0.04, y, lab, color=MUTED, fontsize=10, transform=ax.transAxes)
        ax.text(0.96, y, val, color=GREEN, fontsize=10, ha="right", fontweight="bold", transform=ax.transAxes)
        y -= 0.08
    fig.text(
        0.01,
        0.02,
        f"Explorer: explorer.xprnetwork.org/account/kinship1 · {updated}",
        color=MUTED,
        fontsize=7,
    )
    fig.savefig(ASSETS / "kinship1-reflections-summary.png", facecolor=BG, bbox_inches="tight")
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
    ax.set_title("kinship1 · cumulative reflections (EASY)", color=WHITE, loc="left")
    ax.tick_params(colors=MUTED)
    for s in ax.spines.values():
        s.set_color("#3f3f3f")
    ax.set_ylabel("EASY", color=MUTED)
    ax.grid(True, color="#2c2c2c", axis="y")
    fig.text(0.99, 0.02, f"Inbound mon3y → kinship1 · {updated}", ha="right", color=MUTED, fontsize=7)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(ASSETS / "kinship1-reflections-cumulative.png", facecolor=BG, bbox_inches="tight")
    plt.close()

    # Monthly
    months = list(lake["monthly"].items())
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(CARD)
    ax.bar([m[0] for m in months], [m[1] for m in months], color=GREEN)
    ax.set_title("kinship1 · reflections by month (EASY)", color=WHITE, loc="left")
    ax.tick_params(colors=MUTED)
    plt.setp(ax.get_xticklabels(), rotation=40, ha="right")
    for s in ax.spines.values():
        s.set_color("#3f3f3f")
    ax.set_ylabel("EASY", color=MUTED)
    ax.grid(True, color="#2c2c2c", axis="y")
    fig.text(0.99, 0.02, f"Source: Hyperion mon3y:transfer · {updated}", ha="right", color=MUTED, fontsize=7)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(ASSETS / "kinship1-reflections-monthly.png", facecolor=BG, bbox_inches="tight")
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
        "EASY = $100 buy x kinship1 reflection rate · coins = Binance close · USDC yield = DefiLlama APY compounded",
        ha="right",
        color=MUTED,
        fontsize=6.5,
    )
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(ASSETS / "kinship1-vs-bluechips.png", facecolor=BG, bbox_inches="tight")
    plt.close()


def write_markdown(data: dict) -> None:
    kin = data["kinship1"]
    gift = data["gift"]
    rows = []
    for i, r in enumerate(data["benchmarks"], 1):
        mark = "**" if r["id"] == "easy" else ""
        rows.append(
            f"| {i} | {mark}{r['name']}{mark} | {r['kind']} | {money(r['now_usd'])} | "
            f"{mark}{pct(r['usd_gain'])}{mark} | {pct(r['usd_apy'])} |"
        )
    bench = "\n".join(rows)
    first = (kin.get("first_ts") or "")[:10] or data["start"]
    last = (kin.get("last_refl_ts") or "")[:10]

    md = f"""# Success Stories

Pics or it didn’t happen. `kinship1` is a live XPR account, not a backtest. *Updated {data['updated']}.*

![kinship1 reflections case study](assets/reflections-kinship.png)

## Case study: `kinship1`

[`kinship1`](https://explorer.xprnetwork.org/account/kinship1) received **{kin['day_one_easy']:,.2f} EASY** from the `reflections` account on **{first}** (“When things seem hard, Take it EASY”). That seed is the principal. It is not counted as yield. Yield is only inbound transfers from `mon3y`.

**Reflections earned since then:** **{kin['reflections_easy']:,.2f} EASY** across **{kin['reflection_payments']}** payments from `mon3y` (through {last or 'today'}).

That is **{pct(kin['qty_gain'])} more EASY** on the seed (about **{pct(kin['qty_apy'])} APY** on quantity over {kin['days']} days). Wallet now: **{kin['balance_easy']:,.2f} EASY** (≈**{money(kin['balance_usd'])}**).

The comparison below takes that same reflection rate and applies it to a **${kin['compare_usd']:.0f}** buy of EASY on **{first}**, when EASY was **${kin['price_start']:.4f}**. That buy is **{kin['easy_bought']:,.2f} EASY**. After the same reflection rate it is **{kin['held_easy']:,.2f} EASY**, about **{money(kin['now_usd'])}** at **${kin['price_now']:.4f}**: **{pct(kin['usd_gain'])}** vs the $100 (**{pct(kin['usd_apy'])} APY** in USD).

| | |
| --- | --- |
| Account | [kinship1](https://explorer.xprnetwork.org/account/kinship1) |
| Seed (from `reflections`, not yield) | {kin['day_one_easy']:,.2f} EASY on {first} |
| Reflections (mon3y → kinship1) | **{kin['reflections_easy']:,.2f} EASY** (≈**{money(kin['reflections_usd'])}** at today’s mark) |
| Reflection gain (EASY qty) | **{pct(kin['qty_gain'])} EASY** · **{pct(kin['qty_apy'])} APY** |
| $100 buy on that day | **{kin['easy_bought']:,.2f} EASY** at ${kin['price_start']:.4f} |
| Same rate, extrapolated bag | **{kin['held_easy']:,.2f} EASY** (≈**{money(kin['now_usd'])}**) |
| USD bag vs the $100 | **{pct(kin['usd_gain'])}** · **{pct(kin['usd_apy'])} APY** |
| Reflection payments | {kin['reflection_payments']} |
| Wallet now | **{kin['balance_easy']:,.2f} EASY** |

![kinship1 reflections summary](assets/kinship1-reflections-summary.png)

![kinship1 cumulative reflections](assets/kinship1-reflections-cumulative.png)

![kinship1 monthly reflections](assets/kinship1-reflections-monthly.png)

You can verify any payment on the explorer: transfers from `mon3y` with memos like “Take it EASY 🍹 Reflect & Collect ❇️” / “Be EASY 🍹 flex.town 🏘”.

## The Perfect Gift

Your relatives probably do not know crypto, and they do not want it. Open the wallet for them. Put in **100 EASY** and **1 WON**. That is a few dollars. They can ignore it. It still pays.

[`{gift['account']}`](https://explorer.xprnetwork.org/account/{gift['account']}) is one of those wallets.

On **{gift['day']}**, `printy` sent **{gift['easy_seed']:,.0f} EASY** once, and **1 WON** twice (**{gift['won_in']:,.0f} WON**). Memos said Merry Christmas. At that day's prices the package was **{money(gift['then_usd'])}** ({gift['easy_seed']:,.0f} EASY at ${gift['px_easy_then']:.4f}, {gift['won_in']:,.0f} WON at ${gift['px_won_then']:.2f}).

| | Gift day | Now |
| --- | --- | --- |
| EASY | {gift['easy_seed']:,.2f} ({money(gift['easy_seed'] * gift['px_easy_then'])}) | **{gift['easy_now']:,.2f}** ({money(gift['easy_now'] * gift['px_easy_now'])}) |
| WON | {gift['won_in']:,.2f} ({money(gift['won_in'] * gift['px_won_then'])}) | **{gift['won_now']:,.2f}** ({money(gift['won_now'] * gift['px_won_now'])}) |
| Together | **{money(gift['then_usd'])}** | **{money(gift['now_usd'])}** |

The EASY count is **{pct(gift['qty_gain'])}** higher. The dollars are **{pct(gift['usd_gain'])}** higher (**{pct(gift['usd_apy'])} APY** over {gift['days']} days). The WON count is still {gift['won_in']:,.0f}. WON's pay arrived as **{gift['easy_won_flex']:,.2f} EASY** through the WON/EASY pool. Holding the EASY added **{gift['easy_refl']:,.2f} EASY** from `mon3y`. No second deposit.

Copy the size, or copy this wallet's size. **100 EASY and 1 WON** is the same kind of gift. This account was given **{gift['easy_seed']:,.0f} EASY** and **{gift['won_n']}** transfers of **1 WON**. Set up the wallet. Put a few dollars in their name. Hand them the account.

## Same dollars, other bags

What if that **${kin['compare_usd']:.0f}** had bought a major coin on **{data['start']}** instead, or sat in USDC / supplied USDC?

Buy-and-hold, no leverage, no trading. Coin marks are Binance USDT daily close vs now. Idle USDC is the USDC/USDT pair. “Staked USDC” rows compound DefiLlama daily supply APY on the named venue (Aave V3 Ethereum, Compound III Ethereum, Morpho Steakhouse USDC on Base, Spark Savings Ethereum). The EASY row is a **${kin['compare_usd']:.0f}** buy on {first}, grown by kinship1’s reflection rate, marked in USD.

![kinship1 vs blue chips](assets/kinship1-vs-bluechips.png)

| Rank | Bag | Kind | Value now | USD change | USD APY |
| ---: | --- | --- | ---: | ---: | ---: |
{bench}

The twelve comparison bags: Bitcoin, Ethereum, XRP, Solana, BNB, Cardano, Polkadot, idle USDC, plus four large USDC supply/savings venues. This is not advice, and a different window can reverse the ranking.

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
    out.get("kinship1", {}).pop("cumulative", None)
    for ex in out.get("examples") or []:
        ex.pop("cumulative", None)
    return out


def main() -> None:
    data = build_payload()
    (STORY / "success-stories.json").write_text(json.dumps(jsonable(data), indent=2) + "\n")
    write_charts(data)
    write_markdown(data)
    kin = data["kinship1"]
    top = data["benchmarks"][0]
    print(f"updated {data['updated']}")
    print(
        f"kinship1 ${kin['compare_usd']:.0f} bag {kin['held_easy']:.2f} EASY · USD {pct(kin['usd_gain'])} · "
        f"qty {pct(kin['qty_gain'])} · vs winner {top['name']} {pct(top['usd_gain'])}"
    )


if __name__ == "__main__":
    main()
