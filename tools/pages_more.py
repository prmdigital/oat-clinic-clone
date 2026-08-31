# -*- coding: utf-8 -*-
"""The remaining pages: what to expect, pharmacies, contact, legal, 404.

Helpers are imported from build inside each function rather than at module
level, because build imports this module. Python caches modules, so by the
time any of these run, build is fully initialised.
"""

import os
import datetime


# --------------------------------------------------------------------------- #
# What to expect
# --------------------------------------------------------------------------- #

def build_what_to_expect():
    from build import (write, pagehead, keypoints_block, faq_block, cta_band, steps_grid)
    from shell import render, crumbs, esc, emergency_note, faq_node
    from content.data import SITE

    path = '/what-to-expect/'
    crumb_items = [('Home', '/'), ('What to expect', None)]

    faqs = [
        ("Do I need a referral or a family doctor?",
         ["<p>No. You can contact us directly, and most of our patients do not have a family "
          "doctor. Walk in, call, or ask at a WinRx pharmacy.</p>"]),
        ("What if I have no identification or no MSP coverage?",
         ["<p>Come anyway. We can begin an assessment without identification and help you sort "
          "out coverage afterwards. Missing paperwork is a problem to solve, not a reason to "
          "turn you away.</p>",
          "<p>If you have a BC Services Card, bring it. If you have lost it, we can usually "
          "look up your coverage with your name and date of birth.</p>"]),
        ("How long does the first appointment take?",
         ["<p>Plan for ninety minutes to two hours. There is a full history to take, a physical "
          "assessment, a urine drug screen and a conversation about which pharmacy you want to "
          "use. Arriving before 4:00 PM gives the best chance of finishing the same day.</p>"]),
        ("Will I be tested for drugs, and what happens to the result?",
         ["<p>Yes. A urine drug screen is part of the assessment and part of ongoing care. Its "
          "purpose is clinical. It tells us what is actually in the supply you have been using, "
          "which shapes both your dose and your safety plan.</p>",
          "<p>Results are not shared with police, employers or family. An unexpected result is a "
          "reason for a conversation, not for discharge.</p>"]),
        ("Can I keep using the pharmacy I already go to?",
         ["<p>In almost every case, yes. Tell us which pharmacy you prefer and we will send the "
          "prescription there. Continuity with a pharmacist who already knows you is genuinely "
          "valuable and we would rather not disrupt it.</p>"]),
        ("What happens if I am still using while in treatment?",
         ["<p>You stay in treatment. Continued use tells us the current plan needs adjusting, "
          "which is clinical information rather than grounds for discharge.</p>",
          "<p>It may affect how quickly take home doses are offered, because those decisions are "
          "about safety. It does not affect whether you are welcome here.</p>"]),
        ("Is telemedicine as good as being seen in person?",
         ["<p>For most follow up appointments, yes, and it removes the travel entirely. For a "
          "first assessment it depends on your situation, and there are cases where we will ask "
          "you to come in, particularly where a physical examination matters.</p>",
          "<p>You need somewhere private and a phone or a computer. That is all.</p>"]),
        ("What does any of this cost?",
         ["<p>Appointments with our physicians are billed to the Medical Services Plan, so there "
          "is no fee to see us if you have active MSP coverage. Methadone and Suboxone are "
          "covered by BC PharmaCare for most residents, and people receiving income assistance "
          "or disability assistance are generally covered in full including dispensing fees.</p>",
          "<p>If you have no coverage at all, tell us at the first appointment. It can almost "
          "always be arranged, and it should never be the reason you do not start.</p>"]),
    ]

    steps = [
        ("Reach out", "Call, request a callback, walk into the Vancouver clinic, or ask your "
                      "WinRx pharmacy to send a request. Nothing else is required to begin."),
        ("Assessment", "A physician takes a full history, examines you, and runs a urine drug "
                       "screen. You will be asked what you want from treatment, and the answer "
                       "does not have to be abstinence."),
        ("A plan you agree with", "Which medication, what starting dose, which pharmacy, and how "
                                  "often we see you. You are part of this decision rather than "
                                  "the subject of it."),
        ("First dose", "Where clinically appropriate, the same day, taken under observation at "
                       "your pharmacy. With Suboxone the timing needs more planning."),
        ("Finding the right dose", "The first two to four weeks are about adjustment. Expect "
                                   "frequent contact, and expect the early days to be harder "
                                   "than the later ones."),
        ("Settling in", "As your dose stabilises, appointments space out and take home doses "
                        "begin. Treatment stops being the centre of your week."),
    ]

    parts = []
    parts.append(pagehead(
        crumbs(crumb_items),
        'What to expect',
        'What actually happens from the moment you get in touch to the point where treatment '
        'settles into the background of your life. No jargon, and no pretending that the first '
        'fortnight is easy.'))

    parts.append('<section class="section-sm"><div class="wrap" style="max-width:860px;">')
    parts.append(keypoints_block([
        'No referral, no family doctor and no waiting list',
        'A first assessment takes roughly ninety minutes to two hours',
        'Treatment can often begin the same day you make contact',
        'Appointments are billed to MSP, so there is no fee to see us',
        'You keep the dispensing pharmacy you already use',
    ], heading='The short version'))
    parts.append('</div></section>')

    parts.append('<section class="section" style="padding-top:0;"><div class="wrap">'
                 '<div class="sec-head"><span class="eyebrow">The process</span>'
                 '<h2>Six stages, from first call to steady</h2>'
                 '<p class="lede">Timelines vary between people. The shape rarely does.</p></div>')
    parts.append(steps_grid(steps, columns=3))
    parts.append('</div></section>')

    parts.append('<section class="section band-tint"><div class="wrap">'
                 '<div class="grid-2" style="align-items:start;">'
                 '<div class="prose"><h2>What to bring</h2><ul>'
                 '<li>Photo identification and your BC Services Card, if you have them</li>'
                 '<li>The name and address of the pharmacy you would like to use</li>'
                 '<li>A list of any other medications you take, including anything from a walk '
                 'in clinic</li>'
                 '<li>Whatever you know about your treatment history, even roughly</li>'
                 '</ul><p>If you have none of this, come anyway. We would rather start from an '
                 'incomplete picture than not start.</p></div>'
                 '<div class="prose"><h2>What we will ask you</h2><ul>'
                 '<li>What you are using, how much, and how you take it</li>'
                 '<li>What else you use, including alcohol, benzodiazepines and stimulants</li>'
                 '<li>Any overdoses, and whether you usually use alone</li>'
                 '<li>Your physical and mental health history</li>'
                 '<li>What you want treatment to do for you</li>'
                 '</ul><p>The honest answer is always the useful one. We are working out a safe '
                 'dose, and an answer shaped to please us produces a plan built on the wrong '
                 'information.</p></div>'
                 '</div></div></section>')

    parts.append('<section class="section"><div class="wrap"><div class="split">'
                 '<div><span class="eyebrow">Telemedicine</span>'
                 '<h2>When you cannot get to a clinic</h2>'
                 '<p class="lede" style="margin-top:16px;">Telemedicine covers most of what an '
                 'in person appointment covers, and for follow up it is often better, because it '
                 'does not cost you half a day.</p>'
                 '<div class="prose" style="margin-top:20px;">'
                 '<p>You need a phone or a computer and somewhere private. That can be your home, '
                 'a private room at your pharmacy, or a friend flat. A physician assesses you the '
                 'same way, and the prescription goes directly to your pharmacy.</p>'
                 '<p>There are limits. A first assessment sometimes needs a physical examination, '
                 'and some situations are safer handled in person. We will tell you plainly if '
                 'yours is one of them.</p></div></div><div>')
    parts.append(keypoints_block([
        'Somewhere private, and a phone or a computer',
        'Assessed by the same physicians who work in our clinics',
        'Prescriptions sent straight to your pharmacy',
        'Available across British Columbia, well beyond our five clinic towns',
        'Follow up appointments without the travel',
    ], heading='What telemedicine needs'))
    parts.append('</div></div></div></section>')

    parts.append(faq_block(faqs, heading='Before your first appointment',
                           eyebrow='Common questions',
                           intro='The questions we are asked most often before someone comes in.'))
    parts.append('<section class="section-sm"><div class="wrap">' + emergency_note()
                 + '</div></section>')
    parts.append(cta_band('Still deciding? That is completely fine.',
                          'Call and ask questions. A phone call commits you to nothing.'))

    write(path, render(
        path, 'What to Expect',
        'What happens at your first OAT Clinic appointment in British Columbia: assessment, '
        'drug screening, choosing a medication, your first dose, and finding a stable dose.',
        ''.join(parts), active='what-to-expect', crumb_items=crumb_items,
        extra_nodes=[faq_node(faqs, SITE['base_url'] + path)]))


# --------------------------------------------------------------------------- #
# For pharmacies
# --------------------------------------------------------------------------- #

def build_pharmacies():
    from build import (write, pagehead, keypoints_block, faq_block, cta_band)
    from shell import render, crumbs, esc, icon, faq_node
    from content.data import SITE

    path = '/for-pharmacies/'
    crumb_items = [('Home', '/'), ('For pharmacies', None)]

    faqs = [
        ("Which version of WinRx do we need?",
         ["<p>The OAT telemedicine appointment option appears once WinRx is updated to a current "
          "release. If you cannot see it on the patient profile, an update is almost always the "
          "reason. Contact our support line and we will confirm which build you need.</p>"]),
        ("Does the patient have to change pharmacy?",
         ["<p>No, and that is rather the point. The patient keeps dispensing with you. We handle "
          "the assessment and the prescribing, and the prescription comes back to your "
          "pharmacy.</p>"]),
        ("How quickly are requests picked up?",
         ["<p>Requests submitted during clinic hours are generally reviewed the same business "
          "day. Anything submitted after hours or at a weekend is reviewed the next business "
          "day.</p>",
          "<p>If a patient is in front of you and the situation is urgent, phone us rather than "
          "submitting a request and waiting. A phone call is faster.</p>"]),
        ("What does the OAT bundle include?",
         ["<p>Consent forms, the treatment agreement and the information needed to begin. "
          "Signatures can be collected by sending the patient a link, by opening the forms "
          "directly, or by signing on screen at the counter, whichever suits the moment.</p>"]),
        ("Can we order urine drug screen supplies through the same workflow?",
         ["<p>Yes. Cups can be ordered from the same screen you use to track request status, so "
          "it does not become a separate process to remember.</p>"]),
        ("What if the patient has no MSP coverage or no identification?",
         ["<p>Submit the request anyway and note it. Coverage gaps are common and are usually "
          "solvable, but only if we know about them early enough to do something.</p>"]),
        ("Who do we contact when something does not work?",
         ["<p>Call our main line at {phone} and ask for pharmacy support. Please have the "
          "pharmacy name, your WinRx version and the patient reference to hand, since it makes "
          "the call considerably shorter.</p>".format(phone=SITE['main_phone'])]),
    ]

    steps = [
        ('Update WinRx', 'Move to a current release so the OAT telemedicine appointment option '
                         'appears on the patient profile.'),
        ('Book from the profile', 'Open the patient record and choose telemedicine or life '
                                  'tracking. No fax, no separate portal, no phone tag.'),
        ('Complete the OAT bundle', 'Collect consent and agreement signatures by link, by direct '
                                    'opening, or signed on screen at the counter.'),
        ('Track and reorder', 'Follow request status and order urine drug screen supplies from '
                              'the same workflow.'),
    ]
    steps_html = ''.join(
        '<li><b>{t}.</b> {d}</li>'.format(t=esc(t), d=esc(d)) for t, d in steps)

    parts = []
    parts.append(pagehead(
        crumbs(crumb_items),
        'For pharmacy teams',
        'A pharmacy counter is often the first place someone raises opioid treatment, with a '
        'pharmacist they already trust. Requesting an OAT telemedicine appointment from inside '
        'WinRx keeps that conversation moving instead of ending it with a phone number.',
        aside='<div class="btn-row">'
              '<a class="btn btn-primary" href="' + SITE['main_phone_href'] + '">'
              + icon('phone', 17) + ' Pharmacy support</a>'
              '<a class="btn btn-ghost" href="/contact/">Contact the clinic</a></div>'))

    parts.append('<section class="section-sm"><div class="wrap" style="max-width:860px;">')
    parts.append(keypoints_block([
        'Request telemedicine OAT appointments from the patient profile in WinRx',
        'The patient keeps dispensing with you, so you do not lose the relationship',
        'Signatures collected by link, direct opening, or signed on screen',
        'Request status and urine drug screen ordering in one workflow',
        'Requests submitted in clinic hours are generally reviewed the same day',
    ], heading='What this gives your pharmacy'))
    parts.append('</div></section>')

    parts.append('<section class="section band-dark" style="margin-top:0;"><div class="wrap">'
                 '<div class="split"><div>'
                 '<span class="eyebrow on-dark">The workflow</span>'
                 '<h2>Four steps, inside software you already run</h2>'
                 '<p class="lede" style="margin-top:16px;">There is no separate portal to learn '
                 'and no credentials for your team to keep track of. The OAT request sits on the '
                 'patient profile alongside everything else.</p></div>'
                 '<ol class="split-list">' + steps_html + '</ol>'
                 '</div></div></section>')

    parts.append('<section class="section"><div class="wrap">'
                 '<div class="sec-head"><span class="eyebrow">Why it matters</span>'
                 '<h2>The referral that does not survive the walk home</h2></div>'
                 '<div class="grid-2" style="align-items:start;">'
                 '<div class="prose"><p>Willingness to start treatment tends to arrive in narrow '
                 'windows. Someone raises it at the counter on a Tuesday afternoon, is handed a '
                 'phone number, and the window has closed by the time they get home.</p>'
                 '<p>Every step between that moment and an assessment loses people. A request '
                 'submitted while the patient is still standing in front of you removes most of '
                 'those steps.</p></div>'
                 '<div class="prose"><p>It also keeps care connected. We prescribe, you dispense, '
                 'and you keep the daily contact that makes you the person most likely to notice '
                 'when something changes.</p>'
                 '<p>Pharmacists routinely spot missed doses, sedation and interactions before '
                 'anyone else does. If something concerns you about a shared patient, call us. '
                 'We would far rather take that call than not.</p></div>'
                 '</div></div></section>')

    parts.append(faq_block(faqs, heading='Pharmacy questions',
                           eyebrow='Support',
                           intro='If your question is not here, call our main line and ask for '
                                 'pharmacy support.'))
    parts.append(cta_band('Have a patient in front of you right now?',
                          'Call us rather than submitting a request. Urgent situations are faster '
                          'by phone.'))

    write(path, render(
        path, 'For Pharmacies',
        'Request OAT telemedicine appointments from inside WinRx. Workflow, signatures, request '
        'tracking and pharmacy support for British Columbia pharmacies.',
        ''.join(parts), active='for-pharmacies', crumb_items=crumb_items,
        extra_nodes=[faq_node(faqs, SITE['base_url'] + path)]))


# --------------------------------------------------------------------------- #
# Contact
# --------------------------------------------------------------------------- #

def build_contact():
    from build import write, pagehead, callback_form, cta_band
    from shell import render, crumbs, esc, icon, emergency_note, full_address, maps_link
    from content.data import SITE, LOCATIONS, DEFAULT_HOURS

    path = '/contact/'
    crumb_items = [('Home', '/'), ('Contact', None)]

    loc_rows = ''.join(
        '<div class="loc-fact"><div class="k">{c}</div><div class="v">{a}<br>'
        '<a href="{ph}">{p}</a> &middot; <a href="/locations/{s}/">Clinic details</a></div></div>'
        .format(c=esc(l['city']), a=esc(full_address(l)), ph=l['phone_href'],
                p=l['phone'], s=l['slug'])
        for l in LOCATIONS)

    parts = []
    parts.append(pagehead(
        crumbs(crumb_items),
        'Contact us',
        'Call during opening hours and you will speak to someone who can book an assessment. '
        'Use the form and we will call you back the same business day. Both routes reach the '
        'same team.'))

    parts.append('<section class="section"><div class="wrap">'
                 '<div class="grid-2" style="align-items:start;gap:clamp(32px,5vw,72px);">'
                 '<div>'
                 '<span class="eyebrow">By phone</span>'
                 '<h2>Speak to someone now</h2>'
                 '<p class="lede" style="margin-top:16px;">This is the fastest route, and it is '
                 'the one we recommend if you are in a difficult position today.</p>'
                 '<div class="btn-row" style="margin-top:26px;">'
                 '<a class="btn btn-primary" href="' + SITE['main_phone_href'] + '">'
                 + icon('phone', 17) + ' Call ' + SITE['main_phone'] + '</a></div>'
                 '<div class="loc-facts" style="margin-top:36px;">' + loc_rows + '</div>'
                 '<h2 style="margin-top:44px;">Opening hours</h2>'
                 '<table class="hours-table" style="margin-top:20px;max-width:420px;">'
                 + ''.join('<tr><th>{d}</th><td class="{c}">{h}</td></tr>'.format(
                     d=d, c='' if h else 'closed', h=h or 'Closed') for d, h in DEFAULT_HOURS)
                 + '</table>'
                 '<p style="margin-top:16px;font-size:15px;color:var(--ink-3);">'
                 + esc(SITE['hours_note']) + '</p>'
                 '</div>'
                 '<div>' + callback_form(
                     heading='Request a confidential callback',
                     sub='Under a minute to complete. We call back the same business day, from a '
                         'number that does not identify the clinic.')
                 + '</div>'
                 '</div></div></section>')

    parts.append('<section class="section band-tint"><div class="wrap">'
                 '<div class="grid-2" style="align-items:start;">'
                 '<div class="prose"><h2>If you are calling about someone else</h2>'
                 '<p>You are welcome to call. We cannot discuss another adult medical '
                 'information without their consent, but we can explain exactly how the process '
                 'works, what a first visit involves and what to have ready, so that you are '
                 'prepared when they are.</p>'
                 '<p>Our article on <a href="/blog/helping-someone-not-ready-for-treatment/">'
                 'helping someone who is not ready yet</a> covers the ground most of these calls '
                 'end up on.</p></div>'
                 '<div class="prose"><h2>If you are a pharmacy</h2>'
                 '<p>Call our main line and ask for pharmacy support, or read the '
                 '<a href="/for-pharmacies/">pharmacy workflow guide</a> for how OAT telemedicine '
                 'requests work inside WinRx.</p>'
                 '<p>For anything involving a shared patient where you have a clinical concern, '
                 'phone rather than submitting a request. It is faster and we would rather hear '
                 'it directly.</p></div>'
                 '</div></div></section>')

    parts.append('<section class="section-sm"><div class="wrap">' + emergency_note()
                 + '</div></section>')
    parts.append(cta_band('There is no wrong way to get in touch.',
                          'Call, use the form, or walk into the Vancouver clinic during opening '
                          'hours.'))

    write(path, render(
        path, 'Contact Us',
        'Contact OAT Clinic in British Columbia. Phone numbers for all five clinics, opening '
        'hours, and a confidential callback request form.',
        ''.join(parts), active='contact', crumb_items=crumb_items))


# --------------------------------------------------------------------------- #
# Legal and utility pages
# --------------------------------------------------------------------------- #

def _simple_page(path, title, h1, lede, prose, desc, crumb_label, robots='index, follow'):
    from build import write, pagehead, cta_band
    from shell import render, crumbs

    crumb_items = [('Home', '/'), (crumb_label, None)]
    body = pagehead(crumbs(crumb_items), h1, lede)
    body += ('<section class="section"><div class="wrap"><div class="prose">'
             + prose + '</div></div></section>')
    body += cta_band('Questions about any of this?',
                     'Call us and ask. We would rather explain it than have you guess.')
    write(path, render(path, title, desc, body, crumb_items=crumb_items, robots=robots))


def build_privacy():
    from content.data import SITE
    prose = (
        '<p><strong>Last updated {today}.</strong></p>'
        '<h2>What we collect</h2>'
        '<p>When you contact us we collect the information needed to provide care and to reach '
        'you: your name, contact details, the reason for contact, and the clinical information '
        'gathered during assessment and treatment.</p>'
        '<p>This website itself does not set advertising cookies and does not run third party '
        'tracking. Pages that display a map load that map from Google, which means Google '
        'receives your IP address when a location page is viewed. No other third party receives '
        'information about your visit.</p>'
        '<h2>How your health information is protected</h2>'
        '<p>Your clinical record is personal health information under British Columbia law, '
        'including the Personal Information Protection Act and the E-Health Act. It is stored in '
        'a secure clinical record system, access is limited to the people involved in your care, '
        'and access is logged.</p>'
        '<h2>Who we share information with</h2>'
        '<p>We share only what is needed to deliver your care, principally with your dispensing '
        'pharmacy and, where relevant to your treatment, with other clinicians involved in it. '
        'We do not share your information with police, employers, landlords or family members '
        'without your consent.</p>'
        '<p>Narrow legal exceptions apply to every health professional in British Columbia. '
        'These include an immediate risk to your life or someone else, a duty to report a child '
        'at risk of harm, and a valid court order. If any of these ever applies to you, we will '
        'tell you plainly.</p>'
        '<h2>Drug screening results</h2>'
        '<p>Urine drug screen results form part of your clinical record and are used to guide '
        'your treatment. They are not reported to police, to employers or to any other party '
        'outside your care.</p>'
        '<h2>The callback form</h2>'
        '<p>Information submitted through the callback form is used to return your call and to '
        'begin a clinical record if you become a patient. It is not used for marketing and is '
        'not sold or shared with anyone.</p>'
        '<h2>Your rights</h2>'
        '<p>You may request access to your own record, ask for corrections to factual errors, '
        'and ask questions about who has accessed it. Contact us at '
        '<a href="mailto:{email}">{email}</a> or call {phone}.</p>'
        '<h2>Complaints</h2>'
        '<p>If you believe your privacy has not been respected, please raise it with us first. '
        'You may also contact the Office of the Information and Privacy Commissioner for British '
        'Columbia.</p>'
    ).format(today=datetime.date.today().strftime('%d %B %Y'),
             email=SITE['email'], phone=SITE['main_phone'])

    _simple_page('/privacy/', 'Privacy Policy', 'Privacy policy',
                 'How we handle your personal and health information, who can see it, and the '
                 'narrow circumstances in which the law requires us to disclose it.',
                 prose,
                 'How OAT Clinic collects, protects and shares personal health information '
                 'under British Columbia privacy law.',
                 'Privacy policy')


def build_terms():
    from content.data import SITE
    prose = (
        '<p><strong>Last updated {today}.</strong></p>'
        '<h2>This website is not medical advice</h2>'
        '<p>Everything published here is general information intended for education. It is not '
        'a substitute for assessment by a qualified clinician who knows your history, and it '
        'cannot account for your particular circumstances.</p>'
        '<p>Never start, stop or change a prescribed medication based on something you have read '
        'on this website. Doing so can be dangerous, and with some of the medications discussed '
        'here it can be fatal.</p>'
        '<h2>No clinician and patient relationship</h2>'
        '<p>Reading this website, or submitting the callback form, does not create a clinician '
        'and patient relationship. That relationship begins at an assessment.</p>'
        '<h2>Emergencies</h2>'
        '<p>This website and its forms are not monitored continuously and must never be used to '
        'report an emergency. If you are experiencing an overdose, difficulty breathing, chest '
        'pain, seizures or an immediate mental health crisis, call 911.</p>'
        '<h2>Accuracy</h2>'
        '<p>We review clinical content against current British Columbia practice and update it '
        'when guidance changes. Medicine moves, and we cannot guarantee that every page reflects '
        'the most recent guidance at the moment you read it. If something here conflicts with '
        'what your treating clinician tells you, follow your clinician.</p>'
        '<h2>External links</h2>'
        '<p>Where we link to other organisations, we do so because the information is likely to '
        'be useful. We do not control those websites and are not responsible for their content.</p>'
        '<h2>Contact</h2>'
        '<p>Questions about these terms can be sent to <a href="mailto:{email}">{email}</a> or '
        'raised by calling {phone}.</p>'
    ).format(today=datetime.date.today().strftime('%d %B %Y'),
             email=SITE['email'], phone=SITE['main_phone'])

    _simple_page('/terms/', 'Terms of Use', 'Terms of use',
                 'The terms that apply to using this website, including the limits of what '
                 'general health information can do for you.',
                 prose,
                 'Terms of use for the OAT Clinic website, including medical disclaimer and '
                 'emergency guidance.',
                 'Terms of use')


def build_accessibility():
    from content.data import SITE
    prose = (
        '<p><strong>Last updated {today}.</strong></p>'
        '<h2>Our aim</h2>'
        '<p>People reach this website in poor conditions: an old phone, a borrowed laptop, a '
        'library computer, a slow connection, and often while feeling unwell. The site is built '
        'to work in those conditions rather than only in good ones.</p>'
        '<h2>What we have built in</h2>'
        '<ul>'
        '<li>The site works without JavaScript. Menus, forms and answers remain reachable.</li>'
        '<li>Every interactive element can be reached and operated by keyboard, with a visible '
        'focus indicator.</li>'
        '<li>Text and background colours are chosen to meet WCAG 2.1 AA contrast.</li>'
        '<li>Text resizes without breaking layout, and page structure uses real headings and '
        'landmarks for screen readers.</li>'
        '<li>Animation is disabled automatically when your device requests reduced motion.</li>'
        '<li>Pages are lightweight, so they load on a slow connection.</li>'
        '</ul>'
        '<h2>Physical access to our clinics</h2>'
        '<p>All five clinics have step free entry at street or parking level. Details of transit, '
        'parking and access are on each <a href="/locations/">clinic page</a>. If you have an '
        'access need we have not covered, call ahead and we will make arrangements.</p>'
        '<h2>Known limitations</h2>'
        '<p>The embedded maps on our location pages come from Google and we do not control their '
        'accessibility. Every map is accompanied by the full street address in text, and by a '
        'directions link, so no information exists only inside the map.</p>'
        '<h2>Tell us if something does not work</h2>'
        '<p>If any part of this site is difficult to use, we want to hear about it. Email '
        '<a href="mailto:{email}">{email}</a> or call {phone}. Please tell us the page and what '
        'went wrong, and we will fix it and reply.</p>'
    ).format(today=datetime.date.today().strftime('%d %B %Y'),
             email=SITE['email'], phone=SITE['main_phone'])

    _simple_page('/accessibility/', 'Accessibility', 'Accessibility',
                 'What we have done to make this site usable on old devices, slow connections '
                 'and assistive technology, and how to tell us when it falls short.',
                 prose,
                 'Accessibility statement for the OAT Clinic website and clinics, including '
                 'WCAG 2.1 AA commitments and clinic step free access.',
                 'Accessibility')


def build_404():
    from build import write
    from shell import render, icon
    from content.data import SITE

    body = (
        '<section class="pagehead"><div class="wrap">'
        '<div style="max-width:640px;">'
        '<span class="eyebrow on-dark">Error 404</span>'
        '<h1>That page has moved or never existed.</h1>'
        '<p class="lede">Which is frustrating, so here are the places people are usually looking '
        'for.</p>'
        '<div class="btn-row" style="margin-top:30px;">'
        '<a class="btn btn-primary" href="' + SITE['main_phone_href'] + '">'
        + icon('phone', 17) + ' Call ' + SITE['main_phone'] + '</a>'
        '<a class="btn btn-ghost" href="/">Back to the homepage</a>'
        '</div></div></div></section>'
        '<section class="section"><div class="wrap">'
        '<div class="grid-3">'
        '<a class="card" href="/treatments/"><div class="card-body"><h3>Treatments</h3>'
        '<p>Methadone, Suboxone, substance use care, benzodiazepine support and nicotine '
        'cessation.</p></div></a>'
        '<a class="card" href="/locations/"><div class="card-body"><h3>Locations</h3>'
        '<p>Five clinics across British Columbia, with hours, directions and phone '
        'numbers.</p></div></a>'
        '<a class="card" href="/what-to-expect/"><div class="card-body"><h3>What to expect</h3>'
        '<p>What happens at a first appointment, and what the first weeks are actually '
        'like.</p></div></a>'
        '</div></div></section>'
    )
    write('/404.html', render('/404.html', 'Page Not Found',
                              'That page could not be found. Links to treatments, clinic '
                              'locations and how to get in touch.',
                              body, robots='noindex, follow'))


# --------------------------------------------------------------------------- #
# Assets, sitemap, robots
# --------------------------------------------------------------------------- #

def build_sitemap(paths):
    from build import write
    from content.data import SITE

    today = datetime.date.today().isoformat()
    priority = {'/': '1.0'}
    entries = []
    for p in sorted(set(paths)):
        if p.endswith('.html') or p.endswith('.xml') or p.endswith('.txt'):
            continue
        depth = p.strip('/').count('/')
        prio = priority.get(p, '0.8' if depth == 0 else '0.6')
        entries.append(
            '  <url>\n    <loc>{u}</loc>\n    <lastmod>{d}</lastmod>\n'
            '    <changefreq>monthly</changefreq>\n    <priority>{p}</priority>\n  </url>'
            .format(u=SITE['base_url'] + p, d=today, p=prio))

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + '\n'.join(entries) + '\n</urlset>\n')
    write('/sitemap.xml', xml)

    if SITE.get('preview'):
        # A preview deployment must not be crawled. The clinical copy has not
        # been reviewed by the clinic and the domain is not the real one.
        robots = ('# Preview deployment, not for indexing.\n'
                  'User-agent: *\n'
                  'Disallow: /\n')
    else:
        robots = ('User-agent: *\n'
                  'Allow: /\n\n'
                  '# Assistive and AI crawlers are welcome. The clinical pages here are\n'
                  '# written to be quoted accurately.\n\n'
                  'Sitemap: {0}/sitemap.xml\n').format(SITE['base_url'])
    write('/robots.txt', robots)
