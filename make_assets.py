#!/usr/bin/env python3
"""Generate web assets from the app's existing art. Run once, or after a
screenshot refresh: python3 make_assets.py

Site screenshots only, from a fresh capture (see capture.py in the app repo):
    python3 make_assets.py shots <raw_dir> [es]

Sources: ../StopGamble/marketing/screenshots/en-US/*.png (1290x2796)
         ../StopGamble/App/Assets.xcassets/AppIcon.appiconset/AppIcon1024.png
"""

import sys
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


def screenshots(raw: Path = RAW_SRC, out: Path = SHOT_OUT) -> None:
    """Clean app screens, not the App Store marketing panels — those have their own
    baked-in headlines and crops that fight the page copy."""
    out.mkdir(parents=True, exist_ok=True)
    for name in ("dashboard", "program", "protect", "panic", "collection", "money"):
        src = raw / f"raw_{name}.png"
        if not src.exists():
            print(f"  missing {src}")
            continue
        im = Image.open(src).convert("RGB")
        # 2x of the largest CSS display width (the hero phone, 22.5rem).
        im = im.resize((720, round(720 * im.height / im.width)), Image.LANCZOS)
        dst = out / f"{name}.jpg"
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
        im.thumbnail((360, 360), Image.LANCZOS)
        dst = out / f"{slug}.png"
        im.save(dst, "PNG", optimize=True)
        print(f"  {dst.relative_to(HERE)}  {dst.stat().st_size // 1024} KB")


def icons() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    icon = Image.open(ICON_SRC).convert("RGBA")
    for size, name in ((180, "icon-180.png"), (32, "favicon.png")):
        icon.resize((size, size), Image.LANCZOS).save(OUT / name, "PNG", optimize=True)
        print(f"  assets/{name}")


def og() -> None:
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (8, 9, 13))
    serif = ImageFont.truetype("/System/Library/Fonts/NewYork.ttf", 92)
    d = ImageDraw.Draw(im)
    d.text((72, 150), "Quit gambling.", font=serif, fill=TEXT)
    d.text((72, 256), "Keep the money.", font=serif, fill=TEXT)
    d.text((72, 396),
           "Silex blocks gambling across your phone and walks\n"
           "you through 90 days, one at a time.",
           font=rounded(30, "Medium"), fill=MUTED, spacing=12)
    d.text((72, 520), "trysilex.com", font=rounded(28, "Semibold"), fill=MINT)

    orb = Image.open(sorted(ORB_SRC.glob("firstlight-*.png"))[0]).convert("RGBA")
    orb = orb.resize((420, 420), Image.LANCZOS)
    im.paste(orb, (W - 420 - 20, (H - 420) // 2), orb)

    im.save(OUT / "og.png", "PNG", optimize=True)
    print(f"  assets/og.png  {(OUT / 'og.png').stat().st_size // 1024} KB")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    if len(sys.argv) > 2 and sys.argv[1] == "shots":
        sub = sys.argv[3] if len(sys.argv) > 3 else ""
        screenshots(Path(sys.argv[2]), SHOT_OUT / sub)
        sys.exit()
    icons()
    screenshots()
    orbs()
    og()
