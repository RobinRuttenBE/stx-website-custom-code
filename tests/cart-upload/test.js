// Local harness for sections/cart-upload-v1.html: fake Odoo cart page + mocked shop routes + Playwright.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.STX_PLAYWRIGHT || '../../../stx-tools/node_modules/playwright');

const REPO = path.resolve(__dirname, '../..');
const CSV = process.env.STX_ORDER_CSV || path.join(__dirname, 'example-order.csv'); // echte klantbestelling, 108 regels
const FIX = JSON.parse(fs.readFileSync(path.join(__dirname, 'autocomplete-fixture.json'), 'utf8'));
const OUT = __dirname;

let cartCalls = [];
let updateCalls = [];
let comboCalls = 0;
// Fake Odoo cart. /shop/cart/add ADDS to what is already on the line (that is what the live shop
// does, tested 21/09/2026) and /shop/cart/update sets an exact quantity. The section has to end up
// with the quantity from the file, whatever was in the cart before.
let fakeCart = {};   // line_id -> { tid, qty }
let lineByTid = {};  // template id -> line_id
let nextLineId = 1000;
function cartTotal() { return Object.keys(fakeCart).reduce((a, k) => a + fakeCart[k].qty, 0); }
function cartQtyOf(tid) { const lid = lineByTid[tid]; return lid ? fakeCart[lid].qty : 0; }
function readBody(req) { return new Promise(r => { let b = ''; req.on('data', c => b += c); req.on('end', () => r(b)); }); }

function cartPage(lang, loggedIn) {
  return `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><title>Cart</title></head><body>
<div id="wrapwrap"><header>${loggedIn ? '<a href="/web/session/logout">Logout</a>' : '<a href="/web/login">Login</a>'}</header>
<div id="wrap"><div class="oe_website_sale o_website_sale_checkout_container container">
<div class="o_wizard">steps</div>
<div class="oe_clear_stucture oe_cart col-12"><div id="shop_cart" class="col"><div class="js_cart_lines">CART LINES HERE</div></div><div class="o_wsale_shorter_cart_summary">summary</div></div>
</div></div></div>
<script>
(function(){
  function inject(htmlText){ var tpl=document.createElement('template'); tpl.innerHTML=htmlText;
    var scripts=Array.prototype.slice.call(tpl.content.querySelectorAll('script')); scripts.forEach(function(s){ s.parentNode.removeChild(s); });
    document.body.appendChild(tpl.content);
    scripts.forEach(function(old){ var s=document.createElement('script'); s.text=old.text; document.body.appendChild(s); }); }
  fetch('/sections/cart-upload-v1.html').then(function(r){return r.text()}).then(inject);
})();
</script></body></html>`;
}

const server = http.createServer(async (req, res) => {
  const u = new URL(req.url, 'http://x');
  if (u.pathname === '/sections/cart-upload-v1.html') { res.setHeader('Content-Type', 'text/html'); return res.end(fs.readFileSync(path.join(REPO, 'sections/cart-upload-v1.html'))); }
  if (/\/shop\/cart$/.test(u.pathname)) {
    const lang = u.pathname.startsWith('/en_GB') ? 'en' : u.pathname.startsWith('/fr') ? 'fr' : 'nl';
    res.setHeader('Content-Type', 'text/html'); return res.end(cartPage(lang, u.searchParams.get('guest') !== '1'));
  }
  if (req.method === 'POST') {
    const body = JSON.parse(await readBody(req) || '{}');
    res.setHeader('Content-Type', 'application/json');
    if (u.pathname.endsWith('/website/snippet/autocomplete')) {
      await new Promise(r => setTimeout(r, 30));
      const term = body.params.term;
      return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: FIX[term] || { results_count: 0, results: [] } }));
    }
    if (u.pathname === '/website_sale/get_combination_info') { comboCalls++; return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: { product_id: body.params.product_template_id * 10, price: 1 } })); }
    if (u.pathname === '/shop/cart/add') {
      cartCalls.push(body.params);
      const tid = body.params.product_template_id;
      if (tid === 3773) return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, error: { message: 'Odoo Server Error', data: { message: 'The given product does not exist therefore it cannot be added to cart.' } } }));
      let lid = lineByTid[tid];
      if (!lid) { lid = ++nextLineId; lineByTid[tid] = lid; fakeCart[lid] = { tid, qty: 0 }; }
      fakeCart[lid].qty += body.params.quantity;
      return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: { quantity: fakeCart[lid].qty, cart_quantity: cartTotal(), notification_info: { warning: '', lines: [{ id: lid, quantity: fakeCart[lid].qty, name: 'x' }] } } }));
    }
    if (u.pathname === '/shop/cart/update') {
      updateCalls.push(body.params);
      const lid = body.params.line_id;
      const before = fakeCart[lid] ? fakeCart[lid].qty : 0;
      if (fakeCart[lid]) fakeCart[lid].qty = body.params.quantity;
      return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: { line_id: lid, quantity: body.params.quantity, added_qty: body.params.quantity - before, cart_quantity: cartTotal() } }));
    }
  }
  res.statusCode = 404; res.end('nope');
});

function assert(c, msg) { if (!c) { console.error('FAIL', msg); process.exitCode = 1; } else { console.log('ok  ', msg); } }

(async () => {
  await new Promise(r => server.listen(0, r));
  const base = 'http://localhost:' + server.address().port;
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  page.on('pageerror', e => { console.error('PAGEERROR', e.message); process.exitCode = 1; });

  // 1. live (BETA = false): the card shows on a plain visit, no hash needed
  await page.goto(base + '/en_GB/shop/cart'); await page.waitForSelector('#stx-upl:not([hidden])', { timeout: 8000 });
  assert(await page.$eval('#stx-upl', e => !e.hidden), 'live: card shows without #stxupload');
  assert(await page.$('#stx-upl .su-beta') === null, 'live: no beta badge left');
  // 2. the hash still works and changes nothing
  await page.goto('about:blank'); await page.goto(base + '/en_GB/shop/cart#stxupload'); await page.waitForSelector('#stx-upl:not([hidden])');
  assert(await page.$eval('#stx-upl', e => e.nextElementSibling && e.nextElementSibling.classList.contains('oe_cart')), 'card placed before .oe_cart');
  assert((await page.textContent('#stx-upl h3')).includes('Upload your order'), 'english copy');
  // 3. guest: hidden even with beta
  await page.goto(base + '/en_GB/shop/cart?guest=1'); await page.waitForTimeout(400);
  assert(await page.$eval('#stx-upl', e => e.hidden), 'guest: card hidden');
  // 4. NL page + upload the real CSV
  await page.goto(base + '/shop/cart'); await page.waitForSelector('#stx-upl:not([hidden])');
  assert((await page.textContent('#stx-upl h3')).includes('Upload je bestelling'), 'dutch copy');
  await page.click('#su-toggle');
  await page.setInputFiles('#su-file', CSV);
  await page.waitForSelector('#su-preview:not([hidden])', { timeout: 20000 });
  const pills = await page.$$eval('#su-sum .su-pill', els => els.map(e => e.textContent));
  console.log('   pills:', pills.join(' | '));
  const rows = await page.$$eval('#su-rows tr', trs => trs.map(tr => tr.className));
  if (process.env.STX_DUMP) { // STX_DUMP=1 prints code, matched product and quantity per line, to compare with the source file
    const dump = await page.$$eval('#su-rows tr', trs => trs.map(tr => [tr.querySelector('.su-code').textContent, tr.querySelector('.su-qty').textContent, tr.querySelector('td:nth-child(2)').textContent.trim(), tr.className].join(' | ')));
    console.log('   --- preview rows ---'); dump.forEach((d, i) => console.log('   ' + String(i + 1).padStart(3) + '  ' + d));
  }
  assert(rows.length === 108, '108 lines parsed (got ' + rows.length + ')');
  assert(rows.filter(c => c === 'ok').length === 107, '107 exact matches (R12826 resolved to the plain 50 pcs product by the exact rule)');
  assert(rows.filter(c => c === 'multi').length === 0, '0 ambiguous');
  assert(rows.filter(c => c === 'chk').length === 1, '1 via search (20021027)');
  const r826 = await page.$$eval('#su-rows tr', trs => { const tr = trs.find(x => x.querySelector('.su-code').textContent === 'R12826'); return tr.querySelector('td:nth-child(2)').textContent; });
  assert(r826 === 'R12 - Silk Cool Mint - 826 - 50 Pcs', 'R12826 -> plain 50 pcs product, not the punten variant (' + r826 + ')');
  const chkName = await page.$eval('#su-rows tr.chk td:nth-child(2)', td => td.textContent);
  assert(chkName.includes('Nozzle Up - Cosmo Pink - 013'), '20021027 -> N260013 (' + chkName + ')');
  const btn = await page.textContent('#su-add'); assert(btn.trim() === '108 regels in winkelmandje', 'add button label: ' + btn.trim());
  await page.screenshot({ path: path.join(OUT, 'preview-nl.png'), fullPage: true });
  // 5. add all
  cartCalls = []; comboCalls = 0;
  await page.click('#su-add');
  await page.waitForFunction(() => document.querySelector('#su-lastresult') && !document.querySelector('#su-lastresult').hidden, null, { timeout: 60000 });
  const resultTxt = await page.textContent('#su-lastresult'); console.log('   result:', resultTxt.trim());
  assert(cartCalls.length === 108, '108 cart calls (' + cartCalls.length + ')');
  assert(cartCalls.some(c => c.quantity === 440), 'quantity passed through as packs (440 line)');
  const c440 = cartCalls.find(c => c.quantity === 440);
  assert(cartQtyOf(c440.product_template_id) === 440, 'cart holds exactly 440 for that product (' + cartQtyOf(c440.product_template_id) + ')');
  assert(updateCalls.length === 0, 'empty cart: no correction needed (' + updateCalls.length + ' updates)');
  assert(resultTxt.includes('107 regels') && resultTxt.includes('N160080'), 'result: 107 added, N160080 failed (mocked cart error)');
  assert(resultTxt.includes('De shop meldt') && resultTxt.includes('does not exist'), 'the shop error message is shown, not just "failed": ' + resultTxt.slice(-150));
  await page.screenshot({ path: path.join(OUT, 'done-nl.png'), fullPage: true });
  await page.waitForURL(/\/shop\/cart$/, { timeout: 8000 });
  await page.waitForSelector('#su-lastresult:not([hidden])');
  assert((await page.textContent('#su-lastresult')).includes('107 regels'), 'result banner survives the reload');
  // 6. paste with semicolons, header, duplicates, spaces, decimal comma, junk line
  await page.click('#su-reset');
  await page.click('#su-pastebtn');
  await page.fill('#su-paste', 'code;aantal\nr12005 ; 2\nR12005;3\nN260080;1,0\nFOOBAR1;4\n;;\nhallo dit is tekst\nLOL6015;0\nMULTI1;9\n');
  await page.click('#su-paste-go');
  await page.waitForSelector('#su-preview:not([hidden])');
  const rows2 = await page.$$eval('#su-rows tr', trs => trs.map(tr => tr.querySelector('.su-code').textContent + ':' + tr.querySelector('.su-qty').textContent + ':' + tr.className));
  console.log('   paste rows:', rows2.join(' | '));
  assert(rows2.length === 4 && rows2[0] === 'R12005:5:ok' && rows2[1] === 'N260080:1:ok' && rows2[2] === 'FOOBAR1:4:no' && rows2[3] === 'MULTI1:9:multi', 'paste: merged, header skipped, junk skipped, unknown red, ambiguous dropdown');
  assert((await page.textContent('#su-add')).trim() === '3 regels in winkelmandje', 'paste: 3 addable');
  await page.selectOption('#su-rows tr.multi select', '1');
  const qtyBefore = {}; Object.keys(lineByTid).forEach(tid => { qtyBefore[tid] = cartQtyOf(Number(tid)); });
  cartCalls = []; updateCalls = []; await page.click('#su-add');
  await page.waitForFunction(() => !document.querySelector('#su-lastresult').hidden && document.querySelector('#su-lastresult').textContent.includes('3 regels'), null, { timeout: 20000 });
  assert(cartCalls.some(c => c.product_template_id === 222 && c.quantity === 9), 'dropdown choice (Something B, tid 222) went to the cart');
  // The bug Robin hit: /shop/cart/add sums, so a product that was already in the cart ended up too high.
  const reAdded = cartCalls.filter(c => qtyBefore[c.product_template_id] > 0);
  assert(reAdded.length >= 1, 'at least one product was already in the cart from the 108-line run (' + reAdded.length + ')');
  const wrong = cartCalls.filter(c => cartQtyOf(c.product_template_id) !== c.quantity)
    .map(c => c.product_template_id + ': asked ' + c.quantity + ', cart has ' + cartQtyOf(c.product_template_id));
  assert(wrong.length === 0, 'every line ends at the quantity from the file, not added on top: ' + (wrong.join(' | ') || 'all correct'));
  assert(updateCalls.length === reAdded.length, 'each line that was already in the cart got a /shop/cart/update correction (' + updateCalls.length + ' updates for ' + reAdded.length + ')');
  await page.waitForURL(/\/shop\/cart$/, { timeout: 8000 }); await page.waitForSelector('#stx-upl:not([hidden])');
  // 7. xlsx: build one in the browser with SheetJS and upload it
  const xp = await ctx.newPage();
  await xp.setContent('<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>');
  await xp.waitForFunction(() => !!window.XLSX);
  const b64 = await xp.evaluate(() => { const wb = XLSX.utils.book_new(); XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet([['Supplier Code', 'Quantity'], ['R12005', 7], ['LOL6015', 2]]), 'Order'); return XLSX.write(wb, { type: 'base64', bookType: 'xlsx' }); });
  await xp.close();
  await page.click('#su-reset');
  await page.setInputFiles('#su-file', { name: 'order.xlsx', mimeType: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', buffer: Buffer.from(b64, 'base64') });
  await page.waitForSelector('#su-preview:not([hidden])', { timeout: 30000 });
  const rows3 = await page.$$eval('#su-rows tr', trs => trs.map(tr => tr.querySelector('.su-code').textContent + ':' + tr.querySelector('.su-qty').textContent + ':' + tr.className));
  console.log('   xlsx rows:', rows3.join(' | '));
  assert(rows3.length === 2 && rows3[0] === 'R12005:7:ok' && rows3[1] === 'LOL6015:2:ok', 'xlsx read via SheetJS');
  // 8. live: #stxupload-uit no longer hides the card
  await page.goto('about:blank'); await page.goto(base + '/shop/cart#stxupload-uit'); await page.waitForSelector('#stx-upl:not([hidden])', { timeout: 8000 });
  assert(await page.$eval('#stx-upl', e => !e.hidden), 'live: #stxupload-uit does not hide it any more');
  // mobile screenshot
  const mp = await b.newPage({ viewport: { width: 390, height: 800 } });
  await mp.goto(base + '/en_GB/shop/cart'); await mp.waitForSelector('#stx-upl:not([hidden])'); await mp.click('#su-toggle');
  await mp.setInputFiles('#su-file', CSV); await mp.waitForSelector('#su-preview:not([hidden])', { timeout: 20000 });
  await mp.screenshot({ path: path.join(OUT, 'preview-mobile.png'), fullPage: false });
  await b.close(); server.close();
  console.log(process.exitCode ? 'SOME TESTS FAILED' : 'ALL TESTS PASSED');
})().catch(e => { console.error(e); process.exit(1); });
