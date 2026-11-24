# Funnel stage F5 of F5: Review, feedback and hand-off to GoHighLevel

## 1. Self-review before anyone sees it
1. `python3 PLAYBOOK/tools/build_funnel_pages.py my-funnel-pages/funnel-pages.json` → 0 to fix. Settle every CHECK line: fix it, or accept it with the client's reason (`accepted`), or list it as open.
2. `node PLAYBOOK/tools/check_funnel_pages.mjs my-funnel-pages` → "All pages pass" (takes about 1 to 2 minutes).
3. Open **every** screenshot in `shots/` (first screens and full pages). Write `my-funnel-pages/review.md`: page → issue → fix.
4. Go through this list:
   - [ ] Same brand on all pages (colors, fonts, logo) as the sales page.
   - [ ] Prices, names and guarantee identical everywhere (sales page, checkout, upsell, emails).
   - [ ] The bump is nowhere on the sales page or in the main email.
   - [ ] No dashes, no "regular price", no fake deadline, no income promise, one number per claim.
   - [ ] No text from the Rickey example. No placeholder.
   - [ ] The "Who gets what" table in `dist/ghl-texts.md` is right for this offer, and nobody gets something they didn't buy.
   - [ ] Every `proof`, quote and founder note is real, with its source.
   - [ ] Every image loads, is sharp, and shows the right product.

## 2. Show the person
Open the previews (`open my-funnel-pages/preview/upsell.html`, and the others). Tell them: what's approved, what's still open, which lines are yours. Take feedback as in Stage 7 (log each decision in `my-funnel-pages/learned-rules.md`; change the JSON or the CSS; rebuild; re-check both sizes).

If the feedback would apply to any client, add the rule to `knowledge/upsell-and-bump.md` or `funnel-offers.md`, and to `feedback-log.md`.

## 3. Publish the fragments
`dist/*.html` and `images/` go to the client's public page repo (Stage 9), with `assets_base` set to its URL, then rebuild. **Only pages and images. Never paid files, course decks or the client's documents.** `--final` treats every open CHECK as a stop (the person can OK one: put their words in `accepted`, e.g. they looked at the light-brand previews, or read the live sales page for the bump): run it when the links, values and approvals are in (the course link comes from GHL). Until then build without it and list what's open.

## 4. Hand off to the GHL Funnel Playbook (https://github.com/shuri-lab/GHL-connection-skill)
Give it the folder. `dist/ghl-texts.md` lists the product names, prices, step addresses, order-form, bump, YES/NO and email texts, root ids, workflows and who gets what. Funnel name, sender, tags, lessons, tax and tracking come from the GHL plan. Its stages use:

| File | GHL stage |
|---|---|
| `dist/ghl-texts.md` | 1 (plan), 3 (products), 4 (paths) |
| `dist/checkout-left.html` | 6 |
| `dist/<upsell>.html`, YES and NO texts | 7 |
| `dist/thank-you.html` | 8 |
| `dist/emails/*.html`, subjects, previews | 10 |

## Done when
- [ ] `--final` passes, the checker passes, `review.md` is all fixed, the person said yes.
- [ ] Fragments and images are live on the page host, or the repo is ready.
