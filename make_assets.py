#!/usr/bin/env python3
"""Generate web assets from the app's existing art. Run once, or after a
screenshot refresh: python3 make_assets.py

Sources: ../StopGamble/marketing/screenshots/en-US/*.png (1290x2796)
         ../StopGamble/App/Assets.xcassets/AppIcon.appiconset/AppIcon1024.png
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
APP = HERE.parent / "StopGamble"
RAW_SRC = APP / "marketing" / "screenshots" / "pipeline" / "raw"
ORB_SRC = APP / "marketing" / "screenshots" / "pipeline" / "orbs"
ICON_SRC = APP / "App/Assets.xcassets/AppIcon.appiconset/AppIcon1024.png"
OUT = HERE / "assets"
SHOT_OUT = OUT / "shots"

ROUNDED = "/System/Library/Fonts/SFNSRounded.ttf"

INK = (10, 11, 16)
MINT = (110, 231, 192)
TEAL = (53, 200, 216)
INDIGO = (139, 142, 240)
TEXT = (237, 239, 245)
MUTED = (163, 171, 187)


def rounded(size: int, weight: str = "Bold") -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(ROUNDED, size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def screenshots() -> None:
    """Clean app screens, not the App Store marketing panels — those have their own
    baked-in headlines and crops that fight the page copy."""
    SHOT_OUT.mkdir(parents=True, exist_ok=True)
    for name in ("dashboard", "program", "protect", "panic", "collection", "money"):
        src = RAW_SRC / f"raw_{name}.png"
        if not src.exists():
            print(f"  missing {src}")
            continue
        im = Image.open(src).convert("RGB")
        # 2x of the 12rem CSS display width — plenty for retina, tiny on the wire.
        im = im.resize((430, 932), Image.LANCZOS)
        dst = SHOT_OUT / f"{name}.jpg"
        im.save(dst, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"  {dst.relative_to(HERE)}  {dst.stat().st_size // 1024} KB")


def orbs() -> None:
    """A few milestone pieces, alpha preserved, as decorative art."""
    out = OUT / "orbs"
    out.mkdir(parents=True, exist_ok=True)
    wanted = {"vow": "vow", "firstlight": "first-light", "halfyear": "half-year",
              "kintsugi": "kintsugi"}
    for stem, slug in wanted.items():
        matches = sorted(ORB_SRC.glob(f"{stem}-*.png"))
        if not matches:
            print(f"  no orb render for {stem}")
            continue
        im = Image.open(matches[0]).convert("RGBA")
        im.thumbnail((320, 320), Image.LANCZOS)
        dst = out / f"{slug}.png"
        im.save(dst, "PNG", optimize=True)
        print(f"  {dst.relative_to(HERE)}  {dst.stat().st_size // 1024} KB")


def icons() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    icon = Image.open(ICON_SRC).convert("RGBA")
    for size, name in ((180, "icon-180.png"), (32, "favicon.png")):
        icon.resize((size, size), Image.LANCZOS).save(OUT / name, "PNG", optimize=True)
        print(f"  assets/{name}")


def aurora(w: int, h: int) -> Image.Image:
    """Radial aurora glows on near-black, matching the site's CSS ground."""
    base = Image.new("RGB", (w, h), INK)
    for cx, cy, rad, color, strength in (
        (0.12, -0.10, 0.85, TEAL, 0.30),
        (0.92, 0.05, 0.75, INDIGO, 0.26),
        (0.50, 1.10, 0.70, MINT, 0.20),
    ):
        layer = Image.new("RGB", (w, h), color)
        mask = Image.new("L", (w, h), 0)
        d = ImageDraw.Draw(mask)
        px, py, r = cx * w, cy * h, rad * w
        steps = 90
        for i in range(steps, 0, -1):
            t = i / steps
            a = int(255 * strength * (1 - t) ** 2.0)
            d.ellipse([px - r * t, py - r * t * 0.72, px + r * t, py + r * t * 0.72],
                      fill=a)
        base = Image.composite(layer, base, mask)
    return base


def og() -> None:
    W, H = 1200, 630
    im = aurora(W, H)
    d = ImageDraw.Draw(im)

    d.text((72, 150), "Quit for good.", font=rounded(84, "Heavy"), fill=TEXT)
    d.text((72, 246), "Keep the money.", font=rounded(84, "Heavy"), fill=MINT)
    d.text((72, 380),
           "Silex blocks gambling across your iPhone and walks you\n"
           "through 90 days, one at a time.",
           font=rounded(32, "Medium"), fill=MUTED, spacing=12)
    d.text((72, 520), "trysilex.com", font=rounded(30, "Semibold"), fill=TEAL)

    icon = Image.open(ICON_SRC).convert("RGBA").resize((132, 132), Image.LANCZOS)
    mask = Image.new("L", (132, 132), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, 131, 131], radius=30, fill=255)
    im.paste(icon, (W - 132 - 72, 72), mask)

    im.save(OUT / "og.png", "PNG", optimize=True)
    print(f"  assets/og.png  {(OUT / 'og.png').stat().st_size // 1024} KB")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    icons()
    screenshots()
    orbs()
    og()
