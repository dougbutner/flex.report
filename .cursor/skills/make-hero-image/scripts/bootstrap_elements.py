#!/usr/bin/env python3
"""Build image-elements pool: chrome shapes, geometric icons, optional Lucide/crypto downloads.

Usage (from repo root):
  python3 .cursor/skills/make-hero-image/scripts/bootstrap_elements.py
  python3 .cursor/skills/make-hero-image/scripts/bootstrap_elements.py --download

--download fetches Lucide (ISC) + open-crypto-icons SVGs and rasterizes to yellow PNGs.
Requires: Pillow. Optional for SVG raster: cairosvg (preferred) or svglib+reportlab.
"""
from __future__ import annotations

import argparse
import io
import json
import math
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw

SKILL = Path(__file__).resolve().parents[1]
ELEMS = SKILL / "image-elements"
CHROME = ELEMS / "chrome"
GEOM = ELEMS / "icons" / "geometric"
LUCIDE = ELEMS / "icons" / "lucide"
CRYPTO = ELEMS / "icons" / "crypto"

YELLOW = (255, 214, 0, 255)
GOLD = (245, 186, 32, 255)
BLACK = (0, 0, 0, 255)
CLEAR = (0, 0, 0, 0)
UA = {"User-Agent": "flex.report-make-hero-image/1.0"}

LUCIDE_NAMES = [
    "wallet",
    "arrow-right",
    "arrow-left",
    "arrow-up",
    "arrow-down",
    "chevrons-right",
    "refresh-cw",
    "repeat",
    "link",
    "users",
    "user",
    "heart",
    "star",
    "zap",
    "flame",
    "sun",
    "moon",
    "leaf",
    "trees",
    "mountain",
    "waves",
    "wind",
    "brain",
    "eye",
    "target",
    "compass",
    "gauge",
    "layers",
    "layout-dashboard",
    "pie-chart",
    "bar-chart-3",
    "line-chart",
    "coins",
    "circle-dollar-sign",
    "hand-coins",
    "landmark",
    "building-2",
    "lock",
    "unlock",
    "shield",
    "key",
    "fingerprint",
    "clock",
    "calendar",
    "hourglass",
    "timer",
    "activity",
    "dumbbell",
    "utensils",
    "bed",
    "alarm-clock",
    "message-circle",
    "messages-square",
    "megaphone",
    "share-2",
    "handshake",
    "network",
    "globe",
    "map",
    "route",
    "book-open",
    "graduation-cap",
    "lightbulb",
    "sparkles",
    "play",
    "pause",
    "focus",
    "maximize-2",
    "check",
    "x",
    "plus",
    "minus",
    "equal",
    "triangle",
    "circle",
    "square",
    "hexagon",
    "workflow",
    "git-branch",
    "infinity",
    "orbit",
    "heart-pulse",
    "scale",
]

CRYPTO_SYMS = {
    "btc": "btc",
    "eth": "eth",
    "sol": "sol",
    "usdc": "usdc",
    "usdt": "usdt",
    "xrp": "xrp",
}


def save(folder: Path, name: str, img: Image.Image) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    img.save(path, "PNG")
    print("wrote", path.relative_to(SKILL.parent.parent.parent))


def make_chrome() -> None:
    for direction, rot in [("right", 0), ("left", 180), ("up", -90), ("down", 90)]:
        im = Image.new("RGBA", (128, 128), CLEAR)
        d = ImageDraw.Draw(im)
        d.polygon(
            [(20, 54), (78, 54), (78, 30), (118, 64), (78, 98), (78, 74), (20, 74)],
            fill=YELLOW,
        )
        if rot:
            im = im.rotate(rot, expand=False, fillcolor=CLEAR)
        save(CHROME, f"arrow-{direction}.png", im)

    im = Image.new("RGBA", (96, 96), CLEAR)
    d = ImageDraw.Draw(im)
    d.line([(28, 20), (68, 48), (28, 76)], fill=YELLOW, width=10)
    save(CHROME, "chevron-right.png", im)

    im = Image.new("RGBA", (320, 160), CLEAR)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 319, 159], radius=16, fill=(28, 28, 28, 255))
    save(CHROME, "panel-soft.png", im)

    im = Image.new("RGBA", (256, 256), CLEAR)
    d = ImageDraw.Draw(im)
    d.ellipse([16, 16, 239, 239], outline=YELLOW, width=8)
    d.ellipse([64, 64, 191, 191], outline=GOLD, width=4)
    save(CHROME, "ring.png", im)

    im = Image.new("RGBA", (64, 64), CLEAR)
    d = ImageDraw.Draw(im)
    d.ellipse([8, 8, 55, 55], fill=YELLOW)
    save(CHROME, "dot.png", im)

    im = Image.new("RGBA", (640, 16), CLEAR)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 6, 640, 10], fill=GOLD)
    save(CHROME, "divider.png", im)

    im = Image.new("RGBA", (240, 120), CLEAR)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 239, 119], radius=12, fill=(28, 28, 28, 255))
    save(CHROME, "flow-node.png", im)

    im = Image.new("RGBA", (128, 128), CLEAR)
    d = ImageDraw.Draw(im)
    d.ellipse([8, 8, 119, 119], fill=YELLOW)
    d.line([(36, 66), (56, 88), (96, 40)], fill=BLACK, width=10)
    save(CHROME, "check-badge.png", im)

    im = Image.new("RGBA", (256, 200), CLEAR)
    d = ImageDraw.Draw(im)
    d.polygon([(128, 10), (246, 190), (10, 190)], outline=YELLOW)
    d.line([(128, 10), (128, 190)], fill=GOLD, width=2)
    save(CHROME, "pyramid-outline.png", im)

    im = Image.new("RGBA", (256, 256), CLEAR)
    d = ImageDraw.Draw(im)
    d.arc([24, 24, 231, 231], 20, 150, fill=YELLOW, width=10)
    d.arc([24, 24, 231, 231], 200, 330, fill=GOLD, width=10)
    save(CHROME, "flywheel-arcs.png", im)

    im = Image.new("RGBA", (320, 80), CLEAR)
    d = ImageDraw.Draw(im)
    pts = [(x, 40 + int(22 * math.sin(x / 28))) for x in range(0, 320, 4)]
    d.line(pts, fill=YELLOW, width=5)
    save(CHROME, "breath-wave.png", im)

    im = Image.new("RGBA", (200, 160), CLEAR)
    d = ImageDraw.Draw(im)
    for i, h in enumerate([50, 90, 130]):
        x = 30 + i * 55
        d.rectangle([x, 150 - h, x + 40, 150], fill=YELLOW if i == 2 else GOLD)
    save(CHROME, "bars-up.png", im)

    im = Image.new("RGBA", (256, 256), CLEAR)
    d = ImageDraw.Draw(im)
    d.pieslice([20, 20, 235, 235], -90, 47, fill=YELLOW)
    d.pieslice([20, 20, 235, 235], 47, 184, fill=GOLD)
    d.pieslice([20, 20, 235, 235], 184, 270, fill=(100, 85, 20, 255))
    d.ellipse([70, 70, 185, 185], fill=BLACK)
    save(CHROME, "pie-382-382-236.png", im)


def make_geometric() -> None:
    def canvas(size=256):
        return Image.new("RGBA", (size, size), CLEAR), size

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.ellipse([40, 40, s - 40, s - 40], outline=YELLOW, width=14)
    save(GEOM, "circle.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([48, 48, 208, 208], radius=24, outline=YELLOW, width=14)
    save(GEOM, "square.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    for o in range(-5, 6):
        d.line([(128, 36 + o), (220, 200 + o)], fill=YELLOW, width=3)
        d.line([(220, 200 + o), (36, 200 + o)], fill=YELLOW, width=3)
        d.line([(36, 200 + o), (128, 36 + o)], fill=YELLOW, width=3)
    save(GEOM, "triangle.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([40, 70, 216, 190], radius=16, outline=YELLOW, width=12)
    d.rectangle([140, 110, 216, 150], outline=YELLOW, width=10)
    d.ellipse([175, 122, 195, 142], fill=YELLOW)
    save(GEOM, "wallet.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.ellipse([88, 40, 148, 100], outline=YELLOW, width=10)
    d.arc([50, 110, 186, 220], 200, 340, fill=YELLOW, width=10)
    d.ellipse([160, 60, 210, 110], outline=GOLD, width=8)
    d.arc([140, 120, 240, 210], 220, 320, fill=GOLD, width=8)
    save(GEOM, "users.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    for r in (40, 70, 100):
        d.ellipse([128 - r, 128 - r, 128 + r, 128 + r], outline=YELLOW, width=10)
    d.ellipse([118, 118, 138, 138], fill=YELLOW)
    save(GEOM, "target.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.ellipse([36, 36, 220, 220], outline=YELLOW, width=12)
    d.polygon([(128, 56), (148, 128), (128, 200), (108, 128)], fill=YELLOW)
    save(GEOM, "compass.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.arc([40, 80, 130, 170], 40, 320, fill=YELLOW, width=14)
    d.arc([126, 80, 216, 170], 220, 140, fill=YELLOW, width=14)
    save(GEOM, "link.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.polygon(
        [(150, 30), (90, 130), (130, 130), (106, 226), (186, 110), (140, 110)],
        fill=YELLOW,
    )
    save(GEOM, "zap.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([68, 110, 188, 210], radius=12, outline=YELLOW, width=12)
    d.arc([88, 50, 168, 130], 180, 0, fill=YELLOW, width=12)
    save(GEOM, "lock.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.ellipse([36, 36, 220, 220], outline=YELLOW, width=12)
    d.line([(128, 128), (128, 70)], fill=YELLOW, width=10)
    d.line([(128, 128), (170, 150)], fill=GOLD, width=8)
    save(GEOM, "clock.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([50, 40, 206, 216], radius=8, outline=YELLOW, width=12)
    d.line([(128, 40), (128, 216)], fill=GOLD, width=6)
    save(GEOM, "book.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    d.polygon([(40, 110), (140, 70), (140, 180)], fill=YELLOW)
    d.rectangle([140, 100, 200, 150], fill=GOLD)
    d.ellipse([190, 115, 220, 145], fill=YELLOW)
    save(GEOM, "megaphone.png", im)

    im, s = canvas()
    d = ImageDraw.Draw(im)
    pts1 = [(x, 100 + int(30 * math.sin(x / 20))) for x in range(30, 226, 3)]
    pts2 = [(x, 150 + int(18 * math.sin(x / 18 + 1))) for x in range(30, 226, 3)]
    d.line(pts1, fill=YELLOW, width=8)
    d.line(pts2, fill=GOLD, width=6)
    save(GEOM, "breath.png", im)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def svg_to_png(svg_bytes: bytes, out: Path, size: int = 256) -> bool:
    text = svg_bytes.decode("utf-8")
    text = text.replace("currentColor", f"rgb{YELLOW[:3]}")
    text = text.replace("#fff", f"rgb{YELLOW[:3]}")
    text = text.replace("#FFFFFF", f"rgb{YELLOW[:3]}")
    text = text.replace("#ffffff", f"rgb{YELLOW[:3]}")
    if "stroke-width=" not in text:
        text = text.replace("<svg ", '<svg stroke-width="2.25" ', 1)
    try:
        import cairosvg

        png = cairosvg.svg2png(
            bytestring=text.encode(), output_width=size, output_height=size
        )
        Image.open(io.BytesIO(png)).save(out, "PNG")
        return True
    except Exception:
        try:
            from reportlab.graphics import renderPM
            from svglib.svglib import svg2rlg

            drawing = svg2rlg(io.BytesIO(text.encode()))
            if drawing:
                renderPM.drawToFile(drawing, str(out), fmt="PNG", dpi=144)
                return True
        except Exception:
            out.with_suffix(".svg").write_text(text)
            return False
    return False


def download_lucide() -> None:
    LUCIDE.mkdir(parents=True, exist_ok=True)
    base = "https://cdn.jsdelivr.net/npm/lucide-static@0.468.0/icons/{}.svg"
    ok = 0
    for name in LUCIDE_NAMES:
        out = LUCIDE / f"{name}.png"
        try:
            data = fetch(base.format(name))
            if svg_to_png(data, out):
                ok += 1
                print("lucide", name)
            else:
                print("lucide svg-only", name)
        except Exception as e:
            print("lucide fail", name, e)
    print(f"lucide rasterized={ok}/{len(LUCIDE_NAMES)}")


def download_crypto() -> None:
    CRYPTO.mkdir(parents=True, exist_ok=True)
    base = "https://essamamdani.github.io/open-crypto-icons/icons/{}/{}.svg"
    for fname, sym in CRYPTO_SYMS.items():
        for variant in ("white", "colored"):
            out = CRYPTO / f"{fname}-{variant}.png"
            try:
                data = fetch(base.format(variant, sym))
                if svg_to_png(data, out):
                    print("crypto", out.name)
                else:
                    print("crypto svg-only", fname, variant)
            except Exception as e:
                print("crypto fail", fname, variant, e)


def write_catalog() -> None:
    catalog = {
        "tokens": sorted(p.name for p in (ELEMS / "tokens").glob("*.png")),
        "chrome": sorted(p.name for p in CHROME.glob("*.png")),
        "geometric": sorted(p.name for p in GEOM.glob("*.png")),
        "lucide": sorted(p.name for p in LUCIDE.glob("*.png")),
        "crypto": sorted(p.name for p in CRYPTO.glob("*.png")),
        "preferred_images": "User-only. Agent must never write files here.",
    }
    (ELEMS / "catalog.json").write_text(json.dumps(catalog, indent=2) + "\n")
    print(
        "catalog",
        {k: (len(v) if isinstance(v, list) else v) for k, v in catalog.items()},
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--download",
        action="store_true",
        help="Also fetch Lucide + open-crypto-icons (network)",
    )
    args = ap.parse_args()
    make_chrome()
    make_geometric()
    if args.download:
        download_lucide()
        download_crypto()
    write_catalog()


if __name__ == "__main__":
    main()
