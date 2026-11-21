# GoHighLevel notes (out of scope for this playbook)

Kept for the future GHL skill. Not needed to build a sales page.


- **Safety first:** do a read-only audit of the sub-account (funnels, products, courses with member counts, workflows, domains, Stripe, transactions) before creating anything. Prefix internal names ("Rickey · …") but keep buyer-facing names plain. Don't touch existing items, Stripe, domains, users or billing without asking. The user signs in themselves; test purchases are done by the user or in Stripe test mode.
- **Domains:** this account had no free default funnel domain, so an existing domain was used with a path prefix (`/headstart-page`, `-checkout`, `-upsell`, `-thank-you`). Switching domains later is easy, but update shared links (or add redirects), re-verify the Meta pixel domain, and renew a domain that's about to expire.
- **Funnel settings:** turn off "Optimize JavaScript", because it lazy-loads custom code.
- **Products:** they default to "Physical", which adds address fields, so hide those in the order form. Products sync to Stripe in live and test mode.
- **Order form:**
  - One-step; only Full Name + Email; quantity, multi-product and coupons off.
  - Bump = Form settings → Order bump → headline / OTO headline / description (the image is upload-only).
  - After purchase: "Go to a website URL" until the upsell exists, then "Go to the next funnel step".
  - The form renders in the page DOM, so it can be restyled with `.c-order-form .order-form__*` selectors.
- **One-click upsell:** the YES button's "link to" = "One click up/down sell product" + Products = the step's product. NO = a link to the thank-you page. The browser pane couldn't operate these native selects inside the cross-origin builder iframe, so the user had to set them.
- **Builder quirks:**
  - It runs in a cross-origin iframe (`page-builder.leadconnectorhq.com`), so find/read_page/form_input don't reach inside.
  - No drag-and-drop. Add a section first, then section "+" → Quick Add search → click the card.
  - Custom dropdowns: hover + Return, or Up/Down + Return.
  - Save explicitly after every step (an unsaved upsell build was lost).
  - Never open the builder iframe URL standalone (it caused 401s and an expired sign-in).
- **Email editor:** type HTML in short chunks (long input gets garbled). A From Name requires a From email.
- **Courses / workflows:**
  - New-style courses are granted by a workflow action. A "Free" offer would let anyone enroll.
  - Uploads aren't possible from the browser pane.
  - An email can't show or hide sections conditionally, so the bump gets its own workflow and email.
- **Users:** invite a teammate as a user (Account Admin here) and leave the password blank so they set their own.
- **Before going private:** move the loader-hosted code, images and PDFs into GHL Media.
