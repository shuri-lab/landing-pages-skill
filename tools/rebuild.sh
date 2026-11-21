#!/bin/bash
# One command to rebuild, check, export (and optionally publish) a page after every change.
#
# Usage:
#   tools/rebuild.sh <WORK dir> "<Page title>" [--publish <repo dir> <public base URL>]
# Example:
#   ~/sales-page-playbook/tools/rebuild.sh ~/clients/acme/my-sales-page "Acme Course | Acme"
#   ~/sales-page-playbook/tools/rebuild.sh ~/clients/acme/my-sales-page "Acme Course | Acme" \
#       --publish ~/clients/acme/acme-repo https://your-org.github.io/acme-repo/
#
# Steps:
#   1. body-src.html + page-config.json -> body.html     (tools/expand_body.py; skipped if no page-config.json)
#   2. body.html + brand-kit.md         -> index.html    (kit build_page.py)
#   3. check against copy.md                              (kit check_page.py: fix everything it flags)
#   4. export: index-final.html + paste-ready.html        (kit export_final.py --images keep)
#   5. --publish: copy page + images/opt into the repo; paste-ready gets absolute image URLs
set -euo pipefail
PLAYBOOK="$(cd "$(dirname "$0")/.." && pwd)"
KIT="$PLAYBOOK/kit/sales-page-generator-kit/kit/4-build"
WORK="${1:?WORK dir (my-sales-page) required}"
TITLE="${2:?Page title required}"
WORK="$(cd "$WORK" && pwd)"

if [ -f "$WORK/page-config.json" ] && [ -f "$WORK/body-src.html" ]; then
  python3 -I "$PLAYBOOK/tools/expand_body.py" "$WORK/body-src.html" "$WORK/body.html" --config "$WORK/page-config.json"
fi
python3 -I "$KIT/build_page.py" --body "$WORK/body.html" --kit "$WORK/brand-kit.md" --out "$WORK/index.html" --title "$TITLE" >/dev/null
echo "built  $WORK/index.html"
python3 -I "$KIT/check_page.py" --page "$WORK/index.html" --copy "$WORK/copy.md" --images-dir "$WORK/images" | tail -6
python3 -I "$KIT/export_final.py" --in "$WORK/index.html" --out-dir "$WORK/export" --images keep >/dev/null
echo "export $WORK/export/index-final.html + paste-ready.html"

if [ "${3:-}" = "--publish" ]; then
  REPO="${4:?repo dir}"; BASE="${5:?public base URL ending in /}"
  mkdir -p "$REPO/images/opt"
  [ -d "$WORK/images/opt" ] && cp "$WORK/images/opt/"*.webp "$REPO/images/opt/" 2>/dev/null || true
  cp "$WORK/export/index-final.html" "$REPO/index.html"
  mkdir -p "$REPO/page-source"
  cp "$WORK/body-src.html" "$WORK/copy.md" "$WORK/brand-kit.md" "$WORK/learned-rules.md" "$REPO/page-source/" 2>/dev/null || true
  python3 -I - "$WORK/export/paste-ready.html" "$REPO/page-source/paste-ready-absolute.html" "$BASE" <<'PY'
import sys, re
src, out, base = sys.argv[1], sys.argv[2], sys.argv[3].rstrip('/') + '/images/'
h = open(src, encoding='utf-8').read()
h = h.replace('src="images/', 'src="' + base).replace('srcset="images/', 'srcset="' + base)
h = h.replace(', images/', ', ' + base).replace('url(images/', 'url(' + base)
open(out, 'w', encoding='utf-8').write(h)
print('paste-ready with absolute image URLs: %.0f KB, relative images left: %d'
      % (len(h.encode()) / 1024, len(re.findall(r'(?:src|srcset)="images/', h))))
PY
  echo "published into $REPO (commit and push it yourself, then wait ~1 min for GitHub Pages)"
fi
