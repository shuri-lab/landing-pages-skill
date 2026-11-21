# Stage 4 of 9: Images and media (the hands-on stage)

**Goal:** every image and video the page needs is in `my-sales-page/images/`, named by role, checked, and planned to a section. There are no placeholders left for go-live.

**Why it matters:** a strong page is mostly visuals. On Rickey's page, half the polish came from images:
- AI mockups of each product
- real TikTok screenshots under each claim
- the brand-logo sliders
- muted video loops
- two real founder photos

That took a person's hands: generating images in ChatGPT and grabbing screenshots from TikTok and Instagram. Plan it early, so the person can do it in one go.

## 4a. Make the image plan (Claude)

1. Read `kit/sales-page-generator-kit/kit/3-images/image-slots.md`, then look at every image in the project folder yourself.
2. Write `my-sales-page/image-plan.md` as a table:

   | # | Section | What it must show | Have it? (file) | Source if missing |
   |---|---|---|---|---|

3. Use the house-style list of visuals as the checklist:
   - **Hero:** the offer mockup, transparent background (PNG with alpha) so it sits on the hero gradient.
   - **Brand/press logos:** 5–8 logos for the slider under the hero. Use logos of brands the founder really worked with, or press that really featured them.
   - **One visual per outcome claim:**
     - proof claims get real screenshots (social posts, results, the method in action);
     - product features get AI mockups in the same style as the hero.
   - **Each item in the offer:** a mockup in the same style family. Never a PDF cover or a document page.
   - **Founder:** 1–2 real photos, never AI. Confirm the license, and don't show the same photo twice.
   - **Video:** 4–6 short vertical clips of the founder for a muted autoplay carousel.
   - **Proof wall:** 6–10 real screenshots for a slider.
4. **Name files by role.** That way `tools/optimize_images.py` picks the right sizes:
   - prefixes: `hero-`, `product-`, `section-`, `photo-`, `logo-`, `brand-`, `shot-`, `proof-`, `thumb-`
   - lower-case kebab-case
   - Example: `product-30-day-challenge.png`, `shot-pocket-knife.jpg`, `brand-subway.png`.

## 4b. Write the ChatGPT image prompts (Claude)

Write `my-sales-page/image-prompts.md` so the person can paste everything into ChatGPT in one session.

- **First: the style brief, pasted once.**
  - It matches the hero mockup.
  - Brand colors are given as hex codes.
  - The logo is described in words.
  - It sets the typography and the person's likeness (attach a clear front-facing photo).
  - "Spell every word exactly as written in quotes."
  - **"Never show money amounts, income, earnings, sales numbers, payout notifications, prices, star ratings, follower counts or testimonials."**
  - **"No brand logos other than [our brand]."**
  - Landscape 16:10, no watermark.
- **Then one prompt per missing image.** Each one has:
  - a header with the **file name to save as** and **where it's used**;
  - the composition, with the exact on-screen text in quotes;
  - explicit negatives.
- **Make every prompt self-contained,** so a re-run works in a fresh chat.

Template and Rickey's real prompts: `knowledge/prompts/image-prompts-template.md` and `examples/rickey-headstart/image-prompts.md`.

## 4c. The person's checklist (send this as one message, then wait)

> **Stage 4: images. Here's what I need from you (about 30–45 min):**
> 1. **ChatGPT:** open `image-prompts.md`. Attach [the style image] and [the founder photo], paste the style brief, then paste each prompt. Save each image with the file name in its header.
> 2. **Screenshots:** from [the founder's TikTok/Instagram], grab [N] screenshots of [what]. Crop out phone status bars if you can. Cover any buyer emails or phone numbers.
> 3. **Photos:** [N] real photos of [founder] (e.g. at their old job, on a set). Licensed ones only.
> 4. **Logos:** PNG logos (transparent if possible) of [brands].
> 5. **Videos:** [N] short vertical clips (10–30s). Upload them to Cloudinary, or put them in the folder.
> Put everything in `[PROJECT]/page-images/` and tell me when it's done.

## 4d. Pick up, check, place (Claude)

1. Find the files. ChatGPT names files in its UI language ("Imagen de ChatGPT…", "Pack de desafío…"), so search by folder or date, not by English name.
2. **Match returned files to the prompts one by one.** Batches silently skip prompts. Report what's missing.
3. **Inspect every image** before placing it:
   - third-party logos (a Nike swoosh appeared on generated sneakers)
   - wrong product
   - misspelled text
   - white boxes where a transparent background is needed
   - personal data in screenshots
   - Use `sips -g pixelWidth -g pixelHeight -g hasAlpha file`, and look at a small preview.
4. Copy each one into `my-sales-page/images/` under its role name. Never edit, crop or restyle a testimonial or result screenshot.
5. Videos go to Cloudinary (or another CDN) and are served light with `w_320,q_auto:eco,ac_none,du_10,f_auto`. See `stages/8-speed.md`.
6. Update `image-plan.md`, and show the client the table: image → section.
7. **Go-live rule:** if something is still missing at go-live, drop that spot. Don't ship a placeholder. A section can run as text only.

## Done when

- [ ] Every row in `image-plan.md` is either filled with a checked file or dropped by decision
- [ ] No third-party logos in AI images; founder photos are real and licensed
- [ ] Videos hosted on a CDN with the light transform
- [ ] Files named by role

---

# Reference: what happened on the Rickey page

## E. Image and media sourcing

## E1. What was needed and where it came from
| Asset | Source | Notes |
|---|---|---|
| Hero/offer mockup | Client (`offer 1 image v3 no background.png`, 1672×941, alpha) | Transparent version needed for the gradient. The older `hero-headstart-mockup.png` is kept inside the offer card |
| WhatsApp channel ×2, 7-day course, templates, Starter Product List | ChatGPT batch (5 × 1586×992 PNG) | Templates later dropped. Nike swoosh on the sneakers |
| 30-Day Challenge mockup | ChatGPT re-run (`Pack de desafío Game Tape 30 días.png`) | Missing from the first batch. An HTML visual stood in meanwhile |
| TikTok screenshots ×10 (946×2048) | Client | Section 2 outcome 1 (3 of them) and the section 10 slider (all) |
| Product check screenshots ×2 | Client | Section 2 outcome 2 |
| Brand logos ×6 | Client | Press strip and section 3 slider |
| Rickey red carpet photo | Client | Looks like a cropped Getty photo, so check the license |
| Rickey Best Buy photo (672×1033) | Client (`rickey-bestbuy.jpeg`) | Real photo; `object-position:50% 18%` |
| Rickey's Instagram caption | Client (pasted text) | Story material, which the client then decided not to use |
| TikTok videos ×5 | Cloudinary | Light transforms (C4) |
| Offer contents and names | Offer ladder (Nov 14), Offer Stack v11 PDF, Nov 17 meeting transcript, the client's word | The client's latest word wins |

**File handling:** Claude found files by the name the client used (`mdfind -onlyin ~/Downloads -name …`, `find -iname`), checked size and alpha with `sips -g pixelWidth -g pixelHeight -g hasAlpha`, made previews with `sips -Z 800 -s format jpeg … --out scratch/prev.jpg` and viewed them, then copied them into `images/` under descriptive kebab-case names.

## E2. The ChatGPT prompt pattern (`image-prompts.md`)
1. **Attach first:** the style reference (`offer-1-image-v2.png`) and a clear, front-facing photo of the person for likeness.
2. **Paste the style brief once** (the same brief for the whole set):
   - "photo-realistic 3D product mockup on a pure white or very light grey seamless background, soft studio lighting, soft natural shadows, slight depth of field"
   - brand colors as hex only (`#D30805`, `#101017`, white), with red used for accents, swooshes, buttons and highlights
   - the logo described in words (bold black slanted italic capitals plus a red rounded "REC" badge with a white dot)
   - typography ("heavy, bold, condensed sans serif, all caps for titles")
   - the likeness ("same face, skin tone, rimless glasses, short hair, friendly smile")
   - the device list (laptop, current iPhone, tablet, printed booklets)
   - "Spell every word exactly as written in quotes. No other readable words except small grey placeholder lines."
   - **"Never show money amounts, income, earnings, sales numbers, payout notifications, prices, star ratings, follower counts or testimonials"**, so the images can't make claims you'd have to back up
   - "Landscape 16:10, high resolution, no border, no watermark"
3. **One prompt per image:** a header with the **file name** and **where it's used**, then the composition (device, angle, exactly what's on screen with the quoted text, secondary element, red swoosh, logo corner) and explicit negatives ("No money, prices or numbers other than 'DAY 7'").
4. **The re-run prompt is self-contained** (style brief folded in), so it works in a new chat. The prompt-3 re-send also said: "No brand logos other than GAME TAPE (no Nike, no TikTok logo)."
5. **Not AI:** real story photos. "Please don't generate fake 'old' photos of him for this, since the story says they're real."

Example re-run prompt (abridged): "Create one photo-realistic product mockup image for 'TikTok Shop Headstart' by GAME TAPE. Match the style of the attached offer image exactly… On the left: a printed booklet… title 'THE 30 DAY FIRST SALE CHALLENGE', with 'FIRST SALE' in red… On the right… an iPhone… a 30-day calendar grid… Days 1 to 7 filled red with white checkmarks, day 8 has a red outline… a red pill badge 'DAY 7 STREAK'… two milestone badges with a small lock icon… '1,000 FOLLOWERS' and 'FIRST SALE'. Spell every word exactly… No brand logos other than GAME TAPE (no Nike, no TikTok logo). Landscape 16:10…"

## E3. What went wrong, and the rules
- **The batch silently skipped one prompt** (the challenge). *Rule:* match the returned files to the prompts one by one, and report what's missing in the wrap-up.
- **Third-party logos crept in** (a Nike swoosh on the sneakers). *Rule:* inspect every AI image for brand marks before placing it, and put "no brand logos other than <ours>" in every prompt.
- **The wrong image for a product** (the challenge PDF cover used as its picture). *Rule:* every product visual must be a mockup in the same style family. Build an HTML stand-in rather than reuse a document cover.
- **An image for a deliverable that isn't included** (templates). *Rule:* check the offer contents before generating images for them.
- **A white-box image on a tinted band.** *Rule:* ask for and use transparent PNGs on gradients and grey bands.
- **Possible stock photo of the founder.** *Rule:* confirm rights before going live, and avoid showing the same photo twice.
- **Big PNGs (1.6-2 MB)** made screenshots look blank while decoding. *Rule:* compress and convert to WebP before going live. (This was done later: `images/opt/*-720/1280.webp` with `srcset`.)
- **File names come back in ChatGPT's UI language** ("Imagen de ChatGPT…", "Pack de desafío…"). Search by date or folder, not by English name.
