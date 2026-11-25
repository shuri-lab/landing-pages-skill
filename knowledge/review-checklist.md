# Review checklist (pass/fail)

Used in Stage 6 (Claude reviews its own page before anyone sees it) and by the test (`test/rubric.md`). **[auto]** means `test/grade.py` / `tools/shoot.mjs` checks it. Everything else, Claude checks by looking at the screenshots. Every item came from David's feedback on the Rickey page.

## A. Phone first (393×852, iPhone 16)
1. **[auto] Above the fold:** the alert bar, logo, proof pill, headline, hero image, subheadline and **button** are all visible before scrolling. Target: button bottom ≤ ~800px of 852; Rickey's was 764.
2. Not cramped. Phone minimums:
   - alert bar 12.5px
   - pill 13.5px
   - headline ≥ 30px
   - subheadline 17px / 1.55
   - fine print 13.5px
   - full-width button
3. **[auto] No sideways scroll** at any size.
4. Brand-logo slider under the hero is big enough to notice (logos ~40px tall) and never runs out (no empty gap at any width).
5. Sticky bottom bar appears after the hero, hides at the offer stack, never covers the footer text.
6. Every section: headline first, then media, then body. Nothing overlaps; nothing is cut off.
7. Statement lists and cards have air (no cramped stacks); about 40px between a slider and the next text.

## B. Desktop (1280×800, 1440×900, 1920×1080)
8. **[auto]** Hero in two columns (text left, mockup right) and fits the first screen. The logo strip is visible on the first screen at 1280×800 and 1440×900.
9. Body text 17.5–21px; outcome titles are real headings (~29px); no big empty white areas.
10. Sliders and carousels fill the width at 1920 (no gaps).

## C. Copy
11. **[auto] One CTA label on every button** (e.g. `GET INSTANT ACCESS · $27 →`).
12. **[auto] Every button goes straight to checkout**, the sticky bar included, all with the same link. None jumps to `#buy`.
13. **[auto] No em/en dashes. No "steal".** No other words on the client's "never" list.
14. **[auto] No placeholders** (`[Insert…]`, `[image]`, `PASTE-YOUR…` except the checkout link before it exists).
15. Headline = end result + time + emotional payoff. Subheadline = how, made easy, with 3–4 value props, and the proof phrase marked. Nothing highlighted that is filler.
16. Every number is real and correctly labeled (sales ≠ earnings). No income promises. No invented testimonials.
17. The offer lists only what is really included. Values say "value". Total value and "you save" add up.
18. No fake urgency ("Today only") without a real deadline.
19. The founder's story is the client's words, unchanged unless they approved a change.
20. The order bump is NOT announced on the sales page. It lives only in the checkout.

## D. Sections and components
21. Alert bar at the top (brand gradient, offer one-liner).
22. Dark/light rhythm: dark sections spread through the page (about every 3rd section) so it never reads as one long section.
23. Each outcome claim has its visual (real screenshots for proof, mockups for features).
24. Pain cards: no 01/02/03 numbers; bold lead line, muted body, colored punchline.
25. Offer stack:
    - dark header band
    - product mockup
    - item rows with thumbnail and crossed-out value
    - "Total value" bar
    - deal box with a "You save" badge, "Today: just $X."
    - button and trust row
26. Guarantee is its own block right after the offer stack (seal + one-sentence condition).
27. Video carousel: muted, looping, lazy-loaded from a CDN.
28. Proof slider of real screenshots, with a "not a promise of what you'll make" note.
29. Footer: logo, earnings disclaimer, platform non-affiliation notice, refund policy.

## E. Images and speed
30. **[auto] No broken images.**
31. Images are WebP at display size; the hero has `fetchpriority="high"` and a `srcset`; everything below the fold is lazy. **[auto]** Total image weight on a phone full scroll ≤ ~1.5 MB.
32. Videos are light (`w_320,q_auto:eco,ac_none,du_10,f_auto`) and load only near the screen.
33. No third-party logos in AI images. Founder photos are real and licensed; no photo is used twice.
34. Transparent mockups wherever a background tint or gradient sits behind them.

## F. Before showing the client
35. `check_page.py` says "OK: nothing that must be fixed".
36. You looked at **every section** at phone and desktop size (screenshots in `my-sales-page/shots/`).
37. Your wrap-up says which lines are your own wording ("these lines are mine, please check them").

## G. Part 2 pages (checkout, bump, upsell, thank-you, emails)
38. **[auto]** `build_funnel_pages.py` says 0 to fix; `check_funnel_pages.mjs` says all pages pass.
39. Checkout: first field on the first phone screen; the bump box is the loudest thing in the form and starts unticked; totals change and change back.
40. The bump is not on the sales page, not in the main email, and its file is not in the main course.
41. Upsell: alert bar at the very top (order confirmed + access time + stay on this page), progress bar, headline on the first phone screen, stack with crossed total and savings, price the biggest thing, guarantee the client agreed covers it, YES with product and price, honest NO.
42. Squint test on the phone screenshot: alert bar, price and YES stand out.
43. Thank-you: first action in one tap, no paid file links, no selling, every link filled before real traffic.
44. Every email: one product, the founder's voice, one action, a real help line.
45. Every number, value and claim has a source or the client's yes.
