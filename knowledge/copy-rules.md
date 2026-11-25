# Copy rules

Every rule here came from David's feedback on the Rickey page (Nov 2026) or from the kit. They apply to any sales page. Claude applies them in Stage 2d **as proposals the client approves**: never silently rewrite the client's words.

## The short list (check every page)
1. **Never invent** facts, numbers, results, names, testimonials or credentials. Missing = ask or drop it.
2. **Never rewrite the client's own words** (especially the founder's story) without asking. Propose; they approve. After one rejected rewrite, restore the approved text at once.
3. **No em dashes (—) or en dashes (–)** anywhere. Use a comma, colon, "to", "for" or parentheses.
4. **No "steal"** (buttons say GET). Check the client's own "never" list too.
5. **One button label everywhere**, with the price: `GET INSTANT ACCESS · $27 →`. Every button goes straight to checkout.
6. **5th-grade clarity.** Short sentences. One idea per line. A claim carries **one** number, not five. ("Get my list of 37 products people are buying right now", not "37 picks across 8 lanes, 8 viral, plus a calendar".)
7. **Headline** = end result + time + emotional payoff. **Subheadline** = how, made easy, 3–4 value props. **Eyebrow pill** = proof, not the founder's name.
8. **Promise sales/results, never income.** Next to any revenue number: "Those are my results… Not a promise of what you'll make." Label numbers correctly (sales/GMV ≠ earnings).
9. **Only list what's really in the offer.** Check every item against the client's latest word, before setting values. AI tools add items that don't exist.
10. **"Value", never "regular price"** for stack values. Add-ons stay out of the total. Recompute total and "you save" whenever an item changes.
11. **No fake urgency.** "Today only" only with a real deadline. On an upsell page, "only on this page" is true and fine.
12. **Don't announce the order bump on the sales page.** It appears only in the checkout.
13. **Section headlines sell on their own** (people skim headlines only). "Real people, real results" is banned; say the benefit.
14. **Proof headline matches the proof type** (owner's own proof → "Don't Take My Word for It.").
15. **Risk reducer under buttons is short** ("One-time $27 · instant access"). Refund terms live in the guarantee block.
16. **Highlight proof and the main benefits**, never filler (Rickey: not "one video a day").
17. **Mark your own wording.** When Claude writes a new line, say so and ask for the OK.

## The full rules with Rickey examples and why
| Rule (general) | Rickey example | Why |
|---|---|---|
| Save the client's original untouched and treat `copy.md` as the approved version. Never rewrite the client's words without asking. | `copy-original.md`; the tool's note said "Body copy otherwise unchanged, David rated it very solid". The v10/v11 Instagram rewrite of section 3 was rejected (#31: "Have the copy as it was before. Don't make any changes.") | Kit rule, and the client owns the voice. An unrequested "improvement" cost two rounds. |
| Resolve every option to a single line before building. Strip tool notes. | Hero "1 + A"; review, framework and traffic notes plus the hero image description removed | The page can show only one headline. The notes aren't page copy. |
| No em or en dashes anywhere, including in client-supplied text and HTML comments. Use a comma, colon, "for", "to" or parentheses. | "Days, Starting From Zero", "sales: set up", "FOR $27", "3 to 5 hours", "($57 value)" | David's standing preference (#16). Verify with `grep -c '—\|–' index.html` = 0. |
| Never use "steal". Buttons say "GET". | "GET MY HEADSTART FOR $27", later "GET INSTANT ACCESS · $27 →" | Client taste (#16). This conflicts with the kit's "Steal my…" subheadline formula, so drop that formula. |
| Anchor values are labeled "value", never "regular price", "was" or "Today only". Add-ons stay out of the total. | $57/$47/$29/$97 = $230, later $57/$47/$97 = $201, "You save $174"; the $17 add-on separate | Honest framing: the items never sold at those prices, and there's no deadline. |
| Before setting values, confirm every listed deliverable is in the offer. | "Templates" ($29) and "both milestone playbooks" were in the tool's copy but not in the offer: removed at #23 and #27 | AI-generated copy can list items that don't exist. |
| Wherever revenue numbers appear, add the compliance line. Promise sales, never income amounts. | "Those are my results, so you can see it's real. Not a promise of what you'll make." in sections 10 and 12 | Earnings-claim risk. The tool's framework note: "promises *sales*, never income amounts". |
| A proof headline must fit the type of proof. | "Wait… This Actually Works for People Like Me?" (student proof) became "Don't Take My Word for It." (owner proof) | A mismatched promise reads as fake. |
| Keep the risk-reducer under the button short. Refund terms belong in the guarantee. | Hero fine print became "One-time $27 · instant access", plus the same line in the top alert bar | The long refund sentence cluttered every button (#16). The guarantee later got its own block (#22). |
| The hero pill is proof only, not the creator's name. | "$4M+ in TikTok Shop sales · top-1% creator" | #17 |
| Section 2 headline: action and ongoing, not one-off; end on what they get. | "Post Your First One." → "You Need to Start Posting." → "You Need a Plan That Gets You Sales." (v1.1, Nov 24) | #16, P4.9 |
| Emphasize proof and the main benefits, not the mechanics. Ask which phrases to emphasize. | Highlight "behind Rickey's $4M+ in TikTok Shop sales"; red bold on "find winning products", "make viral videos", "make sales". Not "one video a day". | #20 reversed Claude's carry-over emphasis |
| Use one CTA label everywhere, with the price. (Adopted after Slice A.) | Every button "GET INSTANT ACCESS · $27 →". On Nov 20 they jumped to the offer stack; since v1.1 (Nov 24) every button goes straight to checkout. | #20: consistency and price clarity |
| Never invent facts. Flag claims that need backing up. Leave the client's disclaimers as a `{FILL IN}` note until they supply them. | Footer `{FILL IN: your disclaimers…}`; logo partnerships flagged | Kit rule and legal exposure |
| Leave quotes and parenthetical lines in `copy.md` as plain lines, without `>` or `(`, so the checker verifies them. | `"I'm not lazy…"` lost its blockquote; "(Those are my results…)" lost its parentheses | `check_page.py` skips lines starting with `>`, `<!--`, `(` or `[` |

## Order bump and upsell copy

1. The bump is never mentioned on the sales page. It appears only at checkout.
2. Headline = the checkbox sentence: "Yes! Add [Product]".
3. Price line: "Only $[price] today. One-time payment." (plain, no brackets or shouting).
4. Description = **one pain + one number + one promise**, one sentence: "Stop guessing what to sell. Get my list of 37 products people are buying right now, so you can pick your first product tonight."
5. Count something concrete the buyer gets ("37 products"), and get the number from the real deliverable (counted with pypdf). Never use internal structure words ("lanes", "scroll-stoppers", "seasonal calendar").
6. **One number only.** Sub-counts confuse (the "29 picks across 8 lanes, 8 viral" version was rejected).
7. 5th-grade test: a 10-year-old can say what they get and why it helps.
8. Length: it must fit on a phone next to the 96–110px image (~130 characters worked; 256 was "too long").

---

