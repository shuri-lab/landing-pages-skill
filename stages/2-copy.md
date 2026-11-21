# Stage 2 of 9: The copy

**Goal:** an approved `my-sales-page/copy.md` that follows the kit's 14-section structure, has a hero built on the landing-page framework, and passes every rule in `knowledge/copy-rules.md`.

**Why this order:** copy first, design after. The design is built around what the copy says, never the other way round (`knowledge/frameworks/HOW-WE-USE-THEM.md`).

**Input:** `my-sales-page/brief.md` from Stage 1. It must pass the gate in `knowledge/copy-context.md`. If it doesn't, go back to Stage 1.

---

## 2a. First draft with the AI Sales Page Tool

The tool: **https://tasteofreedom.com/the-buy-now-sales-page-tool-page** (Isabelle's Buy-Now Sales Page). No login needed for the tool page. Answers save in that browser only. It opens with Isabelle's example product loaded: press **Clear all** first.

It has 4 input steps (16 fields: Isabelle's 15 questions plus "Numbers, facts or claims"), then Generate. Fill every field from the Project Brief. Use the client's real facts only. Where the brief has nothing, leave the field empty and tell the human; never invent.

| Step | Field (exact label) | Fill it from the brief | Notes |
|---|---|---|---|
| 1 Your Product | Product name | Offer name | Customer-facing name, exactly as it will appear on the page |
| | What are you selling? | One-paragraph offer summary: what it is, who it's for, the end result | Plain words. Say the format (course, plan, channel, kit) |
| | Price | Price + payment type (+ coupon if any) | E.g. "$27 one-time payment" |
| | What does the buyer get? | Every component + what it does, one per line | ONLY what is really included (Rickey: course, 30-day plan, private channel. Old offer docs listed more; the client's latest word wins) |
| | Your product content (optional) | Course outlines, deck text, workbook text, transcripts | Import files (PDF, DOCX, TXT, MD, SRT/VTT). The more real detail, the more specific the page |
| 2 Your Buyer | Who is it for? | Avatar: who they are, their situation, what they've tried | Use the customer research + the founder's description of a typical buyer |
| | What are they trying to get or do? | Desires, dream outcome, in the buyer's words | Pull quotes from community research / reviews / calls |
| | What are they doing now instead? | Current behavior + failed alternatives | E.g. "watching TikTok Shop videos, never posting" |
| | Dream Buyer Deep Dive (optional) | The full customer research doc | Isabelle's "Buyer Mind Reader" output goes here if you have one; otherwise paste the customer research |
| 3 Why Yours? | What makes your product or method different? | The mechanism / unique method | From the founder's answers ("how I'd take someone from zero") |
| | What becomes easier, faster, or better? | Concrete before/after benefits | Bullets |
| | What might stop them from buying? | Objections → what they need to understand | Format: "objection" → answer. From research + founder answers |
| 4 Your Proof | What's your story? | Founder story in their own voice | From the founder's voice doc, interviews, posts |
| | What results have you gotten? | Real results + which screenshots exist | List the proof assets you actually have |
| | Testimonials | Real testimonials only | Leave EMPTY if none. The tool then uses placeholders, which you handle in 2c |
| | Numbers, facts or claims you can use | Every verified number | Sales vs earnings must be labeled correctly (Rickey: $4M+ is sales/GMV, not earnings) |

**Always write `my-sales-page/tool-inputs.md` first.** That's the text for all 16 fields, filled only from the brief (rules in `knowledge/copy-context.md`). It is the record of what the copy was built from, and it's graded in the test.

**How to run it:**
- **Option A, Claude drives (preferred).** Open the tool in the browser pane and press Clear all. Fill each field (form inputs on the page), then go through the steps with NEXT. On step 5 press **Generate my sales page**. Then read the result with page text or the **Copy page text** button.
- **Option C, the tool is down or unreachable (fallback).** Claude writes the 2 runs itself, using the same logic the tool uses (the kit's `questions.md`, `structure.md` and `voice.md`) plus two real input→output examples. Follow `knowledge/copy-fallback.md` step by step, and label the runs "written by Claude (fallback)". Then continue with 2b as normal.
- **Option B, a person runs it.** Claude writes `my-sales-page/tool-inputs.md` with the text for every field, and the person pastes them in and pastes the result back.
- **Generate twice.** Each run differs. Save both, word for word, to `my-sales-page/copy-tool-output-run1.md` and `-run2.md`.
- **Pick one.** Choose the run whose angle best fits the buyer's emotional state, and say why in one line. Rickey's pick was Run 1: empathetic and pain-led ("stop watching, you're not the problem").
- **The headline button.** "New headline options ↻" in the tool gives more headlines. Use it if both runs' headlines are weak.

Examples of inputs → output:
- `examples/rickey-headstart/tool-inputs.md` → `copy-tool-output.md` (Rickey)
- `knowledge/copy-examples/sample-3-email-inputs.md` → `sample-3-email-output.md` (the tool's own sample)

## 2b. Rework the hero with the framework

The tool's body copy was very solid. The hero needed real work every time, so this step is not optional.

**Read first:**
- `knowledge/frameworks/HOW-WE-USE-THEM.md` (1 page)
- `knowledge/frameworks/thrillx-landing-page-prompts.md`
- the full framework when in doubt: `landing-pages-framework-v2.txt`

**The rules:**
- **Headline = end result + time period + emotional payoff.** One big promise, readable in 5 seconds. Quantify where possible. Promise *sales/results*, never income amounts.
- **Subheadline = how it works, made to feel effortless.** "Without X, Y, Z", plus the 3–4 biggest value props. It can open on the pain.
- **Eyebrow / pill above the headline = proof.** E.g. "$4M+ in TikTok Shop sales · top-1% creator". Don't open with the founder's name.
- **Hormozi value equation levers:**
  - dream outcome: the headline
  - proof: the eyebrow
  - short time delay: "30 days"
  - low effort: "no following, no inventory…"

**What to write:**
- **5 headline options and 3 subheadline options.** Mark one recommended pick ⭐ and number them (1–5, A–C).
- **A traffic note.** Cold or Meta traffic gets an emotional headline. Warm or search traffic gets the direct outcome.
- **The client's pick.** Show them and let them choose ("Use 1 + A"). The client may also hand you their own subheadline. Use it word for word.

**Save** the options and the client's pick in `my-sales-page/hero-options.md`.

**Then:**
- Pre-format the subheadline highlights for the build. That means a marker on the proof phrase and bold color on the 3 value props. Don't highlight filler like "one video a day".
- Trim the subheadline so the whole hero fits a phone screen. Rickey: we dropped "a 7-day course" from it.

## 2c. Structure check, gaps, client decisions

Follow the kit: `kit/sales-page-generator-kit/kit/1-copy/structure.md` (14 sections).

1. Match the chosen run to the 14 sections. Tell the client, in a short list: covered / missing / off-structure.
2. **Never rewrite the client's words without asking.** Propose the house-rule fixes as one list for approval (2d), then apply what they approve.
3. Resolve every placeholder the tool left. Ask the client:
   - **Item values for the offer stack.** They are made up by the client, reasonable for the item (Rickey: course $57, plan $47, channel $97 = $201). Always call it "value", never "regular price".
   - **No testimonials yet?** Offer the choices:
     - a "Don't Take My Word for It." section with the founder's own proof (screenshots);
     - real friends' or family stories as text;
     - skip the testimonial sections until results come in.
     - Never invent one.
   - **Proof screenshots** the tool asked for: list which exist; the rest are dropped, not placeholdered.
4. Save the approved copy, as plain lines, to `my-sales-page/copy.md`. Use `## SECTION N` markers and `>` notes, as the kit requires, because the checker matches it line by line.

## 2d. House copy rules pass (propose, then apply)

Run `knowledge/copy-rules.md` over the whole copy. These came from David's feedback, so the client shouldn't have to ask for them again. The most common:
- No em or en dashes anywhere.
- One CTA label on every button: "GET INSTANT ACCESS · $PRICE →".
- No "steal".
- No fake deadlines ("today only" with no deadline).
- 5th-grade clarity.
- One number per claim.

Save the list as `my-sales-page/copy-rules-pass.md` (line → proposed change → rule). Show it and get a yes before applying.

## Done when

- [ ] `tool-inputs.md` written: all 16 fields, from the brief only
- [ ] Both tool runs saved word for word, the pick explained
- [ ] Hero: headline and subheadline chosen by the client, highlights marked
- [ ] Every placeholder resolved or the section dropped by decision
- [ ] `copy.md` saved in kit format, house rules applied with approval
- [ ] One line per client decision added to `my-sales-page/learned-rules.md`
