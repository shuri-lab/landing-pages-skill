# Stage 7 of 9: Feedback rounds with the client

**Goal:** turn the client's feedback into changes quickly and safely, and make sure each piece of feedback is never needed again (on this page **or the next one**).

## Each round, in order
1. **Back up** before touching anything: `copy-vN.md`, `body-src-vN.html`, `index-vN.html` (N = next number). This makes "put it back how it was" a one-step restore.
2. **Split the feedback into numbered items** (long voice messages hold 10–20 items). Repeat them back as a short list only if something is unclear.
3. **Apply each item** to `copy.md` and `body-src.html` together (they must stay in sync, or `check_page.py` fails).
   - Phone feedback: fix phone **and** re-check desktop. Desktop feedback: fix desktop **and** re-check phone.
   - If the client's own text breaks a standing rule (e.g. contains a dash), apply the rule, say so, and offer the alternative.
   - Don't rewrite the client's copy beyond what they asked. If they give source material ("make this stronger with his Instagram post"), propose a draft and wait for approval.
4. **Log it:** one line per decision in `my-sales-page/learned-rules.md`. When a rule changes, write "OVERRIDES …" so it isn't undone later. Re-read this file before every build.
5. **Rebuild + self-review:** `tools/rebuild.sh`, then Stage 6's automatic checks and a look at the changed sections at both sizes.
6. **Reopen the page** for the client (`open my-sales-page/index.html`, "refresh if you still see the old version").
7. **Report per item:** what changed, with measured numbers where it matters ("phone button now ends at 764 of 852"), and **which lines are your own wording**.

## When the feedback is general, make it general
If the feedback would apply to any page ("the sliders run out", "text too small on phone", "make the bump copy simpler"), it belongs in the playbook too: suggest adding it to `knowledge/house-style.md` or `knowledge/copy-rules.md` so the next page starts with it. (This is how the house style was built: see `knowledge/feedback-log.md`.)

## Typical rounds to expect (from the Rickey page)
| Round | What the client asked | Already in house style? |
|---|---|---|
| 1 | Mobile first; hero above the fold; one CTA label; highlights in the subheadline; screenshots under claims; alert bar; sticky CTA; logo slider; JJ-style offer stack | Yes, all of it |
| 2 | Hero too cramped (bigger text); story beats look alike; guarantee as its own block; desktop rework | Yes |
| 3 | Wrong product image; remove an item not in the offer; desktop fold + bigger image; logo slider under the photo | Yes (checks) |
| 4 | Transparent hero image; sliders run out; bigger desktop text; crossed-out values | Yes |
| 5 | Price comparison like the reference page; bigger phone logos; list missing images | Yes |
| 6–8 | Real images arrive; offer contents corrected; go live without placeholders | Yes (process) |
| 9–11 | Founder photos; a story rewrite rejected ("have it as it was") | Yes (rule: never rewrite the story) |
| Later | Images load slowly (speed); don't announce the bump; bump copy simpler | Yes (Stage 8, copy rules) |

With the house style applied from the first build, expect 2–4 rounds about taste instead of 12.
