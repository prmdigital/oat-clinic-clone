# -*- coding: utf-8 -*-
"""The homepage.

Deliberately restrained. The reference sites the client picked share one
discipline: a single idea per screen, a short headline, one line of
explanation, two actions, and nothing else competing for attention.

So the callback form is not in the hero. It lives on /contact/, which every
call to action points at. The homepage's job is to route people, not to
capture them in the first viewport.

Section count is the thing to guard. Nine bands, each with one job:
  hero, proof, three ways in, treatments, how it works, locations,
  pharmacies, blog, closing call to action.
"""


def build_home():
    from build import write, cta_band, post_card
    from shell import render, icon, esc, organization_node, _clinic_node
    from content.data import SITE, LOCATIONS
    from content.treatments import TREATMENTS
    from content.posts import POSTS

    # ---------------------------------------------------------------- hero
    hero = '''
<section class="hero">
  <div class="wrap reveal stagger">
    <h1>Treatment that starts <span class="hl">today</span>, not next month.</h1>
    <p class="lede">Methadone, Suboxone and substance use care, in person or by
      telemedicine.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="{ph}">{phi} Call {phone}</a>
      <a class="btn btn-outline" href="/contact/">Request a callback</a>
    </div>
    <p class="hero-note">Already a patient? <a href="/locations/">Find your clinic</a></p>
  </div>
</section>'''.format(ph=SITE['main_phone_href'], phi=icon('phone', 17), phone=SITE['main_phone'])

    # --------------------------------------------------------------- proof
    proof_items = [
        ('shield', 'No referral required'),
        ('clock', 'Same day assessment'),
        ('video', 'Telemedicine across BC'),
        ('check', 'Covered by MSP'),
    ]
    proof = '<div class="proof"><div class="wrap">{0}</div></div>'.format(
        ''.join('<div class="proof-item">{ic}<span>{t}</span></div>'.format(
            ic=icon(k, 19), t=esc(t)) for k, t in proof_items))

    # ------------------------------------------------------- three ways in
    ways = [
        ('clinic', False, 'Walk into a clinic',
         'Five locations across the Lower Mainland. Assessment and, where appropriate, '
         'a first dose the same day.',
         '/locations/', 'Find your clinic'),
        ('video', True, 'Start by telemedicine',
         'See a physician from home or anywhere private. No travel, and no waiting room.',
         '/what-to-expect/', 'How it works'),
        ('pharmacy', False, 'Ask at your pharmacy',
         'Pharmacies running WinRx can request an appointment at the counter. You keep '
         'your pharmacy.',
         '/for-pharmacies/', 'For pharmacy teams'),
    ]
    ways_html = ''.join('''
      <div class="soft{acc}">
        <span class="ico">{ic}</span>
        <h3>{t}</h3>
        <p>{d}</p>
        <a class="link-arrow" href="{h}">{cta} {ar}</a>
      </div>'''.format(acc=' accent' if accent else '', ic=icon(k, 26, 1.6),
                       t=esc(t), d=esc(d), h=h, cta=esc(cta), ar=icon('arrow', 15))
        for k, accent, t, d, h, cta in ways)

    three_ways = '''
<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <h2>Three ways to begin</h2>
      <p class="lede" style="margin-inline:auto;">The route in matters less than taking one.
        All three reach the same clinical team.</p>
    </div>
    <div class="grid-3 reveal stagger">{ways}</div>
  </div>
</section>'''.format(ways=ways_html)

    # ---------------------------------------------------------- treatments
    tiles = ''.join('''
      <a class="tile" href="/treatments/{s}/">
        <h3>{n}</h3>
        <p>{d}</p>
        <span class="go">Read more {ar}</span>
      </a>'''.format(s=t['slug'], n=esc(t['name']), d=esc(t['nav_desc']),
                     ar=icon('arrow', 15)) for t in TREATMENTS)
    tiles += '''
      <a class="tile all" href="/treatments/">
        <h3>All treatment programmes</h3>
        <p>How each one works, what the first weeks are like, and what it costs in BC.</p>
        <span class="go">See all five {ar}</span>
      </a>'''.format(ar=icon('arrow', 15))

    treatments = '''
<section class="section band-tint">
  <div class="wrap">
    <div class="sec-head center reveal">
      <h2>What we treat</h2>
      <p class="lede" style="margin-inline:auto;">Opioids are rarely the whole picture,
        so our assessment covers everything you use.</p>
    </div>
    <div class="tiles reveal stagger">{tiles}</div>
  </div>
</section>'''.format(tiles=tiles)

    # -------------------------------------------------------- how it works
    steps = [
        ('Reach out', 'Call us, request a callback, or ask at a WinRx pharmacy. '
                      'No referral and no family doctor needed.'),
        ('Get assessed', 'A physician reviews your history and what you want from '
                         'treatment. Usually about ninety minutes.'),
        ('Start the same day', 'Where it is clinically appropriate, treatment begins '
                               'that day, with a plan built around your life.'),
    ]
    steps_html = ''.join(
        '<div class="step"><h3>{t}</h3><p>{d}</p></div>'.format(t=esc(t), d=esc(d))
        for t, d in steps)

    how = '''
<section class="section">
  <div class="wrap">
    <div class="sec-head center reveal">
      <h2>How it works</h2>
    </div>
    <div class="steps steps-3 reveal stagger">{steps}</div>
    <div class="btn-row reveal" style="justify-content:center;margin-top:34px;">
      <a class="btn btn-outline" href="/what-to-expect/">Read the full walkthrough</a>
    </div>
  </div>
</section>'''.format(steps=steps_html)

    # ----------------------------------------------------------- locations
    places = ''.join('''
      <a class="place" href="/locations/{s}/">
        <span class="pin">{ic}</span>
        <span class="txt"><b>{c}</b><span>{st}</span></span>
        <span class="go">{ar}</span>
      </a>'''.format(s=l['slug'], ic=icon('pin', 19), c=esc(l['city']),
                     st=esc(l['street']), ar=icon('arrow', 17))
        for l in LOCATIONS)

    locations = '''
<section class="section band-tint">
  <div class="wrap">
    <div class="grid-2" style="align-items:center;gap:clamp(32px,5vw,72px);">
      <div class="reveal">
        <h2>Five clinics across the Lower Mainland</h2>
        <p class="lede" style="margin-top:18px;">Every location offers assessment,
          prescribing and follow up. Your medication can be dispensed at whichever
          pharmacy suits you.</p>
        <p class="lede" style="margin-top:18px;">Choose a clinic for its address,
          hours, parking and directions.</p>
      </div>
      <div class="places reveal stagger">{places}</div>
    </div>
  </div>
</section>'''.format(places=places)

    # ---------------------------------------------------------- pharmacies
    pharmacies = '''
<section class="section band-dark">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <h2>Pharmacies: request appointments inside WinRx</h2>
        <p class="lede" style="margin-top:18px;">Book telemedicine assessments, collect
          signatures and track requests without faxes or phone tag. Your patient keeps
          dispensing with you.</p>
        <div class="btn-row" style="margin-top:30px;">
          <a class="btn btn-primary" href="/for-pharmacies/">See how it works</a>
        </div>
      </div>
      <ol class="split-list reveal stagger">
        <li><b>Update WinRx</b> so the OAT telemedicine option appears on the patient profile.</li>
        <li><b>Book from the profile</b> and choose telemedicine or life tracking.</li>
        <li><b>Complete the OAT bundle</b> with signatures by link or signed on screen.</li>
        <li><b>Track and reorder</b> request status and screening supplies in one place.</li>
      </ol>
    </div>
  </div>
</section>'''

    # ---------------------------------------------------------------- blog
    blog = '''
<section class="section">
  <div class="wrap">
    <div class="sec-head-split reveal">
      <div class="sec-head">
        <h2>Plain answers, from our physicians</h2>
        <p class="lede">The questions that most often keep people out of treatment.</p>
      </div>
      <a class="btn btn-outline" href="/blog/">Read the blog</a>
    </div>
    <div class="grid-3 reveal stagger">{posts}</div>
  </div>
</section>'''.format(posts=''.join(post_card(p) for p in POSTS[:3]))

    # ------------------------------------------------------------- closing
    closing = cta_band('You have already done the hardest part by looking.',
                       'Call now or request a callback. Treatment can start today.')

    body = (hero + proof + three_ways + treatments + how + locations
            + pharmacies + blog + closing)

    nodes = [_clinic_node(l) for l in LOCATIONS]
    nodes.append({
        "@type": "WebSite",
        "@id": SITE['base_url'] + '/#website',
        "url": SITE['base_url'] + '/',
        "name": SITE['name'],
        "publisher": {"@id": SITE['base_url'] + '/#organization'},
        "inLanguage": "en-CA",
    })

    write('/', render('/', 'Opioid Agonist Treatment in BC | OAT Clinic',
                      SITE['description'], body, active='home', extra_nodes=nodes))
