# flexforex (contract: [`for3x`](https://explorer.xprnetwork.org/account/for3x))

One account, many symbols. Each token is `(for3x, symbol)`. Verify actions on the [XPR explorer](https://explorer.xprnetwork.org/account/for3x). Day-to-day use is the Flex launcher, not raw actions. `setconfig` and `receiverand` are not in the launcher.

## Contract surface

Issuer launch path:

- `create`: two fields, issuer and max supply. Rates start at 0.
- `setfees`: reflection, burn, project, project account. First call can be any split up to 100%. Later calls cannot raise the total or lower reflection.
- `mint`: 100% to the issuer before liftoff.
- `startlaunch`: quote (amount 0), fee, ticks, sqrt price, proof pool id, `swap_underlying_default`.
- `liftoff`: checks the Alcor position, 100% of supply on `swap.alcor`, and lock remaining at least 90 days. Sets `launched` false if a presale row exists.
- `addpool`: register an Alcor pool as a flex reward route. Launch pair first.
- `golive`: ends a presale window and sets `launched` true.

Presale (issuer, or the contract):

- `setpresale`, `setlaunchtime`, `addinsiders`, `rminsider`.
- Holder: `reginsider`, `provelock`.

After launch:

- `transfer`: tax on top of wallet-to-wallet sends. Alcor inbound tax is taken from the amount. Skipped for contract payouts, fee-opted-out accounts, and the pre-liftoff Alcor seed.
- `makeitrain(token_symbol, keeper)`: anyone may sign as `keeper`. Splashes 38.2% of `reflection_pool`. Optional keeper tip only when `keeper_min` is at most 1% of that splash.
- `checklock`: after `unlock_time`, may add 0.25% to `dev_bps` and 0.25% to `club_bps`, once.
- `choosereward`: empty output contract means native. Pool id 0 uses the launch quote only if `swap_underlying_default` was true.
- `feeoptout`: self can only set the flag on. Turning it off needs the contract.
- `inheritance`, `inheritmemo`: beneficiary and memo on the holder's splash.
- `ratios`: angel and jackpot as a share of `reflection_rate` only. Does not change the tax total.
- `setdist`: one shot for the issuer (anytime for the contract). Sets those ratios plus jackpot winners, jackpot min hold, angel cooldown, keeper min, and reflect min. Then `dist_locked`.
- `setangelnum`: holder picks 0-999. 1000 on the row means unset.
- `pullangel`, `pulljackpot`: anyone. Pot must be above zero and no draw in flight. Payout happens in `receiverand`.
- `receiverand`: `rng` only. Not a user action.
- `setconfig`: contract only. Pagination cursor, page limit (1-1000), admin. The rate arguments are ignored. Tax is `setfees`.
- `burn`, `open`, `close`: token lifecycle.

## Tables

Scope is the symbol code except `launches` (scope is `for3x`) and `accounts` (scope is the owner).

- `stat`: supply, max supply, issuer, `reflection_pool`, `burn_pool`, `project_pool`, `angel_numbers_pool`, `jackpot_pool`, `angel_numbers_last`, `flexer_count`.
- `settings`: rates, project account, admin, `dist_locked`, angel and jackpot bps, jackpot winners, jackpot min hold, angel cooldown, `keeper_min`, `reflect_min`, `rng_kind`, `rng_amt`.
- `flexers`: owner, balance, fee opt-out, reward pool id, beneficiary, bene rate, memo, angel number. Secondary index `byangel`.
- `flexpools`: Alcor pool id, input symbol and contract, output symbol and contract.
- `launches`: quote, fee, ticks, sqrt price, proof pool, flex quote flag, launched, pool id, position id, dev bps, club bps, unlock time, swap-underlying default.
- `presales`: clocks, mode, caps, NFT and hold and LP gates, `gates_all`, KYC flag.
- `insiders`: account, approved, source, locked position id.

## What is different from `3asy` and `fl3x`

`3asy` has no project tax, no inheritance, no angels, no jackpot. `fl3x` has project tax and inheritance, and no angels or jackpot. Both pay with `makeitrain(token_symbol, sender)`. This contract's field is `keeper`.

Liftoff EASY hold on this contract is 50,000 whole EASY times (prior launches by that issuer on `for3x`, plus one), then the discount in [How your token works](../launch-your-own/how-your-token-works.md). `3asy` uses 5,000. `fl3x` uses 10,000. The discount clock is the same date on all three.
