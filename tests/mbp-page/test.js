// Check for sections/mbp-v1.html: the public MBP page at /mbp.
//
// Serves a rebuilt Odoo page and injects the section the way the loader does,
// on /mbp and on the language versions. No connection to the live site.
//
//   node test.js
//
// Playwright comes from stx-tools/node_modules (or set STX_PLAYWRIGHT).

const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const SECTION = fs.readFileSync(path.resolve(__dirname, '../../sections/mbp-v1.html'), 'utf8');

function page() {
  return `<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>MBP | Sempertex Europe</title></head><body>
<div id="wrapwrap">
  <header id="top"><nav class="navbar"><ul id="top_menu" class="nav">
    <li class="nav-item"><a href="/shop" class="nav-link"><span>Shop</span></a></li>
  </ul></nav></header>
  <main><div id="wrap"><div class="oe_structure"></div></div></main>
  <footer id="bottom">Sempertex Europe BV</footer>
</div>
<script>
// Wat de section loader doet: markup injecteren en de scripts erin uitvoeren.
fetch('/section.html').then(function (r) { return r.text(); }).then(function (html) {
  var tpl = document.createElement('template');
  tpl.innerHTML = html;
  var scripts = Array.prototype.slice.call(tpl.content.querySelectorAll('script'));
  scripts.forEach(function (s) { s.parentNode.removeChild(s); });
  document.body.appendChild(tpl.content);
  scripts.forEach(function (old) {
    var s = document.createElement('script');
    s.text = old.text;
    document.body.appendChild(s);
  });
  window.__injected = true;
});
</script>
</body></html>`;
}

function serve() {
  return new Promise((res) => {
    const s = http.createServer((req, rsp) => {
      const url = req.url.split('?')[0];
      if (url === '/section.html') {
        rsp.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
        rsp.end(SECTION);
        return;
      }
      rsp.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
      rsp.end(page());
    });
    s.listen(0, '127.0.0.1', () => res(s));
  });
}

let failures = 0;
function check(name, ok, extra) {
  console.log((ok ? '  ok   ' : '  FOUT ') + name + (ok || extra === undefined ? '' : '  -> ' + extra));
  if (!ok) { failures++; }
}

(async () => {
  const server = await serve();
  const base = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch();

  async function open(p, width = 1400) {
    const ctx = await browser.newContext({ viewport: { width, height: 1000 } });
    const pg = await ctx.newPage();
    pg.on('pageerror', (e) => { check('geen scriptfout op ' + p, false, e.message); });
    await pg.route('**', (r) => (r.request().url().startsWith(base) ? r.continue() : r.abort()));
    await pg.goto(base + p, { waitUntil: 'domcontentloaded' });
    await pg.waitForTimeout(700);
    return { ctx, pg };
  }

  console.log('\n/mbp (Nederlands)');
  {
    const { ctx, pg } = await open('/mbp');

    check('sectie staat er', (await pg.$('#stx-mbp-root')) !== null);
    const vis = await pg.evaluate(() => {
      const n = document.querySelector('#stx-mbp-root');
      return n ? getComputedStyle(n).display !== 'none' : false;
    });
    check('sectie is zichtbaar', vis);

    const inWrap = await pg.evaluate(() => !!document.querySelector('#wrap #stx-mbp-root'));
    check('sectie zit in #wrap, zoals de andere secties', inWrap);

    const h1 = await pg.textContent('#stx-mbp-root h1');
    check('titel staat in het Nederlands', /Master Balloon Professional/.test(h1) && /Word/.test(h1), h1);

    const total = await pg.textContent('#mbp-count-total');
    const eu = await pg.textContent('#mbp-count-eu');
    check('aantallen kloppen', total === '266' && eu === '63', total + ' / ' + eu);

    const crit = await pg.$$eval('#mbp-p1 li, #mbp-p2 li', (e) => e.length);
    const pts = await pg.$$eval('#mbp-p1 b, #mbp-p2 b', (e) =>
      e.reduce((a, x) => a + parseInt(x.textContent, 10), 0));
    check('acht criteria, samen 100 punten', crit === 8 && pts === 100, crit + ' criteria, ' + pts + ' punten');

    const euCards = await pg.$$eval('#mbp-eu-grid .p', (e) => e.length);
    check('alle Europese MBPs staan er', euCards === 63, String(euCards));

    const euChips = await pg.$$eval('#mbp-eu-filters button', (e) => e.length);
    check('landenfilter voor Europa', euChips === 14, euChips + ' knoppen');

    await pg.click('#mbp-eu-filters [data-c="Italy"]');
    await pg.waitForTimeout(200);
    const italy = await pg.$$eval('#mbp-eu-grid .p', (e) => e.length);
    check('filteren op land werkt', italy === 27, String(italy));

    await pg.click('#mbp-eu-filters [data-c="__all__"]');
    await pg.fill('#mbp-search', 'audrey');
    await pg.waitForTimeout(200);
    const found = await pg.$$eval('#mbp-eu-grid .p', (e) => e.map((x) => x.textContent));
    check('zoeken op naam werkt', found.length === 1 && /Audrey Parsons/.test(found[0]), JSON.stringify(found));

    await pg.fill('#mbp-search', '');
    await pg.waitForTimeout(200);
    const restShown = await pg.$$eval('#mbp-rest-grid .p', (e) => e.length);
    await pg.click('#mbp-rest-toggle');
    await pg.waitForTimeout(250);
    const restAll = await pg.$$eval('#mbp-rest-grid .p', (e) => e.length);
    check('rest van de wereld staat ingeklapt onder Europa', restShown === 16 && restAll === 203,
      restShown + ' -> ' + restAll);

    // Europa moet prominenter staan dan de rest: hoger op de pagina en met zoekveld.
    const order = await pg.evaluate(() => {
      const eu = document.querySelector('#mbp-eu-grid').getBoundingClientRect().top;
      const rest = document.querySelector('#mbp-rest-grid').getBoundingClientRect().top;
      return { eu, rest, search: !!document.querySelector('#mbp-search') };
    });
    check('Europa staat boven de rest van de wereld', order.eu < order.rest && order.search);

    const book = await pg.getAttribute('#mbp-book', 'href');
    check('examenknop gaat naar de eventpagina', book === '/events', book);

    await pg.screenshot({ path: path.resolve(__dirname, 'mbp-nl.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\n/en_GB/mbp (Engels, met taalprefix)');
  {
    const { ctx, pg } = await open('/en_GB/mbp');
    const h1 = await pg.textContent('#stx-mbp-root h1');
    check('titel staat in het Engels', /Become a/.test(h1), h1);
    const book = await pg.getAttribute('#mbp-book', 'href');
    check('links houden de taalprefix', book === '/en_GB/events', book);
    await ctx.close();
  }

  console.log('\n/fr/mbp en /de/mbp');
  for (const [p, needle] of [['/fr/mbp', 'Devenez'], ['/de/mbp', 'Werde']]) {
    const { ctx, pg } = await open(p);
    const h1 = await pg.textContent('#stx-mbp-root h1');
    check(p + ' is vertaald', h1.indexOf(needle) === 0, h1);
    await ctx.close();
  }

  console.log('\n/shop (de sectie hoort daar niet te staan)');
  {
    const { ctx, pg } = await open('/shop');
    check('sectie verwijdert zichzelf buiten /mbp', (await pg.$('#stx-mbp-root')) === null);
    await ctx.close();
  }

  console.log('\nTelefoonformaat');
  {
    const { ctx, pg } = await open('/mbp', 390);
    const scroll = await pg.evaluate(() =>
      document.documentElement.scrollWidth - document.documentElement.clientWidth);
    check('geen horizontale scroll', scroll <= 2, scroll + 'px');
    await pg.screenshot({ path: path.resolve(__dirname, 'mbp-mobile.png'), fullPage: true });
    await ctx.close();
  }

  await browser.close();
  server.close();
  console.log(failures === 0 ? '\nAlles in orde.\n' : `\n${failures} controle(s) mislukt.\n`);
  process.exit(failures === 0 ? 0 : 1);
})();
