# Liquidity & Farms

100% of supply stashed in stablecoin pools day 1.  
100% of USD(c) profits used to purchase EASY (raising the redeemable price of EASY).  
Extensive rewards pools available. Farm MEME by providing liquidity.

```mermaid
flowchart TB
  V[Volume in EASY pools] --> F[Swap fees]
  F -->|USD profits| Buy[Buy EASY]
  F -->|EASY profits| Re[Re-pool]
  Buy --> Floor[Higher redeemable floor]
  Re --> Club[~33% Club]
  Re --> Inf[Rest stays in pools]
  LP[`reflections` LP + MEME farm fees] --> Rew[Rewards pool]
```

Liquidity positions are managed within the `reflections` account and go back to the rewards pool. View them on Alcor anytime by searching `reflections`.

Additionally, `m3m3` feeds the `reflections` account with their earned LP fees.

Farms: [alcor.exchange/v/xpr/analytics?tab=farms](https://alcor.exchange/v/xpr/analytics?tab=farms)
