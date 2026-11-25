# Stage 6 of 9: Self-review (before anyone sees the page)

**Goal:** the client's first look already passes `knowledge/review-checklist.md`, so their feedback is about taste, not about things we already know.

**Why:** on the Rickey page, most of David's 12 rounds of feedback were the same kinds of fixes every page needs:
- fold fit
- text too small or cramped
- desktop neglected
- sliders running out
- one CTA label
- the offer stack structure

Catch them yourself.

## 1. Automatic checks

```bash
python3 PLAYBOOK/test/grade.py --page my-sales-page/index.html --copy my-sales-page/copy.md
node PLAYBOOK/tools/shoot.mjs my-sales-page/index.html --out my-sales-page/shots --views mobile,desktop,1280,1920 --full
```

- **What `grade.py` checks.** Fold fit at 393×852 and the desktop sizes, sideways scroll, broken images, one button label, button routing, dashes and banned words, placeholders, and image weight.
- **What `shoot.mjs` saves.** A first-screen PNG and a full-page JPG per view in `my-sales-page/shots/`.
- **If a check fails,** fix it and run both again.

## 2. Look at every section (both sizes)

**Two ways to look:**
- **Browser pane (best).** Serve the folder (`python3 -m http.server 8765 --directory my-sales-page`), open it in the pane, and resize to 393×852, then 1280×800, 1440×900 and 1920×1080. Walk every section with the prep snippet below.
- **No pane.** Read the full-page JPGs from `shoot.mjs` in parts (they're tall), and use `--views` for each size.

**For each section,** go through checklist sections A–E.

**Write the review down.** Put the findings in `my-sales-page/review.md` as a section → issue → fix table.

## 3. Fix, rebuild, re-check

- Fix everything, then run `tools/rebuild.sh` and both automatic checks again.
- Stop when the grade has no failures and the review table is all fixed.
- Only then open the page for the client: `open my-sales-page/index.html`, or the preview link.

## 4. Tell the client (short)

- What's on the page and what's still open, such as missing images.
- The measured fold numbers, e.g. "the phone hero ends at 764 of 852".
- **Which lines are your own wording,** for their OK.

---

## The review method we used on the Rickey page (exact snippets)


1. **Serve and size:** the local server is at `http://localhost:8765/`. Browser pane: `resize_window` to **393×852** (iPhone 16), then **1280×800** (and 1280×860 in round 1), **1440×900** and **1920×1080**. Finish with `resize_window {preset:"desktop"}`.
2. **Prep JS before measuring or screenshotting:**
   ```js
   await document.fonts.ready;
   document.documentElement.classList.remove('anim');          // kill reveal animations
   document.documentElement.style.scrollBehavior='auto';       // instant jumps
   [...document.querySelectorAll('button,div,a')].filter(e=>/Edit layout$/.test(e.textContent.trim())&&e.textContent.trim().length<16).forEach(e=>e.style.display='none'); // hide kit editor button
   document.querySelectorAll('img').forEach(i=>i.loading='eager'); // so jumped-to images paint
   window.__go=(s,d)=>{const e=typeof s==='number'?document.querySelector('section[data-section="'+s+'"]'):document.querySelector(s);window.scrollTo(0,e.getBoundingClientRect().top+scrollY+(d||0));return e.offsetHeight};
   ```
3. **Above-the-fold measurement:** `const b=e=>Math.round(document.querySelector(e).getBoundingClientRect().bottom)`, then compare `b('.hero h1')`, `b('.hero-img')`, `b('.hero .lede')`, `b('.hero .btn')` and `b('.hero .fine')` against `innerHeight`. Also check `offsetWidth` of `.hero .btn` (357 = full width at 393).
   - Phone targets and results: round 1 btn 632 / fine 659; round 2 onward btn 764 / fine 795 (accepted).
   - Desktop: 1440×900 btn 697-698, hero bottom 764-798. At 1280×800, `.press .marquee` bottom must be < 800 (773 → 753). Hero image width ≈ 700 (596 → 701).
4. **No sideways scroll:** `document.documentElement.scrollWidth === innerWidth` at every size. This caught the 2051px overflow from the section 3 slider. Also check the width of the suspect column (`.side3` = 387).
5. **Component checks:**
   - Sliders: for each track, `scrollWidth/2` must exceed the container `clientWidth` (logged at 1920). For the video carousel, compare `[.vcar.clientWidth, track.scrollWidth/2]`.
   - Spacing: `r('.s3-story').top - r('.mini-marquee').bottom` = 46.
   - CTA flow: `[...new Set([...document.querySelectorAll('a.btn')].map(a=>a.href))]` must give exactly one link, the checkout (or the placeholder before it exists). With the real link, click the hero button and the sticky bar button: both must land on the checkout. Then scroll to `#buy`: `.stickybar` must not have `show`.
   - Images: count `[...document.images].filter(i=>i.loading!=='lazy'&&!(i.complete&&i.naturalWidth>0)).length` (should be 0). Check `naturalWidth` of specific images (`.feature img`, `.pols img`).
6. **Screenshots:** at scale .45-.6. Section-by-section `__go(n, offset)` walks, `zoom` on regions for detail, and a wait of 1-2s after each jump.
7. **Copy and content checks:** after every build, `check_page.py` (the copy must match `copy.md`; it flags `{FILL IN}` and `.ph` placeholders) plus greps for dashes (`—`/`–`) = 0, "steal" = 0, removed items = 0, and checkout placeholders = 0 (or every button, while the link doesn't exist yet).
8. **Close the loop:** run `open my-sales-page/index.html` so the client sees the new version, append the rules to `learned-rules.md`, and in the wrap-up list each change with its measured numbers and mark any line Claude wrote itself ("this is my wording, needs your OK").
