# Part 2 test: build the rest of a funnel for a new offer

Can someone (or a fresh Claude agent) build a checkout, order bump, upsell, thank-you page and emails at our level for an offer we've never seen? **The client and offer here are made up for this test.**

1. Use only this playbook and `inputs/`. Write your questions in `my-funnel-pages/questions.md` first. Then have **another person (or session)** read `client-answers.md` and give you only the answers to what you asked. If you must read it yourself, use nothing you didn't ask for, and say so.
2. Work in a new folder `my-funnel-pages/`. Follow `stages/funnel-1-plan.md` to `funnel-5`.
3. Hand in: `funnel-pages.json`, `dist/`, `shots/`, `questions.md`, `review.md`.
   Also run `python3 test/part-2/probes.py`: the builder must catch every bad input.
4. Graded with `rubric.md`. **Pass: 85 with no hard fail.**
