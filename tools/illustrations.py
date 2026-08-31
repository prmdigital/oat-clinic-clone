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
# Hero field
# --------------------------------------------------------------------------- #
# Motion, not another still picture. Five clinics sit on a soft field, each
# giving off a slow expanding ring, joined by a path whose dashes travel from
# left to right. Read together it is reach: five places, one network, care
# moving between them. Nothing here is a loop for its own sake.
#
# Everything animates through CSS so a single media query can stop all of it,
# and the rings scale rather than redraw, which keeps them on the compositor.

_PIN_X = [168, 452, 720, 1002, 1276]
_PIN_Y = [188, 154, 132, 160, 194]
_PIN_DELAY = ['0s', '1.1s', '2.2s', '3.3s', '4.4s']


def _hero_pin(x, y, delay, accent=False):
    colour = 'var(--orange)' if accent else 'var(--blue)'
    return (
        '<g class="pin" style="--d:{d}">'
        '<circle class="pulse" cx="{x}" cy="{y}" r="15" fill="none" stroke="{c}" '
        'stroke-width="2"/>'
        '<circle class="pulse pulse-b" cx="{x}" cy="{y}" r="15" fill="none" stroke="{c}" '
        'stroke-width="2"/>'
        '<circle cx="{x}" cy="{y}" r="9.5" fill="{c}"/>'
        '<circle cx="{x}" cy="{y}" r="3.6" fill="#fff"/>'
        '</g>'
    ).format(x=x, y=y, d=delay, c=colour)


def hero_field():
    """Five clinics on a field, pulsing, joined by a travelling path."""
    pts = list(zip(_PIN_X, _PIN_Y))
    d = 'M{0} {1}'.format(pts[0][0], pts[0][1])
    for i in range(1, len(pts)):
        x0, y0 = pts[i - 1]
        x1, y1 = pts[i]
        mx = (x0 + x1) / 2.0
        d += 'C{0} {1} {2} {3} {4} {5}'.format(mx, y0, mx, y1, x1, y1)

    return (
        '<svg class="hero-field" viewBox="0 0 1440 300" preserveAspectRatio="none" '
        'aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">'
        # the route between the clinics, dashes travelling along it
        '<path class="route" d="{d}" fill="none" stroke="var(--blue)" '
        'stroke-opacity=".28" stroke-width="2.5" stroke-linecap="round" '
        'stroke-dasharray="2 16"/>'.format(d=d)
        + ''.join(_hero_pin(x, y, dl, accent=(i == 2))
                  for i, (x, y, dl) in enumerate(zip(_PIN_X, _PIN_Y, _PIN_DELAY)))
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
