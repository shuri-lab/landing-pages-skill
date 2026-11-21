# Stage 5 of 9: Build the page

**Goal:** `my-sales-page/index.html`, built with the kit, with the **house style built in from the first draft**.

**Read before writing a line:**
- `kit/sales-page-generator-kit/kit/4-build/sections.md`: the layout of the 14 sections.
- `example-body.html`: for structure only. It is Isabelle's page, so never reuse its words, images or links.
- `knowledge/house-style.md`
- `knowledge/components/CATALOGUE.md`
- `knowledge/pitfalls.md`

## Steps
1. **Start from the working example, not from zero.** Copy the component markup, CSS and JS you need from `examples/rickey-headstart/body-src.html` (catalogue line numbers point into it):
   - alert bar, hero, logo marquee
   - video carousel, outcome cards, pain cards
   - story split with photos, offer stack, guarantee
   - screenshot slider, sticky bar, footer
   Swap in the new copy, images and brand. Colors come from the brand kit's CSS variables, so no hex codes are hard-coded except in the alert-bar gradient.
2. **Write `my-sales-page/body-src.html`:**
   - Each section is `<section data-section="N" data-name="…">`.
   - Copy goes in exactly as approved in `copy.md`.
   - Use markers for the repeated parts: `@@CTA@@`, `@@LOGOS@@`, `@@VIDEOS@@`, `@@SLIDER@@`.
   - Put custom CSS in one commented `<style>` block at the top, with phone rules last.
3. **Write `my-sales-page/page-config.json`:** the button label, logos, videos and slider screenshots. See `examples/rickey-headstart/page-config.json`.
4. **Build and check in one command:**
   ```bash
   PLAYBOOK/tools/rebuild.sh my-sales-page "Offer name | Brand"
   ```
   This runs expand → `build_page.py` → `check_page.py` → export. Fix everything `check_page.py` flags.
   - **What it doesn't catch:** button labels and `PASTE-YOUR-CHECKOUT-LINK` hrefs.
   - **That's why** `test/grade.py` exists. Run it too (Stage 6).
5. **Images:** run `python3 PLAYBOOK/tools/optimize_images.py my-sales-page/images` **before the first build**: `expand_body.py` writes logos, slider and screenshots as `images/opt/<name>-<width>.webp`. Hand-written `<img>` tags can use the originals until Stage 8 switches them to WebP.
6. Go to Stage 6. **Don't show the client before the self-review.**

## Rules that save rework (from the Rickey rounds)
- **The hero, on phones:**
  - order: alert bar → logo → proof pill → headline → **hero image** → subheadline → button → fine print;
  - all of it fits 393×852;
  - put the image first in the HTML for `fetchpriority`, and order it with CSS.
- **Hero, on desktop:** two columns (text left, mockup right), and the logo strip still shows on the first screen at 1280×800.
- **Buttons:** every one is `href="#buy"`. The offer stack button is the only checkout link.
- **Back up** `body-src`, `copy` and `index` as `-vN` before each round.
- **Edit with guarded scripts** (assert the old text exists before replacing it) or the Edit tool. A failed match leaves the file untouched.

## Process and tooling rules (exact, from the Rickey build)
### C3. Process rules
| Rule | Rickey example | Why |
|---|---|---|
| Follow the kit steps 0 to 5. Ask one question at a time and show "Step N of 5". Offer 2 answer buttons. | Every turn ended with one ask | The client stays oriented. Fast. |
| Ask for the project folder at Step 1 and inventory it yourself. | #10: "you have averything you need regarding branding and images" | Saves upload rounds and finds assets the client forgot (videos, deliverable PDFs). |
| Before each feedback round, back up under new names: `copy-vN.md`, `body-vN.html`, `index-vN.html`, `brand-kit-vN.md`. | v1 before the 9-point round; up to v12 by the end | Kit: "Never overwrite… save new versions". Makes the "have it as it was before" rollback (#31) trivial. |
| Log every client decision in `learned-rules.md` right away, one line each. When a rule changes, write an explicit "OVERRIDES …" line. | "OVERRIDES the Instagram lines above: section 3 story text stays exactly as the original copy" | Kit rule. It carries decisions across rebuilds and sessions. |
| Keep `copy.md` in sync with every text change on the page, including new UI text such as the alert bar. | The alert line was added under `## SECTION 1` | `check_page.py` can then prove every approved line is on the page |
| Look at every image. Read its text. Place it by content. Present a numbered table with confidence. Flag rights, PII and endorsement risks, then follow the client's call and restate the flags in the final summary. | Getty photo, logo strip, commenters' names | Kit rule and liability |
| QA every build at desktop 1280×860 and phone 375×812 before reporting. Reset the viewport after. | 6 issues found and fixed before the first report | Don't ship what you haven't seen |
| After each round: rebuild, check, grep the rule counts, reopen in the user's browser, "refresh it if the old version is still showing" | `open my-sales-page/index.html` after every round | The client reviews in their own browser |
| Report per numbered item. Disclose anything beyond the literal request. | En-dash ranges disclosed | Trust; easy to veto |
| If client text breaks a standing rule, apply the rule, say so, and offer alternatives. | Em dash in the new subheadline became a colon, with a period or comma offered | Consistency without overriding the client |
| Treat a move-on reply as approval, but say so out loud. | "I'll take that as a yes on the values" | Avoids silent assumptions |
| Copy questions come in page order: hero → price anchor → proof → headline. | #3 to #8 | Each answer can unblock the next |

### C4. Tooling rules
| Rule | Detail / command | Why |
|---|---|---|
| Run the build and check from the kit root | `cd sales-page && python3 kit/4-build/build_page.py --body my-sales-page/body.html --kit my-sales-page/brand-kit.md --out my-sales-page/index.html --title "TikTok Shop Headstart \| Game Tape"`, then `python3 kit/4-build/check_page.py --page my-sales-page/index.html --copy my-sales-page/copy.md` | Kit paths are relative |
| Know what `check_page.py` matches | Each `copy.md` line of 25 characters or more (after stripping `#*- `) must have its first **40 normalized characters** (lowercase a–z0–9) in the page's visible text plus alt text. Skipped: lines starting with `>`, `<!--`, `(`, `[`. So **button labels are never checked**, `> image:` notes are skipped, `<ol>` numbers must be real text, and duplicate images need alt text. `{FILL IN…}` / `{{…}}` / `TODO` / `[ASK…]` in visible text are FIX items. `class="ph"` boxes are only a NOTE. | Write `copy.md` to fit, and know what isn't covered |
| `check_page.py` does **not** catch `href="PASTE-YOUR-CHECKOUT-LINK"`, only empty or `#` hrefs. Grep for it. | `grep -c 'PASTE-YOUR-CHECKOUT-LINK' my-sales-page/body.html` (13 in v1) | Avoid publishing dead buttons |
| Grep for reference leakage too | `grep -ci 'isabelle\|tasteofreedom\|buy-now' body.html` → 0 | Belt and braces on the reference-phrase check |
| Know how `build_page.py` reads the brand kit | Roles via `^\s*[-*]\s*(ink-soft\|on-dark-2\|on-dark\|on-hi\|bg\|paper\|ink\|accent\|soft\|hi\|sand\|dark)\s*(\(...\))?\s*:\s*#RRGGBB`. Required: bg, paper, ink, ink-soft, accent, soft, hi, sand, dark, on-dark, on-dark-2 (on-hi optional). Fonts from lines `- Big…:`, `- Standard…:`, `- Handwritten…:` as "Name 800". Loads head font weights 700/800/900 (+ the given weight), body 400/700/900, hand at the default weight only (so **no italics**). Prints a contrast report. **Ignores the Logo field**, so place logos by hand. Adds class `anim` to `<html>`. | A malformed kit line is silently ignored |
| macOS without poppler, PIL or ffmpeg | PDFs: JXA + PDFKit (`osascript -l JavaScript pdf2png.js <pdf> <outdir> 1400`) for page PNGs and the text layer. Resize/convert/crop: `sips -Z`, `-s format jpeg -s formatOptions 82`, `-c H W --cropOffset Y X`. Logo bounding box: pure-Python PNG decode. Contact sheet: JXA + AppKit. Video: Cloudinary URL transforms (`avconvert` exists but wasn't needed). | Works on a stock Mac |
| Check fonts before committing to them | `curl -s -o /dev/null -w '%{http_code}' "https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap"`, plus grep `kit/4-build/font-fallbacks.json` for metric fallbacks | Avoids invisible fallback fonts |
| Local preview server | `.claude/launch.json`: `python3 -m http.server 8765 --bind 127.0.0.1 --directory sales-page/my-sales-page`, started with `preview_start` | The Browser pane can screenshot and run JS |
| QA helpers in the page | Remove `anim` from `<html>` (shows all fade-ins); `scroll-behavior:auto`; `__go(n,offset)` to jump to a section; check `scrollWidth` vs `innerWidth`; list elements past the right edge (sliders excluded); list unloaded images; check video `paused`/`readyState`/`muted`; `document.fonts.check(...)` | Fast, objective checks |
| Edit with guarded Python transforms | `python3 -I - file <<'EOF' … assert old in h … write at end` | A failed pattern leaves the file untouched (this happened once, safely) |
| After a script edits a file, re-read it before using Edit tool calls that depend on context | The tool warned "file had been modified on disk" | Stale context leads to wrong edits |
| The scratchpad is temporary | `tools/mac/` holds `pdf2png.js`, `pdf2png-n.js`, `bbox.py`, `sheet.js`, `layout2.py`, `expand_body.py (was gen_body.py)`, `rebuild.sh`, `optimize_images.py` | Save the useful ones into the playbook (Appendix) |

## Mac helpers

`tools/mac/`: `pdf2png.js` / `pdf2png-n.js` (PDF pages to PNG plus the text layer, via `osascript -l JavaScript`), `sheet.js` (contact sheet of images), `bbox.py` (trim empty space around a logo PNG). Snippets: `tools/snippets.md`.
