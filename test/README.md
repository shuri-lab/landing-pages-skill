# test/: can someone else do it?

Start with **`TEST.md`** (the task and rules). Then:
- `inputs.md`: the only inputs allowed, all inside this playbook
- `client-answers.md`: stands in for the client
- `rubric.md`: 100 points (50 automatic + 50 judged); pass = 85 with no hard fail
- `grade.py`: the automatic 50: `python3 test/grade.py --page my-sales-page/index.html --copy my-sales-page/copy.md`
- `tj-review-sheet.md`: one page for TJ to fill in
- `reference/`: our final page at phone and desktop size, for the side-by-side
- `dry-run-2026-11-20/`: a fresh agent took this test blind: **50/50 automatic, about 96/100 overall** (its estimate), with its screenshots and the playbook problems it found (all fixed)
