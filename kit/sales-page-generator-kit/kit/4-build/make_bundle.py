#!/usr/bin/env python3
"""Make ONE file with the whole kit inside, for normal Claude chat (where a folder cannot be attached).

usage:  python3 make_bundle.py   (run from the sales-page-generator-kit folder; writes START-HERE-SINGLE-FILE.md)
The instruction file stays first. Every kit file follows in a "KIT FILES" section; Step 0 tells Claude to write them out.
"""
import os, sys
if len(sys.argv) > 1:
    print(__doc__)
    sys.exit(0)
root =os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
kit = os.path.join(root, 'kit')
out = open(os.path.join(root, 'START-HERE.md'), encoding='utf-8').read().rstrip() + '\n\n---\n\n## KIT FILES\n\nWrite each file below to the path shown (create folders as needed), exactly as written, then continue with Step 0.\n'
for d, _, files in sorted(os.walk(kit)):
    for f in sorted(files):
        if f.endswith(('.pyc', '.DS_Store')) or '__pycache__' in d:
            continue
        p = os.path.join(d, f)
        rel = os.path.relpath(p, root).replace(os.sep, '/')
        out += '\n### FILE: %s\n\n`````\n%s\n`````\n' % (rel, open(p, encoding='utf-8').read().rstrip())
dest = os.path.join(root, 'START-HERE-SINGLE-FILE.md')
open(dest, 'w', encoding='utf-8').write(out)
print('wrote', dest, len(out.encode('utf-8')) // 1024, 'KB')
