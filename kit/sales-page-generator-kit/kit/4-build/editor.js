/* Layout editor for draft sales pages. The owner can select an image (resize, align, move, send to a section,
   space above/below, hide) or any text (size, color, alignment, spacing, highlighter), undo, and save.
   Sizes are stored per device (desktop / phone) so the page stays responsive.
   Needs: <div id="page">, <style id="layout-edits">, <script type="application/json" id="layout-edits-data">. */
(function () {
  var page = document.getElementById('page');
  var styleEl = document.getElementById('layout-edits');
  var dataEl = document.getElementById('layout-edits-data');
  if (!page || !styleEl || !dataEl) return;

  var MQ = '(max-width:820px)';
  var BLOCKS = 'p,h2,h3,figure,.cta,ul,ol,.card,.outcome,.claim,.feature,.stmt,.flow,.maybes,.lede,.note,.trust,.proofgrid,.shots,.bonuses';
  var TEXT = 'h1,h2,h3,p,li,.hand,.fine,.btn,.trust,.tag,.chip,.eyebrow,.num,.q,.reframe';
  var SWATCHES = [['Ink', '--ink'], ['Soft ink', '--ink-soft'], ['Accent', '--accent'], ['Soft', '--soft'], ['Button', '--hi'],
                  ['White', '--paper'], ['Sand', '--sand'], ['On dark', '--on-dark'], ['On dark 2', '--on-dark-2']];
  var edits = {};
  try { edits = JSON.parse(dataEl.textContent || '{}'); } catch (e) { edits = {}; }
  var on = false, sel = null, kind = '', hist = [], uid = 0, teUid = 0, dragEl = null, raf = 0;

  function mode() { return window.matchMedia(MQ).matches ? 'm' : 'd'; }
  function targetOf(img) { return img.closest('.fig,.pol') || img; }
  function idOf(el) { return kind === 'text' ? 't' + el.getAttribute('data-te') : el.getAttribute('data-ed'); }

  function ensureIds() {
    page.querySelectorAll('[data-ed]').forEach(function (e) { uid = Math.max(uid, +e.getAttribute('data-ed') || 0); });
    page.querySelectorAll('[data-te]').forEach(function (e) { teUid = Math.max(teUid, +e.getAttribute('data-te') || 0); });
    page.querySelectorAll('img').forEach(function (img) {
      var t = targetOf(img);
      if (!t.getAttribute('data-ed')) t.setAttribute('data-ed', ++uid);
    });
  }

  function inSwipe(id) { var el = page.querySelector('[data-ed="' + id + '"]'); return !!(el && el.closest('.swipe-frame')); }
  function css(forEdit) {
    var out = { d: '', m: '' };
    Object.keys(edits).forEach(function (id) {
      var sel_ = id.charAt(0) === 't' ? '#page [data-te="' + id.slice(1) + '"]' : '#page [data-ed="' + id + '"]';
      ['d', 'm'].forEach(function (m) {
        var e = edits[id][m]; if (!e) return;
        var r = '';
        if (e.w != null) r += inSwipe(id) ? 'width:' + e.w + '%!important;max-width:none!important;' : 'width:100%!important;max-width:' + e.w + '%!important;';
        if (e.a === 'l') r += 'margin-left:0!important;margin-right:auto!important;';
        if (e.a === 'c') r += 'margin-left:auto!important;margin-right:auto!important;';
        if (e.a === 'r') r += 'margin-left:auto!important;margin-right:0!important;';
        var u = function (n) { return m === 'm' ? 'calc(' + n + '*var(--px))' : n + 'px'; };
        if (e.mt != null) r += 'margin-top:' + u(e.mt) + '!important;';
        if (e.mb != null) r += 'margin-bottom:' + u(e.mb) + '!important;';
        if (e.fs != null) r += 'font-size:' + u(e.fs) + '!important;';
        if (e.c) r += 'color:' + e.c + '!important;';
        if (e.ta) r += 'text-align:' + (e.ta === 'l' ? 'left' : e.ta === 'r' ? 'right' : 'center') + '!important;';
        if (e.h) r += forEdit ? 'opacity:.22!important;' : 'display:none!important;';
        if (r) out[m] += sel_ + '{' + r + '}';
      });
    });
    return '@media (min-width:821px){' + out.d + '}@media (max-width:820px){' + out.m + '}';
  }
  function apply() { styleEl.textContent = css(on); }

  function push() {
    hist.push({ h: page.innerHTML, e: JSON.stringify(edits) });
    if (hist.length > 40) hist.shift();
  }
  function undo() {
    var s = hist.pop(); if (!s) { toast('Nothing to undo'); return; }
    page.innerHTML = s.h; edits = JSON.parse(s.e);
    sel = null; kind = ''; prepare(); apply(); refreshTools(); toast('Undone');
  }

  function setE(id, key, val) {
    var m = mode();
    edits[id] = edits[id] || {}; edits[id][m] = edits[id][m] || {};
    if (val == null) delete edits[id][m][key]; else edits[id][m][key] = val;
    apply();
  }

  function contentW(p) {
    var cs = getComputedStyle(p);
    return p.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  }
  function capOf(t) { return t.closest('.swipe-frame') ? 300 : 100; }
  function pctOf(t) { return Math.max(5, Math.min(capOf(t), Math.round(t.offsetWidth / contentW(t.parentElement) * 100))); }

  /* UI */
  function swatches(action) {
    return SWATCHES.map(function (s) {
      return '<button class="ed-sw" data-a="' + action + '" data-c="' + s[1] + '" title="' + s[0] + '" style="background:var(' + s[1] + ')"></button>';
    }).join('');
  }
  var STEPS = function (x) {
    return '<span class="ed-step">Space above <button data-a="mt-">−</button><b data-v="mt">0</b><button data-a="mt+">+</button></span>' +
           '<span class="ed-step">Space below <button data-a="mb-">−</button><b data-v="mb">0</b><button data-a="mb+">+</button></span>';
  };
  var ui = document.createElement('div');
  ui.id = 'ed-ui';
  ui.innerHTML =
    '<button class="ed-main" data-a="toggle">✎ Edit layout</button>' +
    '<div class="ed-panel" hidden>' +
      '<div class="ed-hint"></div>' +
      '<div class="ed-sel" hidden>' +
        '<div class="ed-id"></div>' +
        '<label class="ed-size">Size <input type="range" min="10" max="100" step="1"><b>60%</b></label>' +
        '<span class="ed-grp"><button data-a="al">Left</button><button data-a="ac">Center</button><button data-a="ar">Right</button></span>' +
        '<span class="ed-grp"><button data-a="up">Move up</button><button data-a="down">Move down</button></span>' +
        STEPS() +
        '<label class="ed-send">Send to section <select></select></label>' +
        '<button data-a="hide">Hide</button><button data-a="reset">Reset this image</button>' +
      '</div>' +
      '<div class="ed-txt" hidden>' +
        '<div class="ed-id"></div>' +
        '<span class="ed-step">Text size <button data-a="fs-">A−</button><b data-v="fs">18</b><button data-a="fs+">A+</button></span>' +
        '<span class="ed-grp"><button data-a="tl">Left</button><button data-a="tc">Center</button><button data-a="tr">Right</button></span>' +
        STEPS() +
        '<div class="ed-colors"><span>Text color</span>' + swatches('col') + '<input type="color" class="ed-wcolor" title="Any color" value="#c0392b"></div>' +
        '<div class="ed-tip">Select some words first and the color changes only those words. Select nothing and it changes the whole line.</div>' +
        '<div class="ed-colors"><span>Highlight color</span>' + swatches('hlc') + '</div>' +
        '<span class="ed-grp"><button data-a="hl">Highlight</button><button data-a="unhl">Remove highlight</button></span>' +
                '<span class="ed-grp"><button data-a="bold"><b>B</b></button><button data-a="ital"><i>I</i></button><button data-a="wclr">Clear word colors</button></span>' +
        '<span class="ed-grp"><button data-a="dup">Add text below</button><button data-a="hide">Hide</button><button data-a="del">Delete this</button></span>' +
        '<button data-a="treset">Reset this text</button>' +
        '<div class="ed-tip">Click the text to type in it. Select words to color them, make them bold or highlight them. Highlight: select some words first, or click Highlight with nothing selected to highlight the whole line. Select words inside a highlight and click Highlight again to remove just those.</div>' +
      '</div>' +
      '<div class="ed-row"><button data-a="undo">Undo</button><button data-a="save">Save draft</button><button data-a="export">Export final (no editor)</button></div>' +
    '</div><div class="ed-toast" hidden></div>';
  document.body.appendChild(ui);
  var ov = document.createElement('div');
  ov.id = 'ed-sel'; ov.hidden = true; ov.innerHTML = '<i class="ed-handle" title="Drag to resize"></i>';
  document.body.appendChild(ov);

  var tagBox = document.createElement('div'); tagBox.id = 'ed-tags'; tagBox.hidden = true; document.body.appendChild(tagBox);
  var tagMap = {};
  var panel = ui.querySelector('.ed-panel'), hint = ui.querySelector('.ed-hint'),
      selBox = ui.querySelector('.ed-sel'), txtBox = ui.querySelector('.ed-txt'), slider = ui.querySelector('input[type=range]'),
      sizeLbl = ui.querySelector('.ed-size b'), sendSel = ui.querySelector('.ed-send select'), toastEl = ui.querySelector('.ed-toast');

  page.querySelectorAll('section[data-section]').forEach(function (sc) {
    var o = document.createElement('option');
    o.value = sc.getAttribute('data-section'); o.textContent = sc.getAttribute('data-section') + '. ' + (sc.getAttribute('data-name') || '');
    sendSel.appendChild(o);
  });
  function toast(msg) {
    toastEl.textContent = msg; toastEl.hidden = false;
    clearTimeout(toast.t); toast.t = setTimeout(function () { toastEl.hidden = true; }, 3200);
  }
  function modeName() { return mode() === 'm' ? 'PHONE' : 'DESKTOP'; }
  function setV(name, v) { ui.querySelectorAll('[data-v=' + name + ']').forEach(function (n) { n.textContent = v; }); }

  function refreshTools() {
    hint.innerHTML = 'Editing <b>' + modeName() + '</b> sizes' + (mode() === 'd' ? ' (make the window narrow to edit phone sizes)' : '') +
      '. Click an image or any text to select it.';
    if (!sel || !document.body.contains(sel)) { sel = null; kind = ''; selBox.hidden = true; txtBox.hidden = true; ov.hidden = true; return; }
    ov.hidden = !on; ov.classList.toggle('ed-text-mode', kind === 'text');
    var cs = getComputedStyle(sel), sc = sel.closest('section[data-section]'), secNo = sc ? sc.getAttribute('data-section') : '?';
    setV('mt', Math.round(parseFloat(cs.marginTop) || 0));
    setV('mb', Math.round(parseFloat(cs.marginBottom) || 0));
    if (kind === 'img') {
      selBox.hidden = false; txtBox.hidden = true;
      slider.max = capOf(sel); var p = pctOf(sel); slider.value = p; sizeLbl.textContent = p + '%';
      var e = (edits[sel.getAttribute('data-ed')] || {})[mode()] || {};
      selBox.querySelector('[data-a=hide]').textContent = e.h ? 'Show' : 'Hide';
      var im = sel.querySelector('img') || sel;
      selBox.querySelector('.ed-id').innerHTML = '<b>Image ' + sel.getAttribute('data-ed') + '</b> · ' + (im.getAttribute('src') || '').split('/').pop() + ' · in section ' + secNo;
      if (sc) sendSel.value = secNo;
    } else {
      selBox.hidden = true; txtBox.hidden = false;
      setV('fs', Math.round(parseFloat(cs.fontSize) || 0));
      var snippet = (sel.textContent || '').trim().replace(/\s+/g, ' ');
      txtBox.querySelector('.ed-id').innerHTML = '<b>Text</b> · ' + sel.tagName.toLowerCase() + ' · section ' + secNo + ' · “' + snippet.slice(0, 40) + (snippet.length > 40 ? '…' : '') + '”';
    }
  }

  function prepare() {
    ensureIds();
    page.querySelectorAll('img').forEach(function (img) { img.draggable = false; });
    page.querySelectorAll('[data-ed]').forEach(function (t) { if (on) t.setAttribute('draggable', 'true'); else t.removeAttribute('draggable'); });
  }

  function select(t, k) {
    page.querySelectorAll('.ed-selected').forEach(function (e) { e.classList.remove('ed-selected'); });
    page.querySelectorAll('[contenteditable]').forEach(function (e) { e.removeAttribute('contenteditable'); e.removeAttribute('spellcheck'); });
    if (t && k === 'text' && t !== sel) push();
    sel = t; kind = t ? k : '';
    if (t && k === 'text') { t.setAttribute('contenteditable', 'true'); t.setAttribute('spellcheck', 'false'); }
    if (t) {
      t.classList.add('ed-selected');
      if (k === 'text' && !t.getAttribute('data-te')) t.setAttribute('data-te', ++teUid);
    }
    refreshTools(); place();
  }

  function place() {
    if (!on || !sel) return;
    var r = sel.getBoundingClientRect();
    ov.style.left = r.left + 'px'; ov.style.top = r.top + 'px'; ov.style.width = r.width + 'px'; ov.style.height = r.height + 'px';
  }
  function tags() {
    tagBox.hidden = !on; if (!on) return;
    page.querySelectorAll('[data-ed]').forEach(function (t) {
      var id = t.getAttribute('data-ed'), g = tagMap[id];
      if (!g) { g = document.createElement('i'); g.textContent = id; tagBox.appendChild(g); tagMap[id] = g; }
      var r = t.getBoundingClientRect(), vis = r.width > 0 && r.bottom > 20 && r.top < innerHeight;
      g.style.display = vis ? '' : 'none';
      if (vis) { g.style.left = (r.left + 8) + 'px'; g.style.top = (Math.max(r.top, 0) + 8) + 'px'; }
    });
  }
  function loop() { place(); tags(); raf = requestAnimationFrame(loop); }

  function setOn(v) {
    on = v;
    document.documentElement.classList.toggle('ed-on', on);
    if (on) document.documentElement.classList.remove('anim');
    panel.hidden = !on;
    ui.querySelector('.ed-main').textContent = on ? '✓ Done editing' : '✎ Edit layout';
    prepare(); apply();
    if (!on) { select(null); cancelAnimationFrame(raf); tagBox.hidden = true; } else { refreshTools(); raf = requestAnimationFrame(loop); }
  }

  /* clicks on the page */
  document.addEventListener('click', function (e) {
    if (!on) return;
    if (ui.contains(e.target) || ov.contains(e.target)) return;
    if (page.contains(e.target)) {
      e.preventDefault();
      var img = e.target.closest('img');
      if (img) return select(targetOf(img), 'img');
      var tx = e.target.closest(TEXT);
      select(tx && page.contains(tx) ? tx : null, 'text');
    }
  }, true);

  /* keep the user's text selection when a panel button is pressed */
  ui.addEventListener('mousedown', function (e) { if (e.target.closest('button')) e.preventDefault(); });

  /* words: color, bold, italic on the selected words */
  var lastR = null;
  document.addEventListener('selectionchange', function () { var r = curSel(); if (r) lastR = r.cloneRange(); });
  function wordRange() { var r = curSel(); if (!r && lastR && sel && sel.contains(lastR.commonAncestorContainer)) r = lastR; if (!r) toast('Select some words first'); return r; }
  function wordWrap(tag) {
    var r = wordRange(); if (!r) return;
    var m = document.createElement(tag);
    try { r.surroundContents(m); } catch (err) { m.appendChild(r.extractContents()); r.insertNode(m); }
    window.getSelection().removeAllRanges();
  }
  function wordColor(c) {
    var r = wordRange(); if (!r) return;
    var m = document.createElement('span'); m.style.color = c;
    try { r.surroundContents(m); } catch (err) { m.appendChild(r.extractContents()); r.insertNode(m); }
    window.getSelection().removeAllRanges();
  }
  function wordClear() {
    var r = wordRange(); if (!r) return;
    Array.prototype.slice.call(sel.querySelectorAll('span[style*="color"],b,i')).forEach(function (x) { if (r.intersectsNode(x)) { x.style.color = ''; if (x.tagName !== 'SPAN' || !x.getAttribute('style')) unwrap(x); } });
  }
  ui.addEventListener('input', function (e) {
    if (e.target.classList.contains('ed-wcolor') && sel) { push(); if (wordRange()) wordColor(e.target.value); }
  });

  /* highlighter */
  function unwrap(m) { var p = m.parentNode; while (m.firstChild) p.insertBefore(m.firstChild, m); p.removeChild(m); p.normalize(); }
  function marksIn(el) { return Array.prototype.slice.call(el.querySelectorAll('mark')); }
  function curSel() {
    var s = window.getSelection();
    if (!s || !s.rangeCount || s.isCollapsed || !sel) return null;
    var r = s.getRangeAt(0);
    return sel.contains(r.commonAncestorContainer) ? r : null;
  }
  function highlight(color) {
    var r = curSel(), mk;
    if (r) {
      var an = r.commonAncestorContainer; an = an.nodeType === 1 ? an : an.parentElement;
      var inside = an.closest('mark');
      if (inside && sel.contains(inside)) { unwrap(inside); window.getSelection().removeAllRanges(); return; }
      mk = document.createElement('mark');
      try { r.surroundContents(mk); } catch (err) { mk.appendChild(r.extractContents()); r.insertNode(mk); }
      window.getSelection().removeAllRanges();
    } else {
      if (marksIn(sel).length) { toast('This line already has a highlight. Select words to add more, or Remove highlight.'); return; }
      mk = document.createElement('mark');
      while (sel.firstChild) mk.appendChild(sel.firstChild);
      sel.appendChild(mk);
    }
    if (color) mk.style.setProperty('--hl', 'var(' + color + ')');
  }
  function setHlColor(color) {
    var r = curSel(), list = [];
    if (r) {
      var an = r.commonAncestorContainer; an = an.nodeType === 1 ? an : an.parentElement;
      var m = an.closest('mark'); if (m && sel.contains(m)) list = [m];
      else list = marksIn(sel).filter(function (x) { return r.intersectsNode(x); });
    } else list = marksIn(sel);
    if (!list.length) { highlight(color); return; }
    list.forEach(function (x) { x.style.setProperty('--hl', 'var(' + color + ')'); });
  }

  ui.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    var a = b.getAttribute('data-a');
    if (a === 'toggle') return setOn(!on);
    if (a === 'undo') return undo();
    if (a === 'save') { dl('index.html', serialize(false)); return toast('Saved: check your Downloads folder for index.html'); }
    if (a === 'export') { dl('index-final.html', serialize(true)); return toast('Exported index-final.html (no editor inside)'); }
    if (!sel) return;
    var id = idOf(sel);
    push();
    if (a === 'al') setE(id, 'a', 'l');
    if (a === 'ac') setE(id, 'a', 'c');
    if (a === 'ar') setE(id, 'a', 'r');
    if (a === 'tl') setE(id, 'ta', 'l');
    if (a === 'tc') setE(id, 'ta', 'c');
    if (a === 'tr') setE(id, 'ta', 'r');
    if (a === 'hide') { var cur = ((edits[id] || {})[mode()] || {}).h; setE(id, 'h', cur ? null : true); }
    if (a === 'reset' || a === 'treset') { if (edits[id]) delete edits[id][mode()]; apply(); }
    if (a === 'fs-' || a === 'fs+') {
      var f0 = ((edits[id] || {})[mode()] || {}).fs;
      if (f0 == null) f0 = Math.round(parseFloat(getComputedStyle(sel).fontSize) || 16);
      setE(id, 'fs', Math.max(10, Math.min(140, f0 + (a === 'fs+' ? 2 : -2))));
    }
    if (a === 'col') { if (curSel() || (lastR && sel.contains(lastR.commonAncestorContainer) && !lastR.collapsed)) wordColor('var(' + b.getAttribute('data-c') + ')'); else setE(id, 'c', 'var(' + b.getAttribute('data-c') + ')'); }
    if (a === 'hlc') setHlColor(b.getAttribute('data-c'));
    if (a === 'hl') highlight(null);
    if (a === 'wcol') wordColor('var(' + b.getAttribute('data-c') + ')');
    if (a === 'wclr') wordClear();
    if (a === 'bold') wordWrap('b');
    if (a === 'ital') wordWrap('i');
    if (a === 'dup') { var cp = sel.cloneNode(true); ['data-te', 'data-ed', 'contenteditable', 'class'].forEach(function (x) { if (x !== 'class') cp.removeAttribute(x); }); cp.classList.remove('ed-selected'); cp.textContent = 'New text. Click it to type.'; sel.parentNode.insertBefore(cp, sel.nextSibling); select(cp, 'text'); return; }
    if (a === 'del') { var gone = sel; select(null); gone.remove(); return; }
    if (a === 'unhl') marksIn(sel).forEach(unwrap);
    if (a === 'mt-' || a === 'mt+' || a === 'mb-' || a === 'mb+') {
      var k = a.slice(0, 2), cs2 = getComputedStyle(sel), cur2 = ((edits[id] || {})[mode()] || {})[k];
      if (cur2 == null) cur2 = Math.round(parseFloat(k === 'mt' ? cs2.marginTop : cs2.marginBottom) || 0);
      setE(id, k, Math.max(-80, Math.min(240, cur2 + (a.charAt(2) === '+' ? 8 : -8))));
    }
    if (a === 'up') { var p = sel.previousElementSibling; if (p) sel.parentNode.insertBefore(sel, p); }
    if (a === 'down') { var n = sel.nextElementSibling; if (n) sel.parentNode.insertBefore(n, sel); }
    refreshTools(); place();
  });

  slider.addEventListener('pointerdown', push);
  slider.addEventListener('input', function () {
    if (!sel || kind !== 'img') return;
    setE(sel.getAttribute('data-ed'), 'w', +slider.value);
    sizeLbl.textContent = slider.value + '%';
  });

  sendSel.addEventListener('change', function () {
    if (!sel || kind !== 'img') return;
    var s2 = page.querySelector('section[data-section="' + sendSel.value + '"]'); if (!s2) return;
    push();
    var cta = s2.querySelector('.cta');
    if (cta) cta.parentNode.insertBefore(sel, cta);
    else (s2.querySelector('.story') || s2.querySelector('.wrap:last-of-type') || s2).appendChild(sel);
    refreshTools(); place();
    sel.scrollIntoView({ behavior: 'smooth', block: 'center' });
    toast('Image ' + sel.getAttribute('data-ed') + ' moved to section ' + sendSel.value);
  });

  /* corner handle (images) */
  var rs = null;
  ov.querySelector('.ed-handle').addEventListener('pointerdown', function (e) {
    if (!sel || kind !== 'img') return; e.preventDefault(); e.stopPropagation(); push();
    var pr = sel.parentElement.getBoundingClientRect(), r = sel.getBoundingClientRect();
    rs = { x: e.clientX, w0: pctOf(sel), cw: contentW(sel.parentElement), k: (r.left - pr.left < 4) ? 1 : 2 };
    this.setPointerCapture(e.pointerId);
  });
  ov.querySelector('.ed-handle').addEventListener('pointermove', function (e) {
    if (!rs || !sel) return;
    var v = Math.max(10, Math.min(capOf(sel), Math.round(rs.w0 + (e.clientX - rs.x) * rs.k / rs.cw * 100)));
    setE(sel.getAttribute('data-ed'), 'w', v);
    slider.value = v; sizeLbl.textContent = v + '%';
  });
  ov.querySelector('.ed-handle').addEventListener('pointerup', function () { rs = null; refreshTools(); });

  /* drag to move (images) */
  var line = document.createElement('div'); line.id = 'ed-line'; line.hidden = true; document.body.appendChild(line);
  function dropTarget(e) {
    var b = e.target.closest ? e.target.closest(BLOCKS) : null;
    if (!b || !dragEl || !page.contains(b) || b === dragEl || dragEl.contains(b) || b.contains(dragEl) && b.tagName !== 'SECTION') return null;
    if (b.closest('footer')) return null;
    var r = b.getBoundingClientRect();
    return { b: b, before: e.clientY < r.top + r.height / 2, r: r };
  }
  document.addEventListener('dragstart', function (e) {
    if (!on) return;
    var t = e.target.closest ? e.target.closest('[data-ed]') : null;
    if (!t || !page.contains(t)) return;
    dragEl = t; select(t, 'img');
    e.dataTransfer.effectAllowed = 'move'; e.dataTransfer.setData('text/plain', 'move');
  });
  document.addEventListener('dragover', function (e) {
    if (!on || !dragEl) return;
    var d = dropTarget(e); if (!d) { line.hidden = true; return; }
    e.preventDefault(); e.dataTransfer.dropEffect = 'move';
    line.hidden = false; line.style.left = d.r.left + 'px'; line.style.width = d.r.width + 'px';
    line.style.top = (d.before ? d.r.top : d.r.bottom) - 2 + 'px';
  });
  document.addEventListener('drop', function (e) {
    if (!on || !dragEl) return;
    var d = dropTarget(e); line.hidden = true; if (!d) { dragEl = null; return; }
    e.preventDefault(); push();
    d.b.parentNode.insertBefore(dragEl, d.before ? d.b : d.b.nextSibling);
    dragEl = null; refreshTools(); place();
  });
  document.addEventListener('dragend', function () { dragEl = null; line.hidden = true; });

  document.addEventListener('keydown', function (e) {
    if (!on) return;
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'z' && !(document.activeElement && document.activeElement.isContentEditable)) { e.preventDefault(); undo(); }
    if (e.key === 'Escape') select(null);
  });
  window.addEventListener('resize', function () { if (on) { apply(); refreshTools(); } });

  /* save / export */
  function serialize(final) {
    var cl = document.documentElement.cloneNode(true);
    cl.classList.remove('ed-on', 'anim');
    ['#ed-ui', '#ed-sel', '#ed-line', '#ed-tags'].forEach(function (s) { var n = cl.querySelector(s); if (n) n.remove(); });
    cl.querySelectorAll('.ed-selected').forEach(function (e) { e.classList.remove('ed-selected'); });
    cl.querySelectorAll('[contenteditable]').forEach(function (e) { e.removeAttribute('contenteditable'); e.removeAttribute('spellcheck'); });
    cl.querySelectorAll('[draggable]').forEach(function (e) { e.removeAttribute('draggable'); });
    cl.querySelector('#layout-edits').textContent = css(false);
    cl.querySelector('#layout-edits-data').textContent = JSON.stringify(edits);
    if (final) ['#layout-editor', '#editor-css', '#layout-edits-data'].forEach(function (s) { var n = cl.querySelector(s); if (n) n.remove(); });
    return '<!DOCTYPE html>\n' + cl.outerHTML;
  }
  function dl(name, text) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type: 'text/html' }));
    a.download = name; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 800);
  }
  window.__layoutEditor = { serialize: serialize, edits: function () { return edits; } };

  ensureIds(); apply();
})();
