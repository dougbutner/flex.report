# Celestial Buybacks

![Celestial Buybacks](assets/heroes/celestial-buybacks.png)

Scheduled buybacks on celestial time. Day-one project liquidity stays **date-locked** until a Venus window; then **one** pool is cleared and re-seeded higher.

## Venus Buybacks

**Passed.** The five project EASY/stable pools are locked until Venus alignments (**≈1.6 years / 584 days** apart, inferior conjunction). At each alignment, **exactly one** pool unlocks for a buyback: that pool is cleared, and the stables + EASY go back into pools at a **new range** (end still **$100,000 / EASY**; new start = current market price). All other pools stay locked.

Background: [YouTube explanation](https://www.youtube.com/watch?v=HoZTD60D1lw).

| | |
| --- | --- |
| **Cadence** | Every **≈1.6 years** (Venus synodic · ≈584 days) |
| **What unlocks** | **One** of the five project EASY/stable pools |
| **What happens** | Clear that pool → redeploy stables + EASY at a higher band |
| **Range** | New start = market price · end still **$100,000 / EASY** |

### Locked project pools

| Pool | Alcor |
| --- | --- |
| EASY / XMD | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) |
| EASY / XUSDC | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) |
| EASY / XPYUSD | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) |
| EASY / XPAX | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) |
| EASY / XUSDT | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) |

![Venus buyback loop](assets/diagrams/venus-loop.png)

Between Venus beats, day-to-day support still comes from the living loop: **stablecoin-side** swap fees buy EASY and re-pool; **EASY-side** fees fund Welcome / Club / MEME. See [Tokenomics](tokenomics.md) and [Liquidity & Farms](core-tech/liquidity-and-farms.md).

## WON buybacks (superior conjunction)

**WON** uses the **same ≈584-day** Venus cadence, keyed to **superior conjunction** (opposite EASY’s inferior conjunction). Beats sit about **≈292 days** apart inside the cycle.

| | |
| --- | --- |
| **Cadence** | Every **≈584 days**, superior conjunction |
| **What** | Buybacks supporting the WON / EASY stack |
| **Relation to EASY** | Same period; opposite conjunction (≈292 days apart) |

![WON and EASY Venus series](assets/diagrams/won-half-step.png)

Live depth: [Market Stats](market-stats.md) · Trade: [Swap EASY](https://alcor.exchange/v/xpr/swap?input=XUSDC-xtokens&output=EASY-mon3y).
