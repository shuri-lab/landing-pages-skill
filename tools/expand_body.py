#!/usr/bin/env python3
"""Expand the repeated parts of a page body from one config file, so every button label, logo strip,
video carousel and screenshot slider is written once and stays identical everywhere.

Usage:
  python3 tools/expand_body.py my-sales-page/body-src.html my-sales-page/body.html --config my-sales-page/page-config.json

In body-src.html write these markers where the parts go:
  @@CTA@@      the one button label used on every button
  @@CHECKOUT@@ the checkout link used on every button (href="@@CHECKOUT@@"); empty = the placeholder PASTE-YOUR-CHECKOUT-LINK
  @@PRICE@@    the price, e.g. $27
  @@LOGOS@@    the brand/press logo strip (written twice so the marquee never runs out)
  @@LOGOS1@@   the same logos once (for a static row)
  @@VIDEOS@@   the muted video carousel cards (written twice)
  @@SLIDER@@   the screenshot slider images (written twice)

page-config.json example (see examples/rickey-headstart/page-config.json):
{
  "cta": "GET INSTANT ACCESS · $27 →",
  "checkout": "https://your-domain.com/offer-checkout",
  "price": "$27",
  "logos": [{"file": "brand-subway-360.webp", "w": 800, "h": 160, "alt": "Subway logo"}],
  "video_base": "https://res.cloudinary.com/<cloud>/video/upload/",
  "video_transform": "w_320,q_auto:eco,ac_none,du_10,f_auto",
  "videos": [{"id": "v1792744659/Download", "alt": "Rickey in his car showing a pocket knife"}],
  "slider": [{"file": "shot-pocket-knife-480.webp", "w": 946, "h": 2048, "alt": "Rickey's TikTok: ..."}]
}
The second copy of each loop is aria-hidden so screen readers read it once.
"""
import json, re, sys


PLACEHOLDER = 'PASTE-YOUR-CHECKOUT-LINK'


def img(src, w, h, alt, hidden):
    return ('<img decoding="async" src="images/opt/%s" alt="%s" width="%d" height="%d" loading="lazy"%s>'
            % (src, alt, w, h, ' aria-hidden="true"' if hidden else ''))


def main():
    if len(sys.argv) < 3 or '--config' not in sys.argv:
        sys.exit(__doc__)
    src, out = sys.argv[1], sys.argv[2]
    cfg = json.load(open(sys.argv[sys.argv.index('--config') + 1], encoding='utf-8'))
    h = open(src, encoding='utf-8').read()

    # Every button goes straight to checkout, so the link is written once, here.
    link = str(cfg.get('checkout') or '').strip() or PLACEHOLDER
    if link != PLACEHOLDER and not re.match(r'https?://[^\s"\'<>]+$', link):
        sys.exit('page-config.json "checkout" must be a full https:// link (or empty until it exists): %r' % link)

    logos = cfg.get('logos', [])
    logos1 = '\n'.join(img(l['file'], l['w'], l['h'], l['alt'], False) for l in logos)
    logos2 = logos1 + '\n' + '\n'.join(img(l['file'], l['w'], l['h'], l['alt'], True) for l in logos)

    base, tf = cfg.get('video_base', ''), cfg.get('video_transform', 'w_320,q_auto:eco,ac_none,du_10,f_auto')

    def vcard(v, hidden):
        label = '' if hidden else ' aria-label="%s"' % v['alt']
        return ('<div class="vcard"%s><video muted loop playsinline preload="none" data-src="%s%s/%s" '
                'poster="%sw_320,so_1,f_auto,q_auto/%s.jpg"%s></video></div>'
                % (' aria-hidden="true"' if hidden else '', base, tf, v['id'], base, v['id'], label))
    vids = cfg.get('videos', [])
    videos = '\n'.join(vcard(v, False) for v in vids) + '\n' + '\n'.join(vcard(v, True) for v in vids)

    shots = cfg.get('slider', [])
    slider = '\n'.join(img(s['file'], s['w'], s['h'], s['alt'], False) for s in shots) + '\n' + \
        '\n'.join(img(s['file'], s['w'], s['h'], s['alt'], True) for s in shots)

    for k, v in (('@@CTA@@', cfg.get('cta', '')), ('@@CHECKOUT@@', link), ('@@PRICE@@', cfg.get('price', '')), ('@@LOGOS1@@', logos1),
                 ('@@LOGOS@@', logos2), ('@@PRESS@@', logos2),  # @@PRESS@@ = old name used in the Rickey body
                 ('@@VIDEOS@@', videos), ('@@SLIDER@@', slider)):
        h = h.replace(k, v)
    left = [m for m in ('@@CTA@@', '@@PRICE@@', '@@LOGOS@@', '@@VIDEOS@@', '@@SLIDER@@') if m in h]
    jumps = [a for a in re.findall(r'<a\b[^>]*>', h) if re.search(r'class="[^"]*\bbtn\b', a) and re.search(r'href="(#[^"]*|)"', a)]
    if jumps:
        sys.exit('%d button(s) do not go to checkout: use href="@@CHECKOUT@@" on every button. First: %s' % (len(jumps), jumps[0][:120]))
    if '@@' in h:
        sys.exit('Unexpanded marker left in the body: %s' % (left or 'check for typos like @@LOGO@@'))
    open(out, 'w', encoding='utf-8').write(h)
    print('ok: %d buttons use the same label' % h.count(cfg.get('cta', '\0')))
    print('checkout link on %d buttons: %s%s' % (h.count('href="%s"' % link), link,
          '  <- fill "checkout" in page-config.json before real traffic' if link == PLACEHOLDER else ''))


if __name__ == '__main__':
    main()
