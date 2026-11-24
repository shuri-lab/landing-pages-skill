# Funnel stage F3 of F5: The upsell page

**Goal:** a one-click upsell page that already matches the standard David approved, with this client's offer, brand and voice.

**Read first:** `knowledge/funnel-offers.md` ("The upsell page, top to bottom"), `knowledge/upsell-and-bump.md` part D. Open `examples/rickey-headstart/funnel-pages/shots/upsell-phone-full.jpg`: that's the bar.

## Steps
1. **Build and check** (same two commands as F2). Output: `dist/<upsell slug>.html`, `preview/<upsell slug>.html`, `shots/`.
2. **Read the page as the buyer, on the phone screenshot, top to bottom.** For each part ask its question; if the answer is no, rewrite that field in the JSON:

   | Part | Question |
   |---|---|
   | Alert bar | Do I know in 2 seconds that my order worked, when I get it, and that I should stay? Two short sentences, 230 px or less on a phone (they wrap; keep the words few) |
   | First screen | Can I see the alert, the pill, the whole headline and the start of the image without scrolling? |
   | Headline | Does it name what I just bought and a result I want next? Would I say it out loud? |
   | Subheadline | What it is, how it works, what I get. Under 45 words |
   | Bridge | Is the second line a result the first product doesn't give? |
   | Bullets | Result first, then how. No feature lists, no jargon |
   | Stack | Does each item say why I want it? Is every item real? Does the total look believable next to the price? |
   | Price | Is the price the biggest thing on that screen? |
   | Proof / founder note | Is there one real thing that makes me believe it? If the client gave nothing, say so in your report: it's the page's weakest spot |
   | Questions | Are the two real doubts answered in plain words? |
   | Guarantee | The client's words, and it really covers this product |
   | YES | Does it name the product and the price? |
   | NO | Honest, not insulting, clearly a way out |

3. **Squint test** on the phone screenshot: the three things that stand out must be the alert bar, the price and the YES button. Then look for what no tool sees: one-word last lines, pills that wrap badly, a duplicated name, an emoji that fights the brand, tiny thumbnails.
4. **Read it aloud at a 5th-grade level.** Cut every word that doesn't change meaning.
5. **Write down three reasons someone would say no** (too expensive, "I already bought the course", "will I use it?") and point to the line that answers each. If one has no line, answer it in `faq` (short) or a bullet, **using only what the client told you**; if they told you nothing, ask.
6. **Long page?** On a phone the YES is far down. `jump_button` adds a small link to the offer after the bridge. Optional, not on Rickey's page; add it if the client wants it.
7. **Brand color:** "red" in our notes means *the brand's accent*. If it's light (yellow, peach, lime) the build switches to dark text and a highlighter by itself; look at every screen. If it's too soft for an alert, set `brand.alert_color`.
8. Rebuild, check, look again.

## What GoHighLevel adds (the GHL Funnel Playbook, Stage 7)
- The **YES** button is a native GHL button (it charges the saved card). The page finds it by its first word, `YES!`, and styles it.
- The **NO** link is a small Custom Code element, styled by `No thanks`.
- GHL can take about 10 seconds to render the YES button. The page keeps looking for 24 seconds.

## Done when
- [ ] Checker passes the upsell at both sizes.
- [ ] The table above is answered yes, part by part, in `my-funnel-pages/review.md`.
- [ ] Every number, value and claim has a source or the client's yes.
