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
# Hero background
# --------------------------------------------------------------------------- #

_HERO_W, _HERO_H, _HERO_MID = 1440.0, 240.0, 172.0
_HERO_A0, _HERO_DECAY = 64.0, 330.0


def _signal_points(phase=0.0, step=6):
    """A volatile signal whose amplitude decays until it runs flat.

    This is the one idea the whole clinic rests on, and the treatment pages
    already say it in words: instead of the sharp rise and fall that drives
    the cycle of using, the level in your blood stays flat. Drawn rather than
    written, it gives the hero a background that means something instead of a
    decorative gradient.

    Three incommensurate frequencies keep it irregular, so it reads as a
    signal settling rather than as a sine wave or an ECG trace. Deterministic,
    so every build produces the same curve.
    """
    pts = []
    x = 0.0
    while x <= _HERO_W:
        amp = _HERO_A0 * math.exp(-x / _HERO_DECAY)
        w = (math.sin(x / 37.0 + phase)
             + 0.62 * math.sin(x / 16.3 + 1.2 + phase)
             + 0.33 * math.sin(x / 71.0 + 0.4 + phase)) / 1.95
        pts.append((x, _HERO_MID - amp * w))
        x += step
    return pts


def _path(pts):
    return 'M' + ' L'.join('%.1f %.1f' % (x, y) for x, y in pts)


def hero_signal():
    """Full bleed hero background. Decorative, so it is hidden from readers."""
    main = _signal_points()
    echo = _signal_points(phase=2.1)
    area = _path(main) + ' L%.0f %.0f L0 %.0f Z' % (_HERO_W, _HERO_H, _HERO_H)
    return (
        '<svg class="hero-signal" viewBox="0 0 1440 240" preserveAspectRatio="none" '
        'aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">'
        # the ground the line settles onto
        '<path d="%s" fill="var(--blue)" opacity=".075"/>' % area
        # a fainter echo, for depth
        + '<path d="%s" fill="none" stroke="var(--blue)" stroke-opacity=".13" '
          'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' % _path(echo)
        # the signal itself
        + '<path d="%s" fill="none" stroke="var(--blue)" stroke-opacity=".26" '
          'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' % _path(main)
        + '</svg>'
    )


# --------------------------------------------------------------------------- #
# Hero objects
# --------------------------------------------------------------------------- #
# Isometric solids, built from three faces each: a light top, a mid left and a
# dark right. Real shading rather than a flat icon, so they read dimensional
# without needing a 3D library or a raster render. Each floats on a slow loop
# and carries a CSS drop shadow, which is what sells the depth.

# top, left, right
_BLUE_FACES = ('#4A93C1', '#015F9C', '#01486F')
_ORANGE_FACES = ('#F9A55F', '#F47F20', '#C4620F')
_PALE_FACES = ('#FFFFFF', '#E3EFF7', '#C4DCEC')


def _iso_box(cx, ty, hw, hh, depth, faces):
    """An isometric box. cx, ty is the apex of the top face."""
    top, left, right = faces
    return (
        '<path d="M{cx} {ty}L{r} {m}L{cx} {b}L{l} {m}Z" fill="{ft}"/>'
        '<path d="M{l} {m}L{cx} {b}L{cx} {bd}L{l} {md}Z" fill="{fl}"/>'
        '<path d="M{r} {m}L{cx} {b}L{cx} {bd}L{r} {md}Z" fill="{fr}"/>'
    ).format(cx=cx, ty=ty, l=cx - hw, r=cx + hw, m=ty + hh, b=ty + 2 * hh,
             md=ty + hh + depth, bd=ty + 2 * hh + depth,
             ft=top, fl=left, fr=right)


def iso_bottle():
    """A dosing bottle. The object the whole service hands over."""
    return (
        '<svg class="obj" viewBox="0 0 150 190" aria-hidden="true" '
        'focusable="false" xmlns="http://www.w3.org/2000/svg">'
        + _iso_box(75, 96, 46, 25, 58, _BLUE_FACES)
        + _iso_box(75, 52, 22, 12, 34, _ORANGE_FACES)
        # label wrapped across the two visible body faces
        + '<path d="M29 139L75 165L75 143L29 117Z" fill="#FFFFFF" opacity=".92"/>'
        + '<path d="M121 139L75 165L75 143L121 117Z" fill="#EAF3F9" opacity=".92"/>'
        + '<path d="M38 133L64 148" stroke="#9FC3DA" stroke-width="4" '
          'stroke-linecap="round"/>'
        + '<path d="M38 124L56 134" stroke="#BBD6E7" stroke-width="4" '
          'stroke-linecap="round"/>'
        + '</svg>'
    )


def iso_screen():
    """A tablet lying flat, mid appointment.

    The first attempt floated the screen as a separate plane above the base
    and read as two unconnected diamonds. Everything now sits coplanar with
    the top face of one slab, which is what makes it a single object. A circle
    on a 2:1 isometric plane projects to an ellipse of half the height, so the
    caller is drawn with ry exactly half of rx.
    """
    return (
        '<svg class="obj" viewBox="0 0 180 150" aria-hidden="true" '
        'focusable="false" xmlns="http://www.w3.org/2000/svg">'
        + _iso_box(90, 34, 68, 37, 15, _PALE_FACES)
        # screen inset into the top face
        + '<path d="M90 46L143 71L90 96L37 71Z" fill="#015F9C"/>'
        # the caller, featureless, foreshortened onto the same plane
        + '<ellipse cx="90" cy="65" rx="9" ry="4.5" fill="#EAF3F9"/>'
        + '<ellipse cx="90" cy="79" rx="17" ry="8.5" fill="#EAF3F9"/>'
        + '<ellipse cx="90" cy="88" rx="7" ry="3.5" fill="#F47F20"/>'
        + '</svg>'
    )


def iso_stack():
    """Three slabs stacked. Doses, and the take home ones that follow."""
    return (
        '<svg class="obj" viewBox="0 0 130 150" aria-hidden="true" '
        'focusable="false" xmlns="http://www.w3.org/2000/svg">'
        + _iso_box(65, 74, 44, 24, 11, _PALE_FACES)
        + _iso_box(65, 54, 44, 24, 11, _PALE_FACES)
        + _iso_box(65, 34, 44, 24, 11, _BLUE_FACES)
        + '<ellipse cx="65" cy="58" rx="9" ry="4.5" fill="#F47F20"/>'
        + '</svg>'
    )


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
