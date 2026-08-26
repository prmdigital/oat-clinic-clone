# -*- coding: utf-8 -*-
"""Page chrome: head, masthead, mobile drawer, footer, icons, JSON-LD.

Kept separate from build.py so the page renderers stay readable.
"""

import hashlib
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from content.data import SITE, LOCATIONS, SCHEMA_HOURS, FOOTER_QUICK_LINKS
from content.treatments import TREATMENTS

# --------------------------------------------------------------------------- #
# Icons. A single stroked set at 24x24 so nothing reads as clip art.
# --------------------------------------------------------------------------- #

def _svg(paths, size=24, stroke=1.5, fill=False):
    attrs = (
        'xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" '
        'viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" '
        'aria-hidden="true" focusable="false"'
    ).format(s=size, w=stroke)
    return '<svg {a}>{p}</svg>'.format(a=attrs, p=paths)


ICON_PATHS = {
    "check": '<path d="m20 6-11 11-5-5"/>',
    "arrow": '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "phone": '<path d="M6.6 2.5a1.5 1.5 0 0 1 1.9.6l1.5 2.6a1.5 1.5 0 0 1-.3 1.9l-1.2 1a11 11 0 0 0 5 5l1-1.2a1.5 1.5 0 0 1 1.9-.3l2.6 1.5a1.5 1.5 0 0 1 .6 1.9l-.8 1.9a2 2 0 0 1-2.2 1.2A17.5 17.5 0 0 1 3.4 6.5 2 2 0 0 1 4.6 4.3z"/>',
    "pin": '<path d="M20 10c0 5.5-8 12-8 12s-8-6.5-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="2.8"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.2l3.2 2"/>',
    "video": '<rect x="2.5" y="6" width="13" height="12" rx="2.2"/><path d="m15.5 10.8 5-2.9v8.2l-5-2.9z"/>',
    "clinic": '<path d="M3.5 20.5V9.2L12 3.5l8.5 5.7v11.3"/><path d="M9.5 20.5v-5.2h5v5.2"/><path d="M12 8v4M10 10h4"/>',
    "pharmacy": '<rect x="3.5" y="3.5" width="17" height="17" rx="4"/><path d="M12 8v8M8 12h8"/>',
    "shield": '<path d="M12 2.8 4.5 6v6c0 4.4 3.1 8.1 7.5 9.2 4.4-1.1 7.5-4.8 7.5-9.2V6z"/><path d="m9.2 12 2 2 3.6-3.8"/>',
    "alert": '<path d="M12 3.2 1.9 20.8h20.2z"/><path d="M12 9.5v4.4M12 17.4h.01"/>',
    "doc": '<path d="M14 2.8H7a2 2 0 0 0-2 2v14.4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7.8z"/><path d="M14 2.8V7.8h5"/><path d="M8.8 13h6.4M8.8 16.5h4.4"/>',
    "users": '<circle cx="9.5" cy="8" r="3.2"/><path d="M3.2 20.2a6.3 6.3 0 0 1 12.6 0"/><path d="M16.5 5.2a3.2 3.2 0 0 1 0 5.6M17.5 14.4a6.3 6.3 0 0 1 3.3 5.8"/>',
    "route": '<circle cx="6" cy="18.5" r="2.5"/><circle cx="18" cy="5.5" r="2.5"/><path d="M15.5 5.5H9.8A3.8 3.8 0 0 0 9.8 13h4.4a3.8 3.8 0 0 1 0 7.6H8.5"/>',
}


def icon(name, size=24, stroke=1.5):
    return _svg(ICON_PATHS[name], size=size, stroke=stroke)


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #

def asset_version(relpath):
    """Short content hash, so browsers refetch an asset only when it changes."""
    full = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), relpath)
    try:
        fh = open(full, 'rb')
        digest = hashlib.sha1(fh.read()).hexdigest()[:8]
        fh.close()
        return digest
    except IOError:
        return '0'


CSS_VERSION = asset_version(os.path.join('assets', 'css', 'site.css'))
JS_VERSION = asset_version(os.path.join('assets', 'js', 'site.js'))


def esc(text):
    return (str(text).replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


def maps_query(loc):
    q = '{0}, {1}, {2} {3}'.format(loc['street'], loc['city'], loc['region'], loc['postal'])
    return q.replace(' ', '+').replace(',', '%2C').replace('#', '%23')


def maps_link(loc):
    return 'https://www.google.com/maps/search/?api=1&amp;query=' + maps_query(loc)


def maps_embed(loc):
    return 'https://maps.google.com/maps?q={0}&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed'.format(maps_query(loc))


def full_address(loc, sep=', '):
    return sep.join([loc['street'], '{0}, {1} {2}'.format(loc['city'], loc['region'], loc['postal'])])


# --------------------------------------------------------------------------- #
# Structured data
# --------------------------------------------------------------------------- #

def _clinic_node(loc):
    node = {
        "@type": "MedicalClinic",
        "@id": SITE['base_url'] + '/locations/' + loc['slug'] + '/#clinic',
        "name": loc['name'],
        "parentOrganization": {"@id": SITE['base_url'] + '/#organization'},
        "url": SITE['base_url'] + '/locations/' + loc['slug'] + '/',
        "telephone": loc['phone'],
        "medicalSpecialty": "Addiction Medicine",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": loc['street'],
            "addressLocality": loc['city'],
            "addressRegion": loc['region'],
            "postalCode": loc['postal'],
            "addressCountry": "CA",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": loc['lat'], "longitude": loc['lng']},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": h['days'],
             "opens": h['opens'], "closes": h['closes']} for h in SCHEMA_HOURS
        ],
    }
    if loc.get('fax'):
        node['faxNumber'] = loc['fax']
    return node


def organization_node():
    return {
        "@type": ["MedicalOrganization", "Organization"],
        "@id": SITE['base_url'] + '/#organization',
        "name": SITE['legal_name'],
        "url": SITE['base_url'] + '/',
        "description": SITE['description'],
        "telephone": SITE['main_phone'],
        "email": SITE['email'],
        "areaServed": {"@type": "AdministrativeArea", "name": "Lower Mainland, British Columbia"},
        "medicalSpecialty": "Addiction Medicine",
        "location": [{"@id": SITE['base_url'] + '/locations/' + l['slug'] + '/#clinic'}
                     for l in LOCATIONS],
    }


def breadcrumb_node(crumbs, url):
    items = []
    for i, (label, href) in enumerate(crumbs, start=1):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = SITE['base_url'] + href
        items.append(entry)
    return {"@type": "BreadcrumbList", "@id": url + '#breadcrumbs', "itemListElement": items}


def faq_node(faqs, url):
    return {
        "@type": "FAQPage",
        "@id": url + '#faq',
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": ' '.join(a)}}
            for q, a in faqs
        ],
    }


def jsonld(nodes):
    graph = {"@context": "https://schema.org", "@graph": [n for n in nodes if n]}
    body = json.dumps(graph, ensure_ascii=False, indent=2).replace('</', '<\\/')
    return '<script type="application/ld+json">\n{0}\n</script>'.format(body)


# --------------------------------------------------------------------------- #
# Chrome
# --------------------------------------------------------------------------- #

def _nav_panel_treatments():
    rows = []
    for t in TREATMENTS:
        rows.append(
            '<a href="/treatments/{s}/">{n}</a>'.format(
                s=t['slug'], n=esc(t['nav_name'])))
    rows.append('<div class="all"><a href="/treatments/">All treatment programmes '
                + icon('arrow', 15) + '</a></div>')
    return ''.join(rows)


def _nav_panel_locations():
    rows = []
    for l in LOCATIONS:
        rows.append(
            '<a href="/locations/{s}/">{c}</a>'.format(
                s=l['slug'], c=esc(l['city'])))
    rows.append('<div class="all"><a href="/locations/">All five clinics '
                + icon('arrow', 15) + '</a></div>')
    return ''.join(rows)


def masthead(active):
    def cur(key):
        return ' aria-current="page"' if active == key else ''

    return '''
<header class="masthead">
  <div class="wrap">
    <a class="wordmark" href="/">
      <img src="/assets/img/logo-96.png" alt="OAT Clinic" width="56" height="56">
    </a>

    <nav class="nav" aria-label="Primary">
      <div class="nav-item" data-dropdown>
        <a class="nav-link" href="/treatments/" aria-expanded="false"{ct}>Treatments {chev}</a>
        <div class="nav-panel">{tpanel}</div>
      </div>
      <div class="nav-item" data-dropdown>
        <a class="nav-link" href="/locations/" aria-expanded="false"{cl}>Locations {chev}</a>
        <div class="nav-panel">{lpanel}</div>
      </div>
      <div class="nav-item"><a class="nav-link" href="/what-to-expect/"{cw}>What to expect</a></div>
      <div class="nav-item"><a class="nav-link" href="/for-pharmacies/"{cp}>For pharmacies</a></div>
      <div class="nav-item"><a class="nav-link" href="/blog/"{cb}>Blog</a></div>
    </nav>

    <a class="mast-call" href="{phref}">
      <span class="l">Call us now</span>
      <span class="n">{phone}</span>
    </a>
    <a class="btn btn-accent mast-cta" href="/contact/">Get help today</a>

    <button class="burger" type="button" aria-expanded="false"
            aria-controls="drawer" aria-label="Open menu"><span></span></button>
  </div>
</header>

<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer-head">
    <a class="wordmark" href="/">
      <img src="/assets/img/logo-96.png" alt="OAT Clinic" width="44" height="44">
    </a>
    <button class="burger" type="button" data-close aria-expanded="true"
            aria-label="Close menu"><span></span></button>
  </div>
  <div class="drawer-body">
    <div class="drawer-group">
      <a href="/">Home</a>
      <a href="/what-to-expect/">What to expect</a>
      <a href="/for-pharmacies/">For pharmacies</a>
      <a href="/blog/">Blog</a>
      <a href="/contact/">Contact</a>
    </div>
    <div class="drawer-group sub">
      <p class="h">Treatments</p>
      {dtreat}
      <a href="/treatments/">All treatment programmes</a>
    </div>
    <div class="drawer-group sub">
      <p class="h">Locations</p>
      {dloc}
      <a href="/locations/">All five clinics</a>
    </div>
  </div>
  <div class="drawer-foot">
    <a class="btn btn-primary" href="{phref}">{phoneicon} Call {phone}</a>
    <a class="btn btn-outline" href="/contact/">Request a callback</a>
  </div>
</div>
'''.format(
        name=SITE['name'],
        phone=SITE['main_phone'],
        phref=SITE['main_phone_href'],
        phoneicon=icon('phone', 17),
        chev='<span class="chev">' + icon('chevron', 14) + '</span>',
        tpanel=_nav_panel_treatments(),
        lpanel=_nav_panel_locations(),
        ct=cur('treatments'), cl=cur('locations'), cw=cur('what-to-expect'),
        cp=cur('for-pharmacies'), cb=cur('blog'),
        dtreat=''.join('<a href="/treatments/{s}/">{n}</a>'.format(s=t['slug'], n=esc(t['name']))
                       for t in TREATMENTS),
        dloc=''.join('<a href="/locations/{s}/">{c}</a>'.format(s=l['slug'], c=esc(l['city']))
                     for l in LOCATIONS),
    )


def footer():
    treat_links = ''.join(
        '<li><a href="/treatments/{s}/">{n}</a></li>'.format(s=t['slug'], n=esc(t['name']))
        for t in TREATMENTS)
    quick_links = ''.join(
        '<li><a href="{h}">{n}</a></li>'.format(h=h, n=esc(n))
        for n, h in FOOTER_QUICK_LINKS)
    addr = ''.join(
        '<li><a href="/locations/{s}/">{c}</a></li>'.format(s=l['slug'], c=esc(l['city']))
        for l in LOCATIONS)

    return '''
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-main">
      <div>
        <span class="wordmark foot">
          <img src="/assets/img/logo-light.png" alt="OAT Clinic" width="93" height="44">
        </span>
        <p class="foot-desc">Opioid agonist treatment across the Lower Mainland. In clinic,
          by telemedicine, and through the pharmacy you already use.</p>
        <div class="foot-phones">
          <a href="tel:+16046706580"><span class="c">Vancouver</span><span class="n">604-670-6580</span></a>
          <a href="tel:+16047554408"><span class="c">Abbotsford</span><span class="n">604-755-4408</span></a>
        </div>
      </div>
      <div>
        <h3>Treatments</h3>
        <ul class="foot-links">{treat}</ul>
      </div>
      <div>
        <h3>Clinic</h3>
        <ul class="foot-links">{quick}</ul>
      </div>
      <div>
        <h3>Our clinics</h3>
        <ul class="foot-links">{addr}</ul>
      </div>
    </div>
    <p class="foot-disclaimer">
      The information on this website is general and is provided for education. It is not
      medical advice and it does not replace an assessment by a qualified clinician. Never
      start, stop or change a prescribed medication based on what you read here. If you are
      experiencing a medical emergency, call 911.
    </p>
  </div>
  <div class="foot-legal">
    <div class="wrap" style="display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap;">
      <span>&copy; <span data-year>2026</span> {name}. All rights reserved.</span>
      <nav aria-label="Legal">
        <a href="/privacy/">Privacy policy</a>
        <a href="/terms/">Terms of use</a>
        <a href="/accessibility/">Accessibility</a>
      </nav>
    </div>
  </div>
</footer>

<div class="callbar">
  <a class="c1" href="{phref}">{ph} Call now</a>
  <a class="c2" href="/contact/">Request a callback</a>
</div>
'''.format(treat=treat_links, quick=quick_links, addr=addr,
           name=SITE['legal_name'], phref=SITE['main_phone_href'], ph=icon('phone', 16))


def crumbs(items):
    """items: [(label, href_or_None)] with the last entry being the current page."""
    parts = []
    for i, (label, href) in enumerate(items):
        if i:
            parts.append('<span class="sep">/</span>')
        if href:
            parts.append('<a href="{h}">{l}</a>'.format(h=href, l=esc(label)))
        else:
            parts.append('<span aria-current="page">{l}</span>'.format(l=esc(label)))
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ''.join(parts) + '</nav>'


def emergency_note():
    return (
        '<div class="emergency">' + icon('alert', 22) +
        '<p><b>If this is an emergency, call 911.</b> Overdose symptoms, trouble breathing, '
        'chest pain, seizures or an immediate mental health crisis need emergency care, not a '
        'callback form. In British Columbia you can also reach the <a href="tel:18007847233">'
        'Suicide Crisis Helpline at 988</a> or call 811 for HealthLink BC nurse advice.</p></div>'
    )


# --------------------------------------------------------------------------- #
# Document
# --------------------------------------------------------------------------- #

PAGE = '''<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">

<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{sitename}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_CA">
<meta property="og:image" content="{ogimage}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="OAT Clinic. Opioid agonist treatment across the Lower Mainland.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimage}">

<meta name="theme-color" content="#015F9C">
<meta name="format-detection" content="telephone=yes">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap">
<script>document.documentElement.className += ' js';</script>
<link rel="stylesheet" href="/assets/css/site.css?v={cssv}">
{head_extra}
{structured}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
{masthead}
<main id="main">
{body}
</main>
{footer}
<script src="/assets/js/site.js?v={jsv}" defer></script>
</body>
</html>
'''


def render(path, title, desc, body, active=None, extra_nodes=None,
           ogtype='website', head_extra='', robots='index, follow', crumb_items=None):
    canonical = SITE['base_url'] + path
    # A preview deployment must never be indexed: the clinical copy has not
    # been reviewed by the clinic, and the domain is not the real one.
    if SITE.get('preview') and robots == 'index, follow':
        robots = 'noindex, nofollow'
    nodes = [organization_node()]
    if crumb_items:
        nodes.append(breadcrumb_node(crumb_items, canonical))
    if extra_nodes:
        nodes.extend(extra_nodes)

    full_title = title if title.endswith(SITE['name']) else '{0} | {1}'.format(title, SITE['name'])
    return PAGE.format(
        ogimage=SITE['base_url'] + '/assets/img/og-default.png',
        cssv=CSS_VERSION,
        jsv=JS_VERSION,
        title=esc(full_title),
        desc=esc(desc),
        canonical=canonical,
        robots=robots,
        ogtype=ogtype,
        sitename=esc(SITE['name']),
        head_extra=head_extra,
        structured=jsonld(nodes),
        masthead=masthead(active),
        body=body,
        footer=footer(),
    )
