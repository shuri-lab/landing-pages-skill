# Stage 9 of 9: Share and hand off

**Goal:** the team and the client can see the page on a real link, and everything needed to keep working on it is in one repo.

**Out of scope here:** wiring checkout, order bump, upsell and course delivery in GoHighLevel (the GHL Funnel Playbook). The **loader** below is how we put our HTML into GHL (or any builder that accepts custom code) without pasting 100 KB into its editor.

## The steps (any project)
1. **Export:** `tools/rebuild.sh <WORK> "<title>"` writes `export/index-final.html` (no editor) and `export/paste-ready.html`.
2. **Repo:** ask the person to create an empty GitHub repo (or do it in the browser if they're signed in). Put in: `index.html` (= index-final), the `images/` the page uses, a `page-source/` folder (body-src, copy, brand-kit, learned-rules, image-prompts, paste-ready), and the client's project files if the client agrees they can be shared. Run `tools/rebuild.sh … --publish <repo> <pages URL>` to copy them.
3. **Before a public push:** scan for secrets (`grep -rIE "sk_live|pk_live|AKIA|ghp_|xox|PRIVATE KEY|password" .`) and files over 50 MB. Confirm with the client what may be public (research, transcripts, photos with unclear licenses).
4. **GitHub Pages:** Settings → Pages → branch `main`, folder `/ (root)`. The link works about a minute after each push.
5. **README:** what it is, the live link, how buttons work (all jump to the offer stack; one checkout link), what's still open (placeholders, missing images, licenses), and where each source file is.
6. **Tell the client and team** with the link and a 5-line summary. Show any email to the person before sending.

---

## B. Share and packaging method

### B1. What the user does vs what Claude does
1. **User:** creates an empty **public** GitHub repo (no README, so the first push isn't rejected) and sends its URL.
2. **Claude:** checks push access before relying on it:
   - `git --version`, `git config --global credential.helper`, `ls ~/.ssh`
   - `ssh -o BatchMode=yes -o ConnectTimeout=8 -T git@github.com` → here it was "Permission denied (publickey)": the key existed but wasn't on GitHub.
   - Fallback that worked: HTTPS with the macOS keychain. Test without prompts: `GIT_TERMINAL_PROMPT=0 git push -q https://github.com/<owner>/<repo>.git main`. If it succeeds, set `git remote set-url origin https://github.com/<owner>/<repo>.git`.
   - (`timeout` isn't on macOS; use `ssh -o ConnectTimeout=8`.)
3. **User confirms exposure:** list what becomes public (meeting transcripts, customer research, strategy docs, a possibly-licensed photo) and get an explicit yes.
4. **User:** turns on Pages after the first push: repo → Settings → Pages → Branch `main`, folder `/ (root)` → Save. Live in a minute or two at `https://<owner>.github.io/<repo>/`. Free plans need the repo to stay public for Pages.

### B2. Assembly recipe (what goes in the repo)
1. **Export the final page without the kit's editor:** `python3 kit/4-build/export_final.py --in my-sales-page/index.html --out-dir my-sales-page/export --images keep` → `export/index-final.html` (87 KB plus images) and `export/paste-ready.html`.
2. **Fresh folder:** `rm -rf <repo>; mkdir -p <repo>/images <repo>/offer-1-sales-page`.
3. `cp export/index-final.html <repo>/index.html`.
4. **Copy only the images the page uses:** regex `images/([A-Za-z0-9_.-]+\.(?:png|jpe?g|webp|gif))` over `index.html` and `body-src.html`, then copy each match (29 images here).
5. **Sources** into `offer-1-sales-page/`: `body-src.html copy.md copy-original.md brand-kit.md learned-rules.md image-prompts.md` plus `export/paste-ready.html`.
6. **Nothing the client sells, and no private material.** Never copy deliverables, paid PDFs, course decks, transcripts or the whole client folder into a public repo. Copy a file into `project-files/` only if the person approved that exact file. A file that was public once can still be found after it's removed.
7. **Size check:** `du -sh <repo>` (115 MB) and `find <repo> -type f -size +50M` (none). GitHub warns above 50 MB per file and rejects files above 100 MB.
8. **Secret scan before anything goes public:**
   - `grep -rIl -E 'sk_(live|test)_[A-Za-z0-9]{8,}|pk_(live|test)_[A-Za-z0-9]{8,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|xox[bp]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY|(api[_-]?key|secret|password|passwd)\s*[:=]\s*["'"'"']?[A-Za-z0-9/+_-]{12,}' .`
   - .docx text: `unzip -p "$f" word/document.xml | sed 's/<[^>]*>//g' | grep -i -o -E '.{0,30}(password|api key|sk_live|token|card number).{0,30}'`
   - Result here: nothing found.
9. `printf '.DS_Store\n' > .gitignore`.
10. **Commit identity:** never the user's personal email in a public repo. Use the GitHub noreply form: `git config user.name "<owner>"`, `git config user.email "<owner>@users.noreply.github.com"`. `git init -q -b main`, commit with the attribution trailer, push.
11. **Verify:** `git ls-remote` matches `git rev-parse HEAD`. `curl -s https://api.github.com/repos/<owner>/<repo>` → `private`, `has_pages`. `curl -o /dev/null -w '%{http_code}'` on the Pages URL.

Later additions in the same repo: `downloads/` (**free** files only; paid files live in the course, behind the login), `images/opt/` (WebP variants), `offer-2-upsell/`, and the builder fragments `ghl-*.html`.

### B3. Final folder layout (template for any project)
```
<project>-repo/
  README.md                 # written for the teammate (B5)
  .gitignore                # .DS_Store
  index.html                # final exported sales page (Pages root = shareable preview)
  images/                   # originals actually used by the page
  images/opt/               # <name>-<width>.webp variants (C)
  downloads/                # FREE files only, never paid deliverables
  offer-1-sales-page/
    body-src.html  copy.md  copy-original.md  brand-kit.md  learned-rules.md  image-prompts.md
    paste-ready.html        # kit export for a builder HTML block (relative paths)
    ghl-sales-page.html     # builder version: absolute URLs + checkout link + wrapper fix + title
    ghl-checkout-left.html  # Part 2: dist/checkout-left.html
    ghl-thank-you.html      # Part 2: dist/thank-you.html
  offer-2-upsell/
    ghl-upsell.html         # Part 2: dist/<upsell slug>.html
  project-files/            # only files the person approved one by one; never deliverables
```
Local working layout during the session: `sales-page/kit/` (the kit: `1-copy 2-brand 3-images 4-build 5-publish`), `sales-page/my-sales-page/` (working copy: `body-src.html` + `body-src-vN.html` backups, `copy.md` + `copy-vN.md`, `brand-kit.md`, `learned-rules.md`, `images/`, `images/opt/`, `export/`), the repo folder next to it, and `tools/` (scripts).

### B4. Emailing a teammate (pattern used)
- **Subject:** "<Client> / <Brand>: Offer 1 page is done. How do we put the funnel live with <tool>?"
- **Body order:**
  1. One line: what's finished (offer name and price).
  2. "Live page:" link.
  3. "Everything is in this public repo, so download or clone whatever you need:" repo link.
  4. One sentence on what's in it ("the page (index.html + images), the source files and copy, and all of the project files… The README explains what's where").
  5. What you're doing next.
  6. Numbered questions (checkout type and where its link goes, i.e. the placeholder `PASTE-YOUR-CHECKOUT-LINK`; bump as a checkbox; one-click upsell on the same card; PDF delivery; course hosting and access; community access).
  7. The user's constraints in their words (speed, reliability, go live ASAP).
  8. Ask for the plan: what gets built, with which tools, what's needed from us, timeline.
  9. Signed with the user's first name.
- **Process:** create a draft and show the text, then send only on the user's go-ahead. Verify the live link first (curl). Delete superseded drafts. When the teammate replies, read the thread and summarize it as plan / what they need from us / timeline / risks.

### B5. README contents (what the teammate needs)
1. One-paragraph purpose.
2. Live preview link, with the Pages switch-on steps.
3. What the page file is: one self-contained HTML (styles and scripts inline); images from `images/` (later `images/opt/`); fonts from Google Fonts; videos from Cloudinary with the transform used.
4. The viewports it was tested on: iPhone 16 393×852, 1280×800, 1440×900, 1920×1080.
5. The offer contents with values, total, price, bump, guarantee.
6. How the buttons work: every CTA jumps to `#buy`, only the offer-stack button goes to checkout, the placeholder name to replace, the sticky phone bar.
7. "Still open": checkout, upsell, disclaimers to approve, image license to confirm, FAQs.
8. A folders table.
9. Brand: colors and fonts.
10. Funnel table (step / URL / how it's built) once the builder is wired.
11. Delivery: course, workflows, downloads, and the placeholders still to fill (with the exact token to search for, e.g. `WHATSAPP-LINK-GOES-HERE`, `GT_LINKS.whatsapp`).
12. A "Speed" section (image sizes, total weights, video transform).
13. **Warning:** "Before you make the repo private, move the page code, images and PDFs into the platform's storage, or the pages go blank" (the loader depends on Pages).

**Keep it current.** At the end of the session the README still said "Images are full-size originals… compress them", "The $17 Starter Product List is shown on the page as 'Add at checkout for $17'" and "PASTE-YOUR-CHECKOUT-LINK". All three were out of date. `learned-rules.md` never got the late rules either (no bump on the sales page; WebP sizes; bump copy rule). Playbook rule: after every feedback round, update `learned-rules.md` and the README in the same commit.

---


## F. The loader technique (any builder that accepts custom code)

### F1. Why
- In the session, pasting 116 KB of page code into the builder's code editor wasn't possible: clipboard paste didn't reach the browser pane, and typing that much is slow and error-prone.
- So the builder element holds a ~500-character loader that fetches the page fragment from GitHub Pages and injects it.
- Side benefits: the page source stays in git, any `git push` goes live in ~1 minute with no builder edits, and the same fragment can be previewed directly at its Pages URL.
- It works because GitHub Pages sends `access-control-allow-origin: *`, which was checked with `curl -sI … | grep -i access-control`, so a page on another domain can `fetch()` the file.

### F2. Generic loader (final form, with the 404 guard)
```html
<div id="X-root"></div>
<script>(function(){
  var u='https://<owner>.github.io/<repo>/<folder>/<fragment>.html';
  fetch(u,{cache:'no-cache'})
    .then(function(r){ if(!r.ok){ throw 0; } return r.text(); })
    .then(function(h){
      var root=document.getElementById('X-root');
      root.innerHTML=h;
      // innerHTML never runs <script> tags: re-create each one so it executes
      root.querySelectorAll('script').forEach(function(s){
        var n=document.createElement('script');
        if(s.src){ n.src=s.src; } else { n.textContent=s.textContent; }
        s.parentNode.replaceChild(n,s);
      });
    }).catch(function(){});
})();</script>
```
- One unique root id per page: `gt-root` (sales), `gtc-root` (checkout left), `gtty-root` (thank-you), `gtu-root` (upsell).
- `cache:'no-cache'` makes the browser revalidate every load, so pushes show up without hard refreshes.
- Version history in the session:
  - The first loaders had no `r.ok` check. The checkout's left column once rendered **GitHub's 404 page** because Pages hadn't deployed the new file yet. Later loaders added `if(!r.ok) throw` plus `.catch`.
  - The sales-page loader also copies `s.src` for external scripts. The later ones only copied inline `textContent`, because those fragments had only inline scripts. Use the full version above.

### F3. Fragment contract (what each fetched file must contain)
1. **Wrapper fix first** (F4), using the same root id.
2. Font `<link>`s (and `preconnect`). They work when injected into the body.
3. CSS **scoped under a unique container id** (`#gtc`, `#gty`, `#gtu`), with `!important` only where builder styles must be overridden.
4. **Absolute URLs** for every image, `srcset` entry and CSS `url()`, pointing to the static host.
5. Inline scripts only. Make them idempotent and tolerant of late DOM (retry interval and/or MutationObserver).
6. `document.title='…'` in a script. The builder page title came back empty, so the fragment sets it.
7. Config at the top for anything the client fills in later, e.g. `var GT_LINKS={course:'…',whatsapp:'',support:''}`. An empty value shows a graceful placeholder state (greyed button + "coming to your email" note).
8. No `<html>/<head>/<body>`.

### F4. Wrapper-padding fix
Builders wrap custom code in several layers that add padding and a max-width. To diagnose, walk up from the root and print each layer:
```js
let a=[],e=document.getElementById('X-root');
for(let i=0;i<10&&e;i++){const cs=getComputedStyle(e);a.push(e.tagName+'.'+String(e.className).split(' ').slice(0,2).join('.')+' p:'+cs.padding+' mt:'+cs.marginTop+' mw:'+cs.maxWidth+' top:'+Math.round(e.getBoundingClientRect().top));e=e.parentElement}
a
```
Found here: column `p:10px 5px`, row `p:10px 5px`, an inner `max-width:1170px`, and a section with `padding-top:20px`. The section is a **`div` with a `section-XXXX` class, not a `<section>` tag**, so the first rule missed it and left a 20px white strip on the thank-you page. Final rule, prepended to every fragment:
```css
section:has(#X-root),[class*="section-"]:has(#X-root),.c-row:has(#X-root),.c-column:has(#X-root),
.inner:has(#X-root),.c-custom-code:has(#X-root),.custom-code-container:has(#X-root)
{padding:0!important;margin:0!important;max-width:none!important;width:100%!important}
```
- It needs `:has()` (current Chrome, Safari and Firefox; older browsers would just keep the padding).
- Also turn on the builder's own "full width rows" and zero section padding as a fallback.
- The same `:has()` trick restyles native elements next to the fragment (the upsell button wrappers, the checkout section padding on phones).

### F5. Deploy and verify loop
1. Edit the fragment → `git add -A && git commit -m … && git push`.
2. Poll Pages until the **new content** is served (not just HTTP 200, because the CDN can serve the old file for a while). Use a cache-buster and a marker string from the change: `for i in $(seq 1 18); do curl -s "<url>?r=$i" | grep -q '<marker>' && { echo "live after ~$((i*10))s"; break; }; sleep 10; done`. Observed: 50–70 s typically, once 10 s. One check after a fixed `sleep 45` still saw the old file.
3. Reload the live builder page at 393×852 and 1280×800. Run the overflow check and screenshots.

### F6. Limits and production advice
- The page depends on a **public** repo and GitHub Pages uptime. **Before making the repo private,** move the code into the builder (paste `paste-ready.html`) and the images/PDFs into the platform's media storage, or the pages go blank.
- Content appears only after JS runs. Turn off any builder setting that lazy-loads custom code (in this builder, "Optimize JavaScript"). Crawlers that don't run JS see an empty page, which is fine for ad-traffic funnels and bad for SEO pages.
- The kit's intended production path is still: host images on the platform (`MAKE-YOUR-PAGE-LOAD-FASTER.txt` step 4, `export_final.py --images urls --urls image-urls.json`) and paste `paste-ready.html` (target <150 KB with hosted images).

---

