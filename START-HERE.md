# SALES PAGE PLAYBOOK: START HERE (instructions for Claude)

You are building a high-converting, mobile-first sales page for a client's offer. You follow this playbook from start to finish: 9 stages, one at a time. You do the work yourself (read files, write copy, build, check in a browser, fix). You ask the person only for what you can't find or decide from the playbook.

This playbook is how David and Claude built Rickey's "TikTok Shop Headstart" page (Nov 2026), turned into a process anyone can run for any project. The quality bar is that page: `examples/rickey-headstart/screenshots/`, live at https://shuri-lab.github.io/rickey-tiktokshop-project/.

`PLAYBOOK` below means the folder this file is in.

## How to run the conversation
- **Start at Stage 0 right away.** Show where you are: **"Stage 3 of 9: brand"**.
- **Read the whole project folder before asking anything.** Then ask one question at a time, in plain words, with 2–3 answer options when that helps. Never ask what the files already answer.
- **Before each stage:** read that stage's file in `stages/` in full.
- **Before Stage 1:** read `knowledge/copy-context.md`. It says what context the copy needs, and there's a gate: no copy work until the brief passes it.
- **Before writing or building anything:** read `knowledge/house-style.md`, `knowledge/copy-rules.md` and `knowledge/pitfalls.md` once. They hold the 12 rounds of feedback that made the Rickey page good. **Apply them from the first draft. Don't wait for the client to ask.**
- **Log every client decision** as one line in `my-sales-page/learned-rules.md`, and re-read that file before every build.
- **Back up before every big change** (`copy-v2.md`, `body-src-v2.html` …). Never delete or overwrite the client's files.
- **Mark your own wording.** When you write a line the client didn't give you, say so in your report.
- **Be autonomous between questions.** Build, check, fix and re-check without asking permission for each step. Stop and ask only at the gates marked ★ below.

## The 9 stages

| Stage | File | What you produce | ★ Gate (needs the person) |
|---|---|---|---|
| 0 Setup | `stages/0-setup.md` | Working folder, tools checked | The project folder path, if not given |
| 1 Context | `stages/1-context.md` + `knowledge/copy-context.md` | `brief.md`: every fact, with its source, passing the copy-context gate | ★ "Is this summary right?" (especially: what's really in the offer) |
| 2 Copy | `stages/2-copy.md` (+ `knowledge/copy-fallback.md` if the tool is down) | Copy-tool output (2 runs) → hero reworked with `knowledge/frameworks/` → structure check → `copy.md` | ★ Hero pick (e.g. "1 + A") · ★ item values · ★ proof plan if there are no testimonials · ★ approve the rules pass |
| 3 Brand | `stages/3-brand.md` | `brand-kit.md`, swatches shown | ★ "Does this feel like you?" |
| 4 Media | `stages/4-media-sourcing.md` | `image-plan.md`, `image-prompts.md`; images checked and placed | ★ The person runs ChatGPT and grabs screenshots/photos (one message with the full list, then wait) |
| 5 Build | `stages/5-build.md` | `body-src.html`, `page-config.json` → `index.html` via `tools/rebuild.sh` | none |
| 6 Self-review | `stages/6-self-review.md` | `test/grade.py` clean, `review.md`, `shots/`: every section checked at phone and desktop size | none. Don't show the client before this passes |
| 7 Feedback | `stages/7-feedback-rounds.md` | Rounds of client changes, each logged | ★ The client's feedback |
| 8 Speed | `stages/8-speed.md` | WebP images, light videos, under ~1.5 MB of images on a phone | none |
| 9 Share | `stages/9-share.md` | Repo + GitHub Pages link, README, paste-ready file | ★ Create the repo / OK to make it public / OK to send any email |

Order in practice: 0 → 1 → 2 → 3 → 4 → 5 → 6 → show the client → 7 (repeat) → 8 → 6 again → 9.

## Always
- **Never invent** facts, numbers, results, names, prices, testimonials or images. If something is missing, ask, or drop that spot. A live page never shows a placeholder.
- **Never rewrite the client's own words** (the founder story above all) without asking.
- **Phone first:** 393×852 (iPhone 16). The hero, through the button, fits the first screen. Then 1280×800, 1440×900 and 1920×1080.
- **One button label everywhere.** Every button jumps to the offer stack; only that one goes to checkout.
- **Promise sales or results, never income.** Label numbers correctly.
- **Never put passwords, API keys or payment details in any file.** Logins for tools are "ask TJ".
- **Never publish, upload, push or email** without the person's OK.

## When you finish
Tell the person, in a few lines:
- the link or file;
- the phone fold numbers;
- what's still open (missing images, licenses, checkout link);
- which lines are your wording;
- the `test/grade.py` score.

Then offer the next step: client feedback, speed pass or share.

## Map of this repo
- `stages/`: what to do, step by step
- `knowledge/`: rules (`copy-rules.md`, `house-style.md`, `design-rules.md`), `review-checklist.md`, `feedback-log.md` (why each rule exists), `pitfalls.md`, `components/CATALOGUE.md`, `frameworks/` (landing-page framework + prompts), `prompts/`, `templates/`, `tools-and-links.md`, `references.md`, `upsell-and-bump.md`
- `kit/`: the complete "Sales Page Generator - for clients" folder (Isabelle's kit, the build engine, unchanged; see `kit/README.md`)
- `tools/`:
  - `rebuild.sh` (one-command build), `expand_body.py`, `optimize_images.py`
  - `shoot.mjs` (screenshots + fold measurements)
  - `mac/` and `snippets.md`
- `examples/rickey-headstart/`: the full worked example (brief, tool inputs, tool output, final copy, brand kit, body source, learned rules, prompts, screenshots, timeline), with the complete "Rickey-TikTokShop-Project-Files" folder in `project-files/` and extra context in `more-context/`
- `test/`: the replication test, the rubric and the grader
