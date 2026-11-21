# Tools and links

Everything the playbook uses: what each tool is for, where it lives, and who has access. No passwords live in this repo. Ask TJ for logins.

## The core tools

| Tool | What we use it for | Where | Access |
|---|---|---|---|
| **Claude Code** (desktop app, Code tab, or the CLI) | Runs the whole playbook: reads the project, writes copy, builds the page, checks it in a browser, fixes it | claude.ai/code, or the Claude desktop app | Your own Claude account |
| **Claude's browser pane** (built into the desktop app) | Looking at the page at phone and desktop sizes, measuring the fold, studying reference pages | Desktop app, right side | Built in |
| **Buy-Now Sales Page: AI Sales Page Tool** (by Isabelle, tasteofreedom.com) | Writes the first full draft of the sales page copy from 4 steps of inputs (Product, Buyer, Why Yours, Proof) | https://tasteofreedom.com/the-buy-now-sales-page-tool-page (opens without login; answers save in that browser only) | Public page. The course portal (below) needs the shared login: ask TJ |
| **Buy-Now Sales Page: course portal** | Isabelle's lessons, the Sales Page Generator download ("Claude creates your entire sales page" section), bonuses | https://tasteofreedom.app.clientclub.net/ | Shared login: ask TJ |
| **Sales Page Generator kit** (Isabelle's Claude kit) | The build engine: copy structure (14 sections), brand kit, image slots, page builder, checker, export, publish guide, in-page editor | `kit/` in this repo (unchanged copy) | Included |
| **Brand palettes PDF** | 42 ready color palettes when a client has no brand | `kit/all-brand-palettes.pdf`, `kit/palettes/` | Included |
| **Landing-pages framework v2** | Rewriting the hero headline and subheadline (and checking every section's job) after the tool's draft | `knowledge/frameworks/landing-pages-framework-v2.txt` + summary in `knowledge/frameworks/HOW-WE-USE-THEM.md` | Included |
| **ThrillX landing page prompts** | Ready prompts for headline, subheadline, pain section, value props, CTA | `knowledge/frameworks/thrillx-landing-page-prompts.md` | Included |
| **Hormozi VSL framework** | For pages that will get a VSL later | `knowledge/frameworks/alex-hormozi-vsl-framework.txt` | Included |
| **ChatGPT (image generation)** | Making the images a page is missing (product mockups, bundle shots, a phone showing a channel, section visuals). We write the prompts, a person pastes them in ChatGPT as one batch | chatgpt.com | Team ChatGPT account |
| **Cloudinary** | Hosting the short muted video loops and serving them light (`w_320,q_auto:eco,ac_none,du_10,f_auto`) | cloudinary.com (Rickey's videos are on cloud `fje4fcoe`) | Team account |
| **GitHub + GitHub Pages** | One repo per project (page, images, source files), a free preview link to share with the team and the client | github.com/shuri-lab | Ask David to be added to the org |
| **Python 3 (standard library)** | The kit's build, check and export scripts | Comes with macOS | Built in |
| **Pillow** (Python image library) | `tools/optimize_images.py` makes WebP images at display size | `python3 -m pip install Pillow` (or a venv) | Free |
| **Node 22+ and Google Chrome** | `tools/shoot.mjs` takes phone/desktop screenshots and measures the fold; `test/grade.py` uses it | nodejs.org, google.com/chrome | Free |

## Out of scope here (separate skill later)

- **GoHighLevel**: checkout, order bump, one-click upsell, thank-you page, course hosting (Memberships), delivery workflows. The Rickey funnel lives on davidhsai.com (`/headstart-page`, `/headstart-checkout`, `/headstart-upsell`, `/headstart-thank-you`). The way we load our HTML into GHL (a "loader" custom-code block that fetches the page from GitHub Pages) is documented in `stages/9-share.md` because it works with any builder.

## Project links for the worked example (Rickey · Game Tape)

See `examples/rickey-headstart/links.md`.
