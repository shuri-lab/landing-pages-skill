# The frameworks: how we use them

Three source files sit in this folder. This page is the 1-page version of how we apply them. Read the source when you need the detail or the examples.

| File | What it is | When we use it |
|---|---|---|
| `landing-pages-framework-v2.txt` | Transcript of a landing-page agency's two videos (ThrillX, 400+ pages built): part 1 is the block-by-block anatomy, part 2 is Alex Hormozi's landing page strategy | Stage 2b (rework the hero) and Stage 5/6 (does every section do its one job?) |
| `thrillx-landing-page-prompts.md` | Ready-made prompts: headline, subheadline (2 versions), pain section (Problem-Agitate-Solve), pain headline, value props, CTA | Stage 2b: generate options, then pick with the client |
| `alex-hormozi-vsl-framework.txt` | Hormozi's VSL framework | Only when a page gets a video sales letter (not used on Rickey's Offer 1) |

## The anatomy we follow

1. **Copy first, design after.** Write the messaging, then design every section to *show* what that section says. A course page shows the course (mockup, module list); a "community" claim shows the community (phone with the channel); a "fast results" claim shows the timeline.
2. **Above the fold** (the first screen; about 60% of visitors never scroll past it). It holds:
   - **Headline:** end result + time period + emotional payoff. One promise, clear in 5 seconds. Don't explain who you are.
   - **Subheadline:** how you get that result. Open on the pain ("Tired of X?") or "without X, Y, Z", then the 3–4 biggest value props.
   - **Two forms of social proof:** stats, badges, press or brand logos, reviews. For Rickey: the "$4M+ · top-1%" pill plus the brand-logo strip.
   - **One call to action.**
   - **A friction reducer:** guarantee, "one-time payment", "instant access".
   - **One image or video** that shows the thing they get or the outcome they want.
   - **On a phone, all of it stacks and must fit the first screen.** This is the rule David enforced on every page (393×852).
3. **Right after the fold**, pick by traffic temperature:
   - **Warm / high-intent** (search, people who know the founder): social proof first. Show the proof up front, not hidden in a carousel nobody swipes.
   - **Cold / interruption** (Meta, TikTok ads) or a complex offer: the pain section first, written as Problem → Agitate → Solve.
4. **Value props** (4–8 of them across the page):
   - Each headline pairs the feature with the benefit.
   - Assume people read only the headlines, so each one must sell on its own.
5. **"How it works":** step 1 → 4, each step written as a benefit, and the section headline is a benefit ("Get X in 4 simple steps"), not "How it works".
6. **For courses and digital products:**
   - Show what's inside (visual + modules).
   - Stack the bonuses with crossed-out values so the price feels like a no-brainer.
7. **FAQ plus the fear/uncertainty/doubt reducers** (guarantee badge, refund terms).
8. **Closer:** a mini version of the top of the page: recap headline, the benefits, social proof, the offer box or button.
9. **Social proof headlines say the benefit.** Never "Real people, real results"; instead "Join thousands who…".

## Hormozi levers (value equation) we check in the hero

Value goes **up** with:
- **Dream outcome:** what the headline promises.
- **Perceived likelihood:** proof such as the eyebrow, logos and screenshots.

Value goes **down** with:
- **Time delay:** say the timeframe ("in 30 days").
- **Effort and sacrifice:** say "no following, no inventory, no camera experience".

Make the first two big and the last two small in the hero.

## How we prompt for the hero (Stage 2b)

**Step 1: give Claude the context.**
- The Project Brief.
- The tool's draft.
- The framework file.

**Step 2: ask for options.**
- 5 headlines and 3 subheadlines, using the ThrillX headline structure: dream outcome + functional benefit + timeframe + mechanism/proof.
- Ask for them in a table.
- No em dashes, no clever wordplay.

**Step 3: mark a recommended pick.**
- Mark one ⭐.
- Add a one-line traffic note.

**Step 4: the client picks.**
- They pick a pair (Rickey: "Use 1 + A").
- They may edit their pick. Their edit is final.

**Rickey's final hero:**
- **Headline:** "Get Your First TikTok Shop Sales in the Next 30 Days, Starting From Zero"
- **Eyebrow:** "$4M+ in TikTok Shop sales · top-1% creator"
- **Subheadline:** "Follow the same plan behind Rickey's $4M+ in TikTok Shop sales: how to find winning products, make viral videos, and make sales, plus a 30-day plan that walks you there, one video a day. No following, no camera experience, no guessing what to film."
