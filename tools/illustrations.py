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

_OPEN = ('<svg class="art" viewBox="0 0 240 150" role="img" '
         'aria-label="{alt}" xmlns="http://www.w3.org/2000/svg">'
         '<rect width="240" height="150" rx="14" fill="var(--blue-tint)"/>')
_CLOSE = '</svg>'

# A deeper tint than --blue-tint, used for ground planes and receding shapes.
SHADE = '#C9DFEE'


def _wrap(alt, inner):
    return _OPEN.format(alt=alt) + inner + _CLOSE


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


ART = {
    'clinic': clinic,
    'telehealth': telehealth,
    'pharmacy': pharmacy,
}


def art(name):
    return ART[name]()
