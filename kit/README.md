# kit/: Isabelle's "Sales Page Generator - for clients" (complete, as bought)

This folder is the full **"Sales Page Generator - for clients"** download from the Buy-Now Sales Page portal (tasteofreedom.app.clientclub.net, "Claude creates your entire sales page" section). It's **unchanged**. The playbook uses it as the build engine and adds everything on top.

| Path | What it is |
|---|---|
| `HOW-TO-START.md` / `.html` | Isabelle's own quick start (for her clients) |
| `START-HERE-SINGLE-FILE.md` | The whole kit in one file (for Claude apps that can't open a folder) |
| `sales-page-generator-kit/START-HERE.md` | The kit's step-by-step instructions for Claude (copy → brand → images → build → publish) |
| `sales-page-generator-kit/kit/1-copy/` | `structure.md` (the 14 sections), `questions.md` (copy interview), `voice.md` |
| `sales-page-generator-kit/kit/2-brand/` | `_template.md` (brand kit format) + examples |
| `sales-page-generator-kit/kit/3-images/` | `image-slots.md` |
| `sales-page-generator-kit/kit/4-build/` | `build_page.py`, `check_page.py`, `export_final.py`, `base.css`, `sections.md`, the in-page editor, `example-body.html` (Isabelle's page: structure only) |
| `sales-page-generator-kit/kit/5-publish/` | `publish-guide.md` (Kajabi, GoHighLevel, Systeme.io…) |
| `MAKE-YOUR-PAGE-LOAD-FASTER.html` / `.txt` | Isabelle's speed prompt (our Stage 8 goes further) |
| `all-brand-palettes.pdf`, `palettes/` | 42 ready brand palettes |
| `sales-page-generator-kit.zip`, `original-download/` | The original zips |

**How the playbook uses it:** our `tools/rebuild.sh` calls the kit's `build_page.py`, `check_page.py` and `export_final.py`. Our stages follow the kit's structure, plus the house style, the copy tool, the framework, media sourcing, self-review and speed. You don't need to run the kit's START-HERE on its own: the playbook's `START-HERE.md` covers it.

## Where the playbook overrides the kit
| Kit says | Playbook does | Why |
|---|---|---|
| Hero subheadline formula starts "Steal my…" | "Follow the same plan behind…" / "Get…" | Clients ban "steal" (`knowledge/copy-rules.md`) |
| Section 3 story is text | Section 3 gets the founder photos + a logo slider | David's feedback (`knowledge/house-style.md` #16) |
| One dark band | Dark sections about every 3rd section | David's feedback (#12) |
| Each section has its own button label | One label everywhere | David's feedback (#8) |
