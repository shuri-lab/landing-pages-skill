# Rubric (100 points)

## Automatic: 50 points (`python3 test/grade.py --page my-sales-page/index.html --copy my-sales-page/copy.md`)

| Item | Points |
|---|---|
| Phone 393×852: first button visible without scrolling (**hard fail if not**) | 10 |
| Phone: headline and hero image above the fold | 5 |
| No sideways scroll (phone, 1280, 1440) | 5 |
| Desktop 1280×800 and 1440×900: hero button on the first screen | 5 |
| No broken images | 3 |
| One CTA label on every button | 5 |
| Buttons jump to the offer stack; only one goes to checkout | 5 |
| No em or en dashes, no banned words | 5 |
| No placeholders on the page (**hard fail if any**) | 5 |
| Images light: WebP, under about 2 MB | 2 |

## Judged by TJ: 50 points
Open the page at phone size (Chrome DevTools → iPhone 16 Pro, or the shots in `shots/`) next to `test/reference/`.

| Area | Item | Points |
|---|---|---|
| **Copy (15)** | Hero follows the framework: headline is the end result + time + payoff; the subheadline highlights proof and the 3 outcomes | 5 |
| | Copy rules followed. No invented facts, numbers or testimonials (**hard fail if any**). Sales vs earnings labeled right. No income promise | 5 |
| | Offer stack is accurate: only the 3 real items, values $57/$47/$97, total $201, "You save $174", no bump on the page (**hard fail if a non-included item is listed**) | 5 |
| **Visual (20)** | Phone hero looks as polished as the reference: alert bar, logo, pill, big headline, mockup, subheadline, full-width button; not cramped | 5 |
| | Desktop hero: two columns, big mockup, logo strip on the first screen | 5 |
| | The page body has the house-style parts: logo slider, dark/light rhythm, visuals under claims, video carousel, screenshot slider, sticky phone CTA, story with photos | 5 |
| | Offer stack (mockup, rows with crossed values, total bar, deal box with a "You save" badge, trust row) and guarantee as its own block | 5 |
| **Process (15)** | `brief.md` passes the copy-context gate: all 8 kinds, offer confirmed, 5+ buyer quotes, numbers labeled, every fact sourced | 3 |
| | `tool-inputs.md`: all 16 fields filled from the brief, specific, nothing unconfirmed (compare with `examples/rickey-headstart/tool-inputs.md`) | 3 |
| | Copy stage: hero options written with a ⭐ pick; rules pass logged | 2 |
| | `image-plan.md` + `image-prompts.md` follow the template (style brief, file names, negatives) | 3 |
| | `review.md` + `shots/`: self-review done at phone and desktop, issues fixed | 2 |
| | `learned-rules.md`: every decision logged | 2 |

**Pass = 85+ and no hard fail.** For a score of 70–84, list the 3 biggest gaps. Each one is either a playbook gap (fix the playbook) or an execution gap (redo that stage).
