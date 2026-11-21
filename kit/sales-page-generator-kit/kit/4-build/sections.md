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
