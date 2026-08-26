# -*- coding: utf-8 -*-
"""Post build checks. Run after tools/build.py.

    python tools/check.py

Verifies internal links resolve, JSON-LD parses, required meta tags exist,
headings start at a single h1, images have alt text, and no em dashes have
crept into the copy. Exits non zero on failure so it can gate a deploy.
"""

from __future__ import print_function

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {'.git', 'assets', 'tools', 'content', '__pycache__'}

sys.path.insert(0, ROOT)
try:
    from content.data import SITE
    BASE_PATH = SITE.get('base_path', '').rstrip('/')
    PREVIEW = SITE.get('preview', False)
except ImportError:
    BASE_PATH, PREVIEW = '', False

errors = []
warnings = []


def html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith('.html'):
                yield os.path.join(dirpath, name)


def url_for(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
    if rel == 'index.html':
        return '/'
    if rel.endswith('/index.html'):
        return '/' + rel[:-len('index.html')]
    return '/' + rel


def resolves(href):
    """Does an internal href correspond to a file we generated?"""
    href = href.split('#')[0].split('?')[0]
    # Built pages carry the deployment sub path; strip it before resolving.
    if BASE_PATH and (href == BASE_PATH or href.startswith(BASE_PATH + '/')):
        href = href[len(BASE_PATH):] or '/'
    if not href:
        return True
    if href == '/':
        return os.path.isfile(os.path.join(ROOT, 'index.html'))
    local = href.strip('/').replace('/', os.sep)
    if os.path.isfile(os.path.join(ROOT, local)):
        return True
    if os.path.isfile(os.path.join(ROOT, local, 'index.html')):
        return True
    return False


def main():
    pages = sorted(html_files())
    if not pages:
        errors.append('No HTML files found. Run tools/build.py first.')

    for path in pages:
        url = url_for(path)
        fh = open(path, encoding='utf-8')
        html = fh.read()
        fh.close()

        # --- typography ---
        for ch, label in ((u'—', 'em dash'), (u'–', 'en dash')):
            if ch in html:
                errors.append('{0}: contains {1}'.format(url, label))

        # --- required head elements ---
        for pattern, label in (
            (r'<title>[^<]{10,}</title>', 'title'),
            (r'<meta name="description" content="[^"]{50,}"', 'meta description'),
            (r'<link rel="canonical"', 'canonical'),
            (r'<meta property="og:title"', 'og:title'),
            (r'<meta name="robots"', 'robots'),
            (r'<meta name="viewport"', 'viewport'),
            (r'<html lang="', 'lang attribute'),
        ):
            if not re.search(pattern, html):
                errors.append('{0}: missing or too short {1}'.format(url, label))

        # --- title length, a soft SEO limit ---
        m = re.search(r'<title>([^<]+)</title>', html)
        if m and len(m.group(1)) > 65:
            warnings.append('{0}: title is {1} chars, over the 65 char guideline'
                            .format(url, len(m.group(1))))
        m = re.search(r'<meta name="description" content="([^"]+)"', html)
        if m and len(m.group(1)) > 165:
            warnings.append('{0}: meta description is {1} chars, over the 165 char guideline'
                            .format(url, len(m.group(1))))

        # --- exactly one h1 ---
        h1s = re.findall(r'<h1[ >]', html)
        if len(h1s) != 1:
            errors.append('{0}: found {1} h1 elements, expected exactly 1'.format(url, len(h1s)))

        # --- JSON-LD parses ---
        for block in re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                data = json.loads(block.replace('<\\/', '</'))
            except ValueError as exc:
                errors.append('{0}: JSON-LD does not parse ({1})'.format(url, exc))
                continue
            if '@graph' not in data:
                errors.append('{0}: JSON-LD has no @graph'.format(url))

        # --- images have alt text ---
        for tag in re.findall(r'<img [^>]*>', html):
            if 'alt=' not in tag:
                errors.append('{0}: img without alt attribute'.format(url))

        # --- iframes have a title ---
        for tag in re.findall(r'<iframe [^>]*>', html):
            if 'title=' not in tag:
                errors.append('{0}: iframe without title attribute'.format(url))

        # --- internal links resolve ---
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#', 'data:')):
                continue
            if not resolves(href):
                errors.append('{0}: broken internal link to {1}'.format(url, href))

        # --- external links carry rel=noopener when targeting a new tab ---
        for tag in re.findall(r'<a [^>]*target="_blank"[^>]*>', html):
            if 'noopener' not in tag:
                warnings.append('{0}: target=_blank without rel=noopener'.format(url))

    print('Checked {0} pages.'.format(len(pages)))
    for w in warnings:
        print('  WARN  ' + w)
    for e in errors:
        print('  FAIL  ' + e)

    if errors:
        print('\n{0} error(s), {1} warning(s).'.format(len(errors), len(warnings)))
        return 1
    print('\nAll checks passed ({0} warning(s)).'.format(len(warnings)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
