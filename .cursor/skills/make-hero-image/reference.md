# Style reference

## Composition patterns (used across heroes / Skool)

1. **Title block**: top-left Bebas title + Open Sans gold subtitle.
2. **Flow**: soft DIM panels + gold arrows (Wallet → Swap → Flex → Stack).
3. **Cards grid**: 2–3 columns of soft panels (title + short sub).
4. **Cover**: oversized title, optional tagline, optional token watermark.
5. **Split**: two equal panels for contrasts (Reflect vs Flex, Hustle vs Rhythm).
6. **Diagram extras**: paste `chrome/pie-*.png`, `pyramid-outline`, `flywheel-arcs`, `breath-wave`, Lucide icons above a flow.

## Spacing

- Outer pad ≈ 56–64px
- Soft panel radius 12
- Flow box height ≈ 100–140
- Avoid yellow box outlines (older draft style); filled DIM only

## Icon resolution order (`resolve_icon`)

1. `icons/lucide/{name}.png`
2. `icons/geometric/{name}.png`
3. `chrome/{name}.png`
4. `tokens/{name}.png`
5. `icons/crypto/{name}.png` then `{name}-white.png` / `{name}-colored.png`
6. `preferred-images/{name}.png` (read-only)

## Good educational defaults

| Topic | Icons / chrome |
| --- | --- |
| Wallet / onboard | `wallet`, `link`, tokens |
| Reflections | `refresh-cw`, `coins`, flow |
| LP / CLMM | `layers`, `bar chart geometric`, `bars-up` |
| Ambassadors | `megaphone`, `users`, `share-2` |
| Breath / life | `breath-wave`, `breath`, `heart-pulse` |
| Fee split | `pie-382-382-236` |
| Frameworks | `compass`, `pyramid-outline`, `flywheel-arcs` |
