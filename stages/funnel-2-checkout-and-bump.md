# Funnel stage F2 of F5: Checkout page and order bump

**Goal:** the checkout's left column, the restyled order form and a bump that stands out, reviewed in a local preview before GoHighLevel exists.

**Read first:** `knowledge/upsell-and-bump.md` part E (every design value and why).

## Steps
1. **Build:** `python3 PLAYBOOK/tools/build_funnel_pages.py my-funnel-pages/funnel-pages.json`. It writes:
   - `dist/checkout-left.html`: the left column **plus** the CSS and script that restyle GHL's own order form and bump;
   - `preview/checkout.html`: the page next to a mock of GHL's order form (real class names), so the styling is visible now.
2. **Check:** `node PLAYBOOK/tools/check_funnel_pages.mjs my-funnel-pages`, then open the checkout screenshots in `shots/`.
3. **Look for** (phone first, 393×852):
   - the first field is on the first screen, ideally in its top half; the summary is **one card plus one trust line**;
   - the bump is the loudest thing in the form: dashed border, tinted box, banner, moving arrow, large **unticked** checkbox, image;
   - bump text left-aligned, the sentence fits beside the image, nothing under 11 px;
   - "Select product" and the subtotal are hidden; "Total due today" stays and changes when the box is ticked, and back;
   - desktop: the left column repeats the promise, what they get, the total value, today's price and the guarantee in the approved words.
4. **Change copy in the JSON.** A design change for this client only goes in `my-funnel-pages/extra-checkout.css` (or `extra-upsell.css`, `extra-thank-you.css`): the build adds it after the standard styles every time. A change every client should get goes in the playbook's `tools/funnel_templates/`. Never edit `dist/` by hand: the next build overwrites it.
5. Open `shots/checkout-phone-bump-ticked.png` too: the ticked box must look clearly chosen and the total must have changed.

## Rules
- Only Full Name and Email for a digital product. One-step form. No quantity, coupons or second product.
- The sales page never mentions the bump. The build checks this when `sales_page` is set in the JSON. If there is no file, read the live page yourself, then accept the `sales_page` CHECK.
- If the main guarantee doesn't cover the bump, `guarantee_covers_bump: false` adds one line saying what it's for.
- On phones the left column is hidden, so the guarantee shows under the order button, added by the page's script (never tried on a live GHL page yet: look at it there).
- The bump's file isn't in the main course. Its delivery is its own (see `funnel-offers.md`, "Who gets what").
- Legal links (privacy, terms, refunds) show under the left column when the JSON has them. Never write legal text.
- GHL re-renders its form when the bump is ticked, so anything added by script must check before adding. The built script does.

## Done when
- [ ] Checker passes checkout at both sizes; bump totals go base → base + bump → base.
- [ ] You looked at all four checkout screenshots.
