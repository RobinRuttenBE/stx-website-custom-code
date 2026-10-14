// Local harness for sections/design-sheet-v1.html + sections/design-sheet/app-v10.html.
// A fake shop on localhost: the section loads the app in its srcdoc iframe like on Odoo.
// Shop search and product photos are passed through to the live shop (public, no prices),
// so foil names and template ids are real. Cart, session, Odoo models and the AI server are fakes.
// Run: node tests/design-sheet/test.js
const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const assert = require('assert');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const REPO = path.resolve(__dirname, '../..');
const OUT = __dirname;
const LIVE = 'www.sempertexeurope.com';

const cartAdds = [];
const odooCalls = [];
const designs = {};           // id -> record (fake x_stx_design)
let nextId = 1;
let aiRequests = 0;
let loggedIn = true;

function readBody(req) { return new Promise(r => { let b = ''; req.on('data', c => b += c); req.on('end', () => r(b)); }); }
function json(res, obj, status) { res.writeHead(status || 200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify(obj)); }
function rpcOk(res, result) { json(res, { jsonrpc: '2.0', id: 1, result: result }); }
function rpcErr(res, msg) { json(res, { jsonrpc: '2.0', id: 1, error: { message: 'Odoo Server Error', data: { message: msg } } }); }
function passLive(req, res, body) {
  const up = https.request({ host: LIVE, path: req.url, method: req.method, headers: { 'Content-Type': req.headers['content-type'] || 'application/json', 'User-Agent': 'stx-harness' } }, ur => {
    res.writeHead(ur.statusCode, { 'Content-Type': ur.headers['content-type'] || 'application/octet-stream' }); ur.pipe(res);
  });
  up.on('error', () => { res.writeHead(502); res.end(); });
  if (body) up.write(body);
  up.end();
}
function injectPage(title, sectionPath, extra) {
  return `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${title}</title></head><body><div id="wrapwrap"><header>Odoo header</header><div id="wrap"></div></div>
<script>window.STX_SECTIONS_BASE = '/sections/';${extra || ''}
(function(){ function inject(t){ var tpl=document.createElement('template'); tpl.innerHTML=t; var sc=Array.prototype.slice.call(tpl.content.querySelectorAll('script')); sc.forEach(function(s){ s.parentNode.removeChild(s); }); document.body.appendChild(tpl.content); sc.forEach(function(o){ var s=document.createElement('script'); if (o.src) { s.src=o.src; } else { s.text=o.text; } document.body.appendChild(s); }); }
fetch('${sectionPath}').then(function(r){return r.text()}).then(inject); })();
</script></body></html>`;
}

const server = http.createServer(async (req, res) => {
  const url = req.url.split('?')[0];
  const body = req.method === 'POST' ? await readBody(req) : '';
  if (url === '/design-sheet' || url === '/fr/design-sheet') { res.writeHead(200, { 'Content-Type': 'text/html' }); res.end(injectPage('Design sheet', '/sections/design-sheet-v1.html')); return; }
  if (url === '/tools') { res.writeHead(200, { 'Content-Type': 'text/html' }); res.end(injectPage('Tools', '/sections/inspiration-v18.html')); return; }
  if (url === '/shop/cart' || url === '/shop') { res.writeHead(200, { 'Content-Type': 'text/html' }); res.end('<!doctype html><title>Cart</title><h1>Cart</h1>'); return; }
  if (url === '/sections/design-sheet-v1.html') {
    let s = fs.readFileSync(path.join(REPO, 'sections/design-sheet-v1.html'), 'utf8');
    s = s.replace("var AI_ENDPOINT = '';", "var AI_ENDPOINT = '/fake-ai';");
    res.writeHead(200, { 'Content-Type': 'text/html' }); res.end(s); return;
  }
  if (url.indexOf('/sections/') === 0) { const f = path.join(REPO, decodeURIComponent(url)); if (fs.existsSync(f)) { res.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : 'text/html' }); fs.createReadStream(f).pipe(res); return; } }
  if (url === '/en_GB/website/snippet/autocomplete') { passLive(req, res, body); return; }
  if (url.indexOf('/web/image/') === 0) { passLive(req, res); return; }
  if (url === '/website_sale/get_combination_info') { const p = JSON.parse(body).params; rpcOk(res, { product_id: p.product_template_id * 10, price: 0 }); return; }
  if (url === '/shop/cart/add') { const p = JSON.parse(body).params; cartAdds.push(p); rpcOk(res, { cart_quantity: cartAdds.length }); return; }
  if (url === '/web/session/get_session_info') { if (loggedIn) rpcOk(res, { uid: 5, name: 'Tester' }); else rpcErr(res, 'Session expired'); return; }
  if (url.indexOf('/web/dataset/call_kw/') === 0) {
    const p = JSON.parse(body).params; odooCalls.push(p.model + '.' + p.method);
    if (p.model === 'x_stx_design') {
      if (p.method === 'search_read') { rpcOk(res, Object.values(designs).map(d => ({ id: d.id, x_pid: d.x_pid, x_name: d.x_name, x_thumb: d.x_thumb, write_date: d.write_date }))); return; }
      if (p.method === 'create') { const v = p.args[0][0]; const id = nextId++; designs[id] = Object.assign({ id: id, write_date: '2026-10-14 10:00:00' }, v); rpcOk(res, [id]); return; }
      if (p.method === 'write') { const id = p.args[0][0]; Object.assign(designs[id], p.args[1]); rpcOk(res, true); return; }
      if (p.method === 'read') { rpcOk(res, p.args[0].map(i => ({ id: i, x_data: designs[i].x_data }))); return; }
      if (p.method === 'unlink') { p.args[0].forEach(i => delete designs[i]); rpcOk(res, true); return; }
    }
    if (p.model === 'x_stx_ai_request' && p.method === 'create') { rpcOk(res, [900 + (++aiRequests)]); return; }
    rpcErr(res, 'Object ' + p.model + " doesn't exist"); return;
  }
  if (url === '/fake-ai') {
    const b = JSON.parse(body);
    assert.ok(b.request_id > 900 && b.image.indexOf('data:image/jpeg') === 0 && b.prompt.length > 50);
    json(res, { image: b.image, used: 1, limit: 40 }); return;
  }
  res.writeHead(404); res.end('nf ' + url);
});

(async function main() {
  await new Promise(r => server.listen(0, r));
  const base = 'http://localhost:' + server.address().port;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|404|Failed to load resource/.test(m.text())) errors.push(m.text()); });
  const ok = (msg) => console.log('ok  ' + msg);

  // 1. without the beta switch: the coming soon card, no tool
  await page.goto(base + '/design-sheet');
  await page.waitForSelector('#stx-ds-soon');
  assert.strictEqual(await page.$('#stx-ds-frame'), null);
  ok('without #stxdesign the page shows the coming-soon card');

  // 2. with the switch: the tool in its iframe
  await page.goto(base + '/design-sheet#stxdesign');
  await page.waitForSelector('#stx-ds-frame');
  const frame = () => page.frames().find(f => f.url() === 'about:srcdoc');
  await page.waitForFunction(() => { const f = document.getElementById('stx-ds-frame'); return f && f.contentWindow && f.contentWindow.STX; }, null, { timeout: 30000 });
  let f = frame();
  assert.ok(await f.evaluate(() => !!window.STX_ENV && window.STX_ENV.shop === true));
  await page.waitForFunction(() => !document.getElementById('stx-ds-wait'));
  ok('#stxdesign loads the tool full screen, STX_ENV says shop');

  // 3. number stack: every digit becomes the real Grabo product
  await f.click('.gen-tabs button[data-gen="number"]');
  await f.fill('#num-text', '25');
  await f.selectOption('#num-foil', '40');
  await f.click('#num-build');
  await f.waitForFunction(() => window.STX.state.foils.length >= 2 && window.STX.state.foils.every(x => x.tid), null, { timeout: 30000 });
  const foils = await f.evaluate(() => window.STX.state.foils.map(x => x.pname));
  assert.deepStrictEqual(foils, ['Number 2 - Gold - 40 inch - Grabo', 'Number 5 - Gold - 40 inch - Grabo']);
  await page.waitForTimeout(1500);
  ok('number 25 in gold 40" = ' + foils.join(' + '));

  // 4. foil browser: live shop search, tap to add
  await f.click('.gen-tabs button[data-gen="foil"]');
  await f.fill('#foil-q', 'Star Gold 18 inch');
  await f.waitForSelector('#foil-grid .fg', { timeout: 30000 });
  const firstName = await f.$eval('#foil-grid .fg', el => el.title);
  await f.click('#foil-grid .fg');
  await f.waitForFunction(() => window.STX.state.foils.some(x => x.prod), null, { timeout: 10000 });
  ok('foil browser added "' + firstName + '"');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(OUT, 'foils-desktop.png') });

  // 5. column + bouquet, then the cart with suggestions
  await f.click('.gen-tabs button[data-gen="column"]');
  await f.click('#col-build');
  await f.click('.gen-tabs button[data-gen="bouquet"]');
  await f.click('#bq-build');
  await f.waitForFunction(() => window.STX.state.foils.filter(x => x.ribbon).every(x => x.tid), null, { timeout: 30000 });
  await f.click('.tabs button[data-pane="order"]');
  await f.click('#order-cart');
  await f.waitForSelector('#ck-add');
  await f.waitForFunction(() => document.querySelectorAll('.sug .pr, .sug img').length > 0);
  await page.waitForTimeout(2500); // live check of the suggestion names
  let sugs = await f.$$eval('.sug [data-s]', els => els.map(e => e.dataset.s + (e.checked ? '+' : '-')));
  assert.ok(sugs.indexOf('col-stand+') >= 0 && sugs.indexOf('ribbon+') >= 0 && sugs.indexOf('weights+') >= 0, sugs.join(','));
  assert.ok(sugs.every(s => s.indexOf('water') < 0));
  await page.screenshot({ path: path.join(OUT, 'cart-suggestions-indoor.png') });
  await f.check('#ck-out');
  await page.waitForTimeout(300);
  sugs = await f.$$eval('.sug [data-s]', els => els.map(e => e.dataset.s + (e.checked ? '+' : '-')));
  assert.ok(sugs.indexOf('water-base+') >= 0 && sugs.indexOf('water-bag+') >= 0 && sugs.indexOf('weights-big+') >= 0 && sugs.indexOf('col-stand-') >= 0, sugs.join(','));
  await page.screenshot({ path: path.join(OUT, 'cart-suggestions-outdoor.png') });
  ok('suggestions indoor: ' + sugs.length + ' rows; outdoor adds water bases, water bags, big weights');
  const nav = page.waitForURL(/\/shop\/cart$/, { timeout: 60000 });
  await f.click('#ck-add');
  await nav;
  const tids = cartAdds.map(a => a.product_template_id);
  assert.ok(cartAdds.length >= 8, 'cart lines ' + cartAdds.length);
  assert.ok(tids.indexOf(2942) >= 0 && tids.indexOf(2935) >= 0, 'water base + bag in cart');
  assert.ok(cartAdds.every(a => a.product_id === a.product_template_id * 10 && a.quantity > 0));
  ok('cart: ' + cartAdds.length + ' lines added (balloons, foils, water base, water bag, ...), then /shop/cart');

  // 6. account storage: the project was written to the fake x_stx_design
  const rec = Object.values(designs)[0];
  assert.ok(rec && rec.x_pid && JSON.parse(rec.x_data).foils.length >= 3, 'design saved to account');
  assert.ok(rec.x_thumb.indexOf('data:image/jpeg') === 0);
  ok('project saved on the account (x_stx_design), ' + Math.round(rec.x_data.length / 1024) + ' KB');

  // another device: empty localStorage, the project comes from the account
  const ctx2 = await browser.newContext({ viewport: { width: 1280, height: 860 } });
  const p2 = await ctx2.newPage();
  p2.on('pageerror', e => errors.push('device2: ' + e.message));
  await p2.goto(base + '/design-sheet#stxdesign');
  await p2.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX; }, null, { timeout: 30000 });
  const f2 = p2.frames().find(x => x.url() === 'about:srcdoc');
  await f2.click('#tab-projects');
  await f2.waitForSelector('[data-cload]', { timeout: 10000 });
  await f2.click('[data-cload]');
  await f2.waitForFunction(() => window.STX.state.balloons.length > 50 && window.STX.state.foils.length >= 3, null, { timeout: 15000 });
  ok('second device: project listed "on your account" and opened from Odoo');

  // 7. quote: hand-off to the cost calculator
  const nav2 = p2.waitForURL(/\/tools#cost$/, { timeout: 30000 });
  await f2.click('.tabs button[data-pane="order"]');
  await f2.click('#order-quote');
  await nav2;
  await p2.waitForSelector('#cc-mat-rows .cc-mat input[data-f=name]', { timeout: 30000 });
  const mat = await p2.$$eval('#cc-mat-rows input[data-f=name]', els => els.map(e => e.value));
  assert.ok(mat.length >= 5 && mat.some(n => /Number 2 - Gold - 40 inch/.test(n)), mat.join(' | '));
  assert.strictEqual(await p2.evaluate(() => localStorage.getItem('stx_quote_import')), null);
  await p2.screenshot({ path: path.join(OUT, 'quote-in-cost-calculator.png'), fullPage: false });
  ok('Make a quote: ' + mat.length + ' material lines in the Cost Calculator, import key cleared');

  // 8. AI: Odoo request record first, then the AI server
  await page.goto(base + '/design-sheet#stxdesign');
  await page.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX && fr.contentWindow.STX.state.balloons.length; }, null, { timeout: 30000 });
  f = page.frames().find(x => x.url() === 'about:srcdoc');
  await f.click('#btn-ai');
  await f.waitForSelector('#ai-gen');
  await f.click('#ai-gen');
  await f.waitForFunction(() => window.STX.state.impression && window.STX.state.impression.img, null, { timeout: 20000 });
  assert.strictEqual(aiRequests, 1);
  ok('AI impression: request logged in Odoo, image back from the AI server, compare view on');

  // 9. not logged in: device storage only, clear message
  loggedIn = false;
  await page.goto(base + '/design-sheet?reload=1#stxdesign');
  await page.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX; }, null, { timeout: 30000 });
  f = page.frames().find(x => x.url() === 'about:srcdoc');
  await page.waitForTimeout(1500);
  const modalTxt = await f.evaluate(() => document.getElementById('modal').classList.contains('show') ? document.getElementById('modal-box').innerText.slice(0, 300) : '');
  assert.strictEqual(modalTxt, '', 'modal open on load: ' + modalTxt);
  await f.click('#tab-projects');
  await f.waitForFunction(() => /Log in on the shop/.test(document.getElementById('cloud-status').textContent));
  ok('logged out: "Saved on this device. Log in on the shop to keep your projects on your account"');
  loggedIn = true;

  // 10. phone
  const ph = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  ph.on('pageerror', e => errors.push('phone: ' + e.message));
  await ph.goto(base + '/design-sheet#stxdesign');
  await ph.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX; }, null, { timeout: 30000 });
  await ph.waitForTimeout(2000);
  await ph.screenshot({ path: path.join(OUT, 'phone.png') });
  ok('phone layout renders');

  assert.deepStrictEqual(errors, [], 'page errors: ' + errors.join(' / '));
  ok('no page errors');
  await browser.close(); server.close();
  console.log('ALL PASSED');
})().catch(async e => { console.error('FAIL', e); process.exit(1); });
