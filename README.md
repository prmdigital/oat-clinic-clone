# OAT Clinic website

Static, multi-page website for OAT Clinic, an opioid agonist treatment provider
with five clinics across British Columbia.

Plain HTML and CSS with a small amount of progressive-enhancement JavaScript.
No frameworks, no npm, no build step for whoever hosts it. Pages are generated
from content files by a Python script and the output is committed, so any static
host can serve the repository as is.

---

## Quick start

Serve the site locally:

```bash
python -m http.server 4321
```

Rebuild after editing anything in `content/`:

```bash
python tools/build.py && python tools/check.py
```

`build.py` needs Python 3.6 or newer and nothing else.

---

## How it fits together

```
content/            What you edit
  data.py             Site settings, clinic locations, hours, footer links
  treatments.py       One entry per treatment page, including its FAQs
  posts.py            Blog posts, newest first
tools/              How it gets built
  build.py            Generator, shared blocks and page renderers. Run this.
  home.py             The homepage, kept separate as the most edited file
  pages_more.py       Remaining pages: what to expect, pharmacies, contact, legal
  shell.py            Head, masthead, drawer, footer, icons, JSON-LD
  check.py            Post-build validation. Run this before deploying.
assets/             Served as is
  css/site.css        Whole design system. Tokens at the top.
  js/site.js          Menu, accordion, form validation, scroll reveal
index.html          Generated. Do not edit by hand.
treatments/ …       Generated. Do not edit by hand.
```

Everything at the repository root except `assets/`, `content/`, `tools/` and this
README is generated output. Editing it directly means losing the change on the
next build.

---

## Common tasks

### Publish a blog post

Add a dict to the **top** of `POSTS` in `content/posts.py` and rebuild. Fields:

| Field | Notes |
| --- | --- |
| `slug` | Becomes `/blog/<slug>/`. Lowercase, hyphens. |
| `title` | The `h1`. |
| `seo_title` | Optional. Used for the `<title>` tag when the headline is long. |
| `lede` | Standfirst paragraph. |
| `date`, `updated` | `YYYY-MM-DD`. Drives display date and Article schema. |
| `category`, `category_class` | Label and pill colour (`''`, `orange`, `sage`). |
| `read_time`, `author` | Author key comes from `AUTHORS`. |
| `meta_desc` | Keep under 165 characters or `check.py` warns. |
| `toc` | `[(label, anchor_id)]`, matching the `id`s in the body. |
| `body` | List of HTML strings. |
| `related_treatments` | Treatment slugs to cross-link. |

### Add or change a clinic

Edit `LOCATIONS` in `content/data.py`. Each entry generates a page, a card on
`/locations/`, footer and navigation entries, and a `MedicalClinic` schema node
with its address, geo coordinates and opening hours.

### Add a treatment page

Add an entry to `TREATMENTS` in `content/treatments.py`. It appears in the
navigation dropdown, the treatments index, the footer, and cross-links from
related pages automatically. `faqs` are rendered as an accordion and emitted as
`FAQPage` structured data.

Two fields drive the page furniture, and both are required:

| Field | What it does |
| --- | --- |
| `facts` | Five `(label, value)` pairs. Becomes the at a glance strip under the hero, which is what most visitors scan before deciding to read. |
| `pullquote` | One sentence, usually the most important safety point. Placed after the second section, where an unbroken text column starts to drag. |

The section rail down the left is generated from `sections`, so anchors and
numbering stay in step automatically. It sticks on desktop, highlights the
section you are reading, and collapses to a contents card below 1024px.

### Change the look

Design tokens are at the top of `assets/css/site.css` under `:root`. Colours,
type, spacing rhythm and radii are all there. Change a token rather than a value
further down the file.

---

## Brand

Sampled directly from `assets/img/oat-clinic-logo.jpg`, the supplied logo.
**These two values are the brand. Do not substitute them.**

| Token | Value | Use |
| --- | --- | --- |
| `--blue` | `#015F9C` | The logo tile. Primary buttons, links, headings on light. |
| `--orange` | `#F47F20` | The bar beneath the wordmark. Accents, primary CTA. |
| `--orange-ink` | `#012A45` | Text placed **on** orange. See the note below. |
| `--orange-deep` | `#A85105` | Orange used **as** small text on light surfaces. |

Every other blue and orange in `site.css` is a tint or shade derived from these.

### Why orange surfaces carry navy text

White on `#F47F20` is **2.66:1**, which fails WCAG AA (4.5:1 needed). Rather
than darken the brand orange, orange surfaces use deep navy text at **5.57:1**.
The brand colour stays exact and the contrast passes.

For the same reason, orange used as small text on the warm paper background is
darkened to `--orange-deep`. The brand orange is still used at full strength for
fills, rules, icons and accents, where contrast rules do not apply.

### Logo files

| File | Use |
| --- | --- |
| `assets/img/oat-clinic-logo.jpg` | Original supplied artwork. |
| `assets/img/logo-96.png` | Blue tile. Masthead and mobile drawer, on light. |
| `assets/img/logo-light.png` | White wordmark on transparent. Footer, on navy. |
| `assets/img/og-default.png` | 1200x630 social share card. |
| `assets/apple-touch-icon.png` | 180x180 iOS home screen icon. |
| `assets/favicon.ico`, `favicon-32.png` | Browser tab icons. |

The blue tile is part of the mark on light surfaces and is never recoloured.
On the navy footer the tile would read as a pasted square, so `logo-light.png`
is used instead: the same wordmark and bar lifted onto transparency straight
from the supplied artwork. Regenerate both with `python tools/make_logos.py`.

---

## Design rules

The homepage is modelled on two reference sites the client chose,
[porchlighthealth.com](https://porchlighthealth.com) and
[affect.com](https://www.affect.com). Both follow the same discipline, and the
site now follows it too.

**One idea per screen.** The hero carries a headline, one line of explanation
and two actions. Nothing else. The callback form is **not** in the hero; it
lives on `/contact/`, which every call to action points at. Putting a five field
form beside the headline was the single largest source of clutter.

**Nine bands, each with one job.** Hero, proof strip, three ways in, treatments,
how it works, locations, pharmacies, blog, closing call to action. If a tenth
band is proposed, something else should leave.

**Say it once.** Before adding copy, grep the built page for the phrase. An
earlier draft said "no referral" four times above the fold, across a utility
bar, a hero badge and the proof strip. The utility bar and the badge were both
removed.

**Three items, not five.** Card rows are threes. The treatment grid is the one
exception, and its sixth cell links to the index rather than adding a sixth
item.

### Illustration

Homepage only, in `tools/illustrations.py`. Places and objects, never
characters or faces. The rules are documented at the top of that file.

The hero background moves. Three blurred blobs drift on long, mismatched
cycles so it never repeats a pose, five clinic pins pulse in sequence, and the
route joining them has dashes that travel. Read together it is reach: five
places, one network, care moving between them.

Everything animates through CSS, so one media query stops all of it, and the
rings scale rather than redraw, which keeps them on the compositor.

Three earlier attempts are recorded so they are not retried. A settling signal
line was too quiet to carry the space. Three solids scattered at the edges
left the middle empty. A dark ground with a still isometric scene looked
composed but had no motion at all.

### Type

| Role | Face | Weight |
| --- | --- | --- |
| Display (`--display`) | Outfit | 600 to 700 |
| Body and UI (`--sans`) | Inter | 400 to 600 |

Outfit is the same family Porch Light uses. There is no serif in the system.
The `--serif` token was removed, so do not reintroduce references to it.

### Motion

Four rules, because the audience often arrives in crisis on a slow device.

1. **Only `opacity` and `transform` are animated.** Both run on the compositor,
   so nothing triggers layout or paint. `tools/check.py` does not enforce this,
   but every `@keyframes` block in `site.css` obeys it.
2. **Nothing above the fold is delayed past ~250ms.** The hero stagger runs
   0.02s to 0.20s. The call button is readable almost immediately.
3. **Everything is off under `prefers-reduced-motion`.** Reveals, staggers, the
   accordion and the view transitions all have reduce branches.
4. **Motion confirms actions, it never gates them.** No entrance animation on a
   phone number, no scroll hijacking, no parallax, no counters, no preloader.

What is implemented:

| Effect | How | Cost |
| --- | --- | --- |
| Page to page crossfade | `@view-transition { navigation: auto }` | 8 lines of CSS |
| Staggered section reveals | `.reveal.stagger` on a container | CSS only, existing observer |
| Hero entrance | Same, with tighter delays | none |
| Accordion height | `interpolate-size` + `::details-content` | CSS only, no JS |
| Masthead settle on scroll | `.is-stuck` class already set by `site.js` | 3 rules |
| Button, card and clinic hovers | Transitions on transform, colour, shadow | already present |

No animation library. No GSAP, no AOS, no Lenis. Adding one would cost more
kilobytes than the entire current stylesheet.

To add a staggered section, put `reveal stagger` on the container and leave the
children unmarked. The container drives them, up to six delays, then flat.

### Shape and surface

White ground, `--paper-2` for alternating bands, deep navy for dark bands.
Radius is `8px` on buttons, `16px` on cards, pill on chips. Shadows are soft and
blue tinted, never grey.

## House style

- **No em dashes or en dashes** in any copy. `check.py` fails the build if one
  appears. Use commas, full stops, or a rewrite.
- Clinical content is written for patients, not clinicians, and states drawbacks
  honestly rather than only benefits.
- Nothing on the site claims an outcome or gives individual medical advice. The
  disclaimer in the footer is not optional.

---

## Before deploying

`python tools/check.py` must pass. It verifies:

- every internal link resolves to a real generated file
- every page has a title, meta description, canonical URL, OG tags and `lang`
- exactly one `h1` per page
- all JSON-LD parses and carries an `@graph`
- images have `alt`, iframes have `title`
- no em dashes or en dashes anywhere
- titles are under 65 characters and meta descriptions under 165

It exits non zero on failure, so it works as a CI gate.

---

## Deployment

The repository root is the document root. No build step is needed on the host.

- **GitHub Pages.** Settings, Pages, deploy from `main` branch, `/` root.
- **Netlify or Vercel.** No build command, publish directory `.`.
- **Any web server.** Serve the repository root. Ensure `404.html` is wired to
  the 404 handler.

Asset URLs carry a content hash (`site.css?v=897fb285`), so stylesheets and
scripts can be cached indefinitely and still update on deploy.

---

## Known gaps

These need a decision or information from the clinic before launch.

1. **`base_url` is a placeholder.** `content/data.py` sets
   `https://www.oatclinic.ca`. It drives canonical URLs, Open Graph tags, the
   sitemap and all structured data. Set the real origin before going live.
2. **The callback form has no endpoint.** Until `data-endpoint` is set on the
   form, it validates input and then tells the visitor to phone instead. It
   never silently pretends a request was received.
3. **Three clinics have no direct phone number.** Chilliwack, Surrey and Burnaby
   currently fall back to the Vancouver line. Add real numbers to `LOCATIONS`.
4. **Location details are drafted, not confirmed.** Transit routes, parking,
   accessibility notes and clinic days for the smaller sites need checking by
   someone who works there.
5. **Geo coordinates are approximate.** Fine for schema, worth replacing with
   exact values from the Google Business Profile.
6. **Blog posts are attributed to the clinical team, not a named physician.**
   Named authorship with credentials is a meaningful E-E-A-T signal for health
   content and is worth adding.
7. **The logo is a 200x200 JPG.** It is sharp at the sizes used, but a vector
   original (SVG, AI or EPS) would be better for print and for large displays.
   The social card and icons are all derived from this one raster file.
