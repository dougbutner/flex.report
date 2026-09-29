# Game guide

You do not have to be the issuer. You need a connected wallet to sign.

## Presale

A presale exists only if the issuer signed `setpresale` before liftoff. No row means the token opens at liftoff.

With a row, and until `golive`:

1. **Insider time.** Approved insiders may deposit into the pool. Join (`reginsider`) opens here. Before this clock the button shows the wait in hours and minutes. An issuer invite can put you on the list without that click. "Not on list" means neither has happened. Deposits close when public launch starts.
2. **Public launch.** Buys out of the pool open, only to approved insiders, up to the cap. The cap is `insider_bps` of supply, or `locked_insider_bps` after a proved lock. Buy room is that cap minus what you already hold.
3. **`golive`.** The issuer opens normal transfers. Until then, wallet-to-wallet sends stay closed.

Gates are a hold, an NFT, LP, or every gate the issuer turned on. Invites are not a gate. **Prove lock** shows only when a lock bonus is set. Paste the Alcor position id.

The issuer can freeze the window, move the clocks later, add or remove names, and call `golive`.

## Make it rain

Blue squares are tokens with unpaid reflections. Click one and sign. A gray square is under the minimum.

`makeitrain` pays 38.2% of `reflection_pool`, split by balance. The swap, the contract, and a few other vaults are not in the share count.

Take the pay in the token, or flex it. `choosereward` on the token page picks another token the issuer has added. If you never choose, and the launch swaps the default, you are paid in the launch quote.

## Call the angels

`for3x` only, and only if angels were given a share of reflection. That share fills `angel_numbers_pool`. It is not extra tax.

Pick 0 to 999 with `setangelnum`. `pullangel` asks the randomness contract to draw. Matching numbers are paid when the draw comes back. White squares are pots above zero. Anyone can call. An empty pot is not shown. A second call while a draw is pending fails.

## Jackpot

Gold squares, no number to pick. `jackpot_pool` fills from the jackpot share of reflection. `pulljackpot` draws winners. Winner count, and the minimum hold checked after the draw, are what the issuer set. Anyone can call when the pot is above zero.

## On the token page

- Make it rain, pull angel, or pull jackpot when the button is there and the pot is above zero.
- Choose the token your splash arrives as.
- Fee opt-out turns tax off for your sends. You can only turn that on.
- On `fl3x` and `for3x`, name a beneficiary so part of your splash pays someone else.
