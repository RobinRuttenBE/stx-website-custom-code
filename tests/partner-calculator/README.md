# Test harness: partner-calculator

Draait `sections/partner-calculator-v1.html` samen met `sections/inspiration-v18.html` en
`sections/partner-head-antiflash.html` tegen een nagebouwde Odoo-pagina (header, menu, `#wrap`,
footer) op het echte pad `/partner/liragram/tools`, zonder verbinding met de live site.
De loader wijst naar de lokale `sections/` map, dus dit test wat er in deze repo staat.

```
node test.js
```

Playwright komt uit `stx-tools/node_modules` (of zet `STX_PLAYWRIGHT` naar een ander pad).

## Wat het controleert

**Op `/partner/liragram/tools`:** onze header, menu, footer, zijmenu en de livechat
rechtsonder zijn weg, de
kostprijscalculator en de Colour Matching Tool ook. Het logo van Liragram staat er als
data-URI (geen hotlink naar hun server), hun kleur, hun font en hun tabtitel en favicon staan
op de pagina, de teksten van de calculator staan in het Spaans, de Sempertex winkelmandknop is
weg en het bestelblok toont de twee gekozen kleurcodes met een knop naar hun eigen shop. De
pagina staat op `noindex`. Er is geen kopieerknop meer en elke link naar Liragram (logo,
"Volver a la tienda", bestelknop, maatknoppen) opent een nieuw tabblad, zodat de calculator
openblijft. Er staat geen zichtbare link terug naar onze site, en het woord
Sempertex komt alleen voor op de twee plekken waar het hoort: hun bestelknop en de creditregel
in de footer. Het laadscherm gaat precies een keer weg, pas nadat beide secties binnen zijn.

**Mobiel (390px):** het bestelblok staat er en er is geen horizontale scroll.

**Met `?livechat=force`:** de harness mount de livechat dan toch, ook al staat
`can_load_livechat` uit. Dat test het CSS-vangnet apart: de host is verborgen en de knop in de
shadow root heeft geen plek meer op de pagina. Odoo bouwt de chat namelijk in een eigen
host-element met een shadow root en een id dat per pageload verandert, dus de host verbergen is
het enige wat van buitenaf werkt.

**Op `/tools`:** de gewone Sempertex pagina verandert niet. Header, footer, zijmenu, livechat en
tabtitel blijven staan, er komt geen partnerheader of bestelblok bij en de teksten blijven
Nederlands.

**Op `/partner/onbekend/tools`:** een slug die niet in PARTNERS staat krijgt geen halve
partnerpagina; de calculator draait daar gewoon.

## Screenshots

`partner-desktop.png` en `partner-mobile.png` worden bij elke run overschreven (gitignored).
