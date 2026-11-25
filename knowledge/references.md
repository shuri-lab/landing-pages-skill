# Reference pages and repos

Pages and code we learned from. Borrow **structure and components**, never branding, colors, words or claims.

| Reference | Link | What we took |
|---|---|---|
| JJ Smith "Look Younger After 40" (our own earlier page) | https://mycoach.jjsmithonline.com/look-younger | Gradient alert bar, hero that fits the phone screen, sticky bottom CTA, "featured in" logo slider, offer stack and deal box structure, one CTA label that scrolls to the stack (details below) |
| JJ landing page source (React/Vite, Lovable) | https://github.com/shuri-lab/jj-landing-page | Same components in code (`src/`); partner logos in `src/assets/landing/partners/` |
| Hormone Focus bridge landing page | https://github.com/shuri-lab/hormon-focus-landing-jane | One responsive layout with a fluid type scale and alternating color bands (see its README) |
| Hormone Check quiz funnel | https://github.com/shuri-lab/focus-quiz-funnel and https://github.com/shuri-lab/hormon-focus-quiz-funnel-jane | Quiz-funnel structure (not used on Rickey's page) |
| JJ "first 100" pages | https://github.com/shuri-lab/jj-first-100 | Earlier JJ funnel work |
| Game Tape "Offer first seven" page | https://gametape-blue.vercel.app/offer-first-seven | The muted autoplay video reel in "Learn it from someone who actually sells." → our video carousel |
| Upsell page structure (AI Avatars) | https://www.davidhsai.com/upsell-1-product--model-videos-page | Alert bar "order confirmed", headline "You just unlocked…", offer stack with crossed values, one-time-offer line, YES/NO buttons (see `knowledge/upsell-and-bump.md`) |
| Isabelle's own Buy-Now page (in the kit) | `kit/sales-page-generator-kit/kit/4-build/example-body.html` | The 14-section structure only. Never reuse its words, images, numbers or links (the kit's checker enforces this) |
| Our finished Rickey page | https://shuri-lab.github.io/rickey-tiktokshop-project/ · repo https://github.com/shuri-lab/rickey-tiktokshop-project | The quality bar for this playbook |

**How to study a reference page** when its code isn't reachable: open it in the browser pane at 393×852 and 1440×900 and use JS to list the sections with their positions, read the computed styles of the hero, pull the CSS rules for the components you like out of the `<style>` tags, and read the `outerHTML` of the sticky bar and the offer box. That's how the JJ components were rebuilt for Rickey.

## What we borrowed from the JJ Smith page, in detail

How it was studied: the live page at 393×852, with JS that listed elements and their positions, pulled CSS from `<style>` tags with a regex per selector, found every price on the page with its y position (`/\$\d/` text nodes) to locate the stack, and read the `outerHTML` of the sticky bar and deal box. The GitHub code couldn't be reached (no `gh`, no connector, no local clone).

| JJ component | What we took | What we didn't |
|---|---|---|
| `.ly-announce` gradient alert bar (purple → magenta, 11px 800 uppercase, 5px 18px) | A thin gradient bar at the very top with the offer one-liner | Their colors. Ours runs black → `#5C0503` → `#D30805`, at a bigger size (12.5-13px) after feedback |
| Hero fits alert, logo, headline, sub, button and image on the iPhone screen | The above-the-fold rule and the measurement target | |
| `.ly-sticky` bottom bar: "Instant access · **$27** · 14-day money-back guarantee" + "Get Instant Access →" | A sticky bar after the hero, hidden at the offer, label "Instant access · $27" + the same CTA | Their guarantee text in the bar |
| "Featured in" press logos | "Brands Rickey has worked with" logo slider under the hero (and in section 3) | |
| CTA label "Get Instant Access · $27 →" and every button scrolling to the stack | One label everywhere. We copied the jump to the stack at first; since Nov 24 every button goes straight to checkout | |
| `.ly-stack` offer: item rows with values, a total ("$197+"), and `.ly-stack-deal` with badge "Today Only · Save 86%", "Normal price ~~$97~~", "Today just $27", "One-time payment · instant digital access", full-width button | Crossed values on the right, a "Total value" bar, a bordered deal box with a "You save $174" badge on its edge, "Today: just $27.", a note, the button and a trust row | "Today only" (we have no deadline) and their colors |
| Order bump (JJ: $9 vs regular $17) | A $17 add-on box after the deal (later moved out of the page) | |
| FAQ section | Planned, with the client supplying the questions later | |

Why: David liked how "clean" those components looked and the conversion structure (proof logos early, persistent CTA, one decision point). He was explicit: "what I mean by style is structure, not, of course, the branding, the colors" and "I'm not saying you have to change the whole design language."
