#!/usr/bin/env python3
"""Compose Flex Report / Skool heroes in the black + yellow Bebas style.

Examples (from repo root):

  python3 .cursor/skills/make-hero-image/scripts/make_hero.py \\
    --title "What is a Flex Token?" \\
    --subtitle "Reflection-style asset on XPR" \\
    --flow "Transfer|Tax fills pool|Send It|Rewards" \\
    --out assets/heroes/skool/foundations/demo.png

  python3 .cursor/skills/make-hero-image/scripts/make_hero.py \\
    --title "EASY Life" --subtitle "from flex.town" \\
    --layout cover --out /tmp/easy-life.png
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SKILL = Path(__file__).resolve().parents[1]
ELEMS = SKILL / "image-elements"
FONTS = SKILL / "fonts"
REPO = SKILL.parents[2]

BLACK = (0, 0, 0)
YELLOW = (255, 214, 0)
GOLD = (245, 186, 32)
MUTED = (160, 140, 50)
DIM = (28, 28, 28)
W, H = 1280, 720


def _font_path(name: str) -> Path:
    bundled = FONTS / name
    if bundled.exists():
        return bundled
    # fallbacks on macOS user fonts
    alts = {
        "BebasNeue-Bold.otf": [
            Path.home() / "Library/Fonts/BebasNeue Bold.otf",
            Path.home() / "Library/Fonts/BebasNeue Regular.otf",
        ],
        "OpenSans-Bold.ttf": [Path.home() / "Library/Fonts/OpenSans-Bold.ttf"],
    }
    for p in alts.get(name, []):
        if p.exists():
            return p
    raise FileNotFoundError(f"Missing font {name}. Place it in {FONTS}")


def bebas(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(_font_path("BebasNeue-Bold.otf")), size)


def openb(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(_font_path("OpenSans-Bold.ttf")), size)


def canvas() -> Image.Image:
    return Image.new("RGB", (W, H), BLACK)


def soft(d: ImageDraw.ImageDraw, box, radius: int = 12) -> None:
    d.rounded_rectangle(box, radius=radius, fill=DIM)


def title_block(
    d: ImageDraw.ImageDraw,
    title: str,
    subtitle: str | None = None,
    y: int = 48,
    title_size: int = 64,
) -> None:
    # Never use em dashes in rendered copy
    title = title.replace("\u2014", ":").replace("\u2013", "-")
    if subtitle:
        subtitle = subtitle.replace("\u2014", ":").replace("\u2013", "-")
    d.text((56, y), title.upper(), fill=YELLOW, font=bebas(title_size))
    if subtitle:
        d.text((56, y + int(title_size * 1.12)), subtitle, fill=GOLD, font=openb(26))


def arrow_h(d: ImageDraw.ImageDraw, x0: int, x1: int, y: int) -> None:
    d.line([(x0, y), (x1 - 10, y)], fill=GOLD, width=3)
    d.polygon([(x1, y), (x1 - 12, y - 8), (x1 - 12, y + 8)], fill=GOLD)


def flow_boxes(
    d: ImageDraw.ImageDraw,
    labels: list[str],
    y: int = 320,
    box_h: int = 120,
    gap: int = 24,
    font_size: int = 22,
) -> None:
    n = len(labels)
    avail = W - 112
    box_w = max(90, min(260, int((avail - (n - 1) * gap) / n)))
    total = n * box_w + (n - 1) * gap
    x0 = (W - total) // 2
    for i, lab in enumerate(labels):
        x = x0 + i * (box_w + gap)
        soft(d, [x, y, x + box_w, y + box_h])
        lines = lab.split("\n")
        fs = font_size if max(len(l) for l in lines) < 16 else max(14, font_size - 4)
        f = openb(fs)
        mid = y + box_h // 2
        step = fs + 6
        start = mid - (len(lines) - 1) * step / 2
        for li, line in enumerate(lines):
            d.text(
                (x + box_w // 2, start + li * step),
                line,
                fill=YELLOW,
                font=f,
                anchor="mm",
            )
        if i < n - 1:
            arrow_h(d, x + box_w + 4, x + box_w + gap - 2, y + box_h // 2)


def grid_cards(
    d: ImageDraw.ImageDraw,
    items: list[tuple[str, str | None]],
    y: int = 230,
    cols: int = 3,
    box_h: int = 130,
) -> None:
    gap_x, gap_y, pad = 24, 24, 64
    avail = W - 2 * pad
    box_w = (avail - (cols - 1) * gap_x) // cols
    for i, (title, sub) in enumerate(items):
        r, c = divmod(i, cols)
        x = pad + c * (box_w + gap_x)
        yy = y + r * (box_h + gap_y)
        soft(d, [x, yy, x + box_w, yy + box_h])
        cx = x + box_w // 2
        if sub:
            d.text(
                (cx, yy + box_h // 2 - 18),
                title.upper(),
                fill=YELLOW,
                font=bebas(28),
                anchor="mm",
            )
            d.text(
                (cx, yy + box_h // 2 + 22),
                sub,
                fill=GOLD,
                font=openb(16 if len(sub) > 26 else 18),
                anchor="mm",
            )
        else:
            d.text(
                (cx, yy + box_h // 2),
                title.upper(),
                fill=YELLOW,
                font=bebas(26),
                anchor="mm",
            )


def load_element(*parts: str, size: int | None = None) -> Image.Image:
    path = ELEMS.joinpath(*parts)
    if not path.exists():
        raise FileNotFoundError(path)
    im = Image.open(path).convert("RGBA")
    if size:
        im = im.resize((size, size), Image.Resampling.LANCZOS)
    return im


def paste_center(base: Image.Image, overlay: Image.Image, xy: tuple[int, int]) -> None:
    x, y = xy
    base.paste(overlay, (x, y), overlay)


def resolve_icon(name: str, size: int = 96) -> Image.Image | None:
    """Resolve an icon from lucide / geometric / chrome / tokens / crypto / preferred."""
    candidates = [
        ELEMS / "icons" / "lucide" / f"{name}.png",
        ELEMS / "icons" / "geometric" / f"{name}.png",
        ELEMS / "chrome" / f"{name}.png",
        ELEMS / "tokens" / f"{name}.png",
        ELEMS / "icons" / "crypto" / f"{name}.png",
        ELEMS / "icons" / "crypto" / f"{name}-white.png",
        ELEMS / "icons" / "crypto" / f"{name}-colored.png",
        ELEMS / "preferred-images" / f"{name}.png",
    ]
    for p in candidates:
        if p.exists():
            im = Image.open(p).convert("RGBA")
            return im.resize((size, size), Image.Resampling.LANCZOS)
    return None


def layout_flow(
    title: str, subtitle: str | None, labels: list[str], icons: list[str] | None
) -> Image.Image:
    img = canvas()
    d = ImageDraw.Draw(img)
    title_block(d, title, subtitle)
    flow_boxes(d, labels, y=300 if not icons else 360)
    if icons:
        n = len(icons)
        gap = 40
        size = 88
        total = n * size + (n - 1) * gap
        x0 = (W - total) // 2
        for i, name in enumerate(icons):
            icon = resolve_icon(name, size)
            if icon:
                paste_center(img, icon, (x0 + i * (size + gap), 220))
    return img


def layout_cards(
    title: str, subtitle: str | None, cards: list[tuple[str, str | None]]
) -> Image.Image:
    img = canvas()
    d = ImageDraw.Draw(img)
    title_block(d, title, subtitle)
    grid_cards(d, cards)
    return img


def layout_cover(title: str, subtitle: str | None, tagline: str | None) -> Image.Image:
    img = canvas()
    d = ImageDraw.Draw(img)
    title_block(d, title, subtitle, y=80, title_size=88)
    if tagline:
        d.text((56, 280), tagline, fill=YELLOW, font=bebas(52))
    # brand token watermark
    tok = resolve_icon("easy", 220)
    if tok:
        paste_center(img, tok, (W - 320, H - 340))
    return img


def layout_split(
    title: str,
    subtitle: str | None,
    left: tuple[str, str],
    right: tuple[str, str],
) -> Image.Image:
    img = canvas()
    d = ImageDraw.Draw(img)
    title_block(d, title, subtitle)
    soft(d, [80, 230, 600, 600])
    soft(d, [680, 230, 1200, 600])
    d.text((340, 340), left[0].upper(), fill=YELLOW, font=bebas(48), anchor="mm")
    d.text((340, 440), left[1], fill=GOLD, font=openb(24), anchor="mm")
    d.text((940, 340), right[0].upper(), fill=YELLOW, font=bebas(48), anchor="mm")
    d.text((940, 440), right[1], fill=GOLD, font=openb(24), anchor="mm")
    return img


def parse_cards(raw: str) -> list[tuple[str, str | None]]:
    # "Title=Sub|Title2=Sub2|Title3"
    out = []
    for part in raw.split("|"):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            a, b = part.split("=", 1)
            out.append((a.strip(), b.strip()))
        else:
            out.append((part, None))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Make a Flex black/yellow hero image")
    ap.add_argument("--title", default=None)
    ap.add_argument("--subtitle", default=None)
    ap.add_argument(
        "--layout",
        choices=["flow", "cards", "cover", "split"],
        default="flow",
    )
    ap.add_argument(
        "--flow",
        default=None,
        help="Pipe-separated flow labels. Use \\n for line breaks inside a box.",
    )
    ap.add_argument(
        "--cards",
        default=None,
        help='Pipe-separated cards: "Title=Sub|Title2=Sub2"',
    )
    ap.add_argument(
        "--icons",
        default=None,
        help="Pipe-separated icon names from image-elements (wallet|coins|…)",
    )
    ap.add_argument("--tagline", default=None, help="Cover layout large line")
    ap.add_argument(
        "--left",
        default=None,
        help='Split left "TITLE=subtitle"',
    )
    ap.add_argument(
        "--right",
        default=None,
        help='Split right "TITLE=subtitle"',
    )
    ap.add_argument("--out", default=None, help="Output PNG path")
    ap.add_argument(
        "--list-elements",
        action="store_true",
        help="Print catalog.json and exit",
    )
    args = ap.parse_args()

    if args.list_elements:
        cat = ELEMS / "catalog.json"
        print(cat.read_text() if cat.exists() else "No catalog yet. Run bootstrap_elements.py")
        return

    if not args.title or not args.out:
        ap.error("--title and --out are required unless --list-elements")

    if args.layout == "flow":
        labels = []
        if args.flow:
            labels = [p.strip().replace("\\n", "\n") for p in args.flow.split("|") if p.strip()]
        else:
            labels = ["Step 1", "Step 2", "Step 3"]
        icons = [p.strip() for p in args.icons.split("|")] if args.icons else None
        img = layout_flow(args.title, args.subtitle, labels, icons)
    elif args.layout == "cards":
        cards = parse_cards(args.cards or "One=Detail|Two=Detail|Three=Detail")
        img = layout_cards(args.title, args.subtitle, cards)
    elif args.layout == "cover":
        img = layout_cover(args.title, args.subtitle, args.tagline)
    else:
        def split_pair(s: str | None, default: tuple[str, str]) -> tuple[str, str]:
            if not s:
                return default
            if "=" in s:
                a, b = s.split("=", 1)
                return a.strip(), b.strip()
            return s, ""

        img = layout_split(
            args.title,
            args.subtitle,
            split_pair(args.left, ("LEFT", "detail")),
            split_pair(args.right, ("RIGHT", "detail")),
        )

    out = Path(args.out)
    if not out.is_absolute():
        out = REPO / out
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
