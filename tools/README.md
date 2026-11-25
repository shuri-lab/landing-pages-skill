# tools/: scripts (no installs except where noted)

| Tool | What it does | Run |
|---|---|---|
| `rebuild.sh` | One command: expand repeated parts → kit build → kit check → export (→ optional publish into a repo) | `tools/rebuild.sh my-sales-page "Title \| Brand" [--publish <repo> <pages URL>]` |
| `expand_body.py` | Writes the button label, checkout link, logo strips, video cards and screenshot slider from `page-config.json` (used by rebuild.sh) | `python3 tools/expand_body.py body-src.html body.html --config page-config.json` |
| `optimize_images.py` | WebP at display size by file-name role (hero-, product-, brand-, shot-…). Needs Pillow | `python3 tools/optimize_images.py my-sales-page/images` |
| `shoot.mjs` | Real phone (393×852) and desktop screenshots + first-screen measurements through Chrome. Needs Node 22+ and Chrome | `node tools/shoot.mjs my-sales-page/index.html --out my-sales-page/shots --full` |
| `mac/pdf2png.js`, `mac/pdf2png-n.js` | PDF pages to PNG + the text layer (macOS, no installs) | `osascript -l JavaScript tools/mac/pdf2png.js file.pdf outdir 1400` |
| `mac/sheet.js` | Contact sheet of many images (to pick visually) | `osascript -l JavaScript tools/mac/sheet.js <dir> <out.png> <n>` |
| `mac/bbox.py` | Find the empty margin around a logo PNG (for trimming) | `python3 tools/mac/bbox.py logo.png` |
| `build_funnel_pages.py` | Part 2: checkout column, upsell(s), thank-you page, emails, GHL texts and local previews from one JSON file. Computes totals; refuses rule-breaking copy (52 bad inputs in `test/part-2/probes.py`) | `python3 tools/build_funnel_pages.py my-funnel-pages/funnel-pages.json` (`--check`, `--final`) |
| `funnel_templates/` | The approved CSS behind those pages, with brand tokens (`%%ACCENT%%` …) | used by the line above |
| `check_funnel_pages.mjs` | Opens the Part 2 previews in Chrome at phone and desktop size, checks them, saves screenshots | `node tools/check_funnel_pages.mjs my-funnel-pages` |
| `snippets.md` | Reusable code from the Rickey build: QA helpers, lazy video, sliders, contrast function… | Copy what you need |

Tested on Nov 20 2026: `rebuild.sh` on Rickey's sources reproduces the live page byte for byte; `test/grade.py` (which uses `shoot.mjs`) scores it 50/50.
