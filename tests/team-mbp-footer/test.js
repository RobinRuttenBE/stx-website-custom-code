// Check for the team page, the new MBP page, the new footer and the MBP menu button:
//   sections/team-v1.html          -> /team
//   sections/mbp-v2.html           -> /mbp
//   sections/footer-v1.html        -> every page (Odoo footer replaced)
//   sections/footer-antiflash.html -> inline, hides the old footer until then
//   sections/menu-blog-button.html -> inline, Blog + MBP in the menu
//
// Serves a rebuilt Odoo page with old content in #wrap and an old footer,
// and injects the sections the way the loader does. No connection to the
// live site except Google Fonts and the team photos on sempertexeurope.com.
//
//   node test.js
//
// Playwright comes from stx-tools/node_modules (or set STX_PLAYWRIGHT).

const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const REPO = path.resolve(__dirname, '../..');
const read = (f) => fs.readFileSync(path.join(REPO, f), 'utf8');
const MENU = read('sections/menu-blog-button.html');
const ANTIFLASH = read('sections/footer-antiflash.html');

function sectionsFor(urlPath) {
  const p = urlPath.replace(/\/+$/, '').toLowerCase();
  const out = [];
  if (p.endsWith('/team')) out.push('team-v1.html');
  if (p.endsWith('/mbp')) out.push('mbp-v2.html');
  out.push('footer-v1.html');
  return out;
}

function page(urlPath, opts) {
  const lang = /^\/fr/.test(urlPath) ? 'fr' : /^\/de/.test(urlPath) ? 'de' : /^\/en_gb/i.test(urlPath) ? 'en-GB' : 'nl';
  const files = JSON.stringify(opts.noFooter ? sectionsFor(urlPath).filter((f) => f !== 'footer-v1.html') : sectionsFor(urlPath));
  return `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><title>STX</title>
<style>
  body { margin: 0; font-family: Arial; }
  header#top { position: ${opts.fixedHeader ? 'fixed' : 'static'}; top: 0; left: 0; right: 0; height: 70px; background: #fff; z-index: 1000; border-bottom: 1px solid #ddd; }
  ${opts.fixedHeader ? 'main { padding-top: 71px; }' : ''}
  .top_menu { display: flex; list-style: none; margin: 0; padding: 20px; gap: 16px; box-sizing: border-box; }
  h2, h3 { color: red; font-family: serif; } /* Odoo-achtige globale stijl die NIET mag doorlekken */
  footer#bottom { background: #eee; color: #333; padding: 40px; }
</style></head><body>
<div id="wrapwrap">
  <header id="top"><nav class="navbar d-lg-block"><ul id="top_menu" class="top_menu nav">
    <li class="nav-item"><a href="/shop" class="nav-link"><span>Shop</span></a></li>
    <li class="nav-item"><a href="/tools" class="nav-link"><span>Tools</span></a></li>
  </ul></nav>
  <div class="o_navbar_mobile"><ul class="top_menu nav">
    <li class="nav-item border-bottom"><a href="/shop" class="nav-link"><span>Shop</span></a></li>
  </ul></div></header>
  <main><div id="wrap" class="oe_structure"><section class="s_company_team"><h2>Oude Odoo teaminhoud</h2></section></div></main>
  <footer id="bottom" class="o_footer"><div id="footer" class="oe_structure"><h3>Oude footer Openingsuren</h3></div>
    <div class="o_footer_copyright">Copyright oud</div></footer>
</div>
${MENU}
${ANTIFLASH}
<script>
window.STX_SECTIONS_BASE = location.origin + '/sections/';
var files = ${files};
var pending = files.length;
files.forEach(function (f) {
  fetch('/sections/' + f).then(function (r) { return r.text(); }).then(function (html) {
    var tpl = document.createElement('template');
    tpl.innerHTML = html;
    var scripts = Array.prototype.slice.call(tpl.content.querySelectorAll('script'));
    scripts.forEach(function (s) { s.parentNode.removeChild(s); });
    document.body.appendChild(tpl.content);
    scripts.forEach(function (old) { var s = document.createElement('script'); s.text = old.text; document.body.appendChild(s); });
    if (--pending === 0) { window.__injected = true; }
  });
});
</script>
</body></html>`;
}

function serve() {
  return new Promise((res) => {
    const s = http.createServer((req, rsp) => {
      const [url, qs] = req.url.split('?');
      if (url.startsWith('/sections/') || url.startsWith('/assets/')) {
        const f = path.join(REPO, decodeURIComponent(url));
        if (!f.startsWith(REPO) || !fs.existsSync(f)) { rsp.writeHead(404); rsp.end(); return; }
        const ext = path.extname(f);
        rsp.writeHead(200, { 'content-type': { '.html': 'text/html; charset=utf-8', '.jpg': 'image/jpeg', '.png': 'image/png' }[ext] || 'application/octet-stream' });
        rsp.end(fs.readFileSync(f));
        return;
      }
      const q = new URLSearchParams(qs || '');
      rsp.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
      rsp.end(page(url, { fixedHeader: q.get('fixed') === '1', noFooter: q.get('nofooter') === '1' }));
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
  const shots = __dirname;

  async function open(p, width = 1400, height = 1000) {
    const ctx = await browser.newContext({ viewport: { width, height } });
    const pg = await ctx.newPage();
    pg.on('pageerror', (e) => { check('geen scriptfout op ' + p, false, e.message); });
    await pg.route('**', (r) => {
      const u = r.request().url();
      if (u.startsWith(base)) return r.continue();
      if (/fonts\.(googleapis|gstatic)|sempertexeurope\.com\/web\/image/.test(u)) return r.continue();
      return r.abort();
    });
    await pg.goto(base + p, { waitUntil: 'domcontentloaded' });
    await pg.waitForFunction(() => window.__injected === true, null, { timeout: 15000 });
    await pg.waitForTimeout(1200);
    return { ctx, pg };
  }
  const noHScroll = async (pg) => {
    const r = await pg.evaluate(() => {
      const w = window.innerWidth;
      const wide = [];
      const walk = (rootNode, label) => rootNode.querySelectorAll('*').forEach((el) => {
        const b = el.getBoundingClientRect();
        if (b.right > w + 1 && b.width > 0) wide.push(label + (el.id ? '#' + el.id : '') + '.' + String(el.className).slice(0, 30) + ' ' + Math.round(b.right));
        if (el.shadowRoot) walk(el.shadowRoot, 'shadow:');
      });
      walk(document, '');
      return { ok: document.documentElement.scrollWidth <= w + 1, sw: document.documentElement.scrollWidth, wide: wide.slice(0, 6) };
    });
    if (!r.ok) console.log('       breed: ' + r.sw + ' ' + r.wide.join(' | '));
    return r.ok;
  };

  console.log('\n/team (Nederlands, desktop)');
  {
    const { ctx, pg } = await open('/team');
    const r = await pg.evaluate(() => {
      const host = document.querySelector('#wrap > #stx-team-host');
      const sr = host && host.shadowRoot;
      const old = document.querySelector('#wrap > section.s_company_team');
      const h2 = sr && sr.querySelector('h2');
      return {
        host: !!sr,
        oldHidden: old && getComputedStyle(old).display === 'none',
        members: sr ? sr.querySelectorAll('.member').length : 0,
        ceo: sr ? !!sr.querySelector('.ceo-card') : false,
        h2font: h2 ? getComputedStyle(h2).fontFamily : '',
        h2colour: h2 ? getComputedStyle(h2).color : '',
        title: sr ? sr.querySelector('h1').textContent : '',
        shopHref: sr ? sr.querySelector('.btn-row a').getAttribute('href') : '',
      };
    });
    check('team staat in #wrap (shadow root)', r.host);
    check('oude Odoo-inhoud verborgen', r.oldHidden);
    check('20 kaarten (14 team + 6 ambassadors) + CEO-kaart', r.members === 20 && r.ceo, r.members + ' kaarten');
    check('Rethink Sans in de pagina', /Rethink Sans/.test(r.h2font), r.h2font);
    check('Odoo-CSS lekt niet door (h2 niet rood)', r.h2colour !== 'rgb(255, 0, 0)', r.h2colour);
    check('titel', /Het team achter/.test(r.title), r.title);
    check('shoplink zonder prefix op NL', r.shopHref === '/shop', r.shopHref);
    check('geen horizontale scroll', await noHScroll(pg));
    await pg.screenshot({ path: path.join(shots, 'team-desktop.png'), fullPage: true });

    // Ankerlink naar het magazijn
    await pg.evaluate(() => document.querySelector('#stx-team-host').shadowRoot.querySelector('.dept-nav a[href="#magazijn"]').click());
    await pg.waitForTimeout(1200);
    const pos = await pg.evaluate(() => {
      const sr = document.querySelector('#stx-team-host').shadowRoot;
      return { sec: Math.round(sr.getElementById('magazijn').getBoundingClientRect().top), nav: Math.round(sr.querySelector('.dept-nav').getBoundingClientRect().top), navH: sr.querySelector('.dept-nav').offsetHeight };
    });
    check('anker #magazijn scrollt naar de sectie, onder de sticky balk', pos.sec >= pos.navH - 2 && pos.sec < pos.navH + 60, JSON.stringify(pos));
    check('afdelingsbalk blijft bovenaan plakken', pos.nav >= -1 && pos.nav <= 1, JSON.stringify(pos));
    await ctx.close();
  }

  console.log('\n/team met een vaste Odoo-header');
  {
    const { ctx, pg } = await open('/team?fixed=1');
    await pg.evaluate(() => window.scrollTo(0, 2500));
    await pg.waitForTimeout(400);
    const navTop = await pg.evaluate(() => Math.round(document.querySelector('#stx-team-host').shadowRoot.querySelector('.dept-nav').getBoundingClientRect().top));
    check('sticky balk staat onder de header (70 px)', navTop >= 69 && navTop <= 72, navTop);
    await ctx.close();
  }

  console.log('\n/fr/team (mobiel)');
  {
    const { ctx, pg } = await open('/fr/team', 390, 844);
    const shopHref = await pg.evaluate(() => document.querySelector('#stx-team-host').shadowRoot.querySelector('.btn-row a').getAttribute('href'));
    check('shoplink krijgt /fr', shopHref === '/fr/shop', shopHref);
    const fr = await pg.evaluate(() => { const sr = document.querySelector('#stx-team-host').shadowRoot; return [sr.querySelector('.stx-doc').getAttribute('lang'), sr.querySelector('h1').textContent, sr.querySelector('.btn-row a').textContent]; });
    check('teampagina in het Frans', fr[0] === 'fr' && /L’équipe derrière le ballon/.test(fr[1]) && fr[2] === 'Vers la boutique', fr.join(' | '));
    check('geen horizontale scroll op mobiel', await noHScroll(pg));
    const tap = await pg.evaluate(async () => {
      const sr = document.querySelector('#stx-team-host').shadowRoot;
      const withBio = Array.from(sr.querySelectorAll('.member')).filter((m) => m.querySelector('.bio'));
      withBio[0].click(); const first = withBio[0].classList.contains('open');
      withBio[1].click(); const swap = !withBio[0].classList.contains('open') && withBio[1].classList.contains('open');
      withBio[1].click(); const closed = !withBio[1].classList.contains('open');
      const amb = Array.from(sr.querySelectorAll('.member.amb img'));
      amb.forEach((i) => { i.loading = 'eager'; });
      const wait = (i) => (i.complete ? null : new Promise((r) => { i.onload = r; i.onerror = r; setTimeout(r, 8000); }));
      await Promise.all(amb.map(wait));
      return { first, swap, closed, cols: getComputedStyle(sr.querySelector('.team-grid')).gridTemplateColumns.split(' ').length,
        amb: amb.length, ambOk: amb.filter((i) => i.naturalWidth > 0).length };
    });
    check('tik opent de bio, andere kaart sluit hem, tweede tik sluit', tap.first && tap.swap && tap.closed, JSON.stringify(tap));
    check('2 kaarten naast elkaar op mobiel', tap.cols === 2, tap.cols);
    check('ambassadeursfoto\'s laden (6)', tap.amb === 6 && tap.ambOk === 6, tap.ambOk + '/' + tap.amb);
    await pg.screenshot({ path: path.join(shots, 'team-mobile.png'), fullPage: true });
    await ctx.close();
  }

  for (const [p, re] of [['/en_GB/team', /The team behind the balloon/], ['/de/team', /Das Team hinter dem Ballon/]]) {
    const { ctx, pg } = await open(p);
    const h1 = await pg.evaluate(() => document.querySelector('#stx-team-host').shadowRoot.querySelector('h1').textContent);
    check(p + ': titel in de juiste taal', re.test(h1), h1);
    await ctx.close();
  }
  for (const [p, re, lst] of [['/fr/mbp', /Devenez Master Balloon Professional/, '/fr/mbp-listing'], ['/de/mbp', /Werde Master Balloon Professional/, '/de/mbp-listing']]) {
    const { ctx, pg } = await open(p);
    const r = await pg.evaluate(() => { const sr = document.querySelector('#stx-mbp-host').shadowRoot; return [sr.querySelector('h1').textContent, sr.querySelector('a[href$="/mbp-listing"]').getAttribute('href')]; });
    check(p + ': titel in de juiste taal', re.test(r[0].replace(/\s+/g, ' ')), r[0]);
    check(p + ': listing-knop met taalprefix', r[1] === lst, r[1]);
    if (p === '/de/mbp') { await pg.screenshot({ path: path.join(shots, 'mbp-de.png'), fullPage: true }); }
    await ctx.close();
  }

  console.log('\n/mbp (desktop)');
  {
    const { ctx, pg } = await open('/mbp');
    await pg.evaluate(async () => {
      const sr = document.querySelector('#stx-mbp-host').shadowRoot;
      await Promise.all(Array.from(sr.querySelectorAll('img')).map((i) => i.complete ? 0 : new Promise((r) => { i.onload = i.onerror = r; })));
    });
    const r = await pg.evaluate(() => {
      const sr = document.querySelector('#stx-mbp-host').shadowRoot;
      const imgs = Array.from(sr.querySelectorAll('img'));
      return {
        imgs: imgs.length, loaded: imgs.filter((i) => i.naturalWidth > 0).length,
        src0: imgs[0] && imgs[0].src,
        h1: sr.querySelector('h1').textContent,
        events: sr.querySelector('.hero-grid .btn').getAttribute('href'),
        p2hidden: sr.getElementById('p2').hidden,
      };
    });
    check('6 beelden geladen uit assets/mbp', r.imgs === 6 && r.loaded === 6, r.loaded + '/' + r.imgs + ' ' + r.src0);
    check('beelden via de loader-commit', /\/assets\/mbp\/mbp-01-/.test(r.src0), r.src0);
    check('titel in het Nederlands op /mbp', /Word een Master Balloon Professional/.test(r.h1.replace(/\s+/g, ' ')), r.h1);
    check('examendata-knop naar /events', r.events === '/events', r.events);
    const listing = await pg.evaluate(() => Array.from(document.querySelector('#stx-mbp-host').shadowRoot.querySelectorAll('a[href$="/mbp-listing"]')).map((a) => a.getAttribute('href') + ' ' + a.textContent.trim()));
    check('twee knoppen naar /mbp-listing (hero + afsluiter)', listing.length === 2 && listing.every((l) => l.startsWith('/mbp-listing ')), listing.join(' | '));
    check('deel 2 eerst verborgen', r.p2hidden === true);
    await pg.evaluate(() => document.querySelector('#stx-mbp-host').shadowRoot.getElementById('tab2').click());
    const after = await pg.evaluate(() => { const sr = document.querySelector('#stx-mbp-host').shadowRoot; return [sr.getElementById('p1').hidden, sr.getElementById('p2').hidden, sr.getElementById('tab2').getAttribute('aria-selected')]; });
    check('tab deel 2 werkt', after.join() === 'true,false,true', after.join());
    check('geen horizontale scroll', await noHScroll(pg));
    await pg.screenshot({ path: path.join(shots, 'mbp-desktop.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\n/en_GB/mbp (mobiel)');
  {
    const { ctx, pg } = await open('/en_GB/mbp', 390, 844);
    const ev = await pg.evaluate(() => document.querySelector('#stx-mbp-host').shadowRoot.querySelector('.hero-grid .btn').getAttribute('href'));
    check('examendata-knop krijgt /en_GB', ev === '/en_GB/events', ev);
    check('geen horizontale scroll op mobiel', await noHScroll(pg));
    await pg.screenshot({ path: path.join(shots, 'mbp-mobile.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\nFooter + menu');
  for (const [p, lang, cat, nl] of [['/team', 'nl', '/shop/category/nieuw-2910', '/nl/team'], ['/fr/events', 'fr', '/fr/shop/category/nouveaute-2910', '/nl/events'], ['/de', 'de', '/de/shop/category/neu-2910', '/nl'], ['/en_GB/shop', 'en', '/en_GB/shop/category/new-2910', '/nl/shop']]) {
    const { ctx, pg } = await open(p);
    const r = await pg.evaluate(() => {
      const host = document.querySelector('footer#bottom > .stx-ft-host');
      const sr = host && host.shadowRoot;
      const old = document.querySelector('footer#bottom > #footer');
      const lis = Array.from(document.querySelectorAll('header#top nav.d-lg-block ul.top_menu > li')).map((l) => l.textContent.trim());
      return {
        host: !!sr,
        oldHidden: old && getComputedStyle(old).display === 'none',
        copyHidden: getComputedStyle(document.querySelector('.o_footer_copyright')).display === 'none',
        lang: sr && sr.querySelector('.stx-footer').getAttribute('lang'),
        active: sr && sr.querySelector('.stx-lang a.is-active').textContent,
        nl: sr && sr.querySelector('.stx-lang a[hreflang="nl"]').getAttribute('href'),
        cat: sr && sr.querySelectorAll('.stx-col-nav')[0].querySelectorAll('a')[1].getAttribute('href'),
        h3: sr && getComputedStyle(sr.querySelector('h3')).color,
        menu: lis,
        mbp: (document.querySelector('li.stx-mbp-item a') || {}).getAttribute ? document.querySelector('li.stx-mbp-item a').getAttribute('href') : null,
      };
    });
    check(p + ': nieuwe footer staat erin, oude weg', r.host && r.oldHidden && r.copyHidden);
    check(p + ': footer in het ' + lang, r.lang === lang && r.active === lang.toUpperCase(), r.lang + '/' + r.active);
    check(p + ': categorie in de juiste taal', r.cat === cat, r.cat);
    check(p + ': NL-knop via /nl', r.nl === nl, r.nl);
    check(p + ': footer-titels geel, niet Odoo-rood', r.h3 === 'rgb(255, 219, 90)', r.h3);
    const logo = await pg.evaluate(() => new Promise((res) => {
      const img = document.querySelector('footer#bottom > .stx-ft-host').shadowRoot.querySelector('.stx-logo');
      const done = () => res(img.naturalWidth);
      if (img.complete) { done(); } else { img.addEventListener('load', done); img.addEventListener('error', done); }
    }));
    check(p + ': logo laadt in de footer', logo === 640, logo);
    check(p + ': menu eindigt op Blog, MBP', r.menu.slice(-2).join() === 'Blog,MBP', r.menu.join(' | '));
    const pre = lang === 'nl' ? '' : lang === 'en' ? '/en_GB' : '/' + lang;
    check(p + ': MBP-knop naar ' + pre + '/mbp', r.mbp === pre + '/mbp', r.mbp);
    if (lang === 'fr') {
      await pg.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
      await pg.screenshot({ path: path.join(shots, 'footer-fr.png') });
      await pg.evaluate(() => window.scrollTo(0, 0));
      await pg.screenshot({ path: path.join(shots, 'menu-blog-mbp.png'), clip: { x: 0, y: 0, width: 1400, height: 80 } });
    }
    await ctx.close();
  }

  console.log('\nFooter mobiel');
  {
    const { ctx, pg } = await open('/shop', 390, 844);
    check('geen horizontale scroll op mobiel', await noHScroll(pg));
    await pg.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await pg.locator('footer#bottom').screenshot({ path: path.join(shots, 'footer-mobile.png') });
    await ctx.close();
  }

  console.log('\nAnti-flits: footer laadt niet');
  {
    const ctx = await browser.newContext({ viewport: { width: 1200, height: 800 } });
    const pg = await ctx.newPage();
    await pg.goto(base + '/shop?nofooter=1', { waitUntil: 'domcontentloaded' });
    const early = await pg.evaluate(() => getComputedStyle(document.querySelector('footer#bottom > #footer')).visibility);
    check('oude footer meteen verborgen', early === 'hidden', early);
    await pg.waitForTimeout(6500);
    const late = await pg.evaluate(() => getComputedStyle(document.querySelector('footer#bottom > #footer')).visibility);
    check('na 6 s komt de oude footer terug als de nieuwe niet laadt', late === 'visible', late);
    await ctx.close();
  }

  await browser.close();
  server.close();
  console.log(failures ? `\n${failures} FOUT(EN)` : '\nAlles ok');
  process.exit(failures ? 1 : 0);
})();
