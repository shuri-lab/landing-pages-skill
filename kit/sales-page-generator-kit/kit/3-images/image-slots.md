# The images the page can use (numbered slots)

Show the client this list in Step 3. Everything is optional except where noted. A missing image becomes a clearly marked placeholder (class "ph"), never an invented one.

| # | Image | Goes in section | Notes |
|---|---|---|---|
| 1 | Top mockup of the product (device frames, covers, screenshots of what's inside) | 1 Hero | Wide. Best first image on the page. |
| 2 | Same mockup, or a second one, for the close | 14 Final close | Placed right after the headline. |
| 3 | Proof image for the origin story (a result screenshot, sales, a photo) | 3 Origin story | Shown whole, centered above the story. |
| 4 | Photo of the owner | 12 Founder story | Polaroid style. One photo only: use it here, and leave section 3 without a photo. |
| 5 | One image per main component (3 to 4) | 6 What they get | Each sits in a feature card beside its text. |
| 6 | One image per bonus | 6 Bonuses | Matched to its bonus by the text in the image. |
| 7 | Illustrations for the belief and problem sections (optional) | 5, 8, 11 | A picture of the problem, of the doubts, or of the worries. |
| 8 | Customer testimonial screenshots | 9 (strongest three), 10 (the rest) | Shown whole, never edited. |
| 9 | The owner's own results (sales, revenue, payouts) | 3, 12 or 13 | Shown whole. Flag any buyer details visible. |
| 10 | Logo (optional) | Footer | |

## How to place them automatically
1. Look at every image and say what it is, reading any text in it: owner photo, product mockup, testimonial or result screenshot, bonus or component graphic, illustration, logo, background. If an image does not match the client's product or brand, do not place it: tell the client what you see and ask.
2. Place by type using the table above. Filenames are only a tie-breaker.
3. Match bonus and component graphics to their text in the copy. A graphic that matches nothing is not placed. List it as unused.
4. Give each placement a confidence: high, medium or low. Place low ones, but flag them.
5. Show a table: image number, file, what it is, section number and name, why, confidence. The client can fix any row by number ("image 5 to section 6"), and later with the "Send to section" dropdown in the editor.
6. Copy every image into `my-sales-page/images/` with a clear name. Add alt text that says what is visible.

## Rules for proof images
- Customer testimonials (comments, messages, reviews from other people) go in sections 9 and 10. The owner's own results go in section 3, 12 or 13.
- Never crop, edit, restyle or retype a screenshot. Show it whole.
- Swipe frame height: set `--ph` on the figure to the image's height divided by its width, times 100, as a percent (a 900x300 image gives `--ph:100%`, a 900x1100 image gives `--ph:122%`). Never leave a fixed value, or the box shows blank space under the screenshot.
- Image check that cannot be skipped: in Step 3, list every image with its alt text and what it shows, and wait for the client to answer keep or reject for any that do not match their product. The check script cannot see which product an image belongs to.
- If there are only 3 to 5 testimonials, put them all in section 9 and skip section 10.
- Wide screenshots (about 1000px or more) shrink to unreadable text on a phone. Put each one in a swipe frame (`.swipe-frame` around the figure, `--ph:186%` on the figure) with a "swipe to read" hint. Typed quote cards (`.tcard`) are optional and only used if the client asks.
- If a screenshot shows personal details (full or partly visible emails, phone numbers, full names of buyers), place it untouched and FLAG it so the client can re-redact before publishing.
- Testimonials show real people's names and photos. Remind the client to make sure they may use them.

## Size
Keep full-quality originals in `images/`. For the paste-ready file, the export script embeds small images and lets big ones (mockups over about 700 KB, GIFs) be hosted on the client's platform and used by link. See 5-publish/publish-guide.md.
