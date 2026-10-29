// Check for the partner white-label skin on /partner/<slug>/tools.
//
// Serves a rebuilt Odoo page (header, top menu, #wrap, footer) at the real partner path,
// with the head anti-flash block, both halves of the loading screen and the section loader.
// The loader is pointed at the local sections folder instead of jsDelivr, so this runs
// against the files in this repo, not against what happens to be published.
//
//   node test.js
//
// Playwright comes from stx-tools/node_modules (or set STX_PLAYWRIGHT to another path).

const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const SECTIONS = path.resolve(__dirname, '../../sections');
const read = (f) => fs.readFileSync(path.resolve(SECTIONS, f), 'utf8');

const HEAD_ANTIFLASH = read('partner-head-antiflash.html');

// Odoo's session info, the way it sits in the head above our own blocks. The livechat
// widget reads can_load_livechat from here, so the anti-flash block can switch it off.
const LIVECHAT_SESSION = `<script>
window.odoo = window.odoo || {};
odoo.__session_info__ = odoo.__session_info__ || {};
odoo.__session_info__.livechatData = { can_load_livechat: true, options: { channel_id: 1 } };
</script>`;

// Stand-in for the livechat widget: a host element at the end of body with a shadow root
// and a fixed button inside it, plus a random id, exactly like Odoo builds it. Only mounts
// when can_load_livechat is still true, unless ?livechat=force is set, which is how the
// test checks the CSS fallback on its own.
const LIVECHAT_MOUNT = `<script>
(function () {
  var forced = /[?&]livechat=force/.test(window.location.search);
  var si = window.odoo && window.odoo.__session_info__;
  if (!forced && !(si && si.livechatData && si.livechatData.can_load_livechat)) { return; }
  var host = document.createElement('div');
  host.className = 'o-livechat-root';
  host.id = 'o-livechat-root-' + Date.now() + '.' + Math.round(Math.random() * 9999);
  document.body.appendChild(host);
  var sr = host.attachShadow({ mode: 'open' });
  var b = document.createElement('button');
  b.className = 'o-livechat-LivechatButton';
  b.textContent = 'Hulp nodig? Chat met ons.';
  b.setAttribute('style', 'position:fixed;right:16px;bottom:16px;width:180px;height:44px');
  sr.appendChild(b);
})();
</script>`;

// Loading screen part 1 (head field) and part 2 (end of body), copied from the live Odoo fields.
const LOADWALL_HEAD = `<script>
(function () {
  'use strict';
  var p = (window.location.pathname || '/').toLowerCase();
  if (p.length > 1 && p.charAt(p.length - 1) === '/') { p = p.slice(0, -1); }
  var SECTION_PATHS = ['/inspiration', '/inspiratie', '/test-inspo', '/tools'];
  if (!SECTION_PATHS.some(function (pp) { return p.slice(-pp.length) === pp; })) { return; }
  document.documentElement.classList.add('stx-loading');
  var st = document.createElement('style');
  st.textContent =
    'html.stx-loading::before{content:"";position:fixed;inset:0;z-index:2147483000;background:#fff}' +
    'html.stx-loading::after{content:"";position:fixed;left:50%;top:50%;width:46px;height:46px;' +
    'margin:-23px 0 0 -23px;border-radius:50%;border:4px solid #f1d9ff;border-top-color:#6b3fb9;' +
    'animation:stxlwspin .8s linear infinite;z-index:2147483001}' +
    '@keyframes stxlwspin{to{transform:rotate(360deg)}}';
  document.head.appendChild(st);
  window.stxLoadwallHeadOff = function () { document.documentElement.classList.remove('stx-loading'); };
  setTimeout(window.stxLoadwallHeadOff, 7000);
})();
</script>`;

const LOADWALL_BODY = `<script>
(function () {
  'use strict';
  var css = document.createElement('style');
  css.textContent =
    '#stx-loadwall{position:fixed;inset:0;z-index:2147483000;background:#fff;' +
    'display:flex;align-items:center;justify-content:center;opacity:1;transition:opacity .3s ease}' +
    '#stx-loadwall.stx-out{opacity:0;pointer-events:none}' +
    '#stx-loadwall .stx-spin{width:46px;height:46px;border-radius:50%;' +
    'border:4px solid #f1d9ff;border-top-color:#6b3fb9;animation:stxlwspin .8s linear infinite}' +
    '@keyframes stxlwspin{to{transform:rotate(360deg)}}';
  document.head.appendChild(css);
  var wall = document.createElement('div');
  wall.id = 'stx-loadwall';
  wall.innerHTML = '<div class="stx-spin"></div>';
  document.body.appendChild(wall);
  if (window.stxLoadwallHeadOff) { window.stxLoadwallHeadOff(); }
  window.stxHideCalls = 0;
  var gone = false;
  window.stxLoadwallHide = function () {
    window.stxHideCalls++;
    if (gone) { return; }
    gone = true;
    wall.classList.add('stx-out');
    setTimeout(function () { if (wall.parentNode) { wall.parentNode.removeChild(wall); } }, 400);
  };
})();
</script>`;

// The loader from the end-of-body field, with BASE pointed at the local sections folder.
const LOADER = `<script>
(function () {
  'use strict';
  var BASE = '/sections/';
  var SECTIONS = [
    { file: 'inspiration-v18.html', paths: ['/inspiration', '/inspiratie', '/test-inspo', '/tools'] },
    { file: 'partner-calculator-v1.html',
      re: /^(\\/(en_gb|fr|de))?\\/partner\\/[a-z0-9-]+\\/tools$/, paths: [] },
    { file: 'silkmas-v1.html', all: true, brand: true, paths: [] },
    { file: 'birthday-v1.html', all: true, brand: true, paths: [] }
  ];
  var p = (window.location.pathname || '/').toLowerCase();
  if (p.length > 1 && p.charAt(p.length - 1) === '/') { p = p.slice(0, -1); }
  /* Zoals de echte loader (v29): brand-secties nooit op een partnerpagina. ?noflag=1 zet dat hier uit,
     om het tweede slot in de secties zelf apart te testen. */
  var partnerPage = /^(\\/(en_gb|fr|de))?\\/partner(\\/|$)/.test(p) && !/noflag=1/.test(window.location.search);
  function onPage(paths) { return paths.some(function (pp) { return p.slice(-pp.length) === pp; }); }
  var pending = 0;
  function sectionDone() {
    pending--;
    if (pending > 0) { return; }
    if (window.stxLoadwallHide) { window.stxLoadwallHide(); }
  }
  function execScriptsSequentially(scripts, i, done) {
    if (i >= scripts.length) { if (done) { done(); } return; }
    var old = scripts[i];
    var s = document.createElement('script');
    for (var a = 0; a < old.attributes.length; a++) { s.setAttribute(old.attributes[a].name, old.attributes[a].value); }
    if (old.src) {
      s.onload = s.onerror = function () { execScriptsSequentially(scripts, i + 1, done); };
      s.src = old.src;
      document.body.appendChild(s);
    } else {
      s.text = old.text;
      document.body.appendChild(s);
      execScriptsSequentially(scripts, i + 1, done);
    }
  }
  function inject(htmlText, done) {
    var tpl = document.createElement('template');
    tpl.innerHTML = htmlText;
    var scripts = Array.prototype.slice.call(tpl.content.querySelectorAll('script'));
    scripts.forEach(function (sc) { if (sc.parentNode) { sc.parentNode.removeChild(sc); } });
    document.body.appendChild(tpl.content);
    execScriptsSequentially(scripts, 0, done);
  }
  function load(section) {
    fetch(BASE + section.file)
      .then(function (r) { if (!r.ok) { throw new Error('HTTP ' + r.status); } return r.text(); })
      .then(function (htmlText) { inject(htmlText, sectionDone); })
      .catch(function (e) { sectionDone(); console.warn('[STX loader]', section.file, e); });
  }
  function run() {
    var hits = [];
    for (var i = 0; i < SECTIONS.length; i++) {
      var sec = SECTIONS[i];
      if (sec.brand && partnerPage) { continue; }
      if (sec.all ? true : (sec.re ? sec.re.test(p) : onPage(sec.paths))) { hits.push(sec); }
    }
    pending = hits.length;
    for (var j = 0; j < hits.length; j++) { load(hits[j]); }
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', run); } else { run(); }
})();
</script>`;

// Een opgeslagen kopie van de tools in de Odoo-pagina (pagina gedupliceerd van /tools of in de
// editor opgeslagen), zoals op de echte Mooideco-pagina van 20/10/2026. Builderteksten blijven anders staan.
function savedCopy() {
  const sec = read('inspiration-v18.html');
  const html = sec.slice(0, sec.indexOf('<script>'));
  // Met de skin erbij, zoals op de echte Euro Party B2B-pagina van 27/10/2026 (header dubbel).
  return '<div class="stx-pt-bar"><div class="stx-pt-in">Header OPGESLAGEN</div></div>'
    + '<div class="stx-pt-tabs"><div class="stx-pt-in">Tabs OPGESLAGEN</div></div>'
    + html
    .replace('id="stx-insp-root"', 'id="stx-insp-root" data-stx-v="31" style="display: block;"')
    .replace(/(data-i18n="cost_h">)[\s\S]*?(<\/h2>)/, '$1Cost calculator OPGESLAGEN$2')
    .replace(/(data-i18n="cc_col_item">)[^<]*/, '$1Item OPGESLAGEN')
    + '<div class="stx-pt-foot"><div class="stx-pt-in">Footer OPGESLAGEN</div></div>';
}

function odooPage(saved) {
  return `<!doctype html><html lang="nl"><head><meta charset="utf-8">
<title>Tools | Sempertex Europe</title>
<link rel="icon" href="/web/image/website/1/favicon">
<style>/* Zoals het Odoo-thema: koppen in ons font en donkerpaars, ook binnen de tools. */ h1,h2,h3,h4,h5,h6{font-family:'RethinkSans-ExtraBold',sans-serif;color:rgb(27,7,61)}</style>
${LOADWALL_HEAD}
${LIVECHAT_SESSION}
${HEAD_ANTIFLASH}
<script>window.__headTitle = document.title; window.__headIcon = (document.querySelector('link[rel~="icon"]') || {}).href || '';</script>
</head><body>
<div id="wrapwrap">
  <header id="top" class="o_header_standard"><div id="top_menu_container">
    <nav class="navbar"><ul id="top_menu" class="nav">
      <li class="nav-item"><a href="/shop" class="nav-link"><span>Shop</span></a></li>
      <li class="nav-item"><a href="/tools" class="nav-link"><span>Tools</span></a></li>
    </ul></nav></div>
  </header>
  <main><div id="wrap"><div class="oe_structure">${saved ? savedCopy() : ''}</div></div></main>
  <footer id="bottom"><div class="o_footer">Sempertex Europe BV</div></footer>
  <div id="website_cookies_bar" class="s_popup o_snippet_invisible o_no_save"><div class="modal s_popup_no_backdrop o_cookies_classic s_popup_bottom show" style="display: block; position: fixed; bottom: 0; left: 0; right: 0; height: 200px; background: #fff;"><h3>Respecting your privacy is our priority.</h3></div></div>
</div>
${LOADWALL_BODY}
${LOADER}
${LIVECHAT_MOUNT}
</body></html>`;
}

const PARTNER_PATH = /^(?:\/(?:fr|de|en_gb))?\/partner\/[a-z0-9-]+\/tools$/;

function serve() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      const url = req.url.split('?')[0];
      // Zoals Odoo: /nl/... zet de taal op Nederlands en stuurt door naar het pad zonder prefix.
      if (url.startsWith('/nl/')) { res.writeHead(302, { location: req.url.slice(3) }).end(); return; }
      if (url.startsWith('/sections/')) {
        const file = path.basename(url);
        const full = path.resolve(SECTIONS, file);
        if (!fs.existsSync(full)) { res.writeHead(404).end('nope'); return; }
        // Zoals live: de tools-code (538 KB via de CDN) komt seconden na de kleine skin binnen.
        const slow = file === 'inspiration-v18.html' && /[?&]saved=1/.test(req.headers.referer || '');
        setTimeout(() => {
          res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
          res.end(fs.readFileSync(full));
        }, slow ? 3500 : 0);
        return;
      }
      // Every other path renders the Odoo page: /tools and /partner/<slug>/tools alike.
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
      res.end(odooPage(/[?&]saved=1/.test(req.url)));
    });
    server.listen(0, '127.0.0.1', () => resolve(server));
  });
}

let failures = 0;
function check(name, ok, extra) {
  console.log((ok ? '  ok   ' : '  FOUT ') + name + (ok || extra === undefined ? '' : '  -> ' + extra));
  if (!ok) { failures++; }
}

(async () => {
  const server = await serve();
  const port = server.address().port;
  const base = `http://127.0.0.1:${port}`;
  const browser = await chromium.launch();

  // Balloon images and the shop routes are not reachable from here; let them fail fast
  // instead of holding the page open.
  async function open(pathname, width = 1400) {
    const ctx = await browser.newContext({ viewport: { width, height: 1000 } });
    // Silkmas testmodus aan, zoals in Robins browser: dan zou de banner overal moeten verschijnen, behalve hier.
    await ctx.addInitScript(() => { try { localStorage.setItem('stx_silkmas_beta', '1'); } catch (e) {} });
    const page = await ctx.newPage();
    await page.route('**', (route) => {
      const u = route.request().url();
      if (u.startsWith(base)) { return route.continue(); }
      return route.abort();
    });
    const warnings = [];
    page.on('console', (m) => { if (m.type() === 'warning' || m.type() === 'error') { warnings.push(m.text()); } });
    await page.goto(base + pathname, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => !!document.querySelector('.stx-pt-order') || Date.now() > window.__t0 + 20000,
      undefined, { timeout: 25000 }).catch(() => {});
    await page.waitForTimeout(600);
    return { ctx, page, warnings };
  }

  console.log('\n/partner/liragram/tools');
  {
    const { ctx, page } = await open('/partner/liragram/tools');

    const shown = (sel) => page.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) { return 'ontbreekt'; }
      const cs = getComputedStyle(el);
      return (cs.display === 'none' || cs.visibility === 'hidden') ? 'verborgen' : 'zichtbaar';
    }, sel);

    check('Sempertex header verborgen', (await shown('header#top')) === 'verborgen');
    check('Sempertex menu verborgen', (await shown('#top_menu_container')) === 'verborgen');
    check('Sempertex footer verborgen', (await shown('footer#bottom')) === 'verborgen');
    check('geen Silkmas-banner (ook niet met de testmodus aan)', (await page.$('#stx-sm-bar, [id^="stx-sm-"]')) === null);
    check('geen cookiebanner van Odoo', (await page.evaluate(() => getComputedStyle(document.querySelector('#website_cookies_bar .modal')).display)) === 'none');
    check('tabtitel tijdens het laden is al zonder Sempertex', await page.evaluate(() => window.__headTitle === 'Liragram'), await page.evaluate(() => window.__headTitle));
    check('favicon tijdens het laden is niet dat van Sempertex', await page.evaluate(() => window.__headIcon.startsWith('data:image/gif')), await page.evaluate(() => window.__headIcon.slice(0, 30)));
    check('geen verjaardagspopup', (await page.$('[id^="stx-bd"], [class*="stx-bday"]')) === null);

    // De livechat hoort hier helemaal niet te booten, want het anti-flitsblok zet
    // can_load_livechat uit voordat de lazy bundle hem bouwt.
    const chat = await shown('.o-livechat-root');
    check('livechat rechtsonder is weg', chat !== 'zichtbaar', chat);

    check('calculator staat er', (await shown('#view-calculator')) === 'zichtbaar');
    check('kostprijscalculator verborgen', (await shown('#view-cost')) === 'verborgen');
    check('colour matching tool verborgen', (await shown('#view-colour')) === 'verborgen');
    check('Sempertex zijmenu verborgen', (await shown('.stx-insp .side')) === 'verborgen');

    check('Liragram header staat er', (await shown('.stx-pt-bar')) === 'zichtbaar');
    check('Liragram footer staat er', (await shown('.stx-pt-foot')) === 'zichtbaar');
    check('bestelblok staat er', (await shown('.stx-pt-order')) === 'zichtbaar');

    const logo = await page.getAttribute('.stx-pt-bar img', 'src');
    check('logo is ingebakken (data-URI, geen hotlink)', !!logo && logo.startsWith('data:image/'));

    check('Sempertex winkelmandknop weg', (await page.$('#calc-cart')) === null);

    const title = await page.title();
    check('tabtitel is van Liragram', title === 'Calculadora de double stuffing | Liragram', title);

    const icon = await page.evaluate(() => {
      const l = document.querySelector('link[rel~="icon"]');
      return l ? l.getAttribute('href').slice(0, 30) : 'geen';
    });
    check('favicon is van Liragram', icon.startsWith('data:image/'), icon);

    const robots = await page.getAttribute('meta[name="robots"]', 'content');
    check('pagina staat op noindex', robots === 'noindex,nofollow', robots);

    const h = await page.textContent('#view-calculator h2');
    check('titel is vertaald', /Calculadora de double stuffing/.test(h || ''), h);
    const inner = await page.textContent('[data-i18n="calc_inner"]');
    check('labels zijn vertaald', (inner || '').trim() === 'Globo interior', inner);
    const note = await page.textContent('[data-i18n="calc_note"]');
    check('disclaimer is vertaald', /aproximación/.test(note || ''), (note || '').slice(0, 40));

    check('Match a colour is Spaans', (await page.textContent('#dsm .picker-label')) === 'Encuentra un color' && (await page.textContent('#dsm .dsm-up')) === 'Subir una foto'
      && (await page.textContent('#dsm .dsm-native span')) === 'o elige un color', await page.textContent('#dsm .dsm-head'));
    check('kleurkiezer staat er nog in het label', (await page.$('#dsm .dsm-native input[type=color]')) !== null);
    await page.$eval('#dsm .dsm-native input[type=color]', (e) => { e.value = '#c0392b'; e.dispatchEvent(new Event('input', { bubbles: true })); e.dispatchEvent(new Event('change', { bubbles: true })); });
    await page.waitForTimeout(400);
    const dsmOut = await page.textContent('#dsm .dsm-out');
    check('resultaten na een kleurkeuze zijn Spaans', /Tu color/.test(dsmOut) && /(Muy parecido|Parecido|Cercano|La opción más cercana)/.test(dsmOut) && !/(Very close|Close|Nearby|Closest option|Your colour)/.test(dsmOut), dsmOut.replace(/\s+/g, ' ').slice(0, 160));
    const english = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('#view-calculator *').forEach((el) => {
        if (el.children.length || !el.offsetParent) { return; }
        const t = (el.textContent || '').trim();
        if (/\b(the|Upload|colour|Tap|closest|Your|Match a)\b/.test(t)) { out.push(t.slice(0, 50)); }
      });
      return out;
    });
    check('geen Engelse zinnen meer in de calculator', english.length === 0, english.join(' | '));

    const brand = await page.evaluate(() =>
      getComputedStyle(document.querySelector('.stx-insp')).getPropertyValue('--purple').trim());
    check('huisstijlkleur staat op de calculator', brand === '#fc3995', brand);

    const font = await page.evaluate(() =>
      getComputedStyle(document.querySelector('.stx-insp')).fontFamily);
    check('font van de partner', /Nunito/.test(font), font);
    const lh2 = await page.evaluate(() => getComputedStyle(document.querySelector('#view-calculator h2')).fontFamily);
    check('titel in het font van de partner, niet dat van het Odoo-thema', /Nunito/.test(lh2), lh2);

    // Pick a colour on each side and read the order block back.
    await page.click('#sw-inner .swatch:nth-child(3)');
    await page.click('#sw-outer .swatch:nth-child(5)');
    await page.waitForTimeout(250);
    const picks = await page.$$eval('.stx-pt-pick .stx-pt-val', (els) => els.map((e) => e.textContent.trim()));
    check('gekozen kleuren staan in het bestelblok', picks.length === 2 && /\d{3}$/.test(picks[0]) && /\d{3}$/.test(picks[1]),
      JSON.stringify(picks));
    const codes = await page.getAttribute('#stx-pt-main', 'data-codes');
    check('kleurcodes gaan mee in de tracking', /^\d{3}, \d{3}$/.test(codes || ''), codes);

    check('geen kopieerknop meer', (await page.$('#stx-pt-copy')) === null);

    const href = await page.getAttribute('#stx-pt-main', 'href');
    check('bestelknop gaat naar de shop van Liragram', /^https:\/\/liragram\.com\//.test(href || ''), href);

    // Elke link naar Liragram opent een nieuw tabblad, anders is de calculator weg
    // zodra iemand op "Volver a la tienda" of op het logo klikt.
    const tabs = await page.$$eval('.stx-pt-bar a, .stx-pt-order a', (els) => els.map((e) => ({
      waar: e.className || 'logo', target: e.getAttribute('target'), rel: e.getAttribute('rel')
    })));
    const fout = tabs.filter((t) => t.target !== '_blank' || !/noopener/.test(t.rel || ''));
    check('alle partnerlinks openen een nieuw tabblad', fout.length === 0, JSON.stringify(fout));
    check('terugknop opent een nieuw tabblad',
      (await page.getAttribute('.stx-pt-back', 'target')) === '_blank');

    // Sempertex mag als PRODUCTnaam wel: Liragram verkoopt onze ballonnen en hun eigen
    // categorie heet ook zo. Wat niet mag is een link terug naar onze site of een
    // Odoo-pad, want dan klikt de bezoeker zo de Sempertex webshop binnen.
    const links = await page.$$eval('#wrapwrap a, .stx-pt-bar a, .stx-pt-foot a, .stx-pt-order a',
      (els) => els.filter((e) => e.offsetParent !== null).map((e) => e.getAttribute('href') || ''));
    const homeward = links.filter((u) => /sempertex-europe|^\/(shop|tools|inspiration|event|blog)/.test(u));
    check('geen zichtbare link terug naar onze eigen site', homeward.length === 0, homeward.join(' '));

    // Elke zichtbare Sempertex-vermelding moet er bewust staan: de bestelknop van de
    // partner ("Ver globos Sempertex") en de creditregel in hun footer. Komt er ergens
    // anders iets van ons in beeld, dan is er chrome blijven staan.
    const leaked = await page.evaluate(() => {
      const hidden = (el) => {
        for (let n = el; n && n !== document.documentElement; n = n.parentElement) {
          const cs = getComputedStyle(n);
          if (cs.display === 'none' || cs.visibility === 'hidden') { return true; }
        }
        return false;
      };
      const out = [];
      document.querySelectorAll('body *').forEach((el) => {
        if (el.children.length || hidden(el)) { return; }
        if (el.closest('#stx-pt-main') || el.closest('.stx-pt-foot')) { return; }
        const t = (el.textContent || '').trim();
        if (/sempertex/i.test(t)) { out.push(t.slice(0, 60)); }
      });
      return out;
    });
    check('buiten de bestelknop en de creditregel staat Sempertex nergens', leaked.length === 0, leaked.join(' | '));

    const credits = await page.$$eval('#stx-pt-main, .stx-pt-foot', (els) => els.map((e) => e.textContent.trim()));
    check('de twee bewuste vermeldingen staan er wel', credits.length === 2 && credits.every((t) => /Sempertex/.test(t)),
      JSON.stringify(credits));

    const hideCalls = await page.evaluate(() => window.stxHideCalls);
    check('laadscherm gaat 1x weg, na beide secties', hideCalls === 1, 'stxLoadwallHide x' + hideCalls);
    check('laadscherm is echt weg', (await page.$('#stx-loadwall')) === null);

    await page.screenshot({ path: path.resolve(__dirname, 'partner-desktop.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\n/partner/liragram/tools op telefoonformaat');
  {
    const { ctx, page } = await open('/partner/liragram/tools', 390);
    check('bestelblok staat er ook mobiel', (await page.$('.stx-pt-order')) !== null);
    const scroll = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    check('geen horizontale scroll', scroll <= 2, scroll + 'px');
    await page.screenshot({ path: path.resolve(__dirname, 'partner-mobile.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\n/partner/liragram/tools#cost (tool die Liragram niet heeft)');
  {
    const { ctx, page } = await open('/partner/liragram/tools#cost');
    await page.waitForTimeout(300);
    check('hash gaat terug naar de calculator', await page.evaluate(() => location.hash) === '#calculator', await page.evaluate(() => location.hash));
    const v = await page.evaluate(() => getComputedStyle(document.querySelector('#view-cost')).display);
    check('kostprijscalculator blijft verborgen', v === 'none', v);
    check('geen tabbladen bij 1 tool', (await page.$('.stx-pt-tabs')) === null);
    await ctx.close();
  }

  console.log('\n/partner/mooideco/tools (3 tools)');
  {
    const { ctx, page } = await open('/partner/mooideco/tools');
    const shown = (sel) => page.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) { return 'ontbreekt'; }
      const cs = getComputedStyle(el);
      return (cs.display === 'none' || cs.visibility === 'hidden') ? 'verborgen' : 'zichtbaar';
    }, sel);

    check('Sempertex header verborgen', (await shown('header#top')) === 'verborgen');
    check('Sempertex zijmenu verborgen', (await shown('.stx-insp .side')) === 'verborgen');
    check('Mooideco header staat er', (await shown('.stx-pt-bar')) === 'zichtbaar');
    const tabs = await page.$$eval('.stx-pt-tab', (els) => els.map((e) => e.textContent.trim() + '|' + e.getAttribute('href')));
    check('drie tabbladen, Nederlands', JSON.stringify(tabs) === JSON.stringify(['Kleurmixer|#calculator', 'Prijscalculator|#cost', 'Kleurzoeker|#colour']), JSON.stringify(tabs));
    check('calculator opent standaard', (await shown('#view-calculator')) === 'zichtbaar' && (await page.textContent('.stx-pt-tab.on')) === 'Kleurmixer');
    check('tabtitel is van Mooideco', (await page.title()) === 'Kleuren en prijzen berekenen | Mooideco', await page.title());
    const icon = await page.evaluate(() => (document.querySelector('link[rel~="icon"]') || {}).href || '');
    check('favicon is het Mooideco-icoon', icon.startsWith('data:image/png'), icon.slice(0, 30));
    const brand = await page.evaluate(() => getComputedStyle(document.querySelector('.stx-insp')).getPropertyValue('--purple').trim());
    check('huisstijlkleur van Mooideco', brand === '#5A6186', brand);
    check('font Montserrat', /Montserrat/.test(await page.evaluate(() => getComputedStyle(document.querySelector('.stx-insp')).fontFamily)));
    const h2 = await page.evaluate(() => { const cs = getComputedStyle(document.querySelector('#view-calculator h2')); return cs.fontFamily + ' | ' + cs.color; });
    check('titel niet in het font en paars van het Odoo-thema', /Montserrat/.test(h2) && !/27, 7, 61/.test(h2), h2);

    // Bestelblok: elke gekozen kleur is een zoeklink op mooideco.nl met de kleurcode.
    await page.click('#sw-inner .swatch:nth-child(3)');
    await page.click('#sw-outer .swatch:nth-child(5)');
    await page.waitForTimeout(250);
    const picks = await page.$$eval('a.stx-pt-pick', (els) => els.map((e) => ({ href: e.getAttribute('href'), code: e.getAttribute('data-code'), target: e.getAttribute('target') })));
    check('beide kleuren linken naar de zoekfunctie van Mooideco', picks.length === 2 && picks.every((p) =>
      /^https:\/\/www\.mooideco\.nl\/website\/index\.php\?Show=Search&KeyWord=\d{3}%20Sempertex$/.test(p.href) && p.href.includes(p.code) && p.target === '_blank'), JSON.stringify(picks));
    check('hoofdknop naar de Sempertex categorie van Mooideco', (await page.getAttribute('#stx-pt-main', 'href')) === 'https://www.mooideco.nl/sempertex-groothandel');

    // Taalschakelaar rechtsboven
    const langs = await page.$$eval('.stx-pt-lang a', (els) => els.map((e) => e.textContent + '|' + e.getAttribute('href') + '|' + (e.classList.contains('on') ? 'aan' : 'uit')));
    check('taalschakelaar NL/EN, NL staat aan', JSON.stringify(langs) === JSON.stringify(['NL|/nl/partner/mooideco/tools#calculator|aan', 'EN|/en_GB/partner/mooideco/tools#calculator|uit']), JSON.stringify(langs));
    const barBox = await page.evaluate(() => { const b = document.querySelector('.stx-pt-bar .stx-pt-in').getBoundingClientRect(); const l = document.querySelector('.stx-pt-lang').getBoundingClientRect(); return { right: Math.round(b.right - l.right), top: Math.round(l.top - b.top) }; });
    check('taalschakelaar staat rechtsboven', barBox.right < 60 && barBox.top < 40, JSON.stringify(barBox));

    // Kostprijscalculator
    await page.click('.stx-pt-tab[data-tool="cost"]');
    await page.waitForTimeout(300);
    check('tab kostprijscalculator opent de kostprijscalculator', (await shown('#view-cost')) === 'zichtbaar' && (await shown('#view-calculator')) === 'verborgen');
    check('actief tabblad volgt', (await page.textContent('.stx-pt-tab.on')) === 'Prijscalculator');
    check('geen "alles in de winkelmand"', (await shown('#cc-cart-all')) === 'verborgen');
    const hint = await page.textContent('[data-i18n="cc_mat_hint"]');
    check('uitleg vraagt de eigen inkoopprijs, niet inloggen', /eigen inkoopprijs/.test(hint) && !/ingelogd/.test(hint), hint.slice(0, 80));
    const note = await page.textContent('#cc-cat-note');
    check('catalogusregel zegt eigen prijs invullen', /Vul je eigen inkoopprijs per stuk in/.test(note) && !/shopaccount/.test(note), note);
    check('offerte zegt Mooideco, niet STX Tools', /Mooideco/.test(await page.textContent('#cc-doc-stx')), await page.textContent('#cc-doc-stx'));
    const heads = await page.$$eval('#view-cost h2, #view-cost h3', (els) => els.filter((e) => e.offsetParent).map((e) => getComputedStyle(e).fontFamily.split(',')[0] + ' ' + getComputedStyle(e).color));
    check('koppen van de kostprijscalculator in Montserrat', heads.length > 0 && heads.every((h) => /Montserrat/.test(h) && !/27, 7, 61/.test(h)), heads.join(' | '));
    const dot = await page.evaluate(() => getComputedStyle(document.querySelector('.cc-legend > :nth-child(1) i')).backgroundColor);
    check('legenda in Mooideco-kleuren', dot === 'rgb(58, 58, 93)', dot);
    check('geen vraag naar onze shopprijzen', await page.evaluate(() => !(performance.getEntriesByType('resource') || []).some((r) => /snippet\/autocomplete|get_combination_info/.test(r.name))));
    await page.screenshot({ path: path.resolve(__dirname, 'mooideco-cost.png'), fullPage: false });

    // Kleurmatch-tool
    await page.click('.stx-pt-tab[data-tool="colour"]');
    await page.waitForTimeout(400);
    check('tab kleurmatch-tool opent de kleurmatch-tool', (await shown('#view-colour')) === 'zichtbaar');
    await page.$eval('#ct-root input[type=color]', (e) => { e.value = '#7b87bf'; e.dispatchEvent(new Event('input', { bubbles: true })); e.dispatchEvent(new Event('change', { bubbles: true })); }).catch(() => {});
    await page.waitForTimeout(400);
    const shopBtn = await page.getAttribute('#ct-shop-btn', 'href');
    check('"Shop deze kleur" zoekt bij Mooideco', /^https:\/\/www\.mooideco\.nl\/website\/index\.php\?Show=Search&KeyWord=\d{3}%20Sempertex$/.test(shopBtn || ''), shopBtn);
    const ctLinks = await page.$$eval('#ct-root a.js-shop', (els) => els.map((e) => e.getAttribute('href') || ''));
    check('ballonnen in de palettes linken naar Mooideco', ctLinks.length > 0 && ctLinks.every((u) => u.startsWith('https://www.mooideco.nl/')), ctLinks.slice(0, 3).join(' '));
    check('geen winkelmandknoppen in de palettes', await page.evaluate(() => [...document.querySelectorAll('#ct-root .js-cart, #ct-root [class*="cart"]')].every((e) => !e.offsetParent)));
    await page.screenshot({ path: path.resolve(__dirname, 'mooideco-colour.png'), fullPage: false });

    const ENGELS = /\b(the|and|your|colour|color|tool|tools|item|items|shop|shoppen|palettes?|finish(es)?|chart|statement|punch|moodboard|upload|garland|blush|job|jobs|event|overhead|match|preview|shortlist|check|remove|settings|hue|profit|multiplier|follows|download|stuffing)\b/i;
    const PRODUCT = /^(Fashion|Pastel Matte|Pastel Dusk|Neon|Pearl|Metallic|Silk|Reflex|Crystal)( [A-Z][\w]+)*( \d{3})?$/;
    const engelsePerTool = {};
    for (const tool of ['calculator', 'cost', 'colour']) {
      await page.click(`.stx-pt-tab[data-tool="${tool}"]`);
      await page.waitForTimeout(300);
      engelsePerTool[tool] = await page.evaluate(([re, prod]) => {
        const ENG = new RegExp(re, 'i'), P = new RegExp(prod);
        const vis = (e) => { for (let n = e; n && n !== document.body; n = n.parentElement) { const cs = getComputedStyle(n); if (cs.display === 'none' || cs.visibility === 'hidden') return false; } return true; };
        const out = [];
        const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let n;
        while ((n = w.nextNode())) {
          const t = n.textContent.replace(/\s+/g, ' ').trim();
          if (!t || !n.parentElement || /SCRIPT|STYLE/.test(n.parentElement.tagName) || !vis(n.parentElement)) continue;
          if (P.test(t) || /Sempertex|Mooideco/.test(t) && !ENG.test(t.replace(/Sempertex[- ]\w+|Mooideco/g, ''))) continue;
          if (ENG.test(t)) out.push(t.slice(0, 60));
        }
        document.querySelectorAll('[placeholder],[aria-label],[title]').forEach((e) => {
          if (!vis(e)) return;
          ['placeholder', 'aria-label', 'title'].forEach((a) => { const v = e.getAttribute(a); if (v && ENG.test(v)) out.push('[' + a + '] ' + v); });
        });
        return out;
      }, [ENGELS.source, PRODUCT.source]);
    }
    const alleEngels = Object.entries(engelsePerTool).filter(([, v]) => v.length).map(([k, v]) => k + ': ' + v.join(' | '));
    check('geen Engelse woorden op de Nederlandse pagina (kleurnamen mogen)', alleEngels.length === 0, alleEngels.join(' || '));
    const uren = await page.evaluate(() => { location.hash = 'cost'; return new Promise((r) => setTimeout(() => r(document.querySelector('#cc-hours-total').textContent), 300)); });
    check('uren in het Nederlands (u, komma)', /^\d+(,\d)? u$/.test(uren), uren);

    const links = await page.$$eval('a', (els) => els.filter((e) => e.offsetParent !== null).map((e) => e.getAttribute('href') || ''));
    const homeward = links.filter((u) => /sempertex-?europe|^\/(shop|tools|inspiration|event|blog)/.test(u));
    check('geen zichtbare link terug naar onze eigen site', homeward.length === 0, homeward.join(' '));

    await page.click('.stx-pt-tab[data-tool="calculator"]');
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.resolve(__dirname, 'mooideco-desktop.png'), fullPage: true });
    check('laadscherm gaat 1x weg', (await page.evaluate(() => window.stxHideCalls)) === 1);
    await ctx.close();
  }

  console.log('\n/en_GB/partner/mooideco/tools (Engels)');
  {
    const { ctx, page } = await open('/en_GB/partner/mooideco/tools#cost');
    const tabs = await page.$$eval('.stx-pt-tab', (els) => els.map((e) => e.textContent.trim()));
    check('Engelse tabbladen', JSON.stringify(tabs) === JSON.stringify(['Double Stuffing Calculator', 'Cost Calculator', 'Colour Matching Tool']), JSON.stringify(tabs));
    check('opent op dezelfde tool', (await page.textContent('.stx-pt-tab.on')) === 'Cost Calculator');
    check('EN staat aan', (await page.textContent('.stx-pt-lang a.on')) === 'EN');
    check('NL-link gaat terug naar dezelfde tool', (await page.getAttribute('.stx-pt-lang a[data-lang="nl"]', 'href')) === '/nl/partner/mooideco/tools#cost');
    check('tabtitel Engels', (await page.title()) === 'Balloon colour and price tools | Mooideco', await page.title());
    check('terugknop Engels', (await page.textContent('.stx-pt-back')) === 'Visit the webshop');
    check('bestelblok Engels', (await page.textContent('.stx-pt-order h3')) === 'Order these balloons from Mooideco');
    const hint = await page.textContent('[data-i18n="cc_mat_hint"]');
    check('kostprijscalculator Engels, eigen inkoopprijs', /Enter your own purchase price per piece/.test(hint), hint.slice(0, 80));
    check('offerte zegt Mooideco', /Mooideco/.test(await page.textContent('#cc-doc-stx')));
    const nl = await page.evaluate(() => /\b(Kleurmixer|Prijscalculator|opdracht|Bestel deze)\b/.test(document.body.innerText));
    check('geen Nederlandse teksten op de Engelse pagina', !nl);
    await page.click('.stx-pt-tab[data-tool="colour"]');
    await page.waitForTimeout(200);
    check('NL-link volgt het tabblad', (await page.getAttribute('.stx-pt-lang a[data-lang="nl"]', 'href')) === '/nl/partner/mooideco/tools#colour');
    await page.click('.stx-pt-lang a[data-lang="nl"]');
    await page.waitForFunction(() => location.pathname === '/partner/mooideco/tools' && !!document.querySelector('.stx-pt-tab.on'), undefined, { timeout: 20000 });
    await page.waitForTimeout(800);
    check('klik op NL: Nederlandse pagina, zelfde tool', (await page.textContent('.stx-pt-tab.on')) === 'Kleurzoeker', await page.textContent('.stx-pt-tab.on'));
    await ctx.close();
  }

  console.log('\n/partner/mooideco/tools?saved=1 (Odoo-pagina met een opgeslagen kopie van de tools)');
  {
    const { ctx, page } = await open('/partner/mooideco/tools?saved=1#cost');
    await page.waitForTimeout(400);
    check('maar 1 keer de tools op de pagina', (await page.$$('[id="stx-insp-root"]')).length === 1);
    const tabs = await page.$$eval('.stx-pt-tab', (els) => els.map((e) => e.textContent.trim()));
    check('tabbladen Nederlands', JSON.stringify(tabs) === JSON.stringify(['Kleurmixer', 'Prijscalculator', 'Kleurzoeker']), JSON.stringify(tabs));
    const h = await page.textContent('#view-cost h2');
    check('teksten van de partner, niet die van de opgeslagen kopie', /Prijscalculator/.test(h.replace(/\s/g, '')) && !/OPGESLAGEN/.test(await page.evaluate(() => document.body.innerText)), h);
    check('kolom Artikel', (await page.textContent('[data-i18n="cc_col_item"]')) === 'Artikel');
    check('skin staat boven de tools die blijven', await page.evaluate(() => { const bar = document.querySelector('.stx-pt-bar'); const r = document.getElementById('stx-insp-root'); return !!bar && !!r && document.body.contains(bar) && !!(bar.compareDocumentPosition(r) & Node.DOCUMENT_POSITION_FOLLOWING); }));
    check('1 header en 1 rij tabbladen', (await page.$$('.stx-pt-bar')).length === 1 && (await page.$$('.stx-pt-tabs')).length === 1);
    check('1 footer', (await page.$$('.stx-pt-foot')).length === 1);
    await ctx.close();
  }

  console.log('\n/partner/mooideco/tools op telefoonformaat');
  {
    const { ctx, page } = await open('/partner/mooideco/tools#cost', 390);
    for (const tool of ['cost', 'colour', 'calculator']) {
      await page.click(`.stx-pt-tab[data-tool="${tool}"]`);
      await page.waitForTimeout(300);
      const scroll = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      check(`geen horizontale scroll op ${tool}`, scroll <= 2, scroll + 'px');
    }
    const header = await page.evaluate(() => { const els = ['.stx-pt-bar img', '.stx-pt-back', '.stx-pt-lang'].map((s) => document.querySelector(s).getBoundingClientRect()); return { rijen: new Set(els.map((r) => Math.round(r.top / 20))).size, rechts: Math.round(window.innerWidth - els[2].right) }; });
    check('logo, terugknop en taal op 1 regel op een telefoon', header.rijen === 1 && header.rechts >= 8, JSON.stringify(header));
    const tabsFit = await page.evaluate(() => { const n = document.querySelector('.stx-pt-tabs .stx-pt-in'); return n.scrollWidth - n.clientWidth; });
    check('tabbladen passen op een telefoon', tabsFit <= 2, tabsFit + 'px');
    await page.screenshot({ path: path.resolve(__dirname, 'mooideco-mobile.png'), fullPage: false });
    await ctx.close();
  }

  // Drie partners met 1 vaste taal (20/10/2026). Geopend op het pad zonder taalprefix, dus Odoo's
  // Nederlands: de skin moet daar toch Engels of Italiaans van maken.
  const NEW_PARTNERS = [
    { slug: 'go-international', name: 'Go International', brand: '#0c6eaf', font: 'Albert Sans',
      tabs: ['Double Stuffing Calculator', 'Cost Calculator', 'Colour Matching Tool'],
      title: 'Balloon colour and price tools | Go International', cur: '£', curCode: 'GBP', dist: 'mi', vat: 20,
      shop: /^https:\/\/gointernational\.co\.uk\/index\.php\?main_page=search_result&keyword=Sempertex%20\d{3}$/,
      hint: /Enter your own purchase price per piece/, foreign: /\b(Kleurmixer|opdracht|inkoopprijs|Bewaar|Instellingen|Materiaal)\b/ },
    { slug: 'dattas-wholesale', name: "Datta's", brand: '#0b81be', font: 'Montserrat',
      tabs: ['Double Stuffing Calculator', 'Cost Calculator', 'Colour Matching Tool'],
      title: "Balloon colour and price tools | Datta's Wholesale", cur: '£', curCode: 'GBP', dist: 'mi', vat: 20,
      shop: /^https:\/\/www\.dattaswholesale\.co\.uk\/action\/search\?search=[a-z]+(%20[a-z]+)+%20sempertex$/,
      hint: /Enter your own purchase price per piece/, foreign: /\b(Kleurmixer|opdracht|inkoopprijs|Bewaar|Instellingen|Materiaal)\b/ },
    { slug: 'europarty', name: 'Euro Party', brand: '#e5007e', font: 'Open Sans',
      tabs: ['Calcolatore double stuffing', 'Calcolatore prezzi', 'Trova colore'],
      title: 'Strumenti per colori e prezzi dei palloncini | Euro Party', cur: '€', curCode: 'EUR', dist: 'km', vat: 22,
      shop: /^https:\/\/www\.europarty\.it\/catalogsearch\/result\/\?q=Sempertex%20\d{3}$/,
      hint: /Inserisci il tuo prezzo d’acquisto al pezzo/,
      foreign: /\b(Kleurmixer|opdracht|inkoopprijs|Bewaar|Instellingen|Materiaal|Settings|Saved quotes|Materials|Inner balloon|Upload a photo|Shop this colour)\b/ },
    // B2B-kopie van Euro Party (27/10/2026): alles hetzelfde, maar geen enkele link naar de B2C-shop.
    { slug: 'europarty-b2b', name: 'Euro Party', brand: '#e5007e', font: 'Open Sans',
      tabs: ['Calcolatore double stuffing', 'Calcolatore prezzi', 'Trova colore'],
      title: 'Strumenti per colori e prezzi dei palloncini | Euro Party', cur: '€', curCode: 'EUR', dist: 'km', vat: 22,
      shop: /^https:\/\/b2b\.europarty\.it\/catalogsearch\/result\/\?q=Sempertex%20\d{3}$/,
      notHost: 'www.europarty.it',
      hint: /Inserisci il tuo prezzo d’acquisto al pezzo/,
      foreign: /\b(Kleurmixer|opdracht|inkoopprijs|Bewaar|Instellingen|Materiaal|Settings|Saved quotes|Materials|Inner balloon|Upload a photo|Shop this colour)\b/ },
    // Pro Balloon Shop (27/10/2026): Shopify, every colour straight to its own product page.
    { slug: 'pro-balloon-shop', name: 'Pro Balloon Shop', brand: '#196c7f', font: 'Figtree',
      tabs: ['Double Stuffing Calculator', 'Cost Calculator', 'Colour Matching Tool'],
      title: 'Balloon colour and price tools | Pro Balloon Shop', cur: '£', curCode: 'GBP', dist: 'mi', vat: 20,
      shop: /^https:\/\/proballoonshop\.co\.uk\/products\/sempertex-[a-z0-9-]+$/,
      hint: /Enter your own purchase price per piece/, foreign: /\b(Kleurmixer|opdracht|inkoopprijs|Bewaar|Instellingen|Materiaal)\b/ },
    // Irish Party Supplies (29/10/2026): Shopify, exact phrase search per colour ("blue 040"),
    // colours they do not stock go to their Sempertex category.
    { slug: 'irish-party-supplies', name: 'Irish Party Supplies', brand: '#0f59a8', font: 'Montserrat',
      tabs: ['Double Stuffing Calculator', 'Cost Calculator', 'Colour Matching Tool'],
      title: 'Balloon colour and price tools | Irish Party Supplies', cur: '€', curCode: 'EUR', dist: 'km', vat: 23,
      shop: /^https:\/\/www\.irishpartysupplies\.ie\/(search\?q=%22[a-z]+(%20[a-z]+)*%20\d{3}%22&type=product|collections\/sempertex)$/,
      hint: /Enter your own purchase price per piece/, foreign: /\b(Kleurmixer|opdracht|inkoopprijs|Bewaar|Instellingen|Materiaal)\b/ },
    // Northwest Greetings (29/10/2026): WooCommerce, every colour straight to its 12" product page.
    { slug: 'northwest-greetings', name: 'Northwest Greetings', brand: '#6a061c', font: 'Roboto',
      tabs: ['Double Stuffing Calculator', 'Cost Calculator', 'Colour Matching Tool'],
      title: 'Balloon colour and price tools | Northwest Greetings', cur: '£', curCode: 'GBP', dist: 'mi', vat: 20,
      shop: /^https:\/\/northwestgreetings\.co\.uk\/product\/[a-z0-9-]+\/$/,
      hint: /Enter your own purchase price per piece/, foreign: /\b(Kleurmixer|opdracht|inkoopprijs|Bewaar|Instellingen|Materiaal)\b/ }
  ];
  for (const N of NEW_PARTNERS) {
    console.log(`\n/partner/${N.slug}/tools (vaste taal, ${N.curCode})`);
    const { ctx, page } = await open(`/partner/${N.slug}/tools`);
    const tabs = await page.$$eval('.stx-pt-tab', (els) => els.map((e) => e.textContent.trim()));
    check('tabbladen in de taal van de partner', JSON.stringify(tabs) === JSON.stringify(N.tabs), JSON.stringify(tabs));
    check('geen taalschakelaar', (await page.$('.stx-pt-lang')) === null);
    check('tabtitel', (await page.title()) === N.title, await page.title());
    const brand = await page.evaluate(() => getComputedStyle(document.querySelector('.stx-insp')).getPropertyValue('--purple').trim());
    check('huisstijlkleur', brand.toLowerCase() === N.brand, brand);
    check('font ' + N.font, new RegExp(N.font).test(await page.evaluate(() => getComputedStyle(document.querySelector('.stx-insp')).fontFamily)));
    const logo = await page.evaluate(() => { const i = document.querySelector('.stx-pt-bar img'); return i && i.complete && i.naturalWidth > 200 && i.getBoundingClientRect().height > 30; });
    check('logo staat in de header', logo);
    await page.click('#sw-inner .swatch:nth-child(3)');
    await page.click('#sw-outer .swatch:nth-child(5)');
    await page.waitForTimeout(250);
    const picks = await page.$$eval('a.stx-pt-pick', (els) => els.map((e) => e.getAttribute('href')));
    check('gekozen kleuren zoeken in de webshop van de partner', picks.length === 2 && picks.every((h) => N.shop.test(h)), JSON.stringify(picks));
    if (N.notHost) {
      const wrong = await page.$$eval('a[href]', (els, host) => els.map((e) => e.href).filter((h) => h.includes(host)), N.notHost);
      check('geen enkele link naar ' + N.notHost, wrong.length === 0, JSON.stringify(wrong.slice(0, 3)));
    }
    if (/^europarty/.test(N.slug)) {
      // Dario 27/10/2026: geen "Realizzato da Sempertex Europe per Euro Party." onder de tools.
      check('geen creditregel onder de tools', (await page.$('.stx-pt-foot')) === null);
    }

    await page.click('.stx-pt-tab[data-tool="cost"]');
    await page.waitForTimeout(400);
    const hint = await page.textContent('[data-i18n="cc_mat_hint"]');
    check('prijscalculator vraagt eigen inkoopprijs', N.hint.test(hint), hint.slice(0, 90));
    check('offerte noemt de partner', (await page.textContent('#cc-doc-stx')).includes(N.name.replace("'s", '')), await page.textContent('#cc-doc-stx'));
    await page.click('#cc-open-settings');
    await page.waitForTimeout(300);
    const cur = await page.evaluate(() => document.getElementById('cc-s-currency').value + '|' + document.getElementById('cc-s-dist').value + '|' + document.getElementById('cc-s-vat').value);
    check(`instellingen beginnen op ${N.curCode}, ${N.dist}, btw ${N.vat}%`, cur === `${N.curCode}|${N.dist}|${N.vat}`, cur);
    await page.click('#cc-scrim', { position: { x: 5, y: 500 } });
    await page.waitForTimeout(300);
    check(`bedragen in ${N.cur}`, (await page.textContent('#view-cost')).includes(N.cur));
    await page.screenshot({ path: path.resolve(__dirname, `${N.slug}-cost.png`), fullPage: false });

    await page.click('.stx-pt-tab[data-tool="colour"]');
    await page.waitForTimeout(400);
    await page.$eval('#ct-root input[type=color]', (e) => { e.value = '#7b87bf'; e.dispatchEvent(new Event('input', { bubbles: true })); e.dispatchEvent(new Event('change', { bubbles: true })); }).catch(() => {});
    await page.waitForTimeout(400);
    const shopBtn = await page.getAttribute('#ct-shop-btn', 'href');
    check('"shop deze kleur" zoekt bij de partner', N.shop.test(shopBtn || ''), shopBtn);
    const bad = await page.evaluate((re) => { const m = new RegExp(re).exec(document.body.innerText); return m ? m[0] : ''; }, N.foreign.source);
    check('geen woorden uit een andere taal', !bad, bad);
    await page.screenshot({ path: path.resolve(__dirname, `${N.slug}-colour.png`), fullPage: false });

    // Opslaan: per partner apart, nooit in de sleutels van onze eigen /tools.
    await page.click('.stx-pt-tab[data-tool="cost"]');
    await page.waitForTimeout(200);
    const keys = await page.evaluate(() => { const ks = []; for (let i = 0; i < localStorage.length; i++) { ks.push(localStorage.key(i)); } return ks; });
    check('bewaart onder een eigen sleutel', keys.includes(`stx_quote_draft@${N.slug}`) && !keys.includes('stx_quote_draft'), keys.join(','));
    await page.click('#sw-inner .swatch:nth-child(3)').catch(() => {});
    await page.screenshot({ path: path.resolve(__dirname, `${N.slug}-desktop.png`), fullPage: false });
    await ctx.close();
  }

  console.log('\n/partner/go-international/tools op telefoonformaat');
  {
    const { ctx, page } = await open('/partner/go-international/tools#cost', 390);
    const scroll = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    check('geen horizontale scroll', scroll <= 2, scroll + 'px');
    await page.screenshot({ path: path.resolve(__dirname, 'go-international-mobile.png'), fullPage: false });
    await ctx.close();
  }

  console.log('\n/partner/liragram/tools?livechat=force (het CSS-vangnet apart)');
  {
    // Zet Odoo de chat ooit op een andere manier neer, dan moet de CSS hem alsnog
    // wegzetten. Hier mount de chat dus wel, ondanks can_load_livechat.
    const { ctx, page } = await open('/partner/liragram/tools?livechat=force');

    const host = await page.evaluate(() => {
      const el = document.querySelector('.o-livechat-root');
      if (!el) { return 'ontbreekt'; }
      return getComputedStyle(el).display === 'none' ? 'verborgen' : 'zichtbaar';
    });
    check('gemounte livechat host is verborgen', host === 'verborgen', host);

    const btn = await page.evaluate(() => {
      const el = document.querySelector('.o-livechat-root');
      if (!el || !el.shadowRoot) { return 'geen shadow root'; }
      const b = el.shadowRoot.querySelector('.o-livechat-LivechatButton');
      if (!b) { return 'geen knop'; }
      const r = b.getBoundingClientRect();
      return (r.width === 0 && r.height === 0) ? 'verborgen' : 'zichtbaar';
    });
    check('knop in de shadow root heeft geen plek op de pagina', btn === 'verborgen', btn);

    await ctx.close();
  }

  console.log('\n/partner/liragram/tools?noflag=1 (loader laadt Silkmas toch: het slot in de sectie zelf)');
  {
    const { ctx, page } = await open('/partner/liragram/tools?noflag=1');
    await page.waitForTimeout(400);
    check('Silkmas-sectie stopt zelf op een partnerpagina', (await page.$('[id^="stx-sm-"]')) === null);
    check('Silkmas-sectie is wel geladen (anders test dit niets)', await page.evaluate(() => window.__stxSilkmas === true));
    await ctx.close();
  }

  console.log('\n/tools (de gewone Sempertex pagina mag niet veranderen)');
  {
    const ctx = await browser.newContext({ viewport: { width: 1400, height: 1000 } });
    await ctx.addInitScript(() => { try { localStorage.setItem('stx_silkmas_beta', '1'); } catch (e) {} });
    const page = await ctx.newPage();
    await page.route('**', (r) => (r.request().url().startsWith(base) ? r.continue() : r.abort()));
    await page.goto(base + '/tools', { waitUntil: 'domcontentloaded' });
    await page.waitForSelector('#stx-insp-root', { timeout: 20000 });
    await page.waitForTimeout(800);

    const vis = (sel) => page.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) { return 'ontbreekt'; }
      const cs = getComputedStyle(el);
      return (cs.display === 'none' || cs.visibility === 'hidden') ? 'verborgen' : 'zichtbaar';
    }, sel);

    check('Sempertex header staat er gewoon', (await vis('header#top')) === 'zichtbaar');
    check('Sempertex footer staat er gewoon', (await vis('footer#bottom')) === 'zichtbaar');
    check('livechat staat er gewoon', (await vis('.o-livechat-root')) === 'zichtbaar');
    check('zijmenu met de drie tools staat er', (await vis('.stx-insp .side')) === 'zichtbaar');
    check('geen partnerheader', (await page.$('.stx-pt-bar')) === null);
    check('cookiebanner staat hier gewoon', (await vis('#website_cookies_bar .modal')) === 'zichtbaar');
    check('Silkmas-banner staat hier wel (testmodus aan)', (await vis('#stx-sm-bar')) === 'zichtbaar');
    check('geen bestelblok', (await page.$('.stx-pt-order')) === null);
    check('tabtitel ongewijzigd', (await page.title()) === 'Tools | Sempertex Europe', await page.title());
    const h = await page.textContent('#view-calculator h2');
    check('titel blijft Nederlands', /calculator/i.test(h || '') && !/Calculadora/.test(h || ''), h);
    await ctx.close();
  }

  console.log('\n/partner/onbekend/tools (partner bestaat niet)');
  {
    const ctx = await browser.newContext({ viewport: { width: 1400, height: 1000 } });
    const page = await ctx.newPage();
    await page.route('**', (r) => (r.request().url().startsWith(base) ? r.continue() : r.abort()));
    await page.goto(base + '/partner/onbekend/tools', { waitUntil: 'domcontentloaded' });
    await page.waitForSelector('#stx-insp-root', { timeout: 20000 });
    await page.waitForTimeout(800);
    check('geen skin, dus geen halve partnerpagina', (await page.$('.stx-pt-bar')) === null);
    check('calculator draait wel gewoon', (await page.$('#view-calculator .calc-grid')) !== null);
    await ctx.close();
  }

  await browser.close();
  server.close();

  console.log(failures === 0 ? '\nAlles in orde.\n' : `\n${failures} controle(s) mislukt.\n`);
  process.exit(failures === 0 ? 0 : 1);
})();
