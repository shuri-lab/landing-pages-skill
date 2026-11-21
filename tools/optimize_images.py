#!/usr/bin/env python3
"""Make every page image light: WebP at the size it is shown, never bigger than the original.

Usage:
  python3 tools/optimize_images.py my-sales-page/images            # sizes picked by file-name prefix
  python3 tools/optimize_images.py my-sales-page/images --spec my-sales-page/image-sizes.json
Writes my-sales-page/images/opt/<name>-<width>.webp and prints a size report.
Needs Pillow:  python3 -m pip install Pillow  (or a venv)

Name your images by role (Stage 4) and the right sizes are chosen for you:
  hero-*      720, 1280      big product mockup at the top (use srcset, see stages/8-speed.md)
  product-*   160, 720, 1280 offer items: 160 for the small offer-stack thumbnail
  section-*   720, 1280      section images (AI images, bundle shots)
  photo-*     900            founder photos
  logo-*      400            your own logo
  brand-*     360            brand / press logos in the slider
  shot-*      480            phone screenshots (TikTok, Instagram, results) in sliders
  proof-*     480            result screenshots shown inline
  thumb-*     160            small thumbnails
  anything else: 720, 1280
A spec file overrides per image: {"rickey-bestbuy.jpg": [672], "starter-product-list.png": [320, 720]}
"""
import json, os, sys

try:
    from PIL import Image
except ImportError:
    sys.exit('Pillow is missing: python3 -m pip install Pillow')

ROLE_SIZES = [
    ('hero-', [720, 1280]), ('product-', [160, 720, 1280]), ('section-', [720, 1280]),
    ('photo-', [900]), ('logo-', [400]), ('brand-', [360]), ('shot-', [480]), ('tiktok-', [480]),
    ('proof-', [480]), ('thumb-', [160]),
]
DEFAULT = [720, 1280]
EXT = ('.png', '.jpg', '.jpeg', '.webp')


def sizes_for(name, spec):
    if name in spec:
        return spec[name]
    for prefix, sizes in ROLE_SIZES:
        if name.lower().startswith(prefix):
            return sizes
    return DEFAULT


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    d = sys.argv[1]
    spec = {}
    if '--spec' in sys.argv:
        spec = json.load(open(sys.argv[sys.argv.index('--spec') + 1]))
    out = os.path.join(d, 'opt')
    os.makedirs(out, exist_ok=True)
    tot_in = tot_out = 0
    for f in sorted(os.listdir(d)):
        p = os.path.join(d, f)
        if not os.path.isfile(p) or not f.lower().endswith(EXT):
            continue
        im = Image.open(p)
        im.load()
        alpha = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
        im = im.convert('RGBA' if alpha else 'RGB')
        tot_in += os.path.getsize(p)
        for w in sizes_for(f, spec):
            w2 = min(w, im.width)
            h2 = round(im.height * w2 / im.width)
            r = im.resize((w2, h2), Image.LANCZOS) if w2 != im.width else im
            q = 82 if w >= 700 else 80
            o = os.path.join(out, '%s-%d.webp' % (os.path.splitext(f)[0], w))
            r.save(o, 'WEBP', quality=q, method=6)
            tot_out += os.path.getsize(o)
            print('%-44s %5dx%-5d %7.1f KB' % (os.path.basename(o), w2, h2, os.path.getsize(o) / 1024))
    print('originals %.1f MB -> all WebP variants %.2f MB (a visitor only downloads one size of each)'
          % (tot_in / 1e6, tot_out / 1e6))


if __name__ == '__main__':
    main()
