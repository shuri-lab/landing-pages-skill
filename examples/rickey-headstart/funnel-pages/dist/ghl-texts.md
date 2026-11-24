# GoHighLevel texts and settings: Rickey, TikTok Shop Headstart

Type these exactly. Written by `tools/build_funnel_pages.py`. The steps to place them: the GHL Funnel Playbook (Stages 3 to 10).

## Products (catalog name → price)
- `Rickey · TikTok Shop Headstart` → $27
- `Rickey · The Starter Product List` → $17 (Bump Product on the checkout step)
- `Rickey · My $4M TikTok Shop System` → $97 (on the upsell step `upsell`)

## Steps and paths
1. https://davidhsai.com/headstart-page
2. https://davidhsai.com/headstart-checkout
3. https://davidhsai.com/headstart-upsell
4. https://davidhsai.com/headstart-thank-you

## Order form (checkout)
- Headline: Contact information
- Payment title: Payment details
- Button: GET INSTANT ACCESS →
- Button subtext: One-Time Payment • Instant Access
- Fields: Full Name + Email only. After purchase: Go to the next funnel step.
- Left column fragment: `dist/checkout-left.html`, root id `gtc-root`

## Order bump (checkout only, box unticked by default)
- Headline: Yes! Add The Starter Product List
- OTO line: Only $17 today. One-time payment.
- Description: Stop guessing what to sell. Get my list of 37 products people are buying right now, so you can pick your first product tonight.
- The banner, arrow and image are added by the page, not typed in GHL.
- Delivers: Its own one-lesson course with the PDF, granted only by the bump workflow

## Upsell step `upsell`
- Fragment: `dist/upsell.html`, root id `gtu-root`
- YES button text: YES! Add My $4M TikTok Shop System to My Order For Only $97
- YES button action: link to = One click up/down sell product; Products = this step's product
- NO link (Custom Code element under YES): `<a class="gtu-no" href="https://davidhsai.com/headstart-thank-you">No thanks, I'll keep guessing which products and hooks work, and take 10x longer to get my sales.</a>`
- Delivers: Its own course (lessons + 3 PDFs), granted only by the upsell workflow

## Thank-you step
- Fragment: `dist/thank-you.html`, root id `gtty-root`

## Delivery: one workflow per product (Order submitted, Global product Is …)
- Workflow `Rickey · TikTok Shop Headstart delivery`: Global product Is **Rickey · TikTok Shop Headstart** (the prefixed catalog product, not the course's own product) → grant the course "TikTok Shop Headstart" only → email `dist/emails/main.html` · Subject: You're in. Here's Day 1 · Preview: Your course login, your guide and the Rickey Army link.
- Workflow `Rickey · The Starter Product List delivery`: Global product Is **Rickey · The Starter Product List** (the prefixed catalog product, not the course's own product) → grant the course "The Starter Product List" only → email `dist/emails/bump.html` · Subject: Your Starter Product List · Preview: Pick your first products tonight instead of guessing.
- Workflow `Rickey · My $4M TikTok Shop System delivery`: Global product Is **Rickey · My $4M TikTok Shop System** (the prefixed catalog product, not the course's own product) → grant the course "My $4M TikTok Shop System" only → email `dist/emails/upsell.html` · Subject: Your $4M TikTok Shop System is ready · Preview: Your course, your three guides and where to start.

## Who gets what (nobody gets what they did not buy)
| Bought | Courses | Emails |
|---|---|---|
| Main only | TikTok Shop Headstart | main |
| Main + bump | TikTok Shop Headstart, The Starter Product List | main, bump |
| Main + My $4M TikTok Shop System | TikTok Shop Headstart, My $4M TikTok Shop System | main, upsell |
| Everything | TikTok Shop Headstart, The Starter Product List, My $4M TikTok Shop System (one login) | all |

## Not in this file (from the GHL plan, Stage 1)
Funnel name, sales page root id, sender address, buyer tags, course lessons, tax, statement name, tracking.
