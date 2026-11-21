#!/usr/bin/env python3
"""Make the final page, and a paste-ready version for page builders (Kajabi, GoHighLevel, Systeme.io, ...).

usage:
  python3 export_final.py --in index.html --out-dir export [--images keep|embed|urls] [--urls image-urls.json]

--in         the draft made by build_page.py, or the file saved with "Save draft" from the layout editor
--out-dir    folder for the results
--images     how the paste-ready file handles images:
               keep   leave "images/xyz.webp" as they are (the page needs the images folder beside it)
               embed  build every image into the file (one paste, but big: keep the total under about 2.5 MB)
               urls   point images at links you got after uploading them to your platform (see --urls)
--urls       a JSON file like {"hero.png": "https://.../hero.png"} for the "urls" mode. Any image that has a link
             is used from its link in every mode; images without a link follow --images.

Results:
  index-final.html   the page without the editor (open in a browser, or publish as a file)
  paste-ready.html   the code to paste into an HTML / custom code block (plain ASCII, styles stay inside the page)
  export-report.txt  what was done and what to check

Only the Python standard library is used.
"""
import argparse
import base64
import json
import mimetypes
import os
import re
import sys

PIXEL = 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='


def strip_editor(h):
    h = re.sub(r'<script id="layout-editor">.*?</script>\s*', '', h, flags=re.S)
    h = re.sub(r'<style id="editor-css">.*?</style>\s*', '', h, flags=re.S)
    h = re.sub(r'<script type="application/json" id="layout-edits-data">.*?</script>\s*', '', h, flags=re.S)
    h = re.sub(r'\sdraggable="(?:true|false)"', '', h)
    h = h.replace(' ed-selected', '').replace('ed-selected ', '')

    def fix_class(m):
        toks = m.group(1).split()
        if 'r' in toks and 'in' in toks:          # never save the "already revealed" state: the scroll effect must replay
            toks = [t for t in toks if t != 'in']
        return 'class="%s"' % ' '.join(toks)
    h = re.sub(r'class="([^"]*)"', fix_class, h)
    h = re.sub(r'<html([^>]*?)\sclass="[^"]*"', r'<html\1', h)
    return h


# ---- scope the page css so it cannot touch the host page ----
def scope_selector(s):
    s = s.strip()
    if not s or s.startswith('#page') or s.startswith(':root') or s == 'html':
        return s
    if s == 'body':
        return '#page'
    if s.startswith('.anim '):
        return '.anim #page ' + s[6:]
    return '#page ' + s


def split_commas(sel):
    out, depth, cur = [], 0, ''
    for ch in sel:
        if ch in '([':
            depth += 1
        if ch in ')]':
            depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur)
            cur = ''
        else:
            cur += ch
    out.append(cur)
    return out


def scope_css(css):
    out, i, n = '', 0, len(css)
    while i < n:
        if css[i].isspace():
            out += css[i]
            i += 1
            continue
        if css.startswith('/*', i):
            i = css.index('*/', i) + 2
            continue
        j = css.index('{', i)
        head = css[i:j]
        depth, k = 1, j + 1
        while depth:
            depth += {'{': 1, '}': -1}.get(css[k], 0)
            k += 1
        body = css[j + 1:k - 1]
        if head.strip().startswith('@'):
            if head.strip().startswith(('@media', '@supports')):
                out += head + '{' + scope_css(body) + '}'
            else:
                out += head + '{' + body + '}'
        else:
            out += ','.join(scope_selector(x) for x in split_commas(head)) + '{' + body + '}'
        i = k
    return out


HARDEN = '''
/* protect the page from the host page's own styles */
#page h1,#page h2,#page h3,#page p,#page li,#page span,#page div,#page a,#page figure,#page blockquote,#page cite,#page b,#page strong{color:inherit}
#page section{border:0;background:transparent}
#page img{border:0}
'''


def esc_html(t):
    return ''.join(c if ord(c) < 128 else '&#x%X;' % ord(c) for c in t)


def esc_css(t):
    return ''.join(c if ord(c) < 128 else '\\%X ' % ord(c) for c in t)


def esc_js(t):
    o = ''
    for c in t:
        if ord(c) < 128:
            o += c
        elif ord(c) > 0xFFFF:
            v = ord(c) - 0x10000
            o += '\\u%04X\\u%04X' % (0xD800 + (v >> 10), 0xDC00 + (v & 0x3FF))
        else:
            o += '\\u%04X' % ord(c)
    return o


def ascii_safe(doc):
    parts = re.split(r'(<style[^>]*>.*?</style>|<script[^>]*>.*?</script>)', doc, flags=re.S)
    return ''.join(esc_css(x) if x.startswith('<style') else esc_js(x) if x.startswith('<script') else esc_html(x) for x in parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='src', required=True)
    ap.add_argument('--out-dir', default='export')
    ap.add_argument('--images', choices=['keep', 'embed', 'urls'], default='keep')
    ap.add_argument('--urls')
    a = ap.parse_args()

    base_dir = os.path.dirname(os.path.abspath(a.src))
    os.makedirs(a.out_dir, exist_ok=True)
    final = strip_editor(open(a.src, encoding='utf-8').read())
    open(os.path.join(a.out_dir, 'index-final.html'), 'w', encoding='utf-8').write(final)

    urls = json.load(open(a.urls)) if a.urls else {}
    styles = re.findall(r'<style[^>]*>(.*?)</style>', final, re.S)
    css = scope_css('\n'.join(styles)) + HARDEN
    def nonblocking(tag):
        # speed: the Google Fonts stylesheet must not hold up the first paint
        if 'fonts.googleapis.com/css' in tag and 'rel="stylesheet"' in tag:
            href = re.search(r'href="([^"]+)"', tag).group(1)
            return ('<link rel="preload" as="style" href="%s" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
                    '<noscript><link rel="stylesheet" href="%s"></noscript>' % (href, href))
        return tag
    links = ''.join(nonblocking(m) + '\n' for m in re.findall(r'<link[^>]*>', final))
    body = re.search(r'<body[^>]*>(.*)</body>', final, re.S).group(1).strip()

    imgs = sorted(set(re.findall(r'images/([^"\' )]+)', body)))
    report, missing, embedded_bytes, dup = [], [], 0, False
    for f in imgs:
        key = 'images/' + f
        if f in urls:
            body = body.replace(key, urls[f])
            report.append('  %-40s -> your link' % f)
            continue
        if a.images == 'keep':
            continue
        if a.images == 'urls':
            body = body.replace(key, 'PASTE-YOUR-LINK-FOR-' + f)
            missing.append(f)
            continue
        path = os.path.join(base_dir, 'images', f)
        if not os.path.exists(path):
            report.append('  %-40s MISSING FILE, left as is' % f)
            continue
        data = open(path, 'rb').read()
        mt = mimetypes.guess_type(f)[0] or 'image/webp'
        uri = 'data:%s;base64,%s' % (mt, base64.b64encode(data).decode())
        embedded_bytes += len(uri)
        tag = '<img src="images/%s"' % f
        if body.count(tag) > 1:        # same picture used twice: embed once, fill the copy with a tiny script
            i = body.index(tag)
            body = body[:i] + '<img data-k="%s" src="%s"' % (f, uri) + body[i + len(tag):]
            body = body.replace(tag, '<img data-from="%s" src="%s"' % (f, PIXEL))
            dup = True
        else:
            body = body.replace(key, uri)
        report.append('  %-40s embedded (%d KB)' % (f, len(data) // 1024))
    if dup:
        body += '\n<script>document.querySelectorAll("img[data-from]").forEach(function(i){var s=document.querySelector("img[data-k=\\""+i.getAttribute("data-from")+"\\"]");if(s)i.src=s.src;});</script>\n'

    preload = ''
    imgm = re.search(r'<img\b[^>]*>', body)
    if imgm and 'fetchpriority="high"' in imgm.group(0):
        u = re.search(r'\ssrc="(https?://[^"]+)"', imgm.group(0))
        if u:
            preload = '<link rel="preload" as="image" href="%s" fetchpriority="high">\n' % u.group(1)
    out = '<!-- Sales page: paste into an HTML / custom code block -->\n' + links + preload + '<style>\n' + css + '\n</style>\n' + body + '\n'
    out = ascii_safe(out)
    pr = os.path.join(a.out_dir, 'paste-ready.html')
    open(pr, 'w', encoding='ascii').write(out)
    size = os.path.getsize(pr)

    lines = ['Export report', '=============', 'paste-ready.html: %.2f MB' % (size / 1e6), 'image mode: ' + a.images, '']
    lines += report or ['(no image changes)']
    if missing:
        lines += ['', 'UPLOAD THESE to your platform, then add their links to image-urls.json and run this again:'] + ['  ' + m for m in missing]
    if size > 2.5e6:
        lines += ['', 'WARNING: this paste is over 2.5 MB. Some builders refuse or break above this. Use --images urls with uploaded images.']
    if a.images == 'embed' and not urls and size > 2.0e6:
        lines += ['', 'Tip: very large images are better uploaded to your platform and used by link.']
    lines += ['', 'Files: index-final.html (no editor), paste-ready.html (for the code block).']
    open(os.path.join(a.out_dir, 'export-report.txt'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
