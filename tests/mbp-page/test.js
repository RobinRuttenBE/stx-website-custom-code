// Check for the two public MBP pages:
//   sections/mbp-v1.html          -> /mbp, the explanation
//   sections/mbp-listing-v1.html  -> /mbp-listing, the directory
//
// Serves a rebuilt Odoo page and injects the section the way the loader does,
// on both paths and on the language versions. No connection to the live site.
//
//   node test.js
//
// Playwright comes from stx-tools/node_modules (or set STX_PLAYWRIGHT).

const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const SECTIONS = {
  '/mbp': fs.readFileSync(path.resolve(__dirname, '../../sections/mbp-v1.html'), 'utf8'),
  '/mbp-listing': fs.readFileSync(path.resolve(__dirname, '../../sections/mbp-listing-v1.html'), 'utf8'),
};

// Welke sectie de loader op welk pad zou laden: endsWith, net als de echte loader.
function sectionFor(urlPath) {
  const p = urlPath.replace(/\/+$/, '').toLowerCase();
  if (p.endsWith('/mbp-listing')) return SECTIONS['/mbp-listing'];
  if (p.endsWith('/mbp')) return SECTIONS['/mbp'];
  return '';
}

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
fetch('/section.html?p=' + encodeURIComponent(location.pathname))
  .then(function (r) { return r.text(); })
  .then(function (html) {
    if (!html) { window.__injected = true; return; }
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
      const [url, qs] = req.url.split('?');
      if (url === '/section.html') {
        const params = new URLSearchParams(qs || '');
        rsp.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
        rsp.end(sectionFor(params.get('p') || '/'));
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
    // Alleen onze server, de Google fonts en de Sempertex CDN (de profielfoto's).
    await pg.route('**', (r) => {
      const u = r.request().url();
      if (u.startsWith(base)) return r.continue();
      if (/fonts\.(googleapis|gstatic)|sempertex\.com\/cdn/.test(u)) return r.continue();
      return r.abort();
    });
    await pg.goto(base + p, { waitUntil: 'domcontentloaded' });
    await pg.waitForTimeout(800);
    return { ctx, pg };
  }

  console.log('\n/mbp: de uitleg (Nederlands)');
  {
    const { ctx, pg } = await open('/mbp');

    check('sectie staat er en is zichtbaar', await pg.evaluate(() => {
      const n = document.querySelector('#stx-mbp-root');
      return !!n && getComputedStyle(n).display !== 'none';
    }));
    check('sectie zit in #wrap', await pg.evaluate(() => !!document.querySelector('#wrap #stx-mbp-root')));

    const h1 = await pg.textContent('#stx-mbp-root h1');
    check('titel staat in het Nederlands', /Word/.test(h1) && /Master Balloon Professional/.test(h1), h1);

    const crit = await pg.$$eval('#mbp-p1 li, #mbp-p2 li', (e) => e.length);
    const pts = await pg.$$eval('#mbp-p1 b, #mbp-p2 b', (e) =>
      e.reduce((a, x) => a + parseInt(x.textContent, 10), 0));
    check('acht criteria, samen 100 punten', crit === 8 && pts === 100, crit + ' criteria, ' + pts + ' punten');

    check('de lijst staat hier NIET meer', (await pg.$('#mbpl-eu-grid')) === null);
    check('wel een doorverwijzing naar de lijst', (await pg.$('#mbp-listing-link')) !== null);
    const link = await pg.getAttribute('#mbp-listing-link', 'href');
    check('die wijst naar /mbp-listing', link === '/mbp-listing', link);

    const counts = await pg.evaluate(() => [
      document.getElementById('mbp-count-total').textContent,
      document.getElementById('mbp-count-eu').textContent,
      document.getElementById('mbp-count-eu2').textContent,
    ]);
    check('aantallen kloppen op beide plekken', counts.join(',') === '266,63,63', counts.join(','));

    const book = await pg.getAttribute('#mbp-book', 'href');
    check('examenknop gaat naar de eventpagina', book === '/events', book);

    const hero = await pg.getAttribute('#mbp-cta-dir', 'href');
    check('de knop in de hero gaat ook naar /mbp-listing', hero === '/mbp-listing', hero);

    await pg.screenshot({ path: path.resolve(__dirname, 'mbp-nl.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\n/mbp-listing: de lijst (Nederlands)');
  {
    const { ctx, pg } = await open('/mbp-listing');

    check('sectie staat er en is zichtbaar', await pg.evaluate(() => {
      const n = document.querySelector('#stx-mbpl-root');
      return !!n && getComputedStyle(n).display !== 'none';
    }));

    const h1 = await pg.textContent('#stx-mbpl-root h1');
    check('titel staat in het Nederlands', /MBP-lijst/.test(h1), h1);

    const euCards = await pg.$$eval('#mbpl-eu-grid .p', (e) => e.length);
    check('alle 63 Europese MBPs staan er', euCards === 63, String(euCards));

    const photos = await pg.$$eval('#mbpl-eu-grid .pic img', (e) => e.length);
    check('elke Europese MBP heeft een profielfoto', photos === 63, String(photos));

    const loaded = await pg.$$eval('#mbpl-eu-grid .pic img', (e) => e.filter((x) => x.naturalWidth > 0).length);
    check('die fotos laden ook echt van de CDN', loaded >= 55, loaded + ' van ' + photos);

    const euChips = await pg.$$eval('#mbpl-eu-filters button', (e) => e.length);
    check('landenfilter voor Europa', euChips === 14, euChips + ' knoppen');

    await pg.click('#mbpl-eu-filters [data-c="Italy"]');
    await pg.waitForTimeout(200);
    check('filteren op land werkt', (await pg.$$eval('#mbpl-eu-grid .p', (e) => e.length)) === 27);

    await pg.click('#mbpl-eu-filters [data-c="__all__"]');
    await pg.fill('#mbpl-search', 'audrey');
    await pg.waitForTimeout(200);
    const found = await pg.$$eval('#mbpl-eu-grid .p', (e) => e.map((x) => x.textContent));
    check('zoeken op naam werkt', found.length === 1 && /Audrey Parsons/.test(found[0]), JSON.stringify(found));
    await pg.fill('#mbpl-search', '');
    await pg.waitForTimeout(200);

    const restShown = await pg.$$eval('#mbpl-rest-grid .p', (e) => e.length);
    await pg.click('#mbpl-rest-toggle');
    await pg.waitForTimeout(250);
    const restAll = await pg.$$eval('#mbpl-rest-grid .p', (e) => e.length);
    check('rest van de wereld staat ingeklapt onder Europa', restShown === 16 && restAll === 203,
      restShown + ' -> ' + restAll);

    const order = await pg.evaluate(() => {
      const eu = document.querySelector('#mbpl-eu-grid').getBoundingClientRect().top;
      const rest = document.querySelector('#mbpl-rest-grid').getBoundingClientRect().top;
      return eu < rest && !!document.querySelector('#mbpl-search');
    });
    check('Europa staat boven de rest, met het zoekveld', order);

    // Profiel: socials en portfolio
    await pg.click('#mbpl-eu-grid .p:has-text("Mazzocca")');
    await pg.waitForTimeout(400);
    const sheet = await pg.evaluate(() => {
      const n = document.querySelector('.stx-mbpl-sheet .in');
      if (!n) return null;
      return {
        name: n.querySelector('h3').textContent.trim(),
        socials: [...n.querySelectorAll('.soc a')].map((a) => a.getAttribute('href')),
        gallery: n.querySelectorAll('.track figure').length,
        photo: !!n.querySelector('.big img'),
      };
    });
    check('profiel toont naam, kanalen en portfolio',
      sheet && /Mazzocca/.test(sheet.name) && sheet.socials.length >= 1 && sheet.gallery === 2 && sheet.photo,
      JSON.stringify(sheet));
    check('de kanaallink gaat naar Instagram',
      sheet && /instagram\.com\/balloonmagico/.test(sheet.socials[0] || ''), (sheet || {}).socials);

    await pg.screenshot({ path: path.resolve(__dirname, 'mbp-profile.png') });
    await pg.keyboard.press('Escape');
    await pg.waitForTimeout(300);
    check('profiel sluit met Escape', (await pg.$('.stx-mbpl-sheet')) === null);

    // Iemand zonder portfolio krijgt een nette lege staat, geen kapotte carrousel.
    await pg.click('#mbpl-eu-grid .p:has-text("Bjorn de Weirdt")');
    await pg.waitForTimeout(350);
    const empty = await pg.evaluate(() => {
      const n = document.querySelector('.stx-mbpl-sheet .in');
      return n ? { none: !!n.querySelector('.none'), track: !!n.querySelector('.track'),
                   socials: n.querySelectorAll('.soc a').length } : null;
    });
    check('zonder portfolio: nette melding, geen lege carrousel',
      empty && empty.none && !empty.track && empty.socials === 3, JSON.stringify(empty));
    await pg.keyboard.press('Escape');

    const back = await pg.getAttribute('#mbpl-about', 'href');
    check('link terug naar de uitleg', back === '/mbp', back);

    await pg.screenshot({ path: path.resolve(__dirname, 'mbp-listing-nl.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\nTaalversies: elke zichtbare tekst in de juiste taal');
  // Woorden die verraden dat er een andere taal doorheen loopt. Dit is al
  // een keer misgegaan (Nederlands met Engelse stukken, Engels met Frans),
  // dus we kijken naar de hele pagina en niet alleen naar de titel.
  const TELLS = {
    en: [/\bYour\b/, /\bthe\b/, /\bwith\b/, /\bEvery\b/, /\bOpen the\b/, /\bworldwide\b/, /\bin Europe\b/],
    nl: [/\bje\b/, /\bhet\b/, /\bvan\b/, /\bwat\b/, /\bOpen de\b/, /\bwereldwijd\b/, /\bin Europa\b/],
    de: [/\bdie\b/, /\bdein/, /\bund\b/, /\bWas\b/, /\bVerzeichnis\b/, /\bweltweit\b/],
    fr: [/\bvotre\b/, /\bvous\b/, /\bpour\b/, /\bannuaire\b/, /\bdans le monde\b/, /\ben Europe\b/],
  };

  for (const [p, sel, lang, needle] of [
    ['/mbp', '#stx-mbp-root', 'nl', 'Word'],
    ['/en_GB/mbp', '#stx-mbp-root', 'en', 'Become a'],
    ['/fr/mbp', '#stx-mbp-root', 'fr', 'Devenez'],
    ['/de/mbp', '#stx-mbp-root', 'de', 'Werde'],
    ['/mbp-listing', '#stx-mbpl-root', 'nl', 'MBP-lijst'],
    ['/en_GB/mbp-listing', '#stx-mbpl-root', 'en', 'directory'],
    ['/fr/mbp-listing', '#stx-mbpl-root', 'fr', 'annuaire'],
    ['/de/mbp-listing', '#stx-mbpl-root', 'de', 'Verzeichnis'],
  ]) {
    const { ctx, pg } = await open(p);
    const h1 = await pg.textContent(sel + ' h1');
    check(p + ': titel klopt', h1.indexOf(needle) > -1, h1);

    // De hele zichtbare tekst van de sectie, zonder de namen en landen uit
    // het register: die zijn in elke taal hetzelfde.
    const text = await pg.evaluate((q) => {
      const clone = document.querySelector(q).cloneNode(true);
      clone.querySelectorAll('.people, .filters, .count').forEach((n) => n.remove());
      return clone.textContent.replace(/\s+/g, ' ');
    }, sel);

    const own = TELLS[lang].filter((r) => r.test(text)).length;
    const strays = [];
    for (const other of ['en', 'nl', 'de', 'fr']) {
      if (other === lang) continue;
      const hits = TELLS[other].filter((r) => r.test(text));
      // Duits en Nederlands lijken op elkaar, dus pas alarm als de andere
      // taal het duidelijk wint.
      if (hits.length >= 3 && hits.length > own) {
        strays.push(other + ' scoort ' + hits.length + ' tegen ' + own);
      }
    }
    check(p + ': geen tekst uit een andere taal', strays.length === 0, strays.join(' | '));
    await ctx.close();
  }

  console.log('\nTaalprefix blijft staan zoals Odoo hem schrijft');
  {
    const { ctx, pg } = await open('/en_GB/mbp-listing');
    const about = await pg.getAttribute('#mbpl-about', 'href');
    const book = await pg.getAttribute('#mbpl-book', 'href');
    check('links op de lijst houden /en_GB', about === '/en_GB/mbp' && book === '/en_GB/events', about + ' | ' + book);
    await ctx.close();
  }
  {
    const { ctx, pg } = await open('/en_GB/mbp');
    const hero = await pg.getAttribute('#mbp-cta-dir', 'href');
    const foot = await pg.getAttribute('#mbp-listing-link', 'href');
    check('beide knoppen naar de lijst houden /en_GB',
      hero === '/en_GB/mbp-listing' && foot === '/en_GB/mbp-listing', hero + ' | ' + foot);
    await ctx.close();
  }

  console.log('\nBuiten de eigen paden');
  for (const [p, sel] of [['/shop', '#stx-mbp-root'], ['/shop', '#stx-mbpl-root']]) {
    const { ctx, pg } = await open(p);
    check('sectie ' + sel + ' staat niet op ' + p, (await pg.$(sel)) === null);
    await ctx.close();
  }
  {
    // /mbp-listing eindigt niet op /mbp, dus de uitlegpagina mag daar niet opduiken.
    const { ctx, pg } = await open('/mbp-listing');
    check('de uitlegsectie duikt niet op in de lijst', (await pg.$('#stx-mbp-root')) === null);
    await ctx.close();
  }

  console.log('\nTelefoonformaat');
  for (const p of ['/mbp', '/mbp-listing']) {
    const { ctx, pg } = await open(p, 390);
    const scroll = await pg.evaluate(() =>
      document.documentElement.scrollWidth - document.documentElement.clientWidth);
    check('geen horizontale scroll op ' + p, scroll <= 2, scroll + 'px');
    await pg.screenshot({ path: path.resolve(__dirname, 'mbp-mobile' + p.replace(/\//g, '-') + '.png'), fullPage: true });
    await ctx.close();
  }

  console.log('\nAlles in Rethink Sans');
  for (const p of ['/mbp', '/mbp-listing']) {
    const { ctx, pg } = await open(p);
    const bad = await pg.evaluate(() => {
      const root = document.querySelector('#stx-mbp-root, #stx-mbpl-root');
      const out = new Set();
      root.querySelectorAll('*').forEach((n) => {
        if (!n.textContent.trim() || n.children.length) return;
        const f = getComputedStyle(n).fontFamily;
        if (!/Rethink Sans/.test(f)) out.add(n.tagName + ': ' + f);
      });
      return [...out];
    });
    check('geen ander font op ' + p, bad.length === 0, bad.slice(0, 3).join(' | '));
    await ctx.close();
  }

  await browser.close();
  server.close();
  console.log(failures === 0 ? '\nAlles in orde.\n' : `\n${failures} controle(s) mislukt.\n`);
  process.exit(failures === 0 ? 0 : 1);
})();
