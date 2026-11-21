# Stage 1 of 9: The context

**Goal:** one file, `my-sales-page/brief.md`, that holds every fact the page may use, with where each fact came from. Everything later (the copy tool's inputs, the hero, the offer stack, the images) is filled from this brief. Nothing goes on the page that isn't in the brief.

**Read first:** `knowledge/copy-context.md`. It defines the 8 kinds of context the copy needs, what "enough" means for each, and the gate.

**Why:** the copy tool only writes good copy when it gets real detail. On Rickey's page the copy was strong because the tool got the founder's own answers, his voice, the customer research and the real offer. Generic inputs give generic pages.

## 1. Read everything first, ask second

Read the whole project folder before asking anything. Convert files you can't read:
- `.docx`: `textutil -convert txt` (macOS) or python-docx
- PDFs: the pdf skill, or `pdftotext`
- Images and screenshots: look at them

Then ask only for what's missing, one question at a time.

## 2. What to collect (the checklist)

| # | Item | Where it usually is | Rickey example (file) |
|---|---|---|---|
| 1 | **The offer: exactly what's included**, the price, payment type | Offer stack / offer ladder doc, the client's latest message | `Game Tape - Offer Stack-v11.pdf`, then corrected by David: course + 30-day plan + private channel only |
| 2 | **Each item's "value"** (for the price stack) | Client decides | Course $57, plan $47, channel $97 = $201 |
| 3 | **Avatar / customer research**: who, situation, desires, fears, words they use | Research doc, community research, reviews | `Customer research.docx`, `TikTok Shop Builders - Community Research.pdf` |
| 4 | **Market and competitors**: what else they've tried, what others promise | Market / competitor docs | `Market.docx`, `Competitors.docx` |
| 5 | **The founder's method**, in their words | Interviews, Q&A, voice notes | `Rickey's answers.docx` |
| 6 | **The founder's voice and story** | Voice doc, social posts, call transcripts | `Rickey's voice.docx`, his Instagram post about Best Buy, call transcripts |
| 7 | **Proof**: verified numbers (label sales vs earnings!), badges, screenshots, brand deals, press | Founder answers, screenshots folders | $4M+ in sales (GMV), top-1% badge, TikTok screenshots, brand logos |
| 8 | **Testimonials**: real ones only, with permission | Client | None yet: use the founder's own proof |
| 9 | **The product itself**: decks, modules, PDFs (for "what's inside" and mockups) | Deliverables folder | Course deck, 30-day challenge PDF, Starter Product List PDF |
| 10 | **Brand**: guidelines, logos, colors, fonts | Branding folder | `Game Tape Brand Guidelines.pdf`, GT logos, REC marks |
| 11 | **Media**: founder photos, videos, screenshots, product images | Media folders | `rickey-photo.jpeg`, `rickey-bestbuy.jpeg`, 5 TikTok videos, 10 TikTok screenshots, 5 product-check screenshots, 6 brand logos |
| 12 | **Reference pages** the client likes (structure, not branding) | Client | mycoach.jjsmithonline.com/look-younger, gametape-blue.vercel.app/offer-first-seven |
| 13 | **Traffic source** (cold ads vs warm audience) | Client | Mostly mobile (90%), social traffic |
| 14 | **Checkout link** (or "not ready yet") and where it will be published | Client | Not ready at build time: buttons jump to the offer stack |
| 15 | **Hard "never" rules** from the client | Client | No dashes, never "steal", no income promises |

## 3. Write the brief

Use `knowledge/templates/brief-template.md`. Every line gets a source in brackets, e.g. `[Rickey's answers.docx]`. Mark anything you inferred as `(inferred, confirm)`.

## 4. Confirm before moving on

Show the client a 10-line summary:
- offer + price
- what's included (and what is NOT)
- avatar in one sentence
- the 3 strongest proof points
- what's missing

Ask: **"Is this right?"** Fix what they flag. Log each decision to `learned-rules.md`.

## Done when

- [ ] `brief.md` written, every fact sourced
- [ ] What's included in the offer is confirmed by the client (old docs can be out of date)
- [ ] Missing items listed, with what each one costs the page
- [ ] Client said yes to the summary
- [ ] **The gate in `knowledge/copy-context.md` passes** (all 8 kinds covered, offer confirmed, 5+ buyer quotes, numbers labeled). Don't start Stage 2 until it does
