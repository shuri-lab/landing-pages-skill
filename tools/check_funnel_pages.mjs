#!/usr/bin/env node
// check_funnel_pages.mjs: looks at the previews from build_funnel_pages.py in real Chrome, at phone and desktop size.
//   node tools/check_funnel_pages.mjs my-funnel-pages [--json]
// Reads my-funnel-pages/preview/*.html, saves full-page screenshots in my-funnel-pages/shots/, prints PASS/FAIL per page and size.
// Exit code: 0 all PASS, 1 any FAIL, 2 can't run. Needs Node 22+ and Google Chrome (or CHROME_PATH). It never buys or submits anything.
// What it can't judge: whether the copy sells. Read stages/funnel-5-review-and-handoff.md and look at the screenshots.
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync, existsSync, mkdirSync, rmSync, readdirSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2), dir = args.find(a => !a.startsWith('-')), jsonOnly = args.includes('--json');
if (!dir || args.includes('--help')) { console.log('Usage: node tools/check_funnel_pages.mjs <my-funnel-pages folder> [--json]'); process.exit(dir ? 0 : 2); }
const prev = join(dir, 'preview'), shots = join(dir, 'shots');
if (!existsSync(prev)) { console.error(`No ${prev}. Run build_funnel_pages.py first.`); process.exit(2); }
let cfg; try { cfg = JSON.parse(readFileSync(join(dir, 'funnel-pages.json'), 'utf8')); } catch (e) { console.error(`Can't read funnel-pages.json: ${e.message}`); process.exit(2); }
const ups = (cfg.upsells || []).map(u => u.slug);
const typeOf = f => f === 'checkout.html' ? 'checkout' : f === 'thank-you.html' ? 'thankyou' : f === 'emails.html' ? 'emails' : ups.includes(f.replace('.html', '')) ? 'upsell' : null;
const files = readdirSync(prev).filter(f => f.endsWith('.html') && typeOf(f));
for (const u of ups) if (!files.includes(u + '.html')) { console.error(`preview/${u}.html is missing. Run build_funnel_pages.py again.`); process.exit(2); }
const VIEWS = { phone: { width: 393, height: 852, deviceScaleFactor: 2, mobile: true }, desktop: { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false }, 1280: { width: 1280, height: 800, deviceScaleFactor: 1, mobile: false }, 1920: { width: 1920, height: 1080, deviceScaleFactor: 1, mobile: false } };
const chromePath = [process.env.CHROME_PATH, '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium', 'C:/Program Files/Google/Chrome/Application/chrome.exe'].filter(Boolean).find(p => existsSync(p));
if (!chromePath || typeof WebSocket === 'undefined') { console.error('Needs Google Chrome and Node 22+.'); process.exit(2); }

const probe = (type) => `(async () => {
  const H = innerHeight, W = document.documentElement.clientWidth, $ = s => document.querySelector(s), bot = e => e ? Math.round(e.getBoundingClientRect().bottom + scrollY) : null, top = e => e ? Math.round(e.getBoundingClientRect().top + scrollY) : null;
  const vis = e => !!(e && e.offsetParent !== null);
  for (let y = 0; y < document.documentElement.scrollHeight; y += H * .7) { scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } scrollTo(0, 0); await new Promise(r => setTimeout(r, 600));
  const r = { W, H, sideways: Math.max(0, document.documentElement.scrollWidth - W), height: document.documentElement.scrollHeight,
    wide: [...document.querySelectorAll('body *')].filter(e => vis(e) && e.getBoundingClientRect().right > W + 1 && !e.closest('.bar')).slice(0, 4).map(e => (e.className || e.tagName).toString().slice(0, 30)),
    broken: [...document.images].filter(i => vis(i) && i.complete && !i.naturalWidth).map(i => i.src.split('/').pop()).slice(0, 5),
    tiny: [...new Set([...document.querySelectorAll('#gtu *, #gtc *, #gty *')].filter(e => vis(e) && e.childNodes.length && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 2) && parseFloat(getComputedStyle(e).fontSize) < 11).map(e => e.className || e.tagName))].slice(0, 4) };
  // contrast of every visible text against the nearest solid background behind it
  const px = c => { const m = c.match(/[\\d.]+/g); return m ? m.map(Number) : [0, 0, 0, 0]; }, lum = c => { const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4; }; return .2126 * f(c[0]) + .7152 * f(c[1]) + .0722 * f(c[2]); };
  const bgOf = e => { for (let n = e; n; n = n.parentElement) { const st = getComputedStyle(n), c = px(st.backgroundColor); if (st.backgroundImage !== 'none') return null; if (c.length < 4 ? st.backgroundColor !== 'transparent' : c[3] > .95) return c; if (c[3] > 0.02) return null; } return [255, 255, 255]; };
  const low = {};
  document.querySelectorAll('#gtu *, #gtc *, #gty *, .gtu-yes, .gtu-no, .c-order-form *').forEach(e => { if (!vis(e) || e.closest('.mock-card') || e.disabled) return; if (![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1)) return; const st = getComputedStyle(e), fg = px(st.color), bg = bgOf(e); if (!bg || e.closest('.off')) return; const A = fg[3] === undefined ? 1 : fg[3], mixc = fg.slice(0, 3).map((v, i) => v * A + bg[i] * (1 - A)), a = lum(mixc), b = lum(bg), k = (Math.max(a, b) + .05) / (Math.min(a, b) + .05), size = parseFloat(st.fontSize), big = size >= 24 || (size >= 18.5 && +st.fontWeight >= 700), crossed = !!e.closest('s'); const need = big || crossed ? 3 : 4.5; if (k < need) low[(e.className || e.parentElement.className || e.tagName).toString().slice(0, 24) + ' "' + e.textContent.trim().slice(0, 18) + '"'] = k.toFixed(1); });
  r.low = Object.entries(low).slice(0, 8).map(([k, v]) => k + ' ' + v + ':1');
  // logos: compare the logo's average visible color with what is behind it
  r.logo = []; for (const im of document.querySelectorAll('#gtc .lg, .gtc-m .mlg, #gty .lg')) { if (!vis(im) || !im.naturalWidth) continue; try { const c = document.createElement('canvas'); c.width = 120; c.height = 40; const x = c.getContext('2d'); x.drawImage(im, 0, 0, 120, 40); const d = x.getImageData(0, 0, 120, 40).data; let n = 0, t = [0, 0, 0]; for (let i = 0; i < d.length; i += 4) if (d[i + 3] > 120) { n++; t[0] += d[i]; t[1] += d[i + 1]; t[2] += d[i + 2]; } if (!n) continue; const a = lum(t.map(v => v / n)), b = lum(bgOf(im.parentElement) || [255, 255, 255]), k = (Math.max(a, b) + .05) / (Math.min(a, b) + .05); if (k < 2) r.logo.push((im.className || 'logo') + ' ' + k.toFixed(1) + ':1'); } catch {} }
  if (${JSON.stringify(type)} === 'checkout') {
    const f = [...document.querySelectorAll('.c-order-form .order-form__input')].find(vis), t = () => $('.order-form__summary-row--total').innerText.replace(/\\s+/g, ' ');
    r.first_field_bottom = bot(f); r.select_hidden = !vis($('.order-form__offer'));
    const b = $('.order-form__bump-check');
    if (b) { r.bump = { ticked_by_default: b.checked, before: t() }; b.click(); await new Promise(x => setTimeout(x, 700)); r.bump.after = t(); b.click(); await new Promise(x => setTimeout(x, 400)); r.bump.back = t();
      r.bump.banner = document.querySelectorAll('.gt-bump-top').length; r.bump.arrow = document.querySelectorAll('.gt-arrow').length; r.bump.img = document.querySelectorAll('.gt-bump-img').length; r.bump.align = getComputedStyle($('.order-form__bump-oto')).textAlign;
      r.bump.height = Math.round($('.order-form__bump').getBoundingClientRect().height); }
  }
  if (${JSON.stringify(type)} === 'upsell') {
    r.alert_top = top($('#gtu .alert')); r.alert_bottom = bot($('#gtu .alert')); r.prog_bottom = bot($('#gtu .prog')); r.h1_bottom = bot($('#gtu h1'));
    r.media_top = top($('#gtu .shot') || $('#gtu .vid')); r.items = document.querySelectorAll('#gtu .item').length; r.price = ($('#gtu .now b') || {}).innerText;
    const y = $('.gtu-yes'), n = $('.gtu-no'); r.yes = y ? { w: Math.round(y.getBoundingClientRect().width), lines: Math.round(y.getBoundingClientRect().height), bg: getComputedStyle(y).backgroundColor } : null; r.no = n ? { align: getComputedStyle(n).textAlign } : null;
    r.offer_before_yes = !!(y && top($('#gtu .offer')) < top(y));
  }
  if (${JSON.stringify(type)} === 'thankyou') { r.steps = document.querySelectorAll('#gty .step').length; r.grey = [...document.querySelectorAll('#gty .btn.off')].map(b => b.innerText.trim()); r.first_button_bottom = bot($('#gty .btn')); }
  return r;
})()`;
const judge = (type, view, r) => {
  const f = [], w = [], phone = view === 'phone';
  if (r.sideways) f.push(`sideways scroll ${r.sideways}px (${r.wide.join(', ')})`);
  if (r.broken.length) f.push(`images that don't load: ${r.broken.join(', ')}`);
  if (r.low && r.low.length) w.push(`hard to read (contrast): ${r.low.join(' | ')}`);
  if (r.logo && r.logo.length) f.push(`a logo nearly disappears on its background: ${r.logo.join(', ')} (logo_on_light needs a DARK logo, logo_on_dark a LIGHT one)`);
  if (r.tiny.length) w.push(`text under 11px: ${r.tiny.join(', ')}`);
  if (type === 'checkout') {
    if (phone && !(r.first_field_bottom <= r.H)) f.push(`first form field ends at ${r.first_field_bottom}px, below the first screen (${r.H})`);
    if (phone && r.first_field_bottom > 470) w.push(`first field ends at ${r.first_field_bottom}px; aim for the top half of the screen`);
    if (!r.select_hidden) f.push('"Select product" is visible');
    if (cfg.bump && !r.bump) f.push('no order bump');
    if (r.bump) { const b = r.bump; if (b.ticked_by_default) f.push('the bump is ticked by default'); if (b.before === b.after || b.before !== b.back) f.push(`totals wrong: ${b.before} / ${b.after} / ${b.back}`);
      if (b.banner !== 1 || b.arrow !== 1 || b.img !== 1) f.push(`bump banner/arrow/image count is ${b.banner}/${b.arrow}/${b.img}, expected 1/1/1`); if (b.align !== 'left') f.push('bump text is not left-aligned'); if (phone && b.height > 330) w.push(`bump box is ${b.height}px tall on a phone; shorten the text`); }
  }
  if (type === 'upsell') {
    if (r.alert_top > 1) f.push(`alert bar starts at ${r.alert_top}px, not at the very top`);
    if (phone && r.alert_bottom > 230) w.push(`alert bar is ${r.alert_bottom}px tall on a phone; shorten it`);
    if (phone && !(r.h1_bottom <= r.H)) f.push(`headline ends at ${r.h1_bottom}px, below the first screen`);
    if (phone && !(r.media_top < r.H - 60)) w.push('the product image or video does not show on the first phone screen');
    if (!r.yes) f.push('YES button not styled'); if (!r.no) f.push('NO link not found');
    if (r.yes && phone && r.yes.w < 300) f.push(`YES button only ${r.yes.w}px wide`);
    if (!r.offer_before_yes) f.push('the offer stack must come before the YES button');
  }
  if (type === 'thankyou') { if (r.steps < 1) f.push('no steps'); if (r.grey.length) w.push(`greyed buttons (links missing): ${r.grey.join(', ')}`); if (phone && r.first_button_bottom > r.H) w.push('the first button is below the first phone screen'); }
  return { f, w };
};

const userDir = mkdtempSync(join(tmpdir(), 'fp-')), port = 9800 + Math.floor(Math.random() * 190), sleep = ms => new Promise(r => setTimeout(r, ms));
const chrome = spawn(chromePath, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check', '--allow-file-access-from-files', `--remote-debugging-port=${port}`, `--user-data-dir=${userDir}`, 'about:blank'], { stdio: 'ignore' });
let ok = true; const all = [];
try {
  let url; for (let i = 0; i < 60 && !url; i++) { try { url = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find(t => t.type === 'page')?.webSocketDebuggerUrl; } catch {} if (!url) await sleep(250); }
  if (!url) throw new Error('Chrome did not start');
  const ws = new WebSocket(url), pend = new Map(); let id = 0; await new Promise((a, b) => { ws.onopen = a; ws.onerror = b; });
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { const [a, b] = pend.get(m.id); pend.delete(m.id); m.error ? b(new Error(m.error.message)) : a(m.result); } };
  const send = (method, params = {}) => new Promise((a, b) => { const i = ++id; pend.set(i, [a, b]); ws.send(JSON.stringify({ id: i, method, params })); });
  await send('Page.enable'); await send('Runtime.enable'); mkdirSync(shots, { recursive: true });
  for (const file of files) for (const [view, vp] of Object.entries(VIEWS)) {
    const type = typeOf(file); if (type === 'emails' && view !== 'phone') continue;
    await send('Emulation.setDeviceMetricsOverride', vp); await send('Emulation.setTouchEmulationEnabled', { enabled: vp.mobile });
    await send('Page.navigate', { url: pathToFileURL(resolve(prev, file)).href }); await sleep(4000);
    const res = await send('Runtime.evaluate', { expression: probe(type), returnByValue: true, awaitPromise: true });
    if (res.exceptionDetails) throw new Error(`${file}: ${res.exceptionDetails.exception?.description || res.exceptionDetails.text}`);
    const r = res.result.value, { f, w } = judge(type, view, r); if (f.length) ok = false; all.push({ file, view, fails: f, warns: w, measured: r });
    const name = file.replace('.html', '') + '-' + view;
    if (view === '1280' || view === '1920') { const fs = await send('Page.captureScreenshot', { format: 'png' }); writeFileSync(join(shots, name + '-first-screen.png'), Buffer.from(fs.data, 'base64')); if (!jsonOnly) { console.log(`${f.length ? 'FAIL' : 'PASS'}  ${file} (${view})`); f.forEach(x => console.log('      FIX   ' + x)); } continue; }
    const fold = await send('Page.captureScreenshot', { format: 'png' }); writeFileSync(join(shots, name + '-first-screen.png'), Buffer.from(fold.data, 'base64'));
    const full = await send('Page.captureScreenshot', { format: 'jpeg', quality: 75, captureBeyondViewport: true, clip: { x: 0, y: 0, width: vp.width, height: Math.min(r.height, 12000), scale: vp.mobile ? 1 : .7 } }); writeFileSync(join(shots, name + '-full.jpg'), Buffer.from(full.data, 'base64'));
    if (type === 'checkout' && r.bump) { await send('Runtime.evaluate', { expression: "document.querySelector('.order-form__bump-check').click();document.querySelector('.order-form__bump').scrollIntoView({block:'center'})" }); await sleep(700); const t = await send('Page.captureScreenshot', { format: 'png' }); writeFileSync(join(shots, name + '-bump-ticked.png'), Buffer.from(t.data, 'base64')); }
    if (!jsonOnly) { console.log(`${f.length ? 'FAIL' : 'PASS'}  ${file} (${view})`); f.forEach(x => console.log('      FIX   ' + x)); w.forEach(x => console.log('      CHECK ' + x)); }
  }
  ws.close();
} catch (e) { console.error('check failed:', e.message); ok = false; } finally { chrome.kill('SIGKILL'); try { rmSync(userDir, { recursive: true, force: true }); } catch {} }
if (jsonOnly) console.log(JSON.stringify(all, null, 2)); else console.log(ok ? `All pages pass the automatic checks. That is not "finished": open every screenshot in ${shots}, settle the CHECK lines, and read the copy as the buyer.` : 'Not ready.');
process.exitCode = ok ? 0 : 1;
