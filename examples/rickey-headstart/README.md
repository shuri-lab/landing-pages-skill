# Worked example: Rickey · Game Tape · TikTok Shop Headstart ($27)

The page this playbook was built from. Live: https://shuri-lab.github.io/rickey-tiktokshop-project/ · repo with all raw project files: https://github.com/shuri-lab/rickey-tiktokshop-project

| File | Stage | What it is |
|---|---|---|
| `brief.md` | 1 | The Project Brief, every fact sourced |
| `tool-inputs.md` | 2a | The 16 AI Sales Page Tool fields, filled from the brief (reconstructed) |
| `copy-tool-output.md` | 2a/2b | The tool's raw output (Run 1, chosen) with the reworked hero options (⭐ picks) |
| `copy-final.md` | 2d/7 | The approved copy after all feedback (kit format) |
| `brand-kit.md` | 3 | Colors, role map, fonts |
| `image-prompts.md` | 4 | The ChatGPT prompts that made the page images |
| `body-src.html` | 5 | The full page source: every component (the catalogue's line numbers point here) |
| `page-config.json` | 5 | Button label, logos, videos, slider for `tools/expand_body.py` |
| `learned-rules.md` | 7 | Every client decision, in order (54 lines) |
| `screenshots/` | 6 | Final page at phone 393×852 and desktop 1440×900 (first screen + full page), and the first draft (`early-v1/`) |
| `timeline.md` | all | Every message David sent during the build, in order |
| `open-items.md` | all | What the client had to supply by hand, assumptions, kit gaps |
| `links.md` | all | Every link for this project |
| `project-files/` | inputs | **The complete "Rickey-TikTokShop-Project-Files" folder**: research, founder answers and voice, deliverables, branding, logos, videos, screenshots, offer images, ChatGPT images, the copy tool's output |
| `more-context/` | inputs | Meeting transcripts, the whole plan, the knowledge base, offer stack and critique PDFs, the earlier Game Tape page |
| `upsell/` | (extra) | The $97 upsell page and the checkout's left column as first hand-built (HTML loaded into GoHighLevel) |
| `funnel-pages/` | F1 to F5 | **The same pages as data** (`funnel-pages.json`), what it builds (`dist/`), the local previews and their screenshots (`shots/`). Links are empty on purpose |

To rebuild it yourself from these files: copy the `sales-page/my-sales-page` layout (body-src, page-config, brand-kit, copy, images) and run `tools/rebuild.sh`. It reproduces the live page byte for byte.

**Version:** `body-src.html`, `copy-final.md` and `page-config.json` are the approved v1.1 (Nov 24: new section-2 header, every button straight to checkout). The full-page screenshots were taken before it, so they show the old header.
