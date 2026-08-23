# Improvements and research notes

Private. Not a GitBook page.

## Why not Behance as the default pack source

Behance is a **portfolio** host, not a rights-cleared icon CDN. Scraping project PNGs risks license and ToS issues. Better defaults for this repo:

| Source | Why |
| --- | --- |
| **Lucide** (ISC) | Consistent stroke icons; already bootstrapped under `icons/lucide/` |
| **Open Crypto Icons** | BTC/ETH/SOL/stables for market teaching slides |
| **Flex token art** (in-repo) | Brand-correct EASY/WON/MEME/GRAMS |
| **Generated chrome** (Pillow) | Arrows, panels, pie, pyramid, flywheel match brand colors exactly |
| **Your `preferred-images/`** | Hand-picked art only you add |

If you want Behance-style assets: download packs yourself into `preferred-images/` with license notes, then tell the agent the filenames.

## Suggested next steps (priority order)

### 1. YAML / JSON scene files

Describe a slide as data the CLI renders:

```yaml
title: PVC Operating System
subtitle: Pleasant · Valuable · Connected
layout: cards
cards:
  - title: Pleasant
    sub: Feels good to be in
  - title: Valuable
    sub: Creates real value
```

Benefits: repeatable Skool decks, diffs in git, less prompt drift.

### 2. Template library named after course modules

Ship named presets: `flex-foundations/what-is-flex-token`, `markets/clmm`, `ambassadors/host-checklist`. Agent picks a preset + fills text.

### 3. Auto layout QA

After save: detect text overflow (bbox vs panel), low contrast, empty panels. Fail the script if title exceeds width.

### 4. Preferred-images index

When you drop files, run a tiny indexer that writes `preferred-images/index.json` with width/height/has_alpha. Agent reads the index instead of listing binaries blindly. (Indexer may write the index file only; still never invent image assets.)

### 5. Optional AI texture pass (controlled)

Keep Pillow for type + structure (brand-safe). Optionally run a **local** img2img only on background atmosphere, never on text. Gate behind an explicit flag so GitBook screenshots stay crisp and identical.

### 6. Rasterize pipeline hardening

Current Lucide path: curl SVG → `@resvg/resvg-js`. Commit PNGs; keep `scripts/.resvg-tools/node_modules` gitignored. Add `scripts/rasterize_svgs.mjs` as the one-button re-raster.

### 7. Brand kit export for Skool / Canva

Export a zip of fonts + swatches + 20 chrome PNGs for human editors who are not in Cursor.

### 8. Live data overlays

Reuse `update-stats` JSON to stamp “EASY mcap” / “24h volume” onto market teaching slides so Skool graphics stay current.

### 9. Accessibility / social crops

Generate 1:1 and 9:16 crops from the same scene for Instagram / Shorts, keeping the same type system.

### 10. Do not

- Do not put element pools under `assets/` (GitBook would surface them).
- Do not auto-commit scraped Behance files.
- Do not let the agent write into `preferred-images/`.

## Tooling stack recommendation

Stay on **Pillow + bundled fonts + element PNGs**. It already matches every public hero. Add scene YAML and QA next; only then consider generative fill for backgrounds.
