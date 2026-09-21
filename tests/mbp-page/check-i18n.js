// Controleert de vertaalblokken van de twee MBP-secties.
//
//   node check-i18n.js
//
// Drie dingen gaan hier mis als je niet oplet, en alle drie zijn ze al
// een keer misgegaan:
//   1. Een sleutel die in een taal ontbreekt. De pagina valt dan terug op
//      de Engelse tekst die in de HTML staat, dus je ziet Engels in een
//      Nederlandse pagina zonder dat er iets stuk lijkt.
//   2. Een sleutel die er wel staat maar met de tekst van een andere taal.
//   3. Een sleutel die nergens meer gebruikt wordt (dode vertaling) of
//      een data-i18n in de markup waar geen vertaling bij hoort.

const fs = require('fs');
const path = require('path');
const os = require('os');
const { execFileSync } = require('child_process');

const FILES = ['mbp-v1.html', 'mbp-listing-v1.html'];

// Woorden die alleen in die ene taal voorkomen. Vindt een taalblok een
// woord uit een andere taal, dan is er iets door elkaar gelopen.
const MARKERS = {
  nl: [/\bje\b/i, /\bhet\b/i, /\been\b/i, /\bvan\b/i, /\bwat\b/i, /\bmet\b/i, /\bvoor\b/i],
  de: [/\bdie\b/i, /\bder\b/i, /\bdu\b/i, /\bund\b/i, /\bmit\b/i, /\bdein/i, /\bwas\b/i],
  fr: [/\bvous\b/i, /\bvotre\b/i, /\bles\b/i, /\bpour\b/i, /\bavec\b/i, /\bqui\b/i, /\bune\b/i],
  en: [/\byour\b/i, /\bthe\b/i, /\bwith\b/i, /\bwhat\b/i, /\bevery\b/i, /\byou\b/i],
};

let failures = 0;
function check(name, ok, extra) {
  console.log((ok ? '  ok   ' : '  FOUT ') + name + (ok || extra === undefined ? '' : '  -> ' + extra));
  if (!ok) failures++;
}

// Haalt de vier taalblokken uit een sectiebestand.
function blocks(src) {
  const out = {};
  for (const lang of ['en', 'nl', 'de', 'fr']) {
    const start = src.indexOf('\n    ' + lang + ': {');
    if (start < 0) continue;
    const end = src.indexOf('\n    }', start);
    out[lang] = src.slice(start, end);
  }
  return out;
}

// Alle sleutels in een blok, met hun tekst. Waarden over meerdere regels
// komen hier niet voor, alles staat op een regel.
function keys(block) {
  const out = {};
  const re = /[\n,]\s*(\w+): '((?:[^'\\]|\\.)*)'/g;
  let m;
  while ((m = re.exec(block))) out[m[1]] = m[2];
  // Arrays (crit: [...]) apart, die zijn ook vertaald.
  const ar = /\n\s+(\w+): \[([\s\S]*?)\]/g;
  while ((m = ar.exec(block))) out[m[1]] = m[2].replace(/\s+/g, ' ');
  return out;
}

// Woorden die overal hetzelfde blijven en dus niets zeggen over de taal:
// merknamen, vaktermen, en korte labels.
const NEUTRAL = /^(Master Balloon Professional|Sempertex|MBP|Instagram|Facebook|TikTok|Website|Europe|Europa|Link-O-Loon)/i;

for (const file of FILES) {
  const src = fs.readFileSync(path.resolve(__dirname, '../../sections/', file), 'utf8');
  console.log('\n=== ' + file + ' ===');

  // Eerst of het script überhaupt nog draait. Een sleutel weghalen met een
  // regex laat makkelijk een losse rest of een verdwenen komma achter, en
  // dan is de hele sectie stuk zonder dat de vertalingen iets laten zien.
  const js = [...src.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)]
    .map((m) => m[1]).join('\n');
  const tmp = path.join(os.tmpdir(), 'stx-i18n-check.js');
  fs.writeFileSync(tmp, js);
  let syntax = '';
  try { execFileSync('node', ['--check', tmp], { stdio: 'pipe' }); }
  catch (e) { syntax = String(e.stderr || e).split('\n').slice(0, 3).join(' ').trim(); }
  fs.unlinkSync(tmp);
  check('het script is geldige JavaScript', syntax === '', syntax);

  const b = blocks(src);
  check('vier taalblokken', Object.keys(b).length === 4, Object.keys(b).join(','));
  if (Object.keys(b).length !== 4) continue;

  const k = {};
  for (const lang of ['en', 'nl', 'de', 'fr']) k[lang] = keys(b[lang]);

  // 1. Elke taal heeft dezelfde sleutels als het Engels.
  const enKeys = Object.keys(k.en).sort();
  for (const lang of ['nl', 'de', 'fr']) {
    const mine = Object.keys(k[lang]).sort();
    const missing = enKeys.filter((x) => mine.indexOf(x) === -1);
    const extra = mine.filter((x) => enKeys.indexOf(x) === -1);
    check(lang + ' heeft alle ' + enKeys.length + ' sleutels',
      missing.length === 0 && extra.length === 0,
      (missing.length ? 'mist: ' + missing.join(', ') : '') +
      (extra.length ? ' te veel: ' + extra.join(', ') : ''));
  }

  // 2. Geen dubbele sleutels binnen een blok.
  for (const lang of ['en', 'nl', 'de', 'fr']) {
    const names = [...b[lang].matchAll(/[\n,]\s*(\w+):/g)].map((m) => m[1]);
    const dup = names.filter((x, i) => names.indexOf(x) !== i);
    check(lang + ' heeft geen dubbele sleutels', dup.length === 0, [...new Set(dup)].join(', '));
  }

  // 3. Geen tekst uit een andere taal in een blok.
  for (const lang of ['en', 'nl', 'de', 'fr']) {
    const wrong = [];
    for (const [key, val] of Object.entries(k[lang])) {
      const plain = String(val).replace(/<[^>]+>/g, ' ');
      if (plain.length < 12 || NEUTRAL.test(plain.trim())) continue;
      for (const other of ['en', 'nl', 'de', 'fr']) {
        if (other === lang) continue;
        const hitsOther = MARKERS[other].filter((r) => r.test(plain)).length;
        const hitsOwn = MARKERS[lang].filter((r) => r.test(plain)).length;
        // Pas een fout als de andere taal duidelijk wint.
        if (hitsOther >= 2 && hitsOther > hitsOwn) {
          wrong.push(key + ' lijkt ' + other + ': "' + plain.slice(0, 60).trim() + '"');
        }
      }
    }
    check(lang + ' bevat geen tekst uit een andere taal', wrong.length === 0, wrong.slice(0, 4).join(' | '));
  }

  // 4. Elke data-i18n in de markup heeft een vertaling, en omgekeerd.
  const used = [...src.matchAll(/data-i18n(?:-ph)?="([\w]+)"/g)].map((m) => m[1]);
  const uniqUsed = [...new Set(used)];
  const noTrans = uniqUsed.filter((x) => !(x in k.en));
  check('elke data-i18n heeft een Engelse vertaling', noTrans.length === 0, noTrans.join(', '));

  // Sleutels die het script zelf gebruikt (fill(), S.xxx) tellen ook mee.
  // Ook geneste sleutels meetellen: S.links.f gebruikt links en f.
  const inCode = [...src.matchAll(/\bS\.(\w+)(?:\.(\w+))?/g)]
    .flatMap((m) => [m[1], m[2]]).filter(Boolean);
  const alive = new Set([...uniqUsed, ...inCode]);
  const dead = enKeys.filter((x) => !alive.has(x));
  check('geen dode vertalingen', dead.length === 0, dead.join(', '));
}

console.log(failures === 0 ? '\nAlle vertalingen in orde.\n' : `\n${failures} controle(s) mislukt.\n`);
process.exit(failures === 0 ? 0 : 1);
