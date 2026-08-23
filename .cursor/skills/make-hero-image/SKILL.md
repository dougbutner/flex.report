---
name: make-hero-image
description: >-
  Create black/yellow Flex Report and Skool hero images with Bebas Neue + Open
  Sans Bold via Pillow (same style as assets/heroes). Use when the user asks to
  make a hero image, Skool graphic, diagram slide, educational PNG, or run the
  make-hero-image skill.
---

# Make Hero Image

Private tooling. Lives under `.cursor/skills/make-hero-image/`. **Never** link it in `SUMMARY.md`. Do not reference these paths from public GitBook pages.

## When

User asks to create / regenerate a hero, Skool course graphic, educational diagram, or black/yellow Flex-style PNG.

## Style (locked)

| Token | Value |
| --- | --- |
| Canvas | 1280×720 RGB |
| Background | `#000000` |
| Yellow | `(255, 214, 0)` |
| Gold | `(245, 186, 32)` |
| Muted | `(160, 140, 50)` |
| Soft panel | `(28, 28, 28)` rounded, **no yellow outline** |
| Title font | Bebas Neue Bold (bundled in `fonts/`) |
| Body font | Open Sans Bold (bundled in `fonts/`) |
| Copy | No em dashes / en dashes (use `:`, `-`, or `to`) |

Match existing heroes in `assets/heroes/` and Skool art in `assets/heroes/skool/`.

## Element pool

Path: `.cursor/skills/make-hero-image/image-elements/`

| Folder | Who writes | Use |
| --- | --- | --- |
| `tokens/` | Agent may refresh from `tokens/` | EASY, WON, MEME, GRAMS |
| `chrome/` | Agent / bootstrap | arrows, panels, rings, pie, waves |
| `icons/geometric/` | Agent / bootstrap | simple yellow icons |
| `icons/lucide/` | Bootstrap download | Lucide (ISC) yellow PNGs |
| `icons/crypto/` | Bootstrap download | BTC/ETH/SOL/USDC/USDT/XRP |
| `preferred-images/` | **User only** | Agent must **never** create, edit, delete, or overwrite files here. Read-only for composition. |

Catalog: `image-elements/catalog.json`  
Sources / licenses: `image-elements/SOURCES.md`

### Preferred images (user-only)

1. Drop PNGs (ideally transparent) into `image-elements/preferred-images/`.
2. Tell the agent the filename to use.
3. Agent may **read / paste** them into compositions. Agent must not invent content into that folder.

## Do this

1. Read this skill. Optionally skim [reference.md](reference.md).
2. Prefer the CLI over one-off inline Python:

```bash
python3 .cursor/skills/make-hero-image/scripts/make_hero.py \
  --title "What is a Flex Token?" \
  --subtitle "Reflection-style asset on XPR" \
  --layout flow \
  --flow "Transfer|Tax fills pool|Send It|Rewards" \
  --icons "wallet|coins|zap|check" \
  --out assets/heroes/skool/foundations/example.png
```

Layouts: `flow` · `cards` · `cover` · `split`

List pool:

```bash
python3 .cursor/skills/make-hero-image/scripts/make_hero.py --list-elements
```

3. For custom layouts beyond the CLI, write Pillow code **using the same colors/fonts helpers** as `scripts/make_hero.py` (import or copy the helpers). Paste icons via `resolve_icon()` / `load_element()`.
4. Refresh chrome / Lucide / crypto if needed:

```bash
python3 .cursor/skills/make-hero-image/scripts/bootstrap_elements.py
python3 .cursor/skills/make-hero-image/scripts/bootstrap_elements.py --download
# then rasterize SVGs with scripts/rasterize_svgs.mjs if PNGs are missing
```

5. Save public-facing outputs under `assets/heroes/` or `assets/heroes/skool/…` as appropriate. Keep the element pool private under `.cursor/`.
6. Spot-check the PNG with the Read tool (vision). Fix overlaps / overflow.

## Hard rules

- Do **not** add this skill, `image-elements/`, or preferred drops to GitBook navigation.
- Do **not** write into `preferred-images/`.
- Do **not** scrape Behance / paid packs into the repo without explicit user license OK.
- Prefer Lucide + geometric + chrome + Flex tokens for consistency.
- Keep text short. One idea per image.

## Next-step research

See [IMPROVEMENTS.md](IMPROVEMENTS.md).
