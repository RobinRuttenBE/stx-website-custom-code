// Check for the order block and the mobile order bar in the Colour Matching Tool (/tools#colour).
//
// Serves a small Odoo-like page at /tools that loads sections/inspiration-v18.html from this repo.
//   ?login=1   header has a /my/home link (logged in)
//   ?prices=1  the shop search route returns prices (account sees prices, cart buttons on)
//
//   node test.js
//
// Playwright comes from stx-tools/node_modules (or set STX_PLAYWRIGHT to another path).

const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const SECTIONS = path.resolve(__dirname, '../../sections');
const OUT = __dirname;

function page(login) {
  return `<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tools | Sempertex Europe</title></head><body>
<div id="wrapwrap"><header id="top"><nav><a href="/shop">Shop</a> ${login ? '<a href="/my/home">Mijn account</a>' : '<a href="/web/login">Inloggen</a>'}</nav></header>
<main><div id="wrap"></div></main><footer>footer</footer></div>
<script>
fetch('/sections/inspiration-v18.html').then(function (r) { return r.text(); }).then(function (h) {
  var tpl = document.createElement('template'); tpl.innerHTML = h;
  var scripts = Array.prototype.slice.call(tpl.content.querySelectorAll('script'));
  scripts.forEach(function (s) { s.parentNode.removeChild(s); });
  document.body.appendChild(tpl.content);
  scripts.forEach(function (o) { var s = document.createElement('script'); s.text = o.text; document.body.appendChild(s); });
});
</script></body></html>`;
}

const server = http.createServer((req, res) => {
  const u = new URL(req.url, 'http://x');
  if (u.pathname.startsWith('/sections/')) {
    const f = path.join(SECTIONS, u.pathname.slice('/sections/'.length));
    if (fs.existsSync(f)) { res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); return res.end(fs.readFileSync(f)); }
    res.writeHead(404); return res.end();
  }
  if (u.pathname.endsWith('/website/snippet/autocomplete')) {
    const prices = /prices=1/.test(req.headers.referer || '');
    let body = '';
    req.on('data', (c) => { body += c; });
    return req.on('end', () => {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: { results: [{ name: 'R12 - test', website_url: '/shop/1', detail: prices ? '<span class="oe_currency_value">12,50</span>&nbsp;€' : '' }], results_count: 1, parts: {} } }));
    });
  }
  if (u.pathname === '/tools') { res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); return res.end(page(u.searchParams.get('login') === '1')); }
  res.writeHead(404); res.end();
});

(async () => {
  await new Promise((r) => server.listen(0, r));
  const base = 'http://127.0.0.1:' + server.address().port;
  const browser = await chromium.launch();
  const results = [];
  const check = (name, ok, extra) => { results.push((ok ? 'PASS ' : 'FAIL ') + name + (extra ? '  ' + extra : '')); };

  async function open(q, viewport) {
    const ctx = await browser.newContext({ viewport });
    const pg = await ctx.newPage();
    const events = [];
    await pg.exposeFunction('__ev', (e) => events.push(e));
    await pg.addInitScript(() => { window.posthog = { capture: function (e, p) { window.__ev(e + ' ' + JSON.stringify(p || {})); } }; });
    await pg.goto(base + '/tools' + q + '#colour');
    await pg.waitForSelector('#ct-order', { timeout: 20000 });
    await pg.waitForTimeout(2500);
    return { ctx, pg, events };
  }

  // 1. Niet ingelogd, desktop: blok met account + login in de kaart, geen pick-event bij laden.
  {
    const { ctx, pg, events } = await open('', { width: 1440, height: 900 });
    const anon = await pg.$('#ct-order .ct-anon');
    check('logged out: account block in card', !!anon);
    const login = await pg.getAttribute('#ct-order .ct-login', 'href');
    check('logged out: login returns to #colour', /redirect=%2Ftools%23colour/.test(login || ''), login);
    check('no colour_tool_pick on page load', !events.some((e) => e.startsWith('colour_tool_pick')), events.filter((e) => e.startsWith('colour_tool')).join(' | '));
    const cartVisible = await pg.isVisible('#ct-order [data-a=cart]');
    check('logged out: no cart button', !cartVisible);
    await (await pg.$('.ct-card')).scrollIntoViewIfNeeded();
    await pg.screenshot({ path: path.join(OUT, 'desktop-logged-out.png'), clip: await (await pg.$('.ct-card')).boundingBox() });
    await ctx.close();
  }

  // 2. Niet ingelogd, mobiel: balk pas na een echte keuze, weg zodra de kaart in beeld is.
  {
    const { ctx, pg, events } = await open('', { width: 390, height: 844 });
    await pg.evaluate(() => document.querySelector('#ct-root').scrollIntoView());
    await pg.waitForTimeout(400);
    let on = await pg.$eval('#ct-bar', (b) => b.classList.contains('on'));
    check('mobile: no bar before a real pick', !on);
    await pg.evaluate(() => document.querySelector('#stx-insp-root').stxColour ? 0 : 0);
    // echte keuze via de colour chart
    await pg.evaluate(() => { var r = document.querySelector('.stx-insp'); r.stxColour.setTarget('#2a7fd4', 'chart'); });
    await pg.evaluate(() => document.querySelector('#ct-root').scrollIntoView());
    await pg.waitForTimeout(600);
    on = await pg.$eval('#ct-bar', (b) => b.classList.contains('on'));
    check('mobile: bar shows after a pick', on);
    check('colour_tool_pick after a real pick', events.some((e) => e.startsWith('colour_tool_pick')));
    check('colour_tool_bar_view tracked', events.some((e) => e.startsWith('colour_tool_bar_view')));
    const label = await pg.textContent('#ct-bar button');
    check('mobile logged out: bar button says Bestellen', label.trim() === 'Bestellen', label);
    await pg.screenshot({ path: path.join(OUT, 'mobile-bar-logged-out.png') });
    await pg.click('#ct-bar button');
    await pg.waitForTimeout(1200);
    on = await pg.$eval('#ct-bar', (b) => b.classList.contains('on'));
    check('mobile: bar hides when card is in view', !on);
    check('order click tracked', events.some((e) => e.startsWith('colour_tool_order_click') && e.includes('scroll')));
    await pg.screenshot({ path: path.join(OUT, 'mobile-card-logged-out.png') });
    await ctx.close();
  }

  // 3. Ingelogd met prijzen: cart-knop in de kaart, balkknop = In winkelmandje, geen accountblok.
  {
    const { ctx, pg } = await open('?login=1&prices=1', { width: 390, height: 844 });
    await pg.waitForTimeout(4000);
    const shopOn = await pg.$eval('.stx-insp', (r) => r.classList.contains('stx-shop-on'));
    check('logged in + prices: shop on', shopOn);
    check('logged in: no account block', !(await pg.$('#ct-order .ct-anon')));
    if (shopOn) {
      check('logged in + prices: cart button visible', await pg.isVisible('#ct-order [data-a=cart]'), await pg.textContent('#ct-order [data-a=cart]'));
      await pg.evaluate(() => { document.querySelector('.stx-insp').stxColour.setTarget('#e0457b', 'chart'); document.querySelector('#ct-root').scrollIntoView(); });
      await pg.waitForTimeout(600);
      const label = await pg.textContent('#ct-bar button');
      check('logged in + prices: bar button adds to cart', label.trim() === 'In winkelmandje', label);
      await pg.screenshot({ path: path.join(OUT, 'mobile-bar-logged-in.png') });
      await (await pg.$('.ct-card')).scrollIntoViewIfNeeded();
      await pg.waitForTimeout(500);
      await pg.screenshot({ path: path.join(OUT, 'mobile-card-logged-in.png') });
    }
    await ctx.close();
  }

  // 4. Taal: Engels op /en_gb/tools wordt niet getest (zelfde code), wel dat alle sleutels in 4 talen staan.
  const src = fs.readFileSync(path.join(SECTIONS, 'inspiration-v18.html'), 'utf8');
  ['ct_cart_one', 'ct_order_h', 'ct_order_note', 'ct_order_reg', 'ct_order_login', 'ct_bar_go'].forEach((k) => {
    const n = (src.match(new RegExp('\\b' + k + ':', 'g')) || []).length;
    check('string ' + k + ' in 4 languages', n === 4, String(n));
  });

  await browser.close();
  server.close();
  console.log(results.join('\n'));
  if (results.some((r) => r.startsWith('FAIL'))) process.exitCode = 1;
})();
