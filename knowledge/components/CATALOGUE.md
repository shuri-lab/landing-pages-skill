# Component catalogue

Every reusable component built for the Rickey page. Line numbers refer to `examples/rickey-headstart/body-src.html` (the full working source: copy the markup, CSS and JS from there). CSS variables (`--hi`, `--accent`, `--ink`, `--soft`, `--paper`, `--font-head`) come from the kit's brand kit, so the components re-color with the brand automatically.

### C1. "Slider never runs out" (all marquees and sliders)
- **Markup:** `.marquee > .marquee-track` (logos) or `.slider > .slider-track` (screenshots). The generator writes the set twice: N items, then N copies with `aria-hidden="true"`.
- **CSS (17-22, 80-83):** `.marquee{overflow:hidden;mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}` (the slider uses 6%/94%). `.marquee-track{display:flex;align-items:center;gap:56px;width:max-content;animation:slideLeft 28s linear infinite}`. `@keyframes slideLeft{from{transform:translateX(0)}to{transform:translateX(-50%)}}`. Moving exactly −50% loops seamlessly as long as both halves are identical.
- **JS (726-733):**
  ```js
  function fill(){document.querySelectorAll('.marquee-track,.slider-track').forEach(function(t){
   var box=t.parentElement,n=0;
   while(t.scrollWidth/2<box.clientWidth+80&&n<4){var kids=[].slice.call(t.children);
     kids.forEach(function(k){var c=k.cloneNode(true);c.setAttribute('aria-hidden','true');if(c.tagName==='IMG')c.loading='eager';t.appendChild(c);});n++;}
  });}
  fill();window.addEventListener('load',fill);window.addEventListener('resize',fill);
  ```
  Cloning *all* current children doubles the track, so the two halves stay equal and −50% still loops. It runs again on `load` (images now have widths) and on `resize`. The cap is 4 doublings.
- **Companion JS (734-741):** images in a slider start off to the side, so native lazy loading would never fetch them. An IntersectionObserver (`rootMargin:'600px 0px'`) sets `loading='eager'` on every slider image once the slider is near the screen.
- **Gotchas:** A max-content track inside a CSS grid column widens the column and the page (scrollWidth went to 2051); fix with `min-width:0` on the grid children. Pause on hover with `.slider:hover .slider-track{animation-play-state:paused}`. For reduced motion, use `animation:none` plus `overflow-x:auto`.
- **Sizes:** Press strip: desktop logos 42px, base 38px (max-width 150px, grayscale(1), opacity .6), phone 40px (max-width 140px, opacity .75, gap 44px). Section 3 mini-marquee: gap 40px, 30px logos (26px phone), dashed top border. Screenshot slider: 210px images (160px phone), 60s loop, margin `40px -24px 0` (bleeds to the edge; `30px -18px 0` on phones), 2px ink border, radius 18, `box-shadow:5px 5px 0 var(--soft)`.

### C2. Press/brand logo strip (330-335)
`.press` is a white band with 1px `#ECE9E4` borders on top and bottom, padding 22/20 (phone 26/24, desktop 16/14 so it fits above the fold). The label `.press-lbl` is head font 800, 13px (12.5px phone, 14px desktop), .12em, uppercase, ink-soft. It sits directly after the hero `</section>`, outside any section.

### C3. Sticky mobile CTA (CSS 95-100, phone 265-267; HTML 723; JS 755-763)
- **CSS:** `.stickybar{position:fixed;left:0;right:0;bottom:0;z-index:60;background:rgba(16,16,23,.97);border-top:2px solid var(--hi);box-shadow:0 -10px 30px -12px rgba(0,0,0,.45);transform:translateY(130%);transition:transform .28s cubic-bezier(.32,.72,0,1);padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px))}`, `.stickybar.show{transform:none}`. `.sb-in` is a flex row (gap 14, max-width 1080). `.sb-lbl` is white 700 15px (13.5px phone) with the price `strong` in `#FF6B63`. The button is `padding:14px 26px;font-size:14px;border-color:#fff` on desktop and `flex:1;padding:13px 10px;font-size:13px` on phones.
- **JS logic:**
  ```js
  var pastHero=false,atBuy=false;
  function upd(){bar.classList.toggle('show',pastHero&&!atBuy);}
  new IntersectionObserver(function(es){pastHero=!es[0].isIntersecting&&es[0].boundingClientRect.top<0;upd();}).observe(hero);
  new IntersectionObserver(function(es){atBuy=es[0].isIntersecting;upd();},{threshold:.15}).observe(buy);
  ```
  `pastHero` requires the hero to be *above* the viewport (top < 0), so the bar doesn't show at page load.
- **Gotchas:** Add `footer{padding-bottom:110px}` so the bar never covers the disclaimers. As built, the bar also shows on desktop (no media query hides it).

### C4. Lazy video carousel (CSS 25-29; HTML 349-353; JS 742-754; markup from `tools/expand_body.py`)
- **Markup per card:** `<div class="vcard"><video muted loop playsinline preload="none" data-src="https://res.cloudinary.com/<cloud>/video/upload/w_320,q_auto:eco,ac_none,du_10,f_auto/<id>" poster=".../w_320,so_1,f_auto,q_auto/<id>.jpg" aria-label="…"></video></div>`. There are 5 originals plus 5 `aria-hidden` duplicates (no aria-label). Cloudinary transforms: `w_320` width, `q_auto:eco` quality, `ac_none` strips audio, `du_10` trims to 10s, `f_auto` picks the format. The poster comes from `so_1` (the frame at 1s). The earlier rule used `w_360,q_auto,ac_none,du_12`.
- **CSS:** `.vcar{overflow:hidden;max-width:1040px;margin:44px auto 40px;mask-image:…5%…95%}`, `.vcar-track{display:flex;gap:16px;width:max-content;animation:slideLeft 45s linear infinite;padding:6px 8px 12px}`, paused on hover, `.vcard{flex:none;width:200px;aspect-ratio:9/16;border-radius:18px;border:2px solid var(--on-dark);box-shadow:5px 5px 0 var(--accent)}`. On phones: `.vcard{width:150px}`, `.vcar{margin:30px 0 28px}`.
- **JS:** An IntersectionObserver (`rootMargin:'300px 0px'`) calls `start()` when the carousel is near the screen. It copies `data-src` into `src` and calls `play()`, catching the rejected promise. It skips autoplay under `prefers-reduced-motion`. **Duplicates wait for their original's `loadeddata`, so each video downloads only once.** `stop()` pauses every video when the carousel leaves the screen.
- **Never runs out:** Videos aren't cloned by JS (too heavy). Instead the container is capped so one half of the track (5 × (200 + 16) = 1080px) is always wider than the box (1040px). On phones, 5 × 166 = 830 > 393.

### C5. Above-the-fold hero (CSS 8-16, phone 205-217, desktop 272-287; HTML 319-328)
Classes: `.hero.center > .wrap.hero-wrap > figure.fig.hero-img`, `img.gt-logo`, `.trust` (pill), `h1`, `p.lede` (with `mark` and `.red`), `.cta > a.btn + span.fine`. Phone layout is a flex column with `order`; desktop is the grid in B5. Measurement method: see D.

### C6. Alert bar (CSS 5-7, phone 205-206, desktop 285; HTML 316)
`<div class="alertbar" role="note"><span class="dot" aria-hidden="true"></span>One-time $27 · instant access</div>`, placed before section 1. Values are in A 1.14 and 2.1.

### C7. Outcome cards with media (CSS 30-38, desktop 288-298; HTML 356-363)
`.outcomes > .outcome > span.n + div > (p > strong + br + text) + div.o-media[.two|.wide]`. Hide the `br` (`.s2 .outcome p br{display:none}`) once `strong` is a block. On desktop the outcomes bleed 130px past the narrow wrap on each side.

### C8. Offer stack (CSS 57-79 base, 153-185 v2, 188-200 JJ deal, phone 227-251; HTML 537-566)
- `.offer`: `max-width:660px` (680 desktop), `padding:0;overflow:hidden`, `background:var(--paper);border:1.5px solid #E2DED8;border-radius:26px` (22 phone), `box-shadow:0 26px 50px -24px rgba(16,16,23,.35)`.
- `.offer-head`: dark, padding 30/26/26 (24/18/22 phone). The h2 is white with a mark tinted `color-mix(in srgb,var(--accent) 75%,transparent)`. `.sub` is a red pill: 13px, 800, .08em, uppercase, padding 6px 14px.
- `.offer-body`: padding 26/30/30 (desktop 30/40/34, phone 20/16/22). `figure.offer-hero` holds the full product mockup (radius 14).
- `.items li`: flex, centered, gap 14, padding 13px 0, 1px `#ECE9E4` bottom border, 16.5px 700 (15.5 phone, 17.5 desktop). `.thumb` is 64×44 with `object-fit:cover` and radius 8 (52×38 phone). `.nm{flex:1}`. `.val s` is 19px ink-soft with a 2.5px red strike.
- `.stack-total`: flex, space-between, sand background, radius 14, padding 15px 18px, head 800 18px. The struck `s` is 26px with a 3px red strike (phone 16px / 23px).
- `.deal`: `position:relative;margin-top:30px;border:2.5px solid var(--hi);border-radius:20px;background:linear-gradient(165deg,#fff,color-mix(in srgb,var(--soft) 45%,#fff));padding:34px 22px 22px;text-align:center` (phone 32/16/18).
- `.deal-badge`: `position:absolute;top:-16px;left:50%;transform:translateX(-50%)`, red pill, head 800 13px .07em uppercase, padding 8px 18px, `box-shadow:0 10px 22px -10px rgba(211,8,5,.7)`.
- `.deal-now`: flex baseline, gap 10. The span "Today: just" is 21px (18 phone); `b` is 84px (70 phone), red, letter-spacing −.03em.
- `.deal-note`: 14.5px 700 ink-soft. `.deal .btn{width:100%}`.
- `.trust-row`: centered flex wrap, gap 8px 20px, `li` 13.5px 700 ink-soft. Its SVGs are 18px with red stroke 2 (card, bolt and shield-check icons).
- Earlier versions are kept in the CSS (v1 `.totals`, v2 `.pricebox`/`.pb-col`). They're harmless but could be removed. The `.bump` add-on (dashed red, red head bar, image + text) followed the deal box in this slice; it's gone from the final file.

### C9. Guarantee block (CSS 109-115, phone 218-221; HTML 569-579)
- `.guar-sec{padding:56px 0;background:var(--paper);border-top:1px solid #ECE9E4}` (40px on phones).
- `.guar-card{display:flex;align-items:center;gap:30px;max-width:720px;margin:0 auto;text-align:left;border:2px dashed var(--hi);border-radius:24px;padding:30px 34px;background:color-mix(in srgb,var(--soft) 30%,#fff)}`. On phones: column, centered, gap 16, padding 26/20.
- Seal: an inline SVG, 120px (96 phone), `rotate(-8deg)`. A red circle (r 56), a white dashed ring (r 47, dasharray `3 4`), and text "90" (24px, 800), "DAYS" (11px, 1.5 letter-spacing), "FULL REFUND" (9px).
- h2 is `clamp(28px,3vw,38px)` with the kit's h2 underline hidden (`::after{display:none!important}`). `p` is 19px 700 (17 phone).

### C10. Founder story split with polaroids (CSS 39-49, 116-131, phone 238-245; HTML 369-421)
`.story-split` grid (A 1.9), `.side3 > .pols > figure.pol.p1/.p2 > span.tape + img.cover`, then `.mini-marquee`. `.s3-story > .beat[.flipbox|.moment|.gem|.circle]`. `.circle` (a dark box with `box-shadow:6px 6px 0 var(--accent)`) is only used by the rejected story versions and stays in the CSS. Set `object-position` per photo so faces stay in frame.

### C11. Built-in "challenge" visual, a stand-in until the real image exists (CSS 134-148; markup was generated in round 3, removed in round 7)
`.cal[role=img][aria-label] > .cal-phone` (290px, `#101017`, radius 34, 6px `#2a2a33` border, offset shadow) holds `.cal-notch`, `.cal-kicker` ("GAME TAPE · CHALLENGE", 10px `#FF6B63`), `.cal-title` ("30 DAY **FIRST SALE** CHALLENGE", 17px), `.cal-streak` (a red pill "DAY 7 STREAK"), `.cal-grid` (6 columns, cells `.d.done` red for 1-7, `.d.today` outlined for 8, grey for 9-30) and `.cal-miles` (dashed locked milestones with lock SVGs: "1,000 FOLLOWERS", "FIRST SALE"). A good pattern for any missing product visual.

### C12. Pain cards (`.traps`, CSS 50-56, phone 252-255; HTML 465-480). Values in A 1.11.

### C13. Footer wordmark (CSS 101-103; HTML 712-721)
`.wordmark{font-size:clamp(40px,12vw,148px);line-height:.85;letter-spacing:-.04em;color:transparent;background:linear-gradient(#d9d9de,#55555f);background-clip:text;white-space:nowrap;overflow:hidden}`. The footer logo `.gt-foot` is 150px.

### C14. Reduced motion (310-313)
`.vcar-track,.slider-track,.marquee-track,.alertbar .dot{animation:none}` and `.vcar,.slider,.marquee{overflow-x:auto}`.

### C15. Generator for repeated pieces (`tools/expand_body.py`)
It keeps the logo list, the video list (Cloudinary IDs plus alt text) and the screenshot list (file plus alt) in one place and writes the original set plus the `aria-hidden` duplicate set, so slider halves are always identical and there are no copy-paste slips. It asserts that no `@@` is left. **Gotcha:** if a token is removed from the source (`@@LOGOS@@`), don't assert that every token exists. The generator had to be relaxed after round 3.
