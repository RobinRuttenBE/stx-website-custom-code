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

**Op `/partner/liragram/tools`:** onze header, menu, footer en zijmenu zijn weg, de
kostprijscalculator en de Colour Matching Tool ook. Het logo van Liragram staat er als
data-URI (geen hotlink naar hun server), hun kleur, hun font en hun tabtitel en favicon staan
op de pagina, de teksten van de calculator staan in het Spaans, de Sempertex winkelmandknop is
weg en het bestelblok toont de twee gekozen kleurcodes met een knop naar hun eigen shop. De
pagina staat op `noindex`. Er staat geen zichtbare link terug naar onze site, en het woord
Sempertex komt alleen voor op de twee plekken waar het hoort: hun bestelknop en de creditregel
in de footer. Het laadscherm gaat precies een keer weg, pas nadat beide secties binnen zijn.

**Mobiel (390px):** het bestelblok staat er en er is geen horizontale scroll.

**Op `/tools`:** de gewone Sempertex pagina verandert niet. Header, footer, zijmenu en tabtitel
blijven staan, er komt geen partnerheader of bestelblok bij en de teksten blijven Nederlands.

**Op `/partner/onbekend/tools`:** een slug die niet in PARTNERS staat krijgt geen halve
partnerpagina; de calculator draait daar gewoon.

## Screenshots

`partner-desktop.png` en `partner-mobile.png` worden bij elke run overschreven (gitignored).
