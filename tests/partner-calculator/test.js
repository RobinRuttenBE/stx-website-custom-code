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
      re: /^(\\/(en_gb|fr|de))?\\/partner\\/[a-z0-9-]+\\/tools$/, paths: [] }
  ];
  var p = (window.location.pathname || '/').toLowerCase();
  if (p.length > 1 && p.charAt(p.length - 1) === '/') { p = p.slice(0, -1); }
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
      if (sec.re ? sec.re.test(p) : onPage(sec.paths)) { hits.push(sec); }
    }
    pending = hits.length;
    for (var j = 0; j < hits.length; j++) { load(hits[j]); }
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', run); } else { run(); }
})();
</script>`;

function odooPage() {
  return `<!doctype html><html lang="nl"><head><meta charset="utf-8">
<title>Tools | Sempertex Europe</title>
<link rel="icon" href="/web/image/website/1/favicon">
${LOADWALL_HEAD}
${HEAD_ANTIFLASH}
</head><body>
<div id="wrapwrap">
  <header id="top" class="o_header_standard"><div id="top_menu_container">
    <nav class="navbar"><ul id="top_menu" class="nav">
      <li class="nav-item"><a href="/shop" class="nav-link"><span>Shop</span></a></li>
      <li class="nav-item"><a href="/tools" class="nav-link"><span>Tools</span></a></li>
    </ul></nav></div>
  </header>
  <main><div id="wrap"><div class="oe_structure"></div></div></main>
  <footer id="bottom"><div class="o_footer">Sempertex Europe BV</div></footer>
</div>
${LOADWALL_BODY}
${LOADER}
</body></html>`;
}

const PARTNER_PATH = /^(?:\/(?:fr|de|en_gb))?\/partner\/[a-z0-9-]+\/tools$/;

function serve() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      const url = req.url.split('?')[0];
      if (url.startsWith('/sections/')) {
        const file = path.basename(url);
        const full = path.resolve(SECTIONS, file);
        if (!fs.existsSync(full)) { res.writeHead(404).end('nope'); return; }
        res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
        res.end(fs.readFileSync(full));
        return;
      }
      // Every other path renders the Odoo page: /tools and /partner/<slug>/tools alike.
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
      res.end(odooPage());
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
    check('disclaimer is vertaald', /aproximacion/.test(note || ''), (note || '').slice(0, 40));

    const brand = await page.evaluate(() =>
      getComputedStyle(document.querySelector('.stx-insp')).getPropertyValue('--purple').trim());
    check('huisstijlkleur staat op de calculator', brand === '#fc3995', brand);

    const font = await page.evaluate(() =>
      getComputedStyle(document.querySelector('.stx-insp')).fontFamily);
    check('font van de partner', /Nunito/.test(font), font);

    // Pick a colour on each side and read the order block back.
    await page.click('#sw-inner .swatch:nth-child(3)');
    await page.click('#sw-outer .swatch:nth-child(5)');
    await page.waitForTimeout(250);
    const picks = await page.$$eval('.stx-pt-pick .stx-pt-val', (els) => els.map((e) => e.textContent.trim()));
    check('gekozen kleuren staan in het bestelblok', picks.length === 2 && /\d{3}$/.test(picks[0]) && /\d{3}$/.test(picks[1]),
      JSON.stringify(picks));
    const codes = await page.getAttribute('#stx-pt-main', 'data-codes');
    check('kleurcodes staan klaar om te kopieren', /^\d{3}, \d{3}$/.test(codes || ''), codes);

    const href = await page.getAttribute('#stx-pt-main', 'href');
    check('bestelknop gaat naar de shop van Liragram', /^https:\/\/liragram\.com\//.test(href || ''), href);

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

  console.log('\n/tools (de gewone Sempertex pagina mag niet veranderen)');
  {
    const ctx = await browser.newContext({ viewport: { width: 1400, height: 1000 } });
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
    check('zijmenu met de drie tools staat er', (await vis('.stx-insp .side')) === 'zichtbaar');
    check('geen partnerheader', (await page.$('.stx-pt-bar')) === null);
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
