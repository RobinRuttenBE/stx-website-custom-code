# -*- coding: utf-8 -*-
"""Topic: 'How to make a balloon garland: step by step for beginners' (ballonslinger).
(sempertexeurope.com/en_GB/blog/how-to-make-a-balloon-garland).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=garland.
Uit de blog: één handeling, steeds herhaald. 3 maten: R12 (12 inch) als basis, R5 (5 inch) voor de gaten, een paar R18
(18 inch) als accent. Kern: stevig touw of sierdraad, 0,5 m extra aan elk uiteinde. Gereedschap: inflator of handpomp,
sizer, schaar, stevige haken, glue dots. 3 of 4 kleuren: één voor de helft, een tweede voor een derde, rest accent.
Fashion = dekkende basis, Pastel Matte = krijtachtig, Pastel Dusk = doffer en warmer, Silk/Reflex voor glans.
Stap 1 alleen het ronde deel opblazen, nek leeg, door de sizer (0,5 cm verschil zie je), in blokken werken, geen helium.
Stap 2 duplets: 2 ballonnen van dezelfde maat nek aan nek, 1 knoop per paar. Stap 3 touw plat, duplet één keer om het
touw, kwartslag t.o.v. de vorige, strak tegen elkaar, R18 verdelen, nooit 2 dezelfde naast elkaar, 3 stappen terug.
Stap 4 gaten vullen met R5, losjes geknoopt, glue dot, knoop naar binnen (meest overgeslagen, grootste winst).
Stap 5 accent: 1, hoogstens 2 (folieballon, bloemen), met glue dots. Stap 6 haken eerst, dan slinger; licht = zelfklevend,
zwaar = stevige haken of frame; midden laten doorhangen als een waslijn. Fouten: op gevoel opblazen, te weinig kopen,
gaten overslaan (R5's = helft van het resultaat). Houdbaar: binnen enkele dagen tot een week, buiten korter. FAQ: hoeveel
(hangt af van lengte en volheid, koop extra), welke maten (3), dag vooraf (ja, in secties, plat, ter plaatse koppelen),
helium (nee). CTA blog: Start Your Balloon Business, tweedaagse workshop. Geen kleurcodes in de blog: voorbeeldpalet
met echte codes uit het assortiment (Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027, Reflex Gold 970)."""

G = {}
def setup(g): G.update(g)
NB = " "
ROPE = "#8A7A66"

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["3 maten…", "Duplets…", "Gaten vullen…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Ballonslinger…",
    "steps_title": "Een ballonslinger in 6 stappen: 3 maten, 1 touw, duplets", "steps_lead": "Zo bouw je hem:",
    "steps": ["Blaas alleen het ronde deel op, nek leeg. Elke ballon door de sizer: een halve cm verschil zie je zodra de slinger hangt", "Knoop 2 ballonnen van dezelfde maat nek aan nek: een duplet. Eén knoop per paar", "Leg het touw plat, draai elke duplet één keer om het touw en een kwartslag verder dan de vorige. Duw ze strak tegen elkaar", "Vul de gaten met R5's, losjes geknoopt, met een glue dot en de knoop naar binnen. Dit is de helft van het resultaat", "Eén accent, hoogstens twee: een folieballon of bloemen, vast met glue dots", "Haken eerst, dan de slinger. Laat het midden doorhangen als een waslijn"],
    "steps_label": "De stappen",
    "rule1_label": "Materiaal", "rule1_title": "3 maten, 3 of 4 kleuren en een touw dat langer is dan je slinger",
    "rule1_body": "R12 is de basis en daar heb je het meeste van nodig, R5 vult de gaten, een paar R18 zijn de grote accenten. Kies 3 of 4 kleuren: één voor ongeveer de helft van de slinger, een tweede voor een derde, de rest als accent. Fashion is de dekkende basis, Pastel Matte oogt krijtachtig, Pastel Dusk iets doffer en warmer. Wil je glans, meng dan een paar Silk of Reflex ballonnen tussen de matte. Verder: een stevig touw of sierdraad, een inflator of handpomp, een sizer, een schaar, stevige haken en glue dots. Geen helium: de slinger hangt aan een muur of frame en gewone lucht houdt langer zijn vorm.",
    "rule1_facts": [["3", "maten: R12 als basis, R5 voor de gaten, R18 als accent"], ["1/2 + 1/3", "van de slinger in kleur 1 en kleur 2, de rest is accent"], ["0,5 m", "touw extra aan elk uiteinde, voor de haken"], ["0", "helium: gewone lucht houdt zijn vorm langer"]],
    "rule2_label": "Fouten", "rule2_title": "De 3 beginnersfouten en 2 vragen die elke klant stelt",
    "rule2_body": "De fouten zitten zelden in het knopen. Ze zitten hier:",
    "alts": [["Op gevoel opblazen", "zonder sizer verschillen je ballonnen een halve cm, en dat zie je zodra de slinger hangt."], ["Te weinig kopen", "halverwege zonder ballonnen zitten is dé klassieker. Koop ruim, er knapt er altijd één."], ["De gaten overslaan", "de R5's maken ongeveer de helft van het resultaat. Gebruik er veel."], ["Een dag vooraf maken?", "ja, met goed latex. Bouw in secties, leg ze plat zonder iets erop en knoop de touwen ter plaatse aan elkaar."], ["Hoe lang blijft hij goed?", "binnen enkele dagen tot een week, buiten korter door zon en warmte. Sempertex latex is 100% natuurrubber zonder vulstoffen en houdt zijn lucht."]],
    "example_label": "Voorbeeld", "example_title": "Eén slinger, twee paletten",
    "ex_items": [["Mat met 1 glansaccent", "R12 in Pastel Dusk Rose 110 (helft) en White Sand 071 (derde), R5 in Eucalyptus 027 voor de gaten, R18 in Reflex Gold 970 als accent."], ["Uit het rek van je distri", "R12 in {p0} (helft) en {p1} (derde), R5 in {p2} voor de gaten, R18 in {p3} als accent."]],
    "example_body": "Zelfde bouw, ander palet. Nooit twee dezelfde ballonnen naast elkaar, verdeel de R18's over de hele lengte en stap af en toe drie stappen terug om te kijken.",
    "client_label": "Klant vraagt", "client_title": "Wat je antwoordt als een klant vraagt",
    "client_answers": [
        "Dat hangt af van de lengte en van hoe vol je hem wilt. Werk in blokken: blaas een reeks op, knoop ze, hang ze aan het touw en meet hoeveel dat gaf. Koop altijd een paar extra, er knapt er altijd één en net te kort komen voor de laatste gaten is zonde.",
        "Ja, met goed latex. Bouw hem in secties, leg die plat zonder iets erop en knoop de touwen ter plaatse aan elkaar. Binnen houdt een Sempertex ballon enkele dagen tot een week zijn vorm.",
        "Nee. Een slinger hangt aan een muur of frame en zit vol gewone lucht. Dat is goedkoper en houdt zijn vorm langer dan helium.",
    ],
    "avoid_lead": "Je eerste slinger, in 5 stappen:",
    "steps5": ["Meet de ophangplek, kies vol of luchtig, koop ruim", "Blaas per blok op, elke ballon door de sizer, nek leeg", "Duplets om het touw, elke keer een kwartslag verder", "R5's in elk gat met een glue dot, knoop naar binnen", "Haken eerst, dan ophangen met een doorhangend midden"],
    "client_body": "Wil je dit met je handen leren? Start Your Balloon Business is de tweedaagse workshop van Sempertex Europe: technieken, materiaalkennis en de basis van je business.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex slinger:", "s3_cover_b": "op gevoel", "s3_cover_c": "vs.", "s3_cover_d": "met sizer",
    "s3_left": "OP GEVOEL", "s3_right": "MET SIZER", "s3_left_meta": "0,5 cm verschil, gaten", "s3_right_meta": "R5 in elk gat",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Op gevoel", "Te weinig gekocht", "Gaten open"], "s3_new_tags": ["Sizer", "Ruim gekocht", "R5 in elk gat", "Kwartslag"],
    "s3_new_quote": "“Elke ballon door de sizer, duplets een kwartslag gedraaid, R5 in elk gat. De slinger oogt vol en het touw is weg.”", "s3_new_badge": "3 maten, 1 touw",
    "s3_changed_bottom": "Zelfde ballonnen, zelfde touw.\nNu zie je geen gat meer.",
    "s3_topic_lbl": "WAAROM", "s3_rule1_topic": "Materiaal", "s3_rule1_old": "Eén maat is genoeg",
    "s3_rule1_quote": "“R12 als basis, R5 voor de gaten, R18 als accent. Drie maten, en de slinger oogt vol.”",
    "s3_rule2_topic": "Fouten", "s3_rule2_old": "Die gaten vallen niet op",
    "s3_rule2_quote": "“De R5's zijn de helft van het resultaat. Vul elk gat, met een glue dot en de knoop naar binnen.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_topic": "Twee paletten", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 en Reflex Gold 970, of {p0}, {p1}, {p2} en {p3} uit het rek.”",
    "s3_client_lbl": "KLANT", "s3_client_topic": "Eerste slinger",
    "s3_client_quote": "“Meten, ruim kopen, sizer, duplets, R5's, haken eerst. Eén avond, één slinger.”",
    "s3_cta_kicker": "3 maten, 1 touw, 1 avond",
    "base_lbl": "basis", "gap_lbl": "gaten", "accent_lbl": "accent", "gaps_stamp": "gaten", "full_stamp": "vol", "sizes_stamp": "3 maten", "chips": ["R12 · R5 · R18", "kwartslag", "glue dots"],
},
"en": {
    "cover_pills": ["3 sizes…", "Duplets…", "Fill the gaps…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Balloon garland…",
    "steps_title": "A balloon garland in 6 steps: 3 sizes, 1 rope, duplets", "steps_lead": "This is how you build it:",
    "steps": ["Inflate only the round part, keep the neck empty. Every balloon through the sizer: half a cm of difference shows once the garland hangs", "Tie 2 balloons of the same size neck to neck: a duplet. One knot per pair", "Lay the rope flat, twist each duplet once around it and a quarter turn past the previous one. Push them tight together", "Fill the gaps with R5s, tied loosely, with a glue dot and the knot turned inward. This is half the result", "One accent, two at most: a foil balloon or flowers, fixed with glue dots", "Hooks first, then the garland. Let the middle sag like a washing line"],
    "steps_label": "The steps",
    "rule1_label": "Materials", "rule1_title": "3 sizes, 3 or 4 colours and a rope longer than your garland",
    "rule1_body": "R12 is the base and the size you need most of, R5 fills the gaps, a few R18 are the big accents. Pick 3 or 4 colours: one for about half the garland, a second for a third, the rest as accent. Fashion is the opaque base, Pastel Matte looks chalky, Pastel Dusk a little duller and warmer. For shine, mix a few Silk or Reflex balloons in among the matte ones. Also: a sturdy rope or decorative wire, an inflator or hand pump, a sizer, scissors, sturdy hooks and glue dots. No helium: the garland hangs on a wall or frame and plain air holds its shape longer.",
    "rule1_facts": [["3", "sizes: R12 as base, R5 for the gaps, R18 as accent"], ["1/2 + 1/3", "of the garland in colour 1 and colour 2, the rest is accent"], ["0.5 m", "of extra rope at each end, for the hooks"], ["0", "helium: plain air holds its shape longer"]],
    "rule2_label": "Mistakes", "rule2_title": "The 3 first-timer mistakes and 2 questions every client asks",
    "rule2_body": "The mistakes are rarely in the tying. They sit here:",
    "alts": [["Inflating by feel", "without a sizer your balloons vary by half a cm, and you see it as soon as the garland hangs."], ["Buying too few", "running out halfway is the classic. Buy generously, one always pops."], ["Skipping the gaps", "the R5s make up about half the result. Use plenty."], ["Make it a day ahead?", "yes, with good latex. Build in sections, lay them flat with nothing on top and tie the ropes together on site."], ["How long does it last?", "indoors a few days to a week, outdoors less because of sun and heat. Sempertex latex is 100% natural rubber with no fillers and holds its air."]],
    "example_label": "Example", "example_title": "One garland, two palettes",
    "ex_items": [["Matte with 1 shiny accent", "R12 in Pastel Dusk Rose 110 (half) and White Sand 071 (a third), R5 in Eucalyptus 027 for the gaps, R18 in Reflex Gold 970 as accent."], ["From your distributor's shelf", "R12 in {p0} (half) and {p1} (a third), R5 in {p2} for the gaps, R18 in {p3} as accent."]],
    "example_body": "Same build, different palette. Never two identical balloons side by side, spread the R18s along the full length and step back three steps now and then to look.",
    "client_label": "Client asks", "client_title": "What you answer when a client asks",
    "client_answers": [
        "That depends on the length and on how full you want it. Work in blocks: inflate a series, tie them, put them on the rope and measure what that gave you. Always buy a few extra, one always pops and coming up just short for the last gaps is a shame.",
        "Yes, with good latex. Build it in sections, lay them flat with nothing on top and tie the ropes together on site. Indoors a Sempertex balloon holds its shape for a few days to a week.",
        "No. A garland hangs on a wall or frame and is filled with plain air. That is cheaper and holds its shape longer than helium.",
    ],
    "avoid_lead": "Your first garland, in 5 steps:",
    "steps5": ["Measure the hanging spot, choose full or airy, buy generously", "Inflate per block, every balloon through the sizer, neck empty", "Duplets around the rope, a quarter turn further each time", "R5s in every gap with a glue dot, knot turned inward", "Hooks first, then hang it with a sagging middle"],
    "client_body": "Want to learn this hands-on? Start Your Balloon Business is Sempertex Europe's two-day workshop: techniques, material knowledge and the basics of your business.",
    "cta_label": "Order",
    "s3_cover_a": "Sempertex garland:", "s3_cover_b": "by feel", "s3_cover_c": "vs.", "s3_cover_d": "with a sizer",
    "s3_left": "BY FEEL", "s3_right": "WITH A SIZER", "s3_left_meta": "0.5 cm off, gaps", "s3_right_meta": "R5 in every gap",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["By feel", "Bought too few", "Gaps open"], "s3_new_tags": ["Sizer", "Bought extra", "R5 in every gap", "Quarter turn"],
    "s3_new_quote": "“Every balloon through the sizer, duplets a quarter turn apart, R5 in every gap. The garland looks full and the rope is gone.”", "s3_new_badge": "3 sizes, 1 rope",
    "s3_changed_bottom": "Same balloons, same rope.\nNow you can't see a gap.",
    "s3_topic_lbl": "WHY", "s3_rule1_topic": "Materials", "s3_rule1_old": "One size is enough",
    "s3_rule1_quote": "“R12 as base, R5 for the gaps, R18 as accent. Three sizes, and the garland looks full.”",
    "s3_rule2_topic": "Mistakes", "s3_rule2_old": "Nobody notices those gaps",
    "s3_rule2_quote": "“The R5s are half the result. Fill every gap, with a glue dot and the knot turned inward.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_topic": "Two palettes", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 and Reflex Gold 970, or {p0}, {p1}, {p2} and {p3} from the shelf.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "First garland",
    "s3_client_quote": "“Measure, buy extra, sizer, duplets, R5s, hooks first. One evening, one garland.”",
    "s3_cta_kicker": "3 sizes, 1 rope, 1 evening",
    "base_lbl": "base", "gap_lbl": "gaps", "accent_lbl": "accent", "gaps_stamp": "gaps", "full_stamp": "full", "sizes_stamp": "3 sizes", "chips": ["R12 · R5 · R18", "quarter turn", "glue dots"],
},
"de": {
    "cover_pills": ["3 Größen…", "Duplets…", "Lücken füllen…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Ballongirlande…",
    "steps_title": "Eine Ballongirlande in 6 Schritten: 3 Größen, 1 Seil, Duplets", "steps_lead": "So baust du sie:",
    "steps": ["Nur den runden Teil aufblasen, Hals leer lassen. Jeden Ballon durch den Sizer: ein halber cm Unterschied ist sichtbar, sobald die Girlande hängt", "2 Ballons derselben Größe Hals an Hals knoten: ein Duplet. Ein Knoten pro Paar", "Seil flach auslegen, jedes Duplet einmal ums Seil drehen und eine Vierteldrehung weiter als das vorige. Fest aneinanderschieben", "Lücken mit R5 füllen, locker geknotet, mit Glue Dot und Knoten nach innen. Das ist die Hälfte des Ergebnisses", "Ein Akzent, höchstens zwei: ein Folienballon oder Blumen, mit Glue Dots befestigt", "Erst die Haken, dann die Girlande. Die Mitte durchhängen lassen wie eine Wäscheleine"],
    "steps_label": "Die Schritte",
    "rule1_label": "Material", "rule1_title": "3 Größen, 3 oder 4 Farben und ein Seil, das länger ist als die Girlande",
    "rule1_body": "R12 ist die Basis und davon brauchst du am meisten, R5 füllt die Lücken, ein paar R18 sind die großen Akzente. Wähl 3 oder 4 Farben: eine für etwa die Hälfte der Girlande, eine zweite für ein Drittel, der Rest als Akzent. Fashion ist die deckende Basis, Pastel Matte wirkt kreidig, Pastel Dusk etwas gedeckter und wärmer. Für Glanz mischst du ein paar Silk- oder Reflex-Ballons unter die matten. Dazu: ein stabiles Seil oder Dekodraht, ein Inflator oder eine Handpumpe, ein Sizer, eine Schere, stabile Haken und Glue Dots. Kein Helium: die Girlande hängt an Wand oder Rahmen, und normale Luft hält die Form länger.",
    "rule1_facts": [["3", "Größen: R12 als Basis, R5 für die Lücken, R18 als Akzent"], ["1/2 + 1/3", "der Girlande in Farbe 1 und Farbe 2, der Rest ist Akzent"], ["0,5 m", "Seil extra an jedem Ende, für die Haken"], ["0", "Helium: normale Luft hält die Form länger"]],
    "rule2_label": "Fehler", "rule2_title": "Die 3 Anfängerfehler und 2 Fragen, die jeder Kunde stellt",
    "rule2_body": "Die Fehler stecken selten im Knoten. Sie stecken hier:",
    "alts": [["Nach Gefühl aufblasen", "ohne Sizer unterscheiden sich die Ballons um einen halben cm, und das siehst du, sobald die Girlande hängt."], ["Zu wenig kaufen", "auf halber Strecke ohne Ballons dazustehen ist der Klassiker. Kauf großzügig, einer platzt immer."], ["Die Lücken auslassen", "die R5 machen etwa die Hälfte des Ergebnisses aus. Nimm viele."], ["Einen Tag vorher bauen?", "ja, mit gutem Latex. In Abschnitten bauen, flach hinlegen ohne etwas darauf und die Seile vor Ort verknoten."], ["Wie lange hält sie?", "drinnen ein paar Tage bis eine Woche, draußen kürzer wegen Sonne und Hitze. Sempertex Latex ist 100% Naturkautschuk ohne Füllstoffe und hält die Luft."]],
    "example_label": "Beispiel", "example_title": "Eine Girlande, zwei Paletten",
    "ex_items": [["Matt mit 1 Glanzakzent", "R12 in Pastel Dusk Rose 110 (Hälfte) und White Sand 071 (Drittel), R5 in Eucalyptus 027 für die Lücken, R18 in Reflex Gold 970 als Akzent."], ["Aus dem Regal deines Händlers", "R12 in {p0} (Hälfte) und {p1} (Drittel), R5 in {p2} für die Lücken, R18 in {p3} als Akzent."]],
    "example_body": "Gleicher Aufbau, andere Palette. Nie zwei gleiche Ballons nebeneinander, die R18 über die ganze Länge verteilen und ab und zu drei Schritte zurücktreten.",
    "client_label": "Kunde fragt", "client_title": "Was du antwortest, wenn ein Kunde fragt",
    "client_answers": [
        "Das hängt von der Länge ab und davon, wie voll sie werden soll. Arbeite in Blöcken: eine Serie aufblasen, knoten, aufs Seil setzen und messen, wie viel das ergab. Kauf immer ein paar extra, einer platzt immer, und für die letzten Lücken knapp zu kurz zu kommen ist schade.",
        "Ja, mit gutem Latex. Bau sie in Abschnitten, leg die flach hin ohne etwas darauf und verknote die Seile vor Ort. Drinnen hält ein Sempertex Ballon ein paar Tage bis eine Woche seine Form.",
        "Nein. Eine Girlande hängt an Wand oder Rahmen und ist mit normaler Luft gefüllt. Das ist günstiger und hält die Form länger als Helium.",
    ],
    "avoid_lead": "Deine erste Girlande, in 5 Schritten:",
    "steps5": ["Aufhängeplatz messen, voll oder luftig wählen, großzügig kaufen", "Blockweise aufblasen, jeden Ballon durch den Sizer, Hals leer", "Duplets ums Seil, jedes Mal eine Vierteldrehung weiter", "R5 in jede Lücke mit Glue Dot, Knoten nach innen", "Erst die Haken, dann aufhängen mit durchhängender Mitte"],
    "client_body": "Willst du das mit den Händen lernen? Start Your Balloon Business ist der zweitägige Workshop von Sempertex Europe: Techniken, Materialwissen und die Basis deines Business.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex Girlande:", "s3_cover_b": "nach Gefühl", "s3_cover_c": "vs.", "s3_cover_d": "mit Sizer",
    "s3_left": "NACH GEFÜHL", "s3_right": "MIT SIZER", "s3_left_meta": "0,5 cm Abstand, Lücken", "s3_right_meta": "R5 in jeder Lücke",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Nach Gefühl", "Zu wenig gekauft", "Lücken offen"], "s3_new_tags": ["Sizer", "Extra gekauft", "R5 in jeder Lücke", "Vierteldrehung"],
    "s3_new_quote": "“Jeder Ballon durch den Sizer, Duplets um eine Vierteldrehung versetzt, R5 in jeder Lücke. Die Girlande wirkt voll und das Seil ist weg.”", "s3_new_badge": "3 Größen, 1 Seil",
    "s3_changed_bottom": "Dieselben Ballons, dasselbe Seil.\nJetzt siehst du keine Lücke mehr.",
    "s3_topic_lbl": "WARUM", "s3_rule1_topic": "Material", "s3_rule1_old": "Eine Größe reicht",
    "s3_rule1_quote": "“R12 als Basis, R5 für die Lücken, R18 als Akzent. Drei Größen, und die Girlande wirkt voll.”",
    "s3_rule2_topic": "Fehler", "s3_rule2_old": "Die Lücken fallen nicht auf",
    "s3_rule2_quote": "“Die R5 sind die Hälfte des Ergebnisses. Füll jede Lücke, mit Glue Dot und Knoten nach innen.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_topic": "Zwei Paletten", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 und Reflex Gold 970, oder {p0}, {p1}, {p2} und {p3} aus dem Regal.”",
    "s3_client_lbl": "KUNDE", "s3_client_topic": "Erste Girlande",
    "s3_client_quote": "“Messen, großzügig kaufen, Sizer, Duplets, R5, erst die Haken. Ein Abend, eine Girlande.”",
    "s3_cta_kicker": "3 Größen, 1 Seil, 1 Abend",
    "base_lbl": "Basis", "gap_lbl": "Lücken", "accent_lbl": "Akzent", "gaps_stamp": "Lücken", "full_stamp": "voll", "sizes_stamp": "3 Größen", "chips": ["R12 · R5 · R18", "Vierteldrehung", "Glue Dots"],
},
"fr": {
    "cover_pills": ["3 tailles…", "Duplets…", "Combler les trous…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Guirlande de ballons…",
    "steps_title": "Une guirlande de ballons en 6 étapes : 3 tailles, 1 corde, des duplets", "steps_lead": "Voilà comment la monter :",
    "steps": ["Gonfle seulement la partie ronde, col vide. Chaque ballon passe par le sizer : un demi-cm d'écart se voit dès que la guirlande est accrochée", "Noue 2 ballons de la même taille col contre col : un duplet. Un nœud par paire", "Pose la corde à plat, enroule chaque duplet une fois autour et décale-le d'un quart de tour par rapport au précédent. Serre-les bien", "Comble les trous avec des R5, noués lâchement, avec un glue dot et le nœud vers l'intérieur. C'est la moitié du résultat", "Un accent, deux au plus : un ballon aluminium ou des fleurs, fixés avec des glue dots", "Les crochets d'abord, puis la guirlande. Laisse le milieu pendre comme une corde à linge"],
    "steps_label": "Les étapes",
    "rule1_label": "Matériel", "rule1_title": "3 tailles, 3 ou 4 couleurs et une corde plus longue que la guirlande",
    "rule1_body": "Le R12 est la base, c'est celui qu'il te faut le plus, le R5 comble les trous, quelques R18 font les grands accents. Choisis 3 ou 4 couleurs : une pour environ la moitié de la guirlande, une deuxième pour un tiers, le reste en accent. Fashion est la base opaque, Pastel Matte a un rendu crayeux, Pastel Dusk est un peu plus terne et plus chaud. Pour de la brillance, glisse quelques ballons Silk ou Reflex parmi les mats. Et aussi : une corde solide ou un fil déco, un gonfleur ou une pompe à main, un sizer, des ciseaux, des crochets solides et des glue dots. Pas d'hélium : la guirlande se fixe à un mur ou à un cadre, et l'air ordinaire garde sa forme plus longtemps.",
    "rule1_facts": [["3", "tailles : R12 en base, R5 pour les trous, R18 en accent"], ["1/2 + 1/3", "de la guirlande en couleur 1 et couleur 2, le reste en accent"], ["0,5 m", "de corde en plus à chaque bout, pour les crochets"], ["0", "hélium : l'air ordinaire garde sa forme plus longtemps"]],
    "rule2_label": "Erreurs", "rule2_title": "Les 3 erreurs de débutant et 2 questions que chaque client pose",
    "rule2_body": "Les erreurs sont rarement dans le nouage. Elles sont ici :",
    "alts": [["Gonfler au jugé", "sans sizer, tes ballons varient d'un demi-cm, et ça se voit dès que la guirlande est accrochée."], ["Acheter trop peu", "se retrouver sans ballons à mi-chemin, c'est le classique. Achète large, il y en a toujours un qui éclate."], ["Sauter les trous", "les R5 font environ la moitié du résultat. Mets-en beaucoup."], ["La faire la veille ?", "oui, avec du bon latex. Monte-la par sections, pose-les à plat sans rien dessus et noue les cordes sur place."], ["Elle tient combien de temps ?", "à l'intérieur quelques jours à une semaine, dehors moins à cause du soleil et de la chaleur. Le latex Sempertex est du caoutchouc 100% naturel sans charges et garde son air."]],
    "example_label": "Exemple", "example_title": "Une guirlande, deux palettes",
    "ex_items": [["Mat avec 1 accent brillant", "R12 en Pastel Dusk Rose 110 (moitié) et White Sand 071 (tiers), R5 en Eucalyptus 027 pour les trous, R18 en Reflex Gold 970 en accent."], ["Depuis l'étagère de ton distributeur", "R12 en {p0} (moitié) et {p1} (tiers), R5 en {p2} pour les trous, R18 en {p3} en accent."]],
    "example_body": "Même montage, autre palette. Jamais deux ballons identiques côte à côte, répartis les R18 sur toute la longueur et recule de trois pas de temps en temps pour regarder.",
    "client_label": "Un client demande", "client_title": "Ce que tu réponds quand un client demande",
    "client_answers": [
        "Ça dépend de la longueur et de la densité voulue. Travaille par blocs : gonfle une série, noue-la, mets-la sur la corde et mesure ce que ça a donné. Achète toujours quelques ballons en plus, il y en a toujours un qui éclate et manquer de peu pour les derniers trous, c'est dommage.",
        "Oui, avec du bon latex. Monte-la par sections, pose-les à plat sans rien dessus et noue les cordes sur place. À l'intérieur, un ballon Sempertex garde sa forme quelques jours à une semaine.",
        "Non. Une guirlande se fixe à un mur ou à un cadre et se gonfle à l'air ordinaire. C'est moins cher et ça garde sa forme plus longtemps que l'hélium.",
    ],
    "avoid_lead": "Ta première guirlande, en 5 étapes :",
    "steps5": ["Mesure l'emplacement, choisis dense ou aérée, achète large", "Gonfle par blocs, chaque ballon par le sizer, col vide", "Duplets autour de la corde, un quart de tour de plus à chaque fois", "Des R5 dans chaque trou avec un glue dot, nœud vers l'intérieur", "Les crochets d'abord, puis accroche avec le milieu qui pend"],
    "client_body": "Tu veux l'apprendre avec les mains ? Start Your Balloon Business est l'atelier de deux jours de Sempertex Europe : techniques, connaissance du matériel et bases de ton activité.",
    "cta_label": "Commander",
    "s3_cover_a": "Guirlande Sempertex :", "s3_cover_b": "au jugé", "s3_cover_c": "vs.", "s3_cover_d": "avec sizer",
    "s3_left": "AU JUGÉ", "s3_right": "AVEC SIZER", "s3_left_meta": "0,5 cm d'écart, trous", "s3_right_meta": "R5 dans chaque trou",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Au jugé", "Trop peu acheté", "Trous ouverts"], "s3_new_tags": ["Sizer", "Acheté large", "R5 dans chaque trou", "Quart de tour"],
    "s3_new_quote": "“Chaque ballon par le sizer, des duplets décalés d'un quart de tour, un R5 dans chaque trou. La guirlande paraît pleine et la corde a disparu.”", "s3_new_badge": "3 tailles, 1 corde",
    "s3_changed_bottom": "Mêmes ballons, même corde.\nMaintenant, plus un trou.",
    "s3_topic_lbl": "POURQUOI", "s3_rule1_topic": "Matériel", "s3_rule1_old": "Une seule taille suffit",
    "s3_rule1_quote": "“R12 en base, R5 pour les trous, R18 en accent. Trois tailles, et la guirlande paraît pleine.”",
    "s3_rule2_topic": "Erreurs", "s3_rule2_old": "Ces trous, personne ne les voit",
    "s3_rule2_quote": "“Les R5 font la moitié du résultat. Comble chaque trou, avec un glue dot et le nœud vers l'intérieur.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_topic": "Deux palettes", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 et Reflex Gold 970, ou {p0}, {p1}, {p2} et {p3} de l'étagère.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Première guirlande",
    "s3_client_quote": "“Mesurer, acheter large, sizer, duplets, R5, crochets d'abord. Une soirée, une guirlande.”",
    "s3_cta_kicker": "3 tailles, 1 corde, 1 soirée",
    "base_lbl": "base", "gap_lbl": "trous", "accent_lbl": "accent", "gaps_stamp": "trous", "full_stamp": "pleine", "sizes_stamp": "3 tailles", "chips": ["R12 · R5 · R18", "quart de tour", "glue dots"],
},
"it": {
    "cover_pills": ["3 misure…", "Duplet…", "Riempi i vuoti…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Ghirlanda di palloncini…",
    "steps_title": "Una ghirlanda di palloncini in 6 passi: 3 misure, 1 corda, duplet", "steps_lead": "Ecco come la costruisci:",
    "steps": ["Gonfia solo la parte rotonda, collo vuoto. Ogni palloncino passa dal sizer: mezzo cm di differenza si vede appena la ghirlanda è appesa", "Lega 2 palloncini della stessa misura collo a collo: un duplet. Un nodo per coppia", "Stendi la corda, gira ogni duplet una volta attorno e un quarto di giro oltre il precedente. Spingili stretti uno contro l'altro", "Riempi i vuoti con gli R5, legati morbidi, con un glue dot e il nodo verso l'interno. È metà del risultato", "Un accento, al massimo due: un palloncino foil o dei fiori, fissati con glue dot", "Prima i ganci, poi la ghirlanda. Lascia che il centro penda come un filo del bucato"],
    "steps_label": "I passi",
    "rule1_label": "Materiale", "rule1_title": "3 misure, 3 o 4 colori e una corda più lunga della ghirlanda",
    "rule1_body": "L'R12 è la base e ne servono di più, l'R5 riempie i vuoti, qualche R18 fa da accento grande. Scegli 3 o 4 colori: uno per circa metà ghirlanda, un secondo per un terzo, il resto come accento. Fashion è la base coprente, Pastel Matte ha un effetto gessoso, Pastel Dusk è un po' più spento e caldo. Per la lucentezza, mescola qualche palloncino Silk o Reflex tra quelli opachi. E poi: una corda robusta o un filo decorativo, un gonfiatore o una pompa a mano, un sizer, forbici, ganci robusti e glue dot. Niente elio: la ghirlanda sta su una parete o un telaio, e l'aria normale tiene la forma più a lungo.",
    "rule1_facts": [["3", "misure: R12 come base, R5 per i vuoti, R18 come accento"], ["1/2 + 1/3", "della ghirlanda nel colore 1 e nel colore 2, il resto è accento"], ["0,5 m", "di corda in più a ogni estremità, per i ganci"], ["0", "elio: l'aria normale tiene la forma più a lungo"]],
    "rule2_label": "Errori", "rule2_title": "I 3 errori da principiante e 2 domande che ogni cliente fa",
    "rule2_body": "Gli errori raramente stanno nel nodo. Stanno qui:",
    "alts": [["Gonfiare a occhio", "senza sizer i palloncini variano di mezzo cm, e lo vedi appena la ghirlanda è appesa."], ["Comprarne troppo pochi", "restare senza palloncini a metà è il classico. Compra abbondante, uno scoppia sempre."], ["Saltare i vuoti", "gli R5 fanno circa metà del risultato. Usane tanti."], ["Farla il giorno prima?", "sì, con un buon lattice. Costruiscila a sezioni, stendile piatte senza niente sopra e lega le corde sul posto."], ["Quanto dura?", "in interni da qualche giorno a una settimana, fuori meno per sole e caldo. Il lattice Sempertex è gomma 100% naturale senza riempitivi e tiene l'aria."]],
    "example_label": "Esempio", "example_title": "Una ghirlanda, due palette",
    "ex_items": [["Opaco con 1 accento lucido", "R12 in Pastel Dusk Rose 110 (metà) e White Sand 071 (un terzo), R5 in Eucalyptus 027 per i vuoti, R18 in Reflex Gold 970 come accento."], ["Dallo scaffale del tuo distributore", "R12 in {p0} (metà) e {p1} (un terzo), R5 in {p2} per i vuoti, R18 in {p3} come accento."]],
    "example_body": "Stessa costruzione, altra palette. Mai due palloncini uguali vicini, distribuisci gli R18 su tutta la lunghezza e ogni tanto fai tre passi indietro per guardare.",
    "client_label": "Il cliente chiede", "client_title": "Cosa rispondi quando un cliente chiede",
    "client_answers": [
        "Dipende dalla lunghezza e da quanto la vuoi piena. Lavora a blocchi: gonfia una serie, legala, mettila sulla corda e misura quanto ha reso. Compra sempre qualche palloncino in più, uno scoppia sempre e restare corto per gli ultimi vuoti è un peccato.",
        "Sì, con un buon lattice. Costruiscila a sezioni, stendile piatte senza niente sopra e lega le corde sul posto. In interni un palloncino Sempertex tiene la forma da qualche giorno a una settimana.",
        "No. Una ghirlanda sta su una parete o un telaio ed è piena di aria normale. Costa meno e tiene la forma più a lungo dell'elio.",
    ],
    "avoid_lead": "La tua prima ghirlanda, in 5 passi:",
    "steps5": ["Misura il punto in cui appenderla, scegli piena o leggera, compra abbondante", "Gonfia a blocchi, ogni palloncino dal sizer, collo vuoto", "Duplet attorno alla corda, ogni volta un quarto di giro oltre", "R5 in ogni vuoto con un glue dot, nodo verso l'interno", "Prima i ganci, poi appendi con il centro che pende"],
    "client_body": "Vuoi impararlo con le mani? Start Your Balloon Business è il workshop di due giorni di Sempertex Europe: tecniche, conoscenza dei materiali e le basi della tua attività.",
    "cta_label": "Ordina",
    "s3_cover_a": "Ghirlanda Sempertex:", "s3_cover_b": "a occhio", "s3_cover_c": "vs.", "s3_cover_d": "con il sizer",
    "s3_left": "A OCCHIO", "s3_right": "CON IL SIZER", "s3_left_meta": "0,5 cm di scarto, vuoti", "s3_right_meta": "R5 in ogni vuoto",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["A occhio", "Comprati pochi", "Vuoti aperti"], "s3_new_tags": ["Sizer", "Comprati in più", "R5 in ogni vuoto", "Quarto di giro"],
    "s3_new_quote": "“Ogni palloncino dal sizer, duplet sfalsati di un quarto di giro, R5 in ogni vuoto. La ghirlanda sembra piena e la corda è sparita.”", "s3_new_badge": "3 misure, 1 corda",
    "s3_changed_bottom": "Stessi palloncini, stessa corda.\nOra non vedi più un vuoto.",
    "s3_topic_lbl": "PERCHÉ", "s3_rule1_topic": "Materiale", "s3_rule1_old": "Una misura basta",
    "s3_rule1_quote": "“R12 come base, R5 per i vuoti, R18 come accento. Tre misure, e la ghirlanda sembra piena.”",
    "s3_rule2_topic": "Errori", "s3_rule2_old": "Quei vuoti non si notano",
    "s3_rule2_quote": "“Gli R5 sono metà del risultato. Riempi ogni vuoto, con un glue dot e il nodo verso l'interno.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_topic": "Due palette", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 e Reflex Gold 970, o {p0}, {p1}, {p2} e {p3} dallo scaffale.”",
    "s3_client_lbl": "CLIENTE", "s3_client_topic": "Prima ghirlanda",
    "s3_client_quote": "“Misurare, comprare in più, sizer, duplet, R5, prima i ganci. Una sera, una ghirlanda.”",
    "s3_cta_kicker": "3 misure, 1 corda, 1 sera",
    "base_lbl": "base", "gap_lbl": "vuoti", "accent_lbl": "accento", "gaps_stamp": "vuoti", "full_stamp": "piena", "sizes_stamp": "3 misure", "chips": ["R12 · R5 · R18", "quarto di giro", "glue dot"],
},
"pl": {
    "cover_pills": ["3 rozmiary…", "Duplety…", "Wypełnij luki…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Girlanda balonowa…",
    "steps_title": "Girlanda balonowa w 6 krokach: 3 rozmiary, 1 sznurek, duplety", "steps_lead": "Tak ją budujesz:",
    "steps": ["Pompuj tylko okrągłą część, szyjka pusta. Każdy balon przez sizer: pół cm różnicy widać, gdy girlanda wisi", "Zwiąż 2 balony tego samego rozmiaru szyjka do szyjki: duplet. Jeden węzeł na parę", "Rozłóż sznurek płasko, okręć każdy duplet raz wokół niego i o ćwierć obrotu dalej niż poprzedni. Dociśnij je mocno do siebie", "Wypełnij luki balonami R5, luźno zawiązanymi, z glue dotem i węzłem do środka. To połowa efektu", "Jeden akcent, najwyżej dwa: balon foliowy albo kwiaty, przyklejone glue dotami", "Najpierw haki, potem girlanda. Niech środek zwisa jak sznur na pranie"],
    "steps_label": "Kroki",
    "rule1_label": "Materiały", "rule1_title": "3 rozmiary, 3 lub 4 kolory i sznurek dłuższy niż girlanda",
    "rule1_body": "R12 to baza i tych potrzebujesz najwięcej, R5 wypełnia luki, kilka R18 to duże akcenty. Wybierz 3 lub 4 kolory: jeden na około połowę girlandy, drugi na jedną trzecią, reszta jako akcent. Fashion to kryjąca baza, Pastel Matte wygląda kredowo, Pastel Dusk jest trochę bardziej przygaszony i cieplejszy. Chcesz połysku, wmieszaj kilka balonów Silk albo Reflex między matowe. Do tego: mocny sznurek albo drut dekoracyjny, inflator albo pompka ręczna, sizer, nożyczki, mocne haki i glue doty. Bez helu: girlanda wisi na ścianie albo stelażu, a zwykłe powietrze trzyma kształt dłużej.",
    "rule1_facts": [["3", "rozmiary: R12 jako baza, R5 na luki, R18 jako akcent"], ["1/2 + 1/3", "girlandy w kolorze 1 i kolorze 2, reszta to akcent"], ["0,5 m", "sznurka więcej na każdym końcu, na haki"], ["0", "helu: zwykłe powietrze trzyma kształt dłużej"]],
    "rule2_label": "Błędy", "rule2_title": "3 błędy początkujących i 2 pytania, które zadaje każdy klient",
    "rule2_body": "Błędy rzadko siedzą w wiązaniu. Siedzą tutaj:",
    "alts": [["Pompowanie na oko", "bez sizera balony różnią się o pół cm, a to widać, gdy tylko girlanda wisi."], ["Za mało balonów", "zostać bez balonów w połowie to klasyk. Kup z zapasem, jeden zawsze pęka."], ["Pominięte luki", "balony R5 to około połowa efektu. Użyj ich dużo."], ["Zrobić dzień wcześniej?", "tak, z dobrym lateksem. Buduj w sekcjach, połóż je płasko bez niczego na wierzchu i zwiąż sznurki na miejscu."], ["Jak długo wytrzyma?", "w środku kilka dni do tygodnia, na zewnątrz krócej przez słońce i ciepło. Lateks Sempertex to 100% naturalny kauczuk bez wypełniaczy i trzyma powietrze."]],
    "example_label": "Przykład", "example_title": "Jedna girlanda, dwie palety",
    "ex_items": [["Mat z 1 błyszczącym akcentem", "R12 w Pastel Dusk Rose 110 (połowa) i White Sand 071 (jedna trzecia), R5 w Eucalyptus 027 na luki, R18 w Reflex Gold 970 jako akcent."], ["Z półki twojego dystrybutora", "R12 w {p0} (połowa) i {p1} (jedna trzecia), R5 w {p2} na luki, R18 w {p3} jako akcent."]],
    "example_body": "Ta sama budowa, inna paleta. Nigdy dwa takie same balony obok siebie, rozłóż R18 na całej długości i co jakiś czas cofnij się o trzy kroki, żeby spojrzeć.",
    "client_label": "Klient pyta", "client_title": "Co odpowiadasz, gdy pyta klient",
    "client_answers": [
        "To zależy od długości i od tego, jak pełna ma być. Pracuj blokami: napompuj serię, zwiąż, załóż na sznurek i zmierz, ile to dało. Zawsze kupuj kilka na zapas, jeden zawsze pęka, a zabraknięcie na ostatnie luki to szkoda.",
        "Tak, z dobrym lateksem. Zbuduj ją w sekcjach, połóż je płasko bez niczego na wierzchu i zwiąż sznurki na miejscu. W środku balon Sempertex trzyma kształt kilka dni do tygodnia.",
        "Nie. Girlanda wisi na ścianie albo stelażu i jest wypełniona zwykłym powietrzem. To tańsze i trzyma kształt dłużej niż hel.",
    ],
    "avoid_lead": "Twoja pierwsza girlanda, w 5 krokach:",
    "steps5": ["Zmierz miejsce, wybierz pełną albo lekką, kup z zapasem", "Pompuj blokami, każdy balon przez sizer, szyjka pusta", "Duplety wokół sznurka, za każdym razem ćwierć obrotu dalej", "R5 w każdą lukę z glue dotem, węzeł do środka", "Najpierw haki, potem zawieś ze zwisającym środkiem"],
    "client_body": "Chcesz nauczyć się tego rękami? Start Your Balloon Business to dwudniowy warsztat Sempertex Europe: techniki, wiedza o materiałach i podstawy twojego biznesu.",
    "cta_label": "Zamów",
    "s3_cover_a": "Girlanda Sempertex:", "s3_cover_b": "na oko", "s3_cover_c": "vs.", "s3_cover_d": "z sizerem",
    "s3_left": "NA OKO", "s3_right": "Z SIZEREM", "s3_left_meta": "0,5 cm różnicy, luki", "s3_right_meta": "R5 w każdej luce",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Na oko", "Za mało kupione", "Luki otwarte"], "s3_new_tags": ["Sizer", "Kupione z zapasem", "R5 w każdej luce", "Ćwierć obrotu"],
    "s3_new_quote": "“Każdy balon przez sizer, duplety co ćwierć obrotu, R5 w każdej luce. Girlanda wygląda na pełną, a sznurka nie widać.”", "s3_new_badge": "3 rozmiary, 1 sznurek",
    "s3_changed_bottom": "Te same balony, ten sam sznurek.\nTeraz nie widać ani jednej luki.",
    "s3_topic_lbl": "DLACZEGO", "s3_rule1_topic": "Materiały", "s3_rule1_old": "Jeden rozmiar wystarczy",
    "s3_rule1_quote": "“R12 jako baza, R5 na luki, R18 jako akcent. Trzy rozmiary i girlanda wygląda na pełną.”",
    "s3_rule2_topic": "Błędy", "s3_rule2_old": "Tych luk nikt nie zauważy",
    "s3_rule2_quote": "“Balony R5 to połowa efektu. Wypełnij każdą lukę, z glue dotem i węzłem do środka.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_topic": "Dwie palety", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 i Reflex Gold 970, albo {p0}, {p1}, {p2} i {p3} z półki.”",
    "s3_client_lbl": "KLIENT", "s3_client_topic": "Pierwsza girlanda",
    "s3_client_quote": "“Zmierzyć, kupić z zapasem, sizer, duplety, R5, najpierw haki. Jeden wieczór, jedna girlanda.”",
    "s3_cta_kicker": "3 rozmiary, 1 sznurek, 1 wieczór",
    "base_lbl": "baza", "gap_lbl": "luki", "accent_lbl": "akcent", "gaps_stamp": "luki", "full_stamp": "pełna", "sizes_stamp": "3 rozmiary", "chips": ["R12 · R5 · R18", "ćwierć obrotu", "glue doty"],
},
"el": {
    "cover_pills": ["3 μεγέθη…", "Duplets…", "Γέμισε τα κενά…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Γιρλάντα από μπαλόνια…",
    "steps_title": "Γιρλάντα από μπαλόνια σε 6 βήματα: 3 μεγέθη, 1 σχοινί, duplets", "steps_lead": "Έτσι τη φτιάχνεις:",
    "steps": ["Φούσκωσε μόνο το στρογγυλό μέρος, ο λαιμός άδειος. Κάθε μπαλόνι από το sizer: μισό εκατοστό διαφορά φαίνεται μόλις κρεμαστεί η γιρλάντα", "Δέσε 2 μπαλόνια ίδιου μεγέθους λαιμό με λαιμό: ένα duplet. Ένας κόμπος ανά ζευγάρι", "Άπλωσε το σχοινί, τύλιξε κάθε duplet μία φορά γύρω του και ένα τέταρτο στροφής πιο πέρα από το προηγούμενο. Σπρώξε τα σφιχτά το ένα στο άλλο", "Γέμισε τα κενά με R5, χαλαρά δεμένα, με glue dot και τον κόμπο προς τα μέσα. Αυτό είναι το μισό αποτέλεσμα", "Ένα accent, το πολύ δύο: ένα foil μπαλόνι ή λουλούδια, στερεωμένα με glue dots", "Πρώτα τα άγκιστρα, μετά η γιρλάντα. Άφησε τη μέση να κρεμάει σαν σχοινί απλώματος"],
    "steps_label": "Τα βήματα",
    "rule1_label": "Υλικά", "rule1_title": "3 μεγέθη, 3 ή 4 χρώματα και ένα σχοινί μακρύτερο από τη γιρλάντα",
    "rule1_body": "Το R12 είναι η βάση και από αυτό χρειάζεσαι τα περισσότερα, το R5 γεμίζει τα κενά, λίγα R18 είναι τα μεγάλα accents. Διάλεξε 3 ή 4 χρώματα: ένα για περίπου τη μισή γιρλάντα, ένα δεύτερο για το ένα τρίτο, τα υπόλοιπα ως accent. Το Fashion είναι η αδιαφανής βάση, το Pastel Matte μοιάζει κιμωλιακό, το Pastel Dusk λίγο πιο μουντό και ζεστό. Για λάμψη, ανακάτεψε λίγα Silk ή Reflex μπαλόνια ανάμεσα στα ματ. Επίσης: ένα γερό σχοινί ή διακοσμητικό σύρμα, inflator ή τρόμπα χειρός, sizer, ψαλίδι, γερά άγκιστρα και glue dots. Χωρίς ήλιο: η γιρλάντα κρέμεται σε τοίχο ή σκελετό, και ο απλός αέρας κρατάει το σχήμα περισσότερο.",
    "rule1_facts": [["3", "μεγέθη: R12 ως βάση, R5 για τα κενά, R18 ως accent"], ["1/2 + 1/3", "της γιρλάντας σε χρώμα 1 και χρώμα 2, τα υπόλοιπα accent"], ["0,5 m", "σχοινί παραπάνω σε κάθε άκρη, για τα άγκιστρα"], ["0", "ήλιο: ο απλός αέρας κρατάει το σχήμα περισσότερο"]],
    "rule2_label": "Λάθη", "rule2_title": "Τα 3 λάθη των αρχάριων και 2 ερωτήσεις που κάνει κάθε πελάτης",
    "rule2_body": "Τα λάθη σπάνια είναι στο δέσιμο. Είναι εδώ:",
    "alts": [["Φούσκωμα με το μάτι", "χωρίς sizer τα μπαλόνια διαφέρουν κατά μισό εκατοστό, και το βλέπεις μόλις κρεμαστεί η γιρλάντα."], ["Αγορά λίγων μπαλονιών", "να μείνεις χωρίς μπαλόνια στα μισά είναι το κλασικό. Αγόρασε με περίσσευμα, ένα πάντα σκάει."], ["Παράλειψη των κενών", "τα R5 είναι περίπου το μισό αποτέλεσμα. Βάλε πολλά."], ["Μία μέρα πριν;", "ναι, με καλό λάτεξ. Φτιάξε τη σε τμήματα, άπλωσέ τα επίπεδα χωρίς τίποτα από πάνω και δέσε τα σχοινιά επιτόπου."], ["Πόσο κρατάει;", "μέσα λίγες μέρες έως μία εβδομάδα, έξω λιγότερο λόγω ήλιου και ζέστης. Το λάτεξ Sempertex είναι 100% φυσικό καουτσούκ χωρίς πρόσθετα και κρατάει τον αέρα."]],
    "example_label": "Παράδειγμα", "example_title": "Μία γιρλάντα, δύο παλέτες",
    "ex_items": [["Ματ με 1 γυαλιστερό accent", "R12 σε Pastel Dusk Rose 110 (μισό) και White Sand 071 (ένα τρίτο), R5 σε Eucalyptus 027 για τα κενά, R18 σε Reflex Gold 970 ως accent."], ["Από το ράφι του διανομέα σου", "R12 σε {p0} (μισό) και {p1} (ένα τρίτο), R5 σε {p2} για τα κενά, R18 σε {p3} ως accent."]],
    "example_body": "Ίδια κατασκευή, άλλη παλέτα. Ποτέ δύο ίδια μπαλόνια δίπλα δίπλα, μοίρασε τα R18 σε όλο το μήκος και κάνε πού και πού τρία βήματα πίσω για να κοιτάξεις.",
    "client_label": "Ρωτάει πελάτης", "client_title": "Τι απαντάς όταν ρωτάει ένας πελάτης",
    "client_answers": [
        "Εξαρτάται από το μήκος και από το πόσο γεμάτη τη θέλεις. Δούλεψε σε μπλοκ: φούσκωσε μια σειρά, δέσε τα, βάλ' τα στο σχοινί και μέτρα πόσο έδωσε. Αγόραζε πάντα λίγα παραπάνω, ένα πάντα σκάει και να σου λείψουν λίγα για τα τελευταία κενά είναι κρίμα.",
        "Ναι, με καλό λάτεξ. Φτιάξε τη σε τμήματα, άπλωσέ τα επίπεδα χωρίς τίποτα από πάνω και δέσε τα σχοινιά επιτόπου. Μέσα, ένα μπαλόνι Sempertex κρατάει το σχήμα του λίγες μέρες έως μία εβδομάδα.",
        "Όχι. Η γιρλάντα κρέμεται σε τοίχο ή σκελετό και είναι γεμάτη απλό αέρα. Είναι φθηνότερο και κρατάει το σχήμα περισσότερο από το ήλιο.",
    ],
    "avoid_lead": "Η πρώτη σου γιρλάντα, σε 5 βήματα:",
    "steps5": ["Μέτρα το σημείο, διάλεξε γεμάτη ή αραιή, αγόρασε με περίσσευμα", "Φούσκωσε σε μπλοκ, κάθε μπαλόνι από το sizer, λαιμός άδειος", "Duplets γύρω από το σχοινί, κάθε φορά ένα τέταρτο στροφής πιο πέρα", "R5 σε κάθε κενό με glue dot, κόμπος προς τα μέσα", "Πρώτα τα άγκιστρα, μετά κρέμασε με τη μέση να κρεμάει"],
    "client_body": "Θέλεις να το μάθεις με τα χέρια σου; Το Start Your Balloon Business είναι το διήμερο workshop της Sempertex Europe: τεχνικές, γνώση υλικών και τα βασικά της επιχείρησής σου.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Γιρλάντα Sempertex:", "s3_cover_b": "με το μάτι", "s3_cover_c": "vs.", "s3_cover_d": "με sizer",
    "s3_left": "ΜΕ ΤΟ ΜΑΤΙ", "s3_right": "ΜΕ SIZER", "s3_left_meta": "0,5 cm διαφορά, κενά", "s3_right_meta": "R5 σε κάθε κενό",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Με το μάτι", "Λίγα μπαλόνια", "Κενά ανοιχτά"], "s3_new_tags": ["Sizer", "Με περίσσευμα", "R5 σε κάθε κενό", "Τέταρτο στροφής"],
    "s3_new_quote": "“Κάθε μπαλόνι από το sizer, duplets ένα τέταρτο στροφής το ένα από το άλλο, R5 σε κάθε κενό. Η γιρλάντα φαίνεται γεμάτη και το σχοινί χάθηκε.”", "s3_new_badge": "3 μεγέθη, 1 σχοινί",
    "s3_changed_bottom": "Ίδια μπαλόνια, ίδιο σχοινί.\nΤώρα δεν βλέπεις ούτε ένα κενό.",
    "s3_topic_lbl": "ΓΙΑΤΙ", "s3_rule1_topic": "Υλικά", "s3_rule1_old": "Ένα μέγεθος αρκεί",
    "s3_rule1_quote": "“R12 ως βάση, R5 για τα κενά, R18 ως accent. Τρία μεγέθη, και η γιρλάντα φαίνεται γεμάτη.”",
    "s3_rule2_topic": "Λάθη", "s3_rule2_old": "Τα κενά δεν τα βλέπει κανείς",
    "s3_rule2_quote": "“Τα R5 είναι το μισό αποτέλεσμα. Γέμισε κάθε κενό, με glue dot και τον κόμπο προς τα μέσα.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_topic": "Δύο παλέτες", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 και Reflex Gold 970, ή {p0}, {p1}, {p2} και {p3} από το ράφι.”",
    "s3_client_lbl": "ΠΕΛΑΤΗΣ", "s3_client_topic": "Πρώτη γιρλάντα",
    "s3_client_quote": "“Μέτρα, αγόρασε παραπάνω, sizer, duplets, R5, πρώτα τα άγκιστρα. Ένα βράδυ, μία γιρλάντα.”",
    "s3_cta_kicker": "3 μεγέθη, 1 σχοινί, 1 βράδυ",
    "base_lbl": "βάση", "gap_lbl": "κενά", "accent_lbl": "accent", "gaps_stamp": "κενά", "full_stamp": "γεμάτη", "sizes_stamp": "3 μεγέθη", "chips": ["R12 · R5 · R18", "τέταρτο στροφής", "glue dots"],
},
"hu": {
    "cover_pills": ["3 méret…", "Dupletek…", "Töltsd ki a réseket…"], "cover_with": "ezzel:", "cover_brand": "Sempertex Europe", "cover_tag": "Lufigirland…",
    "steps_title": "Lufigirland 6 lépésben: 3 méret, 1 zsinór, dupletek", "steps_lead": "Így építed fel:",
    "steps": ["Csak a kerek részt fújd fel, a nyak maradjon üres. Minden lufit a sizeren át: fél cm különbség látszik, amint a girland lóg", "Köss össze 2 azonos méretű lufit nyaktól nyakig: ez a duplet. Páronként egy csomó", "Fektesd le a zsinórt, tekerd minden dupletet egyszer köré, és negyed fordulattal tovább az előzőnél. Nyomd őket szorosan egymáshoz", "Töltsd ki a réseket R5-ösökkel, lazán kötve, glue dottal, a csomóval befelé. Ez az eredmény fele", "Egy akcentus, legfeljebb kettő: egy fólialufi vagy virág, glue dottal rögzítve", "Először a kampók, aztán a girland. A közepe lógjon, mint egy ruhaszárító kötél"],
    "steps_label": "A lépések",
    "rule1_label": "Anyagok", "rule1_title": "3 méret, 3 vagy 4 szín és egy zsinór, ami hosszabb a girlandnál",
    "rule1_body": "Az R12 az alap, ebből kell a legtöbb, az R5 tölti ki a réseket, néhány R18 a nagy akcentus. Válassz 3 vagy 4 színt: egyet a girland nagyjából felére, egy másodikat a harmadára, a többi akcentus. A Fashion a fedő alap, a Pastel Matte krétás hatású, a Pastel Dusk kicsit tompább és melegebb. Ha fényt akarsz, keverj néhány Silk vagy Reflex lufit a matt közé. Ezen kívül: erős zsinór vagy dekordrót, inflátor vagy kézipumpa, sizer, olló, erős kampók és glue dot. Hélium nem kell: a girland falon vagy kereten lóg, és a sima levegő tovább tartja a formáját.",
    "rule1_facts": [["3", "méret: R12 alapnak, R5 a résekhez, R18 akcentusnak"], ["1/2 + 1/3", "a girlandból az 1. és a 2. színben, a többi akcentus"], ["0,5 m", "zsinór ráhagyás mindkét végén, a kampókhoz"], ["0", "hélium: a sima levegő tovább tartja a formát"]],
    "rule2_label": "Hibák", "rule2_title": "A 3 kezdő hiba és 2 kérdés, amit minden ügyfél feltesz",
    "rule2_body": "A hiba ritkán a kötésben van. Itt van:",
    "alts": [["Érzésre fújás", "sizer nélkül a lufik fél cm-t eltérnek, és ez látszik, amint a girland lóg."], ["Túl kevés lufi", "félúton kifogyni a klasszikus. Vegyél bőven, egy mindig kidurran."], ["Kihagyott rések", "az R5-ösök adják az eredmény nagyjából felét. Használj sokat."], ["Egy nappal előre?", "igen, jó latexszel. Építsd szakaszokban, fektesd le laposan, semmi ne legyen rajta, és a zsinórokat a helyszínen kösd össze."], ["Meddig marad jó?", "bent néhány naptól egy hétig, kint rövidebb ideig a nap és a meleg miatt. A Sempertex latex 100% természetes gumi töltőanyag nélkül, és tartja a levegőt."]],
    "example_label": "Példa", "example_title": "Egy girland, két paletta",
    "ex_items": [["Matt, 1 fényes akcentussal", "R12 Pastel Dusk Rose 110 (fele) és White Sand 071 (harmada), R5 Eucalyptus 027 a résekhez, R18 Reflex Gold 970 akcentusnak."], ["A forgalmazód polcáról", "R12 {p0} (fele) és {p1} (harmada), R5 {p2} a résekhez, R18 {p3} akcentusnak."]],
    "example_body": "Ugyanaz az építés, más paletta. Soha két egyforma lufi egymás mellett, az R18-asokat oszd el a teljes hosszon, és néha lépj hátra hármat, hogy ránézz.",
    "client_label": "Ügyfél kérdezi", "client_title": "Mit válaszolsz, ha egy ügyfél kérdezi",
    "client_answers": [
        "A hossztól függ, és attól, milyen tömöttre akarod. Dolgozz blokkokban: fújj fel egy sorozatot, kösd meg, tedd a zsinórra, és mérd meg, mennyit adott. Mindig vegyél néhánnyal többet, egy mindig kidurran, és kár, ha pont az utolsó résekhez nem jut.",
        "Igen, jó latexszel. Építsd szakaszokban, fektesd le laposan, semmi ne legyen rajta, és a zsinórokat a helyszínen kösd össze. Bent egy Sempertex lufi néhány naptól egy hétig tartja a formáját.",
        "Nem. A girland falon vagy kereten lóg, és sima levegő van benne. Olcsóbb, és tovább tartja a formáját, mint a hélium.",
    ],
    "avoid_lead": "Az első girlandod, 5 lépésben:",
    "steps5": ["Mérd meg a helyet, válassz tömött vagy levegős, vegyél bőven", "Fújj blokkonként, minden lufit a sizeren át, üres nyak", "Dupletek a zsinór köré, mindig negyed fordulattal tovább", "R5 minden résbe glue dottal, csomó befelé", "Először a kampók, aztán akaszd fel lógó közepével"],
    "client_body": "Kézzel akarod megtanulni? A Start Your Balloon Business a Sempertex Europe kétnapos workshopja: technikák, anyagismeret és a vállalkozásod alapjai.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Sempertex girland:", "s3_cover_b": "érzésre", "s3_cover_c": "vs.", "s3_cover_d": "sizerrel",
    "s3_left": "ÉRZÉSRE", "s3_right": "SIZERREL", "s3_left_meta": "0,5 cm eltérés, rések", "s3_right_meta": "R5 minden résben",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Érzésre", "Kevés lufi", "Nyitott rések"], "s3_new_tags": ["Sizer", "Bőven véve", "R5 minden résben", "Negyed fordulat"],
    "s3_new_quote": "“Minden lufi a sizeren át, a dupletek negyed fordulattal eltolva, R5 minden résben. A girland tömöttnek látszik, a zsinór eltűnt.”", "s3_new_badge": "3 méret, 1 zsinór",
    "s3_changed_bottom": "Ugyanazok a lufik, ugyanaz a zsinór.\nMost egy rést se látsz.",
    "s3_topic_lbl": "MIÉRT", "s3_rule1_topic": "Anyagok", "s3_rule1_old": "Egy méret elég",
    "s3_rule1_quote": "“R12 alapnak, R5 a résekhez, R18 akcentusnak. Három méret, és a girland tömöttnek látszik.”",
    "s3_rule2_topic": "Hibák", "s3_rule2_old": "A réseket senki se veszi észre",
    "s3_rule2_quote": "“Az R5-ösök az eredmény fele. Tölts ki minden rést, glue dottal, csomóval befelé.”",
    "s3_example_lbl": "PÉLDA", "s3_example_topic": "Két paletta", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 és Reflex Gold 970, vagy {p0}, {p1}, {p2} és {p3} a polcról.”",
    "s3_client_lbl": "ÜGYFÉL", "s3_client_topic": "Első girland",
    "s3_client_quote": "“Mérés, bő vásárlás, sizer, dupletek, R5, először a kampók. Egy este, egy girland.”",
    "s3_cta_kicker": "3 méret, 1 zsinór, 1 este",
    "base_lbl": "alap", "gap_lbl": "rések", "accent_lbl": "akcentus", "gaps_stamp": "rések", "full_stamp": "tömött", "sizes_stamp": "3 méret", "chips": ["R12 · R5 · R18", "negyed fordulat", "glue dot"],
},
"lt": {
    "cover_pills": ["3 dydžiai…", "Dupletai…", "Užpildyk tarpus…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Balionų girlianda…",
    "steps_title": "Balionų girlianda 6 žingsniais: 3 dydžiai, 1 virvė, dupletai", "steps_lead": "Taip ją surenki:",
    "steps": ["Pripūsk tik apvalią dalį, kaklelis tuščias. Kiekvieną balioną per sizer: pusės cm skirtumas matosi, kai girlianda kabo", "Suriš 2 to paties dydžio balionus kaklelis prie kaklelio: dupletas. Vienas mazgas porai", "Patiesk virvę, apsuk kiekvieną dupletą kartą aplink ją ir ketvirčiu posūkio toliau nei ankstesnį. Suspausk juos tvirtai", "Užpildyk tarpus R5, laisvai surištais, su glue dot ir mazgu į vidų. Tai pusė rezultato", "Vienas akcentas, daugiausia du: folinis balionas ar gėlės, pritvirtinti glue dot", "Pirma kabliukai, tada girlianda. Leisk viduriui nukarti kaip skalbinių virvei"],
    "steps_label": "Žingsniai",
    "rule1_label": "Medžiagos", "rule1_title": "3 dydžiai, 3 ar 4 spalvos ir virvė, ilgesnė už girliandą",
    "rule1_body": "R12 yra pagrindas, jų reikia daugiausia, R5 užpildo tarpus, keli R18 yra dideli akcentai. Pasirink 3 ar 4 spalvas: vieną maždaug pusei girliandos, antrą trečdaliui, likusias kaip akcentą. Fashion yra dengiantis pagrindas, Pastel Matte atrodo kreidiškai, Pastel Dusk kiek blankesnis ir šiltesnis. Jei nori blizgesio, įmaišyk kelis Silk ar Reflex balionus tarp matinių. Dar: tvirta virvė ar dekoratyvinė viela, pūstuvas ar rankinė pompa, sizer, žirklės, tvirti kabliukai ir glue dot. Be helio: girlianda kabo ant sienos ar rėmo, o paprastas oras ilgiau išlaiko formą.",
    "rule1_facts": [["3", "dydžiai: R12 pagrindas, R5 tarpams, R18 akcentas"], ["1/2 + 1/3", "girliandos 1 ir 2 spalva, likusi dalis akcentas"], ["0,5 m", "virvės daugiau kiekviename gale, kabliukams"], ["0", "helio: paprastas oras ilgiau išlaiko formą"]],
    "rule2_label": "Klaidos", "rule2_title": "3 pradedančiųjų klaidos ir 2 klausimai, kuriuos užduoda kiekvienas klientas",
    "rule2_body": "Klaidos retai slypi rišime. Jos čia:",
    "alts": [["Pūtimas iš akies", "be sizer balionai skiriasi puse cm, ir tai matosi, vos tik girlianda kabo."], ["Per mažai nupirkta", "likti be balionų pusiaukelėje yra klasika. Pirk su atsarga, vienas visada sprogsta."], ["Praleisti tarpai", "R5 sudaro maždaug pusę rezultato. Naudok daug."], ["Padaryti dieną prieš?", "taip, su geru lateksu. Rink dalimis, paguldyk jas plokščiai, nieko ant viršaus, o virves suriš vietoje."], ["Kiek laiko laikosi?", "viduje kelias dienas iki savaitės, lauke trumpiau dėl saulės ir karščio. Sempertex lateksas yra 100% natūralus kaučiukas be užpildų ir išlaiko orą."]],
    "example_label": "Pavyzdys", "example_title": "Viena girlianda, dvi paletės",
    "ex_items": [["Matinė su 1 blizgiu akcentu", "R12 Pastel Dusk Rose 110 (pusė) ir White Sand 071 (trečdalis), R5 Eucalyptus 027 tarpams, R18 Reflex Gold 970 kaip akcentas."], ["Iš tavo platintojo lentynos", "R12 {p0} (pusė) ir {p1} (trečdalis), R5 {p2} tarpams, R18 {p3} kaip akcentas."]],
    "example_body": "Ta pati konstrukcija, kita paletė. Niekada du vienodi balionai vienas šalia kito, paskirstyk R18 per visą ilgį ir retkarčiais ženk tris žingsnius atgal pažiūrėti.",
    "client_label": "Klausia klientas", "client_title": "Ką atsakai, kai klausia klientas",
    "client_answers": [
        "Priklauso nuo ilgio ir nuo to, kiek pilnos nori. Dirbk blokais: pripūsk seriją, suriš, užmauk ant virvės ir išmatuok, kiek tai davė. Visada pirk kelis papildomai, vienas visada sprogsta, o pritrūkti paskutiniams tarpams gaila.",
        "Taip, su geru lateksu. Rink ją dalimis, paguldyk jas plokščiai, nieko ant viršaus, o virves suriš vietoje. Viduje Sempertex balionas išlaiko formą kelias dienas iki savaitės.",
        "Ne. Girlianda kabo ant sienos ar rėmo ir yra pripildyta paprasto oro. Tai pigiau ir išlaiko formą ilgiau nei helis.",
    ],
    "avoid_lead": "Tavo pirma girlianda, 5 žingsniais:",
    "steps5": ["Išmatuok vietą, pasirink pilną ar orią, pirk su atsarga", "Pūsk blokais, kiekvieną balioną per sizer, kaklelis tuščias", "Dupletai aplink virvę, kaskart ketvirčiu posūkio toliau", "R5 į kiekvieną tarpą su glue dot, mazgas į vidų", "Pirma kabliukai, tada pakabink su nukarusiu viduriu"],
    "client_body": "Nori išmokti rankomis? Start Your Balloon Business yra Sempertex Europe dviejų dienų dirbtuvės: technikos, medžiagų išmanymas ir tavo verslo pagrindai.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Sempertex girlianda:", "s3_cover_b": "iš akies", "s3_cover_c": "vs.", "s3_cover_d": "su sizer",
    "s3_left": "IŠ AKIES", "s3_right": "SU SIZER", "s3_left_meta": "0,5 cm skirtumo, tarpai", "s3_right_meta": "R5 kiekviename tarpe",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Iš akies", "Per mažai pirkta", "Atviri tarpai"], "s3_new_tags": ["Sizer", "Pirkta su atsarga", "R5 kiekviename tarpe", "Ketvirtis posūkio"],
    "s3_new_quote": "“Kiekvienas balionas per sizer, dupletai ketvirčiu posūkio vienas nuo kito, R5 kiekviename tarpe. Girlianda atrodo pilna, o virvės nebesimato.”", "s3_new_badge": "3 dydžiai, 1 virvė",
    "s3_changed_bottom": "Tie patys balionai, ta pati virvė.\nDabar nematai nė vieno tarpo.",
    "s3_topic_lbl": "KODĖL", "s3_rule1_topic": "Medžiagos", "s3_rule1_old": "Vieno dydžio užtenka",
    "s3_rule1_quote": "“R12 pagrindas, R5 tarpams, R18 akcentas. Trys dydžiai, ir girlianda atrodo pilna.”",
    "s3_rule2_topic": "Klaidos", "s3_rule2_old": "Tų tarpų niekas nepastebi",
    "s3_rule2_quote": "“R5 yra pusė rezultato. Užpildyk kiekvieną tarpą, su glue dot ir mazgu į vidų.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_topic": "Dvi paletės", "s3_example_quote": "“Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 ir Reflex Gold 970, arba {p0}, {p1}, {p2} ir {p3} iš lentynos.”",
    "s3_client_lbl": "KLIENTAS", "s3_client_topic": "Pirma girlianda",
    "s3_client_quote": "“Išmatuoti, pirkti su atsarga, sizer, dupletai, R5, pirma kabliukai. Vienas vakaras, viena girlianda.”",
    "s3_cta_kicker": "3 dydžiai, 1 virvė, 1 vakaras",
    "base_lbl": "pagrindas", "gap_lbl": "tarpai", "accent_lbl": "akcentas", "gaps_stamp": "tarpai", "full_stamp": "pilna", "sizes_stamp": "3 dydžiai", "chips": ["R12 · R5 · R18", "ketvirtis posūkio", "glue dot"],
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["Een ballonslinger is één handeling, steeds herhaald: Sempertex R12, R5 en R18, in duplets om een touw", "Je eerste slinger in één avond: 3 maten Sempertex, 1 touw en de stap die iedereen overslaat", "Slinger te leeg? De R5's zijn de helft van het resultaat. Zo bouw je een volle Sempertex slinger, stap voor stap"],
  "cover_sub": ["Wat je nodig hebt, de 6 stappen, de 3 beginnersfouten en een voorbeeld met codes. Zonder helium.", "Opblazen door de sizer, knopen in duplets, om het touw, gaten vullen met R5's, ophangen als een waslijn."],
  "client_question": ["Hoeveel ballonnen heb ik nodig voor een slinger van 3 m?", "Kan ik de slinger een dag vooraf maken?", "Heb ik helium nodig voor een slinger?"],
  "s3_old_quote": ["“Op gevoel opblazen gaat sneller”", "“Die paar gaten vallen niet op”", "“Ik koop precies genoeg”"],
  "s3_client_old": ["“Eén maat ballonnen is genoeg”", "“Ophangen en strak trekken”"],
  "cta_title_tpl": "Bestel je Sempertex R12, R5 en R18 bij {name}", "cta_sub_generic": "3 maten, een touw, een sizer en glue dots. Koop een paar extra, er knapt er altijd één.",
},
"en": {
  "cover_title": ["A balloon garland is one action, repeated: Sempertex R12, R5 and R18, in duplets around a rope", "Your first garland in one evening: 3 Sempertex sizes, 1 rope and the step everyone skips", "Garland looking empty? The R5s are half the result. How to build a full Sempertex garland, step by step"],
  "cover_sub": ["What you need, the 6 steps, the 3 first-timer mistakes and an example with codes. No helium.", "Inflate through the sizer, tie in duplets, around the rope, fill the gaps with R5s, hang it like a washing line."],
  "client_question": ["How many balloons do I need for a 3 m garland?", "Can I make the garland a day ahead?", "Do I need helium for a garland?"],
  "s3_old_quote": ["“Inflating by feel is quicker”", "“Nobody notices a few gaps”", "“I buy exactly enough”"],
  "s3_client_old": ["“One balloon size is enough”", "“Hang it and pull it straight”"],
  "cta_title_tpl": "Order your Sempertex R12, R5 and R18 at {name}", "cta_sub_generic": "3 sizes, a rope, a sizer and glue dots. Buy a few extra, one always pops.",
},
"de": {
  "cover_title": ["Eine Ballongirlande ist ein Handgriff, immer wiederholt: Sempertex R12, R5 und R18, in Duplets ums Seil", "Deine erste Girlande an einem Abend: 3 Sempertex Größen, 1 Seil und der Schritt, den alle auslassen", "Girlande zu leer? Die R5 sind die Hälfte des Ergebnisses. So baust du eine volle Sempertex Girlande, Schritt für Schritt"],
  "cover_sub": ["Was du brauchst, die 6 Schritte, die 3 Anfängerfehler und ein Beispiel mit Codes. Ohne Helium.", "Durch den Sizer aufblasen, in Duplets knoten, ums Seil, Lücken mit R5 füllen, aufhängen wie eine Wäscheleine."],
  "client_question": ["Wie viele Ballons brauche ich für 3 m Girlande?", "Kann ich die Girlande einen Tag vorher bauen?", "Brauche ich Helium für eine Girlande?"],
  "s3_old_quote": ["“Nach Gefühl aufblasen geht schneller”", "“Die paar Lücken fallen nicht auf”", "“Ich kaufe genau genug”"],
  "s3_client_old": ["“Eine Ballongröße reicht”", "“Aufhängen und straff ziehen”"],
  "cta_title_tpl": "Bestell deine Sempertex R12, R5 und R18 bei {name}", "cta_sub_generic": "3 Größen, ein Seil, ein Sizer und Glue Dots. Kauf ein paar extra, einer platzt immer.",
},
"fr": {
  "cover_title": ["Une guirlande de ballons, c'est un geste répété : Sempertex R12, R5 et R18, en duplets autour d'une corde", "Ta première guirlande en une soirée : 3 tailles Sempertex, 1 corde et l'étape que tout le monde saute", "Guirlande trop vide ? Les R5 font la moitié du résultat. Monter une guirlande Sempertex bien pleine, pas à pas"],
  "cover_sub": ["Ce qu'il te faut, les 6 étapes, les 3 erreurs de débutant et un exemple avec codes. Sans hélium.", "Gonfler par le sizer, nouer en duplets, autour de la corde, combler les trous avec des R5, accrocher comme une corde à linge."],
  "client_question": ["Combien de ballons pour une guirlande de 3 m ?", "Je peux faire la guirlande la veille ?", "Il faut de l'hélium pour une guirlande ?"],
  "s3_old_quote": ["“Gonfler au jugé, c'est plus rapide”", "“Ces quelques trous, personne ne les voit”", "“J'achète juste ce qu'il faut”"],
  "s3_client_old": ["“Une seule taille de ballons suffit”", "“Accrocher et tirer bien droit”"],
  "cta_title_tpl": "Commande tes Sempertex R12, R5 et R18 chez {name}", "cta_sub_generic": "3 tailles, une corde, un sizer et des glue dots. Achète quelques ballons en plus, il y en a toujours un qui éclate.",
},
"it": {
  "cover_title": ["Una ghirlanda di palloncini è un gesto ripetuto: Sempertex R12, R5 e R18, in duplet attorno a una corda", "La tua prima ghirlanda in una sera: 3 misure Sempertex, 1 corda e il passo che tutti saltano", "Ghirlanda troppo vuota? Gli R5 sono metà del risultato. Come costruire una ghirlanda Sempertex piena, passo per passo"],
  "cover_sub": ["Cosa ti serve, i 6 passi, i 3 errori da principiante e un esempio con i codici. Senza elio.", "Gonfiare dal sizer, legare in duplet, attorno alla corda, riempire i vuoti con gli R5, appendere come un filo del bucato."],
  "client_question": ["Quanti palloncini servono per una ghirlanda di 3 m?", "Posso fare la ghirlanda il giorno prima?", "Serve l'elio per una ghirlanda?"],
  "s3_old_quote": ["“Gonfiare a occhio è più veloce”", "“Quei pochi vuoti non si notano”", "“Compro giusto quelli che servono”"],
  "s3_client_old": ["“Una misura di palloncini basta”", "“Appendere e tirare dritto”"],
  "cta_title_tpl": "Ordina i tuoi Sempertex R12, R5 e R18 da {name}", "cta_sub_generic": "3 misure, una corda, un sizer e glue dot. Comprane qualcuno in più, uno scoppia sempre.",
},
"pl": {
  "cover_title": ["Girlanda balonowa to jeden ruch, powtarzany: Sempertex R12, R5 i R18, w dupletach wokół sznurka", "Twoja pierwsza girlanda w jeden wieczór: 3 rozmiary Sempertex, 1 sznurek i krok, który wszyscy pomijają", "Girlanda za pusta? Balony R5 to połowa efektu. Jak zbudować pełną girlandę Sempertex, krok po kroku"],
  "cover_sub": ["Co potrzebujesz, 6 kroków, 3 błędy początkujących i przykład z kodami. Bez helu.", "Pompuj przez sizer, wiąż w duplety, wokół sznurka, wypełnij luki balonami R5, zawieś jak sznur na pranie."],
  "client_question": ["Ile balonów potrzebuję na girlandę 3 m?", "Czy mogę zrobić girlandę dzień wcześniej?", "Czy do girlandy potrzebny jest hel?"],
  "s3_old_quote": ["“Pompowanie na oko jest szybsze”", "“Tych paru luk nikt nie zauważy”", "“Kupuję dokładnie tyle, ile trzeba”"],
  "s3_client_old": ["“Jeden rozmiar balonów wystarczy”", "“Zawiesić i naciągnąć prosto”"],
  "cta_title_tpl": "Zamów balony Sempertex R12, R5 i R18 w {name}", "cta_sub_generic": "3 rozmiary, sznurek, sizer i glue doty. Kup kilka na zapas, jeden zawsze pęka.",
},
"el": {
  "cover_title": ["Μια γιρλάντα από μπαλόνια είναι μία κίνηση, ξανά και ξανά: Sempertex R12, R5 και R18, σε duplets γύρω από σχοινί", "Η πρώτη σου γιρλάντα σε ένα βράδυ: 3 μεγέθη Sempertex, 1 σχοινί και το βήμα που όλοι παραλείπουν", "Γιρλάντα πολύ αραιή; Τα R5 είναι το μισό αποτέλεσμα. Έτσι φτιάχνεις μια γεμάτη γιρλάντα Sempertex, βήμα βήμα"],
  "cover_sub": ["Τι χρειάζεσαι, τα 6 βήματα, τα 3 λάθη των αρχάριων και ένα παράδειγμα με κωδικούς. Χωρίς ήλιο.", "Φούσκωμα από το sizer, δέσιμο σε duplets, γύρω από το σχοινί, γέμισμα των κενών με R5, κρέμασμα σαν σχοινί απλώματος."],
  "client_question": ["Πόσα μπαλόνια χρειάζομαι για γιρλάντα 3 m;", "Μπορώ να φτιάξω τη γιρλάντα μία μέρα πριν;", "Χρειάζομαι ήλιο για γιρλάντα;"],
  "s3_old_quote": ["“Με το μάτι φουσκώνεις πιο γρήγορα”", "“Αυτά τα λίγα κενά δεν τα βλέπει κανείς”", "“Αγοράζω ακριβώς όσα χρειάζονται”"],
  "s3_client_old": ["“Ένα μέγεθος μπαλονιών αρκεί”", "“Κρέμασέ τη και τέντωσέ τη ίσια”"],
  "cta_title_tpl": "Παράγγειλε τα Sempertex R12, R5 και R18 σου από {name}", "cta_sub_generic": "3 μεγέθη, ένα σχοινί, ένα sizer και glue dots. Αγόρασε λίγα παραπάνω, ένα πάντα σκάει.",
},
"hu": {
  "cover_title": ["A lufigirland egy mozdulat, újra és újra: Sempertex R12, R5 és R18, dupletekben a zsinór köré", "Az első girlandod egy este alatt: 3 Sempertex méret, 1 zsinór és a lépés, amit mindenki kihagy", "Túl üres a girland? Az R5-ösök az eredmény fele. Így építesz tömött Sempertex girlandot, lépésről lépésre"],
  "cover_sub": ["Mi kell hozzá, a 6 lépés, a 3 kezdő hiba és egy példa kódokkal. Hélium nélkül.", "Fújás a sizeren át, kötés dupletekbe, a zsinór köré, rések kitöltése R5-ösökkel, felakasztás mint egy ruhaszárító kötél."],
  "client_question": ["Hány lufi kell egy 3 m-es girlandhoz?", "Elkészíthetem a girlandot egy nappal előre?", "Kell hélium a girlandhoz?"],
  "s3_old_quote": ["“Érzésre fújni gyorsabb”", "“Azt a pár rést senki se veszi észre”", "“Pont annyit veszek, amennyi kell”"],
  "s3_client_old": ["“Egy lufiméret elég”", "“Felakasztani és egyenesre húzni”"],
  "cta_title_tpl": "Rendeld a Sempertex R12, R5 és R18 lufikat innen: {name}", "cta_sub_generic": "3 méret, egy zsinór, egy sizer és glue dot. Vegyél néhánnyal többet, egy mindig kidurran.",
},
"lt": {
  "cover_title": ["Balionų girlianda yra vienas judesys, kartojamas: Sempertex R12, R5 ir R18, dupletais aplink virvę", "Tavo pirma girlianda per vieną vakarą: 3 Sempertex dydžiai, 1 virvė ir žingsnis, kurį visi praleidžia", "Girlianda per tuščia? R5 yra pusė rezultato. Kaip surinkti pilną Sempertex girliandą, žingsnis po žingsnio"],
  "cover_sub": ["Ko reikia, 6 žingsniai, 3 pradedančiųjų klaidos ir pavyzdys su kodais. Be helio.", "Pūsti per sizer, rišti dupletais, aplink virvę, užpildyti tarpus R5, pakabinti kaip skalbinių virvę."],
  "client_question": ["Kiek balionų reikia 3 m girliandai?", "Ar galiu padaryti girliandą dieną prieš?", "Ar girliandai reikia helio?"],
  "s3_old_quote": ["“Pūsti iš akies greičiau”", "“Tų kelių tarpų niekas nepastebi”", "“Perku lygiai tiek, kiek reikia”"],
  "s3_client_old": ["“Vieno balionų dydžio užtenka”", "“Pakabinti ir ištempti tiesiai”"],
  "cta_title_tpl": "Užsisakyk Sempertex R12, R5 ir R18 iš {name}", "cta_sub_generic": "3 dydžiai, virvė, sizer ir glue dot. Pirk kelis papildomai, vienas visada sprogsta.",
},
}

CAPTIONS_TPL = {
 "nl": "Een ballonslinger is één handeling, steeds herhaald: opblazen in 3 maten, knopen in duplets, om het touw draaien en de gaten vullen met R5's. In deze carousel: wat je nodig hebt (R12, R5, R18, touw, sizer, glue dots), de 6 stappen, de 3 beginnersfouten en een voorbeeld met codes: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 en Reflex Gold 970. Zonder helium.\n\nBestel je Sempertex R12, R5 en R18 bij {domain}.\n\n#ballonslinger #ballongirlande #sempertex #{tag} #ballondecoratie #ballonartiest",
 "en": "A balloon garland is one action, repeated: inflate in 3 sizes, tie in duplets, twist around the rope and fill the gaps with R5s. In this carousel: what you need (R12, R5, R18, rope, sizer, glue dots), the 6 steps, the 3 first-timer mistakes and an example with codes: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 and Reflex Gold 970. No helium.\n\nOrder your Sempertex R12, R5 and R18 at {domain}.\n\n#balloongarland #organicgarland #sempertex #{tag} #balloondecor #balloonartist",
 "de": "Eine Ballongirlande ist ein Handgriff, immer wiederholt: in 3 Größen aufblasen, in Duplets knoten, ums Seil drehen und die Lücken mit R5 füllen. Im Carousel: was du brauchst (R12, R5, R18, Seil, Sizer, Glue Dots), die 6 Schritte, die 3 Anfängerfehler und ein Beispiel mit Codes: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 und Reflex Gold 970. Ohne Helium.\n\nBestell deine Sempertex R12, R5 und R18 bei {domain}.\n\n#ballongirlande #organicgirlande #sempertex #{tag} #ballondeko #ballonkünstler",
 "fr": "Une guirlande de ballons, c'est un geste répété : gonfler en 3 tailles, nouer en duplets, enrouler autour de la corde et combler les trous avec des R5. Dans ce carrousel : ce qu'il te faut (R12, R5, R18, corde, sizer, glue dots), les 6 étapes, les 3 erreurs de débutant et un exemple avec codes : Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 et Reflex Gold 970. Sans hélium.\n\nCommande tes Sempertex R12, R5 et R18 chez {domain}.\n\n#guirlandedeballons #guirlandeorganique #sempertex #{tag} #decorationballons #artisteballon",
 "it": "Una ghirlanda di palloncini è un gesto ripetuto: gonfiare in 3 misure, legare in duplet, girare attorno alla corda e riempire i vuoti con gli R5. Nel carosello: cosa ti serve (R12, R5, R18, corda, sizer, glue dot), i 6 passi, i 3 errori da principiante e un esempio con i codici: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 e Reflex Gold 970. Senza elio.\n\nOrdina i tuoi Sempertex R12, R5 e R18 da {domain}.\n\n#ghirlandadipalloncini #organicgarland #sempertex #{tag} #palloncini #balloonartist",
 "pl": "Girlanda balonowa to jeden ruch, powtarzany: pompuj w 3 rozmiarach, wiąż w duplety, okręcaj wokół sznurka i wypełniaj luki balonami R5. W karuzeli: co potrzebujesz (R12, R5, R18, sznurek, sizer, glue doty), 6 kroków, 3 błędy początkujących i przykład z kodami: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 i Reflex Gold 970. Bez helu.\n\nZamów balony Sempertex R12, R5 i R18 w {domain}.\n\n#girlandabalonowa #girlandaorganiczna #sempertex #{tag} #dekoracjebalonowe #artystabalonowy",
 "el": "Μια γιρλάντα από μπαλόνια είναι μία κίνηση, ξανά και ξανά: φούσκωμα σε 3 μεγέθη, δέσιμο σε duplets, τύλιγμα γύρω από το σχοινί και γέμισμα των κενών με R5. Στο carousel: τι χρειάζεσαι (R12, R5, R18, σχοινί, sizer, glue dots), τα 6 βήματα, τα 3 λάθη των αρχάριων και ένα παράδειγμα με κωδικούς: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 και Reflex Gold 970. Χωρίς ήλιο.\n\nΠαράγγειλε τα Sempertex R12, R5 και R18 σου από {domain}.\n\n#γιρλανταμπαλονια #organicgarland #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "A lufigirland egy mozdulat, újra és újra: fújás 3 méretben, kötés dupletekbe, tekerés a zsinór köré és a rések kitöltése R5-ösökkel. A carouselben: mi kell hozzá (R12, R5, R18, zsinór, sizer, glue dot), a 6 lépés, a 3 kezdő hiba és egy példa kódokkal: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 és Reflex Gold 970. Hélium nélkül.\n\nRendeld a Sempertex R12, R5 és R18 lufikat innen: {domain}.\n\n#lufigirland #organikusgirland #sempertex #{tag} #lufidekoracio #lufiművész",
 "lt": "Balionų girlianda yra vienas judesys, kartojamas: pūsti 3 dydžiais, rišti dupletais, sukti aplink virvę ir užpildyti tarpus R5. Karuselėje: ko reikia (R12, R5, R18, virvė, sizer, glue dot), 6 žingsniai, 3 pradedančiųjų klaidos ir pavyzdys su kodais: Pastel Dusk Rose 110, White Sand 071, Eucalyptus 027 ir Reflex Gold 970. Be helio.\n\nUžsisakyk Sempertex R12, R5 ir R18 iš {domain}.\n\n#balionugirlianda #organicgarland #sempertex #{tag} #balionai #balionumenininkas",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}
TUT = ["duskrose", "whitesand", "eucalyptus", "reflexgold"]   # R12 helft, R12 derde, R5 gaten, R18 accent

def fill_pal(b, c):
    lab = {f"p{i}": G["pal_label"](k, short=False).replace("Fashion ", "").replace("Pastel ", "") for i, k in enumerate(b["pal"][:4])}
    def f(v): return v.format(**lab) if isinstance(v, str) and "{p" in v else v
    out = {}
    for k, v in c.items():
        if isinstance(v, str): out[k] = f(v)
        elif isinstance(v, list): out[k] = [[f(x) for x in item] if isinstance(item, list) else f(item) for item in v]
        else: out[k] = v
    qs = VARIANTS[b["lang"]]["client_question"]
    qi = qs.index(c["client_question"]) if c["client_question"] in qs else 0
    out["client_answer"] = c["client_answers"][qi]
    return out

def _bl(key, size, cls="", extra=""):
    return G["balloon"](key, "fashion", size, extra_style=extra, cls=cls)

def facts_grid(items, cls="facts", num_size=44, lab_size=20):
    esc = G["esc"]
    def fs(n):
        L = len(n); return num_size if L <= 6 else (int(num_size * .72) if L <= 11 else int(num_size * .55))
    cells = "".join(f'<div class="fact"><b style="font-size:{fs(n)}px">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in items)
    return f'<div class="{cls}">{cells}</div>'

def _at(key, size, angle, x, y):
    """Ballon met de nek (onderkant, midden) op punt (x,y), gedraaid rond die nek."""
    h = int(size * G["photo_ratio"](key)) if "photo_ratio" in G else int(size * G["PHOTO_RATIO"])
    return f'<div style="position:absolute;left:{x - size//2}px;top:{y - h}px;transform-origin:50% 100%;transform:rotate({angle}deg)">{_bl(key, size)}</div>'

def rope_garland(keys, w=330, h=300, n=9, size=50, loose=False, ink="#111"):
    """Slinger langs een doorhangend touw (waslijn): per punt een cluster van R12's rond het touw, elke cluster een
    kwartslag verder, R5's op de naden, 2 R18's verdeeld. loose=True: op gevoel: minder clusters, ongelijke maten,
    geen R5's, touw zichtbaar. keys = [R12 helft, R12 derde, R5 gaten, R18 accent]."""
    sag = int(h * .34); y0 = 46
    def P(t): return (14 + t * (w - 28), y0 + 4 * sag * t * (1 - t))
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    out += (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0">'
            f'<path d="M14 {y0} Q {w//2} {y0 + 2*sag} {w-14} {y0}" fill="none" stroke="{ROPE}" stroke-width="4" stroke-linecap="round"/>'
            f'<circle cx="14" cy="{y0}" r="7" fill="{ink}"/><circle cx="{w-14}" cy="{y0}" r="7" fill="{ink}"/></svg>')
    seq = (0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0)
    if loose:
        n = max(4, n - 3)
    for i in range(n):
        x, y = P((i + .5) / n); x, y = int(x), int(y)
        k = keys[seq[i % len(seq)]]
        s = size
        if loose:
            s = int(size * (0.78, 1.12, 0.9, 1.18, 0.84)[i % 5])
            angles = (-70 + i * 40, 110 + i * 40)
        else:
            angles = (-60 + i * 45, 60 + i * 45, 180 + i * 45)
        big = (not loose) and i in (1, n - 3)
        for j, a in enumerate(angles):
            kk = keys[3] if (big and j == 0) else k
            ss = int(s * 1.45) if (big and j == 0) else s
            out += _at(kk, ss, a, x, y)
        if not loose:
            out += _at(keys[2], int(size * .5), 20 + i * 45, x + size // 2, y + 4)
    return out + '</div>'

def duplet(key, size=46, ink="#111"):
    ratio = G["photo_ratio"](key) if "photo_ratio" in G else G["PHOTO_RATIO"]; h = int(size * ratio); w = int(h * 1.6)
    out = f'<div style="position:relative;width:{w}px;height:{h + 10}px">'
    out += _at(key, size, -38, w // 2, h + 4) + _at(key, size, 38, w // 2, h + 4)
    out += f'<div style="position:absolute;left:{w//2 - 6}px;top:{h - 2}px;width:12px;height:12px;border-radius:50%;background:{ink}"></div>'
    return out + '</div>'

def sizes_row(keys, c, ink="#111", lbl_size=17):
    """R12 duplet (basis), R5 (gaten), R18 (accent) naast elkaar met label."""
    esc = G["esc"]
    def col(v, name, what):
        return (f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end">'
                f'<div style="height:150px;display:flex;align-items:flex-end">{v}</div>'
                f'<div style="margin-top:8px;font-size:{lbl_size + 4}px;font-weight:900;color:{ink}">{name}</div>'
                f'<div style="font-size:{lbl_size}px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{ink};opacity:.6;white-space:nowrap">{esc(what)}</div></div>')
    cols = [col(duplet(keys[0], 60, ink), "R12", c["base_lbl"]), col(_bl(keys[2], 50), "R5", c["gap_lbl"]), col(_bl(keys[3], 108), "R18", c["accent_lbl"])]
    return '<div style="display:flex;gap:44px;align-items:flex-end;justify-content:center">' + "".join(cols) + '</div>'

def chips_row(items, ink="#111", bg="#fff", small=False):
    esc = G["esc"]; extra = "font-size:15px;padding:4px 10px;" if small else ""
    return '<div style="display:flex;justify-content:center;gap:6px;flex-wrap:wrap">' + "".join(f'<span class="tchip" style="{extra}border-color:{ink};color:{ink};background:{bg}">{esc(t)}</span>' for t in items) + '</div>'

def _stamp(text, ink, color, left, top, rot=-5):
    esc = G["esc"]
    return (f'<div style="position:absolute;left:{left}px;top:{top}px;transform:rotate({rot}deg);background:#fff;color:{color};border:3px solid {ink};'
            f'border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">{esc(text)}</div>')

def loose_visual(keys, c, ink="#111"):
    return (f'<div style="position:relative;width:330px;height:380px"><div style="position:absolute;left:0;top:40px">{rope_garland(keys, 330, 300, 9, 50, loose=True, ink=ink)}</div>'
            + _stamp(c["gaps_stamp"] + " ✕", ink, "#E03131", 160, 320, -6) + '</div>')

def full_visual(keys, c, ink="#111"):
    return (f'<div style="position:relative;width:330px;height:380px"><div style="position:absolute;left:0;top:40px">{rope_garland(keys, 330, 300, 9, 50, ink=ink)}</div>'
            + _stamp("✓ " + c["full_stamp"], ink, ink, 0, 328, -4) + '</div>')

def sizes_visual(keys, c, ink="#111"):
    return (f'<div style="position:relative;width:330px;height:380px"><div style="position:absolute;left:0;top:40px">{rope_garland(keys, 330, 300, 9, 50, ink=ink)}</div>'
            + _stamp(c["sizes_stamp"], ink, ink, 0, 328, -4) + '</div>')

def two_garlands(keys, c, ink="#111", body_size=21, lbl_size=24, gap=26, vh=300, sc=1.0):
    esc = G["esc"]
    vis = [f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc:.2f});transform-origin:bottom center">{rope_garland(TUT, 330, 300, 9, 50, ink=ink)}</div></div>',
           f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc:.2f});transform-origin:bottom center">{rope_garland(keys, 330, 300, 9, 50, ink=ink)}</div></div>']
    cols = ""
    for v, (t, body) in zip(vis, c["ex_items"]):
        cols += (f'<div style="flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;gap:10px">{v}'
                 f'<div style="font-size:{body_size}px;line-height:1.3;text-align:center"><b style="font-size:{lbl_size}px;display:block;margin-bottom:4px">{esc(t)}</b>{esc(body)}</div></div>')
    return f'<div style="display:flex;gap:{gap}px;align-items:flex-start;width:100%">{cols}</div>'

def rule_cards(c, cls="alts", title_size=24, body_size=18, font=None):
    esc = G["esc"]
    out = f'<div class="{cls}"' + (f' style="font-family:\'{font}\'"' if font else '') + '>'
    n = len(c["alts"])
    for i, (t, body) in enumerate(c["alts"]):
        span = ' style="grid-column:1/-1"' if (i == n - 1 and n % 2 == 1) else ''
        out += f'<div class="alt"{span}><b style="font-size:{title_size}px"><span class="num">{i+1}</span>{esc(t)}</b><span style="font-size:{body_size}px">{esc(body)}</span></div>'
    return out + '</div>'

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

# ---------------------------------------------------------------- STIJL 1
def s1_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, cursor_svg, arrow_svg, balloon = G["esc"], G["hl"], G["cursor_svg"], G["arrow_svg"], G["balloon"]
    s1_footer, logo_img, rot, STX_FULL = G["s1_footer"], G["logo_img"], G["rot"], G["STX_FULL"]
    S = []
    pills = c["cover_pills"]
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:86px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
  <div class="pill" style="background:{b['c1']};color:{b['c1t']};right:60px;top:130px;transform:rotate({rot(b,-4)}deg)">{cursor_svg(b['c1'])}{esc(pills[0])}</div>
  <div class="pill" style="background:{b['c2']};color:{b['c2t']};right:90px;top:835px;transform:rotate({rot(b,3)}deg)">{cursor_svg(b['c2'])}{esc(pills[1])}</div>
  <div class="pill" style="background:{b['c3']};color:{b['c3t']};left:90px;top:880px;transform:rotate({rot(b,-2)}deg)">{cursor_svg(b['c3'])}{esc(pills[2])}</div>
  <div style="position:absolute;left:150px;top:960px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:310px;right:90px;top:1020px;font-size:29px;line-height:1.35">{esc(c['cover_sub'])}</div>
  {s1_footer(b, stx_h=84)}
</section>""")
    L = sum(len(s) for s in c["steps"]); sfs = 26 if L <= 560 else (24 if L <= 600 else 23)
    steps = "".join(f'<div class="step" style="font-size:{sfs}px"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:110px;width:790px;height:380px">
    <h2 data-fit style="font-size:66px;max-height:300px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:872px;top:130px;transform:scale(1.15);transform-origin:top left">{duplet(b['hero'] if b['hero'] in G['SX'] else P[0], 56, b['ink'])}</div>
  <div style="position:absolute;left:110px;top:500px">{arrow_svg(b['ink'], 140, 120)}</div>
  <div class="box" style="left:230px;top:515px;width:780px;height:655px;padding:24px 34px">
    <div style="font-size:25px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:500px;padding:34px 44px">
    <h2 data-fit style="font-size:48px;max-height:130px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:14px;font-size:21px;line-height:1.32">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:720px;height:420px">
    <div class="card" style="top:0;height:320px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:380px;padding:24px 30px">{facts_grid(c['rule1_facts'], 'facts', 46, 18)}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div style="position:absolute;left:80px;right:80px;top:325px;font-size:25px;line-height:1.35" class="body">{esc(c['rule2_body'])}</div>
  <div style="position:absolute;left:70px;right:70px;top:405px">{rule_cards(c, "alts five", 26, 20, b["ui"])}</div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:700px;padding:30px 28px 26px">
    <h2 data-fit style="font-size:50px;margin-bottom:10px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    {two_garlands(P, c, b['ink'], 20, 23, 24, 330, 1.0)}
  </div>
  <div class="box" style="left:70px;top:885px;width:940px;padding:18px 40px"><div class="body" style="font-size:21px">{esc(c['example_body'])}</div><div style="margin-top:10px">{chips_row(c['chips'], b['ink'], 'transparent', True)}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:130px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:480px;display:flex;flex-direction:column;gap:14px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:20px 32px"><div style="font-size:23px;line-height:1.32">{esc(c['client_answer'])}</div></div>
    <div class="card" style="position:relative;left:auto;right:auto;padding:16px 32px"><div style="font-size:22px;font-weight:{b['body_b']};margin-bottom:2px">{esc(c['avoid_lead'])}</div>{avoid_list(c, 'avoid')}</div>
    <div class="body" style="font-size:18px;line-height:1.3;padding-right:40px">{esc(c['client_body'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:80px;right:80px;top:200px;max-height:420px;font-size:88px;text-align:center">{esc(c['cta_title'])}</h1>
  <div style="position:absolute;left:120px;right:120px;top:650px;font-size:30px;line-height:1.4;text-align:center">{esc(c['cta_sub'])}</div>
  <div style="position:absolute;left:0;right:0;top:800px;text-align:center"><span class="url">{esc(c['cta_url'])}</span></div>
  <div style="position:absolute;left:200px;top:745px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:0;right:0;top:980px;display:flex;justify-content:center;align-items:center;gap:40px">{logo_img(b, height=b['cta_logo_h'])}<span style="font-size:40px;opacity:.5">×</span><img src="file://{STX_FULL}" style="height:96px"></div>
</section>""")
    return S

# ---------------------------------------------------------------- STIJL 2
def s2_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, balloon, rot = G["esc"], G["hl"], G["balloon"], G["rot"]
    s2_footer, STX_WT = G["s2_footer"], G["STX_WT"]
    S = []
    S.append(f"""
<section class="slide s2">
  <div class="sq" style="left:70px;top:70px;width:200px;height:120px"><img src="file://{b['logo']}" style="max-width:170px;max-height:90px"></div>
  <div class="conn" style="left:170px;top:190px;width:140px;height:380px"></div>
  <div style="position:absolute;left:300px;top:552px;width:0;height:0;border-left:22px solid #fff;border-top:14px solid transparent;border-bottom:14px solid transparent"></div>
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:62px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.08)">{sizes_visual(P, c, '#111')}</div></div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    L = sum(len(s) for s in c["steps"]); sfs = 24 if L <= 560 else (23 if L <= 640 else 22)
    steps = "".join(f'<div class="step" style="font-size:{sfs}px"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px;font-size:21px"><b style="font-size:31px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:790px;width:930px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:300px;padding:16px 24px;box-sizing:border-box;background:#fff;color:#111;align-items:center;justify-content:flex-end"><div style="transform:scale(1.0);transform-origin:bottom center">{sizes_row(P, c, '#111')}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:50px;max-height:150px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:340px;padding:22px 28px;box-sizing:border-box;align-items:stretch;background:#fff">{facts_grid(c['rule1_facts'], 'facts onwhite', 40, 17)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:760px;font-size:20px;line-height:1.32">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:52px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div class="body" style="position:absolute;left:70px;right:70px;top:330px;font-size:24px">{esc(c['rule2_body'])}</div>
  <div class="frame" style="left:70px;top:420px;width:940px;transform:rotate({rot(b,1)}deg)">
    <div class="ph" style="height:auto;padding:24px 28px;box-sizing:border-box;align-items:stretch;background:#fff;color:#111">{rule_cards(c, 'alts onwhite', 22, 16)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:54px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:300px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:auto;padding:20px 20px;box-sizing:border-box;align-items:flex-start;background:#fff;color:#111">{two_garlands(P, c, '#111', 19, 22, 18, 280, .9)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1000px;font-size:20px">{esc(c['example_body'])}</div>
  <div style="position:absolute;left:70px;right:70px;top:1110px">{chips_row(c['chips'], '#fff', 'transparent', True)}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:150px">{esc(c['client_title'])}</h2>
  <div class="frame" style="left:70px;top:340px;width:940px">
    <div class="ph" style="height:auto;padding:26px 34px;box-sizing:border-box;align-items:flex-start;background:#fff">
      <div style="font-size:28px;line-height:1.3;color:{b['ink']};font-style:italic">{esc(c['client_question'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:12px 0"></div>
      <div style="font-size:21px;line-height:1.32;color:{b['ink']}">{esc(c['client_answer'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:12px 0"></div>
      <div style="font-size:21px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['avoid_lead'])}</div>
      {avoid_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1062px;font-size:18px;line-height:1.3">{esc(c['client_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['cta_label'])}</div>
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:170px;max-height:380px;font-size:80px">{esc(c['cta_title'])}</h1>
  <div class="frame" style="left:160px;top:600px;width:760px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:260px;background:#fff"><img src="file://{b['logo']}" style="max-width:600px;max-height:200px"></div>
  </div>
  <div style="position:absolute;left:0;right:0;top:930px;text-align:center"><span class="url">{esc(c['cta_url'])}</span></div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1060px;text-align:center;font-size:28px">{esc(c['cta_sub'])}</div>
  <div style="position:absolute;left:0;right:0;bottom:50px;text-align:center"><img src="file://{STX_WT}" style="height:80px;display:inline-block"></div>
</section>""")
    return S

# ---------------------------------------------------------------- STIJL 3
def s3_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, balloon, rot = G["esc"], G["hl"], G["balloon"], G["rot"]
    s3_footer, STX_FULL, PAL_SETS = G["s3_footer"], G["STX_FULL"], G["PAL_SETS"]
    loud = PAL_SETS[(b["pal_idx"] + 5) % len(PAL_SETS)]
    S = []
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:50px;right:50px;top:60px;max-height:400px;font-size:84px;text-align:center;line-height:1.08">{hl(c['s3_cover_a'])} {esc(c['s3_cover_b'])} {esc(c['s3_cover_c'])}<br><span class="hl">{esc(c['s3_cover_d'])}</span></h1>
  <div class="vsmark" style="top:520px">VS</div>
  <div class="lblw" style="left:110px;top:500px;transform:rotate({rot(b,-4)}deg)">{esc(c['s3_left'])}<br><span class="meta">● {esc(c['s3_left_meta'])}</span></div>
  <div class="lbld" style="right:110px;top:500px;transform:rotate({rot(b,4)}deg)">{esc(c['s3_right'])}<br><span class="meta" style="background:rgba(255,255,255,.18)">● {esc(c['s3_right_meta'])}</span></div>
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{loose_visual(loud, c, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{full_visual(P, c, b['ink'])}</div>
  <div class="vsbadge" style="left:485px;top:850px">vs</div>
  {s3_footer(b, stx_h=60)}
</section>""")
    old_tags = "".join(f'<span class="chip chipd">{esc(t)}</span>' + ('<span class="plus">+</span>' if i < len(c["s3_old_tags"])-1 else '') for i, t in enumerate(c["s3_old_tags"]))
    new_tags = "".join(f'<span class="chip chipb">{esc(t)}</span>' + ('<span class="plus" style="color:#fff">+</span>' if i < len(c["s3_new_tags"])-1 else '') for i, t in enumerate(c["s3_new_tags"]))
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:60px;right:60px;top:80px;max-height:130px;font-size:92px;text-align:center">{esc(c['s3_changed_title'])}</h1>
  <div class="pilltitle" style="top:232px">{esc(c['s3_old_lbl'])}</div>
  <div class="cardw" style="left:70px;right:70px;top:260px;height:300px;text-align:center;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div>{old_tags}</div>
    <div class="strike" style="font-size:34px">{esc(c['s3_old_quote'])}</div>
  </div>
  <div class="downarrow" style="top:590px">↓</div>
  <div class="pilltitle" style="top:692px;background:#fff;color:{b['bright_text']}">{esc(c['s3_new_lbl'])}</div>
  <div class="cardd" style="left:70px;right:70px;top:720px;height:370px;text-align:center;display:flex;flex-direction:column;justify-content:center;align-items:center">
    <div style="max-width:880px">{new_tags}</div>
    <div class="quote" style="font-size:28px">{esc(c['s3_new_quote'])}</div>
    <div class="badge">◉ {esc(c['s3_new_badge'])}</div>
  </div>
  <div class="bottom" style="top:1125px">{esc(c['s3_changed_bottom'])}</div>
  {s3_footer(b)}
</section>""")
    def topic_slide(topic, old_text, new_visual, quote, label=None):
        label = label or c['s3_topic_lbl']; old_meta = " + ".join(c['s3_old_tags'])
        return f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(label)}</span><span class="v">{esc(topic)}</span></div>
  <div class="cardd" style="left:70px;top:230px;width:440px;height:600px;padding:34px 36px">
    <span class="oldlbl">{esc(c['s3_old_lbl'])}</span>
    <div class="strike" style="font-size:40px;line-height:1.2;color:#fff;text-decoration-color:#E03131;margin-top:34px;font-weight:700;font-family:'{b['ui']}'">{esc(old_text)}</div>
    <div style="position:absolute;left:36px;right:36px;bottom:34px;font-size:22px;opacity:.55;font-weight:600">{esc(old_meta)}</div>
  </div>
  <div class="cardw onwhite" style="left:570px;top:230px;width:440px;height:600px;padding:34px 36px">
    <span class="newlbl">{esc(c['s3_new_lbl'])}</span>
    <div style="margin-top:30px;display:flex;justify-content:center">{new_visual}</div>
  </div>
  <div class="bottom" style="top:890px;font-size:33px;font-weight:700">{esc(quote)}</div>
  {s3_footer(b)}
</section>"""
    vis1 = f'<div style="width:100%">{facts_grid(c["rule1_facts"], "facts s3facts", 34, 16)}</div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="width:100%">{rule_cards(c, "alts s3alts", 17, 13)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['s3_example_topic']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:640px;padding:30px 24px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;gap:16px">
    {two_garlands(P, c, '#111', 20, 23, 18, 340, 1.05)}
    <div style="width:100%">{chips_row(c['chips'], '#111', '#fff', True)}</div>
  </div>
  <div class="bottom" style="top:920px;font-size:29px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    vis6 = (f'<div style="width:100%"><div style="font-size:22px;line-height:1.3;font-style:italic;margin-bottom:12px">{esc(c["client_question"])}</div>'
            f'<div style="font-size:17px;line-height:1.3;margin-bottom:12px">{esc(c["client_answer"])}</div>'
            f'<div style="font-size:17px;font-weight:800;margin-bottom:2px">{esc(c["avoid_lead"])}</div>{avoid_list(c, "s3steps")}</div>')
    S.append(topic_slide(c["s3_client_topic"], c["s3_client_old"], vis6, c["s3_client_quote"], label=c["s3_client_lbl"]))
    S.append(f"""
<section class="slide s3">
  <div class="pilltitle" style="top:90px">{esc(c['s3_cta_kicker'])}</div>
  <h1 data-fit style="position:absolute;left:60px;right:60px;top:180px;max-height:420px;font-size:88px;text-align:center">{esc(c['cta_title'])}</h1>
  <div class="cardw" style="left:160px;right:160px;top:640px;height:240px;display:flex;align-items:center;justify-content:center"><img src="file://{b['logo']}" style="max-width:560px;max-height:170px"></div>
  <div style="position:absolute;left:0;right:0;top:930px;text-align:center"><span class="url">{esc(c['cta_url'])}</span></div>
  <div class="bottom" style="top:1060px;font-size:26px;font-weight:600">{esc(c['cta_sub'])}</div>
  <div style="position:absolute;left:0;right:0;bottom:44px;text-align:center"><span class="logocard"><img src="file://{STX_FULL}" style="height:64px"></span></div>
</section>""")
    return S

EXTRA_CSS = """
.s1 .step{font-size:22px;margin-top:8px;line-height:1.25}
.s1 .avoid .step{font-size:20px;margin-top:6px;line-height:1.22}
.s2 .onwhite .step{color:#111;font-size:18px;margin-top:5px;line-height:1.22}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:10px;font-size:15px;line-height:1.25;margin-top:5px}
.s3 .s3steps .step b{min-width:24px;font-weight:800}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:16px;width:100%}
.facts .fact{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:3px solid #111;border-radius:18px;padding:14px 12px;gap:6px;line-height:1.15}
.facts .fact b{letter-spacing:-.01em;line-height:1;white-space:nowrap}
.facts.onwhite .fact{color:#111}
.facts.s3facts{grid-template-columns:1fr;gap:12px}
.facts.s3facts .fact{border-width:2px;padding:10px 14px;border-radius:14px;align-items:flex-start;text-align:left;gap:3px}
.facts.s3facts .fact b{white-space:normal}
.alts{display:grid;grid-template-columns:1fr 1fr;gap:16px;width:100%}
.alts .alt{display:flex;flex-direction:column;gap:6px;border:3px solid #111;border-radius:18px;padding:18px 22px;background:#fff;line-height:1.3}
.alts .alt b{display:flex;align-items:center;gap:12px;line-height:1.15}
.alts .alt .num{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:#111;color:#fff;font-size:20px;flex:0 0 36px}
.alts.onwhite .alt{color:#111;border-color:#111}
.alts.five{gap:16px}
.alts.five .alt{padding:20px 24px;gap:8px;min-height:212px;justify-content:center}
.alts.five .alt .num{width:40px;height:40px;font-size:22px;flex-basis:40px}
.alts.s3alts{grid-template-columns:1fr;gap:7px}
.alts.s3alts .alt{border-width:2px;padding:7px 12px;border-radius:14px;gap:2px}
.alts.s3alts .alt .num{width:24px;height:24px;font-size:13px;flex-basis:24px}
.tchip{display:inline-block;border:2px solid #111;border-radius:999px;padding:6px 14px;font-size:17px;font-weight:700;white-space:nowrap}
"""
