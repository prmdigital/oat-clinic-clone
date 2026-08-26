# -*- coding: utf-8 -*-
"""Regenerate every logo derivative from the one supplied artwork.

    python tools/make_logos.py

Source of truth is assets/img/oat-clinic-logo.jpg, the file the client
supplied. Everything else on the site is derived from it by this script, so
replacing that one file and re-running is all it takes to reskin the brand.

Requires Pillow. Nothing else in the build does, which is why this is a
separate script rather than part of tools/build.py.

Outputs:
    assets/img/oat-clinic-logo.png   lossless copy of the artwork
    assets/img/logo-96.png           blue tile, masthead and drawer, on light
    assets/img/logo-light.png        white wordmark only, transparent, for navy
    assets/img/og-default.png        1200x630 social share card
    assets/apple-touch-icon.png      180x180
    assets/favicon-32.png            32x32
    assets/favicon.ico               multi resolution
"""

from __future__ import print_function

import math
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print('Pillow is required: python -m pip install Pillow')
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'assets', 'img')
ASSETS = os.path.join(ROOT, 'assets')
SOURCE = os.path.join(IMG, 'oat-clinic-logo.jpg')

# Sampled from the artwork. See the Brand section of the README.
BG = (1, 95, 156)
ORANGE = (244, 127, 32)
WHITE = (255, 255, 255)
NAVY = (1, 42, 69)


def _sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _norm(a):
    return math.sqrt(_dot(a, a)) or 1.0


def make_light(src, target_height=150, lo=26.0, hi=105.0, include_bar=False):
    """Lift the wordmark off its blue tile onto transparency.

    The artwork is flat two colour over a solid tile, so each pixel is a blend
    of the tile blue and one foreground colour. Alpha comes from how far the
    pixel sits from the tile blue; the colour is snapped to whichever
    foreground it is heading toward. That keeps antialiased edges soft without
    leaving a blue fringe, which a plain colour key would.
    """
    w, h = src.size
    px = src.load()
    d_white = _sub(WHITE, BG)
    n_white = _norm(d_white)
    d_orange = _sub(ORANGE, BG)
    n_orange = _norm(d_orange)

    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    op = out.load()
    for y in range(h):
        for x in range(w):
            v = _sub(px[x, y], BG)
            d = _norm(v)
            if d <= lo:
                continue
            alpha = 1.0 if d >= hi else (d - lo) / (hi - lo)
            toward_white = _dot(v, d_white) / (d * n_white)
            toward_orange = _dot(v, d_orange) / (d * n_orange)
            colour = WHITE if toward_white >= toward_orange else ORANGE
            op[x, y] = (colour[0], colour[1], colour[2], int(round(alpha * 255)))

    if not include_bar:
        # The orange rule belongs to the tile lockup, not to the wordmark.
        # Drop it so the footer carries the lettering alone.
        for y in range(h):
            for x in range(w):
                r, g, b, a = op[x, y]
                if a and (r, g, b) == ORANGE:
                    op[x, y] = (0, 0, 0, 0)

    out = out.crop(out.getbbox())
    width = int(round(out.size[0] * target_height / float(out.size[1])))
    return out.resize((width, target_height), Image.LANCZOS)


def _font(size, bold=True):
    names = (['segoeuib.ttf', 'arialbd.ttf', 'calibrib.ttf'] if bold
             else ['segoeui.ttf', 'arial.ttf', 'calibri.ttf'])
    for name in names:
        path = os.path.join(r'C:\Windows\Fonts', name)
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    for path in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
                 '/System/Library/Fonts/Helvetica.ttc'):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def make_og(tile):
    """1200x630 share card. The tile blue matches the card, so the logo's own
    background disappears and only the wordmark reads."""
    w, h = 1200, 630
    card = Image.new('RGB', (w, h), BG)
    d = ImageDraw.Draw(card)
    d.rectangle([0, h - 26, w, h], fill=ORANGE)
    logo = tile.resize((190, 190), Image.LANCZOS)
    card.paste(logo, (86, 96))
    d.text((86, 330), 'Opioid agonist treatment', font=_font(52, False), fill=(196, 222, 238))
    d.text((86, 396), 'across the Lower Mainland', font=_font(52, False), fill=(196, 222, 238))
    d.text((86, 486), 'Same day assessment  \u00b7  No referral  \u00b7  Five BC clinics',
           font=_font(30, True), fill=ORANGE)
    return card


def main():
    if not os.path.exists(SOURCE):
        print('Source artwork missing: %s' % SOURCE)
        return 1

    tile = Image.open(SOURCE).convert('RGB')
    written = []

    def save(im, path, **kw):
        im.save(path, **kw)
        written.append(path)

    save(tile, os.path.join(IMG, 'oat-clinic-logo.png'), format='PNG', optimize=True)
    save(tile.resize((96, 96), Image.LANCZOS), os.path.join(IMG, 'logo-96.png'),
         format='PNG', optimize=True)
    save(make_light(tile), os.path.join(IMG, 'logo-light.png'), format='PNG', optimize=True)
    save(make_og(tile), os.path.join(IMG, 'og-default.png'), format='PNG', optimize=True)
    save(tile.resize((180, 180), Image.LANCZOS), os.path.join(ASSETS, 'apple-touch-icon.png'),
         format='PNG', optimize=True)
    save(tile.resize((32, 32), Image.LANCZOS), os.path.join(ASSETS, 'favicon-32.png'),
         format='PNG', optimize=True)
    save(tile.resize((256, 256), Image.LANCZOS), os.path.join(ASSETS, 'favicon.ico'),
         format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

    for path in written:
        rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
        print('  %-38s %7d bytes' % (rel, os.path.getsize(path)))
    print('\nRun tools/build.py afterwards so the asset hashes update.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
