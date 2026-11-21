# test/: can someone else do it?

Start with **`TEST.md`** (the task and rules). Then:
- `inputs.md`: the only inputs allowed, all inside this playbook
- `client-answers.md`: stands in for the client
- `rubric.md`: 100 points (50 automatic + 50 judged); pass = 85 with no hard fail
- `grade.py`: the automatic 50: `python3 test/grade.py --page my-sales-page/index.html --copy my-sales-page/copy.md`
- `tj-review-sheet.md`: one page for TJ to fill in
- `reference/`: our final page at phone and desktop size, for the side-by-side
