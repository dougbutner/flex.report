# How your token works

The Launch screen is the whole path. Nothing here is a separate product you bolt on later.

- Decide your name.
- Pick your token logo.
- Set a starting price and token supply.
- Decide your pre-sale, or go live together.
- Hold EASY on `mon3y`: 5,000 on `3asy`, 10,000 on `fl3x`, or 50,000 on `for3x`, times one more than the tokens you already launched on that contract. From 9 Sep 2026, XPR, XMD, LOAN, and xtokens start at 90% off that hold and lose 10 points of discount every 30 days until the full hold is back. EASY, WON, GRAMS, and MEME stay at 10% of the full hold and do not rise. A verified first GEASY launch holds 0.
- Launch.
- Promote.
- Send the rain and call the angels.

## Decide your name

The symbol is 1 to 7 uppercase letters. It is fixed forever. The display name can be longer (the field allows 16 characters). You also pick the program: `3asy` (reflections and burn), `fl3x` (plus a project share and inheritance), or `for3x` (plus angel numbers and a jackpot).

![Name, symbol, and program](assets/launch-name.png)

## Pick your token logo

Square PNG or SVG, roughly 256 to 1024 pixels. Pin it, or paste a public image URL. Wallets read the logo from `token.proton`. That registration is signed by the flex contract account (`3asy`, `fl3x`, or `for3x`), not by you. The wizard does not ask you to sign it. Admin pushes the listing later. Until then the launcher still shows the URL you saved.

## Set a starting price and token supply

You set max supply. 100% is minted or issued to you, then deposited into one Alcor position. The pool is one-sided: it starts just outside the range, so the position is entirely your token. Buyers pay the quote as they walk from the start price toward the top.

The fee on that pool is 0.05%, 0.30%, or 1.00%. You pick it. It is not a tax on transfers. It is the swap fee, and it accrues to the locked position, which is yours.

Range width is the other half of the price. A tight range means a little money buys a lot of the supply. A wide range means the same money buys less, and the top of the range is far away. The screen shows what $100 buys at the width you picked. Raise the starting market cap and that percent falls. The shot below is a near-zero start on purpose, so the width is the only thing changing.

![Fee tier and range width](assets/launch-range-width.png)

Transfer tax is separate, and you set it on the previous step. Create writes 0%. `setfees` is the first real split. The sum cannot go above 100%, and a later call cannot raise the total or lower reflection.

![Transfer tax](assets/launch-fees.png)

On `3asy` the split is reflection and burn. On `fl3x` and `for3x` you also set a project rate and a project account (blank stays the issuer). On `for3x` you can give angel numbers and the jackpot a share of the reflection slice only. That does not add tax on top.

## Decide your pre-sale, or go live

Insiders are optional. Leave the box off and everyone starts at liftoff.

Turn it on and you set two clocks: when insiders may buy, and when the public launch is. Insider time has to come first. You can cap how much of supply an insider may hold, add a higher cap for someone who proves a locked LP position, and require a hold, an NFT, or LP. Invites are a list you sign. They are not a buy gate by themselves.

![Presale is optional](assets/launch-insiders.png)

If a presale row exists, liftoff fills the pool and leaves `launched` false until you call `golive`. Until then, transfers stay inside the club rules.

## The EASY hold

This is not a fee. At liftoff the contract reads your EASY balance on `mon3y` and refuses if it is short.

Full hold, whole tokens, times (tokens you already launched on **this** contract + 1):

| Program | Account | Full hold |
| --- | --- | --- |
| easyflex | `3asy` | 5,000 EASY |
| complexflex | `fl3x` | 10,000 EASY |
| flexforex | `for3x` | 50,000 EASY |

The discount clock is in the contracts (`promo_start` = 9 Sep 2026 00:00 UTC, then one step every 30 days):

- EASY, WON, GRAMS, and MEME always use 10% of the full hold. That price does not rise.
- A verified first launch against GEASY (`fl3x`) needs no EASY hold. Later GEASY launches use the monthly discount.
- XPR, XMD, LOAN, and xtokens use the monthly discount: 90% off in the first 30 days, then 80% off, then 70%, and so on until the discount is 0 and the full hold is due.

This month (still inside the first 30 days) a first `for3x` token is 5,000 EASY, which is 10% of 50,000. On 9 Oct 2026 the non-flex quotes step to 20% of the full hold. Flex quotes stay at 10%.

## Launch

You sign a sequence. The flex contract does not sign Alcor for you.

1. `create`
2. `setfees`
3. `issue` on `3asy`, or `mint` on `fl3x` and `for3x`, 100% to you
4. `startlaunch` (quote amount 0, swap-to-quote default on)
5. Alcor `createpool`, activate the pool if it is inactive, deposit the supply, add the one-sided range, `lockpos`
6. Optional `setpresale` (and invites) after the lock
7. `liftoff`
8. `addpool` of the launch quote pair

Do not put liftoff in the same transaction as `createpool`. After a successful create, the token, tax, quote, and range stay frozen in the wizard so a later click cannot drift them. Insiders stay editable until `setpresale` is signed.

The chain checks the lock at liftoff: unlock time must still be at least 90 days out (`MIN_LOCK_SECS`). The UI minimum is 91 days so a slow signing session does not fail that check.

## Promote

The calendar picks up insider dates and the public launch. People who already care will tell the next person if the presale actually fills. A quiet pool does not become loud because the contract exists. Say the start price, the lock length, and what $100 buys. Those three numbers are the ad.

## Send the rain and call the angels

After liftoff, transfer tax sits in `reflection_pool` until someone calls `makeitrain`. That call splashes **38.2%** of the pool to holders (vaults such as `swap.alcor` are left out of the share count). Anyone connected can press the square. You should press it yourself the first time, so holders see the pay.

![Make it rain](assets/make-it-rain.png)

On `for3x`, the same page has angel squares and jackpot squares. `pullangel` draws against holders who set an angel number. `pulljackpot` draws winners who meet the minimum hold. Both need a pot above zero, and both are public calls. The game guide is the click-by-click version.
