#!/usr/bin/env python3
"""Assemble the sales page (draft with the layout editor inside).

usage:
  python3 build_page.py --body body.html --kit brand-kit.md --out index.html [--title "My page"]

--body  the page content: everything that goes inside <div id="page"> (the <section> blocks)
--kit   the brand kit file (a markdown file with a "Role map" and "Fonts", see 2-brand/_template.md)
--out   where to write the finished draft (open it in a browser)

Only the Python standard library is used.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROLE_RE = re.compile(
    r'^\s*[-*]\s*(ink-soft|on-dark-2|on-dark|on-hi|bg|paper|ink|accent|soft|hi|sand|dark)\s*(?:\([^)]*\))?\s*:\s*(#[0-9A-Fa-f]{6})',
    re.M)
REQUIRED = ['bg', 'paper', 'ink', 'ink-soft', 'accent', 'soft', 'hi', 'sand', 'dark', 'on-dark', 'on-dark-2']


def parse_kit(path):
    text = open(path, encoding='utf-8').read()
    roles = {m.group(1): m.group(2).upper() for m in ROLE_RE.finditer(text)}
    fonts = {}
    for key, name in (('Big', 'head'), ('Standard', 'body'), ('Handwritten', 'hand')):
        m = re.search(r'^\s*[-*]\s*' + key + r'[^:\n]*:\s*([^\n]+)', text, re.M)
        if m:
            fonts[name] = m.group(1).strip()
    return roles, fonts


def split_font(spec):
    """'Montserrat 800' -> ('Montserrat', '800'); 'Lato' -> ('Lato', None)"""
    spec = re.sub(r'\(.*?\)', '', spec).strip()
    m = re.match(r'^(.*?)(?:\s+(\d{3}))?(?:\s*\+.*)?$', spec)
    return (m.group(1).strip() or 'Arial'), m.group(2)


def font_url(fonts):
    fams = []
    for key in ('head', 'body', 'hand'):
        if key not in fonts:
            continue
        name, weight = split_font(fonts[key])
        fam = name.replace(' ', '+')
        if key == 'head':
            ws = sorted({'700', '800', '900', weight or '800'})
            fams.append('family=%s:wght@%s' % (fam, ';'.join(ws)))
        elif key == 'body':
            fams.append('family=%s:wght@400;700;900' % fam)
        else:
            fams.append('family=%s' % fam)  # default weight; the page uses it as a handwritten accent
    return 'https://fonts.googleapis.com/css2?%s&display=swap' % '&'.join(fams)



def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def contrast_report(r):
    pairs = [('ink on bg', 'ink', 'bg', 4.5), ('ink on paper', 'ink', 'paper', 4.5), ('ink-soft on bg', 'ink-soft', 'bg', 4.5),
             ('ink on sand', 'ink', 'sand', 4.5), ('on-dark on dark', 'on-dark', 'dark', 4.5), ('on-dark-2 on dark', 'on-dark-2', 'dark', 4.5),
             ('button text on button', 'on-hi', 'hi', 4.5), ('accent on paper (large text only)', 'accent', 'paper', 3.0)]
    out = []
    for label, fg, bgk, need in pairs:
        v = ratio(r[fg], r[bgk])
        out.append('  %-36s %.1f:1  %s' % (label, v, 'ok' if v >= need else 'LOW (needs %.1f). Use a darker or lighter twin and tell the client.' % need))
    return '\n'.join(out)

REVEAL_JS = """(function(){
if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
if(!('IntersectionObserver' in window))return;
document.documentElement.classList.add('anim');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.r').forEach(function(el){io.observe(el)});
setTimeout(function(){document.querySelectorAll('.r:not(.in)').forEach(function(el){var r=el.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)el.classList.add('in')})},2500);
})();
/* Phones and tablets: stretch the page to the full screen width even when the builder pads the code block (no white strips left and right) */
(function(){var p=document.getElementById('page');if(!p)return;
function fit(){p.style.width='';p.style.marginLeft='';p.style.maxWidth='';
if(window.innerWidth>820)return;
var l=p.getBoundingClientRect().left;
p.style.maxWidth='none';p.style.width=window.innerWidth+'px';p.style.marginLeft=(-l)+'px';}
fit();window.addEventListener('resize',fit);window.addEventListener('load',fit);})();"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--body', required=True)
    ap.add_argument('--kit', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--title', default='Sales page')
    a = ap.parse_args()

    roles, fonts = parse_kit(a.kit)
    missing = [r for r in REQUIRED if r not in roles]
    if missing:
        sys.exit('The brand kit is missing these colors in its Role map: %s (see 2-brand/_template.md)' % ', '.join(missing))
    roles.setdefault('on-hi', roles['ink'])
    for k, dflt in (('head', 'Montserrat 800'), ('body', 'Lato'), ('hand', 'Caveat')):
        fonts.setdefault(k, dflt)

    # speed: a stand-in font with the same width as the web font, so the text does not jump when the web font loads
    try:
        fb_table = json.load(open(os.path.join(HERE, 'font-fallbacks.json'), encoding='utf-8')).get('fonts', {})
    except (OSError, ValueError):
        fb_table = {}
    fb_css = ''
    fb_names = set()
    for k in ('head', 'body'):
        nm = split_font(fonts[k])[0]
        r = fb_table.get(nm)
        if r and nm not in fb_names:
            fb_names.add(nm)
            fb_css += ("@font-face{font-family:'%s Fallback';src:local('Arial');font-weight:400 500;size-adjust:%.1f%%}\n"
                       "@font-face{font-family:'%s Fallback';src:local('Arial Bold'),local('Arial-BoldMT');font-weight:600 900;size-adjust:%.1f%%}\n"
                       % (nm, r['400'] * 100, nm, r['700'] * 100))

    def fam(k, generic):
        nm = split_font(fonts[k])[0]
        if nm in fb_names:
            return "'%s','%s Fallback',%s" % (nm, nm, generic)
        return "'%s',%s" % (nm, generic)

    root = fb_css + ':root{' + ''.join('--%s:%s;' % (r, roles[r]) for r in REQUIRED + ['on-hi']) + \
        '--font-head:%s;--font-body:%s;--font-hand:%s;}' % (fam('head', 'sans-serif'), fam('body', 'sans-serif'), fam('hand', 'cursive'))

    css = open(os.path.join(HERE, 'base.css'), encoding='utf-8').read()
    ecss = open(os.path.join(HERE, 'editor.css'), encoding='utf-8').read()
    ejs = open(os.path.join(HERE, 'editor.js'), encoding='utf-8').read()
    body = open(a.body, encoding='utf-8').read()

    # speed: the first image loads first, every other image waits until it is near the screen
    def load_attrs(m, first=[True]):
        tag = re.sub(r'\s(?:loading|decoding|fetchpriority)="[^"]*"', '', m.group(0))
        extra = ' fetchpriority="high" decoding="async"' if first[0] else ' loading="lazy" decoding="async"'
        first[0] = False
        return tag[:-1].rstrip() + extra + '>'
    body = re.sub(r'<img\b[^>]*>', load_attrs, body)

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="%s" rel="stylesheet">
<style>
/* brand kit */
%s
%s
</style>
<style id="layout-edits"></style>
<style id="editor-css">
%s
</style>
</head>
<body>
<div id="page">
%s
</div>
<script type="application/json" id="layout-edits-data">{}</script>
<script id="layout-editor">
%s
</script>
<script>
%s
</script>
</body>
</html>
''' % (a.title.replace('<', '&lt;'), font_url(fonts).replace('&', '&amp;'), root, css, ecss, body, ejs, REVEAL_JS)
    with open(a.out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Contrast check:')
    print(contrast_report(roles))
    print('wrote %s (%d bytes). Open it in a browser. Click "Edit layout" at the bottom to move, resize and recolor.' % (a.out, len(html.encode('utf-8'))))


if __name__ == '__main__':
    main()
