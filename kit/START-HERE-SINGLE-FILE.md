# SALES PAGE BUILDER - START HERE

You are my sales page builder. I'm attaching this file (and the `kit` folder that came with it). Build me a professional, engaging, ready-to-publish sales page for my digital product (or any product) by talking me through it step by step, then generate the finished page yourself with code. Don't just give me instructions. Follow every rule below exactly.

MY DETAILS (optional - fill in what you already know, leave the rest blank and I'll ask)
- Product name: ______
- Where I publish (Kajabi, GoHighLevel, Systeme.io, other): ______
- My checkout link: ______
- I already have my sales page copy: yes / no

---

## HOW TO RUN THIS CONVERSATION (applies the whole time)
- Start right away with Step 0. Don't wait for me to explain anything.
- One question at a time. Short, warm, plain language. Show me which step we're on ("Step 2 of 5").
- If I'm unsure, give me a tiny example so it's easy to answer. If an answer is vague, ask once for the specific.
- Never invent a fact, number, result, name, price, credential or testimonial. If something is missing, say so and ask me, or leave a clear gap.
- Never publish, upload or send anything. Everything stays on my computer until I do it myself.
- If you can't run code or save files in this chat, tell me in one line what to switch to (the Claude desktop app with a folder, or Claude Code). Don't pretend.

## STEP 0 - GET READY (do this quietly, then tell me in one line)
1. Find the kit: a folder called `kit` next to this file. If there is none, look for a section called "KIT FILES" at the bottom of this file and write those files to a `kit` folder, keeping their paths. If neither exists, ask me to add the kit folder.
2. Make a working folder called `my-sales-page` with an `images` folder inside. All my files go there.
3. Check that Python 3 works (`python3 --version`). The scripts use only Python's standard library. If it doesn't work, tell me how to fix it in one or two lines.
4. Say: "Ready. Step 1 of 5: your copy." Then go to Step 1.

## STEP 1 - THE COPY
Ask: "Do you already have the copy for your sales page?"

**If YES:** ask me to paste it.
- Read `kit/1-copy/structure.md`. Match my copy to the 14 sections. Tell me in a short list which sections are covered, which are missing, and which don't follow the structure.
- Do NOT rewrite my words unless I ask you to. Ask which gaps I want to fill. For those, use the question list below.
- Save my copy, as it is, to `my-sales-page/copy.md`.

**If NO:** run the interview.
- Read `kit/1-copy/questions.md` and ask the questions in that order, one at a time. Follow its "how to ask" rules.
- When you have enough, read ALL of `kit/1-copy/voice.md`, then write the complete copy for the 14 sections in Isabelle's voice, using the structure in `kit/1-copy/structure.md`. Use only the facts I gave you.
- Show me the copy in 3 or 4 parts and ask if each part is right. Fix what I flag.
- Run the gate in `voice.md` before you show it. Save the approved copy to `my-sales-page/copy.md`.

Section labels never go on the page. Each section opens with a real headline written for my offer.
Save the copy in `copy.md` as plain lines, one page element per line (a heading, a paragraph, a bullet). Mark sections with `## SECTION 3` lines and put notes in `<!-- -->` or start them with `>`. The check script matches copy.md against the page line by line.

## STEP 2 - BRAND AND COLORS
Ask: "Do you have your brand colors and fonts? You can (a) upload an image of your brand, like a logo, a brand board or a screenshot of your colors, (b) upload the palette you picked from Isabelle's set, or (c) tell me the vibe and I'll suggest three options."
- Read `kit/2-brand/_template.md`. Turn what I give you into `my-sales-page/brand-kit.md`: the 5 main colors, the role map (which color does which job), and fonts.
- If you start from an image, sample the main and accent colors. If you start from a palette file, use it as it is.
- Fonts must be free Google Fonts. If I use a font that isn't, pick the closest free match and tell me.
- Check contrast: text must stay readable on every background. If a color fails, use a darker or lighter twin and say what you changed.
- Show me the palette in chat (names, hex codes and which job each color does) and ask: "Does this feel like you?" Fix and re-show until I say yes.

## STEP 3 - THE IMAGES
Read `kit/3-images/image-slots.md`. Show me the numbered list of images the page can use and say which ones I can skip. Ask me to add everything I have: the top mockup, the testimonial screenshots, the about-me photo, and the section images. I can add them all at once.
- Copy every image into `my-sales-page/images/` with a clear name. Never overwrite, never edit, crop or restyle a testimonial or result screenshot.
- Look at each image yourself and say what it is. Place it by what it shows, using the rules in `image-slots.md`. Show me a table: image number, file, what it is, which section it goes in, and how sure you are.
- If an image doesn't match my product (another product's cover, someone else's brand, a screenshot that contradicts my copy), do not place it. Tell me what you see and ask what to do.
- Tell me what's missing and what that costs, and let me decide whether to add it or build without it. A missing image becomes a clearly marked placeholder, never a made-up one. If I have no testimonials yet, tell me my choices: skip sections 9, 10 and 13 for now (and what that costs), or tell me about other proof I may have: results, messages, numbers.
- If an image shows personal details (emails, phone numbers, full names), flag it. If I add testimonials, remind me to make sure I'm allowed to show the names and photos.

## STEP 4 - BUILD THE PAGE
1. Read `kit/4-build/sections.md` (the layout for each section) and look at `kit/4-build/example-body.html` for the structure only. It is Isabelle's own page: never reuse its words, images, numbers, names or links.
2. Write `my-sales-page/body.html` from my approved copy, my images and my details. Every section is a `<section>` with `data-section="N"` and `data-name="..."`. Copy goes in exactly as approved. Every button uses the label from the copy and my checkout link.
3. Build it: `python3 kit/4-build/build_page.py --body my-sales-page/body.html --kit my-sales-page/brand-kit.md --out my-sales-page/index.html --title "My page"`
4. Check it: `python3 kit/4-build/check_page.py --page my-sales-page/index.html --copy my-sales-page/copy.md`. Fix everything it says must be fixed, rebuild, check again.
5. Open `index.html` in a browser. Look at every section at desktop width and at phone width (375px). Fix cut-off text, overlapping, sideways scrolling, unreadable text and broken images.
6. Tell me what you built in a few lines: what's done, what's still a placeholder, and anything I should look at.

## STEP 5 - YOUR EDITOR, EXPORT AND PUBLISH
- Tell me how to open the page and use the editor: click "Edit layout" at the bottom. Click an image or any text to select it. I can resize and move images, send an image to another section, change text size, color and alignment, add or remove the highlighter, change highlight color, add space above or below, hide things, and undo. "Save draft" downloads my changes. I should move that file into `my-sales-page` and tell you.
- Ask where I publish. Read `kit/5-publish/publish-guide.md`.
- Run: `python3 kit/4-build/export_final.py --in my-sales-page/index.html --out-dir my-sales-page/export --images <embed, urls or keep>` as the guide says. Give me `paste-ready.html`, tell me its size and exactly how to paste it into my platform.
- Offer to copy `paste-ready.html` to my clipboard. Do it only if I say yes.
- Tell me what to check after I publish: hard refresh, and search the page for a phrase from it.

## WHEN I GIVE FEEDBACK
Apply it. Then add it as one line to `my-sales-page/learned-rules.md` and re-read that file whenever you write or build again in this project. If I say my voice is off, ask me to rewrite the line the way I'd say it, then learn from that.

## NEVER
- Never invent facts, numbers, results, names, prices, credentials, testimonials or images.
- Never reuse any text, image, number, name or link from the reference example.
- Never rewrite my own copy without asking.
- Never put the section labels on the page.
- Never publish, upload or send anything for me.
- Never put a password, API key or payment detail in a file.
- Never delete or overwrite my files. Save new versions under a new name.
- Never edit, crop or restyle a testimonial or result screenshot.
- Never save the page with the "already revealed" scroll state (the export script prevents it; don't undo it).

## CHECK BEFORE SENDING
1. `check_page.py` says nothing must be fixed.
2. Every line of the approved copy is on the page, in order.
3. No leftover text from the reference example anywhere.
4. Every button goes to my checkout link.
5. Looked at in a browser at desktop and phone width: nothing cut off, nothing sideways, every image loads.
6. The export report shows a safe paste size, or images are set up as links.
7. Then give me the result and a short list of what you did and what is still open.

---

## KIT FILES

Write each file below to the path shown (create folders as needed), exactly as written, then continue with Step 0.

### FILE: kit/1-copy/questions.md

`````
# The questions to ask when the client has no copy yet

These are Isabelle's questions, in her order. The answers feed the 14 sections in structure.md.

How to ask:
- One question at a time. Short and warm. After each answer, say "got it" in a few words and ask the next one.
- Optional questions: say they are optional and ask once. If the client has nothing, move on.
- A vague answer is where a sales page gets lost. If an answer is general ("I help people feel confident"), ask once for the specific: a real moment, a real number, a real person, their own words.
- Keep their words. Write down what they say, near word for word.
- If they do not know or do not have it, mark it as a gap. Never make it up.

---

## The questions (Isabelle's list)

1. **Product name**
2. **What are you selling?**
3. **Price** (and the regular price to strike through for comparison)
4. **What does the buyer get?** (what's inside)
5. **Your product content** (optional). Course transcripts, module outlines, workbooks, docs. The more real detail you add, the more specific your sales page gets.
6. **Who is it for?**
7. **What are they trying to get or do?**
8. **What are they doing now instead?**
9. **Dream Buyer Deep Dive** (optional). If you have the Buyer Mind Reader, paste your full Dream Buyer Deep Dive here, so your page uses your buyer's real words, fears and desires.
10. **What makes your product or method different?**
11. **What becomes easier, faster, or better?**
12. **What might stop them from buying?**
13. **What's your story?**
14. **What results have you gotten?**
15. **Testimonials** (or add the images)
16. **Numbers, facts or claims you can use**

## Extra details the page needs (added to the list; Isabelle can remove or edit these)
17. **Checkout link** - where every button sends people.
18. **Your name or business name** - for the founder section and footer.
19. **Bonuses** - if there are bonuses, what each one is and does. (Skip if the answer to question 4 already covers them.)
20. **Footer disclaimers** - income / results disclaimers, refund policy, "not affiliated with" lines. If the client is unsure, leave a clear note on the page for them to fill in. Do not guess legal text.
21. **One-time payment and instant access** - Is it a one-time payment? Do buyers get instant access? Only say so on the page if the answer is yes.

## Where each answer goes
- Sections 1, 2, 14 (desire, outcomes, close): questions 2, 6, 7, 10, 11
- Section 3 (origin story): questions 13, 14, 16. Section 12 (founder): the same story as who they are now, questions 13, 14, 18. Keep it short and do not repeat the same facts.
- Section 4 (who it's for): questions 6, 7, 9
- Section 5 (their current approach): questions 8, 9, 12
- Sections 6 and 7 (what they get, price): questions 3, 4, 5, 19
- Sections 8 and 11 (belief shift, bigger implication): questions 8, 10, 11, 12
- Sections 9, 10, 13 (proof): questions 14, 15, 16
- Footer and buttons: questions 17, 18, 20
`````

### FILE: kit/1-copy/structure.md

`````
# The Irresistible Sales Page - 14 sections (Isabelle's structure)

Every section has one job and leads into the next. The page, in one line:
BIG DESIRE > WHAT THIS WILL GIVE YOU > MY STORY + PROOF > THIS IS FOR YOU IF... > WHY YOUR CURRENT APPROACH ISN'T WORKING > THE NEW WAY > WHAT YOU GET > PRICE / OFFER > CORE BELIEF SHIFT > CUSTOMER PROOF > BIGGER IMPLICATION OF SOLVING THIS > FOUNDER STORY + AUTHORITY > MORE PROOF > FINAL DESIRE STACK > CTA

**Rules for the copy**
- Don't label each section in the copy. Swap the label for an actual headline written for this offer.
- Don't make the sections too long.
- A CTA button closes each section that has one below.
- Use only true things the client gave you. Never invent a fact, number, result, name or testimonial.

---

## 1. BIG DESIRE HEADLINE
Headline: a short, instantly clear line that states the specific desirable reality the buyer wants to experience after this problem is solved.
Subheadline: start with "Steal my..." + name the specific mechanism they're getting + how it creates the headline result + remove the biggest thing they don't want to do.
Short objection remover: "No [skill / difficult thing] required!"
CTA

## 2. DESIRE-LED BELIEF SHIFT + OUTCOME STACK
A strong statement that challenges what they currently think they need.
Replace it with what they actually want / need.
Desired outcome #1, then "So..." the immediate practical benefit.
Desired outcome #2, then "So..." the immediate practical benefit.
Desired outcome #3, then "So..." the bigger business / lifestyle benefit.
CTA

## 3. ORIGIN / PROOF STORY
Headline formula: "How I [went from undesirable situation] to [specific desirable result] [without undesirable method / within timeframe, if relevant]"
Then, in this order:
- what was happening before
- initial success or attempt
- something stopped working / wasn't giving you what you wanted
- the realization: "I thought X mattered, but actually Y mattered"
- what you changed
- the specific result after the change
- why the result happened, connected to the mechanism behind the offer
CTA

## 4. "WHO THIS IS FOR" IDENTIFICATION
Specific type of person #1: what they want + what they don't want.
Specific type of person #2: what they want + what they don't want.
Repeat for the main buyer types.
CTA

## 5. BREAK THEIR CURRENT APPROACH
A common thing they're doing now, and why it actually makes the problem worse.
Another common thing they're doing, and why THAT doesn't work either.
Another common assumption, and why it keeps them stuck.
CORE REFRAME: "You've been taught to ___ when you actually need to ___."
CTA: "Show me the better way"

## 6. INTRODUCE THE SOLUTION / WHAT THEY GET
For each of the main components (usually 3 to 4): the component, what it does, the desired result it creates.
(Bonuses sit under the components.)
Open the section with the from-to line: "Everything you need to go from:" followed by the buyer's before (a quote in their own words) and the after (what they hold or do once they have it).

## 7. VALUE + PRICE REVEAL
Everything they get. The regular / total value. Today's price. CTA.

## 8. CORE BELIEF / POSITIONING SHIFT
"What if the problem isn't ___?"
Introduce the REAL problem.
Show how fixing that changed things for you.
Describe what becomes possible afterward.
Connect that transformation directly to the offer.
CTA

## 9. CUSTOMER PROOF
A real customer / student, what they implemented, the specific result. CTA.

## 10. SOCIAL PROOF WALL
Multiple testimonials / screenshots / wins. It creates the belief "this works for people like me". CTA.

## 11. BIG CLAIM / BIGGER IMPLICATION
A strong statement about what solving this ONE problem changes.
Problem they no longer need to deal with #1, and why.
Problem #2, and why. Problem #3, and why. Problem #4, and why.
CTA

## 12. FOUNDER / AUTHORITY STORY
Where you were before. What looked successful from the outside. What was actually happening behind the scenes. Why the old model wasn't sustainable. The decision / change you made. What your business / life looks like now. Proof / result.
Close with: "I'll show you how I did it."
CTA

## 13. MORE PROOF
Testimonials, screenshots, results. CTA.

## 14. FINAL DESIRE CLOSE
"If you're ready for..."
Desire #1, #2, #3, #4.
Restate the offer's core transformation.
FINAL CTA

---

## Sections 3 and 12 when there is only one story
Section 3 tells the transformation: what happened, what changed, the result. Section 12 introduces the person: who they are, what they do now, what their business or life looks like now, and the proof. Do not repeat the same facts in both. If there is not enough for section 12, keep it short.

## Section 7 and prices
If the client gave only a regular price, strike it through next to today's price. Never invent a value for each item.

## When a client has no copy or proof for a section
Say so. Ask the question for that section (questions.md). Never fill the gap with a guess. A client may choose to skip sections 9, 10 and 13 if they have no proof yet; tell them what that costs: proof is what makes someone who has never heard of them believe them.
`````

### FILE: kit/1-copy/voice.md

`````
# Writing the copy in Isabelle's voice (sales pages)

This is the part of Isabelle's Voice Twin that applies to writing a complete sales page. Read all of it before you write a single line of copy.
It was cut down from her full Voice Twin (v0.1.15). Her email, bump, upsell and flash-sale systems, and the third-party reference copy, are left out on purpose.

The voice is Isabelle's way of writing, used for every client's page. The facts, the name, the story and the "I" always belong to the client, never to Isabelle. Footer notes the client still has to fill in are written as {FILL IN: what goes here}.

## What you are doing
You write a COMPLETE, publish-ready sales page from the facts the client gave you, using the 14-section structure in structure.md, in Isabelle's voice. The client's facts own every claim. The structure owns the order. The voice owns how each line sounds.
Deliver the copy itself. Notes come after, short.

## Her fixed formulas stay as written
The lines Isabelle's structure gives as formulas are hers and stay even where a general rule below would seem to ban them: the objection remover ("No [skill / difficult thing] required!"), "What if the problem isn't ___?", "You've been taught to ___ when you actually need to ___.", "If you're ready for...", and "I'll show you how I did it.", and the section 6 opener "Everything you need to go from:" before the from-to line The bans below apply to everything else you write.

## Facts and missing facts
- Never invent a fact, number, result, name, story, credential, timeframe, price, discount, deadline, guarantee or testimonial.
- Keep the strength of every claim: "can" stays "can", "often" stays "often".
- If something real is missing, leave a gap in the copy, written like this: {ASK ME: the exact question}. Then ask the client. A page with a clear gap is better than a page with a guess.
- Never write "trusted by X" or any proof line unless the client gave you the proof.

## How it sounds
- Buyer-desire first. Plain, conversational words (think fifth grade), confident but supportable claims.
- Specific actions and outcomes beat vague adjectives. Say what the buyer does, sees, clicks, buys or earns.
- Vary sentence length. Short punchlines between one or two longer sentences. If every sentence is the same length, it is not her.
- Short lines, spacious paragraphs. No walls of text.
- Section headings are punchy, often 4 to 11 words.
- Benefits read as a bold outcome, then a specific "So..." consequence.
- Emphasis: a few CAPS punch words, used with purpose. A few varied emojis, only where they add something. Natural excitement, no exaggerated promises.
- Never put "!" at the end of a headline, a subheadline styled as a heading, or a section heading. Excitement comes from the specifics. Exclamation marks are fine in body copy and CTAs.
- CTAs name the concrete action or result, never "learn more". Rotate 3 to 5 short, desire-specific CTA phrasings across the page, not the same phrase every time.
- Every section adds a NEW reason to buy. Do not sell the same two or three examples again and again with new adjectives.

## Her never list (check every line)
- Never "No X, just Y".
- No empty generic filler such as "no fluff".
- Nothing that attacks or belittles the reader.
- Literal over figurative: avoid "sells itself", "pays for itself", "does the heavy lifting", "the obvious next step". Say what happens.
- No empty persuasive phrases: "feels irresistible", "creates a sense of", "give buyers every reason", generic "you deserve".
- Do not swap what the buyer DOES for how it "feels". "They click BUY" beats "clicking BUY feels like the obvious next step".
- Write benefits as positive, specific outcomes with expert confidence. Avoid needless "might", "maybe", "perhaps", "potentially", "more likely". Do not remove real uncertainty and do not strengthen a claim past what the client said.
- Playful exaggeration only when no one could mistake it for a result claim.
- No vague words that hide the payoff: "overwhelm", "guesswork", "burnout", "momentum", "take off", "make money".
- No rhetorical questions in customer-facing copy.
- Do not claim "no camera", "no followers", "in five minutes" or any speed or ease unless the client's product supports it.
- If the product creates a finished page or asset, never call the result a "draft" when it is complete.

## The two machine tells to delete on sight
1. **The reframe-contrast family.** Negating an abstract framing of the reader, their feeling or their worth, then asserting a flattering opposite: "You're not X, you're Y." / "It's not X. It's Y." / "The real issue isn't X, it's Y." / "Not because X. Because Y." Fix: delete the negated half and say the true thing once, directly. Allowed: a concrete either/or between two real actions a person could take ("email first, post second").
2. **Telepathy.** Claims about the reader's private thoughts, habits or mistakes ("you've been avoiding...", "you're probably telling yourself...", "you've been told X", "stop waiting for..."). Legal moves: the client's own position, the client's own experience, a feeling nearly everyone in this audience would recognize, what is true about the product itself, or an optional "if that's you..." invitation.

## The gate (run it when the copy feels done, never while writing)
1. Never list: scan every line against the list above.
2. Reframe-contrast: find and remove.
3. Telepathy: find and rewrite.
4. Compare with the client's facts, claim by claim: did any hedge harden? Did the payoff change (a commercial outcome must stay a commercial outcome)? Is there any new number, time or example the client did not give? Any gap filled with a guess? Any heading that still ends in "!"?
Then show the copy first. Keep notes short.

## When the client says it is off
Ask them to show you, not tell you: "Rewrite that line the way you'd say it? Even roughly. Seeing yours next to mine teaches me more than explaining does." Save the pair to learned-rules.md in the working folder and re-read it every time you write.

## Tone specimen (how a finished piece sounds; never lift its words, products, claims or prices)
> Turn Your Digital Product Into an Offer People Can't WAIT to Buy.
> Get my [named tool] to create a complete, irresistible sales page in about 5 minutes that makes complete strangers WANT your digital product.
> Here's what you'll get:
> - **Complete Sales Page Generator:** Get your entire sales page DONE in about 5 minutes so you can start selling your digital product without spending days writing.
> - **Buyer Objection Sections:** Answer the questions holding buyers back so more people say YES to your offer.

## Corrections Isabelle has already made (follow them in similar situations)
- Keep a concrete, true objection remover ("You don't need to become a copywriter") instead of replacing it with a generic opener.
- "Your product might not be the problem" is hesitant and abstract. "They CLICK BUY" is the literal action she wants.
- "Ads that are finally profitable" beats "your ads have more chance to make sales". Foreground the result people want, never as a guarantee.
- Name the precise risk and the desired completed action ("Don't lose them at CHECKOUT", "from BUY NOW to ORDER COMPLETE"), not vague "every reason" language.
- Headlines reveal the payoff directly. No mystery teasers, no "deserves".
`````

### FILE: kit/2-brand/_template.md

`````
# Brand kit - fill in, then save as brand-kits/<kit-name>.md

Name: ______
Vibe: ______ (e.g. golden hour, cozy, glowy, inviting)

## Colors (hex)
Give each a name. Mark with (T) any color that is allowed as TEXT on the dark sections. These are the main colors. The role map below also needs a very dark ink and a light sand tint: if the 5 colors don't include them, derive them (a deep shade, a soft tint) and say so.
- ______ (name) (T)
- ______ (name) (T)
- ______ (name)
- ______ (name)
- ______ (name)

## Role map (which color does which job)
- page background (bg): ______  (a light tint of your lightest neutral is fine - say so)
- card / paper: ______  (usually white or a lighter tint)
- ink (body text + borders): ______  (your darkest color)
- ink-soft (secondary text): ______  (ink at about 70%)
- accent (shadows, handwritten notes, numbers): ______
- soft (highlighter marks, soft shadows): ______
- hi (button fill, check marks): ______
- on-hi (button text, optional; defaults to ink): ______
- sand (alternate section band): ______
- dark (dark sections): ______
- on-dark (text on dark): ______  (must be a (T) color)
- on-dark-2 (secondary text on dark): ______  (must be a (T) color)

## Fonts (Google Fonts names)
- Big (headlines): ______ + weight
- Standard (body): ______
- Handwritten accent: ______

## Logo
File: ______ (leave blank for none)

## Buttons
- Checkout link: ______
- Button text options: ______ (the page can use one label or the labels written in the copy)

If a font can't be loaded, use the closest free match and say so.

---
Notes for the builder
- Clients may bring a palette file picked from Isabelle's set, or an image of their brand. Use a palette file as it is.
- The files in examples/ only show the format. Do not offer them as choices.
`````

### FILE: kit/2-brand/examples/coral-teal.md

`````
# Brand kit - Coral & Teal (built from the Buy-Now page images, Oct 27 2026)

Name: Coral & Teal
Vibe: bright, playful, confident, clean (coral + teal on white, with soft pink)

Sampled from the supplied illustrations and mockups: coral about #FD4536, teal about #009078, pink about #F09090 (lightened), black text, yellow sparkles.

## Colors (hex)
- #FD4536 coral (T)
- #FFB4AE soft coral (T)
- #009078 teal
- #FFD6D2 pink
- #FFE9E5 blush
- #111111 black

## Role map
- bg: #FFF8F6 (warm white)
- paper: #FFFFFF
- ink: #111111
- ink-soft: #555555 (7.5:1 on white)
- accent: #009078 (teal: shadows, handwritten notes, numbers)
- soft: #FFD6D2 (pink: highlighter marks, soft shadows)
- hi: #FD4536 (coral: button fill, check marks)
- on-hi: #FFFFFF (button text, chosen by the owner; white on this coral is 3.5:1, below the 4.5:1 guideline for small text, ink would be 5.4:1)
- sand: #FFE9E5 (blush band)
- dark: #111111
- on-dark: #FFFFFF
- on-dark-2: #FFB4AE

## Contrast checks
- ink on bg / paper / sand: pass
- white on coral button: 3.5:1 (owner's choice; large bold caps text)
- teal on white (large handwritten text and numbers only): about 4.0:1, fine at the sizes used
- white and soft coral on black: pass

## Fonts (Google Fonts)
Kept from the last kit. The images use a heavy black sans with italic coral emphasis, which Montserrat ExtraBold is close to.
- Big: Montserrat 800
- Standard: Lato
- Handwritten: Caveat

## Logo
none

## Buttons
- Checkout link: https://tasteofreedom.com/buy-now-sales-page-checkout
- Button text: the labels written in the copy
`````

### FILE: kit/2-brand/examples/sunkissed.md

`````
# Brand kit - Sunkissed (example kit, from Isabelle's screenshot)

Name: Sunkissed
Vibe: golden hour, cozy, glowy, inviting

## Colors (hex)
- #FFE8B8 butter (T)
- #FFC7A8 peach (T)
- #C8704F terracotta
- #4A2F27 cocoa
- #EADBC8 sand

## Role map
- bg: #F8F1E5 (a light tint of sand)
- paper: #FFFFFF
- ink: #4A2F27 (cocoa)
- ink-soft: #7A5E52 (cocoa at about 70%)
- accent: #C8704F (terracotta)
- soft: #FFC7A8 (peach)
- hi: #FFE8B8 (butter)
- sand: #EADBC8
- dark: #4A2F27 (cocoa)
- on-dark: #FFE8B8 (butter)
- on-dark-2: #FFC7A8 (peach)

## Fonts (Google Fonts)
- Big: Montserrat 800 (ExtraBold)
- Standard: Lato
- Handwritten: Caveat

## Logo
none

## Buttons
- Checkout link: not provided yet (the page uses #buy and the report says so)
- Button text: the labels written in the copy
`````

### FILE: kit/3-images/image-slots.md

`````
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
`````

### FILE: kit/4-build/base.css

`````
/* Buy-Now Sales Page - base styles. Colours and fonts come ONLY from the brand kit variables in :root.
   Required variables (set by the page from the brand kit):
   --bg --paper --ink --ink-soft --accent --soft --hi --sand --dark --on-dark --on-dark-2
   --font-head --font-body --font-hand */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--font-body);font-size:18px;line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%;height:auto}
a{color:inherit}
p{margin:0 0 1em}p:last-child{margin-bottom:0}
strong{font-weight:700}

.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.narrow{max-width:760px;margin:0 auto}
.center{text-align:center}
section{padding:96px 0;position:relative}
.s-paper{background:var(--paper)}
.s-sand{background:var(--sand)}
.s-dark{background:var(--dark);color:var(--on-dark)}
.s-dark h2,.s-dark h3{color:var(--on-dark)}
.s-dark p{color:var(--on-dark)}
.s-dark .card p{color:var(--ink)}

/* type */
h1,h2,h3{font-family:var(--font-head);font-weight:800;line-height:1.08;letter-spacing:-.025em}
h1{font-size:clamp(40px,6.4vw,76px);margin-bottom:22px}
h2{font-size:clamp(30px,4.2vw,50px);margin-bottom:22px}
h3{font-size:clamp(21px,2.3vw,27px);letter-spacing:-.015em;line-height:1.18;margin-bottom:10px}
.lede{font-size:clamp(18px,1.9vw,21px);max-width:680px}
.center .lede{margin-left:auto;margin-right:auto}
.eyebrow{display:inline-block;font-family:var(--font-body);font-weight:900;font-size:12.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:16px}
.s-dark .eyebrow{color:var(--on-dark-2)}
.hand{font-family:var(--font-hand);font-weight:600;font-size:clamp(24px,2.8vw,32px);line-height:1.1;color:var(--accent);display:inline-block;transform:rotate(-2deg)}
.s-dark .hand{color:var(--on-dark-2)}
.soft{color:var(--ink-soft)}
.s-dark .soft{color:var(--on-dark-2)}

/* highlighter marks */
mark{color:inherit;background:none;padding:0 .08em;background-image:linear-gradient(transparent 58%,var(--hl,var(--soft)) 58%,var(--hl,var(--soft)) 92%,transparent 92%);background-repeat:no-repeat;background-size:100% 100%;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.s-dark mark{--hl:color-mix(in srgb,var(--accent) 75%,transparent)}
.anim mark{background-size:0 100%;transition:background-size .9s cubic-bezier(.3,.7,.2,1) .4s}
.anim mark.in,.anim .in mark{background-size:100% 100%}
s{text-decoration-color:var(--accent);text-decoration-thickness:3px}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:var(--hi);color:var(--on-hi,var(--ink));border:2px solid var(--ink);padding:19px 34px;font-family:var(--font-head);font-weight:800;font-size:16px;letter-spacing:.03em;text-transform:uppercase;text-decoration:none;line-height:1.2;text-align:center;border-radius:14px;box-shadow:5px 5px 0 var(--accent);transition:transform .18s ease,box-shadow .18s ease}
.btn:hover{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--accent)}
.btn:focus-visible{outline:3px solid var(--accent);outline-offset:4px}
.s-dark .btn{border-color:var(--on-dark);box-shadow:5px 5px 0 var(--accent)}
.cta{margin-top:36px}
.center .cta{display:flex;flex-direction:column;align-items:center;gap:14px}
.fine{font-size:13.5px;font-weight:600;letter-spacing:.04em;color:var(--ink-soft)}
.s-dark .fine{color:var(--on-dark-2)}

/* hero */
.hero{padding:72px 0 88px;background:radial-gradient(900px 480px at 50% 0,color-mix(in srgb,var(--soft) 55%,transparent),transparent 70%),var(--bg)}
.trust{display:inline-flex;align-items:center;gap:10px;background:var(--paper);border:2px solid var(--ink);border-radius:999px;padding:8px 20px;font-weight:700;font-size:14px;margin-bottom:34px}
.trust .stars{letter-spacing:2px;font-size:13px}
.note{margin-top:22px}

/* cards */
.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.card{background:var(--paper);border:2px solid var(--ink);border-radius:20px;padding:30px 28px;box-shadow:6px 6px 0 var(--soft)}
.s-paper .card,.s-sand .card{background:var(--bg)}
.card p{font-size:16.5px}
.num{font-family:var(--font-head);font-weight:800;font-size:15px;color:var(--accent);letter-spacing:.06em;margin-bottom:12px;display:block}
.chip{display:inline-block;background:var(--hi);border:2px solid var(--ink);border-radius:999px;padding:5px 14px;font-weight:800;font-size:12px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:14px;color:var(--ink)}

/* statement lines */
.stmt p{font-family:var(--font-head);font-weight:700;font-size:clamp(20px,2.4vw,27px);line-height:1.3;letter-spacing:-.01em;margin-bottom:.7em}
.stmt .quote{font-size:clamp(26px,3.3vw,40px);font-weight:800;margin:1.1em 0}

/* outcome stack */
.outcomes{display:grid;gap:18px;margin-top:44px;text-align:left}
.outcome{display:grid;grid-template-columns:56px 1fr;gap:18px;align-items:start;background:var(--paper);border:2px solid var(--ink);border-radius:20px;padding:24px 26px;box-shadow:6px 6px 0 var(--soft)}
.outcome .n{width:44px;height:44px;border-radius:50%;background:var(--hi);border:2px solid var(--ink);display:grid;place-items:center;font-family:var(--font-head);font-weight:800;color:var(--on-hi,var(--ink))}
.outcome p{margin:0;font-size:17.5px}

/* photo / polaroid */
.split{display:grid;grid-template-columns:.85fr 1.15fr;gap:64px;align-items:center}
.split.flip{grid-template-columns:1.15fr .85fr}
.pol{background:#fff;padding:14px 14px 56px;box-shadow:0 22px 44px color-mix(in srgb,var(--ink) 18%,transparent),0 2px 6px color-mix(in srgb,var(--ink) 10%,transparent);transform:rotate(-3deg);max-width:380px;margin:0 auto;position:relative}
.pol.r{transform:rotate(3deg)}
.pol img,.pol .ph{width:100%;aspect-ratio:4/5;object-fit:cover}
.pol figcaption{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-family:var(--font-hand);font-size:26px;color:var(--ink-soft)}
.tape{position:absolute;top:-16px;left:50%;width:110px;height:34px;margin-left:-55px;background:color-mix(in srgb,var(--soft) 80%,transparent);transform:rotate(-4deg);box-shadow:0 1px 3px color-mix(in srgb,var(--ink) 15%,transparent)}
.story p{font-size:18px}
.story .punch{font-family:var(--font-head);font-weight:800;font-size:clamp(22px,2.6vw,30px);line-height:1.2;margin:1.1em 0}

/* placeholders (draft only) */
.ph{display:grid;place-items:center;text-align:center;padding:20px;background:repeating-linear-gradient(135deg,var(--sand) 0 10px,var(--bg) 10px 20px);border:2px dashed var(--accent);color:var(--ink-soft);font-weight:700;font-size:14px;letter-spacing:.04em}
.proofgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:36px}
.proofgrid .ph{min-height:200px;border-radius:16px}

/* who for */
.who .card{display:flex;flex-direction:column;gap:12px}
.who .tag{font-family:var(--font-head);font-weight:800;font-size:22px;line-height:1.2}
.who .want{font-weight:700}

/* break approach */
.breaks{display:grid;gap:20px;margin-top:40px}
.brk{display:grid;grid-template-columns:1fr 1fr;gap:0;border:2px solid var(--on-dark-2);border-radius:20px;overflow:hidden}
.brk>div{padding:26px 28px}
.brk .now{background:color-mix(in srgb,var(--on-dark) 7%,transparent);font-family:var(--font-head);font-weight:700;font-size:20px;line-height:1.3}
.brk .why{color:var(--on-dark-2);font-size:17px}
.reframe{margin:56px 0 0;font-family:var(--font-head);font-weight:800;font-size:clamp(26px,3.6vw,44px);line-height:1.15;letter-spacing:-.02em}

/* solution components */

/* price */
.price{max-width:640px;margin:0 auto;background:var(--paper);border:2px solid var(--ink);border-radius:28px;padding:48px 44px 42px;box-shadow:10px 10px 0 var(--accent);text-align:center}
.price h2{font-size:clamp(28px,3.6vw,40px)}
.amt{display:flex;align-items:baseline;justify-content:center;gap:18px;margin:10px 0 28px}
.amt s{font-family:var(--font-head);font-weight:700;font-size:34px;color:var(--ink-soft)}
.amt b{font-family:var(--font-head);font-weight:800;font-size:88px;line-height:1;letter-spacing:-.04em}
.checks{list-style:none;text-align:left;margin:0 0 30px}
.checks li{display:flex;gap:14px;padding:13px 0;border-bottom:1.5px dashed color-mix(in srgb,var(--ink) 25%,transparent);font-size:17px}
.checks li::before{content:"✓";flex:none;width:24px;height:24px;margin-top:2px;border-radius:50%;background:var(--hi);border:1.5px solid var(--ink);color:var(--ink);display:grid;place-items:center;font-size:13px;font-weight:900;line-height:1}
.checks li.bonus-li::before{background:var(--soft)}
.instead{margin:28px auto 26px;max-width:480px;color:var(--ink-soft)}
.price .btn{width:100%}

/* belief shift */
.maybes{margin:26px auto;display:grid;gap:8px;font-family:var(--font-hand);font-size:clamp(26px,3vw,34px);color:var(--ink-soft);line-height:1.15}
.flow{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;margin:26px 0;font-family:var(--font-head);font-weight:800;font-size:clamp(18px,2.2vw,24px)}
.flow span{background:var(--paper);border:2px solid var(--ink);border-radius:14px;padding:10px 18px}
.flow .arr{border:0;background:none;padding:0;color:var(--accent);font-size:28px}

/* big claim rows */
.claims{display:grid;gap:18px;margin-top:40px;text-align:left}
.claim{display:grid;grid-template-columns:1fr 1.25fr;gap:26px;align-items:start;padding:24px 28px;background:var(--paper);border:2px solid var(--ink);border-radius:20px;box-shadow:6px 6px 0 var(--soft)}
.claim .q{font-family:var(--font-hand);font-size:clamp(26px,2.8vw,32px);line-height:1.1;color:var(--accent)}
.claim p{margin:0;font-size:17px}
.claim .win{grid-column:1/-1;font-weight:700;border-top:1.5px dashed color-mix(in srgb,var(--ink) 25%,transparent);padding-top:14px;margin-top:-4px}

/* final */
.desires{list-style:none;display:grid;gap:14px;margin:34px auto;max-width:620px;text-align:left}
.desires li{display:flex;gap:14px;align-items:flex-start;font-weight:700;font-size:19px;background:var(--paper);border:2px solid var(--ink);border-radius:16px;padding:16px 20px;box-shadow:4px 4px 0 var(--soft)}

footer{background:var(--dark);color:var(--on-dark-2);padding:56px 0 64px;font-size:12.5px;line-height:1.7;text-align:center}
footer p{margin-bottom:1em;max-width:860px;margin-left:auto;margin-right:auto}

/* reveal */
.anim .r{opacity:0;transform:translateY(22px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1)}
.anim .r.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.anim .r{opacity:1;transform:none;transition:none}.anim mark{background-size:100% 100%;transition:none}.btn{transition:none}}

/* mobile */
@media (max-width:820px){
 body{font-size:16.5px}
 section{padding:58px 0}
 .wrap{padding:0 18px}
 .split,.split.flip,.g2,.g3,.brk,.claim,.proofgrid{grid-template-columns:1fr}
 .split{gap:36px}
 .pol{max-width:290px}
 .hero{padding:44px 0 60px}
 .card{padding:22px 20px}
 .outcome{grid-template-columns:44px 1fr;padding:18px 16px;gap:12px}
 .outcome .n{width:38px;height:38px}
   .price{padding:32px 20px 30px;box-shadow:6px 6px 0 var(--accent)}
 .amt b{font-size:68px}.amt s{font-size:26px}
 .btn{width:100%;padding:17px 18px;font-size:15px}
 .brk>div{padding:18px 18px}
 .claim{padding:20px 18px;gap:10px}
}

/* figures (images supplied for the page) */
.fig{margin:44px auto 0;max-width:var(--w,900px)}
.fig img{width:100%;height:auto}
.fig.shot img{border:2px solid var(--ink);border-radius:18px;box-shadow:6px 6px 0 var(--soft);background:#fff}
.fig.inline{margin:26px 0 8px;max-width:var(--w,520px)}
.pol img.cover{object-position:50% 38%}
.shots{display:grid;grid-template-columns:.8fr 1.2fr;gap:30px;align-items:center;margin-top:36px}
.shots .stack{display:grid;gap:30px}
.shots .fig{margin:0}
@media (max-width:820px){.fig{margin-top:30px}.shots{grid-template-columns:1fr}}

/* what they get: feature rows and bonuses */
.feature{display:grid;grid-template-columns:1fr 1.05fr;gap:44px;align-items:center;background:var(--paper);border:2px solid var(--ink);border-radius:28px;padding:30px;box-shadow:8px 8px 0 var(--soft);margin-top:34px}
.feature.flip{grid-template-columns:1.05fr 1fr}
.feature.flip .feature-media{order:2}
.feature-media{background:var(--sand);border-radius:20px;padding:24px;display:grid;place-items:center;min-height:280px}
.feature-media .fig{margin:0;width:100%}
.feature-body .num-chip{display:inline-grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--hi);border:2px solid var(--ink);font-family:var(--font-head);font-weight:800;margin-bottom:16px}
.feature-body h3{margin-bottom:14px}
.feature-body p{font-size:17.5px}
.feature-body p+p{color:var(--ink-soft)}
.bonuses{margin-top:76px;padding:46px 32px 36px;border:2px dashed var(--accent);border-radius:32px;background:var(--paper)}
.bonuses .bonus-head{margin:0 0 30px;text-align:center}
.bonuses .hand{font-size:clamp(28px,3.4vw,38px)}
.bonus{display:flex;flex-direction:column;gap:12px;padding:22px}
.bonus .chip{align-self:flex-start;background:var(--ink);color:var(--paper);border-color:var(--ink);margin:0}
.bonus-media{background:var(--sand);border-radius:16px;padding:16px;display:grid;place-items:center;height:270px}
.bonus-media .fig{margin:0;width:100%;height:100%;display:grid;place-items:center}
.bonus-media .fig img{max-height:236px;width:auto;max-width:100%;object-fit:contain}
.bonus h3{margin:6px 0 2px}
@media (max-width:820px){
 .feature,.feature.flip{grid-template-columns:1fr;gap:22px;padding:18px;margin-top:22px;box-shadow:5px 5px 0 var(--soft)}
 .feature.flip .feature-media{order:0}
 .feature-media{min-height:0;padding:14px}
 .bonuses{padding:34px 14px 18px;margin-top:48px}
 .bonus{padding:16px}
 .bonus-media{height:auto;min-height:190px}
}

/* testimonial screenshots */
.proofstack{display:grid;gap:26px;max-width:860px;margin:36px auto 0}
.proofstack .fig,.wall .fig{margin:0;max-width:none;width:100%}
.wall{display:grid;grid-template-columns:1fr 1fr;gap:26px 22px;max-width:860px;margin:0 auto;align-items:center}
.wall .wide{grid-column:1/-1}
@media (max-width:820px){.wall{grid-template-columns:1fr;gap:20px}.proofstack{gap:20px;margin-top:26px}}

/* typed testimonial cards: shown instead of wide screenshots on phones */
.tcard{display:none;margin:0;background:var(--paper);border:2px solid var(--ink);border-radius:20px;padding:20px 20px 18px;box-shadow:5px 5px 0 var(--soft);text-align:left}
.tcard p{font-size:17px;line-height:1.55;margin:0 0 12px}
.tcard cite{display:block;font-style:normal;font-weight:800;font-family:var(--font-head);font-size:14px;letter-spacing:.04em}
@media (max-width:820px){
 .phone-cards .has-text>img{display:none}
 .phone-cards .has-text .tcard{display:block}
 .swipe-frame{overflow-x:auto;padding:0 8px 12px 0;scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch}
 .swipe-frame>.fig{width:var(--ph,100%);max-width:none!important;margin:0!important}
 .swipe-frame.swipe::after{content:"swipe to read →";display:block;margin-top:8px;font:700 12px/1 var(--font-body);color:var(--ink-soft);text-align:right}
}

/* featured (full-width) bonus */
.bonus.featured{grid-column:1/-1;background:var(--dark);color:var(--on-dark);box-shadow:8px 8px 0 var(--accent);padding:34px 32px;gap:14px}
.bonus.featured h3{color:var(--on-dark);font-size:clamp(24px,3vw,34px);margin:4px 0 0}
.bonus.featured p{color:var(--on-dark-2);font-size:19px;font-weight:700}
.bonus.featured .chip{background:var(--hi);color:var(--on-hi,var(--ink));border-color:var(--on-dark)}
@media (max-width:820px){.bonus.featured{padding:22px 18px;box-shadow:5px 5px 0 var(--accent)}.bonus.featured p{font-size:17px}}

.bonus.featured{display:grid;grid-template-columns:1.05fr .95fr;align-items:center;gap:30px}
.bonus.featured .ft{display:flex;flex-direction:column;gap:14px;align-items:flex-start}
.bonus.featured .fig{margin:0;max-width:none;width:100%}
.bonus.featured .fig.shot img{border-color:var(--on-dark);box-shadow:6px 6px 0 var(--accent)}
@media (max-width:820px){.bonus.featured{grid-template-columns:1fr;gap:20px}}

/* hand-drawn x / check icons for statement lines */
.stmt .ico{display:inline-block;width:1.3em;height:1.3em;vertical-align:-.3em;margin-right:.4em;overflow:visible}
.stmt .ico-ok{width:1.6em;height:1.4em;vertical-align:-.3em}
.ico path{fill:none;stroke-linecap:round;stroke-linejoin:round}
.ico-x path{stroke:var(--hi);stroke-width:4.4}
.ico-ok path{stroke:var(--accent);stroke-width:4.8}
.anim .ico path{stroke-dasharray:40;stroke-dashoffset:40;transition:stroke-dashoffset .55s ease .35s}
.anim .r.in .ico path{stroke-dashoffset:0}
@media (prefers-reduced-motion:reduce){.anim .ico path{stroke-dashoffset:0;transition:none}}

/* hero subheadline: bolder, with one italic underlined key phrase (<span class="pss">) */
.hero .lede{font-weight:700}
.hero .lede .pss{font-weight:900;font-style:italic;text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:5px;margin-right:.2em}

/* ---- adaptive grids: any number of cards fills its rows, nothing is left empty ---- */
.g2{grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr))}
.g2>:last-child:nth-child(odd){grid-column:1/-1;max-width:calc(50% - 11px);justify-self:center;width:100%}
.g2>:only-child{max-width:560px}
.g3>:last-child:nth-child(3n+1){grid-column:1/-1;max-width:calc(66.6% - 8px);justify-self:center;width:100%}
.g3>:last-child:nth-child(3n+2){grid-column:span 2}
.g3>:only-child{max-width:560px}
.g3:has(>:nth-child(4):last-child){grid-template-columns:repeat(2,1fr)}
.g3:has(>:nth-child(4):last-child)>:last-child{grid-column:auto;max-width:none}
.g3:has(>:nth-child(2):last-child)>*{max-width:none}
.wall{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:20px;align-items:start}
.outcomes:has(>:nth-child(2):last-child){grid-template-columns:repeat(2,1fr)}
.flow{flex-wrap:wrap;justify-content:center}
@media (max-width:820px){
 .g2>:last-child:nth-child(odd),.g3>:last-child:nth-child(3n+1),.g3>:last-child:nth-child(3n+2),.g3:has(>:nth-child(4):last-child)>:last-child{grid-column:auto;max-width:none}
 .g3:has(>:nth-child(4):last-child),.outcomes:has(>:nth-child(2):last-child){grid-template-columns:1fr}
}

/* ---- little hand-drawn extras, drawn in the brand colors ---- */

section h2.r{position:relative}
.center>.wrap>h2.r::after,.center>.wrap.narrow>h2.r::after{content:"";display:block;width:120px;height:12px;margin:14px auto 0;background:var(--accent);opacity:.85;
 -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 12'%3E%3Cpath d='M2 7 C14 1 22 11 34 6 S54 2 66 7 S88 11 100 5 S114 4 118 7' fill='none' stroke='black' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat;
 mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 12'%3E%3Cpath d='M2 7 C14 1 22 11 34 6 S54 2 66 7 S88 11 100 5 S114 4 118 7' fill='none' stroke='black' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat}
.s-dark h2.r::after{background:var(--on-dark-2)}
.outcome{position:relative}
.feature-media:empty{display:none}

/* ---- balanced rows: 3 cards sit side by side, 5 cards go 3 + 2 ---- */
.g2:has(>:nth-child(3):last-child),.g3:has(>:nth-child(3):last-child){grid-template-columns:repeat(3,1fr)}
.g2:has(>:nth-child(3):last-child)>:last-child,.g3:has(>:nth-child(3):last-child)>:last-child{grid-column:auto;max-width:none;justify-self:stretch}
.g2:has(>:nth-child(5):last-child),.g3:has(>:nth-child(5):last-child){grid-template-columns:repeat(6,1fr)}
.g2:has(>:nth-child(5):last-child)>*,.g3:has(>:nth-child(5):last-child)>*{grid-column:span 2;max-width:none;justify-self:stretch}
.g2:has(>:nth-child(5):last-child)>:nth-child(n+4),.g3:has(>:nth-child(5):last-child)>:nth-child(n+4){grid-column:span 3}
@media (max-width:820px){
 .g2:has(>:nth-child(3):last-child),.g3:has(>:nth-child(3):last-child),.g2:has(>:nth-child(5):last-child),.g3:has(>:nth-child(5):last-child){grid-template-columns:1fr}
 .g2:has(>:nth-child(5):last-child)>*,.g3:has(>:nth-child(5):last-child)>*,.g2:has(>:nth-child(5):last-child)>:nth-child(n+4),.g3:has(>:nth-child(5):last-child)>:nth-child(n+4){grid-column:auto}
}

/* ---- tidier wrapping ---- */
.reframe,h1,h2,.stmt p,.quote{text-wrap:balance}
.flow span{text-align:center}
@media (max-width:820px){.flow{flex-direction:column}.flow .arr{transform:rotate(90deg)}}

/* ---- phones: one layout that scales with the screen width (reference 390px), so every phone looks the same ---- */
:root{--px:calc(min(100vw,430px)/390)}
html,#page{-webkit-text-size-adjust:100%;text-size-adjust:100%}
.trust{white-space:nowrap;max-width:100%;font-size:min(14px,3.1vw);gap:min(10px,2vw);padding:8px min(20px,3.6vw)}
.trust .stars{letter-spacing:0;font-size:min(13px,2.9vw)}
@media (max-width:820px){
 body{font-size:max(15px,calc(16.5*var(--px)))}
 section{padding:calc(58*var(--px)) 0}
 .wrap{padding:0 calc(18*var(--px))}
 h1{font-size:max(34px,calc(40*var(--px)));margin-bottom:calc(22*var(--px))}
 h2{font-size:max(26px,calc(30*var(--px)))}
 h3{font-size:max(18px,calc(21*var(--px)))}
 .lede{font-size:max(16px,calc(18*var(--px)))}
 .eyebrow{font-size:max(11px,calc(12.5*var(--px)))}
 .hand{font-size:max(20px,calc(24*var(--px)))}
 .btn{font-size:max(13.5px,calc(15*var(--px)));padding:calc(17*var(--px)) calc(18*var(--px))}
 .fine{font-size:max(12px,calc(13.5*var(--px)))}
 .hero{padding:calc(44*var(--px)) 0 calc(60*var(--px))}
 .card{padding:calc(22*var(--px)) calc(20*var(--px))}
 .card p{font-size:max(15px,calc(16.5*var(--px)))}
 .num{font-size:max(13px,calc(15*var(--px)))}
 .chip{font-size:max(11px,calc(12*var(--px)))}
 .stmt p{font-size:max(18px,calc(20*var(--px)))}
 .stmt .quote{font-size:max(22px,calc(26*var(--px)))}
 .outcome p{font-size:max(15.5px,calc(17.5*var(--px)))}
 .story p{font-size:max(16px,calc(18*var(--px)))}
 .story .punch{font-size:max(19px,calc(22*var(--px)))}
 .who .tag{font-size:max(19px,calc(22*var(--px)))}
 .brk .now{font-size:max(17px,calc(20*var(--px)))}
 .brk .why{font-size:max(15px,calc(17*var(--px)))}
 .reframe{font-size:max(22px,calc(26*var(--px)))}
 .price h2{font-size:max(24px,calc(28*var(--px)))}
 .amt b{font-size:max(56px,calc(68*var(--px)))}
 .amt s{font-size:max(22px,calc(26*var(--px)))}
 .checks li{font-size:max(15px,calc(17*var(--px)))}
 .maybes{font-size:max(22px,calc(26*var(--px)))}
 .flow{font-size:max(16px,calc(18*var(--px)))}
 .flow .arr{font-size:max(24px,calc(28*var(--px)))}
 .claim .q{font-size:max(22px,calc(26*var(--px)))}
 .claim p{font-size:max(15px,calc(17*var(--px)))}
 .desires li{font-size:max(16.5px,calc(19*var(--px)))}
 .feature-body p{font-size:max(15.5px,calc(17.5*var(--px)))}
 .tcard p{font-size:max(15px,calc(17*var(--px)))}
 .tcard cite{font-size:max(12.5px,calc(14*var(--px)))}
 footer{font-size:max(11.5px,calc(12.5*var(--px)))}
 .pol figcaption{font-size:max(22px,calc(26*var(--px)))}
 .bonus.featured h3{font-size:max(21px,calc(24*var(--px)))}
 .bonus.featured p{font-size:max(15.5px,calc(17*var(--px)))}
 .bonuses .hand{font-size:max(22px,calc(28*var(--px)))}
}

/* the first screen shows at once: no fade-in wait for the top of the page */
.hero .r{opacity:1!important;transform:none!important;transition:none!important}
`````

### FILE: kit/4-build/build_page.py

`````
#!/usr/bin/env python3
"""Assemble the sales page (draft with the layout editor inside).

usage:
  python3 build_page.py --body body.html --kit brand-kit.md --out index.html [--title "My page"]

--body  the page content: everything that goes inside <div id="page"> (the <section> blocks)
--kit   the brand kit file (a markdown file with a "Role map" and "Fonts", see 2-brand/_template.md)
--out   where to write the finished draft (open it in a browser)

Only the Python standard library is used.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROLE_RE = re.compile(
    r'^\s*[-*]\s*(ink-soft|on-dark-2|on-dark|on-hi|bg|paper|ink|accent|soft|hi|sand|dark)\s*(?:\([^)]*\))?\s*:\s*(#[0-9A-Fa-f]{6})',
    re.M)
REQUIRED = ['bg', 'paper', 'ink', 'ink-soft', 'accent', 'soft', 'hi', 'sand', 'dark', 'on-dark', 'on-dark-2']


def parse_kit(path):
    text = open(path, encoding='utf-8').read()
    roles = {m.group(1): m.group(2).upper() for m in ROLE_RE.finditer(text)}
    fonts = {}
    for key, name in (('Big', 'head'), ('Standard', 'body'), ('Handwritten', 'hand')):
        m = re.search(r'^\s*[-*]\s*' + key + r'[^:\n]*:\s*([^\n]+)', text, re.M)
        if m:
            fonts[name] = m.group(1).strip()
    return roles, fonts


def split_font(spec):
    """'Montserrat 800' -> ('Montserrat', '800'); 'Lato' -> ('Lato', None)"""
    spec = re.sub(r'\(.*?\)', '', spec).strip()
    m = re.match(r'^(.*?)(?:\s+(\d{3}))?(?:\s*\+.*)?$', spec)
    return (m.group(1).strip() or 'Arial'), m.group(2)


def font_url(fonts):
    fams = []
    for key in ('head', 'body', 'hand'):
        if key not in fonts:
            continue
        name, weight = split_font(fonts[key])
        fam = name.replace(' ', '+')
        if key == 'head':
            ws = sorted({'700', '800', '900', weight or '800'})
            fams.append('family=%s:wght@%s' % (fam, ';'.join(ws)))
        elif key == 'body':
            fams.append('family=%s:wght@400;700;900' % fam)
        else:
            fams.append('family=%s' % fam)  # default weight; the page uses it as a handwritten accent
    return 'https://fonts.googleapis.com/css2?%s&display=swap' % '&'.join(fams)



def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def contrast_report(r):
    pairs = [('ink on bg', 'ink', 'bg', 4.5), ('ink on paper', 'ink', 'paper', 4.5), ('ink-soft on bg', 'ink-soft', 'bg', 4.5),
             ('ink on sand', 'ink', 'sand', 4.5), ('on-dark on dark', 'on-dark', 'dark', 4.5), ('on-dark-2 on dark', 'on-dark-2', 'dark', 4.5),
             ('button text on button', 'on-hi', 'hi', 4.5), ('accent on paper (large text only)', 'accent', 'paper', 3.0)]
    out = []
    for label, fg, bgk, need in pairs:
        v = ratio(r[fg], r[bgk])
        out.append('  %-36s %.1f:1  %s' % (label, v, 'ok' if v >= need else 'LOW (needs %.1f). Use a darker or lighter twin and tell the client.' % need))
    return '\n'.join(out)

REVEAL_JS = """(function(){
if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
if(!('IntersectionObserver' in window))return;
document.documentElement.classList.add('anim');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.r').forEach(function(el){io.observe(el)});
setTimeout(function(){document.querySelectorAll('.r:not(.in)').forEach(function(el){var r=el.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)el.classList.add('in')})},2500);
})();
/* Phones and tablets: stretch the page to the full screen width even when the builder pads the code block (no white strips left and right) */
(function(){var p=document.getElementById('page');if(!p)return;
function fit(){p.style.width='';p.style.marginLeft='';p.style.maxWidth='';
if(window.innerWidth>820)return;
var l=p.getBoundingClientRect().left;
p.style.maxWidth='none';p.style.width=window.innerWidth+'px';p.style.marginLeft=(-l)+'px';}
fit();window.addEventListener('resize',fit);window.addEventListener('load',fit);})();"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--body', required=True)
    ap.add_argument('--kit', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--title', default='Sales page')
    a = ap.parse_args()

    roles, fonts = parse_kit(a.kit)
    missing = [r for r in REQUIRED if r not in roles]
    if missing:
        sys.exit('The brand kit is missing these colors in its Role map: %s (see 2-brand/_template.md)' % ', '.join(missing))
    roles.setdefault('on-hi', roles['ink'])
    for k, dflt in (('head', 'Montserrat 800'), ('body', 'Lato'), ('hand', 'Caveat')):
        fonts.setdefault(k, dflt)

    # speed: a stand-in font with the same width as the web font, so the text does not jump when the web font loads
    try:
        fb_table = json.load(open(os.path.join(HERE, 'font-fallbacks.json'), encoding='utf-8')).get('fonts', {})
    except (OSError, ValueError):
        fb_table = {}
    fb_css = ''
    fb_names = set()
    for k in ('head', 'body'):
        nm = split_font(fonts[k])[0]
        r = fb_table.get(nm)
        if r and nm not in fb_names:
            fb_names.add(nm)
            fb_css += ("@font-face{font-family:'%s Fallback';src:local('Arial');font-weight:400 500;size-adjust:%.1f%%}\n"
                       "@font-face{font-family:'%s Fallback';src:local('Arial Bold'),local('Arial-BoldMT');font-weight:600 900;size-adjust:%.1f%%}\n"
                       % (nm, r['400'] * 100, nm, r['700'] * 100))

    def fam(k, generic):
        nm = split_font(fonts[k])[0]
        if nm in fb_names:
            return "'%s','%s Fallback',%s" % (nm, nm, generic)
        return "'%s',%s" % (nm, generic)

    root = fb_css + ':root{' + ''.join('--%s:%s;' % (r, roles[r]) for r in REQUIRED + ['on-hi']) + \
        '--font-head:%s;--font-body:%s;--font-hand:%s;}' % (fam('head', 'sans-serif'), fam('body', 'sans-serif'), fam('hand', 'cursive'))

    css = open(os.path.join(HERE, 'base.css'), encoding='utf-8').read()
    ecss = open(os.path.join(HERE, 'editor.css'), encoding='utf-8').read()
    ejs = open(os.path.join(HERE, 'editor.js'), encoding='utf-8').read()
    body = open(a.body, encoding='utf-8').read()

    # speed: the first image loads first, every other image waits until it is near the screen
    def load_attrs(m, first=[True]):
        tag = re.sub(r'\s(?:loading|decoding|fetchpriority)="[^"]*"', '', m.group(0))
        extra = ' fetchpriority="high" decoding="async"' if first[0] else ' loading="lazy" decoding="async"'
        first[0] = False
        return tag[:-1].rstrip() + extra + '>'
    body = re.sub(r'<img\b[^>]*>', load_attrs, body)

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="%s" rel="stylesheet">
<style>
/* brand kit */
%s
%s
</style>
<style id="layout-edits"></style>
<style id="editor-css">
%s
</style>
</head>
<body>
<div id="page">
%s
</div>
<script type="application/json" id="layout-edits-data">{}</script>
<script id="layout-editor">
%s
</script>
<script>
%s
</script>
</body>
</html>
''' % (a.title.replace('<', '&lt;'), font_url(fonts).replace('&', '&amp;'), root, css, ecss, body, ejs, REVEAL_JS)
    with open(a.out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Contrast check:')
    print(contrast_report(roles))
    print('wrote %s (%d bytes). Open it in a browser. Click "Edit layout" at the bottom to move, resize and recolor.' % (a.out, len(html.encode('utf-8'))))


if __name__ == '__main__':
    main()
`````

### FILE: kit/4-build/check_page.py

`````
#!/usr/bin/env python3
"""Check the page before handing it over.

usage:
  python3 check_page.py --page index.html [--copy copy.md] [--images-dir images] [--reference-phrases reference-phrases.txt]

Checks:
  - leftover text from the reference example (Isabelle's own page) that must never appear on a client's page
  - placeholders still on the page ({{ }}, TODO, PASTE-YOUR, dashed "Your photo here" boxes)
  - images that point to a file that does not exist, or have no alt text
  - buttons without a real link (empty or "#")
  - sections numbered 1..14 present (missing ones are listed, not an error)
  - every line of the copy file is on the page (if --copy is given)
Prints a short report. Exit code 1 if something must be fixed.
"""
import argparse
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def visible_text(h):
    h = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S)
    h = re.sub(r'<[^>]+>', ' ', h)
    return re.sub(r'\s+', ' ', html.unescape(h)).strip()


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--page', required=True)
    ap.add_argument('--copy')
    ap.add_argument('--images-dir', default='images')
    ap.add_argument('--reference-phrases', default=os.path.join(HERE, 'reference-phrases.txt'))
    a = ap.parse_args()

    raw = open(a.page, encoding='utf-8').read()
    text = visible_text(raw)
    problems, notes = [], []

    if os.path.exists(a.reference_phrases):
        for line in open(a.reference_phrases, encoding='utf-8'):
            p = line.strip()
            if p and not p.startswith('#') and p.lower() in text.lower():
                problems.append('Leftover reference text on the page: "%s". Replace it with the client\'s own words.' % p)

    for pat, label in ((r'\{\{.*?\}\}', 'a {{placeholder}}'), (r'\bTODO\b', 'TODO'), (r'PASTE-YOUR', 'PASTE-YOUR link placeholder'), (r'\[ASK[^\]]*\]', 'an unanswered [ASK] gap'), (r'\{ASK ME[^}]*\}', 'an unanswered {ASK ME} gap'), (r'\{FILL IN[^}]*\}', 'an unfilled {FILL IN} note')):
        for m in re.finditer(pat, text):
            problems.append('Placeholder left on the page: %s ("%s")' % (label, m.group(0)[:60]))
    ph = len(re.findall(r'class="[^"]*\bph\b', raw))
    if ph:
        notes.append('%d dashed placeholder box(es) (class "ph") still on the page. Fine in a draft, replace or remove before publishing.' % ph)

    base = os.path.dirname(os.path.abspath(a.page))
    for m in re.finditer(r'<img\b[^>]*>', raw):
        tag = m.group(0)
        src = re.search(r'src="([^"]*)"', tag)
        if not src:
            continue
        s = src.group(1)
        if not s.startswith(('data:', 'http://', 'https://')) and not os.path.exists(os.path.join(base, s)):
            problems.append('Image file not found: %s' % s)
        if not re.search(r'alt="[^"]+"', tag):
            notes.append('Image without alt text: %s' % s[:60])

    for m in re.finditer(r'<a\b[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*>', raw):
        href = re.search(r'href="([^"]*)"', m.group(0))
        if not href or href.group(1) in ('', '#'):
            problems.append('A button has no real link yet (href is empty or "#").')
            break

    found = sorted({int(x) for x in re.findall(r'data-section="(\d+)"', raw)})
    gone = [n for n in range(1, 15) if n not in found]
    if gone:
        notes.append('Sections not on this page: %s (fine if the client chose to skip them).' % ', '.join(map(str, gone)))

    if a.copy and os.path.exists(a.copy):
        nt = norm(text + ' ' + ' '.join(html.unescape(x) for x in re.findall(r'alt="([^"]*)"', raw)))
        lost = []
        for line in open(a.copy, encoding='utf-8'):
            if line.lstrip().startswith(('>', '<!--', '(', '[')):
                continue
            l = line.strip().lstrip('#*- ').strip()
            if len(l) < 25 or l.startswith(('(', '[', '<!--')):
                continue
            if norm(l)[:40] not in nt:
                lost.append(l[:90])
        if lost:
            problems.append('%d line(s) of the approved copy are not on the page, for example: "%s"' % (len(lost), lost[0]))

    print('CHECK REPORT for ' + a.page)
    print('------------')
    if not problems:
        print('OK: nothing that must be fixed.')
    for p in problems:
        print('FIX  ' + p)
    for n in notes:
        print('NOTE ' + n)
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
`````

### FILE: kit/4-build/editor.css

`````
/* Layout editor UI. Draft only: removed in the final export. Neutral tool colors on purpose (not the brand kit). */
#ed-ui{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:99999;display:flex;flex-direction:column;align-items:center;gap:8px;font:600 14px/1.3 system-ui,-apple-system,Segoe UI,sans-serif;max-width:calc(100vw - 20px)}
#ed-ui button{font:inherit;cursor:pointer;border:0;border-radius:10px;padding:9px 14px;background:#2a2a2a;color:#fff}
#ed-ui button:hover{background:#444}
#ed-ui .ed-main{background:#2563eb;box-shadow:0 6px 20px rgba(0,0,0,.28);padding:12px 20px;border-radius:999px;font-size:15px}
#ed-ui .ed-main:hover{background:#1d4ed8}
#ed-ui .ed-panel{background:#161616;color:#fff;border-radius:16px;padding:14px 16px;box-shadow:0 10px 34px rgba(0,0,0,.4);display:grid;gap:10px;width:min(820px,calc(100vw - 20px))}
#ed-ui .ed-panel[hidden],#ed-ui .ed-sel[hidden],#ed-ui .ed-toast[hidden]{display:none}
#ed-ui .ed-hint{font-weight:500;color:#cfcfcf;font-size:13px}
#ed-ui .ed-hint b{color:#fff}
#ed-ui .ed-sel{display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:10px 0;border-top:1px solid #333;border-bottom:1px solid #333}
#ed-ui .ed-size{display:flex;align-items:center;gap:10px;flex:1 1 240px}
#ed-ui .ed-size input{flex:1;accent-color:#2563eb}
#ed-ui .ed-size b{min-width:44px;text-align:right}
#ed-ui .ed-grp{display:inline-flex;gap:2px}
#ed-ui .ed-grp button:first-child{border-radius:10px 0 0 10px}
#ed-ui .ed-grp button:last-child{border-radius:0 10px 10px 0}
#ed-ui .ed-grp button:only-child{border-radius:10px}
#ed-ui .ed-row{display:flex;flex-wrap:wrap;gap:8px}
#ed-ui .ed-toast{background:#161616;color:#fff;border-radius:999px;padding:9px 16px;font-weight:600;box-shadow:0 6px 20px rgba(0,0,0,.3)}
html.ed-on body{padding-bottom:330px}
html.ed-on #page img{cursor:pointer}
html.ed-on #page [data-ed]:hover{outline:3px dashed #2563eb;outline-offset:3px}
html.ed-on #page a{cursor:default}
#ed-sel{position:fixed;z-index:99998;border:3px solid #2563eb;pointer-events:none;box-shadow:0 0 0 9999px rgba(0,0,0,0)}
#ed-sel[hidden]{display:none}
#ed-sel .ed-handle{position:absolute;right:-10px;bottom:-10px;width:22px;height:22px;background:#2563eb;border:3px solid #fff;border-radius:6px;cursor:nwse-resize;pointer-events:auto;box-shadow:0 2px 8px rgba(0,0,0,.35)}
#ed-line{position:fixed;height:4px;background:#2563eb;border-radius:2px;z-index:99998;pointer-events:none}
#ed-line[hidden]{display:none}
@media (max-width:600px){#ed-ui .ed-panel{padding:12px}#ed-ui button{padding:9px 11px}html.ed-on body{padding-bottom:300px}}

#ed-ui .ed-id{flex:1 0 100%;font-weight:500;color:#cfcfcf;font-size:13px}
#ed-ui .ed-id b{color:#fff}
#ed-ui .ed-step{display:inline-flex;align-items:center;gap:6px;background:#222;border-radius:10px;padding:3px 4px 3px 10px;font-size:13px;font-weight:500}
#ed-ui .ed-step b{min-width:34px;text-align:center}
#ed-ui .ed-step button{padding:6px 11px}
#ed-ui .ed-send{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:500}
#ed-ui .ed-send select{font:inherit;background:#2a2a2a;color:#fff;border:0;border-radius:10px;padding:8px 10px;max-width:220px}
#ed-tags i{position:fixed;z-index:99997;font:800 13px/1 system-ui,sans-serif;font-style:normal;background:#111;color:#fff;border:2px solid #fff;border-radius:999px;min-width:28px;height:28px;display:grid;place-items:center;padding:0 8px;pointer-events:none;box-shadow:0 2px 8px rgba(0,0,0,.35)}
#ed-tags[hidden]{display:none}
html.ed-on #page section[data-section]::before{content:"SECTION " attr(data-section) " · " attr(data-name);position:absolute;top:8px;left:8px;z-index:60;background:#2563eb;color:#fff;font:700 12px/1 system-ui,sans-serif;padding:7px 11px;border-radius:8px;pointer-events:none;box-shadow:0 2px 8px rgba(0,0,0,.25)}

#ed-ui .ed-panel{max-height:min(62vh,540px);overflow:auto}
#ed-ui .ed-txt{display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:10px 0;border-top:1px solid #333;border-bottom:1px solid #333}
#ed-ui .ed-txt[hidden]{display:none}
#ed-ui .ed-colors{display:flex;align-items:center;gap:6px;flex:1 1 300px;font-size:13px;font-weight:500}
#ed-ui .ed-colors>span{min-width:104px}
#ed-ui .ed-sw{width:26px;height:26px;border-radius:50%!important;padding:0!important;border:2px solid #fff!important;box-shadow:0 0 0 1px #000}
#ed-ui .ed-tip{flex:1 0 100%;font-size:12px;font-weight:500;color:#aaa}
html.ed-on #page :is(h1,h2,h3,p,li,.hand,.fine,.btn,.trust,.chip,.eyebrow):hover{outline:2px dashed rgba(37,99,235,.6);outline-offset:3px}
html.ed-on #page .ed-selected:is(h1,h2,h3,p,li,.hand,.fine,.btn,.trust,.chip,.eyebrow){outline:0}
#ed-sel.ed-text-mode .ed-handle{display:none}
#ed-sel.ed-text-mode{border-style:dashed}
html.ed-on #page ::selection{background:rgba(37,99,235,.28)}
`````

### FILE: kit/4-build/editor.js

`````
/* Layout editor for draft sales pages. The owner can select an image (resize, align, move, send to a section,
   space above/below, hide) or any text (size, color, alignment, spacing, highlighter), undo, and save.
   Sizes are stored per device (desktop / phone) so the page stays responsive.
   Needs: <div id="page">, <style id="layout-edits">, <script type="application/json" id="layout-edits-data">. */
(function () {
  var page = document.getElementById('page');
  var styleEl = document.getElementById('layout-edits');
  var dataEl = document.getElementById('layout-edits-data');
  if (!page || !styleEl || !dataEl) return;

  var MQ = '(max-width:820px)';
  var BLOCKS = 'p,h2,h3,figure,.cta,ul,ol,.card,.outcome,.claim,.feature,.stmt,.flow,.maybes,.lede,.note,.trust,.proofgrid,.shots,.bonuses';
  var TEXT = 'h1,h2,h3,p,li,.hand,.fine,.btn,.trust,.tag,.chip,.eyebrow,.num,.q,.reframe';
  var SWATCHES = [['Ink', '--ink'], ['Soft ink', '--ink-soft'], ['Accent', '--accent'], ['Soft', '--soft'], ['Button', '--hi'],
                  ['White', '--paper'], ['Sand', '--sand'], ['On dark', '--on-dark'], ['On dark 2', '--on-dark-2']];
  var edits = {};
  try { edits = JSON.parse(dataEl.textContent || '{}'); } catch (e) { edits = {}; }
  var on = false, sel = null, kind = '', hist = [], uid = 0, teUid = 0, dragEl = null, raf = 0;

  function mode() { return window.matchMedia(MQ).matches ? 'm' : 'd'; }
  function targetOf(img) { return img.closest('.fig,.pol') || img; }
  function idOf(el) { return kind === 'text' ? 't' + el.getAttribute('data-te') : el.getAttribute('data-ed'); }

  function ensureIds() {
    page.querySelectorAll('[data-ed]').forEach(function (e) { uid = Math.max(uid, +e.getAttribute('data-ed') || 0); });
    page.querySelectorAll('[data-te]').forEach(function (e) { teUid = Math.max(teUid, +e.getAttribute('data-te') || 0); });
    page.querySelectorAll('img').forEach(function (img) {
      var t = targetOf(img);
      if (!t.getAttribute('data-ed')) t.setAttribute('data-ed', ++uid);
    });
  }

  function inSwipe(id) { var el = page.querySelector('[data-ed="' + id + '"]'); return !!(el && el.closest('.swipe-frame')); }
  function css(forEdit) {
    var out = { d: '', m: '' };
    Object.keys(edits).forEach(function (id) {
      var sel_ = id.charAt(0) === 't' ? '#page [data-te="' + id.slice(1) + '"]' : '#page [data-ed="' + id + '"]';
      ['d', 'm'].forEach(function (m) {
        var e = edits[id][m]; if (!e) return;
        var r = '';
        if (e.w != null) r += inSwipe(id) ? 'width:' + e.w + '%!important;max-width:none!important;' : 'width:100%!important;max-width:' + e.w + '%!important;';
        if (e.a === 'l') r += 'margin-left:0!important;margin-right:auto!important;';
        if (e.a === 'c') r += 'margin-left:auto!important;margin-right:auto!important;';
        if (e.a === 'r') r += 'margin-left:auto!important;margin-right:0!important;';
        var u = function (n) { return m === 'm' ? 'calc(' + n + '*var(--px))' : n + 'px'; };
        if (e.mt != null) r += 'margin-top:' + u(e.mt) + '!important;';
        if (e.mb != null) r += 'margin-bottom:' + u(e.mb) + '!important;';
        if (e.fs != null) r += 'font-size:' + u(e.fs) + '!important;';
        if (e.c) r += 'color:' + e.c + '!important;';
        if (e.ta) r += 'text-align:' + (e.ta === 'l' ? 'left' : e.ta === 'r' ? 'right' : 'center') + '!important;';
        if (e.h) r += forEdit ? 'opacity:.22!important;' : 'display:none!important;';
        if (r) out[m] += sel_ + '{' + r + '}';
      });
    });
    return '@media (min-width:821px){' + out.d + '}@media (max-width:820px){' + out.m + '}';
  }
  function apply() { styleEl.textContent = css(on); }

  function push() {
    hist.push({ h: page.innerHTML, e: JSON.stringify(edits) });
    if (hist.length > 40) hist.shift();
  }
  function undo() {
    var s = hist.pop(); if (!s) { toast('Nothing to undo'); return; }
    page.innerHTML = s.h; edits = JSON.parse(s.e);
    sel = null; kind = ''; prepare(); apply(); refreshTools(); toast('Undone');
  }

  function setE(id, key, val) {
    var m = mode();
    edits[id] = edits[id] || {}; edits[id][m] = edits[id][m] || {};
    if (val == null) delete edits[id][m][key]; else edits[id][m][key] = val;
    apply();
  }

  function contentW(p) {
    var cs = getComputedStyle(p);
    return p.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  }
  function capOf(t) { return t.closest('.swipe-frame') ? 300 : 100; }
  function pctOf(t) { return Math.max(5, Math.min(capOf(t), Math.round(t.offsetWidth / contentW(t.parentElement) * 100))); }

  /* UI */
  function swatches(action) {
    return SWATCHES.map(function (s) {
      return '<button class="ed-sw" data-a="' + action + '" data-c="' + s[1] + '" title="' + s[0] + '" style="background:var(' + s[1] + ')"></button>';
    }).join('');
  }
  var STEPS = function (x) {
    return '<span class="ed-step">Space above <button data-a="mt-">−</button><b data-v="mt">0</b><button data-a="mt+">+</button></span>' +
           '<span class="ed-step">Space below <button data-a="mb-">−</button><b data-v="mb">0</b><button data-a="mb+">+</button></span>';
  };
  var ui = document.createElement('div');
  ui.id = 'ed-ui';
  ui.innerHTML =
    '<button class="ed-main" data-a="toggle">✎ Edit layout</button>' +
    '<div class="ed-panel" hidden>' +
      '<div class="ed-hint"></div>' +
      '<div class="ed-sel" hidden>' +
        '<div class="ed-id"></div>' +
        '<label class="ed-size">Size <input type="range" min="10" max="100" step="1"><b>60%</b></label>' +
        '<span class="ed-grp"><button data-a="al">Left</button><button data-a="ac">Center</button><button data-a="ar">Right</button></span>' +
        '<span class="ed-grp"><button data-a="up">Move up</button><button data-a="down">Move down</button></span>' +
        STEPS() +
        '<label class="ed-send">Send to section <select></select></label>' +
        '<button data-a="hide">Hide</button><button data-a="reset">Reset this image</button>' +
      '</div>' +
      '<div class="ed-txt" hidden>' +
        '<div class="ed-id"></div>' +
        '<span class="ed-step">Text size <button data-a="fs-">A−</button><b data-v="fs">18</b><button data-a="fs+">A+</button></span>' +
        '<span class="ed-grp"><button data-a="tl">Left</button><button data-a="tc">Center</button><button data-a="tr">Right</button></span>' +
        STEPS() +
        '<div class="ed-colors"><span>Text color</span>' + swatches('col') + '<input type="color" class="ed-wcolor" title="Any color" value="#c0392b"></div>' +
        '<div class="ed-tip">Select some words first and the color changes only those words. Select nothing and it changes the whole line.</div>' +
        '<div class="ed-colors"><span>Highlight color</span>' + swatches('hlc') + '</div>' +
        '<span class="ed-grp"><button data-a="hl">Highlight</button><button data-a="unhl">Remove highlight</button></span>' +
                '<span class="ed-grp"><button data-a="bold"><b>B</b></button><button data-a="ital"><i>I</i></button><button data-a="wclr">Clear word colors</button></span>' +
        '<span class="ed-grp"><button data-a="dup">Add text below</button><button data-a="hide">Hide</button><button data-a="del">Delete this</button></span>' +
        '<button data-a="treset">Reset this text</button>' +
        '<div class="ed-tip">Click the text to type in it. Select words to color them, make them bold or highlight them. Highlight: select some words first, or click Highlight with nothing selected to highlight the whole line. Select words inside a highlight and click Highlight again to remove just those.</div>' +
      '</div>' +
      '<div class="ed-row"><button data-a="undo">Undo</button><button data-a="save">Save draft</button><button data-a="export">Export final (no editor)</button></div>' +
    '</div><div class="ed-toast" hidden></div>';
  document.body.appendChild(ui);
  var ov = document.createElement('div');
  ov.id = 'ed-sel'; ov.hidden = true; ov.innerHTML = '<i class="ed-handle" title="Drag to resize"></i>';
  document.body.appendChild(ov);

  var tagBox = document.createElement('div'); tagBox.id = 'ed-tags'; tagBox.hidden = true; document.body.appendChild(tagBox);
  var tagMap = {};
  var panel = ui.querySelector('.ed-panel'), hint = ui.querySelector('.ed-hint'),
      selBox = ui.querySelector('.ed-sel'), txtBox = ui.querySelector('.ed-txt'), slider = ui.querySelector('input[type=range]'),
      sizeLbl = ui.querySelector('.ed-size b'), sendSel = ui.querySelector('.ed-send select'), toastEl = ui.querySelector('.ed-toast');

  page.querySelectorAll('section[data-section]').forEach(function (sc) {
    var o = document.createElement('option');
    o.value = sc.getAttribute('data-section'); o.textContent = sc.getAttribute('data-section') + '. ' + (sc.getAttribute('data-name') || '');
    sendSel.appendChild(o);
  });
  function toast(msg) {
    toastEl.textContent = msg; toastEl.hidden = false;
    clearTimeout(toast.t); toast.t = setTimeout(function () { toastEl.hidden = true; }, 3200);
  }
  function modeName() { return mode() === 'm' ? 'PHONE' : 'DESKTOP'; }
  function setV(name, v) { ui.querySelectorAll('[data-v=' + name + ']').forEach(function (n) { n.textContent = v; }); }

  function refreshTools() {
    hint.innerHTML = 'Editing <b>' + modeName() + '</b> sizes' + (mode() === 'd' ? ' (make the window narrow to edit phone sizes)' : '') +
      '. Click an image or any text to select it.';
    if (!sel || !document.body.contains(sel)) { sel = null; kind = ''; selBox.hidden = true; txtBox.hidden = true; ov.hidden = true; return; }
    ov.hidden = !on; ov.classList.toggle('ed-text-mode', kind === 'text');
    var cs = getComputedStyle(sel), sc = sel.closest('section[data-section]'), secNo = sc ? sc.getAttribute('data-section') : '?';
    setV('mt', Math.round(parseFloat(cs.marginTop) || 0));
    setV('mb', Math.round(parseFloat(cs.marginBottom) || 0));
    if (kind === 'img') {
      selBox.hidden = false; txtBox.hidden = true;
      slider.max = capOf(sel); var p = pctOf(sel); slider.value = p; sizeLbl.textContent = p + '%';
      var e = (edits[sel.getAttribute('data-ed')] || {})[mode()] || {};
      selBox.querySelector('[data-a=hide]').textContent = e.h ? 'Show' : 'Hide';
      var im = sel.querySelector('img') || sel;
      selBox.querySelector('.ed-id').innerHTML = '<b>Image ' + sel.getAttribute('data-ed') + '</b> · ' + (im.getAttribute('src') || '').split('/').pop() + ' · in section ' + secNo;
      if (sc) sendSel.value = secNo;
    } else {
      selBox.hidden = true; txtBox.hidden = false;
      setV('fs', Math.round(parseFloat(cs.fontSize) || 0));
      var snippet = (sel.textContent || '').trim().replace(/\s+/g, ' ');
      txtBox.querySelector('.ed-id').innerHTML = '<b>Text</b> · ' + sel.tagName.toLowerCase() + ' · section ' + secNo + ' · “' + snippet.slice(0, 40) + (snippet.length > 40 ? '…' : '') + '”';
    }
  }

  function prepare() {
    ensureIds();
    page.querySelectorAll('img').forEach(function (img) { img.draggable = false; });
    page.querySelectorAll('[data-ed]').forEach(function (t) { if (on) t.setAttribute('draggable', 'true'); else t.removeAttribute('draggable'); });
  }

  function select(t, k) {
    page.querySelectorAll('.ed-selected').forEach(function (e) { e.classList.remove('ed-selected'); });
    page.querySelectorAll('[contenteditable]').forEach(function (e) { e.removeAttribute('contenteditable'); e.removeAttribute('spellcheck'); });
    if (t && k === 'text' && t !== sel) push();
    sel = t; kind = t ? k : '';
    if (t && k === 'text') { t.setAttribute('contenteditable', 'true'); t.setAttribute('spellcheck', 'false'); }
    if (t) {
      t.classList.add('ed-selected');
      if (k === 'text' && !t.getAttribute('data-te')) t.setAttribute('data-te', ++teUid);
    }
    refreshTools(); place();
  }

  function place() {
    if (!on || !sel) return;
    var r = sel.getBoundingClientRect();
    ov.style.left = r.left + 'px'; ov.style.top = r.top + 'px'; ov.style.width = r.width + 'px'; ov.style.height = r.height + 'px';
  }
  function tags() {
    tagBox.hidden = !on; if (!on) return;
    page.querySelectorAll('[data-ed]').forEach(function (t) {
      var id = t.getAttribute('data-ed'), g = tagMap[id];
      if (!g) { g = document.createElement('i'); g.textContent = id; tagBox.appendChild(g); tagMap[id] = g; }
      var r = t.getBoundingClientRect(), vis = r.width > 0 && r.bottom > 20 && r.top < innerHeight;
      g.style.display = vis ? '' : 'none';
      if (vis) { g.style.left = (r.left + 8) + 'px'; g.style.top = (Math.max(r.top, 0) + 8) + 'px'; }
    });
  }
  function loop() { place(); tags(); raf = requestAnimationFrame(loop); }

  function setOn(v) {
    on = v;
    document.documentElement.classList.toggle('ed-on', on);
    if (on) document.documentElement.classList.remove('anim');
    panel.hidden = !on;
    ui.querySelector('.ed-main').textContent = on ? '✓ Done editing' : '✎ Edit layout';
    prepare(); apply();
    if (!on) { select(null); cancelAnimationFrame(raf); tagBox.hidden = true; } else { refreshTools(); raf = requestAnimationFrame(loop); }
  }

  /* clicks on the page */
  document.addEventListener('click', function (e) {
    if (!on) return;
    if (ui.contains(e.target) || ov.contains(e.target)) return;
    if (page.contains(e.target)) {
      e.preventDefault();
      var img = e.target.closest('img');
      if (img) return select(targetOf(img), 'img');
      var tx = e.target.closest(TEXT);
      select(tx && page.contains(tx) ? tx : null, 'text');
    }
  }, true);

  /* keep the user's text selection when a panel button is pressed */
  ui.addEventListener('mousedown', function (e) { if (e.target.closest('button')) e.preventDefault(); });

  /* words: color, bold, italic on the selected words */
  var lastR = null;
  document.addEventListener('selectionchange', function () { var r = curSel(); if (r) lastR = r.cloneRange(); });
  function wordRange() { var r = curSel(); if (!r && lastR && sel && sel.contains(lastR.commonAncestorContainer)) r = lastR; if (!r) toast('Select some words first'); return r; }
  function wordWrap(tag) {
    var r = wordRange(); if (!r) return;
    var m = document.createElement(tag);
    try { r.surroundContents(m); } catch (err) { m.appendChild(r.extractContents()); r.insertNode(m); }
    window.getSelection().removeAllRanges();
  }
  function wordColor(c) {
    var r = wordRange(); if (!r) return;
    var m = document.createElement('span'); m.style.color = c;
    try { r.surroundContents(m); } catch (err) { m.appendChild(r.extractContents()); r.insertNode(m); }
    window.getSelection().removeAllRanges();
  }
  function wordClear() {
    var r = wordRange(); if (!r) return;
    Array.prototype.slice.call(sel.querySelectorAll('span[style*="color"],b,i')).forEach(function (x) { if (r.intersectsNode(x)) { x.style.color = ''; if (x.tagName !== 'SPAN' || !x.getAttribute('style')) unwrap(x); } });
  }
  ui.addEventListener('input', function (e) {
    if (e.target.classList.contains('ed-wcolor') && sel) { push(); if (wordRange()) wordColor(e.target.value); }
  });

  /* highlighter */
  function unwrap(m) { var p = m.parentNode; while (m.firstChild) p.insertBefore(m.firstChild, m); p.removeChild(m); p.normalize(); }
  function marksIn(el) { return Array.prototype.slice.call(el.querySelectorAll('mark')); }
  function curSel() {
    var s = window.getSelection();
    if (!s || !s.rangeCount || s.isCollapsed || !sel) return null;
    var r = s.getRangeAt(0);
    return sel.contains(r.commonAncestorContainer) ? r : null;
  }
  function highlight(color) {
    var r = curSel(), mk;
    if (r) {
      var an = r.commonAncestorContainer; an = an.nodeType === 1 ? an : an.parentElement;
      var inside = an.closest('mark');
      if (inside && sel.contains(inside)) { unwrap(inside); window.getSelection().removeAllRanges(); return; }
      mk = document.createElement('mark');
      try { r.surroundContents(mk); } catch (err) { mk.appendChild(r.extractContents()); r.insertNode(mk); }
      window.getSelection().removeAllRanges();
    } else {
      if (marksIn(sel).length) { toast('This line already has a highlight. Select words to add more, or Remove highlight.'); return; }
      mk = document.createElement('mark');
      while (sel.firstChild) mk.appendChild(sel.firstChild);
      sel.appendChild(mk);
    }
    if (color) mk.style.setProperty('--hl', 'var(' + color + ')');
  }
  function setHlColor(color) {
    var r = curSel(), list = [];
    if (r) {
      var an = r.commonAncestorContainer; an = an.nodeType === 1 ? an : an.parentElement;
      var m = an.closest('mark'); if (m && sel.contains(m)) list = [m];
      else list = marksIn(sel).filter(function (x) { return r.intersectsNode(x); });
    } else list = marksIn(sel);
    if (!list.length) { highlight(color); return; }
    list.forEach(function (x) { x.style.setProperty('--hl', 'var(' + color + ')'); });
  }

  ui.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    var a = b.getAttribute('data-a');
    if (a === 'toggle') return setOn(!on);
    if (a === 'undo') return undo();
    if (a === 'save') { dl('index.html', serialize(false)); return toast('Saved: check your Downloads folder for index.html'); }
    if (a === 'export') { dl('index-final.html', serialize(true)); return toast('Exported index-final.html (no editor inside)'); }
    if (!sel) return;
    var id = idOf(sel);
    push();
    if (a === 'al') setE(id, 'a', 'l');
    if (a === 'ac') setE(id, 'a', 'c');
    if (a === 'ar') setE(id, 'a', 'r');
    if (a === 'tl') setE(id, 'ta', 'l');
    if (a === 'tc') setE(id, 'ta', 'c');
    if (a === 'tr') setE(id, 'ta', 'r');
    if (a === 'hide') { var cur = ((edits[id] || {})[mode()] || {}).h; setE(id, 'h', cur ? null : true); }
    if (a === 'reset' || a === 'treset') { if (edits[id]) delete edits[id][mode()]; apply(); }
    if (a === 'fs-' || a === 'fs+') {
      var f0 = ((edits[id] || {})[mode()] || {}).fs;
      if (f0 == null) f0 = Math.round(parseFloat(getComputedStyle(sel).fontSize) || 16);
      setE(id, 'fs', Math.max(10, Math.min(140, f0 + (a === 'fs+' ? 2 : -2))));
    }
    if (a === 'col') { if (curSel() || (lastR && sel.contains(lastR.commonAncestorContainer) && !lastR.collapsed)) wordColor('var(' + b.getAttribute('data-c') + ')'); else setE(id, 'c', 'var(' + b.getAttribute('data-c') + ')'); }
    if (a === 'hlc') setHlColor(b.getAttribute('data-c'));
    if (a === 'hl') highlight(null);
    if (a === 'wcol') wordColor('var(' + b.getAttribute('data-c') + ')');
    if (a === 'wclr') wordClear();
    if (a === 'bold') wordWrap('b');
    if (a === 'ital') wordWrap('i');
    if (a === 'dup') { var cp = sel.cloneNode(true); ['data-te', 'data-ed', 'contenteditable', 'class'].forEach(function (x) { if (x !== 'class') cp.removeAttribute(x); }); cp.classList.remove('ed-selected'); cp.textContent = 'New text. Click it to type.'; sel.parentNode.insertBefore(cp, sel.nextSibling); select(cp, 'text'); return; }
    if (a === 'del') { var gone = sel; select(null); gone.remove(); return; }
    if (a === 'unhl') marksIn(sel).forEach(unwrap);
    if (a === 'mt-' || a === 'mt+' || a === 'mb-' || a === 'mb+') {
      var k = a.slice(0, 2), cs2 = getComputedStyle(sel), cur2 = ((edits[id] || {})[mode()] || {})[k];
      if (cur2 == null) cur2 = Math.round(parseFloat(k === 'mt' ? cs2.marginTop : cs2.marginBottom) || 0);
      setE(id, k, Math.max(-80, Math.min(240, cur2 + (a.charAt(2) === '+' ? 8 : -8))));
    }
    if (a === 'up') { var p = sel.previousElementSibling; if (p) sel.parentNode.insertBefore(sel, p); }
    if (a === 'down') { var n = sel.nextElementSibling; if (n) sel.parentNode.insertBefore(n, sel); }
    refreshTools(); place();
  });

  slider.addEventListener('pointerdown', push);
  slider.addEventListener('input', function () {
    if (!sel || kind !== 'img') return;
    setE(sel.getAttribute('data-ed'), 'w', +slider.value);
    sizeLbl.textContent = slider.value + '%';
  });

  sendSel.addEventListener('change', function () {
    if (!sel || kind !== 'img') return;
    var s2 = page.querySelector('section[data-section="' + sendSel.value + '"]'); if (!s2) return;
    push();
    var cta = s2.querySelector('.cta');
    if (cta) cta.parentNode.insertBefore(sel, cta);
    else (s2.querySelector('.story') || s2.querySelector('.wrap:last-of-type') || s2).appendChild(sel);
    refreshTools(); place();
    sel.scrollIntoView({ behavior: 'smooth', block: 'center' });
    toast('Image ' + sel.getAttribute('data-ed') + ' moved to section ' + sendSel.value);
  });

  /* corner handle (images) */
  var rs = null;
  ov.querySelector('.ed-handle').addEventListener('pointerdown', function (e) {
    if (!sel || kind !== 'img') return; e.preventDefault(); e.stopPropagation(); push();
    var pr = sel.parentElement.getBoundingClientRect(), r = sel.getBoundingClientRect();
    rs = { x: e.clientX, w0: pctOf(sel), cw: contentW(sel.parentElement), k: (r.left - pr.left < 4) ? 1 : 2 };
    this.setPointerCapture(e.pointerId);
  });
  ov.querySelector('.ed-handle').addEventListener('pointermove', function (e) {
    if (!rs || !sel) return;
    var v = Math.max(10, Math.min(capOf(sel), Math.round(rs.w0 + (e.clientX - rs.x) * rs.k / rs.cw * 100)));
    setE(sel.getAttribute('data-ed'), 'w', v);
    slider.value = v; sizeLbl.textContent = v + '%';
  });
  ov.querySelector('.ed-handle').addEventListener('pointerup', function () { rs = null; refreshTools(); });

  /* drag to move (images) */
  var line = document.createElement('div'); line.id = 'ed-line'; line.hidden = true; document.body.appendChild(line);
  function dropTarget(e) {
    var b = e.target.closest ? e.target.closest(BLOCKS) : null;
    if (!b || !dragEl || !page.contains(b) || b === dragEl || dragEl.contains(b) || b.contains(dragEl) && b.tagName !== 'SECTION') return null;
    if (b.closest('footer')) return null;
    var r = b.getBoundingClientRect();
    return { b: b, before: e.clientY < r.top + r.height / 2, r: r };
  }
  document.addEventListener('dragstart', function (e) {
    if (!on) return;
    var t = e.target.closest ? e.target.closest('[data-ed]') : null;
    if (!t || !page.contains(t)) return;
    dragEl = t; select(t, 'img');
    e.dataTransfer.effectAllowed = 'move'; e.dataTransfer.setData('text/plain', 'move');
  });
  document.addEventListener('dragover', function (e) {
    if (!on || !dragEl) return;
    var d = dropTarget(e); if (!d) { line.hidden = true; return; }
    e.preventDefault(); e.dataTransfer.dropEffect = 'move';
    line.hidden = false; line.style.left = d.r.left + 'px'; line.style.width = d.r.width + 'px';
    line.style.top = (d.before ? d.r.top : d.r.bottom) - 2 + 'px';
  });
  document.addEventListener('drop', function (e) {
    if (!on || !dragEl) return;
    var d = dropTarget(e); line.hidden = true; if (!d) { dragEl = null; return; }
    e.preventDefault(); push();
    d.b.parentNode.insertBefore(dragEl, d.before ? d.b : d.b.nextSibling);
    dragEl = null; refreshTools(); place();
  });
  document.addEventListener('dragend', function () { dragEl = null; line.hidden = true; });

  document.addEventListener('keydown', function (e) {
    if (!on) return;
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'z' && !(document.activeElement && document.activeElement.isContentEditable)) { e.preventDefault(); undo(); }
    if (e.key === 'Escape') select(null);
  });
  window.addEventListener('resize', function () { if (on) { apply(); refreshTools(); } });

  /* save / export */
  function serialize(final) {
    var cl = document.documentElement.cloneNode(true);
    cl.classList.remove('ed-on', 'anim');
    ['#ed-ui', '#ed-sel', '#ed-line', '#ed-tags'].forEach(function (s) { var n = cl.querySelector(s); if (n) n.remove(); });
    cl.querySelectorAll('.ed-selected').forEach(function (e) { e.classList.remove('ed-selected'); });
    cl.querySelectorAll('[contenteditable]').forEach(function (e) { e.removeAttribute('contenteditable'); e.removeAttribute('spellcheck'); });
    cl.querySelectorAll('[draggable]').forEach(function (e) { e.removeAttribute('draggable'); });
    cl.querySelector('#layout-edits').textContent = css(false);
    cl.querySelector('#layout-edits-data').textContent = JSON.stringify(edits);
    if (final) ['#layout-editor', '#editor-css', '#layout-edits-data'].forEach(function (s) { var n = cl.querySelector(s); if (n) n.remove(); });
    return '<!DOCTYPE html>\n' + cl.outerHTML;
  }
  function dl(name, text) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type: 'text/html' }));
    a.download = name; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 800);
  }
  window.__layoutEditor = { serialize: serialize, edits: function () { return edits; } };

  ensureIds(); apply();
})();
`````

### FILE: kit/4-build/example-body.html

`````
<!--
STRUCTURE REFERENCE ONLY.
This is Isabelle's own live sales page, kept so you can see the exact markup, class names and patterns.
NEVER reuse its words, numbers, names, images, prices or links on a client's page.
Replace every piece of content. check_page.py will flag leftover reference text.
Each <section> needs data-section="N" and data-name="..." (the layout editor uses them).
Image tags: use the client's own files from images/ (never the file names below).
-->
<!-- SECTION 1: BIG DESIRE HEADLINE (hero) -->
<section data-section="1" data-name="Big desire headline" class="hero center">
<div class="wrap">
<div class="trust r"><span class="stars">⭐️⭐️⭐️⭐️⭐️</span> trusted by 6,000+ happy students</div>
<h1 class="r">Make Your Digital Product <mark>Irresistible to Buy</mark></h1>
<figure class="fig r" style="--w:1000px"><img src="images/hero-mockup-v2.png" alt="The Buy-Now Sales Page bundle, built with Claude: the AI sales page tool, the Color Palette Generator, done-for-you templates and payment notifications" width="1851" height="958"></figure><p class="lede r">Steal my <span class="pss">proven sales page</span> structure + custom-built AI sales page tool to make your digital product crystal clear + irresistible to buy in just 5 minutes.</p>
<p class="note r"><span class="hand">No copywriting skills required!</span></p>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">I WANT ACCESS! (ONLY $37)</a><span class="fine">One-Time Payment • Instant Access</span></div>

</div>
</section>

<!-- SECTION 2: DESIRE-LED BELIEF SHIFT + OUTCOME STACK -->
<section data-section="2" data-name="Belief shift + outcomes" class="s-paper center">
<div class="wrap narrow">
<h2 class="r" style="margin-bottom:48px">Your Sales Page Doesn’t Need More Words. It Needs <mark>the Right Ones.</mark></h2>
<div class="stmt r">
<p><svg class="ico ico-x" viewBox="0 0 28 28" aria-hidden="true" style="transform:rotate(-4deg)"><path pathLength="40" d="M6 5.5 C10 10 15 16 22 22.5"/><path pathLength="40" d="M22.5 6 C17 11 12 17 5.5 22"/></svg>You don’t need to become a copywriter.</p>
<p><svg class="ico ico-x" viewBox="0 0 28 28" aria-hidden="true" style="transform:rotate(3deg)"><path pathLength="40" d="M5.5 6.5 C11 9.5 16 15.5 22.5 21.5"/><path pathLength="40" d="M21.5 5.5 C16.5 11 11 16 6.5 22.5"/></svg>You don’t need to spend hours figuring out what goes where.</p>
<p><svg class="ico ico-x" viewBox="0 0 28 28" aria-hidden="true" style="transform:rotate(-2deg)"><path pathLength="40" d="M6.5 5 C11 11 16 15 21.5 22"/><path pathLength="40" d="M22 6.5 C16 10 11 16.5 5.5 21.5"/></svg>And you definitely don’t need to keep asking ChatGPT to “make this more persuasive” for the 17th time.</p>
<p><svg class="ico ico-ok" viewBox="0 0 32 28" aria-hidden="true" style="transform:rotate(-3deg)"><path pathLength="40" d="M4 15 C7 17.5 9.5 21 11.5 24 C15 15 20 8 28 3.5"/></svg>You need a sales page that makes the right person land on it and immediately think:</p>
<p class="quote"><mark>“Ohhh. This is exactly what I need.”</mark></p><figure class="fig shot r"><img src="images/proof-stripe-notifications.webp" alt="Seven Stripe notifications showing payments received, buyer emails covered" width="1200" height="1978" loading="lazy"></figure>
</div>
<p class="r" style="font-weight:700;font-size:20px;margin-top:8px">With The Buy-Now Sales Page™, you’ll:</p>
<div class="outcomes">
<div class="outcome r"><span class="n">1</span><p>Make your offer crystal clear so someone who has never heard of you before immediately understands what you sell + why they want it.</p></div>
<div class="outcome r"><span class="n">2</span><p>Make your digital product feel irresistible to buy so your page doesn't just explain your offer... it makes people want it.</p></div>
<div class="outcome r"><span class="n">3</span><p>Have your entire sales page built in just 5 minutes so you can stop spending hours writing, rewriting + wondering if you said the right thing.</p></div>
</div>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">BUILD MY BUY-NOW SALES PAGE →</a></div>
</div>
</section>

<!-- SECTION 3: ORIGIN / PROOF STORY -->
<section data-section="3" data-name="Origin story">
<div class="wrap narrow">
<figure class="fig shot r" style="--w:520px;margin-bottom:48px"><img src="images/proof-revenue-today.webp" alt="A revenue dashboard showing $1,032.73 today from 23 orders and 12 unique buyers" width="1200" height="542" loading="lazy"></figure>
<div class="story">
<h2 class="r">How I Built Sales Pages That Could <mark>Sell to Complete Strangers</mark></h2>
<div class="r">
<p>When I started using ads to sell my digital products, I learned something FAST:</p>
<p class="punch">My sales page had to do the selling.</p>
<p>Complete strangers were clicking my ads + landing on my offer without watching my content or knowing who I was.</p>
<p>So I stopped asking:</p>
<p><span class="hand">“How do I make this sound good?”</span></p>
<p>And started asking:</p>
<p><span class="hand">“What does someone need to see + believe before clicking BUY NOW?”</span></p>
<p>That became my sales page structure — battle-tested across $1M+ in ad spend + sales.</p>
<p>And now I've built the whole thing into an AI tool.</p>
<p class="punch">Give it your offer → get your sales page.</p>
</div>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">BUILD MY PAGE THAT SELLS →</a></div>
</div>
</div>
</section>

<!-- SECTION 4: WHO THIS IS FOR -->
<section data-section="4" data-name="Who this is for" class="s-sand who">
<div class="wrap">
<div class="center"><figure class="fig r" style="--w:700px"><img src="images/blank-to-sales-page.webp" alt="From a blank sales page, endless rewriting and generic ChatGPT copy to a finished sales page with a checkmark" width="1200" height="800" loading="lazy"></figure><h2 class="r">This Was Built for You <mark>if:</mark></h2></div>
<div class="grid g2" style="margin-top:44px">
<div class="card r">
<span class="tag">You already HAVE your digital product…</span>
<p>But you're staring at a blank sales page thinking:</p>
<p><span class="hand">“Okay… what the heck do I actually say?”</span></p>
<p class="want">You want the page done — without spending the next three days trying to become a copywriter.</p>
</div>
<div class="card r">
<span class="tag">You already HAVE a sales page…</span>
<p>But you keep changing the headline, rewriting sections + wondering whether people actually understand why they should buy.</p>
<p class="want">You want to finally feel:</p>
<p><span class="hand">“YES. This says exactly what I sell + why someone would want it.”</span></p>
</div>
<div class="card r">
<span class="tag">You’ve already tried using AI…</span>
<p>But ChatGPT gives you paragraphs of fluffy copy that sounds like marketing without making your offer feel any more desirable.</p>
<p class="want">You want AI that already knows the structure, strategy + psychology behind the page.</p>
</div>
<div class="card r">
<span class="tag">You want to send strangers to your offer…</span>
<p>And you need a page that doesn't depend on someone already knowing who you are.</p>
<p>Whether they find you through your content OR click an ad as a complete stranger…</p>
<p class="want">Your sales page needs to make them want the offer.</p>
</div>
</div>
<div class="cta r center"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">YES - BUILD MINE →</a></div>
</div>
</section>

<!-- SECTION 5: BREAK THEIR CURRENT APPROACH -->
<section data-section="5" data-name="Break their approach" class="s-dark center">
<div class="wrap narrow">
<h2 class="r">Your Problem Isn’t That You Need a <mark>“Better Prompt”</mark></h2>
<div class="stmt r" style="margin-top:30px">
<p>You ask ChatGPT to write your sales page…</p>
<p>Get a giant wall of generic copy…</p>
<p>Then spend forever rewriting it until you’re basically writing the whole freaking page yourself.</p>
</div>
<figure class="fig r" style="--w:520px;margin-top:30px"><img src="images/chatgpt-generic-copy.webp" alt="A ChatGPT prompt asking for a sales page and a generic wall of copy coming back, with an eye-roll emoji" width="1200" height="800" loading="lazy"></figure>
<p class="r" style="font-weight:700;font-size:20px;margin:34px 0 22px">Because generic AI doesn't know:</p>
</div>
<div class="wrap">
<div class="grid g3" style="text-align:left">
<div class="card r" style="--soft:var(--accent)"><span class="num">01</span><p>What your buyer needs to understand first</p></div>
<div class="card r" style="--soft:var(--accent)"><span class="num">02</span><p>Which desire your headline should lead with</p></div>
<div class="card r" style="--soft:var(--accent)"><span class="num">03</span><p>What belief needs to change before they'll buy</p></div>
<div class="card r" style="--soft:var(--accent)"><span class="num">04</span><p>Where your proof belongs</p></div>
<div class="card r" style="--soft:var(--accent)"><span class="num">05</span><p>What objections need to be handled</p></div>
<div class="card r" style="--soft:var(--accent)"><span class="num">06</span><p>How each section should move them closer to BUY NOW</p></div>
</div>
</div>
<div class="wrap narrow">
<p class="reframe r">You don’t need better AI prompts.<br><mark>You need the right sales page strategy built INTO the AI.</mark></p>
<p class="r" style="margin-top:22px;font-size:20px">That's exactly what I created.</p>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">SHOW ME THE BETTER WAY →</a></div>
</div>
</section>

<!-- SECTION 6: THE SOLUTION / WHAT THEY GET (features + bonuses) -->
<section data-section="6" data-name="What they get">
<div class="wrap">
<div class="center">
<h2 class="r">Meet The <mark>Buy-Now Sales Page™</mark></h2>
<p class="lede r">Everything you need to go from:</p>
<div class="flow r"><span>“I have NO idea what my page should say.”</span><span class="arr">→</span><span>“Holy crap. I want to buy my own product.”</span></div>

</div>

<article class="feature r">
<div class="feature-media"><figure class="fig inline" style="--w:640px"><img src="images/14-section-structure.webp" alt="A proven 14-section sales page structure, with sections 1 to 8 listed beside a laptop preview" width="1200" height="800" loading="lazy"></figure></div>
<div class="feature-body"><span class="num-chip">1</span><h3 class=""><mark style="--hl: var(--soft);">The Irresistible Sales Page Structure</mark></h3>
<p>Get the exact sales page structure I use to take someone from interested → convinced → BUY NOW.</p>
<p>Every section has a job.</p>
<p>Every section leads naturally into the next.</p>
<p>And you'll know exactly what belongs where + WHY it's there.</p></div>
</article>

<article class="feature flip r">
<div class="feature-media"><figure class="fig inline" style="--w:560px"><img src="images/ai-tool-mockup.webp" alt="The Buy-Now Sales Page AI Generator on a desktop monitor and a laptop, a form asking about your digital product" width="1200" height="757" loading="lazy"></figure></div>
<div class="feature-body"><span class="num-chip">2</span><h3 class=""><mark style="--hl: var(--soft);">The Custom-Built AI Sales Page Tool</mark></h3>
<p>This isn't a list of prompts you copy into ChatGPT.</p>
<p>I built the actual sales page strategy into the tool.</p>
<p>Give it the details about your offer and it uses my structure to create your sales page for you in about 5 minutes.</p></div>
</article>

<article class="feature r">
<div class="feature-media"><figure class="fig inline" style="--w:640px"><img src="images/organic-cold-traffic.webp" alt="Organic traffic from social platforms and cold traffic from a Meta ad both landing on one sales page" width="1200" height="600" loading="lazy"></figure></div>
<div class="feature-body"><span class="num-chip">3</span><h3 class=""><mark style="--hl: var(--soft);">Built for Organic + Cold Traffic</mark></h3>
<p>Your page shouldn't only make sense to people who already follow you.</p>
<p>The structure is designed to make your offer clear + desirable whether someone comes from your content or discovers you through an ad.</p></div>
</article>

<div class="bonuses r">
<div class="bonus-head"><span class="hand">+ LIMITED TIME BONUSES! 👇</span></div>
<div class="grid g2">
<div class="card bonus"><span class="chip">Bonus</span>
<div class="bonus-media"><figure class="fig inline" style="--w:300px"><img src="images/color-palette-generator.webp" alt="The Color Palette Generator on a tablet" width="1002" height="997" loading="lazy"></figure></div>
<h3 class=""><mark style="--hl: var(--soft);">THE COLOR PALETTE GENERATOR</mark></h3>
<p>Get a ready-to-use 2-color palette that makes your sales page look polished + put together — without guessing which colors actually look good together.</p>
<p>Just add your product + the vibe you want, and get 5 color (or endless!) combinations to choose from with the exact HEX codes.</p></div>
<div class="card bonus"><span class="chip">Bonus</span>
<div class="bonus-media"><figure class="fig inline" style="--w:360px"><img src="images/template-builder-laptop.webp" alt="A laptop showing the done-for-you sales page template open in a page builder" width="1090" height="779" loading="lazy"></figure></div>
<h3 class=""><mark style="--hl: var(--soft);">DONE-FOR-YOU SALES PAGE TEMPLATES</mark></h3>
<p>Skip building your sales page from a blank screen. Pick my ready-made GoHighLevel template, import it into your account + drop in the copy your Buy-Now Sales Page™ creates.</p>
<p>The sections are already built + laid out for you, so you can go from finished copy → live sales page WAY faster.</p></div>
<div class="card bonus featured r"><div class="ft"><span class="chip">Bonus</span><h3><span style="color:var(--on-dark-2)">MASSIVE NEW BONUS:</span> Generate your entire sales page with my custom-built CLAUDE skill</h3><p>(add → click → get your custom sales page just like mine you are reading now)</p>
<p>Use YOUR brand colors or pick a palette I made for you.</p></div><figure class="fig shot" style="--w:620px"><img src="images/buy-now-sales-page-reveal.gif" alt="The finished Buy-Now sales page as you scroll: headlines, highlights, cards and buttons fade in one after another" width="1456" height="821" loading="lazy"></figure></div>
</div>
</div>
<div class="cta r center"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">GIVE ME THE BUY-NOW SALES PAGE →</a></div>
</div>
</section>

<!-- SECTION 7: VALUE + PRICE REVEAL -->
<section data-section="7" data-name="Value + price" class="s-sand" id="buy">
<div class="wrap">
<div class="price r center">
<h2>Get Your Entire Sales Page Done Today for <s>$297</s> <mark>$37</mark></h2>
<p style="font-weight:700;margin:22px 0 6px;text-align:left">Inside The Buy-Now Sales Page™, you get:</p>
<ul class="checks">
<li>My complete Irresistible Sales Page Structure</li>
<li>The custom-built AI Sales Page Tool</li>
<li>The step-by-step system for making your digital product crystal clear + irresistible to buy</li>
<li>A complete page built for organic AND cold ad traffic</li>
<li class="bonus-li">BONUS: The Color Palette Generator</li>
<li class="bonus-li">BONUS: Done-For-You Sales Page Template, ready to import and customize!</li>
<li class="bonus-li">MASSIVE NEW BONUS: Generate your entire sales page with my custom-built CLAUDE skill</li>
</ul>
<div class="instead"><p>And instead of hiring a copywriter…</p><p>Spending days writing it yourself…</p><p class="">Or going back and forth with generic AI trying to get the words right…</p></div>
<p style="font-weight:700;font-size:20px;margin-bottom:6px">You Get The Buy-Now Sales Page™ today for only</p>
<div class="amt" style="margin:0 0 26px"><b style="color:var(--accent)">$37</b></div>
<a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">I WANT ACCESS! →</a>
<p class="fine" style="margin-top:16px">One-Time Payment • Instant Access</p>
</div>
</div>
</section>

<!-- SECTION 8: CORE BELIEF / POSITIONING SHIFT -->
<section data-section="8" data-name="Core belief shift" class="center">
<div class="wrap narrow">
<h2 class="r">What If Your Digital Product <mark>Isn’t the Problem?</mark> 🤔</h2>
<p class="lede r">When people aren't buying, it's easy to think:</p>
<div class="maybes r"><span>Maybe nobody wants this.</span><span>Maybe I need more bonuses.</span><span>Maybe I should lower the price.</span></div>
<div class="stmt r">
<p>But sometimes?</p>
<p>Your offer isn't the problem.</p>
<p class="quote"><mark>People just don't understand why they need it yet.</mark></p>
</div>
<p class="r">Your sales page should take them from:</p>
<div class="flow r"><span>“What is this?”</span><span class="arr">→</span><span>“Wait… I NEED this.”</span></div>
<figure class="fig r" style="--w:600px;margin-top:10px"><img src="images/maybes-to-need-this.webp" alt="Doubts like maybe nobody wants this turning into a sales page that says Wait, I NEED this" width="1200" height="800" loading="lazy"></figure>
<div class="stmt r" style="margin-top:30px">
<p>You don't need to keep adding more value.</p>
<p>You need to make the value already there impossible to miss.</p>
</div>
<p class="r">That's exactly what The Buy-Now Sales Page™ helps you do.</p>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">MAKE MY OFFER IRRESISTIBLE →</a></div>
</div>
</section>

<!-- SECTION 9: CUSTOMER PROOF (strongest testimonials) -->
<section data-section="9" data-name="Customer proof" class="s-paper center">
<div class="wrap">
<h2 class="r">OUR STUDENTS <mark>LOVE OUR PRODUCTS!</mark></h2>
<div class="proofstack">
<div class="swipe-frame wide swipe"><figure class="fig shot r wide has-text" style="--ph:186%"><img src="images/testimonial-gina-karla-brittain.webp" alt="Facebook comment from Gina Karla Brittain: This system changed everything for me. I stopped stressing about posting daily and finally started seeing consistent sales. If you're tired of the content grind, this is 100% worth it." width="1200" height="233" loading="lazy"><blockquote class="tcard"><p>This system changed everything for me. I stopped stressing about posting daily and finally started seeing consistent sales. If you’re tired of the content grind, this is 100% worth it.</p><cite>Gina Karla Brittain</cite></blockquote></figure></div>
<div class="swipe-frame swipe"><figure class="fig shot r has-text" style="--ph:121%;max-width:65.4%;margin:0 auto"><img src="images/testimonial-christina-degiuli.webp" alt="Facebook comment from Christina DeGiuli: The value in the NPSS is easily worth 20x the price! And I should know, I have bought a lot of these types of courses. Thank you Isabelle!" width="785" height="263" loading="lazy"><blockquote class="tcard"><p>The value in the NPSS is easily worth 20x the price! And I should know, I have bought a lot of these types of courses. Thank you Isabelle!</p><cite>Christina DeGiuli</cite></blockquote></figure></div>
<div class="swipe-frame wide swipe"><figure class="fig shot r wide has-text" style="--ph:186%"><img src="images/testimonial-kate-hahn.webp" alt="Facebook comment from Kate Hahn: I'm about halfway through the No-Posting Sales System and have already learned so much. The prompts alone are worth the price of the course! Isabelle clearly has so much knowledge to share!" width="1200" height="196" loading="lazy"><blockquote class="tcard"><p>I’m about halfway through the No-Posting Sales System™ and have already learned so much. The prompts alone are worth the price of the course! 🤩 Isabelle clearly has so much knowledge to share! 💯</p><cite>Kate Hahn</cite></blockquote></figure></div>
</div>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">I WANT ACCESS! (ONLY $37) →</a></div>
</div>
</section>

<!-- SECTION 10: SOCIAL PROOF WALL -->
<section data-section="10" data-name="Social proof wall" class="s-sand center">
<div class="wrap">
<div class="wall">
<div class="swipe-frame wide swipe"><figure class="fig shot r wide has-text" style="--ph:186%"><img src="images/testimonial-lawless-freedom.webp" alt="Facebook comment from Lawless Freedom: You can actually start using this system right away. She is doing exactly what she's teaching. I really appreciate the authenticity and the great work that was put into this." width="1200" height="142" loading="lazy"><blockquote class="tcard"><p>You can actually start using this system right away. She is doing exactly what she's teaching. I really appreciate the authenticity and the great work that was put into this.</p><cite>Lawless Freedom</cite></blockquote></figure></div>
<div class="swipe-frame wide swipe"><figure class="fig shot r wide has-text" style="--ph:186%"><img src="images/testimonial-meg-meg.webp" alt="Facebook comment from Meg Meg: Bought this course a few days ago and wow, it's jam-packed with actionable steps and bonuses. Well worth every penny! Thanks Isabelle. Very well done." width="1200" height="156" loading="lazy"><blockquote class="tcard"><p>Bought this course a few days ago and wow, it's jam-packed with actionable steps and bonuses. Well worth every penny! Thanks Isabelle. Very well done.</p><cite>Meg Meg</cite></blockquote></figure></div>
<div class="swipe-frame"><figure class="fig shot r has-text"><img src="images/testimonial-nicola-havenga.webp" alt="Facebook comment from Nicola Havenga: Got this course and for the first time, I feel like I can actually do this! Posting all the time can be sooooo exhausting. So this is perfect!" width="620" height="280" loading="lazy"><blockquote class="tcard"><p>Got this course and for the first time, I feel like I can actually do this! Posting all the time can be sooooo exhausting. So this is perfect!</p><cite>Nicola Havenga</cite></blockquote></figure></div>
<div class="swipe-frame"><figure class="fig shot r has-text"><img src="images/testimonial-edwina-kiernan.webp" alt="Facebook comment from Edwina Kiernan: Isabelle really does make it step-by-step simple to follow and to follow through on! Looking forward to implementing this!" width="671" height="290" loading="lazy"><blockquote class="tcard"><p>Isabelle really does make it step-by-step simple to follow and to follow through on! Looking forward to implementing this! 🙂</p><cite>Edwina Kiernan</cite></blockquote></figure></div>
<div class="swipe-frame wide swipe"><figure class="fig shot r wide has-text" style="--ph:186%"><img src="images/testimonial-araeya-niaa.webp" alt="Facebook comment from Araeya Niaa: This course is amazing !!! Worth so much more than what I paid! So excited to start my journey" width="1200" height="147" loading="lazy"><blockquote class="tcard"><p>This course is amazing !!! Worth so much more than what I paid! So excited to start my journey 💗</p><cite>Araeya Niaa</cite></blockquote></figure></div>
<div class="swipe-frame wide swipe"><figure class="fig shot r wide has-text" style="--ph:186%"><img src="images/testimonial-clover-hines.webp" alt="Facebook comment from Clover Hines: I bought this sales system a week ago and I must say it's quite unique. It seems very valid in the tactics that are explained and how to execute them! Thank you for knowledge. Its definitely different then the other systems I tend to see online." width="1200" height="189" loading="lazy"><blockquote class="tcard"><p>I bought this sales system a week ago and I must say it’s quite unique. It seems very valid in the tactics that are explained and how to execute them! Thank you for knowledge. Its definitely different then the other systems I tend to see online.</p><cite>Clover Hines</cite></blockquote></figure></div>
</div>
</div>
</section>

<!-- SECTION 11: BIG CLAIM / BIGGER IMPLICATION -->
<section data-section="11" data-name="Big claim" class="s-sand center">
<div class="wrap narrow">
<h2 class="r">Fix Your Sales Page… And Suddenly <mark>A LOT Gets Easier</mark></h2>
<p class="lede r">Think about how many problems get blamed on everything except the sales page.</p>
<figure class="fig r" style="--w:600px"><img src="images/problems-to-buy-now.webp" alt="Four common worries, like my ads are not working, all pointing to one sales page with a Buy Now button" width="1200" height="800" loading="lazy"></figure>
</div>
<div class="wrap narrow">
<div class="claims">
<div class="claim r"><span class="q">“My ads aren't working.”</span><p>But if people are clicking and your page isn't making them want the product…</p><p class="win">More traffic won't fix that.</p></div>
<div class="claim r"><span class="q">“I need a bigger audience.”</span><p>But if your page makes your offer immediately clear to someone who has never heard of you…</p><p class="win">You don't need every buyer to follow you first.</p></div>
<div class="claim r"><span class="q">“Maybe I need to post more.”</span><p>But your sales page should be able to take someone from curious → interested → ready to buy without needing 30 pieces of content to convince them first.</p></div>
<div class="claim r"><span class="q">“Maybe my product just isn't good enough.”</span><p>But if the value isn't crystal clear on the page…</p><p class="win">They don't KNOW how good it is yet.</p></div>
</div>
<div class="stmt r" style="margin-top:48px">
<p>One sales page sits between all that traffic…</p>
<p>…and the BUY NOW button.</p>
<p class="quote"><mark>Make THAT page better.</mark></p>
</div>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">BUILD MY PAGE IN 5 MINUTES →</a></div>
</div>
</section>

<!-- SECTION 12: FOUNDER / AUTHORITY STORY -->
<section data-section="12" data-name="Founder story">
<div class="wrap split flip">
<div class="story">
<span class="hand r" style="margin-bottom:10px">Hi, I'm Isabelle.</span>
<h2 class="r">I Built My Business So My Sales <mark>Didn’t Depend on Me</mark> Showing Up Every Day</h2>
<div class="r">
<p>When I got pregnant with my son, I knew I wanted a business that gave me freedom.</p>
<p>So I built differently.</p>
<p>Within 1.5 years, I sold 37,000+ digital products.</p>
<p>Then I launched Taste O'Freedom + sold 3,000+ courses within a year purely with ads.</p>
<p>Across both businesses, I’ve generated multiple six figures without relying on posting every day.</p>
<p>But sending strangers straight to an offer only works when:</p>
<p class="punch">👉 Your sales page can do the selling.</p>
<p>That’s why I spent years refining my sales page structure, then built it directly into The Buy-Now Sales Page™.</p>
<p>I’ve already done the testing. Now you get the system.</p>
</div>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">STEAL MY SALES PAGE SYSTEM →</a></div>
</div>
<figure class="pol r" style="transform:rotate(3deg)"><span class="tape"></span><img src="images/isabelle-pumpkin-market.jpg" alt="Isabelle smiling and making a peace sign at a pumpkin stand, with her son beside her" width="1435" height="2000" loading="lazy" class="cover"></figure>
</div>
</section>


<!-- SECTION 14: FINAL DESIRE CLOSE (+ footer disclaimers) -->
<section data-section="14" data-name="Final close" class="s-paper center">
<div class="wrap narrow">
<h2 class="r">Ready for a Sales Page You’re <mark>EXCITED</mark> to Send People To?</h2>
<figure class="fig r" style="--w:760px"><img src="images/hero-mockup-v2.png" alt="The Buy-Now Sales Page bundle, built with Claude: the AI sales page tool, the Color Palette Generator, done-for-you templates and payment notifications" width="1851" height="958" loading="lazy"></figure>
<ul class="desires r">
<li><span>✨</span><span>A page that makes someone immediately think: “Ohhh. THAT’S what this does for me.”</span></li>
<li><span>✨</span><span>A page that makes your digital product crystal clear + irresistible to buy.</span></li>
<li><span>✨</span><span>A page you’re confident sending organic traffic + complete strangers from ads to.</span></li>
<li><span>✨</span><span>And one you didn't spend three days arguing with ChatGPT to create.</span></li>
</ul>
<div class="stmt r">
<p>The strategy is already built into the tool.</p>
<p>Give it your offer → get your sales page in about 5 minutes.</p>
<p class="quote"><mark>Get The Buy-Now Sales Page™ today for only <span style="color:var(--accent)">$37</span>.</mark></p>
</div>
<div class="cta r"><a class="btn" href="https://tasteofreedom.com/buy-now-sales-page-checkout">I WANT MY BUY-NOW SALES PAGE!</a><span class="fine">One-Time Payment • Instant Access</span></div>
</div>
</section>

<footer>
<div class="wrap">
<p>Copyrights 2026 | The Buy-Now Sales Page™</p>
<p>This site is not a part of the Facebook website or Facebook Inc.</p>
<p>Additionally, This site is NOT endorsed by Facebook in any way.</p>
<p>FACEBOOK is a trademark of FACEBOOK, Inc.</p>
<p>Results shown on this page are for example purposes only. We do not guarantee you will achieve any specific results. Your results will vary and depend on many factors, including your work ethic and experience level. The average person who buys any “how to” information gets little to no results. All business involves risk as well as massive and consistent action and effort. If you’re not willing to accept that, do not buy this course</p>
<p>Due to the nature of the product, we do not offer any refunds.</p>
</div>
</footer>
`````

### FILE: kit/4-build/export_final.py

`````
#!/usr/bin/env python3
"""Make the final page, and a paste-ready version for page builders (Kajabi, GoHighLevel, Systeme.io, ...).

usage:
  python3 export_final.py --in index.html --out-dir export [--images keep|embed|urls] [--urls image-urls.json]

--in         the draft made by build_page.py, or the file saved with "Save draft" from the layout editor
--out-dir    folder for the results
--images     how the paste-ready file handles images:
               keep   leave "images/xyz.webp" as they are (the page needs the images folder beside it)
               embed  build every image into the file (one paste, but big: keep the total under about 2.5 MB)
               urls   point images at links you got after uploading them to your platform (see --urls)
--urls       a JSON file like {"hero.png": "https://.../hero.png"} for the "urls" mode. Any image that has a link
             is used from its link in every mode; images without a link follow --images.

Results:
  index-final.html   the page without the editor (open in a browser, or publish as a file)
  paste-ready.html   the code to paste into an HTML / custom code block (plain ASCII, styles stay inside the page)
  export-report.txt  what was done and what to check

Only the Python standard library is used.
"""
import argparse
import base64
import json
import mimetypes
import os
import re
import sys

PIXEL = 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='


def strip_editor(h):
    h = re.sub(r'<script id="layout-editor">.*?</script>\s*', '', h, flags=re.S)
    h = re.sub(r'<style id="editor-css">.*?</style>\s*', '', h, flags=re.S)
    h = re.sub(r'<script type="application/json" id="layout-edits-data">.*?</script>\s*', '', h, flags=re.S)
    h = re.sub(r'\sdraggable="(?:true|false)"', '', h)
    h = h.replace(' ed-selected', '').replace('ed-selected ', '')

    def fix_class(m):
        toks = m.group(1).split()
        if 'r' in toks and 'in' in toks:          # never save the "already revealed" state: the scroll effect must replay
            toks = [t for t in toks if t != 'in']
        return 'class="%s"' % ' '.join(toks)
    h = re.sub(r'class="([^"]*)"', fix_class, h)
    h = re.sub(r'<html([^>]*?)\sclass="[^"]*"', r'<html\1', h)
    return h


# ---- scope the page css so it cannot touch the host page ----
def scope_selector(s):
    s = s.strip()
    if not s or s.startswith('#page') or s.startswith(':root') or s == 'html':
        return s
    if s == 'body':
        return '#page'
    if s.startswith('.anim '):
        return '.anim #page ' + s[6:]
    return '#page ' + s


def split_commas(sel):
    out, depth, cur = [], 0, ''
    for ch in sel:
        if ch in '([':
            depth += 1
        if ch in ')]':
            depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur)
            cur = ''
        else:
            cur += ch
    out.append(cur)
    return out


def scope_css(css):
    out, i, n = '', 0, len(css)
    while i < n:
        if css[i].isspace():
            out += css[i]
            i += 1
            continue
        if css.startswith('/*', i):
            i = css.index('*/', i) + 2
            continue
        j = css.index('{', i)
        head = css[i:j]
        depth, k = 1, j + 1
        while depth:
            depth += {'{': 1, '}': -1}.get(css[k], 0)
            k += 1
        body = css[j + 1:k - 1]
        if head.strip().startswith('@'):
            if head.strip().startswith(('@media', '@supports')):
                out += head + '{' + scope_css(body) + '}'
            else:
                out += head + '{' + body + '}'
        else:
            out += ','.join(scope_selector(x) for x in split_commas(head)) + '{' + body + '}'
        i = k
    return out


HARDEN = '''
/* protect the page from the host page's own styles */
#page h1,#page h2,#page h3,#page p,#page li,#page span,#page div,#page a,#page figure,#page blockquote,#page cite,#page b,#page strong{color:inherit}
#page section{border:0;background:transparent}
#page img{border:0}
'''


def esc_html(t):
    return ''.join(c if ord(c) < 128 else '&#x%X;' % ord(c) for c in t)


def esc_css(t):
    return ''.join(c if ord(c) < 128 else '\\%X ' % ord(c) for c in t)


def esc_js(t):
    o = ''
    for c in t:
        if ord(c) < 128:
            o += c
        elif ord(c) > 0xFFFF:
            v = ord(c) - 0x10000
            o += '\\u%04X\\u%04X' % (0xD800 + (v >> 10), 0xDC00 + (v & 0x3FF))
        else:
            o += '\\u%04X' % ord(c)
    return o


def ascii_safe(doc):
    parts = re.split(r'(<style[^>]*>.*?</style>|<script[^>]*>.*?</script>)', doc, flags=re.S)
    return ''.join(esc_css(x) if x.startswith('<style') else esc_js(x) if x.startswith('<script') else esc_html(x) for x in parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='src', required=True)
    ap.add_argument('--out-dir', default='export')
    ap.add_argument('--images', choices=['keep', 'embed', 'urls'], default='keep')
    ap.add_argument('--urls')
    a = ap.parse_args()

    base_dir = os.path.dirname(os.path.abspath(a.src))
    os.makedirs(a.out_dir, exist_ok=True)
    final = strip_editor(open(a.src, encoding='utf-8').read())
    open(os.path.join(a.out_dir, 'index-final.html'), 'w', encoding='utf-8').write(final)

    urls = json.load(open(a.urls)) if a.urls else {}
    styles = re.findall(r'<style[^>]*>(.*?)</style>', final, re.S)
    css = scope_css('\n'.join(styles)) + HARDEN
    def nonblocking(tag):
        # speed: the Google Fonts stylesheet must not hold up the first paint
        if 'fonts.googleapis.com/css' in tag and 'rel="stylesheet"' in tag:
            href = re.search(r'href="([^"]+)"', tag).group(1)
            return ('<link rel="preload" as="style" href="%s" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
                    '<noscript><link rel="stylesheet" href="%s"></noscript>' % (href, href))
        return tag
    links = ''.join(nonblocking(m) + '\n' for m in re.findall(r'<link[^>]*>', final))
    body = re.search(r'<body[^>]*>(.*)</body>', final, re.S).group(1).strip()

    imgs = sorted(set(re.findall(r'images/([^"\' )]+)', body)))
    report, missing, embedded_bytes, dup = [], [], 0, False
    for f in imgs:
        key = 'images/' + f
        if f in urls:
            body = body.replace(key, urls[f])
            report.append('  %-40s -> your link' % f)
            continue
        if a.images == 'keep':
            continue
        if a.images == 'urls':
            body = body.replace(key, 'PASTE-YOUR-LINK-FOR-' + f)
            missing.append(f)
            continue
        path = os.path.join(base_dir, 'images', f)
        if not os.path.exists(path):
            report.append('  %-40s MISSING FILE, left as is' % f)
            continue
        data = open(path, 'rb').read()
        mt = mimetypes.guess_type(f)[0] or 'image/webp'
        uri = 'data:%s;base64,%s' % (mt, base64.b64encode(data).decode())
        embedded_bytes += len(uri)
        tag = '<img src="images/%s"' % f
        if body.count(tag) > 1:        # same picture used twice: embed once, fill the copy with a tiny script
            i = body.index(tag)
            body = body[:i] + '<img data-k="%s" src="%s"' % (f, uri) + body[i + len(tag):]
            body = body.replace(tag, '<img data-from="%s" src="%s"' % (f, PIXEL))
            dup = True
        else:
            body = body.replace(key, uri)
        report.append('  %-40s embedded (%d KB)' % (f, len(data) // 1024))
    if dup:
        body += '\n<script>document.querySelectorAll("img[data-from]").forEach(function(i){var s=document.querySelector("img[data-k=\\""+i.getAttribute("data-from")+"\\"]");if(s)i.src=s.src;});</script>\n'

    preload = ''
    imgm = re.search(r'<img\b[^>]*>', body)
    if imgm and 'fetchpriority="high"' in imgm.group(0):
        u = re.search(r'\ssrc="(https?://[^"]+)"', imgm.group(0))
        if u:
            preload = '<link rel="preload" as="image" href="%s" fetchpriority="high">\n' % u.group(1)
    out = '<!-- Sales page: paste into an HTML / custom code block -->\n' + links + preload + '<style>\n' + css + '\n</style>\n' + body + '\n'
    out = ascii_safe(out)
    pr = os.path.join(a.out_dir, 'paste-ready.html')
    open(pr, 'w', encoding='ascii').write(out)
    size = os.path.getsize(pr)

    lines = ['Export report', '=============', 'paste-ready.html: %.2f MB' % (size / 1e6), 'image mode: ' + a.images, '']
    lines += report or ['(no image changes)']
    if missing:
        lines += ['', 'UPLOAD THESE to your platform, then add their links to image-urls.json and run this again:'] + ['  ' + m for m in missing]
    if size > 2.5e6:
        lines += ['', 'WARNING: this paste is over 2.5 MB. Some builders refuse or break above this. Use --images urls with uploaded images.']
    if a.images == 'embed' and not urls and size > 2.0e6:
        lines += ['', 'Tip: very large images are better uploaded to your platform and used by link.']
    lines += ['', 'Files: index-final.html (no editor), paste-ready.html (for the code block).']
    open(os.path.join(a.out_dir, 'export-report.txt'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
`````

### FILE: kit/4-build/font-fallbacks.json

`````
{
 "_note": "Width of each Google font compared with Arial (regular and bold), measured in Chrome on 2026-10-29. build_page.py uses it to make a stand-in font of the same width, so text does not jump when the web font loads.",
 "fonts": {
  "Abril Fatface": {
   "400": 1.0283,
   "700": 0.9524
  },
  "Albert Sans": {
   "400": 1.0394,
   "700": 0.9791
  },
  "Alfa Slab One": {
   "400": 1.2116,
   "700": 1.1221
  },
  "Anton": {
   "400": 0.914,
   "700": 0.8466
  },
  "Archivo Black": {
   "400": 1.2483,
   "700": 1.1562
  },
  "Assistant": {
   "400": 0.9244,
   "700": 0.9082
  },
  "Baloo 2": {
   "400": 0.9579,
   "700": 0.9363
  },
  "Barlow": {
   "400": 0.9679,
   "700": 0.9228
  },
  "Be Vietnam Pro": {
   "400": 1.0998,
   "700": 1.0595
  },
  "Bitter": {
   "400": 1.037,
   "700": 0.9817
  },
  "Bodoni Moda": {
   "400": 1.0377,
   "700": 1.0162
  },
  "Bricolage Grotesque": {
   "400": 1.0585,
   "700": 1.0207
  },
  "Cabin": {
   "400": 0.9489,
   "700": 0.902
  },
  "Crimson Pro": {
   "400": 0.8981,
   "700": 0.8872
  },
  "DM Sans": {
   "400": 1.0492,
   "700": 1.0297
  },
  "DM Serif Text": {
   "400": 0.9904,
   "700": 0.9173
  },
  "EB Garamond": {
   "400": 0.8584,
   "700": 0.8734
  },
  "Epilogue": {
   "400": 1.1053,
   "700": 1.0732
  },
  "Figtree": {
   "400": 1.0113,
   "700": 0.9654
  },
  "Fraunces": {
   "400": 1.0567,
   "700": 1.0458
  },
  "Fredoka": {
   "400": 1.011,
   "700": 0.947
  },
  "Gloock": {
   "400": 1.0202,
   "700": 0.9449
  },
  "Hanken Grotesk": {
   "400": 1.0057,
   "700": 0.9478
  },
  "Hind": {
   "400": 0.9629,
   "700": 0.9483
  },
  "IBM Plex Sans": {
   "400": 1.0155,
   "700": 0.9871
  },
  "Instrument Sans": {
   "400": 1.0232,
   "700": 0.9877
  },
  "Instrument Serif": {
   "400": 0.7602,
   "700": 0.7041
  },
  "Inter": {
   "400": 1.0685,
   "700": 1.0243
  },
  "Josefin Sans": {
   "400": 1.0181,
   "700": 1.001
  },
  "Karla": {
   "400": 1.0314,
   "700": 1.0008
  },
  "Lato": {
   "400": 0.973,
   "700": 0.9229
  },
  "Lexend": {
   "400": 1.0991,
   "700": 1.0822
  },
  "Libre Baskerville": {
   "400": 1.1572,
   "700": 1.0986
  },
  "Libre Caslon Text": {
   "400": 1.0667,
   "700": 1.0783
  },
  "Lora": {
   "400": 1.0539,
   "700": 1.0058
  },
  "Manrope": {
   "400": 1.0309,
   "700": 1.0092
  },
  "Marcellus": {
   "400": 1.0251,
   "700": 0.9494
  },
  "Merriweather": {
   "400": 1.0834,
   "700": 1.0327
  },
  "Montserrat": {
   "400": 1.1262,
   "700": 1.1004
  },
  "Mukta": {
   "400": 0.9399,
   "700": 0.918
  },
  "Mulish": {
   "400": 1.0373,
   "700": 0.9964
  },
  "Newsreader": {
   "400": 0.9528,
   "700": 0.9555
  },
  "Nunito": {
   "400": 1.0124,
   "700": 0.9759
  },
  "Nunito Sans": {
   "400": 1.0118,
   "700": 0.9748
  },
  "Open Sans": {
   "400": 1.0485,
   "700": 1.0464
  },
  "Oswald": {
   "400": 0.8196,
   "700": 0.8623
  },
  "Overpass": {
   "400": 1.0083,
   "700": 0.9797
  },
  "Playfair Display": {
   "400": 1.0165,
   "700": 0.9648
  },
  "Plus Jakarta Sans": {
   "400": 1.0533,
   "700": 1.0119
  },
  "Poppins": {
   "400": 1.1256,
   "700": 1.0785
  },
  "Public Sans": {
   "400": 1.045,
   "700": 0.9971
  },
  "Quicksand": {
   "400": 1.0392,
   "700": 1.0164
  },
  "Raleway": {
   "400": 1.0376,
   "700": 0.9988
  },
  "Red Hat Text": {
   "400": 1.0001,
   "700": 1.0275
  },
  "Roboto": {
   "400": 0.9989,
   "700": 0.9434
  },
  "Roboto Slab": {
   "400": 1.0616,
   "700": 0.996
  },
  "Rozha One": {
   "400": 1.0504,
   "700": 0.9729
  },
  "Rubik": {
   "400": 1.0529,
   "700": 1.0454
  },
  "Rufina": {
   "400": 1.0478,
   "700": 0.9832
  },
  "Shrikhand": {
   "400": 1.1967,
   "700": 1.1083
  },
  "Sora": {
   "400": 1.1386,
   "700": 1.0757
  },
  "Source Sans 3": {
   "400": 0.932,
   "700": 0.916
  },
  "Space Grotesk": {
   "400": 1.098,
   "700": 1.0211
  },
  "Spectral": {
   "400": 0.999,
   "700": 0.9651
  },
  "Syne": {
   "400": 0.9835,
   "700": 1.1347
  },
  "Urbanist": {
   "400": 0.9785,
   "700": 0.9387
  },
  "Work Sans": {
   "400": 1.1245,
   "700": 1.0469
  },
  "Young Serif": {
   "400": 1.1271,
   "700": 1.0439
  }
 }
}
`````

### FILE: kit/4-build/make_bundle.py

`````
#!/usr/bin/env python3
"""Make ONE file with the whole kit inside, for normal Claude chat (where a folder cannot be attached).

usage:  python3 make_bundle.py   (run from the sales-page-generator-kit folder; writes START-HERE-SINGLE-FILE.md)
The instruction file stays first. Every kit file follows in a "KIT FILES" section; Step 0 tells Claude to write them out.
"""
import os, sys
if len(sys.argv) > 1:
    print(__doc__)
    sys.exit(0)
root =os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
kit = os.path.join(root, 'kit')
out = open(os.path.join(root, 'START-HERE.md'), encoding='utf-8').read().rstrip() + '\n\n---\n\n## KIT FILES\n\nWrite each file below to the path shown (create folders as needed), exactly as written, then continue with Step 0.\n'
for d, _, files in sorted(os.walk(kit)):
    for f in sorted(files):
        if f.endswith(('.pyc', '.DS_Store')) or '__pycache__' in d:
            continue
        p = os.path.join(d, f)
        rel = os.path.relpath(p, root).replace(os.sep, '/')
        out += '\n### FILE: %s\n\n`````\n%s\n`````\n' % (rel, open(p, encoding='utf-8').read().rstrip())
dest = os.path.join(root, 'START-HERE-SINGLE-FILE.md')
open(dest, 'w', encoding='utf-8').write(out)
print('wrote', dest, len(out.encode('utf-8')) // 1024, 'KB')
`````

### FILE: kit/4-build/reference-phrases.txt

`````
# Text that belongs to the reference example (Isabelle's own page).
# check_page.py flags any of these if they show up on a client's page.
Buy-Now
Isabelle
Taste O'Freedom
tasteofreedom
Color Palette Generator
37,000
3,000+ courses
6,000+
$297
GoHighLevel template
CLAUDE skill
Lawless Freedom
Meg Meg
Araeya Niaa
Gina Karla Brittain
Nicola Havenga
Christina DeGiuli
Edwina Kiernan
Kate Hahn
Clover Hines
homeschool
buy-now-sales-page-checkout
`````

### FILE: kit/4-build/sections.md

`````
# Layout for each section (what to build, which classes to use)

Page shell: you write only the sections. `build_page.py` wraps them in `<div id="page">` and adds the look, the scroll effects and the editor.
Each section: `<section data-section="N" data-name="..." class="...">` then `<div class="wrap">` (or `wrap narrow` for a centered column, `wrap split` for two columns).
Put `class="r"` on blocks that should fade up as the page scrolls (headings, paragraphs, cards, figures, buttons). Never add the class `in` yourself.
Section backgrounds alternate: none (page color), `s-paper` (white), `s-sand` (soft band), and one `s-dark` band.
Buttons: `<div class="cta r"><a class="btn" href="CHECKOUT LINK">Label from the copy</a></div>`; under the main one add `<span class="fine">One-Time Payment • Instant Access</span>` only if the client confirmed it (question 21).
Highlighter: wrap the key phrase of a heading in `<mark>`. A replaced price: `<s>$297</s>`. Handwritten note: `<span class="hand">...</span>`. Section headings are `<h2 class="r">`, small ones `<h3>`.
Images: `<figure class="fig r"><img src="images/x.webp" alt="what is visible" width="W" height="H" loading="lazy"></figure>`; proof screenshots use `fig shot`; set a max width with `style="--w:520px"`.
Never put a section label on the page. Every section opens with its real headline.

| # | Section | Layout |
|---|---|---|
| 1 | Big desire headline | `section.hero.center` > `.wrap`: `.trust` pill (only if the client gave a real trust line) + `h1` (key phrase in `<mark>`) + `p.lede` (one `<span class="pss">` for a bold italic underlined key phrase) + `p.note > span.hand` (the objection remover) + `.cta` + the top mockup figure. |
| 2 | Belief shift + outcomes | `s-paper center` > `.wrap.narrow`: `h2`, `.stmt` with statement lines (the "you don't need" lines start with `<svg class="ico ico-x">` red hand-drawn X; the "you need" line starts with `<svg class="ico ico-ok">` green check; the big quote is `p.quote > mark`), then a lead-in line that names the product or method ("With the [name], you'll get:", never a bare "You'll get:"), then `.outcomes` with one `.outcome` per outcome (`span.n` number + `p`), then `.cta`. |
| 3 | Origin story | `.wrap.narrow`: proof figure (`fig shot`, margin-bottom 48px) above, then `.story`: `h2`, `div.r` of paragraphs (`p.punch` for the key line, `span.hand` for quoted thoughts), then `.cta`. |
| 4 | Who this is for | `s-sand who`: `h2`, `.grid.g2` of `.card` (`span.tag` = the person, `p` = what they want and don't want, `p.want` = what they want), then `.cta`. |
| 5 | Break their approach | `s-dark center`: `h2`, `.stmt` lines, optional illustration figure, `.grid.g3` of `.card` (`span.num` + `p`), then `p.reframe > mark` (the core reframe), then `.cta`. |
| 6 | What they get | heading + a lead-in line `<p class="r" style="font-weight:700;font-size:20px">Everything you need to go from:</p>` + `.flow` ("from" and "to" chips with `span.arr`) + optional wide figure; then one `article.feature` per component (`.feature-media > figure.fig.inline`, `.feature-body` with `span.num-chip`, `h3`, paragraphs); alternate with `article.feature.flip`; then `.bonuses` (`.bonus-head > span.hand`, `.grid.g2` of `.card.bonus` with `span.chip`, `.bonus-media > figure.fig.inline`, `h3`, paragraphs). A feature with no image: `article.feature.no-media` (one column). A missing image of any kind: `<figure class="fig"><div class="ph">Image goes here</div></figure>`. An extra big bonus: `.card.bonus.featured` with `.ft` (chip, h3, p) beside a figure. Then `.cta`. |
| 7 | Value + price | `s-sand#buy`: `.price.center` card: `h2` with `<s>regular</s> <mark>today</mark>`, `ul.checks` (bonuses get `class="bonus-li"`), `.instead` lines, `.amt > b` big price, button, `p.fine`. |
| 8 | Core belief shift | `center .wrap.narrow`: `h2` ("What if the problem isn't ..."), `.maybes` (handwritten doubts), `.stmt` lines with a `p.quote`, `.flow`, optional illustration, `.cta`. |
| 9 | Customer proof | `s-paper center`: `h2`, `.proofstack` of the strongest 3 testimonials, each `div.swipe-frame` > `figure.fig.shot.has-text`, then `.cta`. |
| 10 | Social proof wall | `s-sand center`: `.wall` of the other testimonials (`div.swipe-frame.wide` for wide ones). No heading unless the copy has one. |
| 11 | Bigger implication | `s-sand center`: `h2`, `p.lede`, optional illustration, `.claims` of `.claim` (`span.q` handwritten doubt, `p` reason, `p.win`), closing `.stmt` with `p.quote`, `.cta`. |
| 12 | Founder story | `.wrap.split.flip`: `.story` (`span.hand` greeting, `h2`, paragraphs, `p.punch`, `.cta`) beside `figure.pol` (owner photo with a `span.tape`). |
| 13 | More proof | Same pattern as 9 or 10, or the owner's results shown whole. Skip it if there is nothing to show. |
| 14 | Final desire close | `s-paper center .wrap.narrow`: `h2`, mockup figure, `ul.desires` (4 `li`), `.stmt` lines with `p.quote`, `.cta`; then `<footer>` with the disclaimers, word for word from the client. |

Footer: `<footer><div class="wrap"><p>...</p></div></footer>` after the last section. Disclaimers are the client's. If they gave none, put a clearly marked note in the page for them to fill in.

Grids adapt on their own: 1, 2, 3, 4 or 5 cards in `.g2`, `.g3`, `.wall` or `.outcomes` always fill their rows, so never pad with filler cards and never leave a gap. Small hand-drawn doodles and squiggle underlines are added by the CSS. Every section should still feel full: use a figure, flow chips or an icon where the copy gives you a natural place for one, but never invent content.

Mobile and motion are built in: columns stack, buttons go full width, sections fade up once, the highlighter sweeps in, the X and check icons draw themselves. Do not add your own CSS unless something truly cannot be done with these classes. If you must, add a small `<style>` block at the top of body.html with a comment saying why.
`````

### FILE: kit/5-publish/publish-guide.md

`````
# Publishing the page (any builder that accepts HTML)

The page is one block of HTML. It works in Kajabi, GoHighLevel, Systeme.io and any builder with a custom code / HTML block. The steps below are the same idea everywhere; the menu names differ, so look for a block called Custom Code, Custom HTML, HTML, or Code.

## Pick the image mode first
Run `export_final.py` with one of these:
- `--images embed`: every image is built into the file. One paste, nothing to upload. Only for pages whose paste stays under about 2.5 MB (the report tells you).
- `--images urls`: images are used from links. The client uploads the pictures to their platform's media library, copies each link, and Claude adds them to `my-sales-page/image-urls.json` like `{"hero.png": "https://..."}`. Then run the export again with `--urls my-sales-page/image-urls.json`.
- Mixed (best for most pages): embed the small images, upload only the big ones. Any image that has a link in `image-urls.json` is used by link; the rest follow `--images embed`. Upload the biggest ones first (mockups, GIFs).

Lessons from the first real page:
- A paste of about 2.8 MB loaded. A paste of 3.5 MB had images missing in GoHighLevel. Keep it under 2.5 MB to be safe.
- A very large single image (about 1 MB) is better hosted than embedded.
- A hosted image link that works when opened alone in a browser can still fail inside a builder. If an image does not show after pasting, use the embedded version of that image, or re-upload it under a new name, and tell Claude what you see.
- Always test the pasted page on desktop and on a phone.

## Steps
1. Open the page or funnel step in the builder, on a blank page.
2. Make a full-width area: a section set to full width, with padding and margin at 0, a row with one column, also full width and 0 padding. (Names differ by builder. The page needs the whole screen width.)
3. Add a Custom Code / HTML block to that column and open its code editor.
4. Open `export/paste-ready.html` in a text editor, select all, copy, paste into the code editor, and save the block. (Claude can copy the file to your clipboard for you if you ask.)
5. Replace any old code in the block: click inside, select all (Cmd+A or Ctrl+A), then paste.
6. Save the page. If it is published, publish again.
7. Hard refresh the page (Cmd+Shift+R or Ctrl+Shift+R) or open it in a private window, then check desktop and phone.

## If something looks wrong
- Nothing changed: the old code is still there, the block was not saved, or the page was not published again. Hard refresh. Search the page for a phrase from your newest change (Cmd+F or Ctrl+F).
- Page is narrow or has side margins: the section, row or column is not full width with 0 padding.
- White strips left and right on a phone: the builder pads the code block on mobile. The page already stretches itself to the full screen width on phones and tablets, so a strip that is still there is usually the builder's own section, row or column padding or background color. Set the mobile padding on the section, row and column to 0 and give them the same background color as the page's first section, then save, publish and hard refresh.
- Strange symbols: use `paste-ready.html`, never `index.html`. It is plain text with no special characters inside.
- Images missing: check the paste size in the export report, then see the image-mode notes above.
- Buttons go nowhere: check the checkout link in the copy. Every button uses it.

## Changing the page later
Open `index.html` (the draft with the editor) in a browser, change it, click "Save draft", move the saved file into `my-sales-page`, and ask Claude to run the export again. Do not edit `paste-ready.html` by hand.
`````
