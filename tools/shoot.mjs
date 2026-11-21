#!/usr/bin/env node
// shoot.mjs: screenshots + above-the-fold measurements for a sales page, with no installs.
// Drives your installed Google Chrome over the DevTools protocol (Node 22+, built-in WebSocket).
//
// Usage:
//   node tools/shoot.mjs <url-or-file> [--out DIR] [--views mobile,desktop,1280,1920] [--full] [--json]
// Examples:
//   node tools/shoot.mjs my-sales-page/index.html --out my-sales-page/shots --full
//   node tools/shoot.mjs https://example.github.io/page/ --json        (measurements only, printed as JSON)
//
// Views: mobile = 393x852 (iPhone 16, touch, DPR 2) · desktop = 1440x900 · 1280 = 1280x800 · 1920 = 1920x1080
// What it measures per view (see measureScript below): hero headline / image / first button bottoms vs the
// screen height, sideways scroll, broken images, placeholder text, the sticky bar, section count.

import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync, existsSync, mkdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
if (!args.length || args[0] === '-h' || args[0] === '--help') {
  console.log('Usage: node tools/shoot.mjs <url-or-file> [--out DIR] [--views mobile,desktop] [--full] [--json]');
  process.exit(0);
}
let target = args[0];
const opt = (name, def) => { const i = args.indexOf(name); return i > -1 ? args[i + 1] : def; };
const outDir = opt('--out', null);
const views = opt('--views', 'mobile,desktop').split(',');
const full = args.includes('--full');
const jsonOnly = args.includes('--json');
if (!/^https?:|^file:/.test(target)) target = pathToFileURL(resolve(target)).href;

const VIEWS = {
  mobile: { width: 393, height: 852, deviceScaleFactor: 2, mobile: true },
  desktop: { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false },
  '1280': { width: 1280, height: 800, deviceScaleFactor: 1, mobile: false },
  '1920': { width: 1920, height: 1080, deviceScaleFactor: 1, mobile: false },
};

const CHROME_PATHS = [
  process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
].filter(Boolean);
const chromePath = CHROME_PATHS.find(p => existsSync(p));
if (!chromePath) { console.error('Google Chrome not found. Set CHROME_PATH=/path/to/chrome'); process.exit(2); }
if (typeof WebSocket === 'undefined') { console.error('Needs Node 22+ (built-in WebSocket).'); process.exit(2); }

// Runs inside the page. Generic: works on kit pages (section[data-section]) and on any page.
const measureScript = `(() => {
  const H = innerHeight, W = innerWidth;
  const r = el => el ? el.getBoundingClientRect() : null;
  const hero = document.querySelector('section[data-section="1"]') || document.querySelector('header, section, main > *');
  const scope = hero || document.body;
  const h1 = document.querySelector('h1');
  const imgs = [...scope.querySelectorAll('img')].filter(i => i.offsetWidth > 120 && !/logo/i.test((i.className || '') + ' ' + (i.alt || '') + ' ' + (i.getAttribute('src') || '')));
  const heroImg = imgs[0] || null;
  const btns = [...document.querySelectorAll('a.btn, button.btn, .cta a, a[class*="btn"], a[class*="button"]')]
    .filter(b => b.offsetParent && !b.closest('[class*="sticky"], .sticky, .stick, [id*="sticky"]'));
  const firstBtn = btns[0] || null;
  const bottom = el => el ? Math.round(r(el).bottom + scrollY) : null;
  const broken = [...document.images].filter(i => i.complete && i.naturalWidth === 0 && !(i.loading === 'lazy' && r(i).top > H * 2)).map(i => i.currentSrc || i.src).slice(0, 10);
  const text = document.body.innerText;
  const placeholders = (text.match(/\\[(insert|placeholder|image|screenshot|photo|your |customer name|total value)[^\\]]*\\]|lorem ipsum|PASTE-YOUR/gi) || []).slice(0, 10);
  const dashes = (text.match(/[\\u2014\\u2013]/g) || []).length;
  const labels = btns.map(b => b.innerText.trim().replace(/\\s+/g, ' ')).filter(Boolean);
  const sticky = document.querySelector('[class*="sticky"], .stick, [id*="sticky"]');
  return {
    viewport: { w: W, h: H },
    sideways_scroll_px: Math.max(0, document.documentElement.scrollWidth - W),
    headline: h1 ? { text: h1.innerText.trim().slice(0, 140), bottom: bottom(h1), in_fold: bottom(h1) <= H } : null,
    hero_image: heroImg ? { src: (heroImg.currentSrc || heroImg.src).split('/').pop(), bottom: bottom(heroImg), in_fold: bottom(heroImg) <= H } : null,
    first_button: firstBtn ? { text: firstBtn.innerText.trim().replace(/\\s+/g, ' '), bottom: bottom(firstBtn), in_fold: bottom(firstBtn) <= H, href: firstBtn.getAttribute('href') } : null,
    button_labels: [...new Set(labels)],
    sections: document.querySelectorAll('section').length,
    sticky_bar_present: !!sticky,
    broken_images: broken,
    placeholders,
    dash_count: dashes,
    page_height: document.documentElement.scrollHeight,
  };
})()`;

const userDir = mkdtempSync(join(tmpdir(), 'shoot-'));
const port = 9300 + Math.floor(Math.random() * 500);
const chrome = spawn(chromePath, [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check',
  `--remote-debugging-port=${port}`, `--user-data-dir=${userDir}`, 'about:blank',
], { stdio: 'ignore' });

const sleep = ms => new Promise(r => setTimeout(r, ms));
async function getWsUrl() {
  for (let i = 0; i < 60; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
      const page = list.find(t => t.type === 'page');
      if (page) return page.webSocketDebuggerUrl;
    } catch {}
    await sleep(250);
  }
  throw new Error('Chrome did not start');
}

function connect(url) {
  return new Promise((res, rej) => {
    const ws = new WebSocket(url);
    let id = 0; const pending = new Map(); const listeners = [];
    ws.onmessage = ev => {
      const m = JSON.parse(ev.data);
      if (m.id && pending.has(m.id)) { const { resolve, reject } = pending.get(m.id); pending.delete(m.id); m.error ? reject(new Error(m.error.message)) : resolve(m.result); }
      else listeners.forEach(l => l(m));
    };
    ws.onopen = () => res({
      send: (method, params = {}) => new Promise((resolve, reject) => { const i = ++id; pending.set(i, { resolve, reject }); ws.send(JSON.stringify({ id: i, method, params })); }),
      on: fn => listeners.push(fn),
      close: () => ws.close(),
    });
    ws.onerror = rej;
  });
}

const results = {};
try {
  const cdp = await connect(await getWsUrl());
  await cdp.send('Page.enable'); await cdp.send('Runtime.enable');
  for (const v of views) {
    const vp = VIEWS[v]; if (!vp) { console.error('Unknown view', v); continue; }
    await cdp.send('Emulation.setDeviceMetricsOverride', vp);
    await cdp.send('Emulation.setTouchEmulationEnabled', { enabled: vp.mobile });
    if (vp.mobile) await cdp.send('Emulation.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1' });
    await cdp.send('Page.navigate', { url: target });
    await sleep(4500); // fonts, images, reveal animations
    // Force scroll-reveal content visible for full-page shots, then measure at the top.
    await cdp.send('Runtime.evaluate', { expression: 'document.querySelectorAll(".r,.reveal,[data-reveal]").forEach(e=>e.classList.add("in","is-in","show","visible"));[...document.querySelectorAll("button,a,div")].filter(e=>/^\\W*(Edit layout|Save draft)$/i.test((e.textContent||"").trim())&&e.textContent.trim().length<20).forEach(e=>e.style.display="none");window.scrollTo(0,0)' });
    await sleep(600);
    const m = await cdp.send('Runtime.evaluate', { expression: measureScript, returnByValue: true });
    results[v] = m.result.value;
    if (outDir && !jsonOnly) {
      mkdirSync(outDir, { recursive: true });
      const fold = await cdp.send('Page.captureScreenshot', { format: 'png' });
      writeFileSync(join(outDir, `${v}-${vp.width}x${vp.height}-fold.png`), Buffer.from(fold.data, 'base64'));
      if (full) {
        // Scroll through once so lazy images and videos load, then capture the whole page.
        await cdp.send('Runtime.evaluate', { expression: '(async()=>{for(let y=0;y<document.documentElement.scrollHeight;y+=innerHeight*0.8){scrollTo(0,y);await new Promise(r=>setTimeout(r,250));}scrollTo(0,0);})()', awaitPromise: true });
        await sleep(1500);
        // Hide fixed bars (sticky CTA) so they don't sit over the content, then capture in parts of 12,000px.
        await cdp.send('Runtime.evaluate', { expression: '[...document.querySelectorAll("body *")].filter(e=>getComputedStyle(e).position==="fixed").forEach(e=>e.style.display="none")' });
        const h = results[v].page_height, part = 12000;
        for (let y = 0, n = 1; y < h; y += part, n++) {
          const shot = await cdp.send('Page.captureScreenshot', { format: 'jpeg', quality: 70, captureBeyondViewport: true, clip: { x: 0, y, width: vp.width, height: Math.min(part, h - y), scale: vp.mobile ? 1 : 0.6 } });
          writeFileSync(join(outDir, `${v}-${vp.width}-full${h > part ? '-' + n : ''}.jpg`), Buffer.from(shot.data, 'base64'));
        }
      }
    }
  }
  cdp.close();
} catch (e) {
  console.error('shoot failed:', e.message); process.exitCode = 1;
} finally {
  chrome.kill('SIGKILL');
  try { rmSync(userDir, { recursive: true, force: true }); } catch {}
}
console.log(JSON.stringify(results, null, 2));
