#!/usr/bin/env python3
"""probes.py: breaks a good funnel-pages.json in ways that must never reach a buyer, and checks the builder refuses each one.
   python3 test/part-2/probes.py      (exit 0 = every probe caught)"""
import copy, json, shutil, subprocess, sys, tempfile
from pathlib import Path
R = Path(__file__).resolve().parents[2]; good = json.loads((R / 'test/part-2/reference/funnel-pages.json').read_text(encoding='utf-8'))
good['sales_page'] = 'sales.html'
def run(j, sales='<h1>Bake your first loaf</h1>'):
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / 'sales.html').write_text(sales); shutil.copytree(R / 'test/part-2/reference/images', Path(d) / 'images'); f = Path(d) / 'funnel-pages.json'; f.write_text(json.dumps(j), encoding='utf-8')
        o = subprocess.run([sys.executable, str(R / 'tools/build_funnel_pages.py'), str(f), '--check'], capture_output=True, text=True); return o.returncode, o.stdout + o.stderr
def setp(path, v):
    def go(j):
        o = j
        for k in path[:-1]: o = o[k]
        o[path[-1]] = v
    return go
U = ('upsells', 0); G = good['upsells'][0]
P = [
 ('bump number invented', setp(('bump', 'description'), 'Stop guessing. Get my sheet of 30+ fixes, so you know what to do tonight.')),
 ('claim with a number', setp(U + ('headline',), 'You Just Unlocked Your First Loaf. Now Bake 10x Better…')),
 ('YES price wrong digit', setp(U + ('yes',), 'YES! Add The Bakery-Style Bread System to My Order For Only $870')),
 ('OTO price wrong digit', setp(('bump', 'oto'), 'Only $120 today. One-time payment.')),
 ('main guarantee pasted on the upsell', setp(U + ('guarantee',), good['main']['guarantee'])),
 ('today-only', setp(U + ('lead_1',), 'This is a today-only offer.')),
 ('today only', setp(U + ('lead_1',), 'Today only.')),
 ('last chance, closes at midnight', setp(U + ('lead_2',), 'Last chance! This closes at midnight.')),
 ('spots left', setp(U + ('lead_2',), 'Only 7 spots left.')),
 ('insulting NO', setp(U + ('no',), "No thanks, I'm too lazy to bake good bread.")),
 ('70-word sub', setp(U + ('sub',), 'word ' * 70)),
 ('double dash', setp(U + ('sub',), 'The system -- for every loaf.')),
 ('em dash', setp(U + ('sub',), 'The system — for every loaf.')),
 ('income promise', setp(U + ('sub',), 'Earn $500 a week selling bread.')),
 ('bump short name in the main email', lambda j: j['emails']['main']['paragraphs'].append('Your Fix-It Sheet is in there too.')),
 ('upsell short name in the main email', lambda j: j['emails']['main']['paragraphs'].append('And the Bread System.')),
 ('login link is a file', setp(('links', 'course'), 'https://host.test/x.pdf')),
 ('file-sharing link on thank-you', setp(('links', 'course'), 'https://drive.google.com/file/d/1')),
 ('thank-you sells', setp(('thankyou', 'sub'), 'Add the System for $87 now.')),
 ('bad support email', setp(('links', 'support'), 'hello at bakery')),
 ('email link with an unknown key', lambda j: j['emails']['main']['paragraphs'].append('[Join](whatsapp)')),
 ('no sources', setp(('sources',), {})),
 ('total not above the price', setp(U + ('items',), [dict(G['items'][0], value='$50')])),
 ('Rickey text left in', setp(U + ('sub',), 'Get your Headstart course with Rickey.')),
 ('placeholder left in', setp(U + ('sub',), 'REPLACE-ME')),
 ('sold elsewhere but "only here"', setp(U + ('sold_elsewhere',), True)),
 ('quote without a source', setp(('thankyou', 'quote'), {'text': 'You can do it.', 'by': 'Nora'})),
 ('proof without a source', setp(U + ('proof',), [{'text': 'Great', 'by': 'A'}])),
 ('missing sales page file', setp(('sales_page',), 'nope.html')),
 ('amount that is not in the offer', setp(U + ('price_note',), 'Normally $400.')),
 ('email missing', lambda j: j['emails'].pop('bump')),
 ('flag as text', setp(('main', 'guarantee_covers_bump'), 'no')),
 ('10x in alert 2', setp(U + ('alert_2',), 'Stay here and get 10x better bread.')),
 ('10x in the questions', setp(U + ('faq',), [{'q': 'Is it good?', 'a': 'Yes, 10x better.'}])),
 ('number word claim', setp(U + ('headline',), 'Now bake ten times better bread')),
 ('number in the bump banner', setp(('bump', 'banner'), 'Get 30+ fixes')),
 ('number in an email', lambda j: j['emails']['bump']['paragraphs'].append('It has 30+ fixes.')),
 ('number in a stack item name', lambda j: j['upsells'][0]['items'][1].update(name='The 99-Page Calculator')),
 ('just for today', setp(U + ('lead_1',), 'This price is just for today.')),
 ('disappears at 12am', setp(U + ('lead_2',), 'This deal disappears at 12am.')),
 ('trust longer than the guarantee', setp(('main', 'trust'), ['One-time payment', 'Instant access', '90-day refund'])),
 ('source that says nothing', setp(U + ('guarantee_source',), 'x')),
 ('CHECK accepted with "ok"', setp(('accepted',), {'legal': 'ok'})),
 ('short name without the hyphen', lambda j: j['emails']['main']['paragraphs'].append('Your Fix It Sheet is ready.')),
 ('upsell stack item in the main email', lambda j: j['emails']['main']['paragraphs'].append('And the Bake Calculator.')),
 ('upsell named in the bump email', lambda j: j['emails']['bump']['paragraphs'].append('So is The Bakery-Style Bread System.')),
 ('bump stated as included on thank-you', lambda j: j['thankyou']['steps'][0].update(text='Your Sourdough Fix-It Sheet is inside your course.')),
 ('thank-you sells in words', lambda j: j['thankyou']['steps'][0].update(text='Want more? Buy the next course.')),
 ('file on a notes site', setp(('links', 'course'), 'https://x.notion.site/pdf')),
 ('missing image', setp(('bump', 'image'), 'nope.webp')),
 ('bump sold elsewhere not asked', lambda j: j['bump'].pop('sold_elsewhere')),
]
rc, out = run(good); bad = 0
if rc: print('REFERENCE IS NOT CLEAN\n' + out); sys.exit(1)
for name, f in P:
    j = copy.deepcopy(good); f(j); rc, out = run(j); ok = rc == 1; bad += not ok; print(('caught  ' if ok else 'MISSED  ') + name)
rc, _ = run(good, '<p>Also get The Sourdough Fix-It Sheet</p>'); ok = rc == 1; bad += not ok; print(('caught  ' if ok else 'MISSED  ') + 'bump named on the sales page')
print(f'{len(P) + 1 - bad} of {len(P) + 1} caught'); sys.exit(1 if bad else 0)
