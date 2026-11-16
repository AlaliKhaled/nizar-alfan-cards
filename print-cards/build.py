#!/usr/bin/env python3
"""Inline the vector QR SVGs into nfc-cards.html -> nfc-cards.build.html.
Keeps the QR as true vector in the exported PDF (no rasterization)."""
import re, pathlib
here = pathlib.Path(__file__).parent
tpl = (here / "nfc-cards.html").read_text(encoding="utf-8")

def inline_qr(name):
    svg = (here / "assets" / f"qr-{name}.svg").read_text(encoding="utf-8")
    svg = re.search(r"<svg\b.*</svg>", svg, re.S).group(0)
    svg = re.sub(r'\swidth="[^"]*"', "", svg, count=1)   # let CSS size it
    svg = re.sub(r'\sheight="[^"]*"', "", svg, count=1)
    svg = svg.replace(' preserveAspectRatio="none"', "")  # avoid distortion
    return svg

out = tpl
for n in ("shop", "mahmoud", "moafaq"):
    out = out.replace(f"@@QR_{n.upper()}@@", inline_qr(n))
assert "@@" not in out, "unreplaced token remains"
(here / "nfc-cards.build.html").write_text(out, encoding="utf-8")
print("built nfc-cards.build.html")
