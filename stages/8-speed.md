# Stage 8 of 9: Speed

**Goal:** the page loads fast on a phone without losing quality. Rickey's page went from about 15 MB of images to about 1.2 MB on a phone (full scroll) and 1.5 MB on desktop. Do this **before** going live, not after the client complains ("the images are loading super slow" was a real feedback round).

## The steps (any project)

1. **Name images by role** (Stage 4) and run:
   ```bash
   python3 PLAYBOOK/tools/optimize_images.py my-sales-page/images          # writes images/opt/*.webp
   ```
   Sizes per role are built in (hero 720/1280, product 160/720/1280, brand logos 360, screenshots 480, photos 900…). Override one image with `--spec image-sizes.json`.
2. **Point the page at the WebP files** (`images/opt/<name>-<w>.webp`):
   - Hero: `src` = the 1280 version, `srcset="…-720.webp 720w, …-1280.webp 1280w"`, `sizes` matching its display width, `fetchpriority="high"`, **no** `loading="lazy"`.
   - Everything else: `loading="lazy" decoding="async"`, `width`/`height` set (no layout jump).
   - Slider images start off-screen, so lazy loading never fetches them: the slider JS sets them to eager when the slider is near (component C1).
3. **Videos:** host on Cloudinary (or similar), serve `w_320,q_auto:eco,ac_none,du_10,f_auto`, poster `w_320,so_1,f_auto,q_auto/<id>.jpg`, `preload="none"`, `data-src` filled in only when the carousel is near the screen; duplicate loop cards wait for their original's `loadeddata` so each video downloads once.
4. **Rebuild and verify:** `tools/rebuild.sh`, then `test/grade.py` (image weight, broken images) and a look at the phone screenshots (no blank images).

The exact recipe we used, with every value, follows.

---

### C1. Starting point (measured)
- Originals: ~15–16 MB of images ("originals 16 MB → all WebP variants 1.92 MB" per the optimizer; README says "~15 MB"). Big offenders were 1.6–1.9 MB PNG mockups: `hero-headstart-mockup(-nobg).png` 1,693/1,874 KB, `course-7-day.png` 1,862 KB, `challenge-30-day.png` 1,707 KB, `starter-product-list.png` 1,877 KB, `whatsapp-channel(-alt).png` 1,579/1,659 KB, `offer-2-system.png` 2,104 KB. TikTok screenshots were ~180–290 KB JPGs each at 946×2048.
- Videos: Cloudinary `w_360,q_auto,ac_none,du_12/<id>.mp4` = 913,892 bytes per clip; poster `w_360,so_1/<id>.jpg` = 31,305 bytes.
- Tools on the Mac: no `cwebp`, `magick`/`convert`, `ffmpeg`, `avifenc`, and no Pillow in system Python. `sips --formats` lists WebP and AVIF as readable but **not writable**. Fix: `python3 -m venv $SP/venv && $SP/venv/bin/pip install -q pillow`, then `features.check('webp')` → True.

### C2. Decide display widths per image role (read the CSS first)
Grep each `<img>` and the CSS that sizes it. In this page: `.gt-logo` 150px; marquee logos `height:38–42px; max-width:150px`; mini-marquee 26–30px high; slider screenshots 210px (160px on phones); offer thumbnails `.items .thumb` 64×44 (52×38 on phones); `.vcard` 200px (150px on phones), 9:16; hero full width on phones, ~600–700px on desktop; offer hero 100% of a ~640px card.

**Rule:** target about 2× the largest display width (for retina screens), never upscale, and give a 720/1280 pair with `srcset` to anything that can be full-width.

| Image role | Widths generated | Quality | Example |
|---|---|---|---|
| Hero / offer mockups (full width) | 720 + 1280 (srcset) | 82 | `hero-headstart-mockup-nobg-720.webp` 58 KB, `-1280` 128 KB |
| Feature/product images shown large and as thumbs | 160 (thumb) + 720 + 1280 | 80 (160) / 82 | `course-7-day-160/720/1280.webp` 4/45/97 KB |
| Bump image (checkout) | 320 (+720/1280 for page use) | 80 / 82 | `starter-product-list-320.webp` 14 KB |
| Phone screenshots in a slider (210px) | 480 | 80 | `tiktok-*-480.webp` 45–88 KB each |
| Brand logos in marquee (≤150px) | 360 | 80 | `brand-*-360.webp` 4–25 KB |
| Brand logo (150px) | 400 | 80 | `logo-gametape-black-400.webp` 4 KB |
| Portrait photos (polaroids) | 900 (`rickey-photo`), 672 (`rickey-bestbuy`, original width) | 82 / 80 | 94 KB / 50 KB |
| Proof screenshots (native size) | 388 and 371 (= original width, no resize) | 80 | 27 KB / 22 KB |
| Upsell product image | 720 + 1280 | 82 | `offer-2-system-720/1280.webp` 57/131 KB |
| Upsell stack thumbnails (crops of the product image) | thumbnail fit in 240×240 | 82 | `o2-course-240.webp` 9 KB, `o2-hooks/formats/checklist-240` 5–6 KB |

Encoder settings: Pillow `save(o,'WEBP',quality=q,method=6)`, resize with `Image.LANCZOS`, keep alpha (`RGBA` if mode is RGBA/LA or P with transparency, else `RGB`). Quality is 82 for widths ≥700 and 80 below.

(The kit's own `MAKE-YOUR-PAGE-LOAD-FASTER.txt` suggests WebP q80–86, at most 2× display width, ~1500px for a big top mockup, ≤1200px for most others, q≈90 at full width for testimonial/proof screenshots, and originals kept in `images-original/`. The session used `images/` for originals and `images/opt/` for variants instead.)

### C3. Markup rules (in `body-src.html` and the generator)
- **Hero (the LCP image):**
  ```html
  <img fetchpriority="high" decoding="async"
       src="images/opt/hero-headstart-mockup-nobg-1280.webp"
       srcset="images/opt/hero-headstart-mockup-nobg-720.webp 720w, images/opt/hero-headstart-mockup-nobg-1280.webp 1280w"
       sizes="(min-width: 1000px) 600px, 100vw" alt="…" width="1672" height="941">
  ```
  No `loading="lazy"`. Keep the intrinsic `width`/`height` so nothing jumps (CLS).
- **Other large images:** same `srcset`, `sizes="(min-width: 760px) 640px, 100vw"`, `loading="lazy" decoding="async"`. The upsell product image uses `sizes="(min-width: 800px) 760px, 100vw"` with `fetchpriority="high"`, because it is the upsell's hero.
- **Thumbs:** `class="thumb" src="images/opt/<name>-160.webp"`, keeping the original `width`/`height` attributes for the aspect ratio.
- **Every image:** `decoding="async"`. Every image except the hero: `loading="lazy"`.
- **Sliders and marquees:** images that start off-screen to the side never trigger native lazy loading, so a script switches them to eager when the slider is near:
  ```js
  document.querySelectorAll('.marquee,.slider').forEach(function(sl){
   function load(){sl.querySelectorAll('img').forEach(function(i){i.loading='eager';});}
   if(!('IntersectionObserver' in window)){load();return;}
   var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){load();io.disconnect();}},{rootMargin:'600px 0px'});io.observe(sl);
  });
  ```
  The "never run out" fill script that doubles a track also sets `loading='eager'` on its clones and `aria-hidden="true"`.
- **Bulk conversion of existing tags:** a Python regex over every `<img>` that maps `src="images/<n>.(png|jpg)"` → `images/opt/<n>-160.webp` for `class="thumb"`, `-480` for `tiktok-*`, the 720/1280 srcset for the multi-size set, and fixed widths for singles (`rickey-photo 900, rickey-bestbuy 672, product-check-listing 388, product-check-earnings 371, logos 400`). Then assert "left png/jpg refs: 0" (34 WebP refs after).

### C4. Videos (Cloudinary transforms + lazy loading)
- **Transform strings** (base `https://res.cloudinary.com/<cloud>/video/upload/`):
  - Video: `w_320,q_auto:eco,ac_none,du_10,f_auto/<public_id>` (**no file extension**, so `f_auto` can pick the best format for each browser). `w_320` = 320px wide (card is 200px), `q_auto:eco` = automatic lower quality, `ac_none` = audio removed, `du_10` = first 10 seconds.
  - Poster: `w_320,so_1,f_auto,q_auto/<public_id>.jpg` (`so_1` = frame at 1 s).
- **Measured** with `curl -A "<Safari UA>" -w "%{http_code} %{size_download} %{content_type}"`. Send a real browser UA, because `f_auto` negotiates format by browser:

  | Transform | Bytes |
  |---|---|
  | `w_360,q_auto,ac_none,du_12/…mp4` (before) | 913,892 |
  | `w_320,q_auto,ac_none,du_10/…mp4` | 626,446 |
  | **`w_320,q_auto:eco,ac_none,du_10,f_auto/…`** (after) | **441,770** (−52%) |
  | poster `w_360,so_1/….jpg` (before) | 31,305 |
  | **poster `w_320,so_1,f_auto,q_auto/….jpg`** (after) | **26,310** |
- **Markup** (written by the generator):
  ```html
  <div class="vcard"><video muted loop playsinline preload="none"
    data-src="https://res.cloudinary.com/<cloud>/video/upload/w_320,q_auto:eco,ac_none,du_10,f_auto/<id>"
    poster="https://res.cloudinary.com/<cloud>/video/upload/w_320,so_1,f_auto,q_auto/<id>.jpg"
    aria-label="…"></video></div>
  ```
  The loop duplicates are the same cards wrapped in `aria-hidden="true"` with no label.
- **Loader script:** set `src` from `data-src` only when the carousel is within 300px of the viewport. Pause when it leaves. Don't autoplay under `prefers-reduced-motion`. **Duplicates wait for their original's `loadeddata`**, then reuse the cached file, so each video downloads once:
  ```js
  var box=document.querySelector('.vcar');if(!box)return;
  var vids=[].slice.call(box.querySelectorAll('video[data-src]'));
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function go(v){if(!v.getAttribute('src')){v.src=v.getAttribute('data-src');}if(!reduce){var p=v.play();if(p&&p.catch)p.catch(function(){});}}
  var real=vids.filter(function(v){return !v.parentNode.hasAttribute('aria-hidden');}),dup=vids.filter(function(v){return v.parentNode.hasAttribute('aria-hidden');});
  function start(){real.forEach(go);dup.forEach(function(v,i){var o=real[i%real.length];if(v.getAttribute('src')||!o||o.readyState>=2){go(v);}else if(!v._w){v._w=1;o.addEventListener('loadeddata',function(){go(v);},{once:true});}});}
  function stop(){vids.forEach(function(v){v.pause();});}
  if(!('IntersectionObserver' in window)){start();return;}
  new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)start();else stop();});},{rootMargin:'300px 0px'}).observe(box);
  ```

### C5. Fonts (already handled by the kit's build, keep it)
The export preloads the Google Fonts stylesheet without blocking paint (`<link rel="preload" as="style" … onload="this.rel='stylesheet'">` + `<noscript>` fallback), preconnects to `fonts.googleapis.com`/`fonts.gstatic.com`, and defines same-width fallback faces (`@font-face{font-family:'Poppins Fallback';src:local('Arial');size-adjust:112.6%}` etc.) so text doesn't jump. Only the weights in use are loaded (Poppins 700/800/900, Lato 400/700/900, Caveat). The builder fragments (checkout, thank-you, upsell) load fonts with a plain `<link>`. The kit's guide caps a page at 3 font families.

### C6. Results (before → after)
- Images, full scroll: **~15 MB → ~1,155 KB on phone, ~1,452 KB on desktop** (all variants together 1.92 MB on disk).
- Per video clip: 892 KB → 431 KB; poster 31 → 26 KB. A full-scroll audit counted ~1.5 MB of video in total for the carousel, with duplicates not downloading again.
- Builder page HTML: 116 KB (reported by the build), with 0 relative image paths left and 1 checkout link.
- The hero loads first. Everything else loads on scroll.

### C7. How it was verified
1. Kit check: `check_page.py --page … --copy copy.md --images-dir images` → "OK: nothing that must be fixed".
2. Wait for Pages to serve the new file: poll with a cache-buster and a unique string from the new build, e.g. `for i in $(seq 1 20); do curl -s "<pages-url>/offer-1-sales-page/ghl-sales-page.html?r=$i" | grep -q 'opt/hero-headstart-mockup-nobg-1280.webp' && break; sleep 10; done` → "live after ~60s".
3. Live audit in the browser (run on the real page URL):
   ```js
   await new Promise(r=>setTimeout(r,3000));
   for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,250));}
   await new Promise(r=>setTimeout(r,5000));
   const rs=performance.getEntriesByType('resource'); const g=k=>rs.filter(r=>r.name.includes(k));
   const sum=a=>Math.round(a.reduce((s,r)=>s+(r.transferSize||r.encodedBodySize||0),0)/1024);
   ({imgs:g('<pages-host>/<repo>/images').length,
     oldPngJpg:g('<repo>/images/').filter(r=>/\.(png|jpg)$/.test(r.name)).map(r=>r.name.split('/').pop()),
     videos:g('/video/upload/').filter(r=>!r.name.endsWith('.jpg')).map(r=>r.name.split('/').slice(-3,-1).join('/')+' '+Math.round((r.transferSize||r.encodedBodySize)/1024)+'KB'),
     videoKB:sum(g('/video/upload/')), bumpText:document.body.innerText.includes('<bump product name>'),
     brokenImgs:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.split('/').pop())})
   ```
   Result: 31 images, `oldPngJpg: []`, `brokenImgs: []`, `bumpText: false`.
4. **Cross-origin images report `transferSize` 0**, because GitHub Pages sends no `Timing-Allow-Origin` header. So image weight was computed from the local files the page references: phone = every referenced variant except `-1280`; desktop = the `-1280` file wherever both exist.
   ```python
   refs=set(re.findall(r'images/(opt/[^" ,]+\.webp)',h))
   mob={r for r in refs if not r.endswith('-1280.webp')}
   desk={r for r in refs if not (r.endswith('-720.webp') and r.replace('-720','-1280') in refs)}
   ```
5. Screenshots at 393×852 and 1280×800 of the offer section, to check sharpness. Final phone pass: `scrollWidth` equals viewport width, 0 broken images.
6. **Not done (gap for the playbook):** a PageSpeed Insights mobile run. The kit's guide targets Performance ≥90, FCP/LCP <2.5 s, CLS <0.1. Add it as a required step.

