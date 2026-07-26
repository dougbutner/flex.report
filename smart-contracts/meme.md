# MEME (contract: [`m3m3`](https://explorer.xprnetwork.org/account/m3m3))

![MEME contract](../assets/heroes/contract-meme.png)

Reflexive EOSIO token with flexible swap targets and configurable burn.

## Contract Surface (actions)

- `create`, `issue`, `open`, `close`, `burn`: standard token lifecycle; `burn` (contract-only in practice) reduces supply and the caller’s balance.
- `transfer`: enforces 1% reflection + 1% burn by default; fees are skipped for distributions sent by the contract and for banned flexers; Alcor-originated sends avoid adding fees on top of the transfer amount.
- `distribute`: paginates flexers, shares the reflection pool (≥100 tokens balance + pool).
- `setconfig`: start key, page limit (≤1000), reflection rate, burn rate (sum ≤100%).
- `noflexzone`: ban/unban a flexer from fees/reflections (self-ban allowed; unban requires contract auth).
- `setflexpool`: register or update a flex pool hint (token, contract, Alcor pool IDs).
- `setflextoken`: pick a preferred flex pool by symbol (blank/EASY resets to default).
- `handle_transfer` (notify): when receiving pool fees from `swap.alcor`, forwards them to `reflections`.

## Data Model (tables)

- `accounts` (per owner): balances.
- `stat` (per symbol): supply, max_supply, reflection_pool, burn_pool, issuer.
- `flexers` (contract scope): owner, balance, banned flag, flextoken (pool id).
- `flexpools`: id, token_symbol, token_contract, pool_ids (Alcor hints).
- `settings` (singleton): token_symbol, start_key, limit, reflection_rate, burn_rate.

## Tokenomics: MEME on EOSIO

- **Rates:** 1% reflection, 1% burn (per transfer).
- **Fee skips:** Contract-driven distributions and banned flexers skip fees.
- **Distribution math:** Excludes balances of `alcor`, `mon3y`, `reward.alcor` and `swap.alcor` from supply; requires both holder and reflection pool to have ≥10M tokens; distributes 61.8% of pro-rata share.
- **Burn handling:** Fees accrue to `burn_pool` and are burned during `distribute` via the contract’s `burn` action.
- **Flex pools:** Holders can opt into swap-routing memos via `setflextoken`; memos target `swap.alcor` with provided pool ids and token hints.
