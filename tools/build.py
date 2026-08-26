# -*- coding: utf-8 -*-
"""Static site generator for OAT Clinic.

    python tools/build.py

Reads content/ and writes plain HTML to the repository root. No dependencies
beyond the Python standard library. Output is committed, so the site can be
served by GitHub Pages, Netlify, Vercel or any static host with no build step
on their side.
"""

from __future__ import print_function

import os
import re
import shutil
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from content.data import SITE, LOCATIONS, DEFAULT_HOURS, CALLBACK_REASONS
from content.treatments import TREATMENTS
from content.posts import POSTS, AUTHORS

from shell import (render, crumbs, icon, esc, emergency_note, maps_link,
                   maps_embed, full_address, faq_node, breadcrumb_node,
                   organization_node, _clinic_node, jsonld)

TREATMENT_BY_SLUG = dict((t['slug'], t) for t in TREATMENTS)
LOCATION_BY_SLUG = dict((l['slug'], l) for l in LOCATIONS)

WRITTEN = []


# --------------------------------------------------------------------------- #
# Output helpers
# --------------------------------------------------------------------------- #

def target_is_html(path):
    """Everything except the sitemap and robots.txt is an HTML page."""
    return not (path.endswith('.xml') or path.endswith('.txt'))


# Matches href="/..." and src="/..." but not protocol relative "//host".
_ABS_REF = re.compile(r'\b(href|src)="/(?!/)')


def apply_base_path(html):
    """Prefix internal absolute URLs with the deployment sub path.

    Doing this at one choke point keeps every page renderer readable, and
    moving the site to a root domain becomes a one line config change rather
    than a find and replace across the whole generator.
    """
    base = SITE.get('base_path', '').rstrip('/')
    if not base:
        return html
    return _ABS_REF.sub(lambda m: '%s="%s/' % (m.group(1), base), html)


def write(path, html):
    """path is a URL path such as '/treatments/methadone/'."""
    if target_is_html(path):
        html = apply_base_path(html)
    if path == '/':
        target = os.path.join(ROOT, 'index.html')
    elif path.endswith('.html') or path.endswith('.xml') or path.endswith('.txt'):
        target = os.path.join(ROOT, path.lstrip('/').replace('/', os.sep))
    else:
        target = os.path.join(ROOT, path.strip('/').replace('/', os.sep), 'index.html')

    folder = os.path.dirname(target)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)

    fh = open(target, 'w', encoding='utf-8', newline='\n')
    fh.write(html)
    fh.close()
    WRITTEN.append(path)


def fmt_date(iso):
    d = datetime.datetime.strptime(iso, '%Y-%m-%d')
    return '{0} {1} {2}'.format(d.day, d.strftime('%B'), d.year)


# --------------------------------------------------------------------------- #
# Shared blocks
# --------------------------------------------------------------------------- #

def callback_form(heading='Request a confidential callback',
                  sub='It takes under a minute. Our team calls you back the same business day.'):
    reasons = ''.join('<option>{0}</option>'.format(esc(r)) for r in CALLBACK_REASONS)
    return '''
<div class="callback" id="callback">
  <h2>{h}</h2>
  <p class="dek">{s}</p>
  <form id="callback-form" novalidate>
    <label class="field">
      <span class="lab">Your name <span class="req">*</span></span>
      <input type="text" name="name" data-rule="name" autocomplete="given-name"
             placeholder="A first name is enough" required>
      <span class="err" role="alert"></span>
    </label>
    <label class="field">
      <span class="lab">Phone number <span class="req">*</span></span>
      <input type="tel" name="phone" data-rule="phone" autocomplete="tel"
             inputmode="tel" placeholder="604 555 0123" required>
      <span class="err" role="alert"></span>
    </label>
    <label class="field">
      <span class="lab">What is this about</span>
      <select name="reason">{r}</select>
    </label>
    <label class="field">
      <span class="lab">Best time to call</span>
      <select name="time">
        <option>As soon as possible</option>
        <option>Morning, 10 AM to 12 PM</option>
        <option>Afternoon, 12 to 3 PM</option>
        <option>Late afternoon, 3 to 6 PM</option>
      </select>
    </label>
    <label class="field" style="display:flex;gap:10px;align-items:flex-start;">
      <input type="checkbox" name="consent" data-rule="consent"
             style="width:auto;margin-top:5px;flex:none;">
      <span>
        <span class="lab" style="margin:0;font-weight:500;line-height:1.45;">
          It is safe to leave a voicemail at this number.
        </span>
        <span class="err" role="alert"></span>
      </span>
    </label>
    <button class="btn btn-blue" type="submit">Request a callback</button>
    <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
    <p class="form-note">
      Confidential and handled under BC health privacy law.
      Read our <a href="/privacy/">privacy policy</a>.<br>
      In an emergency, call 911 instead of using this form.
    </p>
  </form>
</div>'''.format(h=esc(heading), s=esc(sub), r=reasons)


def cta_band(heading, text, primary_label='Call {0}'.format(SITE['main_phone'])):
    return '''
<section class="cta-band section">
  <div class="wrap">
    <h2>{h}</h2>
    <p class="lede">{t}</p>
    <div class="btn-row">
      <a class="btn btn-white" href="{ph}">{icon} {pl}</a>
      <a class="btn btn-ghost" href="/contact/">Request a callback</a>
    </div>
  </div>
</section>'''.format(h=esc(heading), t=esc(text), ph=SITE['main_phone_href'],
                     icon=icon('phone', 17), pl=esc(primary_label))


def faq_block(faqs, heading='Questions people actually ask', intro=None, eyebrow='FAQ',
              section_id='faq'):
    items = []
    for q, answers in faqs:
        items.append(
            '<details class="faq-item"><summary>{q}<span class="plus"></span></summary>'
            '<div class="faq-answer">{a}</div></details>'.format(
                q=esc(q), a=''.join(answers)))
    intro_html = '<p class="lede">{0}</p>'.format(esc(intro)) if intro else ''
    return '''
<section class="section" id="{sid}">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">{e}</span>
      <h2>{h}</h2>
      {i}
    </div>
    <div class="faq-list">{items}</div>
  </div>
</section>'''.format(sid=section_id, e=esc(eyebrow), h=esc(heading),
                     i=intro_html, items=''.join(items))


def balance_block(balance):
    def col(kind, title, items):
        ic = icon('check', 19) if kind == 'good' else icon('alert', 19)
        lis = ''.join('<li>{0}</li>'.format(esc(i)) for i in items)
        return ('<div class="balance-col {k}"><h3>{ic} {t}</h3><ul>{l}</ul></div>'
                .format(k=kind, ic=ic, t=esc(title), l=lis))
    return ('<div class="balance">'
            + col('good', balance['good_title'], balance['good'])
            + col('note', balance['note_title'], balance['note'])
            + '</div>')


def keypoints_block(points, heading='In short'):
    lis = ''.join('<li>{0} {1}</li>'.format(icon('check', 17), esc(p)) for p in points)
    return ('<div class="keypoints"><p class="h">{h}</p><ul>{l}</ul></div>'
            .format(h=esc(heading), l=lis))


def pagehead(crumb_html, h1, lede, aside=''):
    # A single column reads calmer than the two column split it replaced,
    # which left a large void beside the headline on every interior page.
    return '''
<section class="pagehead">
  <div class="wrap">
    {c}
    <div class="pagehead-body">
      <h1>{h}</h1>
      <p class="lede">{l}</p>
      {a}
    </div>
  </div>
</section>'''.format(c=crumb_html, h=esc(h1), l=esc(lede), a=aside)


def treatment_rows(exclude=None, limit=None):
    rows = []
    items = [t for t in TREATMENTS if t['slug'] != exclude]
    if limit:
        items = items[:limit]
    for i, t in enumerate(items, start=1):
        tag = ('<span class="tag">{0}</span>'.format(esc(t['tag']))) if t.get('tag') else ''
        rows.append('''
<a class="row-link" href="/treatments/{s}/">
  <span class="row-num">{n:02d}</span>
  <span class="row-body"><h3>{t}{tag}</h3><p>{d}</p></span>
  <span class="row-go">{ic}</span>
</a>'''.format(s=t['slug'], n=i, t=esc(t['name']), tag=tag,
                d=esc(t['lede'].split('. ')[0] + '.'), ic=icon('arrow', 17)))
    return '<div class="rows">' + ''.join(rows) + '</div>'


def location_rows(exclude=None):
    rows = []
    items = [l for l in LOCATIONS if l['slug'] != exclude]
    for i, l in enumerate(items, start=1):
        rows.append('''
<a class="row-link" href="/locations/{s}/">
  <span class="row-num">{n:02d}</span>
  <span class="row-body"><h3>{c}</h3><p>{a}</p></span>
  <span class="row-go">{ic}</span>
</a>'''.format(s=l['slug'], n=i, c=esc(l['city']),
                a=esc(full_address(l)), ic=icon('arrow', 17)))
    return '<div class="rows">' + ''.join(rows) + '</div>'


def post_card(post):
    a = AUTHORS[post['author']]
    pill = 'pill {0}'.format(post.get('category_class', '')).strip()
    return '''
<a class="card" href="/blog/{s}/">
  <div class="card-body">
    <span class="{pc}">{cat}</span>
    <h3 style="margin-top:14px;">{t}</h3>
    <p>{l}</p>
    <div class="post-meta" style="margin-top:18px;">
      <span>{d}</span><span class="dot">&middot;</span><span>{rt}</span>
    </div>
  </div>
</a>'''.format(s=post['slug'], pc=pill, cat=esc(post['category']), t=esc(post['title']),
               l=esc(post['lede']), d=fmt_date(post['date']), rt=esc(post['read_time']))


# --------------------------------------------------------------------------- #
# Home
# --------------------------------------------------------------------------- #

# build_home now lives in tools/home.py, see the note there about section count.


# --------------------------------------------------------------------------- #
# Treatments
# --------------------------------------------------------------------------- #

def build_treatments_index():
    crumb_items = [('Home', '/'), ('Treatments', None)]
    body = pagehead(
        crumbs(crumb_items),
        'Treatment programmes',
        'Five programmes covering opioid agonist treatment and the substances that most often '
        'sit alongside it. Each page explains how the treatment works, what the first weeks are '
        'like, and what it costs in British Columbia.',
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Choose a programme</span>
      <h2>What we treat</h2>
      <p class="lede">If you are not sure which applies to you, that is normal and it is what
        the assessment is for. Call us and we will work it out together.</p>
    </div>
    {rows}
  </div>
</section>

<section class="section band-tint">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <h2>Not sure where to start?</h2>
        <p class="lede" style="margin-top:16px;">Most people arrive unsure whether methadone or
          Suboxone suits them, and the honest answer is that it depends on your tolerance, your
          schedule and what you have already tried. Our comparison walks through how the
          decision actually gets made.</p>
        <div class="btn-row" style="margin-top:26px;">
          <a class="btn btn-blue" href="/blog/methadone-or-suboxone-how-to-choose/">Compare methadone and Suboxone</a>
        </div>
      </div>
      <div>{callout}</div>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="wrap">{emergency}</div>
</section>

{cta}
'''.format(
        rows=treatment_rows(),
        callout=keypoints_block([
            'Assessment covers every substance you use, not opioids alone',
            'Appointments are billed to MSP, so there is no fee to see us',
            'Medication is covered by BC PharmaCare for most residents',
            'You can switch between treatments at any point',
            'Continued substance use is never a reason for discharge',
        ], heading='What applies across all programmes'),
        emergency=emergency_note(),
        cta=cta_band('Talk it through before you decide.',
                     'A first conversation commits you to nothing at all.'),
    )
    write('/treatments/', render(
        '/treatments/', 'Treatment Programmes',
        'Methadone, Suboxone, substance use treatment, benzodiazepine support and nicotine '
        'cessation across five clinics in the BC Lower Mainland.',
        body, active='treatments', crumb_items=crumb_items))


def build_treatment(t):
    path = '/treatments/{0}/'.format(t['slug'])
    crumb_items = [('Home', '/'), ('Treatments', '/treatments/'), (t['name'], None)]

    # At a glance strip. Structured facts answer the questions people scan for
    # before committing to reading, and give the page something other than
    # paragraphs to look at.
    facts = ''.join(
        '<div class="spec-item"><div class="k">{k}</div><div class="v">{v}</div></div>'
        .format(k=esc(k), v=esc(v)) for k, v in t['facts'])

    # Sticky rail. Long clinical pages are much easier to use when you can see
    # the shape of the whole thing and jump within it.
    nav = ''.join(
        '<li><a href="#{a}">{h}</a></li>'.format(a=a, h=esc(h))
        for a, h, _ in t['sections'])
    nav += '<li><a href="#balance">Benefits and trade offs</a></li>'
    nav += '<li><a href="#faq">Questions answered</a></li>'

    # The pull quote lands after the second section, which is the point where
    # an unbroken text column starts to feel long.
    blocks = []
    for i, (anchor, heading, body_blocks) in enumerate(t['sections']):
        blocks.append(
            '<section class="doc-section" id="{a}">'
            '<h2>{h}</h2><div class="prose">{b}</div></section>'.format(
                a=anchor, h=esc(heading), b=''.join(body_blocks)))
        if i == 1:
            blocks.append(
                '<blockquote class="pullquote"><p>{q}</p></blockquote>'.format(
                    q=esc(t['pullquote'])))

    related = ''.join(
        '<a class="card" href="/treatments/{s}/"><div class="card-body">'
        '<h3>{n}</h3><p>{d}</p><span class="link-arrow">Read more {ar}</span>'
        '</div></a>'.format(s=r, n=esc(TREATMENT_BY_SLUG[r]['name']),
                            d=esc(TREATMENT_BY_SLUG[r]['nav_desc']), ar=icon('arrow', 15))
        for r in t['related'])

    body = pagehead(
        crumbs(crumb_items), t['h1'], t['lede'],
        aside='<div class="btn-row">'
              '<a class="btn btn-primary" href="{ph}">{pi} Call {p}</a>'
              '<a class="btn btn-ghost" href="/contact/">Request a callback</a></div>'.format(
                  ph=SITE['main_phone_href'], pi=icon('phone', 17), p=SITE['main_phone']),
    ) + '''
<div class="spec"><div class="wrap">{facts}</div></div>

<section class="section">
  <div class="wrap">
    <div class="doc">
      <aside class="doc-nav" aria-label="On this page">
        <p class="h">On this page</p>
        <ol>{nav}</ol>
        <div class="doc-nav-cta">
          <a class="btn btn-primary" href="{ph}">{pi} Call {phone}</a>
        </div>
      </aside>
      <div class="doc-body">
        {key}
        {blocks}
      </div>
    </div>
  </div>
</section>

<section class="section band-tint" id="balance">
  <div class="wrap">
    <div class="sec-head">
      <h2>What this treatment does well, and what to weigh up</h2>
      <p class="lede">Every option has trade offs. Here are both sides.</p>
    </div>
    {balance}
  </div>
</section>
{faq}
<section class="section band-tint">
  <div class="wrap">
    <div class="sec-head"><h2>Other programmes</h2></div>
    <div class="grid-3">{related}</div>
  </div>
</section>
<section class="section-sm">
  <div class="wrap">{emergency}</div>
</section>
{cta}
'''.format(
        facts=facts, nav=nav, blocks=''.join(blocks),
        key=keypoints_block(t['keypoints']),
        ph=SITE['main_phone_href'], pi=icon('phone', 17), phone=SITE['main_phone'],
        balance=balance_block(t['balance']),
        faq=faq_block(t['faqs'],
                      heading='{0}: your questions answered'.format(t['name']),
                      intro='These are the questions our physicians are asked most often '
                            'about this treatment. If yours is not here, call us and ask.'),
        related=related,
        emergency=emergency_note(),
        cta=cta_band('Ready to talk about {0}?'.format(t['name'].lower()),
                     'No referral needed. Assessment and, where appropriate, treatment '
                     'the same day.'),
    )

    canonical = SITE['base_url'] + path
    write(path, render(
        path, t['name'], t['meta_desc'], body, active='treatments',
        crumb_items=crumb_items,
        extra_nodes=[faq_node(t['faqs'], canonical), {
            "@type": "MedicalWebPage",
            "@id": canonical + '#page',
            "url": canonical,
            "name": t['name'],
            "description": t['meta_desc'],
            "about": {"@type": "MedicalCondition", "name": "Opioid use disorder"},
            "audience": {"@type": "PeopleAudience", "geographicArea": {
                "@type": "AdministrativeArea", "name": "British Columbia"}},
            "lastReviewed": datetime.date.today().isoformat(),
            "publisher": {"@id": SITE['base_url'] + '/#organization'},
        }]))


# --------------------------------------------------------------------------- #
# Locations
# --------------------------------------------------------------------------- #

def build_locations_index():
    crumb_items = [('Home', '/'), ('Locations', None)]
    cards = ''.join('''
<a class="card" href="/locations/{s}/">
  <div class="card-body">
    <span class="pill">{c}</span>
    <h3 style="margin-top:14px;">{n}</h3>
    <p>{a}</p>
    <p style="margin-top:10px;font-size:15px;color:var(--ink-3);">{nb}</p>
    <span class="link-arrow" style="margin-top:18px;">Clinic details {ar}</span>
  </div>
</a>'''.format(s=l['slug'], c=esc(l['city']), n=esc(l['name']),
                a=esc(full_address(l)), nb=esc(l['neighbourhood'].capitalize()),
                ar=icon('arrow', 15)) for l in LOCATIONS)

    body = pagehead(
        crumbs(crumb_items),
        'Five clinics across the Lower Mainland',
        'Vancouver, Abbotsford, Surrey, Burnaby and Chilliwack. Every location offers '
        'assessment, prescribing and follow up, and your medication can be dispensed at '
        'whichever pharmacy is most convenient for you.',
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="grid-3">{cards}</div>
  </div>
</section>

<section class="section band-tint">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <span class="eyebrow">Hours</span>
        <h2>When we are open</h2>
        <p class="lede" style="margin-top:16px;">All clinics keep the same core hours.
          Smaller locations run on set days, so call ahead before travelling to Chilliwack,
          Surrey or Burnaby.</p>
        <p style="margin-top:16px;">{note}</p>
      </div>
      <div>
        <table class="hours-table">{hours}</table>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Cannot travel?</span>
      <h2>Telemedicine reaches further than our clinics do</h2>
      <p class="lede">If none of these locations is realistic for you, a telemedicine
        assessment can usually be arranged instead. Your medication is then dispensed at a
        pharmacy near where you live.</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-blue" href="/contact/">Request a telemedicine assessment</a>
      <a class="btn btn-outline" href="/what-to-expect/">How it works</a>
    </div>
  </div>
</section>

{cta}
'''.format(
        cards=cards,
        note=esc(SITE['hours_note']),
        hours=''.join(
            '<tr><th>{d}</th><td class="{c}">{h}</td></tr>'.format(
                d=d, c='' if h else 'closed', h=h or 'Closed')
            for d, h in DEFAULT_HOURS),
        cta=cta_band('Not sure which clinic to go to?',
                     'Call our main line and we will point you to the right one.'),
    )
    write('/locations/', render(
        '/locations/', 'Clinic Locations',
        'OAT Clinic locations in Vancouver, Abbotsford, Surrey, Burnaby and Chilliwack. '
        'Addresses, hours, phone numbers and directions.',
        body, active='locations', crumb_items=crumb_items,
        extra_nodes=[_clinic_node(l) for l in LOCATIONS]))


def build_location(loc):
    path = '/locations/{0}/'.format(loc['slug'])
    crumb_items = [('Home', '/'), ('Locations', '/locations/'), (loc['city'], None)]

    facts = [
        ('Address', '{0}<br>{1}, {2} {3}'.format(
            esc(loc['street']), esc(loc['city']), loc['region'], loc['postal'])),
        ('Phone', '<a href="{0}">{1}</a>'.format(loc['phone_href'], loc['phone'])),
        ('Hours', 'Mon to Fri<br>10:00 AM to 6:00 PM'),
    ]
    if loc.get('fax'):
        facts.append(('Fax', loc['fax']))
    facts_html = ''.join(
        '<div class="loc-fact"><div class="k">{k}</div><div class="v">{v}</div></div>'
        .format(k=esc(k), v=v) for k, v in facts)

    highlights = ''.join('<li>{0} {1}</li>'.format(icon('check', 17), esc(h))
                         for h in loc['highlights'])

    body = pagehead(
        crumbs(crumb_items),
        'OAT Clinic {0}'.format(loc['city']),
        loc['intro'],
        aside='<div class="btn-row">'
              '<a class="btn btn-primary" href="{ph}">{pi} Call {p}</a>'
              '<a class="btn btn-ghost" href="{m}" target="_blank" rel="noopener">'
              'Get directions</a></div>'.format(
                  ph=loc['phone_href'], pi=icon('phone', 17), p=loc['phone'], m=maps_link(loc)),
    ) + '''
<section class="section-sm">
  <div class="wrap">
    <div class="loc-facts">{facts}</div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="grid-2" style="align-items:start;">
      <div class="map-frame">
        <iframe src="{embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
                title="Map showing OAT Clinic {city} at {addr}"></iframe>
      </div>
      <div>
        <h2>Getting here</h2>
        <div class="prose" style="margin-top:16px;">
          <h3>By transit</h3><p>{transit}</p>
          <h3>Parking</h3><p>{parking}</p>
          <h3>Accessibility</h3><p>{access}</p>
        </div>
        <div class="btn-row" style="margin-top:26px;">
          <a class="btn btn-outline" href="{maps}" target="_blank" rel="noopener">
            {pin} Open in Google Maps</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section band-tint">
  <div class="wrap">
    <div class="grid-2" style="align-items:start;">
      <div>
        <span class="eyebrow">This location</span>
        <h2>What {city} offers</h2>
        <div class="keypoints" style="margin-top:24px;"><ul>{highlights}</ul></div>
      </div>
      <div>
        <span class="eyebrow">Opening hours</span>
        <h2>When to come</h2>
        <table class="hours-table" style="margin-top:24px;">{hours}</table>
        <p style="margin-top:16px;font-size:15px;color:var(--ink-3);">{hnote}</p>
      </div>
    </div>
  </div>
</section>

{faq}

<section class="section band-tint">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Other clinics</span>
      <h2>If {city} is not the right fit</h2>
      <p class="lede">Care transfers between our clinics without starting over, and your
        record follows you.</p>
    </div>
    {others}
  </div>
</section>

<section class="section-sm">
  <div class="wrap">{emergency}</div>
</section>

{cta}
'''.format(
        facts=facts_html, embed=maps_embed(loc), city=esc(loc['city']),
        addr=esc(full_address(loc)), transit=esc(loc['transit']),
        parking=esc(loc['parking']), access=esc(loc['access']),
        maps=maps_link(loc), pin=icon('pin', 17),
        highlights=highlights,
        hours=''.join('<tr><th>{d}</th><td class="{c}">{h}</td></tr>'.format(
            d=d, c='' if h else 'closed', h=h or 'Closed') for d, h in DEFAULT_HOURS),
        hnote=esc(SITE['hours_note']),
        faq=faq_block(loc['faqs'], heading='Visiting our {0} clinic'.format(loc['city']),
                      eyebrow='Local questions'),
        others=location_rows(exclude=loc['slug']),
        emergency=emergency_note(),
        cta=cta_band('Come in, or call first. Either works.',
                     'Assessment and, where appropriate, treatment on the same day.',
                     primary_label='Call {0}'.format(loc['phone'])),
    )

    canonical = SITE['base_url'] + path
    write(path, render(
        path, 'OAT Clinic {0}'.format(loc['city']),
        'Methadone and Suboxone treatment at OAT Clinic {0}, {1}. Same day assessment, '
        'hours, directions and phone number.'.format(loc['city'], loc['street']),
        body, active='locations', crumb_items=crumb_items,
        extra_nodes=[_clinic_node(loc), faq_node(loc['faqs'], canonical)]))


# --------------------------------------------------------------------------- #
# Blog
# --------------------------------------------------------------------------- #

def build_blog_index():
    crumb_items = [('Home', '/'), ('Blog', None)]
    feature = POSTS[0]
    rest = ''.join(post_card(p) for p in POSTS[1:])

    body = pagehead(
        crumbs(crumb_items),
        'Notes from the clinic',
        'Plain, practical writing about opioid agonist treatment in British Columbia. Written '
        'for patients and families rather than for other clinicians, and reviewed by our '
        'prescribing physicians.',
    ) + '''
<section class="section">
  <div class="wrap">
    <article class="post-card-feature">
      <div>
        <span class="pill {fc}">{fcat}</span>
        <h2><a href="/blog/{fs}/">{ft}</a></h2>
        <p class="lede">{fl}</p>
        <div class="post-meta" style="margin-top:20px;">
          <span>{fd}</span><span class="dot">&middot;</span><span>{frt}</span>
        </div>
        <div class="btn-row" style="margin-top:26px;">
          <a class="btn btn-blue" href="/blog/{fs}/">Read the article</a>
        </div>
      </div>
      <div>{key}</div>
    </article>
    <div class="grid-3">{rest}</div>
  </div>
</section>

<section class="section band-tint">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Editorial policy</span>
      <h2>How this blog is written</h2>
      <p class="lede" style="margin-inline:auto;">Everything here is written or reviewed by our
        prescribing physicians and reflects current practice in British Columbia. We aim to be
        useful rather than reassuring, which sometimes means saying that a treatment has real
        drawbacks. Nothing on this blog is a substitute for an assessment.</p>
    </div>
  </div>
</section>

{cta}
'''.format(
        fc=feature.get('category_class', ''), fcat=esc(feature['category']),
        fs=feature['slug'], ft=esc(feature['title']), fl=esc(feature['lede']),
        fd=fmt_date(feature['date']), frt=esc(feature['read_time']),
        key=keypoints_block([
            'Written and reviewed by prescribing physicians',
            'Reflects current British Columbia clinical practice',
            'Written for patients and families, not for clinicians',
            'Updated when provincial guidance changes',
        ], heading='About these articles'),
        rest=rest,
        cta=cta_band('Questions the blog did not answer?',
                     'Call us. There is no charge and no obligation to start anything.'),
    )
    write('/blog/', render(
        '/blog/', 'Blog',
        'Practical articles about methadone, Suboxone and opioid agonist treatment in British '
        'Columbia, written and reviewed by our prescribing physicians.',
        body, active='blog', crumb_items=crumb_items,
        extra_nodes=[{
            "@type": "Blog",
            "@id": SITE['base_url'] + '/blog/#blog',
            "name": "OAT Clinic blog",
            "url": SITE['base_url'] + '/blog/',
            "publisher": {"@id": SITE['base_url'] + '/#organization'},
            "blogPost": [{"@type": "BlogPosting",
                          "headline": p['title'],
                          "url": SITE['base_url'] + '/blog/' + p['slug'] + '/',
                          "datePublished": p['date']} for p in POSTS],
        }]))


def build_post(post):
    path = '/blog/{0}/'.format(post['slug'])
    crumb_items = [('Home', '/'), ('Blog', '/blog/'), (post['title'], None)]
    author = AUTHORS[post['author']]

    toc = ''.join('<li><a href="#{a}">{t}</a></li>'.format(a=a, t=esc(t))
                  for t, a in post['toc'])

    related = ''.join(
        '<a class="card" href="/treatments/{s}/"><div class="card-body">'
        '<h3>{n}</h3><p>{d}</p><span class="link-arrow">Read more {ar}</span></div></a>'
        .format(s=s, n=esc(TREATMENT_BY_SLUG[s]['name']),
                d=esc(TREATMENT_BY_SLUG[s]['nav_desc']), ar=icon('arrow', 15))
        for s in post['related_treatments'])

    more = ''.join(post_card(p) for p in POSTS if p['slug'] != post['slug'])[:99999]

    body = '''
<article>
<section class="pagehead">
  <div class="wrap">
    {crumbs}
    <div style="max-width:820px;">
      <span class="pill {pc}">{cat}</span>
      <h1 style="margin-top:18px;">{title}</h1>
      <div class="post-meta" style="margin-top:22px;color:#8FAEBF;">
        <span>{date}</span><span class="dot">&middot;</span><span>{rt}</span>
        <span class="dot">&middot;</span><span>{author}</span>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="article-grid">
      <div>
        <p class="article-lede">{lede}</p>
        <div class="article-body" style="margin-top:1.6em;">{body}</div>
        <div class="byline" style="margin-top:48px;">
          <span class="av">{initials}</span>
          <span><span class="n">{author}</span><br><span class="r">{role}</span></span>
        </div>
      </div>
      <aside>
        <div class="toc">
          <p class="h">On this page</p>
          <ol>{toc}</ol>
        </div>
        <div class="callout orange" style="margin-top:24px;">
          <h3>Talk to someone today</h3>
          <p>No referral needed. Call {phone} or request a callback.</p>
          <div class="btn-row" style="margin-top:16px;">
            <a class="btn btn-blue" href="/contact/">Request a callback</a>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>
</article>

<section class="section band-tint">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Related treatment</span>
      <h2>Programmes mentioned in this article</h2>
    </div>
    <div class="grid-3">{related}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head-split">
      <div class="sec-head"><span class="eyebrow">Keep reading</span><h2>More from the blog</h2></div>
      <a class="btn btn-outline" href="/blog/">All articles</a>
    </div>
    <div class="grid-3">{more}</div>
  </div>
</section>

<section class="section-sm">
  <div class="wrap">{emergency}</div>
</section>

{cta}
'''.format(
        crumbs=crumbs(crumb_items), pc=post.get('category_class', ''),
        cat=esc(post['category']), title=esc(post['title']),
        date=fmt_date(post['date']), rt=esc(post['read_time']),
        author=esc(author['name']), role=esc(author['role']), initials=esc(author['initials']),
        lede=esc(post['lede']), body=''.join(post['body']), toc=toc,
        phone=SITE['main_phone'], related=related, more=more,
        emergency=emergency_note(),
        cta=cta_band('Ready when you are.',
                     'Same day assessment across five Lower Mainland clinics.'),
    )

    canonical = SITE['base_url'] + path
    write(path, render(
        path, post.get('seo_title', post['title']), post['meta_desc'], body, active='blog',
        ogtype='article', crumb_items=crumb_items,
        head_extra='<meta property="article:published_time" content="{0}">'.format(post['date']),
        extra_nodes=[{
            "@type": "BlogPosting",
            "@id": canonical + '#article',
            "headline": post['title'],
            "description": post['meta_desc'],
            "url": canonical,
            "datePublished": post['date'],
            "dateModified": post.get('updated', post['date']),
            "inLanguage": "en-CA",
            "author": {"@type": "Organization", "name": author['name'],
                       "@id": SITE['base_url'] + '/#organization'},
            "publisher": {"@id": SITE['base_url'] + '/#organization'},
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
            "articleSection": post['category'],
        }]))


def steps_grid(steps, columns=4):
    cls = 'steps steps-{0}'.format(columns) if columns != 4 else 'steps'
    inner = ''.join('<div class="step"><h3>{t}</h3><p>{d}</p></div>'.format(t=esc(t), d=esc(d))
                    for t, d in steps)
    return '<div class="{c}">{i}</div>'.format(c=cls, i=inner)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def clean():
    """Remove previously generated directories so deleted pages do not linger."""
    for name in ('treatments', 'locations', 'blog', 'what-to-expect', 'for-pharmacies',
                 'contact', 'privacy', 'terms', 'accessibility'):
        target = os.path.join(ROOT, name)
        if os.path.isdir(target):
            shutil.rmtree(target)


def main():
    # When this file runs as a script it is registered as __main__, so a plain
    # `import build` inside pages_more would load a second, separate copy with
    # its own WRITTEN list. Alias it first so both names resolve to one module.
    sys.modules.setdefault('build', sys.modules[__name__])
    import pages_more
    from home import build_home

    clean()

    build_home()

    build_treatments_index()
    for t in TREATMENTS:
        build_treatment(t)

    build_locations_index()
    for l in LOCATIONS:
        build_location(l)

    build_blog_index()
    for p in POSTS:
        build_post(p)

    pages_more.build_what_to_expect()
    pages_more.build_pharmacies()
    pages_more.build_contact()
    pages_more.build_privacy()
    pages_more.build_terms()
    pages_more.build_accessibility()
    pages_more.build_404()

    pages_more.build_sitemap(WRITTEN)

    print('Built {0} files:'.format(len(WRITTEN)))
    for p in sorted(WRITTEN):
        print('  ' + p)


if __name__ == '__main__':
    main()
