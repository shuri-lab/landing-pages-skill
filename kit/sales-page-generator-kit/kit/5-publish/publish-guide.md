# Publishing the page (any builder that accepts HTML)

The page is one block of HTML. It works in Kajabi, GoHighLevel, Systeme.io and any builder with a custom code / HTML block. The steps below are the same idea everywhere; the menu names differ, so look for a block called Custom Code, Custom HTML, HTML, or Code.

## Pick the image mode first
Run `export_final.py` with one of these:
- `--images embed`: every image is built into the file. One paste, nothing to upload. Only for pages whose paste stays under about 2.5 MB (the report tells you).
- `--images urls`: images are used from links. The client uploads the pictures to their platform's media library, copies each link, and Claude adds them to `my-sales-page/image-urls.json` like `{"hero.png": "https://..."}`. Then run the export again with `--urls my-sales-page/image-urls.json`.
- Mixed (best for most pages): embed the small images, upload only the big ones. Any image that has a link in `image-urls.json` is used by link; the rest follow `--images embed`. Upload the biggest ones first (mockups, GIFs).

Lessons from the first real page:
- A paste of about 2.8 MB loaded. A paste of 3.5 MB had images missing in GoHighLevel. Keep it under 2.5 MB to be safe.
- A very large single image (about 1 MB) is better hosted than embedded.
- A hosted image link that works when opened alone in a browser can still fail inside a builder. If an image does not show after pasting, use the embedded version of that image, or re-upload it under a new name, and tell Claude what you see.
- Always test the pasted page on desktop and on a phone.

## Steps
1. Open the page or funnel step in the builder, on a blank page.
2. Make a full-width area: a section set to full width, with padding and margin at 0, a row with one column, also full width and 0 padding. (Names differ by builder. The page needs the whole screen width.)
3. Add a Custom Code / HTML block to that column and open its code editor.
4. Open `export/paste-ready.html` in a text editor, select all, copy, paste into the code editor, and save the block. (Claude can copy the file to your clipboard for you if you ask.)
5. Replace any old code in the block: click inside, select all (Cmd+A or Ctrl+A), then paste.
6. Save the page. If it is published, publish again.
7. Hard refresh the page (Cmd+Shift+R or Ctrl+Shift+R) or open it in a private window, then check desktop and phone.

## If something looks wrong
- Nothing changed: the old code is still there, the block was not saved, or the page was not published again. Hard refresh. Search the page for a phrase from your newest change (Cmd+F or Ctrl+F).
- Page is narrow or has side margins: the section, row or column is not full width with 0 padding.
- White strips left and right on a phone: the builder pads the code block on mobile. The page already stretches itself to the full screen width on phones and tablets, so a strip that is still there is usually the builder's own section, row or column padding or background color. Set the mobile padding on the section, row and column to 0 and give them the same background color as the page's first section, then save, publish and hard refresh.
- Strange symbols: use `paste-ready.html`, never `index.html`. It is plain text with no special characters inside.
- Images missing: check the paste size in the export report, then see the image-mode notes above.
- Buttons go nowhere: check the checkout link in the copy. Every button uses it.

## Changing the page later
Open `index.html` (the draft with the editor) in a browser, change it, click "Save draft", move the saved file into `my-sales-page`, and ask Claude to run the export again. Do not edit `paste-ready.html` by hand.
