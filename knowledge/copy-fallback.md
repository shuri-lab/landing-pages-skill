# Fallback: Claude writes the first draft itself (when the tool is down or unavailable)

Use this when the AI Sales Page Tool (https://tasteofreedom.com/the-buy-now-sales-page-tool-page) won't load, errors, or you can't reach it. The result must be as good as the tool's, because the tool's logic is in this repo:

| What the tool does | Where its logic lives here |
|---|---|
| Asks 15 questions (Product, Buyer, Why Yours, Proof) | `kit/sales-page-generator-kit/kit/1-copy/questions.md`: the same 15, in the same order, with the rules for asking |
| Turns the answers into a 14-section page | `kit/sales-page-generator-kit/kit/1-copy/structure.md`: what each section must do, with headline formulas |
| Writes in Isabelle's voice and removes "AI tells" | `kit/sales-page-generator-kit/kit/1-copy/voice.md`: how it sounds, the never list, the 2 machine tells, the final gate |
| Learns from examples | Two real input → output pairs (below) |

## The two example pairs (study both before writing)

| Pair | Inputs (the 15 fields) | Output (what the tool wrote) |
|---|---|---|
| **Rickey · TikTok Shop Headstart** (a course + plan + private channel, $27) | `examples/rickey-headstart/tool-inputs.md` (with `brief.md` as the source) | `examples/rickey-headstart/copy-tool-output.md` (Run 1, the chosen one; the hero was reworked after, see 2b) |
| **The tool's built-in sample: "The 3-Email Profit System™"** (an email system, $97) | `knowledge/copy-examples/sample-3-email-inputs.md` | `knowledge/copy-examples/sample-3-email-output.md` |

**What to learn from them:**
- **Field → section:**
  - "What are they doing now instead?" becomes section 5 (break their current approach).
  - "What might stop them?" becomes section 8 (the belief shift) and the objection lines.
  - "What's your story?" becomes sections 3 and 12, split as `structure.md` says.
  - "What does the buyer get?" becomes section 6 (one block per component: what it is, what it does, the result) and section 7.
- **The buyer's own words** from the inputs show up as quoted lines ("Ohhh. I can actually do that. Tonight.").
- **Every section closes with a CTA,** in the "GIVE ME THE…" / "SHOW ME…" style. Our house rule replaces those with one label, `GET INSTANT ACCESS · $X →`.
- **The tool leaves placeholders** (`[Insert: …]`) where proof is missing instead of inventing it. Do the same.
- **Watch what the tool got wrong for Rickey,** and don't repeat it:
  - it listed items that weren't in the offer (because the inputs said so);
  - it used the word "steal";
  - it used dashes;
  - it wrote 13 different button labels.

## The procedure (Stage 2a, fallback version)

1. **Inputs.** Write `my-sales-page/tool-inputs.md` from the brief (as in Stage 2a). It must pass the gate in `knowledge/copy-context.md`.
2. **Read in full:** `structure.md`, `voice.md`, both example pairs, `knowledge/copy-rules.md`.
3. **Map the inputs to the 14 sections.** Write a short table: section → which input fields and brief facts feed it → what's missing. Missing proof means a placeholder or skip the section (sections 9, 10 and 13 can be skipped when there are no testimonials; say what that costs).
4. **Write 2 versions, each with a different angle:**
   - **Run 1, empathetic, pain-led.** "You're not the problem; the approach is." Leads with what they're stuck in.
   - **Run 2, aspirational, outcome-led.** Leads with the result and the founder's proof.

   Each version has all 14 sections (or the agreed skips), real headlines (never the section labels), and a CTA under each section. Use only facts from the brief.
5. **Run the gate** in `voice.md`:
   - the never list;
   - delete reframe-contrast lines;
   - rewrite telepathy lines;
   - compare claim by claim with the brief (no hardened hedges, no new numbers);
   - then `knowledge/copy-rules.md`.
6. **Save** them as `my-sales-page/copy-tool-output-run1.md` and `-run2.md`. Add a header line to each: **"Written by Claude (fallback: tool unavailable), not by the AI Sales Page Tool."** The client should know.
7. **Pick one, with a one-line reason,** and continue with **Stage 2b** (rework the hero with the framework), **2c** (structure check) and **2d** (rules pass) exactly as with the tool's output.

## Quality bar
Put your chosen run next to `examples/rickey-headstart/copy-tool-output.md`. It should be just as specific: the buyer's real words, the founder's real story beats, the real components with what each does, and no generic lines. A paragraph that could go on any product's page is a fail: rewrite it with a fact from the brief.
