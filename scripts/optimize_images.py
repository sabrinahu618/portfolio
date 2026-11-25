#!/usr/bin/env python3
"""Turn a photo or screenshot into a fast, web-ready WebP.

Usage:
    python3 scripts/optimize_images.py <input> <output.webp> [max_width]

Example:
    python3 scripts/optimize_images.py ~/Desktop/prototype.jpg assets/img/solar-cap/prototype.webp

It resizes to max_width (default 1600px), strips metadata, saves as WebP,
and prints the width/height to paste into the figure include.
Requires Pillow:  pip install pillow
"""
import sys
from PIL import Image, ImageOps


def optimize(src, dst, max_width=1600, quality=80):
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)  # respect phone rotation
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    if im.width > max_width:
        im = im.resize((max_width, round(im.height * max_width / im.width)), Image.LANCZOS)
    im.save(dst, "WEBP", quality=quality, method=6)
    print(f"{dst}  width={im.width} height={im.height}")
    return im.size


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    optimize(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1600)
