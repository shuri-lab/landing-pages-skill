# The context the copy needs (read before Stage 1 and Stage 2)

**The one idea:** the copy tool and the framework only rearrange what you feed them. Rickey's copy was strong because the inputs were real and specific:
- the founder's own answers and voice;
- real buyer research in the buyers' own words;
- the true offer;
- verified proof.

With thin or generic inputs you get a generic page, and no amount of design fixes that.

## The 8 kinds of context (and what "enough" means)

| # | Context | Why the copy needs it | "Enough" means | Where it went on Rickey's page |
|---|---|---|---|---|
| 1 | **The true offer**: every item, what it does, price, guarantee | The offer stack, values, guarantee and every "you'll get" line come from here. Wrong items = false promises | Every item confirmed by the client **in their latest word**. Old offer docs are often out of date | Tool field "What does the buyer get?"; the offer stack ($57 / $47 / $97 = $201) |
| 2 | **The buyer (avatar)**: who, situation, what they want, what they do now, fears | Headline, pain section, "built for you if", objections. Copy speaks to one person | At least 5 real quotes or phrases from buyers (community research, reviews, calls) plus a one-sentence avatar | Fields "Who is it for?", "What are they trying to get?", "What are they doing now?"; the "watching other people win" section |
| 3 | **The method / mechanism**, in the founder's words | The "why this works" sections and the subheadline's "how". It makes the offer believable and different | The founder's own explanation of the steps (interview, Q&A, voice notes), not our summary | Field "What makes it different?"; the subheadline ("find winning products, make viral videos, make sales") |
| 4 | **Objections**, each with the answer | The FAQ-style lines and "What if you're not the problem?" | 4–8 objections from research or calls, each answered with a fact | Field "What might stop them?" |
| 5 | **Proof**: verified numbers, badges, screenshots, brand deals | The pill, the proof sections, every number on the page | Each number labeled correctly (**sales/GMV ≠ earnings**), each with a source, and a list of which screenshots really exist | Fields "Results", "Numbers"; the "$4M+ in TikTok Shop sales · top-1% creator" pill |
| 6 | **The founder's story and voice**: real beats, real phrases | The founder story section and the tone of the whole page | Story beats in their words (Best Buy shirt → background work → Nike/Subway → TikTok Shop) plus 3–5 phrases they really say | Field "What's your story?"; the story section, kept word for word |
| 7 | **Testimonials**: real ones with permission, or "none" | Proof sections | Real quotes only. If there are none, say so and choose the alternative (founder's own proof, friend/family stories) | Field left empty; "Don't Take My Word for It." |
| 8 | **Constraints**: banned words, claims to avoid, traffic source, device mix | Tone, compliance, hero length | The client's "never" list, the platform's rules (no income claims), "90% on phones" | Copy rules: no dashes, no "steal", no income promises |

## The gate (Stage 2 does not start until all of these are true)
- [ ] `brief.md` covers all 8 kinds, and every fact has its source in brackets.
- [ ] The client confirmed **what's in the offer** (item by item) and **the values**.
- [ ] There are at least 5 buyer quotes in the buyer's own words.
- [ ] Every number is labeled (sales, earnings, followers, students), and anything not verified is marked "confirm" and kept off the page.
- [ ] The founder's story beats and voice phrases come from their own words.
- [ ] Testimonials: real ones listed, or "none" with the chosen alternative.
- [ ] Constraints are listed (the never list, compliance, traffic, device).

In the test, `test/client-answers.md` counts as the client's confirmation.

**Cross-check facts:** if the tool's output, a deck and the founder's own words disagree, the founder's own words (answers, transcripts) win. Flag the difference. Facts that exist only in images (deck slides, screenshots) are sourced as "[file, slide/page N]".

If something is missing: **ask the client once, specifically** (e.g. "What are 3 things buyers say before they buy?"). If it's still missing, write the gap in the brief and tell the client what the page loses without it. Never fill a gap with invented detail.

## From brief to tool inputs (Stage 2a)
Write `my-sales-page/tool-inputs.md`: one block per field of the AI Sales Page Tool (the 16 fields are in `stages/2-copy.md`), filled **only** from the brief.
- Each block is a short paragraph or 3–8 bullet lines, specific, in plain words.
- Put the buyer's own phrases in the buyer fields and the founder's own phrases in the story field.
- Leave out anything unconfirmed: old offer items, earnings estimates, items that show only at checkout.
- The model: `examples/rickey-headstart/tool-inputs.md`, next to the brief it came from: `examples/rickey-headstart/brief.md`.

## Mistakes we actually made (so you don't)
- **The tool's copy listed items that weren't in the offer** ("templates", "milestone playbooks"), because an old offer document fed it. It cost two feedback rounds. **Confirm the offer first.**
- **An earnings estimate sat next to the sales number.** Only the verified sales figure goes on the page, labeled as sales.
- **We rewrote the founder's story** to "make it stronger" with an Instagram post. The client rejected it twice. **The story stays in the founder's words.**
- **The order bump got announced on the sales page.** It belongs only in the checkout.
