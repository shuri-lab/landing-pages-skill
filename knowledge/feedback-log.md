# Feedback log: every round of David's feedback on the Rickey page

What David said → the general rule for any page → how it was built → how it was checked. Three parts, in order:
1. Copy intake, brand, first builds (messages #1–#19)
2. The big feedback rounds (mobile, desktop, reference page, offer stack, sliders, guarantee, founder story, AI images)
3. Sharing, speed, checkout, order bump, upsell

The rules distilled from this log live in `copy-rules.md`, `house-style.md`, `design-rules.md` and `review-checklist.md`. Read this when you want to know **why** a rule exists.

---

# Part 1: Copy intake, brand, first builds
> In this list, "Lesson" means the general rule for any future sales page.

### #1 (15:38Z) Zip attached: "run the start here file"
- **Claude did:**
  - Ran `unzip -l`, then extracted to `kit-source/`, excluding `__MACOSX/*` and `*.DS_Store`, and read `HOW-TO-START.md`.
  - Ran `cp -R ".../sales-page-generator-kit" sales-page`. This puts `START-HERE.md` and `kit/` side by side, plus `MAKE-YOUR-PAGE-LOAD-FASTER.*` and `all-brand-palettes.pdf`.
  - Ran `mkdir -p my-sales-page/images` and `python3 --version` (3.9.6).
- **What the zip contains:**
  - `HOW-TO-START.md/.html`, headed "DRAFT for Isabelle to review".
  - `START-HERE-SINGLE-FILE.md` (154 KB): the instructions plus every kit file under a "KIT FILES" heading, for chats that can't take a folder.
  - `all-brand-palettes.pdf` (1.4 MB) and `palettes/` (42 palettes in several PDFs and HTML files).
  - `MAKE-YOUR-PAGE-LOAD-FASTER.html`, and the kit as a folder and as a `.zip`.
- **What the kit contains:**
  - `1-copy/`: `questions.md`, `structure.md`, `voice.md`
  - `2-brand/`: `_template.md`, plus `examples/coral-teal.md` and `examples/sunkissed.md`
  - `3-images/`: `image-slots.md`
  - `4-build/`: `base.css`, `build_page.py`, `check_page.py`, `editor.css`, `editor.js`, `example-body.html`, `export_final.py`, `font-fallbacks.json`, `make_bundle.py`, `reference-phrases.txt`, `sections.md`
  - `5-publish/`: `publish-guide.md`
- **Outcome:** Claude said "Ready. Step 1 of 5: your copy." and asked one question ("Do you already have the copy?") with two buttons.
- **Lesson:**
  - Step 0 is quiet setup. Keep the kit pristine: copy it, never edit it.
  - On Nov 19, Claude also grepped the kit's `.py` files for imports, `urllib`, `socket`, `subprocess`, `os.system`, `rmtree`, `remove` and `unlink` before running anything. Result: "standard library only, no network or deletion". Keep that habit for any zip from outside.
  - The work lived in a scratch workspace. Start in a durable folder instead.

### #2 "Yes, I'll paste it"
- **Claude did:** read `kit/1-copy/structure.md` before receiving the copy. It then asked for the full copy, plus the product name, price, checkout link and publishing platform "if you know them".
- **Lesson:** load the 14-section structure first, so the mapping can come back in the same turn as the copy.

### #3 Copy file: "Offer 1 - Sales Page Copy (Buy-Now tool v1).md"
- **Claude did:**
  - Copied the file **untouched** to `my-sales-page/copy-original.md`.
  - Mapped it to the 14 sections in three groups:
    - **Covered and following the structure:** 2, 3, 4, 5, 8, 11, 14.
    - **Covered but not following it:**
      - Section 1: 5 headlines and 3 subheadlines to pick from. No "Steal my…" opener and no "No ___ required!" line, which is optional.
      - Section 6: the from-to line ("wait… how does the money even move?" → "oh. THAT'S how it works.") sits inside the course item instead of opening the section.
      - Section 12 repeats facts from section 3 (Best Buy shirt, $50/day, Nike + Subway, one-man crew). Claude didn't change this without being asked.
    - **Gaps:** section 7's `[total value]`; section 9's screenshots and the `[Customer name…]` placeholder; sections 10 and 13, which are all placeholders.
  - Listed what won't go on the page: the review notes, the framework note, the traffic note, and the hero image description (kept for Step 3).
  - Pulled the known facts out of the copy (TikTok Shop Headstart, $27, tasteofreedom.com, the Game Tape colors) and listed what was still missing (checkout link, platform).
- **Outcome:** `copy.md` was held back until the hero was picked. Claude asked one question with buttons "Use 1 + A" and "Different combo".
- **Lesson:**
  - Copy from Isabelle's "AI Sales Page Tool" (Buy-Now Sales Page) arrives with options, ⭐ picks, review notes, a framework note, a traffic note (cold traffic: headline 2 or 4; warm traffic: headline 1 or 3) and `[Insert: …]` slots.
  - Resolve every option to one line and strip every note before writing `copy.md`.
  - Then ask about one gap per turn, in page order.

### #4 "Use 1 + A"
- **Claude did:** confirmed the hero:
  - Eyebrow: "RICKEY · $4M+ in TikTok Shop sales · top-1% creator"
  - H1: "Get Your First TikTok Shop Sales in the Next 30 Days — Starting From Zero"
  - Subheadline A
  - Button: "START MY 30 DAYS — $27", with the risk-reducer line under it
- **Next gap:** the section 7 price anchor. Claude offered two choices: a real total value (shown struck through) or drop the line.
- **Lesson:** the kit says "Never invent a value for each item". The default offer is "give me a real number, or we drop it".

### #5 "make up the total value… like $57… the guide $29 and the private channel $97… add them up"
- **Claude did:** proposed this table:

  | Item | Value |
  |---|---|
  | The 7-Day Headstart Course | $57 |
  | The 30-Day First Sale Challenge + both milestone playbooks | $47 |
  | The templates (idea lists, hook starters, product check + daily loop) | $29 |
  | My Private Channel | $97 |
  | **Total value** | **$230** |

  - The challenge got $47 "because it's the main daily tool, so it sits between the course and the templates".
  - Display: "✔ The 7-Day Headstart Course — $57 value", then "Total value: ~~$230~~", then "Today: just $27."
  - Guardrails Claude stated:
    - "These are numbers you chose, so make sure you're comfortable standing behind them."
    - Keep the word "value". Avoid "regular price" and "was $230", because those imply it actually sold at that price.
    - The $17 Starter Product List add-on stays as its own line and isn't counted.
- **Lesson:** when the client explicitly tells you to invent anchor values:
  1. Make each value proportional to the item's role.
  2. Call it "value", never a former price.
  3. Leave add-ons out of the stack total.
  4. Write the decision into `learned-rules.md` and the `copy.md` header.
  5. **First check that every listed item is really in the offer.** This one wasn't (see F1).

### #6 "we dont have testimonials or reviews yet"
- **Claude did:**
  - Said out loud that it read this as a yes: "I'll take that as a yes on the values ($230 total). Tell me if you want to change any of them."
  - Listed the proof David already had:
    - Rickey's top-1% badge, sales dashboard and first-sale notification.
    - The brother's and friend's stories (camera promo, hike page growth).
  - Explained the cost: proof is what makes a stranger believe, and without it the page leans on Rickey's results and the 90-day refund.
  - Gave 3 options:
    1. **Use the proof you have (recommended).** Section 9 keeps the brother and friend stories with their screenshot spots, and `[Customer name…]` comes out. Section 10 becomes Rickey's own screenshots, but its headline "Wait… This Actually Works for People Like Me?" doesn't fit owner results, so it needs a new one. Section 13 is skipped.
    2. **Skip sections 9, 10 and 13.**
    3. **Keep them as placeholders,** but only if David won't publish until real wins exist.
- **Lesson:** this is the kit's proof-gap script, and it works. The headline has to match the proof type: owner results are not "people like me".

### #7 "1 ok"
- **Claude did:** offered 3 section 10 headlines built only from facts in the copy:
  - "Don't Take My Word for It. Here's the Scoreboard." This ties back to the 2K scoreboard in section 8.
  - "The Receipts: $4M+ in TikTok Shop Sales"
  - "Real Numbers. Real Screenshots. No Filters."
- It also proposed putting section 12's compliance line under the screenshots: "Those are my results, so you can see it's real. Not a promise of what you'll make." The button stays "YES, LET'S GO →".

### #8 "just use Don't Take My Word for It. and we will later on ask Rickey for sales numbers screenshots"
- **Claude did:**
  - Turned the task list into 5 steps.
  - **Read `check_page.py` before writing `copy.md`,** to learn which line formats the checker matches.
  - Wrote `copy.md`:
    - 3 header comments recording the decisions (hero 1 + A; values $57/$47/$29/$97 = $230 chosen by the client; section 10 is Rickey's proof; section 13 skipped).
    - `## SECTION N` markers and one page element per line.
    - Buttons as `[BUTTON: …]` lines.
    - Image slots as `> image: …` notes, which the checker skips.
    - Section 13 as `<!-- SECTION 13 skipped until student wins come in. -->`.
  - Read the brand `_template.md` and `coral-teal.md`.
  - Asked about the brand source with buttons "Game Tape colors" and "I'll upload an image". It also listed (a) build from the Game Tape colors already named in the copy, (b) upload a brand image, (c) upload a palette pick from `all-brand-palettes.pdf`.
- **Lesson:** the checker's matching rules decide the `copy.md` format (see C, Tooling). Put the client's decisions in the header so the next session knows why the copy looks the way it does.

### #9 "I'll upload an image"
- Claude listed what works (logo, REC mark, brand board, page screenshot, palette card) and what it would do with it: sample colors, match fonts to Google Fonts, check contrast, show the palette with each color's job.

### #10 "You have full access… folder 'Rickey-TikTokShop-Project-Files'… branding… colors… images, screenshots, brand logos"
- **Claude inventoried the folder** with `find -maxdepth 3`. In `branding/`:
  - `GT-B.png`, `GT-black.png`, `GT-white(RR).png`, `GT-white.png`, `REC-black-red.png`, `REC-white-red.png`, all 3600×3600 with lots of empty space.
  - `Game Tape Brand Guidelines.pdf` (11.8 MB).
- **Rendering the PDF took three tries:**
  1. `pdftotext`/`pdftoppm` weren't installed, and the Read tool can't render a PDF without poppler.
  2. A Swift PDFKit script failed with an SDK/compiler mismatch (`cannot suppress '~Copyable'…`).
  3. **A JXA script (`osascript -l JavaScript`) using PDFKit worked.** It rendered every page to PNG at 1400 px wide and dumped the text layer.
- **From the text layer** came: RED #D30805, BLACK #101017, WHITE #FFFFFF, heading face Archivo Black, subtext face Poppins. The logo typeface is "210 슈퍼 사이즈" (210 Super Size), which is not a Google Font and wasn't used.
- **Pages Claude viewed:** 6 (logo systems), 8 (typeface) and 9 (closing page). Page 7, the colors page, was never opened as an image. The hex codes came from its text.
- **Logos:** previews made with `sips -Z 400`.
- **Contrast:** Claude ran a WCAG ratio calculation in Python for 12 pairs (see E).
- **Kit internals:** read `build_page.py`: the role regex, the required roles, and how fonts are parsed.
- **Fonts:** checked availability with `curl` against `fonts.googleapis.com/css2?family=Archivo+Black…` (200) and grepped `font-fallbacks.json` (Archivo Black and Poppins are listed).
- **Wrote `brand-kit.md`** (now `brand-kit-v1.md`). It showed the palette as markdown tables ("From the brand guide" / "Added by me"), the fonts (Archivo Black, Poppins, Permanent Marker), readability notes, and the logo plan (cropped copies under new names, originals untouched). Then it asked "Does this palette feel like Game Tape?".
- **Lesson:**
  - When the client grants folder access, inventory the folder before asking for uploads.
  - A brand guide's text layer is the most exact source of hex codes and font names.
  - **Ask for the project folder at Step 1** (see G).

### #11 "I cant see the colors just #D30805 numbers"
- **Claude did:** loaded the visualize mockup module and rendered `show_widget` "game_tape_brand_palette":
  - Swatches for the 3 brand colors and 4 helpers, each with name, hex and job, using the real Google Fonts.
  - A mini page preview: a white section with a red accent word, a highlighter mark, the red button and a handwritten note; then the grey band; then a black section.
  - It asked again, with examples of changes David could request ("less red", "warmer grey").
- **Lesson:** never present a palette as hex codes alone. Show swatches **and** a mini page using them. In Claude Code CLI without the visualize widget, write a small `palette-preview.html` and run `open` on it.

### #12 "yes" (Step 3, images)
- **Claude did:**
  - Read `image-slots.md` and listed every project image with its size from `sips -g pixelWidth -g pixelHeight` and `du -k`.
  - Made 700 px JPEG previews in the scratchpad (`sips -Z 700 -s format jpeg`) and **looked at every one**: 10 TikTok screenshots, 5 product-check screenshots, the 4 offer images and the 6 brand logos.
  - Rendered the first 3 pages of each Offer 1 deliverable PDF with a page-limited JXA script (`pdf2png-n.js`). The Course Deck has 35 pages; the 30 Day First Sale Challenge has 10; the Starter Product List was also rendered.
- **The placement table:**

  | # | File | What it is | Section | Confidence |
  |---|---|---|---|---|
  | 1 | `offer-1-image-v2.png` | Headstart mockup (book cover, laptop "How a sale happens", phone with Rickey's TikTok) | 1 Hero | High |
  | 2 | same | repeated at the close | 14 | High |
  | 3 | Course deck PDF cover | 7-Day Course cover | 6 course card | Medium |
  | 4 | 30 Day Challenge PDF cover | black and red cover | 6 challenge card | High |
  | 5 | `Product check 1.png` + `3.png` | TikTok Shop product page + "Earn $2.27–4.16 per sale" panel (Old Navy henley) | 6 templates card | Medium |
  | 6 | Starter Product List cover | cover with 5 product thumbnails | 7 $17 add-on line | High |
  | 7 | 4 TikTok screenshots (red shoes, pocket knife, Puma BMW shoes, red jacket) | Rickey's own product videos | 3, as a row under "show, don't tell" | Medium |
  | 8 | `GT-B.png` / `GT-white(RR).png` | stacked logo, black and white | top + footer | High |
  | — | placeholders | brother's results, friend's page growth | 9 | marked boxes |
  | — | placeholders | top-1% badge, sales dashboard, first sale | 10 | marked boxes |

- **Flagged and not placed:**
  - ⚠️ `rickey.jpg` is a **Getty Images** photo with the watermark and photographer credit printed on it. It can't go on a sales page unless licensed.
  - `brands-logos/` holds Casio, DJI, McDonald's, Meta, Puma and Subway. The copy only names Nike, Subway and Temu. A logo strip claims a real partnership, so Claude asked which brands Rickey actually worked with.
  - The Offer 2, 3 and 4 images are other products ($4M System, TikTok Shop Builders, 1-on-1).
  - 5 more TikTok screenshots went unused: watch, LA hat, drone, red shoes on the floor, toy blaster.
  - `website-footer-design.png` is a design reference, not a page image. The footer was styled after it.
  - The 5 `.mp4` videos weren't used, because they'd be "heavy to paste into a builder".
- **Checks:** no buyer PII in any image. The product check shows an Old Navy listing. Every image would be copied into `my-sales-page/images/` with clear names and the originals left untouched. David could change any row by number.
- **Lesson:**
  - Read the text inside every image.
  - Number the table so the client can answer by number.
  - Flag licensing (watermarks), implied endorsements (logo strips) and other-product images.
  - Propose a role for leftovers instead of silently dropping them.

### #13 Numbered answers
David's answers: (1) use "rickey-photo"; (2) use the brand logos anyway; (3) OK on dropping the other offers' images; (4) put the other TikTok screenshots in a slider and use the TikTok videos "in autoplay muted" like the reel in "Learn it from someone who actually sells." on gametape-blue.vercel.app/offer-first-seven, and "make the videos lighter… but I want those videos"; (5) OK on the footer reference.

**Finding the assets:**
- Found `PF/rickey-photo.jpeg` (1556×2048, 348 KB).
- Checked the video tools: no ffmpeg or ffprobe; `/usr/bin/avconvert` is available.
- The 5 videos, read with `mdls`:

  | File | Size | Length |
  |---|---|---|
  | `Download.mp4` | 9.0 MB | 55.4 s |
  | `Download_3.mp4` | 7.7 MB | 23.0 s |
  | `Download_4.mp4` | 7.0 MB | 40.8 s |
  | `Download_5.mp4` | 7.7 MB | 66.6 s |
  | `Download_6.mp4` | 12 MB | 57.4 s |

**Reverse-engineering the reference page** in the Browser pane:
- `find` located the heading. JavaScript then read the section's videos: autoplay, muted, loop, 220×391 cards, sources on `res.cloudinary.com/fje4fcoe/video/upload/v…/Download*.mp4`.
- The track had class `reel-track reel-up` and animation `40s linear infinite reelUp`.
- **So the same videos were already hosted on Cloudinary.**

**Making the videos lighter without ffmpeg:**
- The Cloudinary URL transform `w_360,q_auto,ac_none,du_12` returns 914,710 bytes instead of 9,478,254: 12 seconds, 360 px wide, no audio, about 0.9 MB instead of 9.5 MB.
- Poster and preview stills come from `.../video/upload/w_240,so_1/<id>.jpg`, where `so_` is the start offset in seconds.
- Claude viewed one still per video: Batarang knife, jewelry chain, "These Won't Last!" denim, camera lens filter, Madden TV setup.

**Reading the kit's layout rules:** `sections.md`, `example-body.html` (for structure only, never its words), `base.css`, `reference-phrases.txt` and the editor hooks.

**Copying the images:**
- Logos: pure-Python PNG bounding box (`bbox.py`) on 1200 px copies, then `sips -c H W --cropOffset Y X`. Output:
  - `logo-gametape-black.png` 852×124
  - `logo-gametape-stacked-black.png` 791×265
  - `logo-gametape-stacked-white.png` 791×265
- PDF covers converted to JPEG at quality 82 (`sips -s format jpeg -s formatOptions 82`).
- New names: `hero-headstart-mockup.png` 1672×941 (1.9 MB), `rickey-photo.jpg`, `product-check-listing.png` 388×827, `product-check-earnings.png` 371×822, `course-deck-cover.jpg` 1200×674, `challenge-cover.jpg` 1200×1695, `starter-product-list-cover.jpg` 1200×1695, `tiktok-*.jpg` 946×2048 (×10), `brand-*.png` (×6). 26 images in all.

**Before writing the page:** checked how `export_final.py` handles images and videos (`--images keep|embed|urls`; embed stays under about 2.5 MB). The videos load from Cloudinary, so they add almost nothing to the paste-ready file.

**Writing `body.html`:** with a commented `<style>` block listing why each extra style exists (the kit allows this): the video reel (section 3), the TikTok screenshot slider (section 10), the brand logo strip (section 12), the top logo, side-by-side screenshots (section 6), the add-on row (section 7) and the big footer wordmark.

**Build and check:**
- Run: `python3 kit/4-build/build_page.py --body my-sales-page/body.html --kit my-sales-page/brand-kit.md --out my-sales-page/index.html --title "TikTok Shop Headstart | Game Tape" && python3 kit/4-build/check_page.py --page my-sales-page/index.html --copy my-sales-page/copy.md`
- First report:
  - FIX: `{FILL IN: your disclaimers…}`.
  - FIX: 7 copy lines missing. The lesson numbers were `<ol>` markers, not text.
  - NOTE: the duplicate slider images had empty alt text.
- Fixed with a Python transform: visible "1. …" text in `<li>`, `ol.lessons{list-style:none}`, and the duplicates given the same alt text plus `aria-hidden="true"`. After that only the `{FILL IN}` FIX remained (expected), plus NOTEs for 5 `ph` boxes and section 13 missing.

**Preview server:** `.claude/launch.json` running `python3 -m http.server 8765 --bind 127.0.0.1 --directory sales-page/my-sales-page`, started with `preview_start "sales-page"`.

**Visual QA, and what it fixed:**

| Problem found | Fix |
|---|---|
| Section 3: the long story left the reel floating mid-column with empty space above it | `.reel{position:sticky;top:48px}` and `align-items:start` |
| At narrow width section 3 stayed 2 columns, because the custom grid rule overrode the kit's phone layout | `@media (max-width:820px){.split.reel-split{grid-template-columns:1fr} .reel{position:relative;top:0;height:520px}}` |
| The course card image (the deck's opening slide) was mostly white and looked thin | Rendered all 35 slides, made a 5-column contact sheet with JXA/AppKit (`sheet.js`), picked **slide 3** (the dark "Lesson 1: How TikTok Shop works, and start posting" title slide), saved as `course-lesson-1-slide.jpg` 1200×674 |
| Desktop 1280×860: the footer "GAME TAPE" wordmark was cut off | `font-size:clamp(64px,17vw,230px)` → `clamp(40px,12vw,148px)` |
| Slider images further along the strip never loaded: lazy loading ignores off-screen transformed items | IntersectionObserver (`rootMargin:'600px 0px'`) sets `loading='eager'` on the slider images |
| Phone 375×812 | Checked `scrollWidth`=375, no element's right edge past the viewport (sliders excluded), every image loaded |

**Wrap-up for this round:**
- Reset the viewport to desktop.
- Wrote `learned-rules.md` (first 6 lines: values, proof plan, founder photo, logos, light videos via Cloudinary, all screenshots in a slider).
- Final check, plus `grep -c 'PASTE-YOUR-CHECKOUT-LINK' body.html` → 13, and `grep -ci 'isabelle\|tasteofreedom\|buy-now'` → 0.
- Reported:
  - What was built.
  - What's still open: checkout link on 13 buttons, footer disclaimers, 5 proof spots.
  - Flags: `rickey-photo.jpeg` "looks like a crop of the same Getty Images photo… cropping out the watermark doesn't make it licensed"; the logo strip implies partnerships; two videos show commenters' names ("Joel Moreno", "KayKay").
  - How to use "Edit layout" and "Save draft".
  - Asked for the checkout link (buttons "I'll paste it" / "Not ready yet").

**Lesson:**
- Before deciding how to slim down media, check whether it's already on a CDN that transforms by URL.
- Reverse-engineer a reference component from its DOM and computed CSS. Don't guess.
- QA every build at 1280 and 375.
- Fix what the screenshots show before you report.

> Transcript note: "#14", an image of 3060×2674, is **not** a user message. It's the contact sheet of the 35 deck slides, which the transcript logged as a user turn.

### #15 "checkout is not ready yet, open the page on my browser"
- **Claude did:** ran `open "my-sales-page/index.html"` (file://), and said:
  - Fonts (Google Fonts) and videos (Cloudinary) need an internet connection.
  - "Edit layout" and "Save draft" work there too.
  - The buttons go nowhere yet.
- **Lesson:** the file works from disk because image paths are relative. After every change round, reopen it and tell the client to refresh.

### #16 The 9-point feedback round (16:21Z)
David's points:
1. No dashes "—" anywhere.
2. The hero image goes below the headline.
3. No "steal".
4. Rickey's photo and the brand logos also go in the "How I Went From a Best Buy Shirt…" section.
5. Remove "· do the 30-day challenge and if you haven't made a sale in 90 days, full refund." from under the CTA buttons.
6. A carousel of Rickey's videos in "You Don't Need Another Video About TikTok Shop…".
7. More black sections, "so the page doesnt look like one continuos section".
8. "You Need to Post Your First One." becomes "You Need to Start Posting."
9. Test new fonts: Poppins for big text, Lato for small text, Caveat for handwritten.

**Backups and dashes:**
- Backed up first: `copy-v1.md`, `brand-kit-v1.md`, `body-v1.html`, `index-v1.html`.
- Ran `grep -n '—\|–' copy.md`.
- Applied a Python list of replacement pairs to `copy.md` and `body.html` (14 and 13 replacements):
  - "in the Next 30 Days — Starting From Zero" → "in the Next 30 Days, Starting From Zero"
  - "over $4M in sales — set up" → "over $4M in sales: set up"
  - "START MY 30 DAYS — $27" → "START MY 30 DAYS FOR $27"
  - "230–240 pounds" → "230 to 240 pounds"; "3–5 hours" → "3 to 5 hours"; "(5–8 min each)" → "(5 to 8 min each)"
  - "Course — $57 value" → "Course ($57 value)", and the same for $47, $29, $97
  - "STEAL MY HEADSTART FOR $27" → "GET MY HEADSTART FOR $27"
  - "You Need to Post Your First One." → "You Need to Start Posting."
  - The hero fine print, both apostrophe variants (' and ’), → "One-time $27 · instant access"
  - The `copy.md` header comment dash → comma

**Layout script:** the first attempt crashed on a regex before writing anything (by design). It was fixed and saved as `S/tools/layout2.py`:
- The hero figure moves right under the `</h1>`, with `margin:10px auto 34px`.
- Section 2 becomes `s-dark`.
- The 5 unique videos move into a horizontal carousel `.vcar` after the statement lines (after "Ohhh. I can actually do that. Tonight."). It has 5 cards plus 5 `aria-hidden` duplicates and replaces the vertical reel in section 3.
- Section 3 becomes `.split.story-split` (`.8fr 1.2fr`) with a sticky side column `.side3`: the polaroid at `rotate(-3deg)`, `max-width:340px`, plus `.logos.mini`, a 3-column grid of 30 px logos.
- Sections 8 and 11 become `s-dark`.
- CSS for white cards inside dark sections: `.s-dark .outcome p,.s-dark .claim p{color:var(--ink)}` and `.s-dark .maybes{color:var(--on-dark-2)}`.

**Fonts:** `brand-kit.md` Fonts block now reads "Font test requested by the client on Nov 20 (the brand guide uses Archivo Black + Poppins; that version is saved in brand-kit-v1.md)", with `- Big: Poppins 800`, `- Standard: Lato`, `- Handwritten: Caveat`. Claude confirmed "Lato" and "Poppins" are in `font-fallbacks.json`.

**Learned rules:** appended 9 lines.

**QA:**
- Fonts confirmed with `document.fonts.check('800 16px Poppins')`, `('16px Lato')` and `('16px Caveat')`, all true.
- Desktop at 1280×860 checked section by section.
- **Phone: `scrollWidth` was 411 on a 375 viewport.** The carousel kept its `margin:34px -18px 30px` edge-to-edge margin after moving outside the column. Fixed to `margin:34px 0 30px`.
- Checked the carousel videos play: `muted:true, paused:false, readyState:4, error:null`.
- Final: `check_page` clean apart from `{FILL IN}`; `dashes: 0 steal: 0`; reopened in the browser.

**Report:** Claude answered per numbered point and disclosed one extension: number ranges with a shorter dash ("3–5 hours") were changed too ("Say if you'd rather keep those as they were").

**Lesson:**
- Treat numbered feedback as a numbered checklist.
- Back up before touching anything.
- Write all the replacements as one explicit list.
- Verify with grep counts.
- Report per number and disclose anything you did beyond the literal request.

### #17 Alert bar "One-time $27 · instant access"; pill without "RICKEY"
- **Claude did:**
  - Python edit of `body.html` and `copy.md`.
  - Inserted `<div class="alertbar" role="note">One-time $27 · instant access</div>` before SECTION 1, outside any section.
  - Alert bar CSS: `background:var(--dark); color:var(--on-dark); text-align:center; font-family:var(--font-body); font-weight:700; font-size:14px; letter-spacing:.06em; text-transform:uppercase; padding:11px 16px; border-bottom:3px solid var(--hi)`.
  - Pill now reads "$4M+ in TikTok Shop sales · top-1% creator".
  - Added the alert text as the first line under `## SECTION 1` in `copy.md`, so the checker covers it.
  - Appended to `learned-rules`, rebuilt, took a screenshot, reopened.
  - Asked a non-blocking question: "Remove the matching line under the hero button?"
- **Lesson:** every new piece of on-page text goes into `copy.md` too. When a change creates a duplicate, ask before removing it.

### #18 "Keep both"
- Claude confirmed, then restated what's still open (checkout link, disclaimers, 5 proof screenshots, platform).

### #19 New subheadline (it contained an em dash)
- **The new text:** "Follow the same plan behind Rickey's $4M+ in TikTok Shop sales — a 7-day course on how to find winning products, make viral videos, and make sales, plus a 30-day plan that walks you there, one video a day. No following, no camera experience, no guessing what to film."
- **Claude did:**
  - Replaced the em dash with a colon, applying the no-dash rule.
  - Moved the kit's `.pss` emphasis (bold, italic, underline) to "one video a day".
  - Updated `copy.md` (curly ’ → straight '; the checker normalizes punctuation) and `learned-rules`.
  - Verified the `.lede` text and that there's no overflow, then reopened the page.
  - Explained the colon and offered a period or comma instead.
- **Lesson:**
  - When client text breaks a standing rule, apply the rule, say so, and offer alternatives.
  - **The emphasis carry-over was wrong.** At #20 David said: "I wouldn't highlight one video a day… I would highlight behind Rickey's 4 million… find winning products, make viral videos, and make sales." Highlight proof and the main benefits, not the mechanics. Ask when the emphasis isn't obvious.

---


---

# Part 2: The big feedback rounds

## A. Feedback log

Format for each item: **David's words** → *General rule* → **Implementation** → **Verification**.

### Round 1: the long walkthrough (mobile-first, JJ page, images)

**1.1** "the page has to be mobile first because 90% of the people… are gonna be on mobile… be very, very thorough"
- *Rule:* Design and check at phone size first (iPhone 16, 393×852), then desktop. Phone rules go last in the CSS so they win.
- **Impl:** `body-src.html` was rewritten from scratch. The extra `<style>` header says "Mobile first: the phone rules come last and win." Everything for phones lives in `@media (max-width:820px)` (final lines 202-268). Section padding on phones is `section{padding:46px 0}` (the kit default is 96px).
- **Verif:** Section-by-section screenshots at 393×852 using the `__go(n)` jump helper (see D). `document.documentElement.scrollWidth` = 393, so there's no sideways scroll.

**1.2** "too much space… it should fit in the screen before the fold… headline, hero image, subheadline, and… the CTA button… in a iPhone 16"
- *Rule:* On 393×852, the alert bar, logo, proof pill, H1, hero image, subheadline, button and fine print all show before any scrolling.
- **Impl (round 1 values, later enlarged in 2.1):** alert bar 10.5px, logo 112px, pill 11.5px, h1 28px/1.1, lede 15px/1.45, button padding 15px 14px, fine print 12px, `.hero{padding:12px 0 28px}`, `.hero h1::after{display:none}` (removes the kit underline). The hero image sits first in the DOM so it loads first (`fetchpriority="high"`) but displays under the H1 via flex order: `.hero-wrap{display:flex;flex-direction:column;align-items:center}` with `.gt-logo{order:1}.trust{order:2}h1{order:3}.hero-img{order:4;width:100%}.lede{order:5}.cta{order:6}`.
- **Verif:** JS `getBoundingClientRect().bottom` measurements: h1 203, img 414, lede 554, btn 621 (632 after the image move), fine 648 (659) of 852. Claude noted that 659 "fits even with Safari's toolbars showing."

**1.3** "highlight the behind Ricky's 4 million TikTok shop sales… find winning products, make viral videos, and make sales… maybe in a different color… I wouldn't highlight one video a day"
- *Rule:* In the subheadline, mark the proof phrase with the highlighter and set the 2-4 key outcomes in bold brand color. Never highlight process details.
- **Impl:** `<mark>behind Rickey's $4M+ in TikTok Shop sales</mark>` plus `<span class="red">` on the three outcomes. CSS: `.hero .lede mark{font-weight:800}`, `.hero .lede .red{color:var(--hi);font-weight:800}`. The old `.pss` underline on "one video a day" was removed.
- **Verif:** Visual check in the mobile screenshot.

**1.4** "I want all the CTAs to be get instant access uh, $27… all of them"
- *Rule:* One CTA label everywhere: verb + price + arrow.
- **Impl:** `expand_body.py (was gen_body.py)` sets `CTA='GET INSTANT ACCESS · $27 →'` and replaces every `@@CTA@@`. There were 14 buttons: hero, sections 2, 3, 4, 5, 6, offer, 8, 9, 10, 11, 12, 14, and the sticky bar. Before this round there were 13 different labels ("START MY 30 DAYS FOR $27", "GIVE ME THE PLAN →", …).
- **Verif:** The generator prints `ok 14 buttons` on every build.

**1.5** "the next section being black… the three x's… looks a bit cramped… needs a little bit more space"
- *Rule:* Statement lists with icons need air: about 1.15-1.25em between lines and more space under the H2.
- **Impl:** `.s2 .stmt p{margin-bottom:1.15em;line-height:1.4}`, `.s2 .stmt .quote{margin:1.3em 0 .4em}`. On phones: `.s2 h2{margin-bottom:30px!important}` and `.s2 .stmt p{margin-bottom:1.25em}`. The H2 inline margin went from 48px to 44px.
- **Verif:** Mobile screenshot of section 2.

**1.6** "know exactly what to post… we need a few small TikTok screenshots from Ricky"
- *Rule:* Every outcome claim gets a visual right under it. When it's a proof claim, use real screenshots.
- **Impl:** Outcome markup became `.outcome > span.n + div > (p + .o-media)`. `.o-media{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:16px;max-width:360px}` holds 3 TikTok screenshots (946×2048), styled `border:1.5px solid var(--ink);border-radius:10px`.
- **Verif:** Screenshot, plus a check that no non-lazy images were left unloaded.

**1.7** "pick products that already sell… add the product checklist screenshots"
- *Rule:* Use the client's real screenshots of the method in action.
- **Impl:** `.o-media.two{grid-template-columns:repeat(2,1fr);max-width:260px}` (240px on phones) with `product-check-listing.png` (388×827) and `product-check-earnings.png` (371×822).

**1.8** "change this section… it has to tell them that they'll join a private… WhatsApp channel… give me the prompt for it"
- *Rule:* When Claude rewrites a client line, say so and ask for an OK. Placeholder images are fine in drafts but must be gone before going live.
- **Impl:** New outcome 3: "Join Rickey's private WhatsApp channel + watch your milestones stack up." (in round 7 it became "Join the Rickey Army, Rickey's private WhatsApp channel + …"). It shipped with a `.ph` placeholder inside `.o-media.wide` (1 column, max-width 420px), filled in round 2 with `whatsapp-channel.png` using `img.mock{border:0;background:none;border-radius:12px}`. Prompt 1 went into `image-prompts.md`.
- **Verif:** The wrap-up asked "Is the new WhatsApp channel line in section 2 good to keep?"

**1.9** "the headline has to be before Ricky's image… on mobile… before Ricky image and the logos"
- *Rule:* On phones, a split section must read headline first, then the media, then the body.
- **Impl:** `.story-split{display:grid;grid-template-columns:.8fr 1.2fr;grid-template-areas:"side head" "side story";column-gap:64px}`. On phones: `grid-template-columns:1fr;grid-template-areas:"head" "side" "story";row-gap:24px`.
- **Verif:** Mobile screenshot of section 3 (`__go(3,0)`).

**1.10** "this was built for you if section is okay" → no change.

**1.11** "watching other people win… text is a bit too small… I don't know why we need the numbers like 01, 02, 03… I like the dark background… I like the… maybe next month"
- *Rule:* No decorative index numbers on pain cards. Use a small icon, a big bold first line and a colored punchline, and make the text bigger.
- **Impl:** `.traps` grid (3 columns, 1 on phones) of `.trap` cards: `background:#1C1C26;border:1px solid #2E2E3A;border-left:5px solid var(--hi);border-radius:18px;padding:26px 24px`. Icon tile `.ti` is 44×44 with radius 12 and a 18% red tint; its SVG is 24px with `stroke:#FF6B63`. `p.lead` is white, Poppins 800, 21px (20px phone, 22px desktop). Body text is `#C9C9D1`, 18px/1.5 (17px phone). `p.hit` is `#FF6B63` weight 800. "Maybe next month" was kept.
- **Verif:** Mobile and desktop screenshots of section 5.

**1.12** "here's everything inside… we'll generate better images… reuse that AI WhatsApp channel image"
- *Rule:* Product feature images should be mockups in the same style as the main offer image. One AI image can serve two spots.
- **Impl:** Prompts 2-5 in `image-prompts.md`. The images went in during round 2 (see 2.10).

**1.13** "analyze that page… you can actually review the code… some of the things look cleaner"
- *Rule:* Study the reference page's structure and components. Never copy its branding.
- **Impl:** `gh` was not installed, there was no GitHub connector, and `mdfind` found no local clone. Claude studied the live page in the browser pane at 393×852 using JS: it listed sections with top and height, read computed styles of the hero children, pulled CSS rules out of `<style>` tags with a regex per selector (`.ly-announce`, `.ly-sticky`, `.ly-press`, `.ly-stack`, `.ly-mark`), and read the `outerHTML` of the sticky bar and deal box. See F.

**1.14** "I like the alert bar design with that gradient… has to be in our branding"
- *Rule:* The thin alert bar at the very top is a gradient from dark to the brand color.
- **Impl:** `.alertbar{background:linear-gradient(90deg,#101017 0%,#5C0503 52%,#D30805 100%);color:#fff;text-align:center;font-family:var(--font-head);font-weight:800;font-size:12px;letter-spacing:.09em;text-transform:uppercase;padding:8px 16px}`. A blinking "REC" dot: `.dot{width:8px;height:8px;border-radius:50%;background:#FF6B63;animation:rec 1.4s ease-in-out infinite}` with `@keyframes rec{50%{opacity:.25}}`. Text: "One-time $27 · instant access". (JJ's version: `linear-gradient(90deg,#5B2A80 0%,#7E36A6 48%,#C0468C 100%)`, 11px, 800, .08em, padding 5px 18px.)

**1.15** "on mobile, there's a pop-up bar that appears at the bottom once you scroll past the hero… stays fixed"
- *Rule:* A sticky CTA bar appears after the hero and hides while the offer stack is on screen.
- **Impl:** `.stickybar` (see C3). Markup: `<div class="stickybar" aria-hidden="true"><div class="sb-in"><span class="sb-lbl">Instant access · <strong>$27</strong></span><a class="btn" href="#buy" tabindex="-1">…</a></div></div>`. Two IntersectionObservers control it. `footer{padding-bottom:110px}` keeps the bar from covering the footer.
- **Verif:** Claude clicked `.hero .btn` and confirmed `#buy` top ≈ 0 and that `.stickybar` was not `.show`: "the sticky bar hides there."

**1.16** "the hero section is fully visible… before the fold" → same as 1.2.

**1.17** "JJ Smith has been featured in and those logos… Ricky has… collaborated with these brands… a slider"
- *Rule:* Put a brand/press logo slider right under the hero.
- **Impl:** `<div class="press"><p class="press-lbl">Brands Rickey has worked with</p><div class="marquee"><div class="marquee-track">@@PRESS@@</div></div></div>`. It holds 6 logos (Subway, Puma, McDonald's, Meta, Casio, DJI) plus 6 `aria-hidden` copies. CSS is in C2. The section 12 logo strip was removed because the logos now show in the slider and in section 3.

**1.18** "when you click get instant access, you go to this offer stack section… I like the offer stack design"
- *Rule (**replaced on Nov 24 by P4.9**: every button goes straight to checkout):* Every CTA jumped to the offer stack (`#buy`). Only the offer stack's button went to checkout, so the checkout link lived in one place.
- **Impl:** All buttons are `href="#buy"`; the offer button is `href="PASTE-YOUR-CHECKOUT-LINK"`. The kit has `html{scroll-behavior:smooth}`. Offer v1 was a clean white card: `.offer-top` title "Everything You Get Today" with the sub "One-time $27 · instant access", then "1 What you get" with value rows, a `.totals` block (~~$230~~, "Today: just", `$27.` at 64px red), a `.bump` ("Optional · add at checkout for $17", dashed red), "2 Your guarantee", one button, and "One-Time Payment • Instant Access".
- **Verif:** The click test in 1.15.

**1.19** "I'm not saying you have to change the whole design language" → *Rule:* Borrow components, and keep the kit's design language (ink borders, offset shadows, marker highlights).

**1.20** "frequently asked questions would be good, but I'll give you those later" → deferred.

**1.21** "give me the prompts… ChatGPT can batch create them… same style as our branding… match the offer image"
- **Impl:** `image-prompts.md`: a style brief to paste once, then 4 prompts plus 1 optional, each with a file name and where it's used. See E.

### Round 2: "too cramped now", guarantee block, full desktop rework

**2.1** "the content looks a bit too cramped now… some of the text is a bit small… in the hero section"
- *Rule:* Fitting above the fold must not cost readability. Hero text minimums on phones: alert bar 12.5px, pill 13.5px, H1 30px, subheadline 17px/1.55, fine print 13.5px, full-width button.
- **Impl (before → after):** `.alertbar` 10.5px/6px 10px → `font-size:12.5px;padding:9px 10px;letter-spacing:.07em`. Dot 7 → 8px. `.hero` padding 12/28 → `18px 0 34px`. `.gt-logo` 112 → `150px` (mb 10 → 16). `.trust` 11.5px/4px 12px → `13.5px;padding:6px 15px;margin-bottom:16px`. H1 28px/1.1 → `30px/1.12` (mb 10 → 16). Hero image margin-bottom 10 → 16. `.lede` 15px/1.45 → `17px/1.55;color:#24242E;letter-spacing:.005em`. `.cta` → `margin-top:20px;gap:9px;width:100%`. `.btn` → `padding:16px 14px;font-size:15px`. `.fine` → `13.5px`.
- **Verif:** btn bottom 764, fine 795 of 852, button width 357px (full width). David's next message: "On mobile, it looks amazing."

**2.2-2.5** "$27 instant access… bigger on the alert bar. Game Tape logo… bigger. The 4 million… pill… bigger. The sub headline… a touch bigger… more readable" → all covered in 2.1. The subheadline got darker text (`#24242E`), more line height, and `.hero .lede mark{padding:0 .1em}`.

**2.6** "brands Rika has worked with is good. The CTA I like… section 2… very good… just missing that image" → no change; the image came in 2.10.

**2.7** "how I went from a Best Buy shirt… there are a lot of them that look… too similar, so it's a bit hard to read through"
- *Rule:* In a long story, give each beat its own visual treatment and keep the words exactly the same.
- **Impl:** The story was split into `.beat` blocks (`margin-bottom:26px`). `.lead` "I didn't come from money." is Poppins 800 at 24px (21px phone). `.aside` is italic ink-soft. `.turn` "Then TikTok Shop." is red 24px. `.flipbox` is a sand box with radius 18 and padding 20/22; inside it, `.was` is struck through in red (2px), "But actually?" is `.hand`, and `.punch` follows. `.moment` (the gut-cleanse beat) has a 4px red left border with padding-left 18, and its `.big` line is 20px 800 with a `<mark>`. In `.gem`, "Your flaw is your angle." is `.hand` at `clamp(30px,3.4vw,40px)`. "show, don't tell" is marked.
- **Verif:** Mobile screenshots at `__go('.s3-story',0)` and further down.

**2.8** "The guarantee has to be separate… its own little section"
- *Rule:* The guarantee is its own block directly after the offer stack.
- **Impl:** `<section data-section="7" data-name="Guarantee" class="guar-sec center">` with `.guar-card`: an SVG seal ("90 DAYS · FULL REFUND"), h2 "Your Money's **Protected**", and one paragraph. Claude dropped the leading "And" from the sentence because it now stands alone. The offer card's steps became "1 What you get / 2 Optional add-on". CSS is in C9.
- **Verif:** Desktop screenshot `__go('.guar-sec',…)`, plus a mobile pass.

**2.9** "for the desktop version… fully rework… the hero section doesn't fit… all the texts have the right sizes"
- *Rule:* On desktop the hero has two columns (text left, mockup right) and fits the first screen. Desktop body text is 18-21px, and outcome cards show text left and image right.
- **Impl:** `@media (min-width:900px)` (v4 values, tuned in 3.3): `.hero-wrap{display:grid;grid-template-columns:1.02fr .98fr;grid-template-areas:"logo logo" "pill img" "h1 img" "lede img" "cta img";column-gap:56px;align-items:center;text-align:left;max-width:1200px}`, h1 `clamp(42px,4.1vw,58px)`, lede 19px/1.6, button `padding:20px 40px;font-size:17px`. Section 2 outcomes: `.s2 .outcomes{margin-left:-130px;margin-right:-130px;gap:22px}` and `.outcome>div{display:grid;grid-template-columns:1fr 380px;gap:34px}`. Text sizes went up across the page: `.s2 .stmt p` 24, `.outcome p` 18.5, `.story p` 19, trap lead 22, `.feature-body p` 18.5, lessons 18, `.items li` 17.5, `.claim p` 18, `.desires li` 20, `.card p` 17.5. `.offer` max-width 680.
- **Verif:** At 1440×900 the button ended at 697 of 900 and the hero at 798. Sections 4-7 and the guarantee were screenshotted at 1440 and 1280×800. No sideways scroll.

**2.10** "all the new images chatgpt created… are in the folder offer-1-page-images"
- **Impl:** Claude listed the files and their sizes (`sips`), made 800px JPEG previews in the scratchpad, viewed them, then copied and renamed: `…13_20_01-3.png` → `whatsapp-channel.png` (section 2), `…13_20_00-1.png` → `whatsapp-channel-alt.png` (section 6 channel), `…13_20_01-2.png` → `course-7-day.png`, `…13_20_02-4.png` → `templates.png` (removed in round 3), `…13_20_02-5.png` → `starter-product-list.png` (add-on). All five are 1586×992, 1.6-2.0 MB each.
- **Found:** Prompt 3 (the challenge) didn't come back, and the generated sneakers showed a **Nike swoosh**. Both were flagged to David.

### Round 3: right images, offer contents, desktop fold

**3.1** "the 30-day first sale challenge… the image is not the right one… this is still the document one"
- *Rule:* Never stand in a PDF or document cover where a product mockup belongs. If the real image doesn't exist yet, build an on-brand visual in HTML/CSS and swap it later.
- **Impl:** A `.cal` phone visual (see C11) replaced `challenge-cover.jpg`, and the offer list got a `.cal-thumb` reading "30 DAYS". Both were replaced by the real image in round 7.

**3.2** "it doesn't include the templates to run it… I would remove that because it's not included"
- *Rule:* Every listed deliverable must really be in the offer. When an item goes, recompute the totals everywhere.
- **Impl:** Removed from section 6 and the offer list (an HTML comment notes it in `copy.md`). Total value $230 → **$201** ($57 + $47 + $97). Claude added "You save $174" and flagged it to David as derived.
- **Verif:** `grep -ci templates body.html` = 0.

**3.3** "on desktop… the brand logos are visible before the fold, and maybe the image could be a bit bigger"
- *Rule:* On desktop, the logo strip under the hero must be visible on the first screen at 1280×800 and 1440×900, and the hero mockup should be about 700px wide at 1280.
- **Impl:** Columns `.92fr 1.08fr`, then `.82fr 1.18fr`. `column-gap:44px`, `max-width:1300px`. h1 `clamp(38px,3.4vw,50px)`, lede 18px, `.hero{padding:16px 0 30px}`, logo margin-bottom 22px, `.hero-wrap>.hero-img img{transform:scale(1.04)}`. A tighter strip on desktop: `.press{padding:16px 0 14px}`, `.press-lbl{margin-bottom:10px}`.
- **Verif:** At 1280×800: logos bottom 773 → 753, image width 596 → 701, text block 101..631. At 1440×900: hero bottom 764, button 698.

**3.4** "below Ricky's image. The logos need to be on a slider, just like the ones in brands Ricky has worked with"
- **Impl:** `.logos-mini` grid → `<div class="marquee mini-marquee r"><div class="marquee-track">@@PRESS@@</div></div>`, with `.mini-marquee{margin-top:30px;padding-top:22px;border-top:1.5px dashed …}`, track gap 40px, logos 30px (26px on phones).
- **Bug found:** At 1280 the max-content track widened its grid column, making page `scrollWidth` 2051. The fix was `.side3,.s3-head,.s3-story{min-width:0}`. After the fix: `[scrollWidth 1280, .side3 width 387]`.

**3.5** "more separation in between that logo slider and I didn't come from money"
- **Impl:** On phones, `.side3{margin-bottom:22px}` and `.mini-marquee{margin-top:26px}`.
- **Verif:** JS `r('.s3-story').top - r('.mini-marquee').bottom` = **46px**.

**3.6** "improve the… everything you get today… I'm sure you can improve it"
- **Impl (offer v2):** A dark header band `.offer-head` (title plus a red pill sub), a product mockup `figure.offer-hero`, item rows with `.thumb` images (64×44), a `.pricebox` (~~$201~~, big red $27, "You save $174", "No subscription. No upsell required."), the add-on, the button, and a `.trust-row` with 3 icons (One-Time Payment, Instant Access, 90-Day Refund).
- **Bug found:** Older `.offer` padding rules (desktop `40px 40px 34px`, phone `26px 18px 22px`) left the dark header band inset inside a white border. The fix was `.offer{padding:0;overflow:hidden}`, with the padding moved to `.offer-body` (`26px 30px 30px`; desktop `30px 40px 34px`; phone `20px 16px 22px`).

### Round 4: no-bg hero, sliders running out, bigger outcome boxes, crossed prices

**4.1** "use this image for the hero section 'offer 1 image v3 no background'… works better with the background gradient"
- *Rule:* The hero mockup must be a transparent PNG so it sits on the hero gradient. Use the same file wherever a white box would show on a tinted band.
- **Impl:** Located with `mdfind -onlyin ~/Downloads -name v3`. `sips` showed 1672×941 with `hasAlpha: yes`. Saved as `images/hero-headstart-mockup-nobg.png` and used in the hero **and** section 14 (its grey band had shown the old image's white box).

**4.2** "brands… logo slider. It runs out of the logos, like it becomes white… not working reliably"
- *Rule:* Sliders must never run out at any screen width.
- **Impl:** The JS `fill()` doubles each track until half its width exceeds the container plus 80px (C1). The video carousel was capped at `max-width:1040px` (from 1080) so its 5 videos always fill it.
- **Verif:** At 1920×1080 Claude logged every track's `scrollWidth/2`, the container `clientWidth` and the child count. Each loop was about 3,900px at 1920.

**4.3** "these three boxes in desktop, the texts have to be way bigger… too much white space… titles and the subtitles have to be bigger"
- *Rule:* On desktop, outcome titles are real headings (29px) and the text is 21px. On phones, titles are 19px.
- **Impl:** `.s2 .outcome strong{display:block;font-family:var(--font-head);font-weight:800;font-size:19px;line-height:1.25;margin-bottom:8px}`. On desktop: `font-size:29px;line-height:1.2;margin-bottom:12px`, `.s2 .outcome p{font-size:21px;line-height:1.5}`, `.outcome{grid-template-columns:64px 1fr;padding:34px 38px;align-items:center}`, `.n{width:52px;height:52px;font-size:20px}`, `.outcome>div{grid-template-columns:1fr 360px;gap:40px}`.
- **Bug found:** On phones, an extra blank line appeared under each title, from the old `<br>` now that `strong` is a block. Fixed with `.s2 .outcome p br{display:none}`.

**4.4** "I don't think you highlight enough what the total value is… you can actually cross the prices… with them still being visible"
- *Rule:* Show each item's value struck through but still readable, and make the total value versus today's price obvious.
- **Impl:** `<span class="val"><s>$57</s> value</span>` with `s{font-family:var(--font-head);font-weight:800;font-size:18px;text-decoration-color:var(--hi);text-decoration-thickness:2.5px}`. The price box became two columns: `.pb-col.was` (sand, 2px dashed, "TOTAL VALUE:", ~~$201~~ at 46px with a 5px red strike) and `.pb-col.now` (dark, `box-shadow:6px 6px 0 var(--accent)`, "TODAY: JUST", `$27.` at 62px in `#FF6B63`), with a red "You save $174" pill under both. This was replaced in round 5.

**4.5** "to make the subheadline shorter… I remove the a 7-day course"
- **Impl:** The text "…sales: a 7-day course on how to find…" became "…sales: how to find…".
- **Verif:** The hero still fits on the phone (btn 764, fine 795).

### Round 5: JJ-style price structure, bigger mobile logos, missing-image list

**5.1** "Improve the price comparison… more like in the JJ Smith websites… structure, not… the branding"
- *Rule:* Price block order: item list with crossed values on the right → a "Total value" bar with the crossed total → a bordered deal box with a "You save" badge on its top edge, the big "Today: just $27.", a note, the full-width checkout button and the trust row → the add-on after it. Never write "Today only" when there's no deadline.
- **Impl:** In this order: `.items .val s` (19px, ink-soft, red 2.5px strike), `.stack-total`, `.deal` with `.deal-badge`, `.deal-now`, `.deal-note`, `.btn`, `.trust-row`. Full CSS in C8. JJ's badge said "Today Only · Save 86%". Claude dropped "Today only" on purpose.
- **Verif:** Phone and desktop screenshots at `.items`.

**5.2** "make the brands… slider in mobile bigger, so it's hard to miss. A bit more space"
- *Rule:* On phones, the logo strip uses 40px-tall logos with about 26px padding.
- **Impl (phone):** `.press{padding:26px 0 24px}` (was 16/14), `.press-lbl{font-size:12.5px;margin-bottom:16px}` (was 11px/10), `.marquee-track{gap:44px}` (was 40), `img{height:40px;max-width:140px;opacity:.75}` (was 28px/110px/.6).

**5.3** "tell me what other images we are missing… very, very concise"
- **Answer (a table):** (1) 30-Day Challenge image (prompt 3), (2) Rickey in his Best Buy outfit (real), (3) brother's results screenshot, (4) friend's page growth screenshot, (5) top-1% creator badge, (6) sales dashboard, (7) first-ever sale notification, (8) redos of the 2 WhatsApp images and the Starter Product List with plain sneakers. Also: a photo of Rickey he's licensed to use, because the current one "looks like a cropped Getty Images photo."

### Round 6-7: challenge image, true offer contents

**6.1** "give me the prompt for the 30-day challenge image again"
- *Rule:* When re-sending a prompt, make it self-contained, with the style brief folded in, so it works in a fresh ChatGPT chat. Text in E2.

**7.1** "chatgpt image generated 'Pack de desafío Game Tape 30 días'"
- **Impl:** Found by name with `mdfind` (ChatGPT named it in Spanish, its UI language). It was 1586×992 with no alpha. Claude checked it for third-party logos (none), saved it as `images/challenge-30-day.png`, and used it in section 6 and as the offer thumbnail, replacing the `.cal` visual and the `.cal-thumb`.
- **Verif:** JS listed every `.feature img` with its `naturalWidth` (all 1586).

**7.2** "there are no 'both milestone playbooks'… the things it includes are, the course, the 30 day plan and the rickey army private channel"
- *Rule:* The client's latest word on offer contents beats older documents. Check the docs, report any conflict, and don't overrule the client.
- **Impl:** Claude read the offer ladder HTML (dated Nov 14) and the Offer Stack v11 PDF (text extracted with `osascript -l JavaScript pdf2png-n.js`). Both were older and listed other items. The "Rickey Army" name came from the Nov 17 meeting transcript. Changes: "Plus two playbooks…" was removed, the list item became "The 30-Day First Sale Challenge", and the channel became "The Rickey Army Private Channel" in sections 2 and 6 and the offer. Values stayed $57 / $47 / $97 = $201. The line "This is the full playbook." in section 12 was kept as a figure of speech.

### Round 8: go-live cleanup, Best Buy photo, Instagram story

**8.1** "'rickey-bestbuy' image in the folder"
- **Impl:** The file was 672×1033 (88 KB). It went into the section 3 polaroid with `style="object-position:50% 18%"` (the kit's default is 50% 38%), so his face stays in frame. Section 12 kept the other photo.

**8.2** "I dont have any more images so either remove those sections… or dont include images we dont have so we can go live"
- *Rule:* Never show a placeholder on a live page. If an asset doesn't exist, drop the spot; text-only is fine.
- **Impl:** Section 9 is now text only (the brother and friend stories). Section 10 keeps only the TikTok screenshot slider (the `.proofgrid3` placeholders are gone). Claude drafted footer disclaimers (earnings, TikTok/ByteDance trademark and non-affiliation, refund policy) so `check_page.py` had nothing to flag.
- **Verif:** `check_page.py` reported "OK: nothing that must be fixed". `.ph` count = 0, and 1 checkout placeholder remained.

**8.3** "this is a text from rickeys instagram… would make the section stronger, more relatable and not so vague"
- **Impl (later reverted):** A new opening line, "I used to work at Best Buy to pay for my acting classes."; a black `.circle` box ("And that Best Buy… Years later, ya boy is shooting a commercial for them."); and a new beat ("Where you are right now is only temporary… Patience + persistence."). Claude left out "7 years ago", which was counted from an old post date, and flagged all its own lines for review.

### Round 9: two photos

**9.1** "both images… First the Best Buy and then the other one… in mobile… next to each other, and on desktop one on top of each other"
- *Rule:* With two founder photos: side by side on phones, stacked and slightly overlapping on desktop (scrapbook look). A column taller than the screen must not be sticky.
- **Impl:** `.pols` holds `.pol.p1` (rotate -3deg) and `.pol.p2` (rotate 3deg). Desktop: `.pols{display:flex;flex-direction:column;align-items:center}`, `.p1{margin:0 30px 0 0}`, `.p2{margin:-34px 0 0 50px}`. Phone: `.pols{display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:start}`, `.pol{max-width:none;margin:0;padding:8px 8px 30px}`, `.p2{margin-top:18px}`. `.side3` lost `position:sticky;top:48px`; otherwise the bottom photo and the logos would stay hidden until the end of the section.
- **Verif:** JS confirmed `naturalWidth` of both photos (672 and 1556), with screenshots at phone and 1440 widths. Claude flagged that the red carpet photo now shows twice (sections 3 and 12) and may be a Getty photo.

### Round 10-11: "don't rewrite the story"

**10.1** "that Best Buy… I don't think that's integrated properly… It should be at the beginning… 'calling myself an actor in Best Buy shirt', that's too bold… frame the starting of the story differently"
- **Impl (rejected):** The story opened with the black `.circle` box (commercial full circle), followed by "But it didn't happen overnight.", and the "Calling myself an actor" line was removed.

**11.1** "No, I don't think that's well integrated… Just have it as it was… Have the copy as it was before. Don't make any changes."
- *Rule:* **The founder's story copy is the client's voice. Don't rewrite it.** You may add photos and styling, never new beats. If the client offers source material ("make it stronger"), propose a draft for approval rather than restructuring the live copy. After one rejected rewrite, revert at once to the last approved text.
- **Impl:** Claude used a regex to splice the `<div class="story s3-story">…<div class="cta r">` block from `body-src-v8.html` back into the current file, and the `## SECTION 3` block of `copy-v8.md` back into `copy.md`. It kept the two photos and the beat styling and wrote a learned rule: "OVERRIDES the Instagram lines above… Do not rewrite it."
- **Verif:** `check_page.py` reported OK, and greps confirmed the original opening line was back.

### Round 12 (end of slice): one repo for the collaborator

- "put everything in one place… a GitHub repository… host it in GitHub temporarily… public"
- **Impl:** `export_final.py --images keep` produced `index-final.html` with no editor (87 KB). The repo was assembled with `index.html`, only the images the page uses (found by regex over the page and source), `offer-1-sales-page/` (body-src, copy, copy-original, brand-kit, learned-rules, image-prompts, paste-ready), and `project-files/` (rsync excluding `.DS_Store`). Size check: no file over 50 MB, 115 MB total. A secret scan ran (`sk_live|pk_|AKIA|ghp_|xox|PRIVATE KEY|password=`, including `.docx` text) and found nothing. A README was written for the collaborator. Then `git init -b main`, commit, push. SSH was refused, but HTTPS worked through the keychain; `git ls-remote` confirmed the push. Pages returned 404 until it was enabled (Settings → Pages → `main` / root).


---

# Part 3: Sharing, speed, checkout, bump, upsell

## A. Feedback and request log (this slice)

Each entry: **David's request** → **general rule for any sales page** → **what was implemented** → **how it was verified**.

### A1. "Put everything in one place… a GitHub repository… public… host the website temporarily… also all the project files. What do you need from me? Be very concise."
- **Rule:** When the page is "done", package it in one self-contained folder and one repo: the hostable page, every asset it needs, the sources (copy, brand kit, rules, prompts), and the client's raw project files. Host a preview on GitHub Pages for sharing. When asking the user for access, list exactly what you need, numbered, and ask them to confirm anything risky (what becomes public).
- **Implementation:** Claude answered in 3 numbered asks (create an empty public repo with no README and send the URL; let this Mac push; turn on Pages after the first push) plus 2 confirmations (everything goes public, including meeting transcripts, research and a possibly-Getty photo; emails to the teammate get shown before sending). Then: export, assemble, secret scan, README, commit, push (details in B).
- **Verification:** `git ls-remote` hash equals local `HEAD`; GitHub API showed `private: False`; Pages URL returned 404 until the user enabled Pages, then 200.

### A2. "Draft the email to Moses… include the Git repo… he can download it… what's most important is understanding how we put this live (checkout, order bump checkbox, one-click upsell, PDFs, course access)."
- **Rule:** The hand-off email to a teammate states what is finished, gives the live link and the repo link, says the README explains what's where, then asks the open questions as a numbered list. Draft first, show it, send only on a clear yes. Flag anything you added that the user didn't ask for.
- **Implementation:** Gmail draft (not sent) with six numbered questions (checkout type, bump checkbox, one-click upsell, PDF delivery, course hosting, adding buyers to the private channel). Claude flagged that question 6 was its own addition.
- **Verification:** The draft text was shown in chat. Nothing was sent until the user gave the Pages link and said to go.

### A3. "This is the link https://shuri-lab.github.io/rickey-tiktokshop-project/… I'm worried about building without a tool like GoHighLevel… we can't afford it not working."
- **Rule:** Before sending a live link to anyone, check that it loads: the page, at least one image, and the `<title>`. Put the user's concern into the email in their terms.
- **Implementation:** `curl` checks (page 200, hero image 200, title "TikTok Shop Headstart | Game Tape"). Sent the email with the live link added at the top and the concern added before the close. Deleted the old draft so only one version exists.
- **Verification:** curl output; sent-message confirmation; draft deleted.

### A4. "Did you also include the link to the Git repo?"
- **Rule:** Every hand-off includes both links: live page and repo. State whether the repo is public (no access request needed).
- **Implementation / verification:** Quoted the exact repo line from the sent email.

### A5. "I don't see the offer 1 landing page created [in the builder]… create one blank and put an HTML component with our code… not sure what to do with the images."
- **Rule:** To put a hand-built page into any page builder, use one Custom Code/HTML element. Images must use absolute URLs to a host the page can reach. If the full code can't be pasted, use a loader that fetches the page fragment from a static host (F).
- **Implementation:** `ghl-sales-page.html` built from `paste-ready.html` (absolute image URLs to GitHub Pages, checkout placeholder replaced with the real checkout URL). The builder's code element holds only a short loader (F1). Wrapper padding/width fix and tab title prepended (F3).
- **Verification:** On the live URL, JS walked from `#gt-root` up the DOM and printed each ancestor's padding and max-width (found `c-column` 10px 5px padding and `.inner` max-width 1170px, fixed by the wrapper CSS). Then at 393×852: `scrollWidth == innerWidth` (no sideways scroll), hero button bottom at 784px of 852 (above the fold), checkout href correct, tab title set.

### A6. "Have you created and verified the offer 1 page and the checkout?"
- **Rule:** Report status per item, honestly: "created and verified" vs "started, not finished", say what the address shows right now, and say what hasn't been tested (e.g. no test purchase).
- **Implementation:** `curl` on each funnel URL (all 200) plus a content check showing the checkout had no order form yet; answered with a ✅/❌ list.

### A7. "In the offer one landing page I don't want to announce the order bump. It's only visible in the checkout."
- **Rule:** The sales page sells one thing at one price. The order bump appears only at checkout, never on the sales page.
- **Implementation:** Backed up first (`body-src-v12.html`, `copy-v12.md`). Removed the `<p class="step"><b>2</b>Optional add-on</p>` label and the whole `.bump` block, and the now-lonely `<p class="step"><b>1</b>What you get</p>` label. Removed the matching line from `copy.md` ("Want a shortcut on picking products? You can add The Starter Product List at checkout for $17…") so the kit's copy check stays in sync.
- **Verification:** Counted `<div`/`</div>` and `<section`/`</section>` to confirm the markup was still balanced after the cut. On the live page, JS checked `document.body.innerText.includes('Starter Product List') === false`. Kit `check_page.py`: "OK: nothing that must be fixed".

### A8. "All the images… loading super slow… the videos too… fully optimize them… keeping a level of quality."
- **Rule:** Every image is served as WebP at about 2× the width it is displayed at (never upscaled), with `srcset` for large images. Only the hero loads eagerly (`fetchpriority="high"`); everything else is lazy. Videos are small, short, muted transforms that load only near the viewport. Each video downloads once.
- **Implementation:** See C (exact recipe). One rebuild script (`rebuild.sh`) "so every change rebuilds the same way".
- **Verification:** Live page scrolled to the bottom by script, then a Resource Timing audit: 31 WebP images requested, 0 old PNG/JPG requests, 0 broken images. Computed image weight ~1,155 KB on phone and ~1,452 KB on desktop for a full scroll (was ~15 MB). Videos ~half size per clip. Screenshots checked for sharpness.

### A9. "Checkout on mobile: everything stacks up… you don't see the checkout form… make it way more compact… the checkout form has to be visible above the fold. Desktop is fine, don't change it."
- **Rule:** On phones, the checkout form must start above the fold. Collapse the offer summary into one small card (thumbnail, product name, one "includes" line, crossed value vs today's price, one trust row). Leave desktop untouched by using two blocks: one shown at ≥768px, one below 768px.
- **Implementation:** `.gtc-d` (desktop, unchanged) and `.gtc-m` (phone card) in `ghl-checkout-left.html`. Builder section/column padding reduced on phones. Details in E2.
- **Verification:** Screenshots at 393×852 showed the contact form starting well above the fold. Desktop checked at 1280×800.

### A10. "The checkout form doesn't look good… font, input fields… make it clear where the inputs go. Remove 'Select product' (the product is already selected). Payment section and 'Get instant access' button are fine."
- **Rule:** Checkout forms get a card surface, numbered steps, big boxed inputs with clear labels and placeholders, a visible focus state, and helper text where it matters. Hide anything the buyer can't act on (single-product picker, subtotal rows). Keep "Total due today". Don't touch the parts the client likes.
- **Implementation:** CSS + a small enhancer script restyle the builder's order form (E3). The product table is hidden, but the product stays selected.
- **Verification:** JS clicked the bump checkbox and read the total: "Total due today $27.00" → "$44.00" → "$27.00". The main product radio was still `checked`. The injected image and arrow survived the form re-rendering (1 of each).

### A11. "The order bump needs the image… the text more compelling… 'get the product lanes' doesn't make sense, say get X amount of products… it has to pop out: a background, an arrow pointing at it, moving, a striped discontinuous border."
- **Rule:** The bump box must be the most eye-catching element in the form: a tinted background, a dashed brand-color border, a gentle glow, a "one-time offer" banner, an animated arrow pointing at a large checkbox, and the product image. The copy counts concrete things the buyer gets ("37 products"), not internal jargon ("lanes").
- **Implementation:** E4 (design). The number 37 came from counting the actual PDF with pypdf (29 picks across 8 all-year lanes plus 8 viral picks). The builder's bump image field is upload-only, so the image is injected by script.
- **Verification:** Phone screenshots and the toggle test above.

### A12. "Build the upsell page… study https://www.davidhsai.com/upsell-1-product--model-videos-page for structure… alert bar that pops… 'access in the next 5 minutes'… exclusive-opportunity language instead of 'watch this video'… headline like 'you just unlocked… now get results 10x faster'… product image, headline, subheadline, offer stack with crossed prices and total, special price… two buttons created in the builder, YES! Add … For Only $97 / No thanks, I'll …… custom HTML for everything except the two buttons… no VSL… make a step-by-step plan."
- **Rule:** One-click upsell page structure: confirmation alert bar → progress bar → "exclusive one-time offer" pill → "You just unlocked X. Now get Y 10x faster" headline → product image → product title → subheadline → bridge from offer 1 to offer 2 → offer stack with crossed values, crossed total, savings badge and a big price → guarantee → "exclusive one-time offer, only here, gone when you leave" lead-in → big YES button → small "No thanks, I'll [pain]" link. Everything is custom HTML except the YES/NO elements, which stay native to the checkout platform so the one-click charge works.
- **Implementation:** D.
- **Verification:** The fragment was previewed directly on its GitHub Pages URL at phone size before wiring it in. On the live page: JS overflow check (every element whose right edge > `clientWidth`), phone and desktop screenshots of each section, both buttons picked up their styles (`.gtu-yes`, `.gtu-no` present).

### A13. "Where can I see the upsell page?"
- **Rule:** Always answer with the live URL, how a buyer reaches it in the real flow, what works and what doesn't yet, and where to edit it.
- **Implementation:** Gave the live URL, explained that buyers land there after paying, that "No thanks" goes to the thank-you page, that YES does nothing until its one-click action is set, and the builder path to edit it.

### A14. "The order bump text is too long… too many numbers (37, 29 picks, 8 lanes, 8 viral)… confusing… good sales copy is one a 5th grader could understand… more concise, more compelling."
- **Rule:** Bump copy = one pain + one number + one promise, in one sentence a 10-year-old understands. No sub-counts, no category names, no jargon. It must fit on a phone next to the image.
- **Implementation:**
  - v1: "Want a shortcut on picking products? Get the product lanes that sell all year + the one move to find today's winner in any lane. Pick your first products tonight instead of guessing."
  - v2: "Stop guessing what to sell. Get 37 hand-picked products you can start promoting this week: 29 picks across 8 lanes that sell all year, 8 viral scroll-stoppers, plus a seasonal calendar that shows you what's about to spike. Pick your first products tonight." (256 characters, rejected)
  - **v3 (final):** "Stop guessing what to sell. Get my list of 37 products people are buying right now, so you can pick your first product tonight." (127 characters)
  - Price line went from "[ONE-TIME ADD-ON] Only $17!" to "Only $17 today. One-time payment."
- **Verification:** Read `.order-form__bump-desc` innerText on the live checkout at 393×852, plus a screenshot.

### A15. (Out of scope, listed for completeness) Build the whole funnel in the builder, invite the teammate as a user, turn on Remote Control for phone use. See H.

### A16. (Session close) "Package everything we learned so anyone can build sales pages this good for any project; include a test; GHL is out of scope." This document is part of that.

---

---

# Part 4: After the pages, finishing and testing the funnel (Nov 23 and 24 2026)

### P4.1 "they just need the access to their course or courses and the pdfs" (about a "Welcome to The Starter Product List!" badge email)
- **He said:** it "just doesnt make any sense to send users, it is not saying the right things not in the right language, not in Rickey voice".
- **Rule:** buyers get only on-brand emails in the founder's voice, with access and files. Every platform's own welcome, badge and certificate email is off.
- **Built:** the three emails in `examples/rickey-headstart/funnel-pages/funnel-pages.json`; the badges and stock emails turned off in GHL (GHL Funnel Playbook, Stages 9 and 10).

### P4.2 "I don't want to put them in a GitHub or anything like that"
- **Rule:** paid files live behind the buyer's login. Never on public hosting, never linked from the thank-you page.
- **Built:** the thank-you page says where the PDF is; `build_funnel_pages.py` refuses a file link on it.

### P4.3 "The order bump… is optional… ok as long as they dont get the products list if they didnt get the order bump"
- **Rule:** nobody receives what they didn't buy. The bump box starts unticked, its file is in its own course, and the email that goes to everyone never names it. Naming it on the shared thank-you page is fine as a question ("Added …?").
- **Built:** `funnel-offers.md` "Who gets what"; the build fails if the main email names the bump or an upsell.

### P4.4 "they should be able to find both courses in their account"
- **Rule:** one login, everything they bought side by side.

### P4.5 "do another test where you buy offer 1 and then offer 2 as well… when you buy offer 1 and you decline offer 2"
- **Rule:** test the accept path and the decline path, with and without the bump.

### P4.6 WhatsApp link and two images for the thank-you page
- **Rule:** a community step has the channel's real picture, one button, and its QR code on desktop only (a phone can't scan itself). Check that the QR and the button open the same place.

### P4.7 A face cut off in a round photo
- **Rule:** set the focal point of every cropped face and look at the screenshot.

### P4.8 "do the skills… have everything they need to also build all the rest of the pages of a funnel"
- **Rule:** the playbook must build the whole funnel for a new offer, not only describe Rickey's. → Part 2 (F1 to F5), the generator and its checker.

### P4.9 Sales page v1.1 build ticket (Nov 24): "Point every landing CTA straight to checkout"
- **He asked for:** every button to link directly to the checkout instead of `#buy`, with the "Everything You Get Today" section left exactly as it is ("it still sells to people who read top-to-bottom"). Then, for this playbook: "Yes, update it".
- **Rule:** every sales page button, the sticky bar included, goes straight to checkout. The offer stack stays, with its own button. This replaces 1.18.
- **Built:** `@@CHECKOUT@@` in `body-src.html`, filled once from `page-config.json`; `expand_body.py` stops if a button still jumps down the page; `grade.py` fails the routing item.
- **Not proven:** no traffic data compares this with jumping to the stack.
- **Also in the ticket (copy):** the section-2 header ends on what the buyer gets ("You Need a Plan That Gets You Sales."), and "watch your milestones stack up" was cut from the third outcome.

### P4.10 Same ticket: "Mobile checkout: add an expandable summary (one addition only)"
- **He asked for:** the phone checkout exactly as it is, plus a collapsed "See everything included" toggle that opens the value stack and the guarantee; no subline under the label ("that would just duplicate the card's subtitle above it"); desktop unchanged. Then: add it to the playbooks.
- **Rule:** on phones the checkout shows little and offers everything: one tap opens what they get, the total, the saving, today's price and the guarantee. The form stays on the first screen.
- **Built:** generated by `build_funnel_pages.py` from the same data as desktop; `check_funnel_pages.mjs` opens and closes it and fails if an item, the price or the guarantee is missing.
- **Measured on Rickey's live checkout:** the first field moved from 313 to 350px (of 852). Not measured: its effect on sales.
