# GRAMS (contract: gold.mon3y)

Tree-aware reflections + flex pools — same pattern as WON, with gold-themed action names. Minted as GRAMS on XPR.

**Backed by XPAXG** (Paxos Gold on XPR via `xtokens`). Pure liquid for gold: 100% of supply vaulted into GRAMS/XPAXG liquidity.

## Contract Surface (actions)

- `forge`, `mint`, `smelt`, `open`, `close` — token lifecycle (`forge` ≈ create, `mint` ≈ issue, `smelt` ≈ burn); smelt reduces supply.
- `transfer` — applies reflection/burn/project rates; fees are skipped for banned flexers and for contract-driven distributions; memo substitution is used during `reflect`.
- `reflect` — walks flexers, distributes the reflection pool (with optional inheritance/tree share), then burns and routes project pool funds.
- `setconfig` — start key, page limit, reflection/burn/project rates, and project account.
- `renounce` — ban/unban a flexer from fees/reflections (self-ban allowed; unban requires contract auth).
- `addpool` — register or update flex pool hints (token, contract, Alcor pool IDs).
- `interestoken` — pick a preferred flex pool by symbol (blank/GRAMS resets to default).
- `inheritance` — pick an inheritance recipient + rate (0–10000, default 10000).
- `inheritmemo` — store a single custom memo (≤200 chars) for the inheritance leg.

### Action map vs WON

| GRAMS (`gold.mon3y`) | WON (`w3won`) |
| --- | --- |
| `forge` / `mint` / `smelt` | `create` / `issue` / `burn` |
| `reflect` | `radiate` |
| `renounce` | `optoutoftax` |
| `interestoken` | `sprouttoken` |
| `inheritance` | `settree` |
| `inheritmemo` | `settreememo` |
| `addpool` / `setconfig` / `transfer` / `open` / `close` | same names |

## Data Model (tables)

- `accounts` (per owner) — balances.
- `stat` (per symbol) — supply, max_supply, reflection_pool, burn_pool, project_pool, issuer.
- `flexers` (contract scope) — owner, balance, banned flag, flextoken, tree, tree_rate, custom_memo.
- `flexpools` — id, token_symbol, token_contract, pool_ids (e.g. Alcor pool hints).
- `settings` (singleton) — token_symbol, start_key, limit, reflection_rate, burn_rate, project_rate, project_account.

## Tokenomics — GRAMS on XPR

- **Supply:** 1,000,000,000 GRAMS (max = supply).
- **Backing / liquidity:** Vaulted against **XPAXG** — pure liquid for Paxos Gold.
- **Rates (live):** 1.1% reflection (`110` / 10000) + 0.11% project (`11` / 10000); burn rate `0`.
- **Project account:** `gold.reflex`.

### Transfer fee budget (per transfer)

- **1.1%** — reflected to GRAMS holders (default reward: GRAMS; flex via `interestoken`).
- **0.11%** — routed to the project account (`gold.reflex`).

### Inheritance + memo substitution

Holders can pass a % of rewards to any account via `inheritance`, with an optional custom memo via `inheritmemo`.

When a flexer has `custom_memo`, the reflect path replaces:

- `@@` → account name
- `$$` → token amount
- `*` → token symbol

### Notes

- `tree_rate` is per 10,000 base points, ie 100 for 1%. The remainder of a reflection stays with the flexer.
- Keep memos under 200 chars; they are stored as a single string per flexer.
- Generational gold: inheritance to any account; GRAMS reflects GRAMS by default.
