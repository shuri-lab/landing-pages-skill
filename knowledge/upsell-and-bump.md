# Upsell page, checkout column and order bump

The same playbook builds the pages around the sales page. This is how we built Rickey's $97 one-click upsell page and styled the checkout's left column and order bump (Nov 20 2026). The live files: `examples/rickey-headstart/upsell/`. GoHighLevel wiring (one-click charge, products, workflows) is out of scope.

## D. Upsell page (one-click upsell, $97)

### D1. How the reference page was studied (repeatable method)
- Opened the reference in the browser. Read each section's text with JS (`.c-section` id + display + first 300 chars). Found its buttons by text (`/yes|no thanks|add/i`) and read their tag, class and href.
- Its offer row was hidden until a video timer ended (`display:none`). It was revealed temporarily (`row.style.display='block'`) only to see the styling.
- Findings: the accept button is a native builder button with a one-click-upsell action. The decline is a plain link to the thank-you page.
- Reference copy pattern: "Your order is on the way & will be available to download in the next 5 minutes. Please watch this important video below for access details and an exclusive opportunity…", "⚡ You Just Unlocked The System. Now Get Results 10x Faster…", a countdown that unlocks the next step, "ONLY $67 $47 NOW", "➡️ This is exclusive one-time offer. Only available right here, right now", "YES! Add The AI Avatars Bonus to My Order For Only $47", "No thanks, I'll spend a lot of time coming up with average AI avatars every time and spend x10 more time".
- What we changed for "no VSL": replaced "watch this video" with "take a look at this exclusive one-time opportunity", and dropped the timer gate.

### D2. Offer contents: sourced, not invented
- The offer stack and deliverable text came from the project PDFs via pypdf (`PdfReader(f).pages[i].extract_text()`).
- The course deck was image-only, so the module titles were read from a contact sheet. Each page's largest embedded image was pulled with pypdf + PIL, resized to 480 wide and pasted 5 per row (39 pages). The Swift PDFKit renderer stopped building after an SDK/compiler mismatch.
- The product image (`offer-2-image-v2.png`, 1672×941) was converted to `offer-2-system-720/1280.webp`. Stack thumbnails were cropped from the same image: `o2-course (355,390,1010,905)`, `o2-hooks (1012,440,1250,885)`, `o2-formats (1236,445,1448,885)`, `o2-checklist (1440,445,1660,885)`, each thumbnailed into 240×240 at WebP q82.
- The price ($97) came from the user. Item values ($297, $47, $47, $37) were **made up as placeholders**, as on Offer 1, and flagged as such in the report.

### D3. Section-by-section structure (final `ghl-upsell.html`, scoped under `#gtu`, tokens `--red:#D30805 --ink:#101017 --cream:#FFF8E7 --line:#E7E3DC`)
1. **Alert bar** (`.alert`, red background, white, centered, `role="status"`, padding 16/16/14):
   - Line 1 (Lato 700, 17px; 20px ≥768px), with a white circle "✓" badge: "Your order is confirmed! You'll have access to TikTok Shop Headstart in the next 5 minutes."
   - Line 2 (Poppins 900, 18px; 22px ≥768px): "Don't close this page. Take a look at this exclusive one-time opportunity first ↓"
2. **Progress band** (`.prog`, ink background): "ORDER 90% COMPLETE" (Poppins 800, 13/14px uppercase) + a 12px bar at 90% width with animated diagonal stripes (`repeating-linear-gradient(45deg,#ff3b37 0 10px,#D30805 10px 20px)`, 1 s loop).
3. **Hero** (centered, padding-top 34px; 44px desktop):
   - Pill (cream background, 2px dashed red border, red text, uppercase 13px): "⚡ Exclusive one-time offer".
   - H1 (Poppins 900, 30px; 44px desktop, max-width 760): "You Just Unlocked Your Headstart. Now Get Your Sales <mark>10x Faster</mark>…" (the mark is red text, not a highlight).
   - Product image (`.shot`, 100% up to 760px, 720/1280 srcset, `fetchpriority="high"`).
   - Product title as a label: black box, white Poppins 900 26/38px, `rotate(-1deg)`, `box-shadow:5px 5px 0 red`: "My $4M TikTok Shop System".
   - Subheadline (19/21px): "The exact system behind my $4M TikTok Shop. **How I find winning products, hook people in the first 2 seconds, and film videos that sell**, so every video you post has a real shot at making money."
4. **Bridge** (dark card, radius 18, max-width 720): H2 "The Headstart gets you your first sale.<br><mark>This is how you keep them coming.</mark>", then 3 check bullets (red circle ✓):
   - "Know if a product will sell **before** you film it, with the exact panel I read on every product."
   - "Stop the scroll in the first 2 seconds with my hook stacks, so your videos get watched instead of skipped."
   - "Film a whole week of videos in one sitting, then turn one winning product into steady income."
5. **Offer stack** (`.offer`, white, 2px ink border, radius 20, `box-shadow:8px 8px 0 red`):
   - Dark header: "Everything You <mark>Get Today</mark>" + red pill "One-time $97 · instant access".
   - Item rows: grid `76px 1fr auto` (92px desktop, 60px ≤420px). Thumbnail tile (#F4F2EE) | title (Poppins 800 17/19px) + one-line benefit | crossed value (`<s>` with a red 2.5px strike).
   - Course "My $4M TikTok Shop System" ~~$297~~: "The full video course. My own method, shown step by step:" + 8 numbered modules in 2 columns (1 column ≤420px): How to find winning products · Make videos people can't scroll past · Sell without looking like you're selling · Turn your views into sales · Film a whole week in one sitting · Turn one winner into steady income · Build multiple income streams · Protect your account.
   - "The Product Checklist" ~~$47~~: "The 6 quick checks I run before I film anything, so you only make videos for products that actually sell."
   - "The Hook Bank" ~~$47~~: "How I stop the scroll in the first 2 seconds, with my real hook stacks you can copy."
   - "The Format List" ~~$37~~: "The 6 video formats that blend into the feed and still sell, so your videos look like content, not ads."
   - Total bar (2.5px ink top border): "Total value:" ~~$428~~ (24px, red strike 3px).
   - Deal: dashed cream pill "Exclusive discount · you save $331" → "Today, only on this page:" + **$97** (Poppins 900 64px; 76px desktop, red) → note "One-time payment. Added to your order in one click, no need to enter your card again."
6. **Guarantee** (#F7F5F1 strip, red shield SVG with a check): "**Your money's protected.** Do the work and still no sale? You get a full refund."
7. **Lead-in to the buttons:** "➡️ This is an exclusive one-time offer." (Poppins 800 19/23px) / "Only available right here, right now. Once you leave this page, it's gone." (16/18px grey) + a red down arrow SVG bouncing 9px (1.1 s).
8. **Buttons, native to the platform** (in their own section/row below the code section, so the code section stays edge-to-edge):
   - YES (native button with the one-click upsell action): "YES! Add My $4M TikTok Shop System to My Order For Only $97"
   - NO (a small custom-code element): `<a class="gtu-no" href="<thank-you URL>">No thanks, I'll keep guessing which products and hooks work, and take 10x longer to get my sales.</a>`
9. `document.title='One-time offer | My $4M TikTok Shop System'`.

### D4. Copy patterns (reusable)
- **Alert bar:** confirm the purchase plus an access time ("in the next 5 minutes"), then "Don't close this page" + "exclusive one-time opportunity" + ↓.
- **Headline:** "You Just Unlocked Your [Offer 1]. Now Get Your [Result] 10x Faster…"
- **Bridge:** "[Offer 1] gets you [first result]. This is how you [keep/multiply it]."
- **Stack:** every item = name + a one-line "so you…" benefit + crossed value. Total crossed. Savings = total − price. "Today, only on this page: $X". One-click reassurance ("no need to enter your card again").
- **Urgency without fake deadlines:** "only on this page / once you leave, it's gone" (true for a one-time offer). Never "today only" when no deadline exists (a learned rule from Offer 1).
- **YES:** "YES! Add [Product] to My Order For Only $[price]".
- **NO:** "No thanks, I'll [keep doing the painful thing] and take 10x longer to [get the result]."

### D5. Design rules
- Same brand tokens and fonts as the sales page (Poppins headings, Lato body).
- Every section is scoped under a unique id (`#gtu`) so builder CSS can't leak in and fragment CSS can't leak out.
- Mobile-first sizes, with one `@media(min-width:768px)` block for desktop sizes and one `@media(max-width:420px)` block for very narrow phones.
- Offset "sticker" shadows (`5px 5px 0` / `8px 8px 0` in red or ink) and dashed pills for the "special" cues, matching Offer 1.
- `@media(prefers-reduced-motion:reduce)` turns off the stripes, bouncing arrow and button pulse.

### D6. Buttons: HTML vs native, and how the native ones were styled
- **What's native and why:** only the YES button is a native builder button, because the one-click charge on the saved card is a platform action. The NO link is plain HTML inside a custom-code element (a link to the thank-you page). Everything else is the HTML fragment.
- **Tagging native elements:** builders rarely let you add classes, so the fragment tags elements by their text, retrying for ~9 s while the builder renders:
  ```js
  function tag(){document.querySelectorAll('.c-button a, .c-button button').forEach(function(b){
    var t=(b.textContent||'').trim().toLowerCase();
    if(t.indexOf('yes!')===0) b.classList.add('gtu-yes'); else if(t.indexOf('no thanks')===0) b.classList.add('gtu-no');});}
  tag(); var n=0,iv=setInterval(function(){tag();if(++n>30)clearInterval(iv);},300);
  ```
- **YES style:** `display:block; width:100%; max-width:720px; background:#D30805; color:#fff; border:2px solid #101017; border-radius:14px; padding:20px 18px (24/22 desktop); Poppins 900 21px (25px desktop) line-height 1.25; text-transform:none; box-shadow:5px 5px 0 #101017; white-space:normal;` with a pulse `scale(1)→scale(1.025)` over 1.8 s, and `filter:brightness(1.06)` on hover. All declarations need `!important` to beat builder styles.
- **NO style:** centered, max-width 620, no background/border/shadow, `color:#6b6b75`, Lato 700 15px (16px desktop), underlined with a 3px offset, `margin-top:18px`.
- **Wrapper spacing for the native elements** (via `:has()`): `.c-button:has(.gtu-yes){padding:4px 18px 0!important;max-width:756px;margin:0 auto!important}`, `.c-custom-code:has(.gtu-no){padding:0 18px 44px!important}`, `[class*="section-"]:has(.gtu-yes){padding-bottom:0!important}`.

### D7. Mobile fixes found on the live page
- **Image overflow:** `#gtu .shot{max-width:760px}` beat the generic `#gtu img{max-width:100%}` because it is more specific, so the image was 760px on a 393px screen (`scrollWidth` 778). Fix: `#gtu .shot{width:100%;max-width:760px}`. Found with:
  ```js
  const W=document.documentElement.clientWidth;
  [...document.querySelectorAll('#gtu *, .c-button, .c-button *, .gtu-no')].filter(e=>e.getBoundingClientRect().right>W+1).map(e=>(e.className||e.tagName)+' '+Math.round(e.getBoundingClientRect().width))
  ```
- **Bullet split into columns:** `li{display:flex}` containing text plus `<b>` turned the bold run into its own flex item. Fix: wrap each `li`'s content in one `<span>`.
- **Edge-to-edge buttons on phones:** added the 18px side padding on the button wrappers (D6).
- **NO link** centered with `text-align:center!important`.
- Checked again on phone (no overflow) and at 1280×800.

---

## E. Order bump and the checkout left column

### E1. Checkout layout (desktop)
Two columns, like the user's reference checkout: left = offer summary (custom HTML via loader, root `#gtc-root`, scope `#gtc`), right = the platform's order form with the bump checkbox. Desktop block `.gtc-d`:
- Logo (34px high).
- Red pill "You're one step away".
- H1 "Get Your First TikTok Shop Sales in the Next 30 Days, <span red>Starting From Zero</span>" (Poppins 800 26px).
- Mockup (no-background hero, 1280 WebP).
- Dark "What you get today" box: rows with red ✓ circles, bold item name + crossed value ($57/$47/$97); "Total value" ~~$201~~ under a 2px red rule; "Today" **$27** in a red badge (Poppins 800 22px).
- Guarantee in a 2px dashed red box with a black ✓ circle. It uses the **approved copy verbatim**: "Your Money's Protected. Do the 30-day challenge, post every day, and if you haven't made a sale in 90 days, you get a full refund." (A paraphrase was caught and replaced with copy.md's exact wording.)

### E2. Mobile-compact rules (form above the fold)
- Below 767px: hide `.gtc-d`, show `.gtc-m`, `#gtc{padding:0}`.
- `.gtc-m` contents:
  - Logo 22px high, centered (`margin:2px auto 10px`).
  - **One dark card**, grid `96px 1fr`, gap 12, radius 14, padding 10/12:
    - 96px product image (720 WebP);
    - title "TikTok Shop Headstart" (Poppins 800 16px);
    - includes line "7-Day Course + 30-Day Challenge + Rickey Army channel" (12.5px, 78% white);
    - price row ~~$201~~ + red badge "$27 today" (15px).
  - **Trust row** under the card, centered, 11.5px #4a4a55, each item prefixed with a red ✓: "One-time payment · Instant access · 90-day refund".
  - Less builder spacing on phones only: `[class*="section-"]:has(.c-order-form){padding-top:6px!important;padding-bottom:6px!important}` and `.c-column:has(#gtc-root)>.inner,.c-column:has(.c-order-form)>.inner{padding-top:4px!important;padding-bottom:4px!important}`.
- General rule: on phones, the summary is at most one card plus one trust line (~140px tall), and the first input sits in the top half of a 393×852 screen. Desktop stays unchanged.

### E3. Contact-form polish (generic rules + the GHL selectors used)
- **Surface:** white card, `1px solid #E7E3DC`, radius 16, `box-shadow:0 10px 30px rgba(16,16,23,.07)`, padding 22/20 (`.order-form__surface`).
- **Numbered steps** with a CSS counter on the two headings (`.order-form__headline`, `.order-form__pay-head`): 28px black circles with white numbers, Poppins 800 19px headings. Result: "1 Contact information", "2 Payment details".
- **Labels:** Lato 700 14px, ink, no uppercase.
- **Inputs:** height 50px, padding 0 14px, background `#FAF9F7`, `1.5px solid #D6D2CA`, radius 10, Lato 16px. Hover border `#B9B4AA`. Focus: white background, border `#D30805`, ring `0 0 0 4px rgba(211,8,5,.12)`. Placeholder colour `#9A968F`. (16px input text also stops iOS from zooming on focus.)
- **Placeholders and autofill** (set by script): "Your full name" (`autocomplete="name"`), "you@example.com" (`autocomplete="email"`).
- **Helper under email:** "Your course login is sent here." (12.5px #6b6b75).
- **Only the useful fields:** Full Name and Email (no phone/company/address for a digital product).
- **Hide what the buyer can't act on:** the single-product picker (`.order-form__offer{display:none}`; the product stays selected), the subtotal rows (`.order-form__summary-row:not(.order-form__summary-row--total)`) and the builder's default subheading ("Upgrade Your Order & Save!", `.order-form__subheadline`). Keep "Total due today" (Poppins 800 16px). Drop the extra border above the total (it made a double divider).
- **Keep what the client liked:** the payment section and the "GET INSTANT ACCESS →" button with subtext "One-Time Payment • Instant Access" and footer "Secure checkout powered by Stripe".

### E4. Order bump design (make it pop)
- **Box** (`.order-form__bump`): grid `auto auto 1fr` (arrow | checkbox | headline), padding `0 14px 14px`, background `#FFF8E7`, **`2.5px dashed #D30805`**, radius 14, `overflow:hidden`, **glow** `@keyframes gtglow{0%,100%{box-shadow:0 0 0 0 rgba(211,8,5,0)}50%{box-shadow:0 0 0 6px rgba(211,8,5,.16)}}` over 2.2 s.
- **Checked state:** `:has(.order-form__bump-check:checked)` → background `#FFEDEC`, solid border, no animation, a static 4px ring.
- **Banner** across the top (`.gt-bump-top`, injected, spans all columns with negative side margins): red background, white Poppins 800 12.5px uppercase, letter-spacing .06em: "⚡ One-time offer · only on this page".
- **Arrow** (`.gt-arrow`, injected before the checkbox): 30×24 SVG `M2 12h20M15 4l8 8-8 8`, stroke 4, red, round caps, nudging `translateX(-3px)↔translateX(4px)` every 1 s.
- **Checkbox:** 24×24, `accent-color:#D30805`.
- **Text:** headline "Yes! Add The Starter Product List" (Poppins 800 17px, 16px ≤400px, underlined with `rgba(211,8,5,.45)`, 3px offset); price/OTO line in red Lato 800 13.5px; description Lato 14.5px/1.45 #2b2b33. All forced `text-align:left` (the builder right-aligned the OTO line). The builder's own price inside the bump is hidden, since the price is already in the OTO line.
- **Image:** `starter-product-list-320.webp`, injected **inside the description**, `float:right; width:110px` (96px ≤400px), radius 8, so the text wraps around it. The body wrapper uses `display:contents` so the headline and OTO sit in grid column 3 and the description spans the full width (`grid-column:1/-1`) with a clearfix.
- **Motion off** under `prefers-reduced-motion`.

### E5. Enhancer script pattern (for platform-rendered forms)
- The order form is rendered by the platform's framework and **re-renders** (e.g. when the bump is ticked), which wipes injected nodes. So `enhance()` is **idempotent** (it checks `if(!b.querySelector('.gt-bump-top'))` and so on before adding anything) and runs: once, then every 250ms for 40 tries, and on every DOM change via `new MutationObserver(enhance).observe(document.body,{childList:true,subtree:true})`.
- What it adds: placeholders and autocomplete, the email helper, the bump banner, the arrow before the checkbox, and the image inside the description.
- **Verification test** (run on the live checkout):
  ```js
  const t=()=>document.querySelector('.order-form__summary-row--total').innerText.replace(/\s+/g,' ');
  const before=t(); document.querySelector('.order-form__bump-check').click(); await new Promise(r=>setTimeout(r,800));
  const after=t(); const radio=document.querySelector('.order-form__prod-radio').checked;
  document.querySelector('.order-form__bump-check').click(); await new Promise(r=>setTimeout(r,800));
  ({before,after,back:t(),mainProductStillSelected:radio,bumpImgs:document.querySelectorAll('.gt-bump-img').length,arrows:document.querySelectorAll('.gt-arrow').length})
  ```
  Expected: `$27.00 → $44.00 → $27.00`, `true`, `1`, `1`.

### E6. Bump copy rules
1. The bump is never mentioned on the sales page. It appears only at checkout.
2. Headline = the checkbox sentence: "Yes! Add [Product]".
3. Price line: "Only $[price] today. One-time payment." (plain, no brackets or shouting).
4. Description = **one pain + one number + one promise**, one sentence: "Stop guessing what to sell. Get my list of 37 products people are buying right now, so you can pick your first product tonight."
5. Count something concrete the buyer gets ("37 products"), and get the number from the real deliverable (counted with pypdf). Never use internal structure words ("lanes", "scroll-stoppers", "seasonal calendar").
6. **One number only.** Sub-counts confuse (the "29 picks across 8 lanes, 8 viral" version was rejected).
7. 5th-grade test: a 10-year-old can say what they get and why it helps.
8. Length: it must fit on a phone next to the 96–110px image (~130 characters worked; 256 was "too long").

---

