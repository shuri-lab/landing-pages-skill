# Dry run, Nov 20 2026: did the playbook work for someone who wasn't there?

A fresh Claude agent with no memory of the original build took the test (`test/TEST.md`). It used only the playbook, the raw Rickey files and `client-answers.md`, and it had no browser pane.

- **Automatic grade:** 50/50, no hard fails (`grade.txt`). Phone button at 762 of 852 (the original: 763). No sideways scroll at any size. One button label. Offer stack correct. 1.23 MB of WebP images.
- **Judged (its own estimate against `rubric.md`):** about 46/50, so **about 96/100, a pass.** TJ should grade it for real.
- **Time:** about 35–40 minutes of agent time.
- **Its first screen:** `mobile-393x852-fold.png` and `desktop-1440x900-fold.png`. Compare with `test/reference/`.
- **What it found wrong with the playbook:** `playbook-feedback.md`. All of it was fixed in the playbook the same night: the test's model files, chunked full-page screenshots, the image-order step, the logo choice for the fold, the brief template's slots, the 16 tool fields, the kit overrides and more.
- **Its self-review table** (22 sections checked): `review.md`.
