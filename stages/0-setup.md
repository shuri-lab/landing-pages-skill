# Stage 0 of 9: Setup

Do this quietly, then report in 2–3 lines.

## 1. Where things go

- **PLAYBOOK** = this repo. It is read-only: never edit files in the playbook while building a page.
- **PROJECT** = the client's folder with their files (research, offer docs, brand guide, photos, videos).
  - Ask for its path if you weren't given one.
  - Never move, rename or delete the client's files.
- **WORK** = `PROJECT/my-sales-page/`. Everything you make goes here. Create:
  ```
  my-sales-page/
    images/          originals you place on the page (copied, never edited)
    images/opt/      the WebP versions you make in Stage 8
    shots/           screenshots from tools/shoot.mjs
    brief.md         Stage 1
    copy.md          Stage 2 (+ copy-tool-output-run1.md, run2.md, tool-inputs.md)
    brand-kit.md     Stage 3
    image-plan.md    Stage 4 (+ image-prompts.md)
    body.html        Stage 5 (the page body you write)
    index.html       built page
    learned-rules.md every client decision and piece of feedback, one line each
  ```
- **Versions:** before a big change, save a copy as `copy-v3.md`, `body-v3.html` and so on. Never overwrite the only copy.

## 2. Check the tools (one command each)

| Check | Command | If it fails |
|---|---|---|
| Python 3 | `python3 --version` | macOS: `xcode-select --install` |
| Pillow (for Stage 8) | `python3 -c "import PIL"` | `python3 -m venv .venv && .venv/bin/pip install Pillow`, then use `.venv/bin/python` for `tools/optimize_images.py` |
| Node 22+ | `node --version` | Install from nodejs.org (only needed for `tools/shoot.mjs` and the test grader) |
| Chrome | `ls "/Applications/Google Chrome.app"` | Install Chrome, or set `CHROME_PATH` |
| Browser pane | Open https://example.com in the pane | If there is no pane (CLI only), use `tools/shoot.mjs` for every visual check |
| Kit | `ls PLAYBOOK/kit/sales-page-generator-kit/kit` | The kit is in this repo; don't download another copy |

## 3. What a person may need to do (say it up front, in one short list)

- Give you the project folder, or confirm the one you found.
- Answer the questions you can't answer from the files (Stage 1 lists them).
- Run the image prompts in ChatGPT and drop the results in a folder (Stage 4).
- Grab screenshots from the founder's TikTok/Instagram, if the page needs them (Stage 4).
- Give feedback on the page (Stage 7).
- Create the GitHub repo if you're sharing it (Stage 9).

Say: **"Ready. Stage 1 of 9: the context."**
