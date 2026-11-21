# Playbook feedback from the replication dry run (Nov 20 2026)

Run by Claude as a new teammate, following START-HERE stages 0 → 6, then 8 (7 and 9 skipped). PROJECT = `rickey-tiktokshop-project/project-files/` (identical to `examples/rickey-headstart/project-files/`), WORK = `dryrun/my-sales-page/`. Client = `test/client-answers.md`. No browser pane (all visual checks via `tools/shoot.mjs` + PNG/JPG files).

**Result:** `grade.py` 50/50, no hard fails, on the first build (one fold tweak afterwards: button 791 → 762). `check_page.py` OK on the first build. Most of the quality came from house-style.md + CATALOGUE + body-src.html, which are excellent. Most of the friction came from the test setup (forbidden-but-referenced files, mid-run rule changes) and from tool gaps when there is no browser pane.

## Time per stage (shell `date` wall clock; agent time only, no human gates)
| Stage | Time | Notes |
|---|---|---|
| 0 Setup | ~1 min | |
| 1 Context | ~5 min + ~5 min retrofit | ~13k words of docx, 10 PDFs (one image-only deck), ~45 images. Retrofit when `copy-context.md` arrived mid-run |
| 2 Copy | ~6 min | Hero options, structure check, rules pass, copy.md, tool-inputs.md |
| 3 Brand | ~2 min | Swatch card rendered with shoot.mjs |
| 4 Media | ~4 min | Inspecting AI images for third-party logos took the most care |
| 5 Build | ~4 min | rebuild.sh worked first time |
| 6 Self-review | ~9 min | Had to write 3 helper scripts because there's no pane (see #6) |
| 8 Speed | ~2 min | Already done because expand_body.py forces WebP (see #7) |
Total ≈ 35-40 min of agent wall clock. With real ★ gates and ChatGPT it would be the 3-4 h the test predicts.

---

## Top 10 problems (fix these first)

1. **The test leaks the answer key and also forbids the model you're graded against.** `examples/rickey-headstart/body-src.html` is "allowed as component source" (TEST.md L16, stages/5-build.md L13) but it contains the *entire final copy*, including client-round decisions not in client-answers.md (s2 outcome 3 rewritten as "Join the Rickey Army…", the footer disclaimers, which product-check screenshots, etc.). Anyone who opens it has seen the final page text. At the same time the files you're *compared with* are forbidden: rubric.md L31 "compare with `examples/rickey-headstart/tool-inputs.md`", copy-context.md L40 "The model: …tool-inputs.md… brief.md", stages/2-copy.md L45-47, knowledge/copy-fallback.md L16. **Fix:** ship a copy-free `components.html` (lorem or placeholder text) for the test, and either allow the model files or remove the references to them.
2. **No allowed visual target.** START-HERE.md L5 and README L16 set the quality bar as `examples/rickey-headstart/screenshots/`; rubric.md L19 and tj-review-sheet.md compare against `test/reference/`. Both are forbidden. A test-taker builds blind to the bar. **Fix:** describe the reference in words in house-style (already mostly done) and say explicitly in START-HERE that test-takers must not open those folders.
3. **Rules changed while the test was running.** TEST.md, rubric.md, inputs.md, stages/1-context.md, stages/2-copy.md, and new files `knowledge/copy-context.md` and `knowledge/copy-fallback.md` all changed between 21:39 and 21:44, after I had finished Stage 1. Two test-takers starting an hour apart are graded on different rules. **Fix:** version the test (TEST.md "v3, frozen Nov 20") and never edit it mid-run.
4. **The "raw" tool output isn't raw.** `Offer 1 - Sales Page Copy (Buy-Now tool v1).md` L3 says "Edited Nov 20: hero section reworked against the landing-page framework + Hormozi (options below)" and already contains the 5 headlines, 3 subheads, ⭐ pick and traffic note that Stage 2b asks you to produce. And there's only run 1, while stages/2-copy.md L41 says "Generate twice… save both". So 2a/2b are partly pre-done and can't be graded fairly. **Fix:** ship the true raw output (two runs) or say in TEST.md "2b options are already in the input; write your own anyway".
5. **`shoot.mjs` full-page shots stop at 16,000 CSS px** (tools/shoot.mjs L150 `Math.min(h, 16000)`). The phone page is ~20,600 px, so sections 11-14 and the footer are never in `shots/`, which is what TJ grades from (rubric L19). Fixed elements (the sticky bar) also render mid-page in full captures, and the kit's floating "Edit layout" button covers the hero fine print in every fold shot of the draft `index.html` (the stage 6 prep snippet hides it only in the pane). **Fix:** capture in 16k slices, hide `.stickybar` and the editor button before capture.
6. **Stage 6 assumes a browser pane.** All component checks (slider halves vs box, CTA click → `#buy`, sticky show/hide, video readyState, unloaded images, overflow finder) are pane JS snippets (stages/6-self-review.md L53-73, tools/snippets.md §5). With no pane (CLI, or this test) there's no tool for them. I had to write `probe.mjs`, `shoot-from.mjs` and `weigh.mjs` (copies in `my-sales-page/shots/tools/`). **Fix:** ship `tools/probe.mjs` (checks) and `tools/weigh.mjs` (full-scroll image/video weight) and call them from Stage 6/8.
7. **Stage 5 and the build tool contradict each other on images.** stages/5-build.md L32 "while building, use the originals. Stage 8 switches the page to WebP", but `tools/expand_body.py` L32 hard-codes `src="images/opt/%s"` for every logo and slider image. Following Stage 5 literally gives broken images. **Fix:** move "run optimize_images.py" into Stage 4d/5 step 0, or make expand_body.py take the folder from page-config.
8. **`grade.py` and the kit disagree on copy notes.** The kit (kit START-HERE L42) and stages/2-copy.md L87 say put notes in copy.md as `>` lines; `check_page.py` skips them, but `grade.py` L159 strips `>` and counts them as page copy, so it reports "154 of 158 lines found; missing e.g. 'Alert bar, pill…'". **Fix:** grade.py should skip lines starting with `>` (and `(`/`[` like check_page), or the playbook should say "use `<!-- -->` only".
9. **Hero fold target depends on an unstated logo choice.** house-style.md #3 says "logo (150px)" and the targets are btn 764 / fine 795. With the stacked brand logo (`GT-B.png`, the natural pick for a centered hero) the logo is 50px tall and the button lands at 791 / fine 822: still "in fold" for grade.py but over the ~800 target and the fine print sits under the editor button. The reference used the one-line logo (~22px tall). **Fix:** house-style #3: "one-line/horizontal logo, ≤ 24px tall at 150px wide".
10. **The context step needs a filled template, not just a gate.** `knowledge/copy-context.md` is good (see the section below), but `knowledge/templates/brief-template.md` has no slots for the things the gate checks (a buyer-quotes list, a labeled-numbers table, the gate checklist itself), and stages/1-context.md L12-13 offers `pdftotext`/"the pdf skill", neither of which exists on a stock Mac/Claude Code; the course deck PDF is image-only, so you need `tools/mac/pdf2png.js`, which Stage 1 never mentions (only stages/3 L12 and snippets.md). **Fix:** update the template; in Stage 1 list `osascript -l JavaScript tools/mac/pdf2png.js` and "pypdf in a venv" as the PDF route, and say "image-only PDFs: render and look".

---

## Everything else (file + line)

### Unclear / contradictory
- **TEST.md (first version) L15 vs L16:** L15 said "Do not open … `examples/rickey-headstart/body-src.html`", L16 said it's allowed as component source. The update removed it from L15 but the contradiction in spirit remains (see top #1).
- **README.md L64 and house-style.md title:** "27 defaults"; the list has 29 items.
- **stages/0-setup.md L21** names the body `body.html`; START-HERE.md L29, stages/5-build.md L19 and house-style #27 use `body-src.html` (rebuild.sh turns body-src into body). The Stage 0 tree also omits `body-src.html`, `page-config.json`, `export/`, `tool-inputs.md` (now required), `copy-original.md` (copy-rules.md L27), the hero-options and rules-pass records.
- **stages/0-setup.md L11:** WORK = `PROJECT/my-sales-page/` assumes the project folder is writable; the test makes it read-only. Fine, but say "or anywhere the person names".
- **stages/1-context.md L27:** lists "his Instagram post about Best Buy" as a source; it isn't in the inputs.
- **stages/2-copy.md L36, copy-context.md L36, TEST.md L21, rubric.md L31:** "15 fields"; the table in stages/2-copy.md L17-34 has **16** rows. I filled all 16.
- **Rubric "hero options written with a ⭐ pick; rules pass logged" (rubric L32) has no file name** in TEST.md's hand-in list or Stage 2. I used `hero-options.md` and `copy-rules-pass.md`; another test-taker might bury them in copy.md comments and lose the points.
- **kit/…/1-copy/structure.md L16** "start with 'Steal my…'" conflicts with copy-rules #4. copy-rules.md L30 notes it, but the kit file itself isn't annotated, and the stage tells you to "follow the kit".
- **kit/sales-page-generator-kit/START-HERE.md L93** "Every button goes to my checkout link" conflicts with house-style #9 (all to `#buy`, one checkout).
- **kit/…/4-build/sections.md L7** fine print "One-Time Payment • Instant Access" vs copy-rules #15 "One-time $27 · instant access".
- **kit/…/3-images/image-slots.md L10** "One photo only: use it in 12, leave section 3 without a photo" vs house-style #16 and the client (both photos in the story). Also "the story section" in client-answers.md is ambiguous: the page has two story sections (3 and 12). I chose 3 (its beats match house-style #16's beat styles).
- **stages/3-brand.md L119-133 (E8 "AI image prompts")** is Stage 4 material in the Stage 3 file.
- **tools/snippets.md L40-41** video transform `w_360,q_auto,ac_none,du_12` is outdated vs stages/4 L80, stages/8 and CATALOGUE C4 (`w_320,q_auto:eco,ac_none,du_10,f_auto`).
- **knowledge/pitfalls.md:** the "More pitfalls" table restarts numbering at 1, so "pitfall #11" is ambiguous (two different #11s).
- **stages/4-media-sourcing.md E1 L104** says use "Product check screenshots ×2" for outcome 2; one natural pick shows "Earn $2.27–4.16 per sale" (a money figure). copy-rules #8 doesn't say whether third-party commission figures count. I avoided it.
- **stages/6-self-review.md L64-65** gives Rickey-specific pixel targets as if universal (fine as examples, label them).
- **grade.py image weight (L141-155)** sums unique `src` files only. On a DPR-2 phone the `srcset` picks the 1280 variants: grade said 1.23 MB, real full scroll measured 1.40 MB. Close to the 1.5 MB target, so the check can pass while the page fails.

### Missing steps
- **No step to cross-check the tool's facts against the founder's own words.** The tool copy (and the course deck p4) says "Another friend grew **his** page just by filming **his** hikes"; Rickey himself says "my friend, **she** was hiking… she built her following to 1000 fairly quick" (more-context, Nov 17 meeting transcript ~L848). I fixed it and flagged it. Copy-rules #9 only covers offer items.
- **No step to compare the course's lesson list with the real deck.** The tool's lesson order (hooks before filming) differs from the deck (filming lesson 4, hooks lesson 5), and "5–8 min each" has no source. I corrected both and logged them.
- **No guidance on handing in `index.html` with the kit's editor in it.** rebuild.sh writes the draft (with "Edit layout") to `index.html` and the clean page to `export/index-final.html` (with relative image paths that only work one folder up). The test grades `index.html`. I handed in both and shot both.
- **`optimize_images.py` still names by requested width** (L72: `proof-product-check-1-480.webp` is 388px wide) although pitfalls "More" #11 says "Name by the actual output width".
- **Stage 4 has no rule for AI images that can't be regenerated** (test rule): both channel mockups have Nike/Jordan marks. I used the one with the faint mark and flagged it; the playbook should say what to do (crop, cover, or drop).
- **Test isolation:** the session scratchpad already contained the original build's working folders (`mine/`, `prev/`, `rbtest/`, `scripts/`, `deck/`, `logos/`, `stack/`, `newimg/`, `vid/`…). A test-taker who `ls`es the scratchpad finds the answers. I didn't open them; I moved my own work into `dryrun/tmp/`.

### client-answers.md was silent on (my calls, all logged in learned-rules.md)
Lesson length; the friend's gender; which story section gets the photos; footer disclaimer text (drafted, flagged); hero logo variant; whether to show third-party commission figures; DJI logo file with a "cleanpng" watermark; which product-check screenshots; values wording "value" vs crossed only (I used "$57 value").

### Script errors
None of the playbook's tools crashed. `rebuild.sh`, `expand_body.py`, `build_page.py`, `check_page.py`, `export_final.py`, `optimize_images.py` (venv Pillow), `shoot.mjs`, `grade.py` and `tools/mac/pdf2png.js` all worked first time. The problems are behavioral (top #5, #7, #8 and the optimizer naming above). My own errors (a mistyped path, a stray `import PIL` under system Python, a blocked `rm` of `shots/*`) were mine, not the playbook's.

---

## Did `knowledge/copy-context.md` make the context step clear?
**Mostly yes.** The 8 kinds of context with an "enough means" column and a 7-box gate turned "read everything" into a checklist I could prove. It made me add a buyer-quotes list, a labeled-numbers table (sales vs earnings vs pay vs unclear) and objection → fact pairs that I'd otherwise have left implicit, and the "Mistakes we actually made" list matches exactly the traps in this input set (templates, milestone playbooks, earnings next to sales, story rewrite, bump on the page).

**Still missing:**
1. The model files it points to (L40) are forbidden in the test (top #1).
2. `brief-template.md` doesn't have the sections the gate checks (top #10).
3. "The client confirmed the values" can't happen in a test or with an absent client: say "client-answers.md counts" (test) or "write it as an open question and don't put values on the page" (real life).
4. No rule to **cross-check tool/deck facts against transcripts** (the friend's gender, the lesson order), and no rule for **facts that live only in images** (deck slides, screenshots): how to source them (`[Course deck p4, rendered]`).
5. It doesn't say whether `more-context/` (meetings, plans) is in scope for the brief. It was useful (the friend fix came from it) but optional per inputs.md.
6. It arrived mid-run, after Stage 1 (top #3). START-HERE L13 now links it ("Before Stage 1: read copy-context.md"), but that line was also added mid-run; anyone who started earlier never saw it.

---

## Honest score estimate (current test/rubric.md)
- **Automatic (grade.py): 50/50, hard fails: none** (`my-sales-page/grade.txt`).
- **Judged: about 46/50.**
  - Copy 14-15/15: the hero is the client's pick with highlights as specified; earnings are removed, sales are labeled; the stack shows only the 3 items, $57/$47/$97, $201, "You save $174", no bump. Small risk: the friend's pronoun and lesson-order fixes are my calls (flagged).
  - Visual 18-19/20: every house-style part is there and the desktop hero is two columns with logos on the first screen. Weak spots: section 12 is text-only on desktop, and the kit's "Edit layout" button covers the hero fine print in the draft fold shots (the clean export is in `shots/final-export/`).
  - Process 14/15: brief passes the copy-context gate; tool-inputs.md fills all 16 rows (not comparable to the forbidden model); hero options, rules pass, image plan/prompts, review + shots and learned-rules are all there. Shots needed extra bottom captures because shoot.mjs stops at 16,000 px.
- **Estimated total: about 96/100, a pass.**
