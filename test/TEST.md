# The replication test

**What it proves:** someone who wasn't there (Moses, or anyone on the team) can follow this playbook and produce a sales page as good as the one David and Claude built for Rickey on Nov 20 2026, without David's 12 rounds of feedback.

**Who:** the person taking the test runs Claude Code with this repo. **TJ** grades it with `rubric.md` and `tj-review-sheet.md`.

**Time box:** 3–4 hours of work (most of it is Claude's). Rickey's original took a full day of back and forth.

## The task

Build the **Offer 1 sales page for "TikTok Shop Headstart" ($27, Rickey · Game Tape)** from the raw inputs only, by following `START-HERE.md`.

### Rules
1. **Use only the inputs in `inputs.md`.**
   - Do not open our finished page or its outputs: in `examples/rickey-headstart/`, the files `copy-final.md`, `learned-rules.md`, `brief.md`, `tool-inputs.md`, `timeline.md`, `open-items.md`, the `screenshots/` and `upsell/` folders, and `test/reference/`. Also not the `rickey-tiktokshop-project` repo's `index.html` / `offer-1-sales-page/`. The `project-files/` and `more-context/` folders are the inputs and are allowed.
   - The playbook's `knowledge/` folder (house style, components, rules) **is** allowed, and so is `examples/rickey-headstart/body-src.html` **only as the component source** that `stages/5-build.md` points to. Copying its components is the point. Copying its copy is not: the copy must come from the tool output plus the client's answers.
2. **`client-answers.md` stands in for the client.**
   - Use it whenever the playbook says to ask the client.
   - If it doesn't cover a question, make the call the playbook recommends and log it in `learned-rules.md`.
3. **Stage 2a.**
   - **Required:** write `tool-inputs.md` (all 15 fields, from your brief only). It's graded: it proves you gathered the right context.
   - **Optional:** running the tool itself (https://tasteofreedom.com/the-buy-now-sales-page-tool-page, no login).
   - **Build from:** the tool's raw output in `inputs.md`, so every test-taker starts from the same draft.
   - **Also required:** stages 2b–2d (hero rework, structure check, rules pass).
4. **Stage 4 images:** the AI images from the original build are in the inputs.
   - Write the image plan and the prompts anyway (they're graded).
   - Use the provided images instead of re-generating them.
5. **No feedback rounds from a human.** The page is graded as the playbook produces it (Stages 1–6 and 8). Stage 9 is optional (a GitHub Pages link is nice for TJ but not required).

## What to hand in
A folder `my-sales-page/` (zip it or push it to a repo) with:
- [ ] `index.html` (built page) and `images/` (with `images/opt/` WebP files)
- [ ] `brief.md`, `tool-inputs.md`, `copy.md`, `brand-kit.md`, `image-plan.md`, `image-prompts.md`, `learned-rules.md`
- [ ] `review.md` (the Stage 6 self-review table) and `shots/` (from `tools/shoot.mjs`)
- [ ] `grade.txt`: the output of `python3 test/grade.py --page my-sales-page/index.html --copy my-sales-page/copy.md`

## How it's graded
- **50 points automatic:** `test/grade.py`. Fold fit, sideways scroll, broken images, one CTA label, button routing, dashes and banned words, placeholders, image weight. Our real page scores 50/50; our first draft scored 25/50.
- **50 points judged by TJ:** copy, visual quality next to the reference screenshots, and process. See `rubric.md`.
- **Pass:** 85 or more, with **no hard fail.** The hard fails are:
  - the phone button is below the fold;
  - placeholders on the page;
  - invented facts or testimonials;
  - an item in the offer that isn't really included.
