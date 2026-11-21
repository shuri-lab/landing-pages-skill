#!/usr/bin/env python3
"""Automatic part of the sales page grade (50 of the 100 points in test/rubric.md).

Usage:
  python3 test/grade.py --page my-sales-page/index.html [--copy my-sales-page/copy.md] [--banned "word1,word2"]
  python3 test/grade.py --page https://your-org.github.io/repo/            (a live URL works too)
  add --json for machine-readable output, --no-browser to skip the Chrome measurements

Needs: Python 3 (standard library). For the fold/scroll/broken-image checks: Node 22+ and Google Chrome
(it runs tools/shoot.mjs). Without them those items are marked MANUAL and Claude/TJ checks them by eye.
Hard fails (the test fails whatever the score): the phone button is below the fold, placeholders on the page.
"""
import argparse, json, os, re, subprocess, sys, urllib.request
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
SHOOT = os.path.join(HERE, '..', 'tools', 'shoot.mjs')


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.buttons, self.imgs, self.text, self._skip, self._btn = [], [], [], 0, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style', 'noscript', 'template'):
            self._skip += 1
        cls = a.get('class', '') or ''
        if tag in ('a', 'button') and re.search(r'\bbtn\b|button', cls):
            self._btn = {'href': a.get('href', ''), 'text': '', 'cls': cls}
        if tag == 'img':
            self.imgs.append(a)

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript', 'template') and self._skip:
            self._skip -= 1
        if tag in ('a', 'button') and self._btn is not None:
            self._btn['text'] = re.sub(r'\s+', ' ', self._btn['text']).strip()
            self.buttons.append(self._btn)
            self._btn = None

    def handle_data(self, data):
        if self._skip:
            return
        self.text.append(data)
        if self._btn is not None:
            self._btn['text'] += data


def load(src):
    if re.match(r'https?://', src):
        return urllib.request.urlopen(src, timeout=30).read().decode('utf-8', 'replace')
    return open(src, encoding='utf-8').read()


def shoot(src, views):
    try:
        out = subprocess.run(['node', SHOOT, src, '--json', '--views', views],
                             capture_output=True, text=True, timeout=240)
        return json.loads(out.stdout[out.stdout.index('{'):])
    except Exception as e:  # node/chrome missing, or page failed
        return {'_error': str(e)[:200]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--page', required=True)
    ap.add_argument('--copy')
    ap.add_argument('--banned', default='steal,regular price,today only,guaranteed income')
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--no-browser', action='store_true')
    a = ap.parse_args()

    html = load(a.page)
    p = Page()
    p.feed(html)
    # The kit's in-page editor adds an "Edit layout" button: ignore it.
    btns = [b for b in p.buttons if b['text'] and not re.search(r'edit layout|save draft|undo', b['text'], re.I)]
    text = re.sub(r'\s+', ' ', ' '.join(p.text))
    items, hard = [], []

    def add(key, name, pts, max_pts, detail, manual=False):
        items.append({'key': key, 'item': name, 'points': pts, 'max': max_pts, 'detail': detail, 'manual': manual})

    # --- Browser measurements -------------------------------------------------------------------
    m = {} if a.no_browser else shoot(a.page, 'mobile,1280,desktop')
    have = bool(m) and '_error' not in m and 'mobile' in m
    if have:
        mob = m['mobile']
        fb = mob.get('first_button') or {}
        ok = bool(fb.get('in_fold'))
        add('fold_button', 'Phone 393x852: first button visible without scrolling', 10 if ok else 0, 10,
            'button bottom %s of 852' % fb.get('bottom'))
        if not ok:
            hard.append('Phone hero button is below the fold (bottom %s of 852)' % fb.get('bottom'))
        h1, hi = mob.get('headline') or {}, mob.get('hero_image') or {}
        pts = (3 if h1.get('in_fold') else 0) + (2 if hi.get('in_fold') else 0)
        add('fold_hero', 'Phone: headline and hero image above the fold', pts, 5,
            'h1 bottom %s, image bottom %s' % (h1.get('bottom'), hi.get('bottom')))
        side = {v: m[v].get('sideways_scroll_px') for v in m if isinstance(m[v], dict)}
        add('sideways', 'No sideways scroll (phone, 1280, 1440)', 5 if all(x == 0 for x in side.values()) else 0, 5,
            'extra px: %s' % side)
        d_ok = [v for v in ('1280', 'desktop') if (m.get(v, {}).get('first_button') or {}).get('in_fold')]
        add('desk_fold', 'Desktop 1280x800 and 1440x900: hero button on the first screen', 5 if len(d_ok) == 2 else (2 if d_ok else 0), 5,
            'in fold at: %s' % (d_ok or 'none'))
        broken = sorted({x for v in m.values() if isinstance(v, dict) for x in v.get('broken_images', [])})
        add('broken', 'No broken images', 3 if not broken else 0, 3, broken[:5] or 'none')
    else:
        why = m.get('_error', 'skipped (--no-browser)') if isinstance(m, dict) else 'skipped'
        for key, name, mx in (('fold_button', 'Phone 393x852: first button visible without scrolling', 10),
                              ('fold_hero', 'Phone: headline and hero image above the fold', 5),
                              ('sideways', 'No sideways scroll', 5),
                              ('desk_fold', 'Desktop hero button on the first screen', 5),
                              ('broken', 'No broken images', 3)):
            add(key, name, 0, mx, 'MANUAL: check in the browser (%s)' % why, manual=True)

    # --- Static checks ------------------------------------------------------------------------------
    labels = sorted({b['text'] for b in btns})
    add('cta_label', 'One CTA label on every button', 5 if len(labels) == 1 else (2 if len(labels) == 2 else 0), 5,
        '%d buttons, %d label(s): %s' % (len(btns), len(labels), labels[:4]))

    to_stack = [b for b in btns if b['href'].startswith('#')]
    out = [b for b in btns if not b['href'].startswith('#')]
    route_ok = len(btns) >= 3 and len(out) <= 1 and len(to_stack) >= len(btns) - 1
    add('routing', 'Buttons jump to the offer stack; only one goes to checkout', 5 if route_ok else 0, 5,
        '%d jump on the page, %d leave it (%s)' % (len(to_stack), len(out), [b['href'][:50] for b in out][:3]))

    dashes = len(re.findall('[—–]', text))
    banned = [w for w in [x.strip() for x in a.banned.split(',') if x.strip()] if re.search(r'\b%s\b' % re.escape(w), text, re.I)]
    add('words', 'No em/en dashes, no banned words', 5 if not dashes and not banned else 0, 5,
        'dashes: %d, banned words found: %s' % (dashes, banned or 'none'))

    ph = re.findall(r'\[(?:insert|placeholder|image|screenshot|photo|customer name|total value|your )[^\]]{0,60}\]|\{FILL IN[^}]*\}|lorem ipsum', text, re.I)
    ph_html = len(re.findall(r'class="[^"]*\bph\b', html))
    ok = not ph and not ph_html
    add('placeholders', 'No placeholders on the page', 5 if ok else 0, 5, ph[:4] or ('%d .ph boxes' % ph_html if ph_html else 'none'))
    if not ok:
        hard.append('Placeholders on the page: %s' % (ph[:3] or '%d .ph boxes' % ph_html))

    # Image weight: the `src` of every <img> (desktop-size picks), local files only.
    base = os.path.dirname(os.path.abspath(a.page)) if not re.match(r'https?://', a.page) else None
    total, webp, counted = 0, 0, 0
    for s in sorted({i.get('src', '') for i in p.imgs}):  # each file once (slider copies reuse the same file)
        if base and s and not re.match(r'https?:|data:', s):
            f = os.path.join(base, s)
            if os.path.exists(f):
                total += os.path.getsize(f); counted += 1
                webp += s.lower().endswith(('.webp', '.avif'))
    if base and counted:
        mb = total / 1e6
        pts = 2 if mb <= 2.0 and webp >= counted * 0.8 else (1 if mb <= 4 else 0)
        add('weight', 'Images light: WebP, total under ~2 MB', pts, 2, '%.2f MB over %d images, %d WebP' % (mb, counted, webp))
    else:
        add('weight', 'Images light: WebP, total under ~2 MB', 0, 2, 'MANUAL: check in DevTools Network (remote page)', manual=True)

    # Copy coverage (optional): the kit's check_page does the full line-by-line match.
    if a.copy and os.path.exists(a.copy):
        lines = [re.sub(r'[*_#>`]', '', l).strip() for l in open(a.copy, encoding='utf-8')]
        lines = [l for l in lines if len(l) > 25 and not l.lower().startswith(('section', '<!--', '[button'))]
        norm = lambda s: re.sub(r'[^a-z0-9$]+', ' ', s.lower()).strip()
        page_n = norm(text)
        miss = [l for l in lines if norm(l)[:60] not in page_n]
        add('copy', 'Approved copy is on the page (copy.md lines found)', 0, 0,
            '%d of %d long lines found%s' % (len(lines) - len(miss), len(lines), ('; missing e.g. "%s"' % miss[0][:70]) if miss else ''))

    score = sum(i['points'] for i in items)
    mx = sum(i['max'] for i in items)
    res = {'page': a.page, 'auto_score': score, 'auto_max': mx, 'hard_fails': hard, 'items': items}
    if a.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return
    print('AUTO GRADE  %s' % a.page)
    print('-' * 72)
    for i in items:
        mark = 'MANUAL' if i['manual'] else ('PASS' if i['points'] == i['max'] else ('PART' if i['points'] else 'FAIL'))
        if i['max'] == 0:
            mark = 'INFO'
        print('%-6s %2d/%-2d %s\n              %s' % (mark, i['points'], i['max'], i['item'], i['detail']))
    print('-' * 72)
    print('Automatic score: %d / %d   (the other 50 points are judged: see test/rubric.md)' % (score, mx))
    print('HARD FAILS: %s' % ('; '.join(hard) if hard else 'none'))


if __name__ == '__main__':
    main()
