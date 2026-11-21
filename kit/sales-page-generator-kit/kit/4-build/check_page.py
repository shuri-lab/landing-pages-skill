#!/usr/bin/env python3
"""Check the page before handing it over.

usage:
  python3 check_page.py --page index.html [--copy copy.md] [--images-dir images] [--reference-phrases reference-phrases.txt]

Checks:
  - leftover text from the reference example (Isabelle's own page) that must never appear on a client's page
  - placeholders still on the page ({{ }}, TODO, PASTE-YOUR, dashed "Your photo here" boxes)
  - images that point to a file that does not exist, or have no alt text
  - buttons without a real link (empty or "#")
  - sections numbered 1..14 present (missing ones are listed, not an error)
  - every line of the copy file is on the page (if --copy is given)
Prints a short report. Exit code 1 if something must be fixed.
"""
import argparse
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def visible_text(h):
    h = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S)
    h = re.sub(r'<[^>]+>', ' ', h)
    return re.sub(r'\s+', ' ', html.unescape(h)).strip()


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--page', required=True)
    ap.add_argument('--copy')
    ap.add_argument('--images-dir', default='images')
    ap.add_argument('--reference-phrases', default=os.path.join(HERE, 'reference-phrases.txt'))
    a = ap.parse_args()

    raw = open(a.page, encoding='utf-8').read()
    text = visible_text(raw)
    problems, notes = [], []

    if os.path.exists(a.reference_phrases):
        for line in open(a.reference_phrases, encoding='utf-8'):
            p = line.strip()
            if p and not p.startswith('#') and p.lower() in text.lower():
                problems.append('Leftover reference text on the page: "%s". Replace it with the client\'s own words.' % p)

    for pat, label in ((r'\{\{.*?\}\}', 'a {{placeholder}}'), (r'\bTODO\b', 'TODO'), (r'PASTE-YOUR', 'PASTE-YOUR link placeholder'), (r'\[ASK[^\]]*\]', 'an unanswered [ASK] gap'), (r'\{ASK ME[^}]*\}', 'an unanswered {ASK ME} gap'), (r'\{FILL IN[^}]*\}', 'an unfilled {FILL IN} note')):
        for m in re.finditer(pat, text):
            problems.append('Placeholder left on the page: %s ("%s")' % (label, m.group(0)[:60]))
    ph = len(re.findall(r'class="[^"]*\bph\b', raw))
    if ph:
        notes.append('%d dashed placeholder box(es) (class "ph") still on the page. Fine in a draft, replace or remove before publishing.' % ph)

    base = os.path.dirname(os.path.abspath(a.page))
    for m in re.finditer(r'<img\b[^>]*>', raw):
        tag = m.group(0)
        src = re.search(r'src="([^"]*)"', tag)
        if not src:
            continue
        s = src.group(1)
        if not s.startswith(('data:', 'http://', 'https://')) and not os.path.exists(os.path.join(base, s)):
            problems.append('Image file not found: %s' % s)
        if not re.search(r'alt="[^"]+"', tag):
            notes.append('Image without alt text: %s' % s[:60])

    for m in re.finditer(r'<a\b[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*>', raw):
        href = re.search(r'href="([^"]*)"', m.group(0))
        if not href or href.group(1) in ('', '#'):
            problems.append('A button has no real link yet (href is empty or "#").')
            break

    found = sorted({int(x) for x in re.findall(r'data-section="(\d+)"', raw)})
    gone = [n for n in range(1, 15) if n not in found]
    if gone:
        notes.append('Sections not on this page: %s (fine if the client chose to skip them).' % ', '.join(map(str, gone)))

    if a.copy and os.path.exists(a.copy):
        nt = norm(text + ' ' + ' '.join(html.unescape(x) for x in re.findall(r'alt="([^"]*)"', raw)))
        lost = []
        for line in open(a.copy, encoding='utf-8'):
            if line.lstrip().startswith(('>', '<!--', '(', '[')):
                continue
            l = line.strip().lstrip('#*- ').strip()
            if len(l) < 25 or l.startswith(('(', '[', '<!--')):
                continue
            if norm(l)[:40] not in nt:
                lost.append(l[:90])
        if lost:
            problems.append('%d line(s) of the approved copy are not on the page, for example: "%s"' % (len(lost), lost[0]))

    print('CHECK REPORT for ' + a.page)
    print('------------')
    if not problems:
        print('OK: nothing that must be fixed.')
    for p in problems:
        print('FIX  ' + p)
    for n in notes:
        print('NOTE ' + n)
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
