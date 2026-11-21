# Reusable snippets (from the Rickey build)

## Appendix: reusable snippets (from the session; the scratchpad copies are temporary)

**1. Render PDF pages to PNG and dump text (macOS, no poppler).** Usage: `osascript -l JavaScript pdf2png.js "<file.pdf>" <outdir> 1400`

```js
ObjC.import('PDFKit'); ObjC.import('AppKit');
function run(argv){
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  var out = argv[1], W = parseFloat(argv[2]||'1400'), txt='';
  for (var i=0;i<doc.pageCount;i++){
    var p = doc.pageAtIndex(i), b = p.boundsForBox(0), s = W/b.size.width;
    var img = p.thumbnailOfSizeForBox($.NSMakeSize(b.size.width*s, b.size.height*s), 0);
    var rep = $.NSBitmapImageRep.imageRepWithData(img.TIFFRepresentation);
    var png = rep.representationUsingTypeProperties(4, $());
    var n = ('0'+(i+1)).slice(-2);
    png.writeToFileAtomically(out+'/page-'+n+'.png', true);
    txt += '=== page '+n+'\n'+ (p.string.js||'') + '\n';
  }
  return txt;
}
```
The page-limited variant `pdf2png-n.js` uses `var N=Math.min(doc.pageCount, parseInt(argv[3]||"999"))` and prints `PAGES <count>`.

**2. Trim logo whitespace:**
- `bbox.py` decodes a PNG in pure Python (zlib plus the filters) and finds the non-transparent bounding box (alpha > 16, or any channel < 240 for RGB). It prints `H W Y X`, with an optional pad argument.
- Then: `read H W Y X <<< "$(python3 -I bbox.py in.png 6)"; sips -c $H $W --cropOffset $Y $X in.png --out out.png`. Run it on a 1200 px copy, made with `sips -Z 1200`.

**3. Contrast (WCAG):**
```python
def L(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]
    return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b): a,b=L(a),L(b); return (max(a,b)+0.05)/(min(a,b)+0.05)
```

**4. Cloudinary light video and poster:**
- Video: `https://res.cloudinary.com/<cloud>/video/upload/w_360,q_auto,ac_none,du_12/<version>/<id>.mp4` (width 360, auto quality, no audio, 12 s).
- Poster: `https://res.cloudinary.com/<cloud>/video/upload/w_360,so_1/<version>/<id>.jpg` (a frame at 1 s).
- Markup: `<video muted loop playsinline preload="none" data-src="…mp4" poster="…jpg" aria-label="what it shows">`.

**5. QA helpers (Browser pane JS):**
```js
document.documentElement.classList.remove('anim');document.documentElement.style.scrollBehavior='auto';
window.__go=(n,d)=>{const s=document.querySelector(n==='f'?'footer':'section[data-section="'+n+'"]');window.scrollTo(0,s.getBoundingClientRect().top+scrollY+(d||0));return s.offsetHeight};
// overflow at phone width
[innerWidth, document.documentElement.scrollWidth, [...document.querySelectorAll('#page *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>innerWidth+1 && !e.closest('.slider') && getComputedStyle(e).position!=='fixed'}).slice(0,8).map(e=>e.tagName+'.'+e.className)]
// broken images
[...document.images].filter(i=>!(i.complete&&i.naturalWidth>0)).map(i=>i.getAttribute('src'))
// videos
[...document.querySelectorAll('.vcar video')].map(v=>({src:!!v.getAttribute('src'),muted:v.muted,paused:v.paused,rs:v.readyState,err:v.error&&v.error.code}))
// fonts
await document.fonts.ready;[document.fonts.check('800 16px Poppins'),document.fonts.check('16px Lato'),document.fonts.check('16px Caveat')]
```
Viewports: `resize_window {width:1280,height:860}` and `{preset:"mobile"}` (375×812). Then `{preset:"desktop"}` to reset.

**6. Preview server (`.claude/launch.json`):**
```json
{"version":"0.0.1","configurations":[{"name":"sales-page","runtimeExecutable":"python3","runtimeArgs":["-m","http.server","8765","--bind","127.0.0.1","--directory","sales-page/my-sales-page"],"port":8765}]}
```

**7. Lazy video start and slider eager-load (end of `body.html`):**
```js
(function(){var sl=document.querySelector('.slider');if(!sl)return;
function load(){sl.querySelectorAll('img').forEach(function(i){i.loading='eager';});}
if(!('IntersectionObserver' in window)){load();return;}
var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){load();io.disconnect();}},{rootMargin:'600px 0px'});io.observe(sl);})();
(function(){var vids=[].slice.call(document.querySelectorAll('.vcar video[data-src]'));if(!vids.length)return;
var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function start(){vids.forEach(function(v){if(!v.src){v.src=v.getAttribute('data-src');}if(!reduce){var p=v.play();if(p&&p.catch)p.catch(function(){});}});}
function stop(){vids.forEach(function(v){v.pause();});}
var reel=document.querySelector('.vcar');if(!('IntersectionObserver' in window)){start();return;}
new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)start();else stop();});},{rootMargin:'300px 0px'}).observe(reel);})();
```

**8. Component CSS (v2 exact values):**
```css
.alertbar{background:var(--dark);color:var(--on-dark);text-align:center;font-family:var(--font-body);font-weight:700;font-size:14px;letter-spacing:.06em;text-transform:uppercase;padding:11px 16px;border-bottom:3px solid var(--hi)}
.gt-logo{width:170px;height:auto;margin:0 auto 30px}
.vcar{overflow:hidden;margin:44px 0 40px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
.vcar-track{display:flex;gap:16px;width:max-content;animation:slideLeft 45s linear infinite;padding:6px 0 12px}
.vcar:hover .vcar-track{animation-play-state:paused}
.vcard{flex:none;width:200px;aspect-ratio:9/16;border-radius:18px;overflow:hidden;border:2px solid var(--on-dark);background:#000;box-shadow:5px 5px 0 var(--accent)}
.vcard video{width:100%;height:100%;object-fit:cover;display:block}
.slider{overflow:hidden;margin:40px -24px 0;-webkit-mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.slider-track{display:flex;gap:18px;width:max-content;animation:slideLeft 60s linear infinite;padding:8px 0 14px}
.slider:hover .slider-track{animation-play-state:paused}
.slider-track img{width:210px;height:auto;border:2px solid var(--ink);border-radius:18px;box-shadow:5px 5px 0 var(--soft);background:#fff}
@keyframes slideLeft{from{transform:translateX(0)}to{transform:translateX(calc(-50% - 9px))}}
.split.story-split{grid-template-columns:.8fr 1.2fr;align-items:start}
.side3{position:sticky;top:48px}.side3 .pol{max-width:340px}
.logos{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:26px 44px;margin-top:64px;padding-top:40px;border-top:1.5px dashed color-mix(in srgb,var(--ink) 25%,transparent)}
.logos img{height:44px;width:auto;max-width:150px;object-fit:contain;filter:grayscale(1);opacity:.75}
.logos.mini{margin-top:44px;padding-top:28px;gap:18px 28px;display:grid;grid-template-columns:repeat(3,1fr);justify-items:center}
.logos.mini img{height:30px;max-width:100%}
.addon{display:grid;grid-template-columns:96px 1fr;gap:18px;align-items:center;text-align:left;margin:26px 0;padding:18px;border:2px dashed color-mix(in srgb,var(--ink) 30%,transparent);border-radius:16px}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:440px;margin:0 auto}
.s-dark .outcome p,.s-dark .claim p{color:var(--ink)}
.s-dark .maybes{color:var(--on-dark-2)}
footer .gt-foot{width:150px;margin:0 auto 26px}
footer .wordmark{font-family:var(--font-head);font-size:clamp(40px,12vw,148px);line-height:.85;letter-spacing:-.04em;color:transparent;background:linear-gradient(#d9d9de,#55555f);-webkit-background-clip:text;background-clip:text;margin-top:40px;white-space:nowrap;overflow:hidden}
@media (max-width:820px){.gt-logo{width:140px;margin-bottom:24px}.split.story-split{grid-template-columns:1fr}.side3{position:relative;top:0}.vcard{width:150px}.vcar{margin:34px 0 30px}.slider{margin:30px -18px 0}.slider-track img{width:160px}.logos img{height:34px;max-width:110px}}
@media (prefers-reduced-motion:reduce){.vcar-track,.slider-track{animation:none}.vcar,.slider{overflow-x:auto}}
```
The v1 vertical reel, replaced at #16:
```css
.reel{position:sticky;top:48px;display:grid;grid-template-columns:1fr 1fr;gap:14px;height:620px;overflow:hidden;mask-image:linear-gradient(transparent,#000 9%,#000 91%,transparent)}
.reel-col{display:flex;flex-direction:column;gap:14px;animation:reelUp 38s linear infinite}
.reel-col.down{animation-name:reelDown;animation-duration:44s}
.reel-card{aspect-ratio:9/16;border-radius:18px;border:2px solid var(--ink);box-shadow:4px 4px 0 var(--soft)}
@keyframes reelUp{to{transform:translateY(calc(-50% - 7px))}}
```
Phone: the reel has `height:520px` and `position:relative`.

**9. `copy.md` header pattern:**
```
<!-- <Product> · $<price>, approved page copy (from copy-original.md, <date>) -->
<!-- Hero: headline N + subheadline X. Values ... chosen by the client. Section 10 = ... Section 13 skipped until ... -->
<!-- One page element per line. Buttons are in [BUTTON: ...] lines. -->
