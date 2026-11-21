# Open items and things a teammate must collect by hand

From the Rickey build. Use it as a checklist for what a client usually has to supply, and for what the kit doesn't cover.


**1. Inputs David supplied by hand.** A teammate must collect these for a new project:
- The copy file, produced beforehand with Isabelle's AI Sales Page Tool (Buy-Now Sales Page, tasteofreedom.com) and polished against a landing-page framework.
- The hero pick: "1 + A".
- The instruction to invent anchor values, and their rough sizes.
- The decision on proof, the section 10 headline, and the founder photo choice ("rickey-photo").
- The decision to keep the logos.
- The idea for the video carousel and slider, plus the reference URL.
- Access to the project folder, with this layout:
  - `branding/` (guide PDF, logo PNGs)
  - `brands-logos/`
  - `rickey-tiktok-videos/` (mp4)
  - `rickey-tiktoks-images/` (screenshots)
  - `Rickey product check screenshots/`
  - `Rickey-TikTokShop-Deliverables/` (Offer 1 PDFs: course deck, 30-day challenge, starter product list)
  - `offer-1-image-v2.png` (hero mockup)
  - `rickey-photo.jpeg`, `rickey.jpg` (Getty)
  - `website-footer-design.png`
  - later `offer-1-page-images/` (ChatGPT images) and `rickey-bestbuy`
- Every design preference: no dashes, no "steal", hero order, more black, fonts, alert bar, pill wording, subheadline wording.
- **Still pending at the end of the slice:** the checkout link, the platform, the disclaimers, and Rickey's proof screenshots (top-1% badge, sales dashboard, first sale).

**2. Assumptions Claude made:**
- "we dont have testimonials" was taken as approval of the $230 values. Claude said so.
- The `.pss` emphasis moved to "one video a day". This was wrong.
- The en-dash number ranges were converted to "to". Disclosed.

**3. Kit gaps the playbook should fill:**
- **Media without hosting:** the kit has no answer for video. The trick only worked because the reference page revealed the videos were already on Cloudinary (`res.cloudinary.com/fje4fcoe/...`). For a new client: upload videos to a CDN that transforms by URL (Cloudinary), or convert locally with `avconvert` or ffmpeg into short, muted, 360 px loops. Always set a poster frame.
- **Components the kit lacks:** alert bar, vertical reel, horizontal video carousel, image slider, logo strip/slider, sticky side column, `.duo` screenshots, `.addon` row, footer wordmark. (Later: sticky mobile CTA, guarantee block, offer stack v2.) The exact CSS for the first set is in C2, E6 and the Appendix.
- **The kit's one-dark-band default** and the bg = paper white problem: see E6.
- **The kit's "Steal my…" subheadline formula** conflicts with clients who dislike "steal". Recommend "Get the…" or "Follow the same plan behind…" instead.
- **`check_page.py` blind spots:** button labels, placeholder hrefs, emphasis, the order of lines, and anything in `>` / `(` / `[` lines.
- **`build_page.py` ignores the brand kit's Logo field,** and its file name was wrong anyway: it says `logo-gametape-white.png`, but the real file is `logo-gametape-stacked-white.png`. Place logos by hand in `body.html`.
- **The build loads only the upright hand font.** If a brand needs an italic (Nov 19: Playfair Display Italic), add a `<link>` and a `.hand{font-style:italic}` override in `body.html`.
- **Tooling the kit assumes but a Mac lacks:** no PDF renderer, no PIL, no ffmpeg. The JXA/sips/pure-Python workarounds live only in the temporary scratchpad : now in `tools/mac/` and `tools/snippets.md`.
- **Visual QA steps aren't specified in the kit** beyond "look at desktop and phone". The helper JS and checks (Appendix 5) make QA repeatable.

**4. Environment notes:**
- The session ran in a scratch workspace (`scratch-workspaces/.../scratch-2026-11-20-c191f0`). Claude offered to move it; for a teammate, start in a durable project folder.
- The palette widget (`show_widget`) and the Browser pane (`preview_start`, `resize_window`, `javascript_tool`) are desktop-app tools. In plain Claude Code CLI, use an HTML preview file plus `open`, and Playwright or the Chrome extension for screenshots.
- Fonts (Google Fonts) and videos (Cloudinary) need internet even when the page opens from disk.
- Local time was UTC−4.

**5. Reference pages David cited:**
- `https://gametape-blue.vercel.app/offer-first-seven`: the "Learn it from someone who actually sells." section has a vertical reel of muted autoplay videos, a track animation of `40s linear infinite reelUp`, and 220×391 cards.
- `https://mycoach.jjsmithonline.com/look-younger` (#20, after this slice): a gradient alert bar, a sticky mobile CTA, a "featured in" logo slider, and the offer stack structure.

**6. Process facts not in the kit:**
- Backup naming.
- Logging decisions in the `copy.md` header comments.
- The "OVERRIDES" convention in `learned-rules.md`.
- `open` after every round.
- The `.claude/launch.json` preview server.
- A "font test" keeps v1 of the brand kit.

**7. Timing benchmark:** zip to first QA'd draft took about 35 minutes (15:38Z to 16:12Z). The 9-point feedback round took about 15 minutes. Most of the time went into image review and browser QA.

---

