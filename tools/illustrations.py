# -*- coding: utf-8 -*-
"""Flat SVG illustrations, homepage only.

Inspired by the reference site's approach rather than its artwork: a site can
feel alive with no photography at all, provided it has one consistent
illustration system. That matters here more than it does for a language app,
because patients cannot be photographed and stock photography of people
looking sad is worse than nothing.

House rules for this set:
  - Places and objects only. No characters, no mascot, no faces. The one
    figure that appears is an abstract silhouette on a phone screen, which
    reads as "a clinician on a call" without becoming a personality.
  - Brand tokens only, referenced as CSS variables so they follow the theme.
  - Flat shapes, no gradients, no textures.
  - Drawn on a 240x150 canvas so every card lines up.
  - Elements marked class="art-lift" get a small hover shift. Everything else
    holds still, so the movement reads as a detail rather than a bounce.

These are inline SVG, so they cost no extra request and inherit the palette.
"""

import math

_OPEN = ('<svg class="art" viewBox="0 0 240 150" role="img" '
         'aria-label="{alt}" xmlns="http://www.w3.org/2000/svg">'
         '<rect width="240" height="150" rx="14" fill="{bg}"/>')
_CLOSE = '</svg>'

# A deeper tint than --blue-tint, used for ground planes and receding shapes.
SHADE = '#C9DFEE'


def _wrap(alt, inner, bg='var(--blue-tint)'):
    return _OPEN.format(alt=alt, bg=bg) + inner + _CLOSE


def _pin(x, y, fill='var(--blue)'):
    """A map pin whose point sits exactly at x, y."""
    return (
        '<path d="M{x} {y}c-7-9-12-15-12-21a12 12 0 0 1 24 0c0 6-5 12-12 21z" '
        'fill="{f}"/><circle cx="{x}" cy="{cy}" r="4.5" fill="#fff"/>'
    ).format(x=x, y=y, cy=y - 21, f=fill)


def clinic():
    """A clinic front. Door, sign, windows, a step up from the pavement."""
    return _wrap('Illustration of a clinic entrance', (
        # pavement
        '<rect x="0" y="122" width="240" height="28" fill="%s"/>' % SHADE
        # building
        + '<rect x="52" y="26" width="136" height="96" rx="7" fill="#fff"/>'
        + '<path d="M52 33a7 7 0 0 1 7-7h122a7 7 0 0 1 7 7v12H52z" fill="var(--blue)"/>'
        # sign over the door
        + '<rect class="art-lift" x="94" y="53" width="52" height="11" rx="5.5" '
          'fill="var(--orange)"/>'
        # windows, raised to clear the arch
        + '<rect x="64" y="74" width="24" height="24" rx="5" fill="var(--blue-tint)"/>'
        + '<rect x="152" y="74" width="24" height="24" rx="5" fill="var(--blue-tint)"/>'
        # arched door
        + '<path d="M102 122V92a18 18 0 0 1 36 0v30z" fill="var(--blue)"/>'
        + '<circle cx="131" cy="108" r="3" fill="#fff"/>'
    ))


def telehealth():
    """A phone on a table at home. A call in progress, a mug, a plant."""
    return _wrap('Illustration of a video appointment on a phone', (
        '<rect x="0" y="126" width="240" height="24" fill="%s"/>' % SHADE
        # phone
        + '<rect class="art-lift" x="88" y="20" width="64" height="106" rx="12" '
          'fill="#fff" stroke="var(--blue)" stroke-width="3"/>'
        + '<rect x="96" y="32" width="48" height="72" rx="7" fill="var(--blue-tint)"/>'
        # abstract clinician: head and shoulders, deliberately featureless
        + '<circle cx="120" cy="56" r="10" fill="var(--blue)"/>'
        + '<path d="M104 88a16 16 0 0 1 32 0z" fill="var(--blue)"/>'
        + '<circle cx="120" cy="114" r="6" fill="var(--orange)"/>'
        # mug
        + '<rect x="34" y="96" width="30" height="28" rx="6" fill="#fff" '
          'stroke="var(--blue)" stroke-width="3"/>'
        + '<path d="M64 104h7a8 8 0 0 1 0 16h-7" fill="none" stroke="var(--blue)" '
          'stroke-width="3"/>'
        # plant
        + '<rect x="178" y="102" width="28" height="24" rx="5" fill="var(--orange)"/>'
        + '<path d="M192 102c0-15-9-22-17-24 2 13 8 21 17 24z" fill="var(--sage)"/>'
        + '<path d="M192 102c0-12 8-19 16-20-2 11-7 18-16 20z" fill="var(--sage)"/>'
    ))


def pharmacy():
    """A pharmacy counter, with the dispensing screen the request goes into."""
    return _wrap('Illustration of a pharmacy counter', (
        # shelf and stock behind the counter
        '<rect x="44" y="18" width="16" height="22" rx="3" fill="var(--blue)"/>'
        + '<rect x="68" y="23" width="14" height="17" rx="3" fill="var(--orange)"/>'
        + '<rect x="90" y="16" width="16" height="24" rx="3" fill="var(--sage)"/>'
        + '<rect x="30" y="40" width="180" height="7" rx="3.5" fill="%s"/>' % SHADE
        # dispensing screen
        + '<rect class="art-lift" x="118" y="56" width="80" height="52" rx="8" '
          'fill="#fff" stroke="var(--blue)" stroke-width="3"/>'
        + '<rect x="128" y="66" width="42" height="6" rx="3" fill="var(--blue)"/>'
        + '<rect x="128" y="79" width="58" height="4" rx="2" fill="%s"/>' % SHADE
        + '<rect x="128" y="89" width="46" height="4" rx="2" fill="%s"/>' % SHADE
        + '<circle cx="186" cy="99" r="6" fill="var(--orange)"/>'
        # dispensed bottle
        + '<rect x="54" y="58" width="22" height="10" rx="3" fill="var(--blue-2)"/>'
        + '<rect x="50" y="68" width="30" height="38" rx="5" fill="var(--blue)"/>'
        + '<rect x="55" y="80" width="20" height="13" rx="2" fill="#fff"/>'
        # counter
        + '<rect x="16" y="106" width="208" height="13" rx="6" fill="#fff"/>'
        + '<rect x="16" y="119" width="208" height="24" rx="6" fill="%s"/>' % SHADE
    ))


def meds():
    """What we treat: a dosing bottle, a measuring cup, a blister strip."""
    return _wrap('Illustration of treatment medication', (
        '<rect x="0" y="120" width="240" height="30" fill="%s"/>' % SHADE
        # liquid bottle
        + '<rect x="46" y="36" width="26" height="12" rx="3" fill="var(--blue-2)"/>'
        + '<rect class="art-lift" x="38" y="48" width="42" height="72" rx="7" '
          'fill="var(--blue)"/>'
        + '<rect x="45" y="66" width="28" height="26" rx="3" fill="#fff"/>'
        + '<rect x="50" y="74" width="18" height="3.5" rx="1.75" fill="%s"/>' % SHADE
        + '<rect x="50" y="81" width="12" height="3.5" rx="1.75" fill="%s"/>' % SHADE
        # measuring cup with a measured dose
        + '<path d="M96 86h34l-4 34h-26z" fill="#fff" stroke="var(--blue)" '
          'stroke-width="3" stroke-linejoin="round"/>'
        + '<path d="M99 104h28l-2 16h-24z" fill="var(--orange)"/>'
        # blister strip
        + '<rect x="150" y="58" width="62" height="46" rx="8" fill="#fff" '
          'stroke="var(--blue)" stroke-width="3"/>'
        + '<circle cx="167" cy="74" r="6" fill="var(--blue-tint)"/>'
        + '<circle cx="181" cy="74" r="6" fill="var(--blue-tint)"/>'
        + '<circle cx="195" cy="74" r="6" fill="var(--blue-tint)"/>'
        + '<circle cx="167" cy="90" r="6" fill="var(--blue-tint)"/>'
        + '<circle cx="181" cy="90" r="6" fill="var(--sage)"/>'
        + '<circle cx="195" cy="90" r="6" fill="var(--blue-tint)"/>'
    ))


def map_pins():
    """Locations: five pins over a simplified stretch of coast and river."""
    return _wrap('Illustration of a map with five clinic locations', (
        # land
        '<path d="M0 44c34-10 58 4 92 2s52-16 88-12 46 16 60 12v104H0z" fill="#fff"/>'
        # water running through it
        + '<path d="M-4 92c40-14 66 10 104 2s58-24 96-16 44 14 48 12" fill="none" '
          'stroke="%s" stroke-width="9" stroke-linecap="round"/>' % SHADE
        # roads
        + '<path d="M28 150l38-56M132 150l-16-42M196 148l-14-40" fill="none" '
          'stroke="%s" stroke-width="4" stroke-linecap="round"/>' % SHADE
        # five clinics, the nearest one picked out in orange
        + _pin(52, 78)
        + _pin(100, 62)
        + _pin(148, 84, 'var(--orange)')
        + _pin(192, 66)
        + _pin(126, 128)
    ))


def workflow():
    """For pharmacies: the request screen, a signature, a confirmation."""
    return _wrap('Illustration of an appointment request being signed off', (
        '<rect x="34" y="20" width="150" height="104" rx="10" '
        'fill="rgba(255,255,255,.06)" stroke="rgba(255,255,255,.38)" stroke-width="3"/>'
        + '<rect x="48" y="36" width="62" height="7" rx="3.5" fill="rgba(255,255,255,.75)"/>'
        + '<rect x="48" y="52" width="108" height="5" rx="2.5" fill="rgba(255,255,255,.28)"/>'
        + '<rect x="48" y="64" width="88" height="5" rx="2.5" fill="rgba(255,255,255,.28)"/>'
        # signature over its line
        + '<path class="art-lift" d="M50 96c8-12 13 6 20-2s10-14 17-4 12 10 20 2" '
          'fill="none" stroke="var(--orange)" stroke-width="3.5" stroke-linecap="round"/>'
        + '<rect x="48" y="104" width="90" height="3" rx="1.5" fill="rgba(255,255,255,.30)"/>'
        # confirmation
        + '<circle cx="184" cy="104" r="22" fill="var(--orange)"/>'
        + '<path d="M174 104l7 7 13-14" fill="none" stroke="#012A45" stroke-width="4" '
          'stroke-linecap="round" stroke-linejoin="round"/>'
    ), bg='transparent')


# --------------------------------------------------------------------------- #
# Hero scene
# --------------------------------------------------------------------------- #
# One connected isometric scene rather than objects scattered at the edges.
# It shows the three ways in that the page goes on to describe: a home with a
# call, the clinic, and a pharmacy, joined by a path. Drawn for a dark hero,
# so the palettes are light on navy rather than dark on white.

def _iso_box(cx, ty, hw, hh, depth, faces):
    """An isometric box from three faces: light top, mid left, dark right.

    cx, ty is the apex of the top face. Shading is what makes these read as
    solids rather than flat shapes, so every solid in the scene uses the same
    three face rule.
    """
    top, left, right = faces
    return (
        '<path d="M{cx} {ty}L{r} {m}L{cx} {b}L{l} {m}Z" fill="{ft}"/>'
        '<path d="M{l} {m}L{cx} {b}L{cx} {bd}L{l} {md}Z" fill="{fl}"/>'
        '<path d="M{r} {m}L{cx} {b}L{cx} {bd}L{r} {md}Z" fill="{fr}"/>'
    ).format(cx=cx, ty=ty, l=cx - hw, r=cx + hw, m=ty + hh, b=ty + 2 * hh,
             md=ty + hh + depth, bd=ty + 2 * hh + depth,
             ft=top, fl=left, fr=right)


_PLINTH = ('#0F3A56', '#0B2E45', '#082334')
_LIGHT = ('#E4F0F8', '#B4D2E7', '#87B2D2')
_MIDBLUE = ('#5AA3CE', '#2E7BAE', '#1B5B87')


def _plinth(cx, ty, hw, hh, depth=13):
    return _iso_box(cx, ty, hw, hh, depth, _PLINTH)


def _dot(cx, cy, r, fill):
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s"/>' % (cx, cy, r, r / 2.0, fill)


def hero_scene():
    """The three ways in, as one isometric scene along the foot of the hero."""
    out = ['<svg class="hero-scene" viewBox="0 0 1440 300" '
           'preserveAspectRatio="xMidYMax meet" aria-hidden="true" focusable="false" '
           'xmlns="http://www.w3.org/2000/svg">']

    # The path linking the three, drawn first so the buildings sit over it.
    out.append('<path d="M250 232C420 262 540 262 720 224S1030 258 1190 232" '
               'fill="none" stroke="#2E7BAE" stroke-width="3" stroke-opacity=".55" '
               'stroke-linecap="round" stroke-dasharray="2 14"/>')

    # 1. Home, with a call coming in.
    out.append(_plinth(250, 172, 112, 58))
    out.append(_iso_box(250, 168, 42, 23, 37, _LIGHT))
    out.append(_dot(250, 191, 11, '#2E7BAE'))
    out.append(_iso_box(316, 150, 15, 8, 26, _MIDBLUE))
    out.append(_dot(316, 158, 6, '#E4F0F8'))
    out.append(_dot(316, 176, 4, '#F47F20'))

    # 2. The clinic, the tallest thing in the scene.
    out.append(_plinth(720, 150, 132, 68, 15))
    out.append(_iso_box(720, 118, 56, 30, 58, _MIDBLUE))
    # sign band and door on the left face
    out.append('<path d="M664 148L720 178L720 194L664 164Z" fill="#F47F20"/>')
    out.append('<path d="M690 186L710 197L710 219L690 208Z" fill="#0F3A56" opacity=".55"/>')
    out.append(_dot(720, 118, 13, '#E4F0F8'))

    # 3. The pharmacy.
    out.append(_plinth(1190, 172, 112, 58))
    out.append(_iso_box(1190, 166, 44, 24, 38, _LIGHT))
    out.append('<path d="M1146 190L1190 214L1190 226L1146 202Z" fill="#F47F20"/>')
    out.append(_dot(1190, 166, 11, '#2E7BAE'))

    out.append('</svg>')
    return ''.join(out)


ART = {
    'clinic': clinic,
    'telehealth': telehealth,
    'pharmacy': pharmacy,
    'meds': meds,
    'map': map_pins,
    'workflow': workflow,
}


def art(name):
    return ART[name]()
