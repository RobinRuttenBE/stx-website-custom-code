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
let searchCalls = 0;
let flakyFails = {}, triesByTerm = {};
// Stock per template id, only for the products listed here (test 10). The live shop (measured 19/10/2026) silently
// caps /shop/cart/add and /shop/cart/update at the free stock and adds nothing when the stock is 0.
let stock = {};
function capQty(tid, q) { return stock[tid] === undefined ? q : Math.min(q, stock[tid]); }
// Fake Odoo cart. /shop/cart/add ADDS to what is already on the line (that is what the live shop
// does, tested 21/09/2026) and /shop/cart/update sets an exact quantity. The section has to end up
// with the quantity from the file, whatever was in the cart before.
let fakeCart = {};   // line_id -> { tid, qty }
let lineByTid = {};  // template id -> line_id
let nextLineId = 1000;
let inFlight = 0, maxInFlight = 0; // concurrent /shop/cart/update calls: the empty button must never go above 1
function cartTotal() { return Object.keys(fakeCart).reduce((a, k) => a + fakeCart[k].qty, 0); }
function cartQtyOf(tid) { const lid = lineByTid[tid]; return lid ? fakeCart[lid].qty : 0; }
function readBody(req) { return new Promise(r => { let b = ''; req.on('data', c => b += c); req.on('end', () => r(b)); }); }

// Same markup as Odoo saas-18.4 website_sale.cart_lines: one js_quantity input per line with data-line-id.
function cartLinesHtml() {
  return Object.keys(fakeCart).map(lid => `<div class="o_cart_product"><a href="#" class="js_delete_product small">Remove</a><input type="text" class="js_quantity quantity form-control" data-line-id="${lid}" data-product-id="${fakeCart[lid].tid * 10}" value="${fakeCart[lid].qty}"/></div>`).join('');
}
function cartPage(lang, loggedIn) {
  return `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><title>Cart</title></head><body>
<div id="wrapwrap"><header>${loggedIn ? '<a href="/web/session/logout">Logout</a>' : '<a href="/web/login">Login</a>'}</header>
<div id="wrap"><div class="oe_website_sale o_website_sale_checkout_container container">
<div class="o_wizard">steps</div>
<div class="oe_clear_stucture oe_cart col-12 col-lg-7"><div id="shop_cart" class="col">`
  + `<div class="d-flex align-items-center mb-3"><h4 class="mb-0">Besteloverzicht</h4><div class="ms-3 border-start ps-2"><span><button id="quick_reorder_button" type="button" class="btn btn-sm btn-link" disabled>Snel opnieuw bestellen</button></span></div></div>`
  + `<div id="cart_products" class="js_cart_lines d-flex flex-column">${cartLinesHtml()}</div></div></div>`
  + `<div class="o_wsale_shorter_cart_summary col-lg-5">summary</div>
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
      searchCalls++;
      await new Promise(r => setTimeout(r, 30));
      const term = body.params.term;
      // Flaky connection (test 12): a term fails its first flakyFails[term] attempts, as HTTP 429 or a dropped connection.
      triesByTerm[term] = (triesByTerm[term] || 0) + 1;
      if (flakyFails[term] && triesByTerm[term] <= flakyFails[term]) {
        if (triesByTerm[term] % 2) { res.statusCode = 429; return res.end('Too Many Requests'); }
        return req.socket.destroy();
      }
      return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: FIX[term] || { results_count: 0, results: [] } }));
    }
    if (u.pathname === '/website_sale/get_combination_info') {
      comboCalls++;
      const tid = body.params.product_template_id;
      const r = { product_id: tid * 10, price: 1 };
      if (stock[tid] !== undefined) Object.assign(r, { is_storable: true, allow_out_of_stock_order: false, free_qty: stock[tid], cart_qty: cartQtyOf(tid) });
      return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: r }));
    }
    if (u.pathname === '/shop/cart/add') {
      cartCalls.push(body.params);
      const tid = body.params.product_template_id;
      if (tid === 3773) return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, error: { message: 'Odoo Server Error', data: { message: 'The given product does not exist therefore it cannot be added to cart.' } } }));
      let lid = lineByTid[tid];
      if (capQty(tid, cartQtyOf(tid) + body.params.quantity) <= 0) return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: { quantity: 0, cart_quantity: cartTotal(), notification_info: { warning: 'out of stock', lines: [] } } }));
      if (!lid) { lid = ++nextLineId; lineByTid[tid] = lid; fakeCart[lid] = { tid, qty: 0 }; }
      fakeCart[lid].qty = capQty(tid, fakeCart[lid].qty + body.params.quantity);
      return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: { quantity: fakeCart[lid].qty, cart_quantity: cartTotal(), notification_info: { warning: '', lines: [{ id: lid, quantity: fakeCart[lid].qty, name: 'x' }] } } }));
    }
    if (u.pathname === '/shop/cart/update') {
      updateCalls.push(body.params);
      const lid = body.params.line_id;
      inFlight++; maxInFlight = Math.max(maxInFlight, inFlight);
      await new Promise(r => setTimeout(r, 25)); // the live shop re-renders the whole cart per call, so it is slow
      inFlight--;
      // A line that no longer exists (e.g. removed together with its parent line) errors, like Odoo does.
      if (!fakeCart[lid]) return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, error: { message: 'Odoo Server Error', data: { message: 'Missing record' } } }));
      const before = fakeCart[lid].qty;
      if (body.params.quantity <= 0) { delete lineByTid[fakeCart[lid].tid]; delete fakeCart[lid]; }
      else fakeCart[lid].qty = capQty(fakeCart[lid].tid, body.params.quantity);
      const now = fakeCart[lid] ? fakeCart[lid].qty : 0;
      return res.end(JSON.stringify({ jsonrpc: '2.0', id: 1, result: { line_id: lid, quantity: now, added_qty: now - before, cart_quantity: cartTotal() } }));
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
  assert(rows.filter(c => c === 'ok').length === 108, '108 matches, SAP/barcode lines count as found too (R12826 resolved to the plain 50 pcs product by the exact rule)');
  assert(rows.filter(c => c === 'multi').length === 0, '0 ambiguous');
  assert(rows.filter(c => c === 'chk').length === 0, 'no "check" status left for a SAP code match');
  const r826 = await page.$$eval('#su-rows tr', trs => { const tr = trs.find(x => x.querySelector('.su-code').textContent === 'R12826'); return tr.querySelector('td:nth-child(2)').textContent; });
  assert(r826 === 'R12 - Silk Cool Mint - 826 - 50 Pcs', 'R12826 -> plain 50 pcs product, not the punten variant (' + r826 + ')');
  const barName = await page.$$eval('#su-rows tr', trs => { const tr = trs.find(x => x.querySelector('.su-code').textContent === '20021027'); return tr.querySelector('td:nth-child(2)').textContent + '|' + tr.className + '|' + tr.querySelector('.su-st').textContent; });
  assert(barName.includes('Nozzle Up - Cosmo Pink - 013') && barName.includes('|ok|'), 'SAP code 20021027 -> N260013, marked found (' + barName + ')');
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
  assert(rows2.length === 4 && rows2[0] === 'MULTI1:9:multi' && rows2[1] === 'FOOBAR1:4:no' && rows2[2] === 'R12005:5:ok' && rows2[3] === 'N260080:1:ok', 'paste: merged, header skipped, junk skipped, unknown red, ambiguous dropdown, problem lines on top');
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
  // 9. empty the cart in one go: one line at a time, cart locked meanwhile, result after the reload
  const before9 = Object.keys(fakeCart).length;
  await page.goto('about:blank'); await page.goto(base + '/shop/cart'); await page.waitForSelector('#stx-upl:not([hidden])');
  const ghost = ++nextLineId; fakeCart[ghost] = { tid: 999999, qty: 1 }; // added after the page rendered: not on screen, so the button must leave it alone
  assert(before9 > 100, 'cart has ' + before9 + ' lines before emptying');
  assert(await page.$eval('.stx-empty-btn', e => !e.hidden && e.textContent === 'Winkelmandje leegmaken'), 'empty button visible with its label');
  assert(await page.$eval('.stx-empty-wrap', e => e.previousElementSibling.querySelector('#quick_reorder_button') !== null && e.parentNode.querySelector('h4').textContent === 'Besteloverzicht'), 'empty button sits right after "Snel opnieuw bestellen" in the Besteloverzicht row');
  assert(await page.$('#stx-upl .stx-empty-btn') === null, 'not inside the upload card');
  updateCalls = []; maxInFlight = 0;
  await page.click('.stx-empty-btn');
  const confirmTxt = await page.textContent('.stx-empty-btn');
  assert(confirmTxt === 'Klik nog eens om alle ' + before9 + ' regels te verwijderen', 'first click only asks to confirm: ' + confirmTxt);
  await page.screenshot({ path: path.join(OUT, 'empty-confirm-nl.png'), clip: { x: 0, y: 0, width: 1280, height: 320 } });
  await page.waitForTimeout(150);
  assert(updateCalls.length === 0, 'nothing removed after the first click');
  await page.click('.stx-empty-btn');
  await page.waitForFunction(() => document.querySelector('#cart_products.stx-cart-locked'), null, { timeout: 3000 });
  assert(await page.$eval('.o_wsale_shorter_cart_summary', e => e.classList.contains('stx-cart-locked')), 'cart lines and summary locked while emptying');
  assert(await page.$eval('.stx-empty-wrap', e => !e.closest('.stx-cart-locked')), 'the row with the button is not faded');
  assert(/Regel \d+ van \d+ verwijderen/.test(await page.textContent('.stx-empty-btn')), 'progress shown on the button');
  await page.waitForURL(/\/shop\/cart$/, { timeout: 30000 }); await page.waitForSelector('.stx-empty-msg:not([hidden])', { timeout: 30000 });
  assert(updateCalls.length === before9 && updateCalls.every(c => c.quantity === 0), before9 + ' remove calls with quantity 0 (' + updateCalls.length + ')');
  assert(maxInFlight === 1, 'never more than 1 update at a time (max ' + maxInFlight + ')');
  assert(Object.keys(fakeCart).length === 1 && fakeCart[ghost], 'every line from the page is gone, nothing else touched');
  const emptyTxt = await page.textContent('.stx-empty-msg');
  assert(emptyTxt.includes('Je winkelmandje is leeg (' + before9 + ' regels verwijderd)'), 'result after reload: ' + emptyTxt.trim());
  assert(await page.$eval('#su-lastresult', e => e.hidden), 'result is next to the button, not in the upload card');
  delete fakeCart[ghost];
  await page.goto('about:blank'); await page.goto(base + '/shop/cart'); await page.waitForSelector('#stx-upl:not([hidden])');
  assert(await page.$eval('.stx-empty-btn', e => e.hidden), 'empty cart: no empty button');
  // 10. stock: out of stock is shown and not added, less stock gets an input set to what is there
  const T_R12005 = 3979, T_N260080 = 3811, T_LOL6015 = 3689;
  Object.keys(fakeCart).forEach(k => delete fakeCart[k]); lineByTid = {};
  stock = { [T_R12005]: 3, [T_N260080]: 0, [T_LOL6015]: 50 };
  await page.goto('about:blank'); await page.goto(base + '/shop/cart'); await page.waitForSelector('#stx-upl:not([hidden])');
  await page.click('#su-toggle'); await page.click('#su-pastebtn');
  await page.fill('#su-paste', 'LOL6015;2\nR12005;10\nN260080;5\n');
  await page.click('#su-paste-go');
  await page.waitForSelector('#su-preview:not([hidden])');
  const rows10 = await page.$$eval('#su-rows tr', trs => trs.map(tr => tr.querySelector('.su-code').textContent + ':' + tr.className + ':' + tr.querySelector('.su-st').textContent));
  console.log('   stock rows:', rows10.join(' | '));
  assert(rows10[0] === 'N260080:oos:niet op voorraad' && rows10[1] === 'R12005:short:3 van 10 op voorraad' && rows10[2] === 'LOL6015:ok:gevonden', 'out of stock first, then less stock, then the rest');
  assert(await page.$eval('#su-rows tr.short input.su-qin', e => e.value === '3' && e.max === '3'), 'less stock: input filled with the 3 that are there');
  const notices = await page.textContent('#su-notices');
  assert(notices.includes('Niet op voorraad, wordt niet toegevoegd') && notices.includes('N260080') && notices.includes('Minder voorraad dan je vroeg'), 'notice names the out of stock product and the short one: ' + notices.trim());
  assert((await page.textContent('#su-add')).trim() === '2 regels in winkelmandje', 'add button counts 2 lines (out of stock left out)');
  await page.fill('#su-rows tr.short input.su-qin', '2');
  assert((await page.textContent('#su-sum')).includes('4 zakken in totaal'), 'total follows the edited quantity (2 + 2)');
  await page.fill('#su-rows tr.short input.su-qin', '9');
  await page.press('#su-rows tr.short input.su-qin', 'Tab');
  assert(await page.$eval('#su-rows tr.short input.su-qin', e => e.value === '3'), 'typing more than the stock goes back to the stock');
  await page.fill('#su-rows tr.short input.su-qin', '2');
  await page.screenshot({ path: path.join(OUT, 'stock-nl.png'), fullPage: true });
  stock[T_LOL6015] = 1; // stock changes between the preview and the click: Odoo caps it, the result must say so
  cartCalls = []; updateCalls = [];
  const nav10 = page.waitForNavigation({ timeout: 15000 }); // same URL before and after, so waitForURL would not wait for the reload
  await page.click('#su-add'); await nav10; await page.waitForSelector('#su-lastresult:not([hidden])');
  assert(!cartCalls.some(c => c.product_template_id === T_N260080), 'out of stock product never sent to the cart');
  assert(cartCalls.some(c => c.product_template_id === T_R12005 && c.quantity === 2), 'edited quantity (2) sent for R12005');
  assert(cartQtyOf(T_R12005) === 2 && cartQtyOf(T_LOL6015) === 1, 'cart: R12005 2, LOL6015 capped to 1');
  const res10 = await page.textContent('#su-lastresult'); console.log('   stock result:', res10.replace(/\s+/g, ' ').trim());
  assert(res10.includes('Niet op voorraad, niet toegevoegd (1)') && res10.includes('N260080'), 'after reload: out of stock list');
  assert(res10.includes('Minder voorraad dan gevraagd (2)') && res10.includes('2 van 10 zakken') && res10.includes('1 van 2 zakken'), 'after reload: short list with what ended up in the cart');
  assert(await page.$eval('#su-lastresult', e => e.classList.contains('warn')), 'result shown as a warning');
  await page.screenshot({ path: path.join(OUT, 'stock-result-nl.png'), fullPage: true });
  stock = {};
  // 11. max 500 order lines: 501 refused without a single shop call, 500 accepted, a 6 MB file not even read
  await page.click('#su-pastebtn');
  searchCalls = 0;
  // fill() chokes on 30000 lines, so the value is set directly
  const pasteLines = n => page.$eval('#su-paste', (e, n) => { e.value = Array.from({ length: n }, (_, i) => 'X' + i + ';1').join('\n'); }, n);
  await pasteLines(30000);
  await page.click('#su-paste-go'); await page.waitForTimeout(300);
  const st30k = await page.textContent('#su-status');
  assert(st30k.includes('30.000 bestelregels') && st30k.includes('maximaal 500'), '30000 lines refused: ' + st30k);
  assert(searchCalls === 0 && await page.$eval('#su-preview', e => e.hidden), 'no shop call and no preview for a refused file');
  await pasteLines(501);
  await page.click('#su-paste-go'); await page.waitForTimeout(200);
  assert((await page.textContent('#su-status')).includes('501 bestelregels') && searchCalls === 0, '501 lines refused');
  await pasteLines(500);
  await page.click('#su-paste-go');
  await page.waitForSelector('#su-preview:not([hidden])', { timeout: 60000 });
  assert((await page.$$('#su-rows tr')).length === 500 && searchCalls === 500, '500 lines accepted (' + searchCalls + ' searches)');
  await page.click('#su-reset'); searchCalls = 0;
  await page.setInputFiles('#su-file', { name: 'huge.csv', mimeType: 'text/csv', buffer: Buffer.alloc(6 * 1024 * 1024, 'A') });
  await page.waitForTimeout(200);
  assert((await page.textContent('#su-status')).includes('te groot') && searchCalls === 0, '6 MB file refused before reading');
  // 12. flaky connection (Balloon Market, 16/10/2026: 41 and 47 "not found" that were in the shop).
  // A search that fails is never "not found": it is retried, and what still fails is "niet gecontroleerd" with a button.
  await page.goto('about:blank'); await page.goto(base + '/shop/cart'); await page.waitForSelector('#stx-upl:not([hidden])');
  await page.click('#su-toggle'); await page.click('#su-pastebtn');
  triesByTerm = {};
  flakyFails = { R12005: 2, LOL6015: 1, N260080: 99 }; // R12005 and LOL6015 recover on their own, N260080 keeps failing
  await page.fill('#su-paste', 'R12005;3\nLOL6015;2\nN260080;1\nFOOBAR1;4\n');
  await page.click('#su-paste-go');
  await page.waitForSelector('#su-preview:not([hidden])', { timeout: 30000 });
  const rows12 = await page.$$eval('#su-rows tr', trs => trs.map(tr => tr.querySelector('.su-code').textContent + ':' + tr.className + ':' + tr.querySelector('.su-st').textContent));
  console.log('   flaky rows:', rows12.join(' | '));
  assert(rows12.includes('R12005:ok:gevonden') && rows12.includes('LOL6015:ok:gevonden'), 'codes that failed 1-2 times are found after the automatic retries');
  assert(rows12[0] === 'N260080:err:niet gecontroleerd', 'a code that keeps failing is "niet gecontroleerd" at the top, not "niet gevonden"');
  assert(rows12.includes('FOOBAR1:no:niet gevonden'), 'a code the shop really does not know is still "niet gevonden"');
  // 3 tries in the first round + 3 in the calm second round = 6 from the card; Chrome itself silently resends some
  // requests whose connection was dropped, so the server can see more.
  assert(triesByTerm.N260080 >= 6, 'the failing code was tried at least 3 + 3 times (' + triesByTerm.N260080 + ' requests seen by the server)');
  const n12 = await page.textContent('#su-notices');
  assert(n12.includes('haperende verbinding, geen ontbrekend product') && !!(await page.$('#su-recheck')), 'notice explains it and offers "Opnieuw controleren"');
  assert((await page.textContent('#su-add')).trim() === '2 regels in winkelmandje', 'unchecked line is not added');
  await page.screenshot({ path: path.join(OUT, 'flaky-nl.png'), fullPage: true });
  flakyFails = {}; // the connection is fine again
  await page.click('#su-recheck');
  await page.waitForFunction(() => !document.querySelector('#su-recheck') && !document.querySelector('#su-rows tr.err'), null, { timeout: 15000 });
  const r12b = await page.$$eval('#su-rows tr', trs => trs.map(tr => tr.querySelector('.su-code').textContent + ':' + tr.className));
  assert(r12b.includes('N260080:ok') && (await page.textContent('#su-add')).trim() === '3 regels in winkelmandje', 'after "Opnieuw controleren" the code is found and can be added');

  // mobile screenshot
  const mp = await b.newPage({ viewport: { width: 390, height: 800 } });
  await mp.goto(base + '/en_GB/shop/cart'); await mp.waitForSelector('#stx-upl:not([hidden])'); await mp.click('#su-toggle');
  await mp.setInputFiles('#su-file', CSV); await mp.waitForSelector('#su-preview:not([hidden])', { timeout: 20000 });
  await mp.screenshot({ path: path.join(OUT, 'preview-mobile.png'), fullPage: false });
  await b.close(); server.close();
  console.log(process.exitCode ? 'SOME TESTS FAILED' : 'ALL TESTS PASSED');
})().catch(e => { console.error(e); process.exit(1); });
