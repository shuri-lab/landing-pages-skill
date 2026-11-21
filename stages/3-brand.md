# Stage 3 of 9: Brand, colors and fonts

**Goal:** `my-sales-page/brand-kit.md` in the kit's format: the 5 main colors plus helper colors, the role map (which color does which job), and the fonts. The client must say "yes, that feels like us".

## Steps
1. **Source**, in this order of preference:
   1. The client's brand guidelines PDF in the project folder.
   2. Their logo or website.
   3. A palette they pick from `kit/all-brand-palettes.pdf` (42 palettes; they screenshot one card).
   4. "Tell me the vibe", and you suggest 3.
2. **Read the exact values. Don't guess them.**
   - **Brand PDFs:** read hex codes and font names from the PDF's text layer: `osascript -l JavaScript tools/mac/pdf2png.js <pdf> <outdir> 1400` (macOS), `pdftotext`, or the pdf skill.
   - **Images:** sample the pixels.
3. **Fill the kit template:** `kit/sales-page-generator-kit/kit/2-brand/_template.md`. The build reads these exact role names:
   - `bg`, `paper`, `ink`, `ink-soft`, `accent`, `soft`, `hi`, `sand`, `dark`, `on-dark`, `on-dark-2`, optionally `on-hi`.
   - Format: `- hi: #D30805`. A malformed line is silently ignored.
4. **Derive helper colors** when the brand has only 2–3 colors:
   - a soft tint of the main color for highlights;
   - a sand or neutral for alternating bands;
   - **a lighter twin of the main color for small text on dark backgrounds**. Rickey: `#D30805` on black is 3.4:1, so small text uses `#FF6B63` at 6.8:1.
5. **Check contrast** (WCAG): body text at least 4.5:1, large text at least 3:1. The build prints a contrast report. Fix failures with a darker or lighter twin, and say what you changed.
6. **Fonts:** free Google Fonts only. Use 3 roles:
   - **Big:** headings, weight 800.
   - **Standard:** body text.
   - **Handwritten:** short notes, upright only. The build doesn't load italics.
   - If the brand font isn't free, pick the closest free match and say so. Check it loads: `curl -s -o /dev/null -w '%{http_code}' "https://fonts.googleapis.com/css2?family=Poppins:wght@800"`.
7. **Plan the section rhythm:**
   - dark bands about every 3rd section, so the page never reads as one long section (Rickey: sections 2, 5, 8, 11);
   - a dark alert bar on top and a dark footer.
8. **Show the palette as swatches,** not just hex codes. David: "I can't see the colors, just numbers". Render a small HTML swatch card in the browser pane, or as an image.
9. **Ask:** "Does this feel like [brand]?" Re-show until yes. Log the decision in `learned-rules.md`.

**Rickey's final brand kit:** `examples/rickey-headstart/brand-kit.md`.
- **Colors:** red `#D30805`, black `#101017`, white, plus derived helpers.
- **Fonts:** Poppins 800 for big text, Lato for body text, Caveat for handwriting. This was David's "font test" in round 1, replacing the brand guide's Archivo Black / Permanent Marker, and it stayed.

---

# How it was done on the Rickey page
## E. Brand method

### E1. Source and extraction
1. **Source priority:** the client's brand guide PDF, then logo files, then a palette pick from `all-brand-palettes.pdf`, then "tell me the vibe, I'll suggest three". For Rickey it was the guide: `PF/branding/Game Tape Brand Guidelines.pdf` (11.8 MB, 9 rendered pages).
2. **Rendering:** JXA + PDFKit renders each page to PNG at 1400 px wide and returns `page.string` (the text layer).
3. **Exact values come from the text layer, not pixel picking.** The colors page (page 7) reads "RED #D30805 / BLACK #101017 / WHITE #FFFFFF". The typeface page (page 8) reads "HEADING TYPEFACE ARCHIVO BLACK / SUBTEXT TYPEFACE POPPINS / LOGO TYPEFACE 210 슈퍼 사이즈". Claude opened pages 6 (logo systems: REC mark plus GAME TAPE wordmark, in black-on-white, white-on-black, red variants), 8 and 9 as images. The logo typeface isn't a Google Font, so the page uses the logo PNGs instead.
4. **When there's no guide** (Nov 19), pixel-sample the banner: `sips -s format bmp`, then Python reads the BMP and counts colors in rectangles. Use the darkest-cluster mode for text and the most saturated cluster for accents.

### E2. Derived helper colors
The kit's template needs 5 colors plus a very dark ink and a light sand. The guide has 3, so Claude derived these and said so:

| Hex | Name | Role | Why |
|---|---|---|---|
| #F4F2EF | warm light grey | `sand` (alternate band) | "so the page doesn't feel like one long white sheet" |
| #FFD6D3 | light red tint | `soft` (highlighter marks, soft shadows) | a highlighter in the brand color that body text still reads on (14.26:1 with black) |
| #FF6B63 | light red (T) | `on-dark-2` (secondary text on black) | brand red on black is only 3.43:1 |
| #4A4A55 | soft grey | `ink-soft` | 8.74:1 on white |

### E3. Contrast checks run (Python, WCAG formula)
| Pair | Ratio | Use |
|---|---|---|
| #101017 on #FFFFFF | 18.94 | body text |
| #101017 on #F4F2EF | 16.95 | text on the grey band |
| #4A4A55 on #FFFFFF / #F4F2EF | 8.74 / 7.82 | secondary text |
| #D30805 on #FFFFFF | 5.52 | red accent words, numbers |
| #D30805 on #F4F2EF | 4.94 | red on the band |
| #FFFFFF on #D30805 | 5.52 | button text |
| #101017 on #D30805 | 3.43 | not used for text |
| #D30805 on #101017 | 3.43 | **large headline words only** on black |
| #FF6B63 on #101017 | 6.8 | small text on black |
| #C9C9D1 on #101017 | 11.51 | (tested, not used) |
| #101017 on #FFD6D3 | 14.26 | text on a highlighter mark |

`build_page.py` re-checks on every build: ink/bg 18.9, ink/paper 18.9, ink-soft/bg 8.7, ink/sand 17.0, on-dark/dark 18.9, on-dark-2/dark 6.8, button 5.5, accent/paper 5.5 (large text only).

### E4. Role map (final, `brand-kit.md`)
| Role | Hex | Job |
|---|---|---|
| bg | #FFFFFF | page background |
| paper | #FFFFFF | cards |
| ink | #101017 | body text, borders |
| ink-soft | #4A4A55 | secondary text |
| accent | #D30805 | shadows, handwritten notes, numbers |
| soft | #FFD6D3 | highlighter, soft shadows |
| hi | #D30805 | button fill, check marks |
| on-hi | #FFFFFF | button text |
| sand | #F4F2EF | alternate band |
| dark | #101017 | dark sections |
| on-dark | #FFFFFF | text on dark |
| on-dark-2 | #FF6B63 | secondary text on dark |

Vibe line: "raw, real, hit-record energy. Bold black type, one hard red, lots of white. Straight talk, no guru gloss."

### E5. Fonts: how the pairing came about
- **v1 (`brand-kit-v1.md`):**
  - Headings: Archivo Black 400, from the guide. It "only comes in one weight".
  - Body: Poppins, from the guide.
  - Handwritten: Permanent Marker. This was **Claude's pick**, because the guide has no handwritten face and "a marker style fits the raw 'hit record' feel".
- **v2 (David's request at #16, labeled a "font test"):**
  - `- Big: Poppins 800`, `- Standard: Lato`, `- Handwritten: Caveat`.
  - **Claude didn't derive this pairing. David asked for it.** Claude checked the fonts exist and have metric fallbacks: Lato and Poppins are in `font-fallbacks.json`; hand fonts don't need one. It kept `brand-kit-v1.md` so the team can switch back, and verified loading in the browser (`document.fonts.check('800 16px Poppins')`, Lato, Caveat).
  - The build generated `family=Poppins:wght@700;800;900&family=Lato:wght@400;700;900&family=Caveat` with fallbacks `'Poppins Fallback'` (Arial, size-adjust 112.6% / 107.8% bold) and `'Lato Fallback'` (97.3% / 92.3%).
  - *Inference, not stated in the session:* the test keeps the brand's own secondary face (Poppins) for headings, so it stays on-brand but softer than Archivo Black. Lato is easier to read at 18 px body size, and Caveat is lighter and friendlier than Permanent Marker.
  - **The live page runs on the test fonts, not the brand guide's.** Teammates should treat "Poppins/Lato/Caveat" as this client's choice. The default for a new client is the guide's fonts.

### E6. Dark-section rhythm
- In this kit, `bg` = `paper` = white, so the kit's alternation of "none / s-paper / s-sand / one s-dark" shows only white and grey.
- **v1:** hero (white with a soft radial tint), then 2 paper, 3 none, 4 sand, **5 dark**, 6 none, 7 sand, 8 none, 9 paper, 10 sand, 11 none, 12 paper, 14 sand, then a black footer. One dark band, so it read as "one continuous section".
- **v2 and final:** black alert bar → hero → **2 dark** → 3 white → 4 grey → **5 dark** → 6 white → 7 grey (+ guarantee block) → **8 dark** → 9 white → 10 grey → **11 dark** → 12 white → 14 grey → **black footer**. Black about every third section.
- **CSS needed when a section turns dark:**
  - The kit's `.outcome` and `.claim` cards stay white, so their text must be ink: `.s-dark .outcome p,.s-dark .claim p{color:var(--ink)}`.
  - Handwritten doubts: `.s-dark .maybes{color:var(--on-dark-2)}`.
  - Video cards on dark: `border:2px solid var(--on-dark); box-shadow:5px 5px 0 var(--accent)`.
  - The kit already handles `.s-dark h2/h3/p`, `.s-dark .card p` (ink), `.s-dark mark` (accent at 75%), `.s-dark .btn` (on-dark border plus an accent shadow) and `.s-dark .fine` / `.hand` (on-dark-2).
- **Tip for the playbook:** set `bg` to a faint tint, or plan the dark bands from the start. Don't rely on none/s-paper alternation when both are white.

### E7. Showing the palette
Render swatches (name, hex, job) for brand colors and helpers separately, plus a mini page using the real fonts: a white section with an accent word, a highlighter mark, the button and a handwritten note, then the band, then a dark section. Ask "Does this feel like <brand>?" and offer example adjustments.

### E8. AI image prompts
This is from `image-prompts.md`, written at 13:12 after #20. It's in this slice's file list.
- **Workflow:** attach `offer-1-image-v2.png` (the style to match) plus a clear front-facing photo of the creator. Paste the style brief once, then one prompt per image. Save each result under the given file name.
- **Style brief rules:**
  - Photo-realistic 3D mockup on a pure white or light grey seamless background, soft studio light.
  - Brand colors only (#D30805, #101017, white).
  - Logo: "bold, black, slanted italic capital letters, followed by a red rounded badge with a white dot and the word 'REC'".
  - Heavy condensed all-caps titles.
  - Creator likeness: "same face, skin tone, rimless glasses, short hair".
  - Spell every quoted word exactly.
  - **Never show money amounts, income, earnings, sales numbers, payout notifications, prices, star ratings, follower counts or testimonials.**
  - Landscape 16:10, no border, no watermark.
- **Prompts:** 1 `whatsapp-channel.png`; 2 `course-7-day.png`; 3 `challenge-30-day.png`; 4 `templates.png` (later unused: not in the offer); optional 5 `starter-product-list.png`.
- **"Not AI":** for the story section, real photos only. "Please don't generate fake 'old' photos of him for this, since the story says they're real."
- **From `learned-rules`:** watch for brand logos (a Nike swoosh) on generated sneakers. The 30-day challenge image is a built-in phone visual until a real image exists. Never use the PDF cover for it.

---

