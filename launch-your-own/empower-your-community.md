# Empower your community

A normal launch sells a bag once. A Flex token keeps paying holders out of transfer tax, then lets anyone send that pay. You are not hiring a team to run a rewards site. The contract already does the split. Your job is to pick numbers your people can understand, lock the pool long enough that they trust it, and show up when it is time to send the rain.

The value, in one pass:

- Holders can be paid in your token, or they can flex that pay into the quote (EASY, WON, GRAMS, MEME, or whatever you launched against).
- You choose the transfer tax. It starts at 0. You cannot raise the total later, and you cannot cut reflection once it is set.
- You choose the Alcor fee on the pool (0.05%, 0.30%, or 1.00%). That fee accrues to your locked position.
- You choose how long the liquidity stays locked. The chain requires at least 90 days remaining at liftoff. The slider starts at 91 so the check still passes after you finish signing.
- On flexforex (`for3x`) you can also split part of the reflection into angel numbers and a jackpot. Anyone can call those, the same way anyone can make it rain.

There is no Flex setup invoice. Liftoff checks that you **hold** EASY on `mon3y`. The contract does not spend that EASY.

## How this compares

Figures below are what each venue published, or what a public indexer returned. Ranks move. Where a number was not published, the cell says so. Pump.fun is treated as the most popular by tokens launched. Bags was described as the next Solana factory, and four.meme as the BNB factory, in a 31 Aug 2026 comparison. That same week, ranked by fees, Pons led, then pump.fun, then Flap.sh. Fee rank and token-count rank are not the same list.

| | Setup cost | Recurring fee | Swap pool % | Swap fees that go to you | Competition |
| --- | --- | --- | --- | --- | --- |
| Flex | 0. EASY hold is a balance check, not a payment. | You set the transfer tax (starts at 0). Flex quotes take no protocol skim. Other quotes start at 0.25% + 0.25% of the rain, and that pair can rise once after the LP unlocks. | You pick 0.05%, 0.30%, or 1.00%. | 100% of that pool fee accrues to your locked position. | A full pool per token, not a mint factory. |
| SimpleDEX | 20,000 XPR to create (admin can change it; read `simplelaunch` fees before you pay). | 1% buy and 1% sell on the curve. | 0.30% default pool fee after graduation, plus a protocol cut on top. | 50% of the curve fee. Graduated liquidity is locked to the protocol, not paid to you. | 468 tokens on the public indexer (Sep 2026). |
| Vibrr | Not published. vibrr.ai is a proof-of-engagement app with a DEX. It does not post a create-any-token fee. | Not published as a launcher schedule. | Not published. | Not published. | Not a token factory. |
| pump.fun | 0 SOL to create (31 Aug 2026 writeup). Graduation was about 0.015 SOL. | 1.25% of trades, split between creator and protocol. The split ratio was not stated in that source. | You do not set a pool fee. The 1.25% is the trade fee. | Split with the protocol. | 11,900,000+ tokens (count dated 10 Jun 2026). |
| Bags (next Solana factory in that writeup) | Not published. | Creators earn 1% of every trade. | Not published. | That 1% is the published creator share. | Token count not published. |
| four.meme (BNB factory in that writeup) | About 0.005 BNB. | 1% trade fee. | Curve, then PancakeSwap. You do not set the percent. | Creator share of the 1% was not stated. | Token count not published. |

Sources for the other venues: [SimpleDEX how it works](https://simpledex.fun/how-it-works) and `https://indexer.protonnz.com/api/stats` (468 tokens), [vibrr.ai](https://vibrr.ai/), and the 31 Aug 2026 launchpad comparison that recorded the pump.fun, Bags, and four.meme rows. Flex numbers are the live contracts (`3asy`, `fl3x`, `for3x`) and the Launch screen.
