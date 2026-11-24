#!/usr/bin/env python3
"""build_funnel_pages.py: turns one funnel-pages.json into the checkout left column (with the order-form and
order-bump styling), the one-click upsell page(s), the thank-you page, the delivery emails and the list of texts
to type into GoHighLevel. Also writes local previews with a mock GHL order form and buttons. No installs.

  python3 tools/build_funnel_pages.py my-funnel-pages/funnel-pages.json            # build dist/ + preview/, report problems
  python3 tools/build_funnel_pages.py my-funnel-pages/funnel-pages.json --final    # same, and warnings become errors
  python3 tools/build_funnel_pages.py my-funnel-pages/funnel-pages.json --check    # report only, write nothing

Start from knowledge/templates/funnel-pages.json. Worked example: examples/rickey-headstart/funnel-pages/funnel-pages.json.
Exit code: 0 ok (warnings allowed unless --final), 1 problems found (dist/ is still written so you can look), 2 can't read the input.
Client-only design changes: put extra-upsell.css, extra-checkout.css or extra-thank-you.css next to the JSON (same %%TOKENS%%).
A CHECK you have settled with the client: add its id and the reason to "accepted" in the JSON, e.g. {"accent_light": "client OK'd the preview"}.
Images: put them in an images/ folder next to the JSON and use "images/x.webp"; previews find them there, and the pages use assets_base + that path.
It computes totals and savings itself, so never type them. Next: node tools/check_funnel_pages.mjs my-funnel-pages
"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TPL = HERE / 'funnel_templates'

# ---------- colour helpers ----------
def rgb(h):
    h = h.lstrip('#')
    if len(h) == 3: h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def hexs(t): return '#%02x%02x%02x' % tuple(int(round(max(0, min(255, x)))) for x in t)
def mix(a, b, t): return hexs(tuple(x * (1 - t) + y * t for x, y in zip(rgb(a), rgb(b))))
def lum(h):
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    r, g, b = (f(x / 255) for x in rgb(h)); return .2126 * r + .7152 * g + .0722 * b
def contrast(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)

# ---------- small helpers ----------
ALLOWED = re.compile(r'&lt;(/?)(b|mark|br|i|span)&gt;')
def rich(s):
    """Escape everything, then allow <b>, <i>, <mark>, <span> and <br>."""
    return ALLOWED.sub(r'<\1\2>', html.escape(str(s or ''), quote=False))
def plain(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', str(s or ''))).strip()
def attr(s): return html.escape(plain(s), quote=True)
def shows(price, text):
    return bool(re.search(re.escape(str(price)) + r'(?![\d,.]*\d)', str(text)))
def money(s):
    m = re.search(r'\$\s*([\d,]+(?:\.\d{2})?)', str(s or ''))
    return float(m.group(1).replace(',', '')) if m else None
def fmt(v): return ('$%s' % format(int(v), ',')) if float(v).is_integer() else '$%s' % format(v, ',.2f')
def js(s): return json.dumps(str(s or ''), ensure_ascii=False).replace('</', '<\\/')

class Report:
    def __init__(self, accepted=None): self.err, self.warn, self.ok, self.acc = [], [], [], accepted or {}
    def e(self, m): self.err.append(m)
    def w(self, m, wid):
        if self.acc.get(wid): self.ok.append(f'{wid}: {self.acc[wid]}')
        else: self.warn.append(f'[{wid}] {m}')

# ---------- rules ----------
BANNED = ['steal', 'regular price', 'today only', 'today-only', 'guaranteed income', 'hurry', 'act now']
URGENCY = re.compile(r"\b(last chance|closes? (at|in|soon|tonight|today)|midnight|countdown|expir(es|ing)|ends? (today|tonight|soon|in \d)|offer ends|before it'?s too late|only \d+ (left|spots?|seats?)|only today\b(?! \$)|just for today|for today only|disappears?|goes away|\d+ ?[ap]\.?m\b|\d+ (spots?|seats?|copies) left|\d+\s*(hours?|minutes?) left)\b", re.I)
INSULT = re.compile(r"\b(stupid|dumb|idiot|lazy|loser|pathetic|broke forever|don'?t care about|hate (my|money)|happy (being|to be) (broke|poor|fat)|stay(ing)? (broke|poor|fat)|fail(ure)? at)\b", re.I)
FILE_LINK = re.compile(r'(\.(pdf|zip|docx?|xlsx?|epub|csv)(\?|#|$))|drive\.google|docs\.google|dropbox\.com|notion\.(so|site)|wetransfer|/wp-content/uploads|/download', re.I)
LEFTOVER = re.compile(r'rickey|game ?tape|\bgametape|tiktok shop headstart|headstart course|davidhsai|shuri-lab\.github\.io/rickey', re.I)
PLACEHOLDER = re.compile(r'REPLACE-ME|\{FILL|\[insert|lorem ipsum|WHATSAPP-LINK|PASTE-YOUR|YOUR-DOMAIN|example\.(com|org)|\.invalid', re.I)

def walk(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items():
            if not str(k).startswith('_'): yield from walk(v, f'{path}.{k}' if path else k)
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, f'{path}[{i}]')
    else: yield path, o

NOT_COPY = re.compile(r'(^brand\.|image|logo|_url|\.url$|^links\.|sources|_source|photo|thumb|\.qr$|^domain|^slug|^assets|root_prefix|video|\.slug$|^accepted|\.source$|^real_deadline)')

def stack(items):
    vals = [money(i.get('value')) for i in items]
    return sum(vals) if vals and all(v is not None for v in vals) else None

def validate(c, sales_text, R):
    for p, v in walk(c):
        if not isinstance(v, str): continue
        if PLACEHOLDER.search(v): R.e(f'{p}: still a placeholder ("{v[:60]}")')
        client = str(c.get('client', ''))
        if LEFTOVER.search(v) and not re.search('rickey', client, re.I): R.e(f"{p}: text from the Rickey example (\"{v[:60]}\")")
        if NOT_COPY.search(p): continue
        if re.search('[—–]', v): R.e(f'{p}: has a dash (— or –); use a comma, colon or period')
        if ' -- ' in v or re.search(r'\w--\w', v): R.e(f'{p}: "--" is a dash; use a comma, colon or period')
        for w in BANNED:
            if re.search(r'\b%s\b' % re.escape(w), v, re.I): R.e(f'{p}: banned wording "{w}"')
        if re.search(r'\b(make|earn|making|earning)\s+(up to\s+)?\$\s*\d', v, re.I): R.e(f'{p}: reads like an income promise; promise results, never income')
        if URGENCY.search(v) and not c.get('real_deadline'): R.e(f'{p}: urgency wording ("{URGENCY.search(v).group(0)}") without a real deadline (set "real_deadline" with the client\'s words if there is one)')
    for k in ('client', 'slug', 'domain', 'brand', 'main', 'thankyou'):
        if not c.get(k): R.e(f'"{k}" is missing')
    b = c.get('brand') or {}
    for k in ('accent', 'ink', 'cream', 'line', 'heading_font', 'body_font', 'fonts_url'):
        if not b.get(k): R.e(f'brand.{k} is missing')
    for k in ('accent', 'ink', 'cream', 'line'):
        if b.get(k) and not re.fullmatch(r'#[0-9a-fA-F]{6}', b[k]): R.e(f'brand.{k} must be a 6-digit hex colour, got {b[k]}')
    m = c.get('main') or {}
    for k in ('name', 'price', 'headline', 'includes_line', 'items', 'guarantee', 'guarantee_source', 'trust'):
        if not m.get(k): R.e(f'main.{k} is missing')
    if m.get('price') and money(m['price']) is None: R.e('main.price needs a $ amount, e.g. "$27"')
    if m.get('items') and stack(m['items']) is None: R.w('main.items: some values are missing, so no total is shown', 'main_total')
    if m.get('items') and stack(m['items']) and not m.get('values_approved'): R.w('main.values_approved is not true: the client has not approved the item values', 'main_values')
    if len(plain(m.get('includes_line'))) > 62: R.w('main.includes_line is over 62 characters and will wrap on the phone card', 'includes_line')
    if m.get('trust') and len(m['trust']) > 3: R.w('main.trust: keep 3 short items', 'trust')
    # bump
    bump = c.get('bump')
    if bump:
        for k in ('name', 'price', 'headline', 'oto', 'description', 'image', 'delivers'):
            if not bump.get(k): R.e(f'bump.{k} is missing')
        if bump.get('headline') and not plain(bump['headline']).startswith('Yes! Add'): R.e('bump.headline must be the checkbox sentence: "Yes! Add [Product]"')
        if bump.get('price') and bump.get('oto') and not shows(bump['price'], bump['oto']): R.e('bump.oto must show the bump price')
        d = plain(bump.get('description'))
        if len(d) > 150: R.e(f'bump.description is {len(d)} characters; keep it to about 130 (150 max)')
        if len(re.findall(r'[.!?](\s|$)', d)) > 2: R.e('bump.description: one sentence, two short ones at most')
        nums = set(re.findall(r'\d[\d,.]*', d))
        if len(nums) > 1: R.e(f'bump.description has {len(nums)} numbers ({", ".join(sorted(nums))}); use one')
        if 'guarantee_covers_bump' not in m: R.e('main.guarantee_covers_bump is missing: ask the client, then write true or false (false adds a line saying the guarantee is for the main product)')
        if money(bump.get('price')) and money(m.get('price')) and money(bump['price']) >= money(m['price']): R.w('the bump costs as much as the main offer or more; an add-on should be the easy yes', 'bump_price')
        if sales_text is not None and bump.get('name') and plain(bump['name']).lower() in sales_text.lower(): R.e('the sales page mentions the order bump; it may appear only on the checkout')
    ups = c.get('upsells') or []
    names = set()
    for n, u in enumerate(ups):
        at = f'upsells[{n}]'
        for k in ('slug', 'name', 'price', 'alert_1', 'alert_2', 'headline', 'sub', 'bridge_headline', 'bullets', 'items', 'guarantee', 'guarantee_source', 'yes', 'no', 'delivers'):
            if not u.get(k): R.e(f'{at}.{k} is missing')
        if u.get('slug') in names: R.e(f'{at}.slug is used twice')
        names.add(u.get('slug'))
        if not (u.get('image') or u.get('video')): R.e(f'{at}: needs "image" (or "video")')
        if u.get('image') and not u.get('image_alt'): R.e(f'{at}.image_alt is missing')
        if u.get('yes') and not u['yes'].startswith('YES!'): R.e(f'{at}.yes must start with "YES!" (the page styles the button by that word)')
        if u.get('yes') and u.get('price') and not shows(u['price'], u['yes']): R.e(f'{at}.yes must show the price {u["price"]}')
        if u.get('yes') and u.get('name') and plain(u['name']).lower() not in u['yes'].lower(): R.w(f'{at}.yes does not name the product', f'{at}.yes_name')
        if u.get('no') and not u['no'].startswith('No thanks'): R.e(f'{at}.no must start with "No thanks" (the page styles the link by those words)')
        if n == 0 and u.get('alert_1') and 'order' not in u['alert_1'].lower(): R.w(f'{at}.alert_1 should confirm the order first', f'{at}.alert')
        if u.get('bullets') and not 2 <= len(u['bullets']) <= 4: R.w(f'{at}.bullets: 3 is the standard', f'{at}.bullets')
        if u.get('items'):
            t, pr = stack(u['items']), money(u.get('price'))
            if t is None: R.w(f'{at}.items: some values are missing, so no total and no savings are shown', f'{at}.total')
            elif pr and t <= pr: R.e(f'{at}: total value {fmt(t)} is not above the price {u["price"]}')
            if t is not None and not u.get('values_approved'): R.w(f'{at}.values_approved is not true: the client has not approved the item values', f'{at}.values')
            for k, i in enumerate(u['items']):
                if not i.get('benefit'): R.w(f'{at}.items[{k}] has no benefit line', f'{at}.items[{k}]')
                if plain(i.get('name')).lower() == plain(u.get('name')).lower() and len(u['items']) > 1: R.w(f'{at}.items[{k}] has the same name as the whole product; call the part by what it is ("The full video course")', f'{at}.item_name')
        if u.get('video'): R.w(f'{at}: video upsells were never run live by us; tell the client', f'{at}.video')
        if n > 0: R.w(f'{at}: a second offer (downsell) was never run live by us; tell the client', f'{at}.downsell')
        if u.get('no') and INSULT.search(u['no']): R.e(f'{at}.no insults the reader ("{INSULT.search(u["no"]).group(0)}"); describe the situation instead')
        if len(plain(u.get('sub')).split()) > 45: R.e(f'{at}.sub is {len(plain(u["sub"]).split())} words; keep it to 45')
        if 'sold_elsewhere' not in u: R.e(f'{at}.sold_elsewhere is missing: ask whether it is or will be sold anywhere else at this price, then write false or true')
        elif u['sold_elsewhere'] and not (u.get('lead_1') and u.get('lead_2')): R.e(f'{at}: it is sold elsewhere, so the default "only available here" lines are not true; write your own lead_1 and lead_2')
        elif u['sold_elsewhere'] and re.search(r"only available|it's gone|one-time", ' '.join(plain(u.get(k)) for k in ('lead_1', 'lead_2', 'pill', 'alert_2')), re.I): R.e(f'{at}: it is sold elsewhere, but the page says it is only available here or one-time')
        if re.search(r'\b\d+ minutes?\b', plain(u.get('alert_1'))) and not u.get('access_confirmed'): R.w(f'{at}.access_confirmed is not true: is the access time in alert_1 real?', f'{at}.access')
        mg, ug = plain((m.get('guarantee') or {}).get('text')), plain((u.get('guarantee') or {}).get('text'))
        if mg and mg == ug and not u.get('guarantee_covers_upsell'): R.e(f'{at}: same guarantee text as the main offer, but guarantee_covers_upsell is not true; ask the client')
        if not u.get('proof') and not u.get('founder_note'): R.w(f'{at}: no proof and no founder note; ask the client for a real quote, result, screenshot or a few words of their own', f'{at}.proof')
        for k, q in enumerate(u.get('proof') or []):
            if not q.get('source'): R.e(f'{at}.proof[{k}].source is missing: proof must be real and traceable')
        if u.get('founder_note') and not u['founder_note'].get('source'): R.e(f'{at}.founder_note.source is missing: only words the client gave or approved')
    if ups and len(ups) > 1 and ups[0].get('price') and money(ups[1].get('price')) and money(ups[1]['price']) >= money(ups[0]['price']): R.w('the downsell costs as much as the upsell or more', 'downsell_price')
    ty = c.get('thankyou') or {}
    for k in ('title', 'headline', 'sub', 'steps'):
        if not ty.get(k): R.e(f'thankyou.{k} is missing')
    if (ty.get('quote') or {}).get('text') and not ty['quote'].get('source'): R.e('thankyou.quote.source is missing: use only words the client said or approved, or remove the quote')
    links = c.get('links') or {}
    for k, v in links.items():
        if not v: R.w(f'links.{k} is empty: its button is grey and its email link is plain text until you fill it', f'links.{k}')
        elif FILE_LINK.search(v): R.e(f'links.{k} points to a file or a file-sharing page; paid files stay behind the course login')
    if links.get('support') and not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]{2,}', links['support']): R.e('links.support is not an email address')
    for k, st in enumerate(ty.get('steps') or []):
        for b2 in st.get('buttons') or []:
            if b2.get('link') not in links: R.e(f'thankyou.steps[{k}]: button link "{b2.get("link")}" is not a key in "links"')
    for p, v in walk(ty):
        if not isinstance(v, str): continue
        if FILE_LINK.search(v): R.e(f'{p}: the thank-you page is public; never link a file from it ({v[:60]})')
        if re.search(r'\$\s*\d', re.sub(r'\$\d+M\b', '', v)): R.e(f'{p}: shows a price; the thank-you page never sells')
    em = c.get('emails') or {}
    need = ['main'] + (['bump'] if bump else []) + [u.get('slug') for u in ups]
    for k in need:
        e = em.get(k)
        if not e: R.e(f'emails.{k} is missing: every product delivers with its own email'); continue
        for f in ('subject', 'preview', 'paragraphs'):
            if not e.get(f): R.e(f'emails.{k}.{f} is missing')
        t = ' '.join(e.get('paragraphs') or [])
        if FILE_LINK.search(t): R.e(f'emails.{k}: links a file directly; paid files stay behind the course login')
        for lab, key in re.findall(r'\[([^\]]+)\]\((\w+)\)', t):
            if key not in ('login',) and key not in links: R.e(f'emails.{k}: link [{lab}]({key}): "{key}" is not a key in "links"')
        if '(login)' not in t: R.w(f'emails.{k} has no [label](login) sign-in link', f'emails.{k}.login')
    flat = lambda t: re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9$ ]', ' ', plain(t).lower())).strip()
    def needles(nm, parts, own):
        w = re.sub(r'^(the|my|your)\s+', '', flat(nm)); words = w.split(); out = [w] + [' '.join(words[i:i + 2]) for i in range(len(words) - 1)]
        for x in parts:
            y = re.sub(r'^(the|my|your)\s+', '', flat(x))
            if len(y.split()) > 1 and not re.match(r'^(full )?(video )?course$', y): out.append(y)
        return [x for x in out if x and x not in own and x not in ('full course', 'video course')]
    prods = [('main', m.get('name'), [i.get('name') for i in m.get('items') or []])] + ([('bump', bump.get('name'), [])] if bump else []) + [(u.get('slug'), u.get('name'), [i.get('name') for i in u.get('items') or []]) for u in ups]
    for key, nm, parts in prods:
        e = em.get(key)
        if not isinstance(e, dict): continue
        body = flat(' '.join([plain(x) for x in e.get('paragraphs') or []] + [plain(e.get('subject')), plain(e.get('preview'))]))
        own = flat(' '.join([plain(nm)] + [plain(x) for x in parts] + [plain(m.get('name'))] + [plain(i.get('name')) for i in m.get('items') or []]))
        for k2, n2, p2 in prods[1:]:
            if k2 == key: continue
            hit = next((x for x in needles(n2, p2, own) if x in body), None)
            if hit: R.e(f'emails.{key} says "{hit}", from "{plain(n2)}": it goes to people who may not have bought that')
    for p, v in walk(ty):
        if not isinstance(v, str) or NOT_COPY.search(p): continue
        own = flat(' '.join([plain(m.get('name'))] + [plain(i.get('name')) for i in m.get('items') or []]))
        for k2, n2, p2 in prods[1:]:
            hit = next((x for x in needles(n2, p2, own) if x in flat(v)), None)
            if hit and '?' not in plain(v): R.e(f'{p} names "{hit}" as if everyone had it; the thank-you page is the same for everyone, so name it only in a question ("Added …?")')
        if re.search(r'\b(buy|order now|add it now|upgrade)\b', plain(v), re.I): R.e(f'{p}: the thank-you page never sells ("{plain(v)[:50]}")')
    # yes/no fields must be real booleans, so "no" in quotes can't count as yes
    for p, v in walk(c):
        if re.search(r'(values_approved|guarantee_covers_bump|guarantee_covers_upsell|sold_elsewhere|access_confirmed|hide_name_label)$', p) and not isinstance(v, bool): R.e(f'{p} must be true or false without quotes, got {v!r}')
    # every number a buyer reads needs a source (prices, values, totals and savings of this offer are known already)
    src = {str(k).lower(): str(v) for k, v in ((c.get('sources') or {}).get('numbers') or {}).items()}
    okm = {money(x) for x in [m.get('price'), (bump or {}).get('price')] + [u.get('price') for u in ups]}
    for grp in [m.get('items') or []] + [u.get('items') or [] for u in ups]:
        okm |= {money(i.get('value')) for i in grp} | ({stack(grp)} if stack(grp) else set())
    for u in ups:
        if stack(u.get('items') or []) and money(u.get('price')): okm.add(stack(u['items']) - money(u['price']))
    names = {x.lower() for nm in [i.get('name') for i in m.get('items') or []] + [m.get('name'), (bump or {}).get('name')] + [u.get('name') for u in ups] for x in re.findall(r'\$?\d[\d,.]*[A-Za-z+%]?(?<![.,])', plain(nm))}
    for p, v in walk({k: c.get(k) for k in ('bump', 'upsells', 'thankyou', 'emails', 'labels')}):
        if not isinstance(v, str) or NOT_COPY.search(p) or re.search(r'(\.price|\.value|\.delivers|\.by|guarantee\.(text|title))$', p): continue
        t = re.sub(r'\b(day|lesson|module|step|part) \d+\b', '', re.sub(r'^\s*\d+[.)]\s', '', plain(v)), flags=re.I); t = re.sub(r'\{\{.*?\}\}|\[([^\]]*)\]\(\w+\)', r'\1', t)
        for num in sorted(set(re.findall(r'\$?\d[\d,.]*[A-Za-z+%]?(?<![.,])', t))):
            if num.startswith('$') and money(num) in okm and not re.search(r'[MmKk+]$', num): continue
            if num.lower() in src or (re.match(r'(thankyou|emails)', p) and num.lower() in names) or (p.startswith('emails') and num == '24' and '24 hours' in t) or (p.endswith('.progress') and num == '90%') or (re.search(r'alert_1$', p) and c['upsells'][0].get('access_confirmed') is not None and re.search(re.escape(num) + r' minutes', t)): continue
            R.e(f'{p}: the number "{num}" has no source; add it to sources.numbers ({{"{num}": "file and how it was counted, or the client\'s words"}})')
        w = re.search(r"\b(ten|dozens?|twenty|thirty|forty|fifty|sixty|hundreds?|thousands?|millions?)\b|\b(two|three|five|ten|twice|double|triple)( times)? (as |the )?(better|faster|more|bigger)\b", t, re.I)
        if w and w.group(0).lower() not in src: R.e(f'{p}: the number word "{w.group(0)}" has no source; add it to sources.numbers')
        cl = re.search(r"\b(guaranteed results?|lifetime|full-?time income|passive income|mak(e|ing) money|get rich|double your money|best in the world|#1|number one)\b", t, re.I)
        if cl: R.w(f'{p}: the claim "{cl.group(0)}" needs the client\'s word and a source', f'claim:{cl.group(0).lower()}')
    for k, v in list(src.items()) + [(f'accepted.{k}', str(v)) for k, v in (c.get('accepted') or {}).items()] + [(p, v) for p, v in walk(c) if re.search(r'(guarantee_source|\.source)$', p) and isinstance(v, str)]:
        if len(plain(v)) < 8: R.e(f'"{k}": "{v}" is not a reason; say where it comes from or who said it')
    gnums = set(re.findall(r'\d+', ' '.join(plain((m.get('guarantee') or {}).get(x)) for x in ('title', 'text'))))
    for x in m.get('trust') or []:
        for num in re.findall(r'\d+', plain(x)):
            if num not in gnums and num not in src: R.e(f'main.trust "{plain(x)}": {num} is not in the guarantee text')
    if not any((c.get('legal') or {}).values()): R.w('no privacy, terms or refund link; ad platforms usually ask for them', 'legal')
    if bump and 'sold_elsewhere' not in bump: R.e('bump.sold_elsewhere is missing: ask whether it is sold anywhere else at this price, then write false or true')
    if bump and bump.get('sold_elsewhere') is True and re.search(r'only|one-time offer', plain(bump.get('banner') or ''), re.I): R.e('bump.banner says it is only here, but it is sold elsewhere')
    for p, v in walk(c):
        if isinstance(v, str) and re.search(r'\.(webp|png|jpe?g|svg)$', v, re.I) and not re.match(r'^\w+:', v) and not (BASE / v).exists() and not (BASE / 'images' / v).exists():
            if not c.get('assets_base'): R.e(f'{p}: image not found: {v} (looked in this folder and in images/)')
    known = {money(x) for x in [m.get('price'), (bump or {}).get('price')] + [u.get('price') for u in ups] if money(x) is not None}
    for n, u in enumerate(ups):
        t = stack(u.get('items') or []); ok = known | {money(i.get('value')) for i in u.get('items') or []} | ({t, t - (money(u.get('price')) or 0)} if t else set())
        for k in ('headline', 'sub', 'alert_1', 'alert_2', 'bridge_headline', 'lead_1', 'lead_2', 'offer_tag', 'price_note', 'yes', 'no'):
            for a in re.findall(r'\$\s*[\d,]+(?:\.\d{2})?(?![\dMmKk])', plain(u.get(k))):
                if money(a) not in ok and a.replace(' ', '').lower() not in src: R.e(f'upsells[{n}].{k}: the amount {a} is not a price or value of this offer')
    if b.get('accent') and re.fullmatch(r'#[0-9a-fA-F]{6}', b['accent']):
        if contrast(b['accent'], '#ffffff') < 3: R.w(f'brand.accent {b["accent"]} is light: buttons use dark text on it; look at every preview', 'accent_light')

# ---------- rendering ----------
def tokens(c, root):
    b = c['brand']; a = b['accent']; ink = b['ink']
    on = '#ffffff' if contrast(a, '#ffffff') >= 3 else ink
    light = mix(a, '#ffffff', .24)
    txt = a
    while min(contrast(txt, '#ffffff'), contrast(txt, b['cream'])) < 4.5: txt = mix(txt, '#000000', .1)
    alert = b.get('alert_color') or a; on_alert = '#ffffff' if contrast(alert, '#ffffff') >= 3 else ink
    dark = a if contrast(a, ink) >= 3 else light
    while contrast(dark, ink) < 3: dark = mix(dark, '#ffffff', .15)
    return {'ACCENT': a, 'ACCENT_RGB': ','.join(map(str, rgb(a))), 'ACCENT_LIGHT': light, 'ACCENT_TINT': mix(a, '#ffffff', .78 if contrast(a, '#ffffff') < 3 else .92), 'VAL': b['body_font'] if re.search(r'(?<!sans-)serif', b['heading_font']) else b['heading_font'], 'ACCENT_TEXT': txt,
            'ACCENT_ON_DARK': dark, 'ON_ACCENT': on, 'ALERT': alert, 'ON_ALERT': on_alert, 'INK': ink, 'INK_RGB': ','.join(map(str, rgb(ink))), 'CREAM': b['cream'], 'LINE': b['line'],
            'HEAD': b['heading_font'], 'BODY': b['body_font'], 'HAND': b.get('hand_font') or b['heading_font'], 'ROOT': root}
def css(c, name, t):
    x = BASE / f'extra-{name}.css'
    light = TPL / f'{name}-light.css'
    extra = light.read_text(encoding='utf-8') if light.exists() and contrast(c['brand']['accent'], '#ffffff') < 3 else ''
    return fill((TPL / f'{name}.css').read_text(encoding='utf-8') + extra + (('\n/* this client only */\n' + x.read_text(encoding='utf-8')) if x.exists() else ''), t)
def L(c, k, d): return (c.get('labels') or {}).get(k) or d
def fill(s, t): return re.sub(r'%%(\w+)%%', lambda m: t[m.group(1)], s)
def fonts(c): return f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="{html.escape(c["brand"]["fonts_url"])}" rel="stylesheet">'
BASE, PREVIEW = Path('.'), False
def img(c, src): # assets_base + relative path, or a full URL; previews use the local file when there is one
    src = str(src or '')
    if PREVIEW and src and not re.match(r'^\w+:', src):
        for q in (BASE / src, BASE / 'images' / src):
            if q.exists(): return '../' + str(q.relative_to(BASE)).replace('\\', '/')
    if re.match(r'^(https?:|data:|file:)', src): return src
    return (c.get('assets_base') or '').rstrip('/') + '/' + src.lstrip('/') if c.get('assets_base') else src
def srcset(c, im): # "image" may be one URL or {"small": 720w, "large": 1280w}
    if isinstance(im, dict): return f'src="{attr(img(c, im["large"]))}" srcset="{attr(img(c, im["small"]))} {im.get("small_w", 720)}w, {attr(img(c, im["large"]))} {im.get("large_w", 1280)}w"', attr(img(c, im['small']))
    return f'src="{attr(img(c, im))}"', attr(img(c, im))
def crossed(v): return '<s>%s</s>' % rich(v) if v else ''
def legal(c):
    L = c.get('legal') or {}
    out = [f'<a href="{attr(L[k])}" target="_blank" rel="noopener">{n}</a>' for k, n in (('privacy', 'Privacy'), ('terms', 'Terms'), ('refund', 'Refunds')) if L.get(k)]
    return f'<p class="legal">{" · ".join(out)}</p>' if out else ''
def rootid(c, kind): return f'{c.get("root_prefix") or "gt"}{kind}-root'

def checkout(c):
    m, b, bump = c['main'], c['brand'], c.get('bump') or {}
    t = tokens(c, rootid(c, 'c')); total = stack(m['items'])
    rows = ''.join(f'        <li><span class="ck">✓</span><span><b>{rich(i["name"])}</b>{crossed(i.get("value"))}</span></li>\n' for i in m['items'])
    tot = f'<div class="tot"><span>{rich(L(c, "total", "Total value"))}</span><s>{fmt(total)}</s></div>' if total else ''
    big, small = srcset(c, m.get('image'))
    logo = f'<img class="{{}}" src="{attr(img(c, b.get("logo_on_light")))}" alt="{attr(b.get("name") or c["client"])}">' if b.get('logo_on_light') else ''
    g = m['guarantee']
    mock = f'<img class="mock" {big} sizes="520px" alt="{attr(m["name"])}">' if m.get('image') else ''
    thumb = f'<img src="{small}" alt="{attr(m["name"])}">' if m.get('image') else ''
    gtitle = '<b>%s</b>' % rich(g['title']) if g.get('title') else ''
    gnote = '<br><small>%s</small>' % rich(L(c, 'guarantee_scope', 'This guarantee is for %s.' % plain(m['name']))) if bump and not m.get('guarantee_covers_bump') else ''
    gphone = gtitle + rich(g['text']) + gnote
    spans = ''.join('<span>%s</span>' % rich(x) for x in m['trust'])
    card = 'card' if thumb else 'card" style="grid-template-columns:1fr'
    return f'''<!-- Checkout: left column + styling for the GHL order form and order bump on the right. Root id: {t["ROOT"]}
     Desktop: full offer column (.gtc-d). Phone: one compact card (.gtc-m) so the form shows on the first screen.
     No wrapper fix here on purpose (it would push the order form under this column). Built by tools/build_funnel_pages.py -->
{fonts(c)}
<style>
{css(c, "checkout", t)}</style>

<div id="gtc">
  <div class="gtc-d">
    {logo.format("lg")}
    <div class="pill">{rich(m.get("pill") or "You're one step away")}</div>
    <h1>{rich(m["headline"])}</h1>
    {mock}
    <div class="box">
      <h2>{rich(L(c, 'what_you_get', 'What you get today'))}</h2>
      <ul>
{rows}      </ul>
      {tot}
      <div class="now"><span>Today</span><span>{rich(m["price"])}</span></div>
    </div>
    <div class="g"><span class="gi">✓</span><span>{gtitle}{rich(g["text"])}{gnote}</span></div>
  </div>
  <div class="gtc-m">
    {logo.format("mlg")}
    <div class="{card}">
      {thumb}
      <div>
        <p class="t">{rich(m["name"])}</p>
        <p class="inc">{rich(m["includes_line"])}</p>
        <div class="pr">{crossed(fmt(total) if total else "")}<b>{rich(m["price"])} today</b></div>
      </div>
    </div>
    <div class="tr">{spans}</div>
  </div>
  {legal(c)}
</div>

<script>
document.title={js("Checkout | " + plain(m["name"]))};
(function(){{
  var IMG={js(img(c, bump.get("image")) if bump.get("image") else "")},GUAR={js(gphone)},ALT={js(plain(bump.get("name")))},BANNER={js(bump.get("banner") or ("Add this to your order" if bump.get("sold_elsewhere") else "One-time offer · only on this page"))},HELP={js(m.get("email_help") or "Your login is sent here.")};
  var ARROW='<svg viewBox="0 0 30 24" aria-hidden="true"><path d="M2 12h20M15 4l8 8-8 8" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  // GHL re-renders the form (e.g. when the bump is ticked), so everything here checks before it adds.
  function enhance(){{
    var f=document.querySelector('.c-order-form'); if(!f) return;
    var n=f.querySelector('input[aria-label="Full Name"]'); if(n){{ if(n.placeholder!=='Your full name') n.placeholder='Your full name'; n.setAttribute('autocomplete','name'); }}
    var e=f.querySelector('input[type="email"]');
    if(e){{ if(e.placeholder!=='you@example.com') e.placeholder='you@example.com'; e.setAttribute('autocomplete','email');
      var c=e.parentNode; if(c&&!c.querySelector('.gt-help')){{var s=document.createElement('span');s.className='gt-help';s.textContent=HELP;c.appendChild(s);}} }}
    var pay=f.querySelector('.order-form__payment'); if(pay&&GUAR&&!pay.querySelector('.gt-guar')){{var g=document.createElement('div');g.className='gt-guar';g.innerHTML=GUAR;pay.appendChild(g);}}
    var b=f.querySelector('.order-form__bump');
    if(b){{
      if(!b.querySelector('.gt-bump-top')){{var t=document.createElement('div');t.className='gt-bump-top';t.textContent=BANNER;b.insertBefore(t,b.firstChild);}}
      var cb=b.querySelector('.order-form__bump-check');
      if(cb&&!b.querySelector('.gt-arrow')){{var a=document.createElement('span');a.className='gt-arrow';a.innerHTML=ARROW;b.insertBefore(a,cb);}}
      var d=b.querySelector('.order-form__bump-desc');
      if(IMG&&d&&!d.querySelector('.gt-bump-img')){{var i=document.createElement('img');i.className='gt-bump-img';i.src=IMG;i.alt=ALT;d.insertBefore(i,d.firstChild);}}
    }}
  }}
  enhance();
  var tries=0,iv=setInterval(function(){{enhance();if(++tries>40)clearInterval(iv);}},250);
  if('MutationObserver' in window){{new MutationObserver(function(){{enhance();}}).observe(document.body,{{childList:true,subtree:true}});}}
}})();
</script>
'''

def upsell(c, n):
    u = c['upsells'][n]; root = rootid(c, 'u' if n == 0 else f'u{n + 1}'); t = tokens(c, root); total = stack(u['items'])
    items = ''
    for i in u['items']:
        cls = 'item' + ('' if i.get('thumb') else ' nothumb') + ('' if i.get('value') else ' noval')
        th = f'<div class="th"><img src="{attr(img(c, i["thumb"]))}" alt="" loading="lazy"></div>' if i.get('thumb') else ''
        mods = '\n            <ol class="mods">' + ''.join(f'<li><b>{k + 1}</b><span>{rich(x)}</span></li>' for k, x in enumerate(i['modules'])) + '</ol>' if i.get('modules') else ''
        val = f'<div class="val"><s>{rich(i["value"])}</s></div>' if i.get('value') else ''
        items += f'        <li class="{cls}">{th}<div><h3>{rich(i["name"])}</h3><p>{rich(i.get("benefit"))}</p></div>{val}{mods}</li>\n'
    if u.get('video'):
        v = u['video']
        media = f'<div class="vid"><video src="{attr(v)}" controls playsinline preload="metadata"></video></div>' if re.search(r'\.(mp4|webm)(\?|$)', v) else f'<div class="vid"><iframe src="{attr(v)}" title="{attr(u["name"])}" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>'
    else:
        big, _ = srcset(c, u['image'])
        media = f'<img class="shot" {big} sizes="(min-width: 800px) 760px, 100vw" alt="{attr(u["image_alt"])}" fetchpriority="high">'
    price = money(u['price']); deal = ''
    if total and price: deal = f'<div class="save">{rich(L(c, "save", "You save"))} {fmt(total - price)}</div>'
    tot = f'<div class="total"><span>{rich(L(c, "total", "Total value"))}:</span><s>{fmt(total)}</s></div>' if total else ''
    ptitle = '' if u.get('hide_name_label') else '<div class="ptitle">%s</div>' % rich(u['name'])
    jump = '    <p class="jump"><a href="#gtu-offer">%s</a></p>\n' % rich(u['jump_button']) if u.get('jump_button') else ''
    cards = ''.join('<figure class="pcard">%s%s%s</figure>' % ('<img src="%s" alt="%s" loading="lazy">' % (attr(img(c, q['image'])), attr(q.get('image_alt'))) if q.get('image') else '', '<blockquote>%s</blockquote>' % rich(q['text']) if q.get('text') else '', '<figcaption>%s</figcaption>' % rich(q['by']) if q.get('by') else '') for q in u.get('proof') or [])
    fn = u.get('founder_note') or {}
    note = '<div class="fnote">%s<div><p>%s</p>%s</div></div>' % ('<img src="%s" alt="%s" style="object-position:%s">' % (attr(img(c, fn['photo'])), attr(fn.get('by')), attr(fn.get('photo_position') or '50% 0')) if fn.get('photo') else '', rich(fn['text']), '<b>%s</b>' % rich(fn['by']) if fn.get('by') else '') if fn.get('text') else ''
    proof = ('    <section class="proof">%s%s%s</section>\n' % ('<h2>%s</h2>' % rich(u['proof_headline']) if u.get('proof_headline') and cards else '', '<div class="pcards">%s</div>' % cards if cards else '', note)) if cards or note else ''
    faq = ('    <section class="faq"><h2>%s</h2>%s</section>\n' % (rich(u.get('faq_headline') or 'Quick questions'), ''.join('<div class="qa"><b>%s</b><p>%s</p></div>' % (rich(q['q']), rich(q['a'])) for q in u['faq']))) if u.get('faq') else ''
    g = u['guarantee']; gtitle = '<b>%s</b>' % rich(g['title']) if g.get('title') else ''; bullets = ''.join('        <li><span>%s</span></li>\n' % rich(x) for x in u['bullets'])
    return f'''<!-- One-click upsell: {html.escape(plain(u["name"]))}, {u["price"]}. Root id: {root}
     Below this block in GHL: a native YES button (action "One click up/down sell product") and a small Custom Code element with the NO link.
     This file styles both by their first words: "YES!" and "No thanks". Built by tools/build_funnel_pages.py -->
{fonts(c)}
<style>
{css(c, "upsell", t)}</style>

<div id="gtu">
  <div class="alert" role="status">
    <p><span class="ok" aria-hidden="true">✓</span>{rich(u["alert_1"])}</p>
    <p>{rich(u["alert_2"]).replace("one-time", "one‑time")}</p>
  </div>
  <div class="prog"><div class="prog-in"><span>{rich(u.get("progress") or "Order 90% complete")}</span><span class="bar" aria-hidden="true"><i></i></span></div></div>

  <div class="wrap">
    <section class="hero">
      <div class="pill">{rich(u.get("pill") or "Exclusive one-time offer")}</div>
      <h1>{rich(u["headline"])}</h1>
      {media}
      {ptitle}
      <p class="sub">{rich(u["sub"])}</p>
    </section>

    <section class="bridge">
      <h2>{rich(u["bridge_headline"])}</h2>
      <ul class="wins">
{bullets}      </ul>
    </section>
{jump}{proof}
    <section class="offer" id="gtu-offer" aria-label="Everything you get">
      <div class="offer-head">
        <h2>{rich(L(c, "offer_head", "Everything You <mark>Get Today</mark>"))}</h2>
        <span>{rich(u.get("offer_tag") or "One-time %s · instant access" % u["price"])}</span>
      </div>
      <ul class="items">
{items}      </ul>
      {tot}
      <div class="deal">
        {deal}
        <p class="now">{rich(L(c, "now", "Today, only on this page:"))}<b>{rich(u["price"])}</b></p>
        <p class="note">{rich(u.get("price_note") or "One-time payment. Added to your order in one click, no need to enter your card again.")}</p>
      </div>
    </section>

    <div class="guar">
      <svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" fill="{t["ACCENT"]}"/><path d="M20 9 11 12.5v6.5c0 5.6 3.8 9.7 9 11.3 5.2-1.6 9-5.7 9-11.3v-6.5z" fill="{t["ON_ACCENT"]}"/><path d="m15.5 20 3 3 6-6" fill="none" stroke="{t["ACCENT"]}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <span>{gtitle} {rich(g["text"])}</span>
    </div>
{faq}
    <div class="lead">
      <p>{rich(u.get("lead_1") or "This is an exclusive one-time offer.")}</p>
      <p>{rich(u.get("lead_2") or "Only available right here, right now. Once you leave this page, it's gone.")}</p>
      <svg class="down" viewBox="0 0 34 34" aria-hidden="true"><path d="M17 5v22M8 18l9 9 9-9" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
  </div>
</div>
<script>
document.title={js(u.get("title") or "One-time offer | " + plain(u["name"]))};
(function(){{
  function tag(){{
    document.querySelectorAll('.c-button a, .c-button button').forEach(function(b){{
      var t=(b.textContent||'').trim().toLowerCase();
      if(t.indexOf('yes!')===0) b.classList.add('gtu-yes');
      else if(t.indexOf('no thanks')===0) b.classList.add('gtu-no');
    }});
  }}
  // GHL can take about 10 seconds to render the one-click button, so keep looking
  tag(); var n=0,iv=setInterval(function(){{tag();if(++n>80)clearInterval(iv);}},300);
}})();
</script>
'''

def thankyou(c):
    ty, b = c['thankyou'], c['brand']; root = rootid(c, 'ty'); t = tokens(c, root); steps = ''
    for k, s in enumerate(ty['steps']):
        btns = ''.join(f'<a class="btn{" dark" if x.get("dark") else ""}" data-link="{attr(x["link"])}" data-missing="{attr(x.get("missing") or "This link is coming to your email.")}" href="#"{" target=_blank rel=noopener" if x.get("new_tab") else ""}>{rich(x["label"])}</a>' for x in s.get('buttons') or [])
        body = f'<p>{rich(s["text"])}</p>' if s.get('text') else ''
        if s.get('photo'): body = f'<div class="wa"><img class="wap" src="{attr(img(c, s["photo"]))}" width="84" height="84" alt="{attr(s.get("photo_alt"))}">{body}</div>'
        qr = f'<div class="waqr"><img src="{attr(img(c, s["qr"]))}" width="150" height="150" alt="{attr(s.get("qr_alt") or "QR code")}"><span>{rich(s.get("qr_note") or "On a computer? Scan this with your phone camera.")}</span></div>' if s.get('qr') else ''
        btnrow = '<div class="btns">%s</div>' % btns if btns else ''
        note = '<div class="note">%s</div>' % rich(s['note']) if s.get('note') else ''
        steps += f'''    <div class="step"><div class="n">{k + 1}</div><div>
      <h2>{rich(s["title"])}</h2>
      {body}
      {btnrow}
      {note}{qr}
    </div></div>
'''
    logo = f'<img class="lg" src="{attr(img(c, b.get("logo_on_dark")))}" alt="{attr(b.get("name") or c["client"])}">' if b.get('logo_on_dark') else ''
    q = ty.get('quote') or {}
    qimg = '<img src="%s" alt="%s" style="object-position:%s">' % (attr(img(c, q['photo'])), attr(q.get('by')), attr(q.get('photo_position') or '50% 0')) if q.get('photo') else ''
    quote = f'''    <div class="rk">
      {qimg}
      <div><q>{rich(q["text"])}</q><div class="sig">{rich(q.get("by"))}</div></div>
    </div>
''' if q.get('text') else ''
    return f'''<!-- Thank-you page. Root id: {root}. Every link lives in GT_LINKS at the bottom; an empty one shows a grey button.
     This page is public: never link a paid file here. Built by tools/build_funnel_pages.py -->
{fonts(c)}
<style>
{css(c, "thank-you", t)}</style>
<div id="gty">
  <div class="top">
    {logo}
    <div class="badge">✓</div>
    <h1>{rich(ty["headline"])}</h1>
    <p class="sub">{rich(ty["sub"])}</p>
  </div>
  <div class="wrap">
{steps}{quote}    <p class="small" id="gty-help">{rich(ty.get("help") or "Didn't get the email? Check spam or Promotions.")}</p>
    {legal(c)}
  </div>
</div>
<script>
(function(){{
  var GT_LINKS={json.dumps(c.get("links") or {}, ensure_ascii=False)};
  document.title={js(ty["title"])};
  document.querySelectorAll('#gty [data-link]').forEach(function(a){{
    var u=GT_LINKS[a.getAttribute('data-link')];
    if(u){{a.href=u;return;}}
    a.className+=' off'; a.removeAttribute('href');
    if(a.getAttribute('data-missing')){{var d=document.createElement('div');d.className='note';d.textContent=a.getAttribute('data-missing');a.parentNode.parentNode.insertBefore(d,a.parentNode.nextSibling);}}
  }});
  if(GT_LINKS.support){{var h=document.getElementById('gty-help'),s=document.createElement('a');s.href='mailto:'+GT_LINKS.support;s.textContent=GT_LINKS.support;h.appendChild(document.createTextNode(' Or write to '));h.appendChild(s);h.appendChild(document.createTextNode('.'));}}
}})();
</script>
'''

def email(c, e):
    P = 'margin:0 0 16px;font-family:Verdana,sans-serif;font-size:16px;line-height:1.6'
    a = tokens(c, 'x')['ACCENT_TEXT']; Lk = c.get('links') or {}; out = []
    ps = e['paragraphs']
    for k, p in enumerate(ps):
        s = rich(p)
        def link(m):
            mk = Lk.get(m.group(2)) or ''
            url = '{{membership_contact.login_url}}' if m.group(2) == 'login' else ('mailto:' + mk if re.fullmatch(r'[^@\s:/]+@[^@\s]+', mk) else mk)
            return f'<a href="{url}" style="color:{a};font-weight:bold">{m.group(1)}</a>' if url else f'<b>{m.group(1)}</b>'
        s = re.sub(r'\[([^\]]+)\]\((\w+)\)', link, s)  # [label](login) / [label](portal) / [label](any key in "links")
        out.append(f'<p style="{P if k < len(ps) - 1 else P.replace("0 0 16px", "0")}">{s}</p>')
    return '\n'.join(out) + '\n'

def sheet(c):
    m, bump, ups = c['main'], c.get('bump'), c.get('upsells') or []
    base = f'https://{c["domain"]}/{c["slug"]}'
    o = [f'# GoHighLevel texts and settings: {c["client"]}, {plain(m["name"])}', '', 'Type these exactly. Written by `tools/build_funnel_pages.py`. The steps to place them: the GHL Funnel Playbook (Stages 3 to 10).', '',
         '## Products (catalog name → price)', f'- `{c["client"]} · {plain(m["name"])}` → {m["price"]}']
    if bump: o.append(f'- `{c["client"]} · {plain(bump["name"])}` → {bump["price"]} (Bump Product on the checkout step)')
    o += [f'- `{c["client"]} · {plain(u["name"])}` → {u["price"]} (on the upsell step `{u["slug"]}`)' for u in ups]
    seq = [f'{base}-page', f'{base}-checkout'] + [f'{base}-{u["slug"]}' for u in ups] + [f'{base}-thank-you']
    o += ['', '## Steps and paths'] + [f'{k + 1}. {x}' for k, x in enumerate(seq)]
    o += ['', '## Order form (checkout)', f'- Headline: Contact information', f'- Payment title: Payment details', f'- Button: {m.get("order_button") or "GET INSTANT ACCESS →"}', f'- Button subtext: {L(c, "order_subtext", "One-Time Payment • Instant Access")}', '- Fields: Full Name + Email only. After purchase: Go to the next funnel step.', f'- Left column fragment: `dist/checkout-left.html`, root id `{rootid(c, "c")}`']
    if bump: o += ['', '## Order bump (checkout only, box unticked by default)', f'- Headline: {plain(bump["headline"])}', f'- OTO line: {plain(bump["oto"])}', f'- Description: {plain(bump["description"])}', '- The banner, arrow and image are added by the page, not typed in GHL.', f'- Delivers: {bump["delivers"]}']
    for n, u in enumerate(ups):
        nxt = f'{base}-{ups[n + 1]["slug"]}' if n + 1 < len(ups) else f'{base}-thank-you'
        o += ['', f'## Upsell step `{u["slug"]}`', f'- Fragment: `dist/{u["slug"]}.html`, root id `{rootid(c, "u" if n == 0 else "u%d" % (n + 1))}`', f'- YES button text: {u["yes"]}', '- YES button action: link to = One click up/down sell product; Products = this step\'s product', f'- NO link (Custom Code element under YES): `<a class="gtu-no" href="{nxt}">{html.escape(u["no"], quote=False)}</a>`', f'- Delivers: {u["delivers"]}']
        if n + 1 < len(ups): o.append('- After YES this buyer must skip the next offer. GHL moves YES to the next step, so set it to the thank-you step explicitly, and test it (never run live by us).')
    o += ['', '## Thank-you step', f'- Fragment: `dist/thank-you.html`, root id `{rootid(c, "ty")}`', '', '## Delivery: one workflow per product (Order submitted, Global product Is …)']
    for k, nm in [('main', m['name'])] + ([('bump', bump['name'])] if bump else []) + [(u['slug'], u['name']) for u in ups]:
        e = (c.get('emails') or {}).get(k) or {}
        o.append(f'- Workflow `{c["client"]} · {plain(nm)} delivery`: Global product Is **{c["client"]} · {plain(nm)}** (the prefixed catalog product, not the course\'s own product) → grant the course "{plain(nm)}" only → email `dist/emails/{k}.html` · Subject: {e.get("subject")} · Preview: {e.get("preview")}')
    frm = (c.get('emails') or {}).get('from_name')
    if frm: o.append(f'- From name on every email: {frm}')
    M, Bn = plain(m['name']), plain(bump['name']) if bump else None
    o += ['', '## Who gets what (nobody gets what they did not buy)', '| Bought | Courses | Emails |', '|---|---|---|', f'| Main only | {M} | main |']
    if Bn: o.append(f'| Main + bump | {M}, {Bn} | main, bump |')
    for u in ups: o.append(f'| Main + {plain(u["name"])} | {M}, {plain(u["name"])} | main, {u["slug"]} |')
    if Bn and ups: o.append(f'| Everything | {M}, {Bn}, ' + ', '.join(plain(u['name']) for u in ups) + ' (one login) | all |')
    o += ['', '## Not in this file (from the GHL plan, Stage 1)', 'Funnel name, sales page root id, sender address, buyer tags, course lessons, tax, statement name, tracking.']
    return '\n'.join(o) + '\n'

# ---------- previews (a mock of how GHL renders, so the page can be reviewed before GHL exists) ----------
MOCK_CSS = '''<style>body{margin:0;font-family:Arial,sans-serif}.section-x{padding:20px 0}.c-row{max-width:1170px;margin:0 auto;display:flex;flex-wrap:wrap;padding:10px 5px;box-sizing:border-box}.c-column{flex:1 1 0;min-width:0;padding:10px 5px;box-sizing:border-box}.order-form__surface{padding:10px}.order-form__field-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.order-form__input{width:100%;border:0;border-bottom:1px solid #ccc;height:32px}.order-form__prod{display:flex;justify-content:space-between}.order-form__bump{display:flex;gap:8px;padding:12px}.order-form__bump-headline{text-align:right}.order-form__bump-oto{text-align:right}.order-form__summary-row{display:flex;justify-content:space-between;padding:6px 0}.mock-card{height:150px;border:1px solid #ddd;border-radius:8px;display:flex;align-items:center;justify-content:center;color:#888;font-size:14px;margin:10px 0}.order-form__cta{width:100%;border:0;border-radius:10px;padding:16px;background:%s;color:%s;font-weight:800;font-size:18px}.order-form__cta-sub{display:block;font-size:12px;font-weight:400}.c-button{text-align:center}.mocknote{background:#fffbe6;border-bottom:1px solid #eadf9c;font:12px/1.4 Arial;padding:6px 10px;color:#5c5200}@media(max-width:767px){.c-row{display:block}.order-form__field-grid{grid-template-columns:1fr}}</style>'''
def frame(title, body, note=True): return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title></head><body>{body}</body></html>'
def mock_form(c):
    m, bump = c['main'], c.get('bump'); p = money(m['price']); bp = money((bump or {}).get('price')) or 0
    bh = f'''<div class="order-form__bumps"><div class="order-form__bump"><input type="checkbox" class="order-form__bump-check" id="mb"><div class="order-form__bump-body"><div class="order-form__bump-headline">{rich(bump["headline"])}</div><div class="order-form__bump-oto">{rich(bump["oto"])}</div><div class="order-form__bump-desc">{rich(bump["description"])}</div><div class="order-form__bump-price">{rich(bump["price"])}</div></div></div></div>''' if bump else ''
    return f'''<div class="c-order-form"><div class="order-form__surface"><div class="order-form__headline">Contact information</div><div class="order-form__subheadline">Upgrade Your Order</div><div class="order-form__field-grid"><div class="order-form__control"><label class="order-form__label">Full Name *</label><input class="order-form__input" aria-label="Full Name" type="text"></div><div class="order-form__control"><label class="order-form__label">Email *</label><input class="order-form__input" type="email"></div></div><div class="order-form__offer">Select Product<label class="order-form__prod"><span><input class="order-form__prod-radio" type="radio" checked>{rich(m["name"])}</span><span>{rich(m["price"])}</span></label></div>{bh}<div class="order-form__summary"><div class="order-form__summary-row"><span>Subtotal</span><span>{fmt(p)}</span></div><div class="order-form__summary-row order-form__summary-row--total"><span>Total due today</span><span id="mt">{fmt(p)}</span></div></div><div class="order-form__payment"><div class="order-form__pay-head">Payment details</div><div class="mock-card">card form (GHL / Stripe)</div><button type="button" class="order-form__cta"><span class="order-form__cta-text">{rich(m.get("order_button") or "GET INSTANT ACCESS →")}</span><span class="order-form__cta-sub">One-Time Payment • Instant Access</span></button></div></div></div><script>var mb=document.getElementById('mb');if(mb)mb.onchange=function(){{document.getElementById('mt').textContent=mb.checked?'{fmt(p + bp)}':'{fmt(p)}'}}</script>'''
def previews(c):
    t = tokens(c, 'x'); css = MOCK_CSS.replace('%s', t['ACCENT'], 1).replace('%s', t['ON_ACCENT'], 1); out = {}
    wrap = lambda root, frag: f'<div class="section-x"><div class="c-row"><div class="c-column"><div class="inner"><div class="c-custom-code"><div class="custom-code-container"><div id="{root}">{frag}</div></div></div></div></div></div></div>'
    out['checkout.html'] = frame('Checkout preview', css + f'<div class="section-x"><div class="c-row"><div class="c-column"><div class="inner"><div class="c-custom-code"><div id="{rootid(c, "c")}">{checkout(c)}</div></div></div></div><div class="c-column"><div class="inner">{mock_form(c)}</div></div></div></div>')
    for n, u in enumerate(c.get('upsells') or []):
        yes = f'<div class="section-y"><div class="c-button"><button type="button"><span class="main-heading-group"><span class="main-heading-button">{rich(u["yes"])}</span></span></button></div><div class="c-custom-code"><a class="gtu-no" href="#thank-you">{rich(u["no"])}</a></div></div>'
        out[f'{u["slug"]}.html'] = frame('Upsell preview', css + wrap(rootid(c, 'u' if n == 0 else f'u{n + 1}'), upsell(c, n)) + yes)
    out['thank-you.html'] = frame('Thank-you preview', css + wrap(rootid(c, 'ty'), thankyou(c)))
    ems = ''
    for k, e in (c.get('emails') or {}).items():
        if not isinstance(e, dict): continue
        ems += f'<div style="max-width:640px;margin:24px auto;border:1px solid #ddd;border-radius:10px;padding:20px"><p style="font:13px Arial;color:#666;margin:0 0 4px">{html.escape(k)}</p><h3 style="font:700 18px Arial;margin:0 0 2px">{rich(e.get("subject"))}</h3><p style="font:13px Arial;color:#888;margin:0 0 18px">{rich(e.get("preview"))}</p>{email(c, e)}</div>'
    out['emails.html'] = frame('Email preview', ems)
    return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]; flags = {a for a in sys.argv[1:] if a.startswith('--')}
    if '--help' in flags or '-h' in sys.argv or not args: print(__doc__); sys.exit(0 if args or '--help' in flags else 2)
    src = Path(args[0])
    try: c = json.loads(src.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        line = src.read_text(encoding='utf-8').splitlines()[e.lineno - 1].strip()[:90]
        print(f"can't read {src}: line {e.lineno}: {e.msg}\n  near: {line}\n  Usual causes: a missing or extra comma at the end of the line above, curly quotes (\u201c \u201d) around a name or value, or an unescaped \" inside a text (write \\\")."); sys.exit(2)
    except Exception as e: print(f"can't read {src}: {e}"); sys.exit(2)
    global BASE, PREVIEW
    BASE = src.parent
    sales = None; R = Report(c.get('accepted'))
    if c.get('sales_page'):
        p = (src.parent / c['sales_page'])
        if p.exists(): sales = plain(re.sub(r'<(style|script)[\s\S]*?</\1>', ' ', p.read_text(encoding='utf-8', errors='ignore')))
        else: R.e(f'sales_page: {p} does not exist, so "the bump is not on the sales page" was not checked')
    else: R.w('sales_page is not set, so "the bump is not on the sales page" was not checked; read the live sales page yourself', 'sales_page')
    validate(c, sales, R)
    if not c.get('assets_base') and any(isinstance(v, str) and re.search(r'\.(webp|png|jpe?g|svg)$', v, re.I) and not re.match(r'^\w+:', v) for _, v in walk(c)): R.w('assets_base is empty and some images are relative: fine for previews, but the live pages need their public URL', 'assets_base')
    out = src.parent
    if '--check' not in flags:
        try:
            files = {'dist/checkout-left.html': checkout(c), 'dist/thank-you.html': thankyou(c), 'dist/ghl-texts.md': sheet(c)}
            for n, u in enumerate(c.get('upsells') or []): files[f'dist/{u["slug"]}.html'] = upsell(c, n)
            for k, e in (c.get('emails') or {}).items():
                if isinstance(e, dict): files[f'dist/emails/{k}.html'] = email(c, e)
            PREVIEW = True
            for k, v in previews(c).items(): files[f'preview/{k}'] = v
            for k, v in files.items():
                f = out / k; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(re.sub(r'\n[ \t]+\n', '\n', v), encoding='utf-8')
            print('Wrote: ' + ', '.join(files))
        except (KeyError, TypeError, ValueError) as e: R.e(f'could not build, a field is missing or has the wrong shape: {e!r}')
    for x in R.err: print('FIX  ', x)
    for x in R.warn: print('CHECK', x)
    for x in R.ok: print('OK\'D ', x)
    bad = bool(R.err) or ('--final' in flags and bool(R.warn))
    print(f'{len(R.err)} to fix, {len(R.warn)} to check. ' + ('Not ready.' if bad else 'OK.'))
    sys.exit(1 if bad else 0)

if __name__ == '__main__': main()
