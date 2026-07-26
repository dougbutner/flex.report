# Tokenomics

Take it EASY 👄 💰 You have EASY 👄 → You are given more EASY.

Get a Wallet | [Buy EASY](https://alcor.exchange/v/xpr/swap?input=XUSDC-xtokens&output=EASY-mon3y) | [Analytics](https://alcor.exchange/v/xpr/analytics/tokens/EASY-mon3y) | [Farms](https://alcor.exchange/v/xpr/analytics?tab=farms) | [Telegram](https://t.me/flextokens)

## EASY

| | |
| --- | --- |
| **Max supply** | 21M EASY (100% minted day one into liquidity) |
| **Day-one placement** | 100% in stablecoin pools (no presale) |
| **Transfer tax** | 2% reflection (opt-out) |
| **Earn threshold** | Hold 100+ EASY · 1,000 EASY in pool to pay |
| **Payout smoothing** | Each `distribute` pays **61.8%** of each flexer’s pro-rata share (Fibonacci smoothing); the rest stays in the pool for later rounds |
| **Protocol fee** | **0.3%** of/from the reflection pool per payout action ([Legal & Terms](legal-and-terms.md)) |
| **Bridges** | Solana, Base, Optimism, BSC |

## Infinitely Liquid

Fair launched 100% max supply into Alcor pools from $0.01-100,000 USD(c).

The math keeping EASY on the up and up is… easy… Every token was purchased with at least 0.01 USD(c) and is instantly redeemable in the same liquidity pools it was originally purchased from. There’s over 25K USD in stablecoins (USDC, USDT, PyUSD, XMD, and PAX) backing EASY, and growing.

Pools earn some profit on EASY/USD(c) swap fee of 0.05%-1%.

EASY provides a highly-used service to the market, liquidity for humans and bots to trade. Over 1.6M USD in 90d volume (and growing).

```mermaid
flowchart TB
  P[EASY pool swap fees]
  P --> I["38.2% invite.mon3y"]
  P --> C["38.2% Contributor Club (reflections)"]
  P --> M["23.6% MEME buyback → glitch.mon3y"]
```

- **38.2%** → [`invite.mon3y`](https://explorer.xprnetwork.org/account/invite.mon3y) (Welcome Program)
- **38.2%** → Contributor Club budget (`reflections`)
- **23.6%** → MEME buyback to [`glitch.mon3y`](https://explorer.xprnetwork.org/account/glitch.mon3y)

Reasoning: the Welcome Program has led to many smaller accounts, which means less EASY to give out at Contributor Club meetings, so a larger share now funds invites + Club, with the rest buying MEME.

## Day-one liquidity allocation

4,200,000 EASY paired day-one into each stable pool on `hands.mon3y` (100% of supply):

```mermaid
flowchart LR
  S["21M EASY"] --> A["4.2M × XMD"]
  S --> B["4.2M × XUSDC"]
  S --> C["4.2M × XPYUSD"]
  S --> D["4.2M × XPAX"]
  S --> E["4.2M × XUSDT"]
```

| Pool | EASY day one | Alcor |
| --- | ---: | --- |
| EASY / XMD | 4,200,000 | [4067](https://alcor.exchange/v/xpr/analytics/pools/4067) |
| EASY / XUSDC | 4,200,000 | [4065](https://alcor.exchange/v/xpr/analytics/pools/4065) |
| EASY / XPYUSD | 4,200,000 | [4068](https://alcor.exchange/v/xpr/analytics/pools/4068) |
| EASY / XPAX | 4,200,000 | [4070](https://alcor.exchange/v/xpr/analytics/pools/4070) |
| EASY / XUSDT | 4,200,000 | [4066](https://alcor.exchange/v/xpr/analytics/pools/4066) |
| **Total** | **21,000,000** | |

Live depth and volume: [Market Stats](market-stats.md) · Venus unlocks (one pool at a time): [Celestial Buybacks](celestial-buybacks.md).

## Flex family (all tokens)

<!-- LIVE:FLEX-TOKENOMICS -->
*Live snapshot: **2026-07-25 21:32 UTC** · Alcor + chain `stat` tables*

### Supply (all Flex tokens)

| Token | Supply | Max | Price (USD) | Reflection pool |
| --- | ---: | ---: | ---: | ---: |
| **EASY** | 21,000,000 | 21,000,000 | $0.016271 | 1,322.4338 EASY |
| **WON** | 1,000,000 | 1,000,000 | $1.628887 | 6.8844 WON |
| **MEME** | 9,986,257,831,743 | 10,000,000,000,000 | $0.000000 | 53,291,849.6836 MEME |
| **GRAMS** | 1,000,000,000 | 1,000,000,000 | $132.562443 | 0.0818 GRAMS |

### Fee rates

| Token | Reflection | Burn | Team | Hold to earn | Pool to pay | Tagline |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| **EASY** | 2% | - | - | 100+ | 1,000 EASY | Take it EASY |
| **WON** | 2.2% | - | 0.8% | 1.0+ | 8 WON | We WON |
| **MEME** | 1% | 1% | - | 1M+ | 10M MEME | burns + farms |
| **GRAMS** | 1.1% | - | 0.11% | see contract | see contract | gold-backed |

### Major-token USD backing (live)

USD value of **major** counter-assets sitting in each token’s Alcor pools (not full Alcor `tvlUSD`).

| Token | Total major backing | Breakdown |
| --- | ---: | --- |
| **EASY** | **$59,376** | XMD $12,070, XUSDC $12,354, XPYUSD $11,477, XPAX $11,577, XUSDT $11,899 |
| **WON** | **$1,537** | EASY $1,446, XPR $90.72 |
| **MEME** | **$1,269** | XPR $328.48, XUSDC $272.53, EASY $668.16 |
| **GRAMS** | **$1,160** | XPAXG $1,160 |

- **EASY majors:** XMD · XUSDC · XPYUSD · XPAX · XUSDT  
- **WON majors:** EASY · XPR  
- **MEME majors:** XPR · XUSDC · EASY  
- **GRAMS majors:** XPAXG  

<!-- /LIVE:FLEX-TOKENOMICS -->

Each may have additional farming rewards. EASY alone has a protocol fee path that funds Flex volunteer work and infrastructure (see [Legal & Terms](legal-and-terms.md)).
