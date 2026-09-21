// Quick check for sections/menu-blog-button.html: button still there, popup gone, no network calls.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const BLOCK = fs.readFileSync(path.resolve(__dirname, '../../sections/menu-blog-button.html'), 'utf8');

function page(lang) {
  return `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><title>STX</title></head><body>
<header id="top"><nav class="navbar d-lg-block"><ul id="top_menu" class="top_menu nav d-flex">
<li class="nav-item"><a href="/shop" class="nav-link"><span>Shop</span></a></li>
<li class="nav-item"><a href="/tools" class="nav-link"><span>Tools</span></a></li>
<li class="nav-item border-bottom"><a href="/why-sempertex" class="nav-link"><span>Why Sempertex?</span></a></li>
</ul></nav>
<div class="o_navbar_mobile"><ul class="top_menu nav">
<li class="nav-item"><a href="/shop" class="nav-link"><span>Shop</span></a></li>
<li class="nav-item border-bottom"><a href="/tools" class="nav-link"><span>Tools</span></a></li>
</ul></div></header>
<div id="wrap">content</div>
${BLOCK}
</body></html>`;
}

const server = http.createServer((req, res) => {
  const p = req.url.split('?')[0];
  if (/^\/(en_GB|fr|de)?\/?$|^\/(en_GB|fr|de)?\/?blog/.test(p) || p === '/' ) {
    res.setHeader('Content-Type', 'text/html');
    return res.end(page(p.startsWith('/fr') ? 'fr' : 'nl'));
  }
  res.setHeader('Content-Type', 'text/html'); res.end(page('nl'));
});

let fails = 0;
function assert(c, m) { if (c) console.log('ok  ', m); else { console.error('FAIL', m); fails++; } }

(async () => {
  await new Promise(r => server.listen(0, r));
  const base = 'http://localhost:' + server.address().port;
  const b = await chromium.launch();
  const ctx = await b.newContext();
  const p = await ctx.newPage();
  const calls = [];
  p.on('request', r => { if (!r.url().startsWith(base) || r.url() !== base + '/') calls.push(r.method() + ' ' + r.url().replace(base, '')); });
  p.on('pageerror', e => { console.error('PAGEERROR', e.message); fails++; });

  await p.goto(base + '/');
  await p.waitForTimeout(1500);
  assert(await p.$('li.stx-blog-item a.nav-link[href="/blog"]') !== null, 'desktop: Blog button in the menu row');
  assert(await p.$('li.stx-blog-item-m a.nav-link[href="/blog"]') !== null, 'mobile: Blog in the collapsed menu');
  assert(await p.$('.stx-blog-pop') === null, 'desktop: no popup element');
  assert(await p.$('.stx-blog-pop-m') === null, 'mobile: no pinned title line');
  assert(await p.$eval('#top_menu', e => e.classList.contains('stx-has-blog')), 'menu row gets stx-has-blog');
  const extra = calls.filter(c => /autocomplete|sitemap|\/blog\//.test(c));
  assert(extra.length === 0, 'no background requests any more (' + (extra.join(', ') || 'none') + ')');

  await p.goto(base + '/fr/');
  await p.waitForTimeout(800);
  assert(await p.$('li.stx-blog-item a.nav-link[href="/fr/blog"]') !== null, 'fr: link keeps the language prefix');

  const ls = await p.evaluate(() => { try { localStorage.setItem('stx_blog_pin_v1', 'x'); localStorage.setItem('stx_blog_pop_off', 'y'); } catch (e) {} return 1; });
  await p.reload(); await p.waitForTimeout(800);
  const left = await p.evaluate(() => [localStorage.getItem('stx_blog_pin_v1'), localStorage.getItem('stx_blog_pop_off')]);
  assert(left[0] === null && left[1] === null, 'old popup keys are cleaned up on load (' + JSON.stringify(left) + ')');

  await b.close(); server.close();
  console.log(fails ? 'SOME CHECKS FAILED' : 'ALL CHECKS PASSED');
  process.exit(fails ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
