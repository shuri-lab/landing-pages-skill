# Stage 6: self-review (before anyone sees the page)

**How I looked (no browser pane in this test):** `tools/shoot.mjs` at mobile 393×852, 1280×800, 1440×900 and 1920×1080 (`shots/`), the full-page JPGs read in parts, plus a JS probe built on shoot.mjs (`dryrun/tmp/bin/probe.mjs`) for the checks stage 6 runs in the pane: fonts, slider halves vs box width, video state, CTA click → `#buy`, sticky bar, unloaded images, overflow finder. The bottom of the page was captured with a shoot.mjs variant (`--from 15500`) because shoot.mjs caps full-page shots at 16000 CSS px (the page is ~20,600 px on phones).

**Automatic:** `test/grade.py` 50/50, no hard fails (`grade.txt`). `check_page.py`: "OK: nothing that must be fixed" (only note: section 13 skipped by decision).

## Measurements (final build)
| View | h1 bottom | hero image | button | fine print | logo strip (`.press .marquee`) bottom | sideways px |
|---|---|---|---|---|---|---|
| Phone 393×852 | 280 | 497 | **762** | **793** | 931 (below fold, as on the reference) | 0 |
| 1280×800 | 357 | 557 | 598 | 635 | **757** (< 800 ✔) | 0 |
| 1440×900 | 380 | 572 | 622 | 658 | **780** (< 900 ✔) | 0 |
| 1920×1080 | 385 | 575 | 627 | 663 | 785 | 0 |
Hero button width on phone: 357 (full width at 393). Fonts loaded: Poppins 800, Lato, Caveat (all true).

## Section → issue → fix (phone and desktop)
| # | Section | Size | Checked (review-checklist item) | Issue found | Fix | Status |
|---|---|---|---|---|---|---|
| 1 | Hero | phone | A1-A2: alert 12.5px, pill 13.5px, h1 30px, lede 17/1.55, full-width button, fine 13.5px | First build: button bottom **791**, fine print ~822 (just under the fold edge, over the ~800 target). Cause: the stacked GT-B logo was 50px tall at 150px wide | Switched to the horizontal REC + GAME TAPE logo (21px tall at 150px; 190px on desktop). Button 791 → **762**, fine 822 → **793** | ✔ fixed |
| 2 | Hero | phone | A6 | The kit's floating "Edit layout" button sits over the fine print in every draft screenshot | It exists only in the draft `index.html`; the exported page (`export/index-final.html`, copied to `index-final.html`) has no editor. Shot the clean version too: `shots/final-export/` | ✔ (draft-only) |
| 3 | Hero | desktop | B8: two columns, mockup right ~700px at 1280, logo strip on first screen | none | none | ✔ |
| 4 | Logo strip | all | A4, B10: logos 40px phone / 42px desktop, grayscale; track half (853 / 1944 / 3916) > box (393 / 1280 / 1920) | none | none | ✔ |
| 5 | 2 Belief shift + outcomes (dark) | both | D23, D27: X/check statements, video carousel, 3 outcome cards each with a visual | none. Videos: all 10 cards readyState 4, muted, playing; half track 830 > 393 (phone), 1080 > 1040 (desktop) | none | ✔ |
| 6 | 3 Story | phone | house-style #16: headline → 2 photos side by side → logo slider → story beats | none; Best Buy photo first, face in frame (`object-position:50% 18%`) | none | ✔ |
| 7 | 3 Story | desktop | photos stacked and overlapping, column not sticky | none | none | ✔ |
| 8 | 4 Who it's for (sand) | both | A7 | none | none | ✔ |
| 9 | 5 Pain cards (dark) | both | D24: no 01/02/03, icon tile, bold lead, muted body, red punchline | none | none | ✔ |
| 10 | 6 What's inside | both | D23: one mockup per item, lessons numbered as text (F4) | Course image shows 7 lesson rows: matches the 7 lessons | none | ✔ |
| 11 | 7 Offer stack (sand, `#buy`) | both | C17, D25: dark head band + red pill, mockup, 3 rows with thumb + crossed "$57/$47/$97 value", "Total value: $201" bar, deal box with "You save $174" badge, "Today: just $27.", note, checkout button, trust row | none; only the 3 real items; no bump | none | ✔ |
| 12 | Guarantee | both | D26: own block, seal "90 DAYS FULL REFUND", "Your Money's Protected", one-sentence condition | none | none | ✔ |
| 13 | 8 Belief shift (dark) | both | A7 | none | none | ✔ |
| 14 | 9 Brother/friend | both | C16: text only, no invented results | Friend's pronoun: tool says "his hikes", Rickey's own words say "she" | Page says "her" (flagged for the client) | ✔ (flag) |
| 15 | 10 "Don't Take My Word for It." (sand) | both | D28: 10 real TikTok screenshots, compliance note | Slider half 1771 > 393, 2271 > 1080 at 1920 | none | ✔ |
| 16 | 11 Bigger implication (dark) | both | A7 | none | none | ✔ |
| 17 | 12 Hi, I'm Rickey | desktop | B9 "no big empty white areas" | Text column with white space on both sides (no photo: both photos are in s3 so none shows twice) | Proof list styled as 3 dark stat cards so the section has a visual anchor. Accepted | ✔ (accepted) |
| 18 | 14 Close (sand) | both | house-style #6: transparent mockup reused | none | none | ✔ |
| 19 | Footer | both | D29: logo, earnings disclaimer, TikTok non-affiliation, refund policy, ©, gradient wordmark | Kit default footer text color is the light red `on-dark-2` (hard to read in long paragraphs) | Footer text set to #C9C9D1 (11.5:1) | ✔ fixed |
| 20 | Sticky bar | phone | A5: hidden at top (false), shown mid-page (true), hidden at the offer after a CTA click (false); `footer{padding-bottom:110px}` | Full-page screenshots show the fixed bar at the viewport line (a capture artifact of shoot.mjs, not on the live page) | none needed | ✔ |
| 21 | CTA flow | all | C11-C12: 14 buttons, 1 label; hero click → `#buy` top = 0 (−1 at 1280) | none | none | ✔ |
| 22 | Overflow | all | A3: overflow finder returns nothing at every size | none | none | ✔ |
| 23 | Images | all | E30-E34: 0 broken, 0 unloaded, all WebP, 1.23 MB unique `src` weight | Channel mockup has a faint Jordan wings mark on a sneaker (E33) | Flagged; re-run prompt in `image-prompts.md` | ⚠ open (client) |
| 24 | Copy check | n/a | `check_page.py` 0 FIX; `grade.py` 154/154 copy lines; dashes 0; "steal" 0; templates/playbooks/bump/earnings 0; checkout placeholder count 1 | First grade showed 154/158: `grade.py` counts `>` note lines in copy.md as copy | Notes in copy.md changed to `<!-- -->` | ✔ fixed |

## Lines that are my wording (need the client's OK)
"Real product videos from my own TikTok." (s10) · "Brands Rickey has worked with" (logo strip label) · "A private WhatsApp channel." (s6, client fact in my sentence) · offer pill "One-time $27 · instant access", trust row, "Your Money's Protected", seal text · sticky label "Instant access · $27" · "My little brother" / "A friend" card tags · the whole footer (disclaimers drafted for approval).

## Still open (not blockers for the build)
- Checkout link: `PASTE-YOUR-CHECKOUT-LINK` on the one offer button (client: not ready).
- Red carpet photo license unconfirmed.
- Channel mockup: faint Jordan mark; DJI logo file has a faint "cleanpng" watermark.
- Disclaimers are drafts.
- No badge or sales-dashboard screenshot yet (the $4M+ and top-1% claims have no picture).

## Stage 8: speed (verified on the built page)
- All page images are WebP from `tools/optimize_images.py` (`images/opt/`, 1.57 MB for every variant on disk; originals 11.1 MB untouched in `images/`). `grade.py`: 1.23 MB over 30 unique `src` files, 30 WebP.
- Hero: `src` = 1280 WebP + `srcset` 720/1280, `fetchpriority="high"`, not lazy (the kit's build adds that to the first `<img>`). Everything else `loading="lazy" decoding="async"` with width/height. Slider images switch to eager near the screen.
- Measured full scroll with a CDP network probe (cache off): **phone 1,396 KB of images** (DPR 2 picks the 1280 variants; target ≤ ~1.5 MB ✔), desktop 1,187 KB. Fonts 105 KB.
- Videos: Cloudinary `w_320,q_auto:eco,ac_none,du_10,f_auto` (261-656 KB per clip, measured with curl), posters `w_320,so_1,f_auto,q_auto` ≈ 25 KB, `preload="none"`, `data-src` set only near the carousel, duplicates wait for the original. Desktop full scroll: 1,367 KB of video.
- Speed pass done before showing the client, as stage 8 asks.
