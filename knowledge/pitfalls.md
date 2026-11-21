# Pitfalls and fixes

Things that went wrong while building the Rickey page, and the fix. Read before Stage 5; check again in Stage 6.

1. **No GitHub access to the reference repo** (`gh` missing, no connector) → study the live page via browser JS instead (F). For a playbook: ask for the reference repo or a local clone up front.
2. **A command ran in the wrong folder**, so the rules went into a stray `learned-rules.md` next to the kit → it was moved and deleted. Use absolute paths, or `cd` explicitly in each command.
3. **A JS check timed out (45s)** while awaiting `img.decode()` with the browser pane hidden → don't await decode or other long promises. Check `img.complete`/`naturalWidth` instead.
4. **`location.reload()` inside a JS call** cut the script off and lost its return value → reload in one call and measure in the next.
5. **Blank images in screenshots** (a 1.9 MB PNG still decoding, or lazy images after a jump) → set `loading='eager'` and wait 1-2s, and confirm `naturalWidth` before calling it a bug.
6. **The generator asserted a removed token** (`@@LOGOS@@`) and the build failed → make replacements tolerant and assert only that no `@@` is left.
7. **A max-content slider widened its grid column** (page 2051px wide at 1280) → `min-width:0` on grid children.
8. **Old padding rules fought a new design** (the offer's dark header looked inset at both breakpoints) → when restyling a component, search all its rules (base, phone, desktop) and neutralize the old ones (`.offer{padding:0}`, padding moved to `.offer-body`).
9. **A leftover `<br>`** made a blank line once the title became `display:block` → `p br{display:none}`.
10. **Sliders ran out on wide screens** → the `fill()` doubling JS, plus capping the video carousel width.
11. **A sticky side column taller than the screen** hid content → remove `position:sticky` when the column grows.
12. **Hero too tight after squeezing it above the fold** (round 1) → set font-size floors (B3). Above the fold still held at btn 764 / fine 795.
13. **Desktop was neglected** while phone was perfected → rework desktop explicitly (two-column hero, bigger type, outcome grid) and check at 1280, 1440 and 1920.
14. **The offer listed items that aren't included** (templates, "both milestone playbooks") → check against the client's latest list and recompute the totals ($230 → $201, save $174).
15. **Conflicting source documents** (an older offer ladder or PDF) → report the conflict, follow the client, and record the decision in `learned-rules.md` so it isn't undone later.
16. **Fake urgency copied from the reference** → don't copy "Today only" without a real deadline.
17. **Relative dates from social posts** ("7 years ago") go stale → leave them out.
18. **Placeholders blocking go-live** → remove the empty spots, drop sections without assets, and draft disclaimers for approval so the check passes.
19. **Rewriting the founder story** (twice) → the client said "Have the copy as it was before. Don't make any changes." Restore from the backup with one splice, keep only the photos and styling, and write the override rule. Prevention: when the client shares source material, offer it as a separate draft or a single added line for approval, and never restructure approved story copy.
20. **Claude-written lines slipping in unflagged** → every round's wrap-up marked its own wording ("These lines are mine, so please check them").
21. **AI image issues** (a missing image, a Nike swoosh, a wrong image for a product, a white box) → see E3.
22. **Possible stock photo of the founder, shown twice** → flag the license and the duplicate before going live.
23. **(Repo step) SSH key not on GitHub** → try HTTPS through the keychain (`GIT_TERMINAL_PROMPT=0 git push https://…`) and verify with `git ls-remote`. Pages shows 404 until it's enabled under Settings → Pages. Scan for secrets and files over 50 MB before pushing a public repo, and get the client to confirm what goes public (transcripts, research, the Getty photo).

## More pitfalls (sharing, speed, checkout, upsell)

| # | Pitfall | Fix / rule |
|---|---|---|
| 1 | SSH push failed: "Permission denied (publickey)" | Try HTTPS with the keychain: `GIT_TERMINAL_PROMPT=0 git push https://…`; switch the remote to HTTPS |
| 2 | Push rejected after Pages was enabled | Pages setup made CNAME create/delete commits. `git fetch`, inspect with `git log HEAD..origin/main`, then `git pull --rebase` and push |
| 3 | New file 404s / old content served for ~1 min after push | Poll with `?r=$i` and a content marker; don't trust a fixed sleep |
| 4 | Loader injected GitHub's 404 page into the checkout | `if(!r.ok) throw` + `.catch(function(){})` in every loader |
| 5 | Injected scripts don't run | Re-create each `<script>` node after `innerHTML` |
| 6 | Clipboard paste never reached the browser pane; huge typing is risky | Keep builder code tiny (the loader). Check that typing works and the editor doesn't auto-close tags with a test string first |
| 7 | 20px white strip above a fragment | Builder sections are `div.section-*`; add `[class*="section-"]:has(#root)` |
| 8 | Blank tab title | Set `document.title` inside the fragment |
| 9 | Resource Timing shows 0 KB for cross-origin images | No `Timing-Allow-Origin` header; compute weight from local files or use DevTools |
| 10 | No image tools; `sips` can't write WebP | venv + Pillow (ask before installing). The kit suggests `my-sales-page/.tools` for the venv |
| 11 | Optimizer names files by requested width even when the original is smaller | Name by the actual output width |
| 12 | Lazy images in horizontal marquees never load | IntersectionObserver switches them to `eager` at 600px rootMargin |
| 13 | Duplicate carousel cards download each video twice | Duplicates wait for the original's `loadeddata`, then use the cached file |
| 14 | `f_auto` changes format by browser, so measurements vary | Measure with a real browser UA; omit the extension on the video URL |
| 15 | Swift PDF renderer broke (SDK/compiler mismatch) | pypdf `page.images` → PIL contact sheet; pypdf `extract_text()` for counts |
| 16 | Upsell image overflowed phones | A more specific `max-width:760px` beat `max-width:100%`; use `width:100%;max-width:760px`; run the overflow finder |
| 17 | Flex `li` with `<b>` split into columns | Wrap the li content in one `<span>` |
| 18 | Bump image stacked above the text; text squeezed | `display:contents` on the bump body; image inside the description, floated right |
| 19 | Builder right-aligned the bump's OTO line | `text-align:left!important` on headline/OTO/description |
| 20 | Double divider above the total | Remove the summary's top border |
| 21 | Injected bump banner/arrow/image vanished on re-render | Idempotent `enhance()` + interval + MutationObserver |
| 22 | The builder's bump image field is upload-only (no uploads from the browser pane) | Inject the image from the static host by script |
| 23 | `cmd+a` didn't select in builder fields, so new text was appended to old | Clear with End or cmd+Down + many Backspace/Delete, then zoom to verify before saving |
| 24 | Paraphrased guarantee in the checkout | Always pull guarantee/offer wording verbatim from `copy.md` |
| 25 | Bump copy v2 too long, too many numbers | One pain + one number + one promise |
| 26 | Made-up stack values | Label them placeholders in the report; ask the client to approve |
| 27 | README and `learned-rules.md` went stale (still say originals, bump on page, checkout placeholder) | Update both in the same commit as each feedback round |
| 28 | Thank-you fragment still uses `images/rickey-bestbuy.jpg` and `logo-gametape-stacked-white.png` (not WebP) | Run every fragment through the same image pass, not just the sales page |
| 29 | Pages `index.html` still has `PASTE-YOUR-CHECKOUT-LINK` | Fine for a preview; never send traffic to the Pages copy. The builder version gets the real link at build time |
| 30 | Public repo also holds transcripts and research; `.git` is 96 MB | Confirm exposure up front; consider keeping heavy or raw files out of the page repo |
| 31 | `expand_body.py (was gen_body.py)` assert failed after a token was removed | Replacements must tolerate missing tokens; only assert that no `@@` remains |
| 32 | Not verified end to end: no PageSpeed run, no test purchase | Add both as required steps in the playbook |
| 33 | Back-ups | Save `body-src-vN.html`/`copy-vN.md` (and script `-v1` copies) before each round, so "put it back as it was" is one copy |

---


## More pitfalls (copy intake, brand, first builds)


| # | Pitfall | Symptom | Fix / prevention |
|---|---|---|---|
| F1 | The AI tool's copy listed deliverables that aren't in the offer | Values were set for "templates" ($29) and "both milestone playbooks". Removed at #23 and #27. Totals went from $230 to $201. | At intake, check the "What you get" list against the offer ladder or offer document and ask the client |
| F2 | Hex codes shown as text only | "I cant see the colors just #D30805 numbers" | Always render swatches plus a mini page |
| F3 | No PDF tooling (no poppler); the Swift script failed with an SDK/compiler mismatch | Read tool: "pdftoppm is not installed" | JXA + PDFKit script (Appendix 1) |
| F4 | `<ol>` numbers render as list markers, so they're not text | `check_page`: "7 line(s) of the approved copy are not on the page" | Put "1. …" in the `<li>` text with `list-style:none` |
| F5 | Duplicate slider items had `alt=""` | NOTE "Image without alt text" | Give duplicates the same alt text plus `aria-hidden="true"` |
| F6 | Sticky/split custom rule overrode the kit's mobile stack | Section 3 stayed 2 columns at narrow widths | Add the single-column override inside `@media (max-width:820px)` |
| F7 | A long story left the media column floating with empty space | Reel stuck mid-column | `position:sticky;top:48px` plus `align-items:start` on desktop |
| F8 | Big display text not clamped for the viewport | Footer wordmark cut off at 1280 | `clamp(40px,12vw,148px)` with `white-space:nowrap; overflow:hidden` |
| F9 | Lazy-loaded images inside a translated marquee never load | Blank cards further along the slider | IntersectionObserver sets `loading='eager'` when the slider is within 600 px |
| F10 | Negative margins kept after moving an element outside the column | `scrollWidth` 411 vs 375 on phones | `margin:34px 0 30px`. Always check `scrollWidth == innerWidth`. |
| F11 | Weak first-choice image (a mostly white cover) | "looks thin" | Render all pages, make a contact sheet, pick the strongest slide |
| F12 | The transform script's regex didn't match | `AttributeError: 'NoneType'…` | Assert-then-write pattern: the file stayed untouched. Fix the pattern and rerun. |
| F13 | A global button-label replace also changed the `copy.md` header comment | Comment reads "Buttons are in [BUTTON: GET INSTANT ACCESS · $27 →] lines" | Anchor regexes to `^\[BUTTON:` lines. Harmless here. |
| F14 | Emphasis carried over to the wrong phrase | `.pss` on "one video a day", reversed at #20 | Ask which phrases to emphasize. Default to proof and benefits. |
| F15 | Invented values versus the kit's rule against inventing them | A risk of misleading anchors | Only on an explicit client instruction. Call it "value", never "regular price". Log the decision. |
| F16 | Photo rights | `rickey.jpg` is Getty with a watermark; `rickey-photo.jpeg` is likely a cropped version of it | Flag it, follow the client's decision, repeat the flag in the summary. (Later replaced by `rickey-bestbuy.jpg` plus the red carpet photo.) |
| F17 | Logo strip implies endorsement | 6 logos, but the copy names Nike, Subway and Temu | Flag it and ask which brands are real. The client decided to keep them "anyways". |
| F18 | PII in social screenshots and videos | Commenters' names "Joel Moreno", "KayKay" | Flag it. Public comments, but still listed. |
| F19 | The checker misses placeholder checkout links | `href="PASTE-YOUR-CHECKOUT-LINK"` passes | `grep -c 'PASTE-YOUR-CHECKOUT-LINK'` before export |
| F20 | `{FILL IN}` disclaimer note keeps the check at FIX | The check stayed at FIX through every round of Slice A. Claude only drafted disclaimers later, around #28 ("so we can go live"). | Ask for disclaimers early, or offer drafts for the client to approve (done later: earnings, TikTok/ByteDance non-affiliation, refund policy) |
| F21 | Reveal animation hides content in screenshots | Blank sections | `document.documentElement.classList.remove('anim')` during QA (on Nov 19: add `in` to `.r` with JS, never in the source) |
| F22 | Edit tool after a script changed the file | "file had been modified on disk since you last read it" | Re-read before context-dependent edits |
| F23 | Videos too heavy (7 to 12 MB each); no ffmpeg | — | Cloudinary transforms `w_360,q_auto,ac_none,du_12` (9.5 MB → 0.9 MB). If not hosted, `avconvert` presets or upload to a CDN. |
| F24 | The Nov 19 checker's false alarm | "$297" flagged as reference text | Explain it to the client and leave it |
| F25 | Brand guide fonts replaced by a client "test" | The live page isn't on the official brand fonts | Keep `brand-kit-v1.md` and label the test in `brand-kit.md` |

---

