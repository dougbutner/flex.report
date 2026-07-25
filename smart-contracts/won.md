# WON (contract: [`w3won`](https://explorer.xprnetwork.org/account/w3won))

Tree-aware reflections + flex pools, minted as WON on XPR.

## Contract Surface (actions)

- `create`, `issue`, `open`, `close`, `burn`: standard token lifecycle; burn reduces supply.
- `transfer`: applies reflection/burn/project rates; fees are skipped for banned flexers and for contract-driven distributions; memo substitution is used during `radiate`.
- `radiate`: walks flexers, distributes the reflection pool (with optional tree share), then burns and routes project pool funds.
- `setconfig`: start key, page limit, reflection/burn/project rates, and project account.
- `optoutoftax`: ban/unban a flexer from fees/reflections (self-ban allowed, unban requires contract auth).
- `addpool`: register or update flex pool hints (token, contract, Alcor pool IDs).
- `sprouttoken`: pick a preferred flex pool by symbol (blank/EASY resets to default).
- `settree`: pick a tree recipient + rate (0-10000, default 10000).
- `settreememo`: store a single custom memo (≤200 chars) for the tree leg.
- `handle_transfer` (notify): when receiving from `swap.alcor` with memos starting `Col`, forwards fees to `1won`.

## Data Model (tables)

- `accounts` (per owner): balances.
- `stat` (per symbol): supply, max_supply, reflection_pool, burn_pool, project_pool, issuer.
- `flexers` (contract scope): owner, balance, banned flag, flextoken, tree, tree_rate, custom_memo.
- `flexpools`: id, token_symbol, token_contract, pool_ids (e.g. Alcor pool hints).
- `settings` (singleton): token_symbol, start_key, limit, reflection_rate, burn_rate, project_rate, project_account.

## Tokenomics: WON on XPR

- **Supply:** 1,000,000 WON (max + initial supply).
- **Liquidity:** 100% paired with EASY on Alcor DEX at launch.

### Pools (EASY per WON; 100 EASY ≈ 1.20 USD)

| WON allocation | Price range (EASY/WON) | Swap LP fee |
| --- | --- | --- |
| 100,000 WON | 100-200 | 1% |
| 300,000 WON | 100-1,000 | 0.3% |
| 600,000 WON | 100-10,000 | 0.05% |

### Transfer fee budget (per transfer)

- **2.2%**: reflected to WON holders as swaps that buy the ecovillage token (freshly launched).
- **0.8%**: routed to volWONteers, distributed by fractal vote every two weeks.

### Memo substitution

When a flexer has `custom_memo`, the distribute path replaces:

- `@@` → account name
- `$$` → token amount
- `*` → token symbol

### Notes

- `tree_rate` is per 10,000 base points, ie 100 for 1%. The remainder of a reflection stays with the flexer.
- Keep memos under 200 chars; they are stored as a single string per flexer.
