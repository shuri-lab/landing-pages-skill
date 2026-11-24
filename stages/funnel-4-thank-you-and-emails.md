# Funnel stage F4 of F5: Thank-you page and delivery emails

**Goal:** every buyer knows the first thing to do within seconds, and each product arrives by its own email.

## The thank-you page
1. Build and check as in F2. Output: `dist/thank-you.html`.
2. It has: ✓ and "You're in", two or three numbered steps with one action each, an optional community step, a short quote from the founder (only words they said or approved; otherwise leave it out), a help line. **It never sells.**
3. Rules:
   - **Public page: no paid file links.** Say where the file is ("inside your course, in the first lesson").
   - Every link lives in `links` in the JSON. An empty one shows a grey button with a note, so the page can go up before every link exists. Fill them all before real traffic.
   - The page can't know what was bought, so the bump and the upsell appear only inside a question: "Added [Bump] or [Upsell]? They're in the same place, next to your course."
   - First-time login: "First time? Tap 'Open my course' in the email I just sent you. It signs you in."
   - Community: the channel's real picture, one button, and its QR code **on desktop only** (a phone can't scan itself).
   - Face photos in circles: set `photo_position` (e.g. `"50% 0"`) and look at the screenshot so the face isn't cut.

## The emails
1. One email per product: `main`, `bump`, and each upsell slug. GHL can't show a paragraph only to bump buyers, so separate emails are the only safe way.
2. **The main email goes to everyone.** It never names the bump or the upsell (the build fails if it does).
3. Links in the JSON: `[Open my course](login)` becomes GHL's one-click sign-in link, `[log in here](course)` uses `links.course`, `[Join](community)` uses `links.community`. Any key must exist in `links` (Rickey's uses `whatsapp`). An empty link becomes plain bold text, so **check every email again after the links are filled**. The sign-in link works for 24 hours; the first time it asks the buyer to choose a password.
4. Pattern: subject = the win plus the first step ("You're in. Here's Day 1"). Preview = what's inside. Then a numbered list of what they got with one link each, one action for today with the time it takes, the founder's first name, and a P.S. with a real way to get help.
5. `emails.from_name`: the founder. In the founder's voice. No badges, no "Congratulations on enrolling in our program": GHL sends its own messages like that unless they're turned off (GHL Funnel Playbook, Stage 10).
6. Look at `preview/emails.html`, then get the person's yes on each email.

## Done when
- [ ] Thank-you passes at both sizes; every link is filled or listed as open.
- [ ] Each product has its email; the person approved the texts and who they come from.
