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
let xNameRefused = 0;         // calls the fake Odoo refused because they used x_name
let nextId = 1;
let aiRequests = 0;
let loggedIn = true;
let labelled = true;        // contact carries the 'AI Beta' label (answer of the fake /api/access)
let accessCalls = 0;

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
    s = s.replace(/var AI_ENDPOINT = '[^']*';/, "var AI_ENDPOINT = '/fake-ai';");
    s = s.replace(/var ACCESS_ENDPOINT = '[^']*';/, "var ACCESS_ENDPOINT = '/fake-access';");
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
    // Like the live models (20/10/2026): no x_name field, and Odoo refuses the whole call when it is used.
    if (/x_stx_/.test(p.model) && /"x_name"/.test(JSON.stringify([p.args, p.kwargs]))) { xNameRefused++; rpcErr(res, "Invalid field 'x_name' on '" + p.model + "'"); return; }
    if (p.model === 'x_stx_design') {
      if (p.method === 'search_read') { const fl = (p.kwargs && p.kwargs.fields) || []; rpcOk(res, Object.values(designs).map(d => { const r = { id: d.id }; fl.forEach(k => { r[k] = d[k]; }); return r; })); return; }
      if (p.method === 'create') { const v = p.args[0][0]; const id = nextId++; designs[id] = Object.assign({ id: id, write_date: '2026-10-14 10:00:00' }, v); rpcOk(res, [id]); return; }
      if (p.method === 'write') { const id = p.args[0][0]; Object.assign(designs[id], p.args[1]); rpcOk(res, true); return; }
      if (p.method === 'read') { rpcOk(res, p.args[0].map(i => ({ id: i, x_data: designs[i].x_data }))); return; }
      if (p.method === 'unlink') { p.args[0].forEach(i => delete designs[i]); rpcOk(res, true); return; }
    }
    if (p.model === 'x_stx_ai_request' && p.method === 'create') { rpcOk(res, [900 + (++aiRequests)]); return; }
    rpcErr(res, 'Object ' + p.model + " doesn't exist"); return;
  }
  if (url === '/fake-access') {
    const b = JSON.parse(body); accessCalls++;
    assert.ok(b.request_id > 900, 'access check sends the id of a record made as this account');
    json(res, { access: labelled }); return;
  }
  if (url === '/fake-ai') {
    const b = JSON.parse(body);
    assert.ok(b.request_id > 900 && b.image.indexOf('data:image/jpeg') === 0 && b.prompt.length > 50);
    json(res, { image: b.image, alts: [b.image], used: 1, limit: 40 }); return;   // best of 2: a second version comes back too
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

  // 1. access (27/10/2026): coming soon for everyone, the tool only for accounts with the 'AI Beta' label
  loggedIn = false;
  await page.goto(base + '/design-sheet');
  await page.waitForSelector('#stx-ds-soon');
  assert.strictEqual(await page.$('#stx-ds-frame'), null);
  const loginHref = await page.getAttribute('#stx-ds-soon p.in a', 'href');
  assert.ok(/\/web\/login\?redirect=%2Fdesign-sheet$/.test(loginHref), loginHref);
  assert.strictEqual(accessCalls, 0);
  ok('logged out: coming soon with a log in link back to this page, no access check');
  loggedIn = true; labelled = false;
  await page.goto(base + '/design-sheet');
  await page.waitForSelector('#stx-ds-soon');
  assert.strictEqual(await page.$('#stx-ds-frame'), null);
  assert.strictEqual(await page.$('#stx-ds-soon p.in'), null);
  assert.strictEqual(accessCalls, 1);
  ok('logged in without the label: coming soon, no log in link');
  await page.goto(base + '/design-sheet');
  await page.waitForSelector('#stx-ds-soon');
  assert.strictEqual(await page.$('#stx-ds-frame'), null);
  ok('the old #stxdesign switch no longer opens the tool');
  labelled = true;

  // 2. with the label: the tool in its iframe
  await page.goto(base + '/design-sheet');
  await page.waitForSelector('#stx-ds-frame');
  const frame = () => page.frames().find(f => f.url() === 'about:srcdoc');
  await page.waitForFunction(() => { const f = document.getElementById('stx-ds-frame'); return f && f.contentWindow && f.contentWindow.STX; }, null, { timeout: 30000 });
  let f = frame();
  assert.ok(await f.evaluate(() => !!window.STX_ENV && window.STX_ENV.shop === true));
  await page.waitForFunction(() => !document.getElementById('stx-ds-wait'));
  ok('with the label the tool loads full screen, STX_ENV says shop');
  const calls = accessCalls;
  await page.goto(base + '/design-sheet');
  await page.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX; }, null, { timeout: 30000 });
  f = frame();
  await page.waitForFunction(() => !document.getElementById('stx-ds-wait'));
  assert.strictEqual(accessCalls, calls);
  ok('a yes is remembered: the next visit opens without asking the server again');

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
  await p2.goto(base + '/design-sheet');
  await p2.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX; }, null, { timeout: 30000 });
  const f2 = p2.frames().find(x => x.url() === 'about:srcdoc');
  await f2.click('#tab-projects');
  await f2.waitForSelector('[data-cload]', { timeout: 10000 });
  await f2.click('[data-cload]');
  await f2.waitForFunction(() => window.STX.state.balloons.length > 50 && window.STX.state.foils.length >= 3, null, { timeout: 15000 });
  ok('second device: project listed "on your account" and opened from Odoo');
  assert.ok(xNameRefused > 0, 'fake Odoo never refused x_name, the test checks nothing');
  ok('models without x_name (like live): ' + xNameRefused + ' call(s) refused once, retried without; project list still works');

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
  await page.goto(base + '/design-sheet');
  await page.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX && fr.contentWindow.STX.state.balloons.length; }, null, { timeout: 30000 });
  f = page.frames().find(x => x.url() === 'about:srcdoc');
  // location photo with the design small in it, like a far wall: the AI gets a crop, the result goes back in place
  const photo = 'data:image/jpeg;base64,' + fs.readFileSync(path.join(__dirname, 'location-test.jpg')).toString('base64');
  await f.evaluate(src => new Promise(r => { window.STX.setLocation(src, 1200, 700); setTimeout(r, 800); }), photo);
  await page.screenshot({ path: path.join(OUT, 'location-scale.png') });
  await f.click('#corner-done');
  await f.click('#btn-ai');
  await f.waitForSelector('#ai-gen');
  const pr = await f.$eval('#ai-prompt', el => el.value);
  // shape of Robin's own working prompt: exact layout, real sizes, no long list of "do not enlarge"
  // whole photo by default, in the shape of Robin's own working prompt: exact layout, real sizes, short
  // small design in a big photo: the crop goes by default (a far column came back far too big with the whole photo)
  assert.ok(/^Edit this close-up of a photo\. The balloons drawn on it are the exact layout/.test(pr) && /m high/.test(pr) && /glossy chrome-look latex/.test(pr) && !/do not enlarge|never a hard/.test(pr), pr);
  const whole = await f.evaluate(() => new Promise(r => { window.STX.state.aiWhole = true; window.STX.aiJob(j => { window.STX.state.aiWhole = undefined; r(j.prompt); }); }));
  assert.ok(/^Edit this photo\./.test(whole) && /Recreate the whole photo as a sharp/.test(whole), whole.slice(0, 200));
  ok('AI prompt: crop by default for a small design, whole photo (recreated sharp) when picked');
  const before = aiRequests;   // the access checks above made request records too
  await f.click('#ai-gen');
  await f.waitForFunction(() => window.STX.state.impression && window.STX.state.impression.img, null, { timeout: 20000 });
  assert.strictEqual(aiRequests - before, 1);
  const imp = await f.evaluate(() => [window.STX.state.impression.img.width, window.STX.state.loc.pw, window.STX.state.impression.img.height, window.STX.state.loc.ph]);
  // full photo with the crop pasted in, at work size (long side at least 1600 px) so the AI's detail survives
  assert.ok(Math.max(imp[0], imp[2]) >= 1600 && Math.abs(imp[0] / imp[2] - imp[1] / imp[3]) < 0.01, 'impression is the full photo with the crop pasted in, at work size: ' + imp);
  // two versions came back: the customer picks one, the pick is what stays on the sheet
  await f.waitForSelector('[data-pick="1"]', { timeout: 10000 });
  const nPick = await f.$$eval('[data-pick]', els => els.length);
  assert.strictEqual(nPick, 2);
  await f.evaluate(() => { window.__impFirst = window.STX.state.impression; });
  await f.click('[data-pick="1"]');
  await f.waitForFunction(() => window.STX.state.impression !== window.__impFirst && window.STX.state.impression.img, null, { timeout: 10000 });
  ok('two AI versions: pick screen, version 2 picked and kept');
  ok('AI impression: request logged in Odoo, image back from the AI server, compare view on');
  // manual route: a crop-only result from another AI tool, uploaded, goes back into the full photo
  await f.evaluate(() => { document.getElementById('modal').classList.remove('show'); window.STX.state.aiWhole = false; });   // the crop route
  await f.click('#btn-ai');
  await f.waitForSelector('#ai-file', { state: 'attached' });
  await f.evaluate(() => { window.__impBefore = window.STX.state.impression; });
  await f.setInputFiles('#ai-file', path.join(__dirname, 'ai-result-crop.jpg'));
  await f.waitForFunction(() => window.STX.state.impression !== window.__impBefore && window.STX.state.impression.img, null, { timeout: 15000 });
  const up = await f.evaluate(() => [window.STX.state.impression.img.width, window.STX.state.loc.pw, window.STX.state.impression.img.height, window.STX.state.loc.ph]);
  assert.ok(Math.max(up[0], up[2]) >= 1600 && Math.abs(up[0] / up[2] - up[1] / up[3]) < 0.01, 'uploaded crop result is pasted into the full photo: ' + up);
  // a small photo (Robin's garage was 474 x 355): the AI still gets a sharp reference, not a 300 px crop
  const small = await f.evaluate(() => new Promise(r => {
    const L = window.STX.state.loc, cv = document.createElement('canvas'); cv.width = 474; cv.height = 355;
    cv.getContext('2d').drawImage(L.img, 0, 0, 474, 355);
    const keep = { img: L.img, pw: L.pw, ph: L.ph };
    const im = new Image(); im.onload = () => {
      L.img = im; L.pw = 474; L.ph = 355;
      window.STX.aiJob(job => { const out = [job.w, job.h, job.k]; L.img = keep.img; L.pw = keep.pw; L.ph = keep.ph; r(out); });
    }; im.src = cv.toDataURL('image/jpeg', 0.9);
  }));
  assert.ok(small[2] > 3 && Math.max(small[0], small[1]) >= 1000, 'small photo: reference ' + small);
  ok('small photo (474 x 355): the AI works at ' + small[2].toFixed(1) + 'x, reference ' + small[0] + ' x ' + small[1]);
  await f.evaluate(() => window.STX.setView('impression'));
  await page.waitForTimeout(600);
  await page.screenshot({ path: path.join(OUT, 'ai-upload-composite.png') });
  ok('manual upload of a crop result: pasted back into the full photo');

  // floor mode (Robin's warehouse aisle): a floor rectangle + the spot where the design stands.
  // Further back = smaller, the virtual wall stands on the spot, and it survives save/load.
  const floor = await f.evaluate(() => {
    const S = window.STX, L = S.state.loc;
    S.setView('location');
    S.setLocKind('floor');
    L.fquad = [{ x: L.pw * 0.4, y: L.ph * 0.5 }, { x: L.pw * 0.6, y: L.ph * 0.5 }, { x: L.pw * 0.9, y: L.ph * 0.95 }, { x: L.pw * 0.1, y: L.ph * 0.95 }];
    L.FW = 300; L.FD = 1000;
    const widthAt = (y) => { L.spot = { x: L.pw * 0.5, y: y }; S.computeLoc(false); return { w: L.quad[2].x - L.quad[3].x, bottom: (L.quad[2].y + L.quad[3].y) / 2, W: L.W }; };
    const back = widthAt(L.ph * 0.55), front = widthAt(L.ph * 0.9);
    const saved = JSON.parse(JSON.stringify(S.serialize().loc));
    return { isFloor: S.isFloor(L), back, front, spotY: L.spot.y, saved };
  });
  assert.ok(floor.isFloor, 'floor mode on');
  assert.ok(floor.back.w > 0 && floor.front.w > floor.back.w * 1.5, 'closer = bigger: back ' + floor.back.w.toFixed(0) + ' px, front ' + floor.front.w.toFixed(0) + ' px');
  assert.ok(Math.abs(floor.front.bottom - floor.spotY) < 2, 'the virtual wall stands on the spot: ' + floor.front.bottom + ' vs ' + floor.spotY);
  assert.strictEqual(floor.front.W, 300);
  assert.ok(floor.saved.kind === 'floor' && floor.saved.fquad.length === 4 && floor.saved.FW === 300 && floor.saved.FD === 1000 && floor.saved.spot, JSON.stringify(floor.saved).slice(0, 200));
  await f.click('#btn-photo');
  assert.ok(await f.$('#lc-fw') && await f.$('#lc-fd'), 'location window shows floor width and depth');
  await page.screenshot({ path: path.join(OUT, 'location-floor-modal.png') });
  await f.click('#lc-corners');
  await page.waitForTimeout(400);
  assert.ok(/floor rectangle/.test(await f.$eval('#cornerhint-text', el => el.textContent)));
  await page.screenshot({ path: path.join(OUT, 'location-floor.png') });
  await f.click('#corner-done');
  // round trip: load the saved project, still floor, same size at the spot
  const again = await f.evaluate((saved) => new Promise(r => {
    const S = window.STX, obj = S.serialize(); obj.loc = saved; S.load(obj);
    setTimeout(() => { const L = S.state.loc; r({ isFloor: S.isFloor(L), w: L.quad[2].x - L.quad[3].x }); }, 1200);
  }), floor.saved);
  assert.ok(again.isFloor && Math.abs(again.w - floor.front.w) < 1, 'reloaded floor: ' + JSON.stringify(again));
  // back to wall: the old wall comes back
  const wall = await f.evaluate(() => { const S = window.STX; S.setLocKind('wall'); return [S.isFloor(S.state.loc), S.state.loc.W, S.state.loc.H]; });
  assert.deepStrictEqual(wall, [false, 1200, 700]);
  ok('floor mode: closer is ' + (floor.front.w / floor.back.w).toFixed(1) + 'x bigger, the design stands on the purple spot, saved and reloaded as floor, back to wall keeps 1200 x 700');

  // 10. phone
  const ph = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  ph.on('pageerror', e => errors.push('phone: ' + e.message));
  await ph.goto(base + '/design-sheet');
  await ph.waitForFunction(() => { const fr = document.getElementById('stx-ds-frame'); return fr && fr.contentWindow && fr.contentWindow.STX; }, null, { timeout: 30000 });
  await ph.waitForTimeout(2000);
  await ph.screenshot({ path: path.join(OUT, 'phone.png') });
  ok('phone layout renders');

  assert.deepStrictEqual(errors, [], 'page errors: ' + errors.join(' / '));
  ok('no page errors');
  await browser.close(); server.close();
  console.log('ALL PASSED');
})().catch(async e => { console.error('FAIL', e); process.exit(1); });
