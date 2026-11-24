# Choosing the order bump and the upsell (and what each page must do)

Read this in Funnel stage F1. It is the thinking behind the pages. The design and copy specs are in `upsell-and-bump.md`.

**What's proven and what isn't.** The structure, design and copy rules come from David's feedback on Rickey's funnel and from the live reference upsell studied for it. Rickey's funnel had no real traffic when this was written (Nov 24 2026), so **no conversion rate is claimed anywhere here**. The price and choice guidance below is direct-response practice, marked as rules of thumb. When a funnel gets real numbers, add them to `feedback-log.md` and correct this file.

## The one idea
Each step sells **the next thing the buyer needs**, at the moment they need it, and asks for one decision.

| Step | The buyer is thinking | The page's only job |
|---|---|---|
| Sales page | "Will this work for me?" | One product, one price, one button. Never mentions the bump or the upsell. |
| Checkout | "OK, let me pay" | Form on the first phone screen. Remind what they get, remove doubt, take the order. |
| Order bump | "I'm here anyway, is there something small that makes this easier?" | One tick, one sentence, no thinking. |
| Upsell | "I bought. What now?" | Confirm the order, then one bigger result, one click, one clear way to say no. |
| Thank you | "Where's my stuff?" | First action in one tap. No selling. |

## Picking the order bump
A good bump answers yes to all of these:
1. **Instantly understood.** A 10-year-old can say what it is from its name and one sentence.
2. **Removes the first obstacle** in using the main product (Rickey: "which product do I sell?" → a list of 37 products).
3. **Done for you, short, usable tonight:** a list, templates, a checklist, a swipe file, a calculator. Not another course.
4. **Complete on its own,** and the main product is complete without it. If the bump solves something the main promise already claims to solve (a starter that keeps dying), say how they differ (a small overlap is fine if the bump clearly goes further), or pick another bump. Never take a needed piece out of the main offer to sell it as a bump.
5. **Countable.** It holds one real number the buyer gets (37 products, 12 scripts). Count it in the file itself.
6. **Cheaper than the main offer.** Rule of thumb: 30% to 70% of the main price (Rickey: $17 on $27).
7. **Delivers itself,** through its own small course or file, with no manual work.

If several candidates pass, choose the one that removes the **earliest** obstacle. If none passes, ship without a bump and say so: a weak bump only adds doubt at the moment of paying.

## Picking the upsell
1. **The next problem, not the same problem again.** Main offer = first result. Upsell = keep it, multiply it, or get it faster. Test: finish "[Main] gets you [first result]. This is how you [next result]." If that sentence sounds forced, it's the wrong upsell.
2. **Wanted by someone who just said yes** and hasn't used the main product yet. It must not imply the main product isn't enough. If it naturally comes after it, say "ready when your first [result] is done".
3. **Deliverable the moment they click YES.** Course access, files, a booking link. If it isn't built, the page doesn't go live.
4. **Priced as a clear step up.** Rule of thumb: 2 to 4 times the main price (Rickey: $97 on $27).
5. **The stack is real.** Every item exists today. Values are the client's, or placeholders marked for approval (`values_approved: false` until they say yes).
6. **The client's real guarantee covers it,** in their words. Ask: "Does your guarantee cover the upsell too?"

Bad upsells: a discount on something they just bought, a second unrelated product, a subscription explained in fine print, anything a person must deliver by hand within minutes.

## Downsell and video upsell
The generator supports both (`upsells` with two entries; `video` instead of `image`). **Neither has been run live by us.** Offer them only if the client asks, and tell them so.
- **Downsell:** a smaller version of the same upsell (fewer parts, lower price), never the same thing cheaper: that teaches buyers to say no first. Its alert bar doesn't re-confirm the order; it says "Wait, before you go: …". YES on the first upsell must **skip** the downsell (set in GHL, then tested).
- **Video upsell:** the same page with a 2 to 5 minute video where the product image was, and "watch this short video" in alert line 2. The text page must still sell with the sound off. Don't hide the offer behind a timer.

## The upsell page, top to bottom, and why each part is there
1. **Alert bar (the brand's accent, full width, first thing seen).** Line 1 confirms the order and says when access arrives. Without it, people think the purchase failed or close the page. Line 2 is the only instruction: "Don't close this page. Take a look at this exclusive one-time opportunity first ↓".
2. **Progress bar, "Order 90% complete".** Shows there's one step left, so leaving feels early.
3. **Pill: "⚡ Exclusive one-time offer".** Names what this page is.
4. **Headline: "You Just Unlocked Your [Main]. Now [the next result they want]…"** Celebrates the purchase, then opens the next want. "10x faster" was Rickey's; any speed or size claim must be the client's to make. If there's no such claim, name the next result instead (looks, ease, variety, keeping it going).
5. **Product image, then the product name** as a label, then **one subheadline**: what it is, how it works in three verbs, what it gives them.
6. **Bridge card:** "[Main] gets you [first result]. This is how you [keep or multiply it]." plus 3 bullets, each a result with its mechanism.
6b. **Proof (optional, strongly wanted):** one real quote, result or screenshot, or a few words from the founder with their photo. Rickey's page has none yet: it's the first thing to add when he gives it.
7. **Offer stack:** name, one-line "so you…" benefit, crossed value. Then crossed total, "You save" (these are values, not old prices: never "discount" or "was" unless it was really sold at that price), "Today, only on this page:" and the price, big. "No need to enter your card again."
8. **Guarantee:** one line, the client's own words.
8b. **Questions (optional):** the one or two real doubts ("I haven't started yet, is it too early?"), answered in a line each.
9. **Lead-in:** "This is an exclusive one-time offer. Only available right here, right now. Once you leave this page, it's gone." and a moving arrow. True **only if it isn't sold anywhere else at this price: ask** (`sold_elsewhere`). **Never** a countdown or "today only" with no real deadline.
10. **YES button:** "YES! Add [Product] to My Order For Only $[price]". Full width, the only colored button on the page.
11. **NO link:** small, underlined, honest about the cost of saying no: "No thanks, I'll keep [the painful thing], and [its honest cost]." Describe the situation, never insult the reader.

No menu, no other links, no footer links that leave the page.

## Who gets what (check this in every funnel)
| Bought | Course access | Emails |
|---|---|---|
| Main only | Main course | Main email |
| Main + bump | Main + the bump's own course | Main email + bump email |
| Main + upsell | Main + upsell course | Main email + upsell email |
| All three | All three, under **one login** | All three |

- **The bump is optional.** Its box starts unticked, its file is **never** in the main course, and no email to every buyer names it. David's check: "as long as they don't get the products list if they didn't get the order bump."
- The thank-you page can't know what was bought. It may say, as a question, "Added [Bump] or [Upsell]? They're in the same place, next to your course." It never links their files.
- Every paid file sits behind the login. Never on GitHub, never on the thank-you page.
