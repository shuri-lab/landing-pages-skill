# Funnel stage F1 of F5: Plan the bump, the upsell and the pages

**Goal:** `my-funnel-pages/funnel-pages.json` holds every fact and every line of copy for the checkout, bump, upsell, thank-you page and emails, approved by the person. Pages come next and are built from this one file.

**Start here directly** if the sales page already exists or someone only needs an upsell, checkout or thank-you page. You need the facts (a brief, or the approved sales page) and the brand. If they don't exist, do Stages 1 and 3 first; skip the rest. The Stage 1 copy-context gate (buyer quotes and so on) applies only if you have to write a brief now.

**Where things go:** everything for Part 2 lives in the client's folder, in `my-funnel-pages/`: `funnel-pages.json`, `images/`, `copy.md`, `questions.md`, `learned-rules.md`, `review.md`, and what the tools write (`dist/`, `preview/`, `shots/`). Never edit the playbook's own files for one client. Needs Python 3 and, for the visual check, Node 22+ and Google Chrome.

**Read first:** `knowledge/funnel-offers.md`, `knowledge/house-style.md`, `knowledge/copy-rules.md`, the copy parts of `knowledge/upsell-and-bump.md` (D4 and E6; the rest is the build diary), and `examples/rickey-headstart/funnel-pages/funnel-pages.json`.

## Steps
1. **Read every deliverable.** Open the real files (PDFs with `pypdf`, the course outline or deck, video titles). List what exists, what's promised but missing, and count what you can ("37 products": counted, with the file and page). Nothing unread goes in a stack. **Stop rule:** if a deliverable is only a name or one line ("The Bake Calculator (spreadsheet)"), open the file or ask what it does. Never guess its benefit.
2. **Choose the bump and the upsell** with the tests in `funnel-offers.md`.
   - If the client already chose, run the tests anyway and say plainly if one fails.
   - If they haven't, propose the real candidates (one or two each, never an invented straw man) with one line of why, and your pick.
   - Write down the finished sentence: "[Main] gets you [first result]. This is how you [next result]."
3. ★ **Ask the person, in one message** (write the questions in `questions.md` first; ask only what the files don't answer):
   - **Offers:** the bump and the upsell (your pick and why), prices, item values. Is each one finished today? Is the upsell sold, or will it be sold, anywhere else at this price? (If yes, "only here" and "one-time offer" aren't true.)
   - **Guarantee:** does it cover the bump? The upsell? In what exact words? If the upsell is for "after your first result", does a refund window that starts at purchase still make sense?
   - **Claims:** every number and every "faster / better" needs their word or a source.
   - **Access:** how long until a buyer really gets in ("in the next 5 minutes")? How does each product reach them, and where does each file live?
   - **The bump:** is it sold, or will it be, anywhere else at this price? Is the file finished (not a placeholder)?
   - **Proof for the upsell:** a real quote (about which product? a main-course quote must not be shown as an upsell result), result, screenshot, or two or three sentences in the founder's own words. A founder photo. None of it may be written by you.
   - **Doubts:** what do buyers ask before buying this?
   - **Thank-you:** the first action and how long it takes; a quote the founder said or approved (no quote → leave it out); community link, picture and QR.
   - **Emails:** who they come from, the support email, what to put in the P.S.
   - **Legal:** privacy, terms and refund pages. A real deadline, if any. Words they never use.
   Never invent a price, value, claim, quote or deadline.
4. **Copy the template:** `cp PLAYBOOK/knowledge/templates/funnel-pages.json my-funnel-pages/funnel-pages.json`. Fill in every field.
   - **Voice:** the client's, first person, from the approved sales page copy. Reuse approved lines (headline, guarantee) word for word.
   - **Bump:** one pain + one number + one promise, one sentence (two short ones at most), about 130 characters.
   - **Upsell:** write **three headline options** and **two sets of bullets**, read them aloud, keep the plainest. Patterns: "You Just Unlocked Your [Main]. Now [next result]…", where the next result is about speed (only with a source), looks ("Make the Next One Look Like It Came From a Bakery"), ease, variety or keeping it going. Any of these is a claim: the client says yes to it. Don't force "10x faster". If the first stack item is the course itself, call it what it is ("The full course"; say "video" only if it is video), not the product's name again. Each bullet = result first, then how. Every stack item = name + "so you…" + value.
   - **NO text:** describe what they keep doing, never mock them: "No thanks, I'll keep [doing it the hard way]."
   - **Guarantee:** the client's sentence, word for word. Split it into `title` + `text`, or leave `title` empty.
   - **Proof, founder note, questions (`proof`, `founder_note`, `faq`):** optional blocks, and usually what an $80+ upsell needs most. Use them whenever the client gives real material.
   - **Emails:** one per product. The main email goes to **every** buyer, so it never names the bump or the upsell.
   - **`sources.numbers`:** every number in the selling copy, with the file and how it was counted, or the client's words. The build refuses a number without one.
   - **`values_approved`:** `true` only after the client says yes to the values.
5. **Check the file:** `python3 PLAYBOOK/tools/build_funnel_pages.py my-funnel-pages/funnel-pages.json --check`. Fix every **FIX** line. Each **CHECK** line is a question: settle it, or (only with the client's answer) add its id to `accepted` with the reason. It can't judge whether a source is true or a claim is fair: that's yours.
6. ★ **Show the copy as text** before building: write it in `my-funnel-pages/copy.md`: bump (4 lines), upsell (headline options with your pick, sub, bridge, bullets, proof, stack table with total and savings, questions, YES, NO), thank-you, emails. Mark your own wording with (mine). Get a clear yes.

## For someone who isn't a developer
You never edit the JSON by hand: say what to change in plain words and Claude edits it. "0 to fix" and "All pages pass" mean the automatic rules passed, not that the page is finished: read it and look at it.

## Optional fields
| Field | What it does |
|---|---|
| `upsells[].proof` `[{text, by, image, image_alt, source}]`, `proof_headline` | Real quotes, results or screenshots, after the bridge |
| `upsells[].founder_note` `{text, by, photo, photo_position, source}` | A few words in the founder's own voice |
| `upsells[].faq` `[{q, a}]`, `faq_headline` | One or two real doubts, after the guarantee |
| `upsells[].jump_button` | Text of a link down to the offer |
| `upsells[].hide_name_label` | `true` when the image already shows the product name |
| `upsells[].pill`, `progress`, `offer_tag`, `price_note`, `lead_1`, `lead_2`, `title` | Replace the standard texts |
| `upsells[].video` | A video instead of the image (never run live by us) |
| `items[].thumb`, `items[].modules` | Small picture; numbered list under the item |
| `bump.banner`, `main.pill`, `main.email_help`, `main.order_button` | Replace the standard texts |
| `labels` `{what_you_get, total, offer_head, save, now, order_subtext, guarantee_scope}` | Wording of fixed labels |
| `brand.alert_color` | A stronger color for the alert bar |
| `thankyou.quote` | Only words the founder said or approved, with `source` |
| `real_deadline`, `accepted`, `legal` | The client's real deadline; settled CHECKs with a reason; privacy, terms and refund links |

## Images to plan (add them to the one ChatGPT batch, Stage 4)
| Image | Size and rule |
|---|---|
| Main mockup | Already made for the sales page. Transparent background. Export 720 and 1280 px WebP |
| Bump image | The product as an object (device + cover), readable at 110 px wide. 320 px WebP |
| Upsell hero | 16:9, the founder (real photo) with the product: laptop + guides, product name readable on a phone. 720 and 1280 px WebP |
| Stack thumbnails | One per item, cropped from the upsell hero so they match, 240 px WebP |
| Community photo and QR | From the client (their channel's picture; its real QR code) |

Save them in `my-funnel-pages/images/` and write `"images/name.webp"` in the JSON (one file, or a small and a large one). Previews find them there; live pages use `assets_base` + that path, so set `assets_base` when the images are online. **Logos:** `logo_on_light` is the DARK logo (it sits on white), `logo_on_dark` the LIGHT one; the checker fails a logo that disappears. If the upsell image already shows the product name, set `hide_name_label`.

No image yet? Leave it out of the JSON where it's optional (thumbnails). Never ship a placeholder.

## Done when
- [ ] Bump and upsell pass the tests, or the client overrode a failed one in their own words (logged in `learned-rules.md`).
- [ ] `--check` shows 0 to fix.
- [ ] The person approved the copy, prices, values and guarantee wording.
