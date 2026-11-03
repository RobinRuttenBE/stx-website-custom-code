# -*- coding: utf-8 -*-
"""Topic: 'What is double stuffing and how do you calculate the colour?'
(sempertexeurope.com/en_GB/blog/what-is-double-stuffing-balloons).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=doublestuff.
Uit de blog: binnenballon volledig in de buitenballon, samen opblazen, het licht mengt de 2 kleuren; Crystal Clear 390
als buitenlaag maakt de binnenkleur zachter en dieper; volgorde binnen/buiten telt; matte in glanzend verschilt van 2x matte;
receptenboek met beide codes; gratis Double Stuffing Calculator (preview is een benadering: maat, licht en finish spelen mee).
De combinaties op slide 5 komen uit het palet van de distri; het resultaat is een simulatie, geen officiële mengkleur."""

G = {}
def setup(g): G.update(g)
CRYSTAL = "Crystal Clear 390"

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["1 in 1…", "Crystal Clear 390…", "Volgorde telt…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "Eén ballon in een andere, samen opblazen. Het licht mengt 2 kleuren tot een nieuwe.", "steps_lead": "Zo werkt het:",
    "steps": ["Steek de binnenballon volledig in de buitenballon", "Blaas ze samen op, als één ballon", "Het licht gaat door de buitenste laag: je ziet de optische menging"],
    "steps_label": "De basis",
    "rule1_label": "Regel 1", "rule1_title": "Crystal Clear 390 buiten: zachter en dieper",
    "rule1_body": "Een transparante buitenlaag is het instappunt. De binnenkleur wordt zachter en krijgt diepte, precies de premium pastellook die klanten vragen. Een felle kleur in Crystal Clear 390 oogt meteen een klasse rustiger.",
    "rule2_label": "Regel 2", "rule2_title": "De volgorde telt, en de textuur ook",
    "rule2_body": "De buitenballon bepaalt hoeveel licht de binnenballon bereikt. Wissel binnen en buiten en je krijgt een ander resultaat. Matte in glanzend oogt anders dan 2 keer matte. Test de combinatie in de calculator voor je bestelt.",
    "example_label": "Voorbeeld", "example_title": "3 combinaties uit je eigen palet",
    "combos": [[CRYSTAL, "{p0}", "zachte pastelversie"], ["{p1}", "{p2}", "dieper en voller"], ["{p3}", "{p0}", "een nieuwe tint"]],
    "example_body": "Buiten {p1}, binnen {p2}: dieper en voller. Buiten {p3}, binnen {p0}: een tint die als losse ballon niet bestaat. En {p0} in Crystal Clear 390 wordt een zachte pastel. Het resultaat hier is een benadering: maat, licht en finish spelen mee.",
    "client_label": "Klantgesprek", "client_title": "Wat je antwoordt als de klant vraagt",
    "client_answers": [
        "Ja. Ik kies een binnen- en buitenballon uit de echte Sempertex kleuren en zie de mengkleur vooraf in de calculator. Stuur me je kleurcode, dan test ik 2 combinaties.",
        "Dat kan. Ik stop die kleur in een Crystal Clear 390: zachter en met meer diepte. Wil je nog zachter, dan wissel ik de binnenkleur.",
        "Ja, als ik het recept bewaar. Ik noteer beide codes, de volgorde en de maat. Zelfde codes, zelfde licht, zelfde resultaat.",
    ],
    "avoid_lead": "Je receptenboek, elke keer:",
    "steps5": ["Noteer beide kleurcodes en welke binnen zit", "Test de combinatie in de calculator voor je bestelt", "Wissel binnen en buiten met 1 klik en vergelijk", "Zelfde maat, licht en finish voor hetzelfde resultaat", "Bestel beide kleuren samen"],
    "client_body": "De gratis Double Stuffing Calculator op sempertexeurope.com/tools toont de mengkleur voor je iets opblaast, met filter op textuur: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk en Reflex.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Double stuffing met Sempertex", "s3_cover_b": "op hoop", "s3_cover_c": "vs.", "s3_cover_d": "uitgerekend",
    "s3_left": "OP HOOP", "s3_right": "UITGEREKEND", "s3_left_meta": "zakken open en kijken", "s3_right_meta": "mengkleur vooraf",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Proberen", "Hopen"], "s3_new_tags": ["Crystal Clear 390", "Volgorde", "Receptenboek"],
    "s3_new_quote": "“Ik kies binnen en buiten uit de echte Sempertex kleuren, zie de mengkleur vooraf en noteer beide codes.”", "s3_new_badge": "1 ballon in 1 ballon",
    "s3_changed_bottom": "Zelfde 2 ballonnen, zelfde klant.\nDe kleur klopt al voor je opblaast.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Fel is fel, daar is niets aan te doen",
    "s3_rule1_quote": "“Een felle kleur in Crystal Clear 390 wordt zachter en krijgt diepte: de premium pastellook.”",
    "s3_rule2_topic": "Volgorde", "s3_rule2_old": "Welke binnen zit maakt niet uit",
    "s3_rule2_quote": "“De buitenballon bepaalt hoeveel licht binnenkomt. Wissel ze en je krijgt een andere kleur.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_quote": "“Buiten {p1}, binnen {p2}. Buiten {p3}, binnen {p0}. En {p0} in Crystal Clear 390.”",
    "s3_client_lbl": "KLANT", "s3_client_topic": "Klantgesprek",
    "s3_client_quote": "“Stuur me je kleurcode. Ik test 2 combinaties en je ziet de mengkleur voor ik iets opblaas.”",
    "s3_cta_kicker": "Je double stuffing recept voor de volgende job",
    "outer_lbl": "buiten", "inner_lbl": "binnen", "result_lbl": "resultaat", "approx_lbl": "benadering", "swap_lbl": "gewisseld",
},
"en": {
    "cover_pills": ["1 in 1…", "Crystal Clear 390…", "Order matters…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "One balloon inside another, inflated together. Light blends 2 colours into a new one.", "steps_lead": "How it works:",
    "steps": ["Push the inner balloon fully inside the outer one", "Inflate them together, as one balloon", "Light passes through the outer layer: you see the optical mix"],
    "steps_label": "The basics",
    "rule1_label": "Rule 1", "rule1_title": "Crystal Clear 390 on the outside: softer and deeper",
    "rule1_body": "A transparent outer layer is the entry point. The inner colour turns softer and gains depth, exactly the premium pastel look clients ask for. A bright colour inside Crystal Clear 390 instantly looks a class calmer.",
    "rule2_label": "Rule 2", "rule2_title": "Order matters, and so does texture",
    "rule2_body": "The outer balloon controls how much light reaches the inner one. Swap inner and outer and you get a different result. Matte inside shiny looks different from matte twice. Test the combination in the calculator before you order.",
    "example_label": "Example", "example_title": "3 combinations from your own palette",
    "combos": [[CRYSTAL, "{p0}", "soft pastel version"], ["{p1}", "{p2}", "deeper and fuller"], ["{p3}", "{p0}", "a brand new shade"]],
    "example_body": "{p1} outside, {p2} inside: deeper and fuller. {p3} outside, {p0} inside: a shade that doesn't exist as a single balloon. And {p0} inside Crystal Clear 390 becomes a soft pastel. The result shown here is an approximation: size, light and finish all play a part.",
    "client_label": "Client chat", "client_title": "What you answer when the client asks",
    "client_answers": [
        "Yes. I pick an inner and an outer balloon from the real Sempertex colours and see the blend in the calculator first. Send me your colour code and I'll test 2 combinations.",
        "I can. I put that colour inside a Crystal Clear 390: softer, with more depth. Want it softer still, I swap the inner colour.",
        "Yes, as long as I keep the recipe. I note both codes, the order and the size. Same codes, same light, same result.",
    ],
    "avoid_lead": "Your recipe book, every time:",
    "steps5": ["Note both colour codes and which one goes inside", "Test the combination in the calculator before ordering", "Swap inner and outer with 1 click and compare", "Same size, light and finish for the same result", "Order both colours together"],
    "client_body": "The free Double Stuffing Calculator at sempertexeurope.com/tools shows the blend before you inflate anything, filtered by texture: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk and Reflex.",
    "cta_label": "Order",
    "s3_cover_a": "Double stuffing with Sempertex", "s3_cover_b": "by hope", "s3_cover_c": "vs.", "s3_cover_d": "worked out",
    "s3_left": "BY HOPE", "s3_right": "WORKED OUT", "s3_left_meta": "open bags and see", "s3_right_meta": "blend shown first",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Trial", "Hope"], "s3_new_tags": ["Crystal Clear 390", "Order", "Recipe book"],
    "s3_new_quote": "“I pick inner and outer from the real Sempertex colours, see the blend first and note both codes.”", "s3_new_badge": "1 balloon in 1 balloon",
    "s3_changed_bottom": "Same 2 balloons, same client.\nThe colour is right before you inflate.",
    "s3_topic_lbl": "RULE", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Bright is bright, nothing to be done",
    "s3_rule1_quote": "“A bright colour inside Crystal Clear 390 turns softer and gains depth: the premium pastel look.”",
    "s3_rule2_topic": "Order", "s3_rule2_old": "Which one goes inside doesn't matter",
    "s3_rule2_quote": "“The outer balloon controls how much light gets in. Swap them and you get a different colour.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_quote": "“{p1} outside, {p2} inside. {p3} outside, {p0} inside. And {p0} inside Crystal Clear 390.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Client chat",
    "s3_client_quote": "“Send me your colour code. I'll test 2 combinations and you'll see the blend before I inflate anything.”",
    "s3_cta_kicker": "Your double stuffing recipe for the next job",
    "outer_lbl": "outside", "inner_lbl": "inside", "result_lbl": "result", "approx_lbl": "approximation", "swap_lbl": "swapped",
},
"de": {
    "cover_pills": ["1 in 1…", "Crystal Clear 390…", "Reihenfolge zählt…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Double Stuffing…",
    "steps_title": "Ein Ballon im anderen, zusammen aufgeblasen. Das Licht mischt 2 Farben zu einer neuen.", "steps_lead": "So funktioniert es:",
    "steps": ["Den inneren Ballon komplett in den äußeren stecken", "Beide zusammen aufblasen, wie einen Ballon", "Das Licht geht durch die äußere Schicht: du siehst die optische Mischung"],
    "steps_label": "Die Basis",
    "rule1_label": "Regel 1", "rule1_title": "Crystal Clear 390 außen: weicher und tiefer",
    "rule1_body": "Eine transparente Außenschicht ist der Einstieg. Die Innenfarbe wird weicher und bekommt Tiefe, genau der Premium-Pastell-Look, den Kunden wollen. Eine knallige Farbe in Crystal Clear 390 wirkt sofort eine Klasse ruhiger.",
    "rule2_label": "Regel 2", "rule2_title": "Die Reihenfolge zählt, die Textur auch",
    "rule2_body": "Der äußere Ballon bestimmt, wie viel Licht den inneren erreicht. Tausch innen und außen und du bekommst ein anderes Ergebnis. Matt in Glänzend sieht anders aus als 2-mal matt. Teste die Kombination im Rechner, bevor du bestellst.",
    "example_label": "Beispiel", "example_title": "3 Kombinationen aus deiner Palette",
    "combos": [[CRYSTAL, "{p0}", "weiche Pastellversion"], ["{p1}", "{p2}", "tiefer und voller"], ["{p3}", "{p0}", "ein neuer Ton"]],
    "example_body": "Außen {p1}, innen {p2}: tiefer und voller. Außen {p3}, innen {p0}: ein Ton, den es als einzelnen Ballon nicht gibt. Und {p0} in Crystal Clear 390 wird ein weiches Pastell. Das Ergebnis hier ist eine Annäherung: Größe, Licht und Finish spielen mit.",
    "client_label": "Kundengespräch", "client_title": "Was du antwortest, wenn der Kunde fragt",
    "client_answers": [
        "Ja. Ich wähle einen inneren und einen äußeren Ballon aus den echten Sempertex Farben und sehe die Mischfarbe vorher im Rechner. Schick mir deinen Farbcode, dann teste ich 2 Kombinationen.",
        "Geht. Ich stecke die Farbe in einen Crystal Clear 390: weicher und mit mehr Tiefe. Soll es noch weicher sein, tausche ich die Innenfarbe.",
        "Ja, wenn ich das Rezept aufhebe. Ich notiere beide Codes, die Reihenfolge und die Größe. Gleiche Codes, gleiches Licht, gleiches Ergebnis.",
    ],
    "avoid_lead": "Dein Rezeptbuch, jedes Mal:",
    "steps5": ["Beide Farbcodes notieren und welcher innen sitzt", "Die Kombination im Rechner testen, bevor du bestellst", "Innen und außen mit 1 Klick tauschen und vergleichen", "Gleiche Größe, Licht und Finish für das gleiche Ergebnis", "Beide Farben zusammen bestellen"],
    "client_body": "Der kostenlose Double Stuffing Rechner auf sempertexeurope.com/tools zeigt die Mischfarbe, bevor du etwas aufbläst, mit Filter nach Textur: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk und Reflex.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Double Stuffing mit Sempertex", "s3_cover_b": "auf gut Glück", "s3_cover_c": "vs.", "s3_cover_d": "berechnet",
    "s3_left": "AUF GUT GLÜCK", "s3_right": "BERECHNET", "s3_left_meta": "Tüten auf und schauen", "s3_right_meta": "Mischfarbe vorher",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Probieren", "Hoffen"], "s3_new_tags": ["Crystal Clear 390", "Reihenfolge", "Rezeptbuch"],
    "s3_new_quote": "“Ich wähle innen und außen aus den echten Sempertex Farben, sehe die Mischfarbe vorher und notiere beide Codes.”", "s3_new_badge": "1 Ballon in 1 Ballon",
    "s3_changed_bottom": "Gleiche 2 Ballons, gleicher Kunde.\nDie Farbe stimmt, bevor du aufbläst.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Knallig bleibt knallig, da geht nichts",
    "s3_rule1_quote": "“Eine knallige Farbe in Crystal Clear 390 wird weicher und bekommt Tiefe: der Premium-Pastell-Look.”",
    "s3_rule2_topic": "Reihenfolge", "s3_rule2_old": "Welcher innen sitzt, ist egal",
    "s3_rule2_quote": "“Der äußere Ballon bestimmt, wie viel Licht reinkommt. Tausch sie und du bekommst eine andere Farbe.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_quote": "“Außen {p1}, innen {p2}. Außen {p3}, innen {p0}. Und {p0} in Crystal Clear 390.”",
    "s3_client_lbl": "KUNDE", "s3_client_topic": "Kundengespräch",
    "s3_client_quote": "“Schick mir deinen Farbcode. Ich teste 2 Kombinationen und du siehst die Mischfarbe, bevor ich etwas aufblase.”",
    "s3_cta_kicker": "Dein Double-Stuffing-Rezept für den nächsten Job",
    "outer_lbl": "außen", "inner_lbl": "innen", "result_lbl": "Ergebnis", "approx_lbl": "Annäherung", "swap_lbl": "getauscht",
},
"fr": {
    "cover_pills": ["1 dans 1…", "Crystal Clear 390…", "L'ordre compte…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "Un ballon dans un autre, gonflés ensemble. La lumière mélange 2 couleurs en une nouvelle.", "steps_lead": "Comment ça marche :",
    "steps": ["Glisse le ballon intérieur entièrement dans le ballon extérieur", "Gonfle-les ensemble, comme un seul ballon", "La lumière traverse la couche extérieure : tu vois le mélange optique"],
    "steps_label": "La base",
    "rule1_label": "Règle 1", "rule1_title": "Crystal Clear 390 à l'extérieur : plus doux et plus profond",
    "rule1_body": "Une couche extérieure transparente, c'est le point d'entrée. La couleur intérieure devient plus douce et gagne en profondeur, exactement le rendu pastel premium que les clients demandent. Une couleur vive dans un Crystal Clear 390 paraît tout de suite plus calme.",
    "rule2_label": "Règle 2", "rule2_title": "L'ordre compte, la texture aussi",
    "rule2_body": "Le ballon extérieur décide de la lumière qui atteint l'intérieur. Inverse intérieur et extérieur et tu obtiens un autre résultat. Mat dans brillant ne ressemble pas à 2 fois mat. Teste la combinaison dans le calculateur avant de commander.",
    "example_label": "Exemple", "example_title": "3 combinaisons de ta propre palette",
    "combos": [[CRYSTAL, "{p0}", "version pastel douce"], ["{p1}", "{p2}", "plus profond, plus plein"], ["{p3}", "{p0}", "une teinte inédite"]],
    "example_body": "Extérieur {p1}, intérieur {p2} : plus profond et plus plein. Extérieur {p3}, intérieur {p0} : une teinte qui n'existe pas en ballon seul. Et {p0} dans un Crystal Clear 390 devient un pastel doux. Le résultat ici est une approximation : taille, lumière et finition jouent.",
    "client_label": "Discussion client", "client_title": "Ce que tu réponds quand le client demande",
    "client_answers": [
        "Oui. Je choisis un ballon intérieur et un extérieur parmi les vraies couleurs Sempertex et je vois le mélange d'abord dans le calculateur. Envoie-moi ton code couleur, je teste 2 combinaisons.",
        "C'est possible. Je mets cette couleur dans un Crystal Clear 390 : plus doux, avec plus de profondeur. Tu la veux encore plus douce, je change la couleur intérieure.",
        "Oui, si je garde la recette. Je note les deux codes, l'ordre et la taille. Mêmes codes, même lumière, même résultat.",
    ],
    "avoid_lead": "Ton carnet de recettes, à chaque fois :",
    "steps5": ["Note les deux codes couleur et lequel va à l'intérieur", "Teste la combinaison dans le calculateur avant de commander", "Inverse intérieur et extérieur en 1 clic et compare", "Même taille, lumière et finition pour le même résultat", "Commande les deux couleurs ensemble"],
    "client_body": "Le calculateur Double Stuffing gratuit sur sempertexeurope.com/tools montre le mélange avant de gonfler quoi que ce soit, avec filtre par texture : Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk et Reflex.",
    "cta_label": "Commander",
    "s3_cover_a": "Le double stuffing avec Sempertex", "s3_cover_b": "au hasard", "s3_cover_c": "vs.", "s3_cover_d": "calculé",
    "s3_left": "AU HASARD", "s3_right": "CALCULÉ", "s3_left_meta": "on gonfle et on voit", "s3_right_meta": "mélange visible avant",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Essayer", "Espérer"], "s3_new_tags": ["Crystal Clear 390", "Ordre", "Carnet de recettes"],
    "s3_new_quote": "“Je choisis intérieur et extérieur parmi les vraies couleurs Sempertex, je vois le mélange d'abord et je note les deux codes.”", "s3_new_badge": "1 ballon dans 1 ballon",
    "s3_changed_bottom": "Mêmes 2 ballons, même client.\nLa couleur est juste avant de gonfler.",
    "s3_topic_lbl": "RÈGLE", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Vif reste vif, rien à faire",
    "s3_rule1_quote": "“Une couleur vive dans un Crystal Clear 390 devient plus douce et gagne en profondeur : le rendu pastel premium.”",
    "s3_rule2_topic": "Ordre", "s3_rule2_old": "Lequel va à l'intérieur, peu importe",
    "s3_rule2_quote": "“Le ballon extérieur décide de la lumière qui entre. Inverse-les et tu obtiens une autre couleur.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_quote": "“Extérieur {p1}, intérieur {p2}. Extérieur {p3}, intérieur {p0}. Et {p0} dans un Crystal Clear 390.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Discussion client",
    "s3_client_quote": "“Envoie-moi ton code couleur. Je teste 2 combinaisons et tu vois le mélange avant que je gonfle quoi que ce soit.”",
    "s3_cta_kicker": "Ta recette double stuffing pour la prochaine prestation",
    "outer_lbl": "extérieur", "inner_lbl": "intérieur", "result_lbl": "résultat", "approx_lbl": "approximation", "swap_lbl": "inversé",
},
"it": {
    "cover_pills": ["1 in 1…", "Crystal Clear 390…", "L'ordine conta…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "Un palloncino dentro l'altro, gonfiati insieme. La luce fonde 2 colori in uno nuovo.", "steps_lead": "Come funziona:",
    "steps": ["Inserisci il palloncino interno del tutto in quello esterno", "Gonfiali insieme, come un unico palloncino", "La luce attraversa lo strato esterno: vedi la fusione ottica"],
    "steps_label": "La base",
    "rule1_label": "Regola 1", "rule1_title": "Crystal Clear 390 all'esterno: più morbido e profondo",
    "rule1_body": "Uno strato esterno trasparente è il punto di partenza. Il colore interno diventa più morbido e guadagna profondità, esattamente il look pastello premium che i clienti chiedono. Un colore acceso dentro un Crystal Clear 390 appare subito una spanna più calmo.",
    "rule2_label": "Regola 2", "rule2_title": "L'ordine conta, e anche la texture",
    "rule2_body": "Il palloncino esterno decide quanta luce raggiunge quello interno. Scambia interno ed esterno e ottieni un risultato diverso. Opaco dentro lucido è diverso da 2 volte opaco. Prova la combinazione nel calcolatore prima di ordinare.",
    "example_label": "Esempio", "example_title": "3 combinazioni dalla tua palette",
    "combos": [[CRYSTAL, "{p0}", "versione pastello morbida"], ["{p1}", "{p2}", "più profondo e pieno"], ["{p3}", "{p0}", "una tinta nuova"]],
    "example_body": "Esterno {p1}, interno {p2}: più profondo e pieno. Esterno {p3}, interno {p0}: una tinta che da sola non esiste. E {p0} dentro un Crystal Clear 390 diventa un pastello morbido. Il risultato qui è un'approssimazione: misura, luce e finitura contano.",
    "client_label": "Dialogo con il cliente", "client_title": "Cosa rispondi quando il cliente chiede",
    "client_answers": [
        "Sì. Scelgo un palloncino interno e uno esterno tra i veri colori Sempertex e vedo prima la fusione nel calcolatore. Mandami il tuo codice colore e provo 2 combinazioni.",
        "Si può. Metto quel colore dentro un Crystal Clear 390: più morbido, con più profondità. Lo vuoi ancora più morbido, cambio il colore interno.",
        "Sì, se conservo la ricetta. Annoto entrambi i codici, l'ordine e la misura. Stessi codici, stessa luce, stesso risultato.",
    ],
    "avoid_lead": "Il tuo ricettario, ogni volta:",
    "steps5": ["Annota entrambi i codici colore e quale va dentro", "Prova la combinazione nel calcolatore prima di ordinare", "Scambia interno ed esterno con 1 clic e confronta", "Stessa misura, luce e finitura per lo stesso risultato", "Ordina entrambi i colori insieme"],
    "client_body": "Il Double Stuffing Calculator gratuito su sempertexeurope.com/tools mostra la fusione prima di gonfiare qualsiasi cosa, con filtro per texture: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk e Reflex.",
    "cta_label": "Ordina",
    "s3_cover_a": "Double stuffing con Sempertex", "s3_cover_b": "a caso", "s3_cover_c": "vs.", "s3_cover_d": "calcolato",
    "s3_left": "A CASO", "s3_right": "CALCOLATO", "s3_left_meta": "gonfia e guarda", "s3_right_meta": "fusione vista prima",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Provare", "Sperare"], "s3_new_tags": ["Crystal Clear 390", "Ordine", "Ricettario"],
    "s3_new_quote": "“Scelgo interno ed esterno tra i veri colori Sempertex, vedo la fusione prima e annoto entrambi i codici.”", "s3_new_badge": "1 palloncino in 1 palloncino",
    "s3_changed_bottom": "Stessi 2 palloncini, stesso cliente.\nIl colore è giusto prima di gonfiare.",
    "s3_topic_lbl": "REGOLA", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Acceso resta acceso, non c'è rimedio",
    "s3_rule1_quote": "“Un colore acceso dentro un Crystal Clear 390 diventa più morbido e guadagna profondità: il look pastello premium.”",
    "s3_rule2_topic": "Ordine", "s3_rule2_old": "Quale va dentro non importa",
    "s3_rule2_quote": "“Il palloncino esterno decide quanta luce entra. Scambiali e ottieni un altro colore.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_quote": "“Esterno {p1}, interno {p2}. Esterno {p3}, interno {p0}. E {p0} dentro un Crystal Clear 390.”",
    "s3_client_lbl": "CLIENTE", "s3_client_topic": "Dialogo con il cliente",
    "s3_client_quote": "“Mandami il tuo codice colore. Provo 2 combinazioni e vedi la fusione prima che gonfi qualsiasi cosa.”",
    "s3_cta_kicker": "La tua ricetta double stuffing per il prossimo lavoro",
    "outer_lbl": "esterno", "inner_lbl": "interno", "result_lbl": "risultato", "approx_lbl": "approssimazione", "swap_lbl": "scambiato",
},
"pl": {
    "cover_pills": ["1 w 1…", "Crystal Clear 390…", "Kolejność ma znaczenie…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "Jeden balon w drugim, pompowane razem. Światło miesza 2 kolory w nowy.", "steps_lead": "Jak to działa:",
    "steps": ["Włóż balon wewnętrzny w całości do zewnętrznego", "Napompuj je razem, jak jeden balon", "Światło przechodzi przez zewnętrzną warstwę: widzisz optyczne mieszanie"],
    "steps_label": "Podstawy",
    "rule1_label": "Zasada 1", "rule1_title": "Crystal Clear 390 na zewnątrz: delikatniej i głębiej",
    "rule1_body": "Przezroczysta warstwa zewnętrzna to punkt wyjścia. Kolor wewnętrzny staje się delikatniejszy i zyskuje głębię, dokładnie ten premium pastelowy look, o który proszą klienci. Jaskrawy kolor w Crystal Clear 390 od razu wygląda o klasę spokojniej.",
    "rule2_label": "Zasada 2", "rule2_title": "Kolejność ma znaczenie, tekstura też",
    "rule2_body": "Balon zewnętrzny decyduje, ile światła dociera do wewnętrznego. Zamień wewnętrzny z zewnętrznym, a dostaniesz inny wynik. Matowy w błyszczącym wygląda inaczej niż 2 razy matowy. Sprawdź kombinację w kalkulatorze, zanim zamówisz.",
    "example_label": "Przykład", "example_title": "3 kombinacje z twojej palety",
    "combos": [[CRYSTAL, "{p0}", "delikatna wersja pastelowa"], ["{p1}", "{p2}", "głębiej i pełniej"], ["{p3}", "{p0}", "zupełnie nowy odcień"]],
    "example_body": "Na zewnątrz {p1}, w środku {p2}: głębiej i pełniej. Na zewnątrz {p3}, w środku {p0}: odcień, który nie istnieje jako pojedynczy balon. A {p0} w Crystal Clear 390 staje się delikatnym pastelem. Wynik tutaj to przybliżenie: rozmiar, światło i wykończenie mają znaczenie.",
    "client_label": "Rozmowa z klientem", "client_title": "Co odpowiadasz, gdy klient pyta",
    "client_answers": [
        "Tak. Wybieram balon wewnętrzny i zewnętrzny z prawdziwych kolorów Sempertex i najpierw widzę mieszankę w kalkulatorze. Wyślij mi swój kod koloru, a przetestuję 2 kombinacje.",
        "Da się. Wkładam ten kolor do Crystal Clear 390: delikatniej, z większą głębią. Chcesz jeszcze delikatniej, zmieniam kolor wewnętrzny.",
        "Tak, jeśli zachowam przepis. Zapisuję oba kody, kolejność i rozmiar. Te same kody, to samo światło, ten sam wynik.",
    ],
    "avoid_lead": "Twoja książka przepisów, za każdym razem:",
    "steps5": ["Zapisz oba kody kolorów i który idzie do środka", "Sprawdź kombinację w kalkulatorze przed zamówieniem", "Zamień wewnętrzny z zewnętrznym jednym kliknięciem i porównaj", "Ten sam rozmiar, światło i wykończenie dla tego samego wyniku", "Zamów oba kolory razem"],
    "client_body": "Darmowy kalkulator Double Stuffing na sempertexeurope.com/tools pokazuje mieszankę, zanim cokolwiek napompujesz, z filtrem po teksturze: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk i Reflex.",
    "cta_label": "Zamów",
    "s3_cover_a": "Double stuffing z Sempertex", "s3_cover_b": "na chybił trafił", "s3_cover_c": "vs.", "s3_cover_d": "policzony",
    "s3_left": "NA CHYBIŁ TRAFIŁ", "s3_right": "POLICZONY", "s3_left_meta": "napompuj i zobacz", "s3_right_meta": "mieszanka wcześniej",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Próbowanie", "Nadzieja"], "s3_new_tags": ["Crystal Clear 390", "Kolejność", "Książka przepisów"],
    "s3_new_quote": "“Wybieram wewnętrzny i zewnętrzny z prawdziwych kolorów Sempertex, najpierw widzę mieszankę i zapisuję oba kody.”", "s3_new_badge": "1 balon w 1 balonie",
    "s3_changed_bottom": "Te same 2 balony, ten sam klient.\nKolor zgadza się, zanim napompujesz.",
    "s3_topic_lbl": "ZASADA", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Jaskrawy zostaje jaskrawy, nic nie poradzisz",
    "s3_rule1_quote": "“Jaskrawy kolor w Crystal Clear 390 staje się delikatniejszy i zyskuje głębię: premium pastelowy look.”",
    "s3_rule2_topic": "Kolejność", "s3_rule2_old": "Który jest w środku, nie ma znaczenia",
    "s3_rule2_quote": "“Balon zewnętrzny decyduje, ile światła wchodzi. Zamień je, a dostaniesz inny kolor.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_quote": "“Na zewnątrz {p1}, w środku {p2}. Na zewnątrz {p3}, w środku {p0}. I {p0} w Crystal Clear 390.”",
    "s3_client_lbl": "KLIENT", "s3_client_topic": "Rozmowa z klientem",
    "s3_client_quote": "“Wyślij mi swój kod koloru. Przetestuję 2 kombinacje i zobaczysz mieszankę, zanim cokolwiek napompuję.”",
    "s3_cta_kicker": "Twój przepis double stuffing na następne zlecenie",
    "outer_lbl": "na zewnątrz", "inner_lbl": "w środku", "result_lbl": "wynik", "approx_lbl": "przybliżenie", "swap_lbl": "zamienione",
},
"el": {
    "cover_pills": ["1 μέσα σε 1…", "Crystal Clear 390…", "Η σειρά μετράει…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "Ένα μπαλόνι μέσα σε άλλο, φουσκωμένα μαζί. Το φως ανακατεύει 2 χρώματα σε ένα νέο.", "steps_lead": "Πώς λειτουργεί:",
    "steps": ["Βάλε το εσωτερικό μπαλόνι ολόκληρο μέσα στο εξωτερικό", "Φούσκωσέ τα μαζί, σαν ένα μπαλόνι", "Το φως περνά από το εξωτερικό στρώμα: βλέπεις την οπτική μίξη"],
    "steps_label": "Τα βασικά",
    "rule1_label": "Κανόνας 1", "rule1_title": "Crystal Clear 390 απ' έξω: πιο απαλό και πιο βαθύ",
    "rule1_body": "Ένα διάφανο εξωτερικό στρώμα είναι το σημείο εκκίνησης. Το εσωτερικό χρώμα γίνεται πιο απαλό και αποκτά βάθος, ακριβώς το premium παστέλ look που ζητούν οι πελάτες. Ένα έντονο χρώμα μέσα σε Crystal Clear 390 δείχνει αμέσως μια κλάση πιο ήρεμο.",
    "rule2_label": "Κανόνας 2", "rule2_title": "Η σειρά μετράει, και η υφή επίσης",
    "rule2_body": "Το εξωτερικό μπαλόνι καθορίζει πόσο φως φτάνει στο εσωτερικό. Άλλαξε εσωτερικό και εξωτερικό και παίρνεις άλλο αποτέλεσμα. Ματ μέσα σε γυαλιστερό δείχνει αλλιώς από 2 φορές ματ. Δοκίμασε τον συνδυασμό στον υπολογιστή πριν παραγγείλεις.",
    "example_label": "Παράδειγμα", "example_title": "3 συνδυασμοί από τη δική σου παλέτα",
    "combos": [[CRYSTAL, "{p0}", "απαλή παστέλ εκδοχή"], ["{p1}", "{p2}", "πιο βαθύ και γεμάτο"], ["{p3}", "{p0}", "μια νέα απόχρωση"]],
    "example_body": "Έξω {p1}, μέσα {p2}: πιο βαθύ και γεμάτο. Έξω {p3}, μέσα {p0}: μια απόχρωση που δεν υπάρχει ως μονό μπαλόνι. Και {p0} μέσα σε Crystal Clear 390 γίνεται απαλό παστέλ. Το αποτέλεσμα εδώ είναι προσέγγιση: μέγεθος, φως και φινίρισμα παίζουν ρόλο.",
    "client_label": "Συζήτηση με πελάτη", "client_title": "Τι απαντάς όταν ο πελάτης ρωτά",
    "client_answers": [
        "Ναι. Διαλέγω εσωτερικό και εξωτερικό μπαλόνι από τα πραγματικά χρώματα Sempertex και βλέπω τη μίξη πρώτα στον υπολογιστή. Στείλε μου τον κωδικό χρώματος και δοκιμάζω 2 συνδυασμούς.",
        "Γίνεται. Βάζω αυτό το χρώμα μέσα σε Crystal Clear 390: πιο απαλό, με περισσότερο βάθος. Το θέλεις ακόμα πιο απαλό, αλλάζω το εσωτερικό χρώμα.",
        "Ναι, αν κρατήσω τη συνταγή. Σημειώνω και τους δύο κωδικούς, τη σειρά και το μέγεθος. Ίδιοι κωδικοί, ίδιο φως, ίδιο αποτέλεσμα.",
    ],
    "avoid_lead": "Το βιβλίο συνταγών σου, κάθε φορά:",
    "steps5": ["Σημείωσε και τους δύο κωδικούς και ποιο πάει μέσα", "Δοκίμασε τον συνδυασμό στον υπολογιστή πριν παραγγείλεις", "Άλλαξε εσωτερικό και εξωτερικό με 1 κλικ και σύγκρινε", "Ίδιο μέγεθος, φως και φινίρισμα για το ίδιο αποτέλεσμα", "Παράγγειλε και τα δύο χρώματα μαζί"],
    "client_body": "Ο δωρεάν Double Stuffing Calculator στο sempertexeurope.com/tools δείχνει τη μίξη πριν φουσκώσεις οτιδήποτε, με φίλτρο υφής: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk και Reflex.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Double stuffing με Sempertex", "s3_cover_b": "στην τύχη", "s3_cover_c": "vs.", "s3_cover_d": "υπολογισμένο",
    "s3_left": "ΣΤΗΝ ΤΥΧΗ", "s3_right": "ΥΠΟΛΟΓΙΣΜΕΝΟ", "s3_left_meta": "φουσκώνεις και βλέπεις", "s3_right_meta": "η μίξη πρώτα",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Δοκιμή", "Ελπίδα"], "s3_new_tags": ["Crystal Clear 390", "Σειρά", "Βιβλίο συνταγών"],
    "s3_new_quote": "“Διαλέγω εσωτερικό και εξωτερικό από τα πραγματικά χρώματα Sempertex, βλέπω τη μίξη πρώτα και σημειώνω και τους δύο κωδικούς.”", "s3_new_badge": "1 μπαλόνι μέσα σε 1 μπαλόνι",
    "s3_changed_bottom": "Ίδια 2 μπαλόνια, ίδιος πελάτης.\nΤο χρώμα είναι σωστό πριν φουσκώσεις.",
    "s3_topic_lbl": "ΚΑΝΟΝΑΣ", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Το έντονο μένει έντονο, δεν γίνεται κάτι",
    "s3_rule1_quote": "“Ένα έντονο χρώμα μέσα σε Crystal Clear 390 γίνεται πιο απαλό και αποκτά βάθος: το premium παστέλ look.”",
    "s3_rule2_topic": "Σειρά", "s3_rule2_old": "Ποιο πάει μέσα δεν έχει σημασία",
    "s3_rule2_quote": "“Το εξωτερικό μπαλόνι καθορίζει πόσο φως μπαίνει. Άλλαξέ τα και παίρνεις άλλο χρώμα.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_quote": "“Έξω {p1}, μέσα {p2}. Έξω {p3}, μέσα {p0}. Και {p0} μέσα σε Crystal Clear 390.”",
    "s3_client_lbl": "ΠΕΛΑΤΗΣ", "s3_client_topic": "Συζήτηση με πελάτη",
    "s3_client_quote": "“Στείλε μου τον κωδικό χρώματος. Δοκιμάζω 2 συνδυασμούς και βλέπεις τη μίξη πριν φουσκώσω οτιδήποτε.”",
    "s3_cta_kicker": "Η συνταγή double stuffing σου για την επόμενη δουλειά",
    "outer_lbl": "έξω", "inner_lbl": "μέσα", "result_lbl": "αποτέλεσμα", "approx_lbl": "προσέγγιση", "swap_lbl": "αντίστροφα",
},
"hu": {
    "cover_pills": ["1 az 1-ben…", "Crystal Clear 390…", "A sorrend számít…"], "cover_with": "partner:", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "Egy lufi a másikban, együtt felfújva. A fény 2 színt kever egy újjá.", "steps_lead": "Így működik:",
    "steps": ["Tedd a belső lufit teljesen a külsőbe", "Fújd fel őket együtt, mint egy lufit", "A fény átmegy a külső rétegen: látod az optikai keveredést"],
    "steps_label": "Az alapok",
    "rule1_label": "1. szabály", "rule1_title": "Crystal Clear 390 kívül: lágyabb és mélyebb",
    "rule1_body": "Az átlátszó külső réteg a belépő. A belső szín lágyabb lesz és mélységet kap, pontosan az a prémium pasztell look, amit az ügyfelek kérnek. Egy élénk szín Crystal Clear 390-ben azonnal egy osztállyal nyugodtabb.",
    "rule2_label": "2. szabály", "rule2_title": "A sorrend számít, és a textúra is",
    "rule2_body": "A külső lufi dönti el, mennyi fény ér a belsőhöz. Cseréld meg a belsőt és a külsőt, és más eredményt kapsz. Matt a fényesben másképp néz ki, mint 2-szer matt. Próbáld ki a kombinációt a kalkulátorban, mielőtt rendelsz.",
    "example_label": "Példa", "example_title": "3 kombináció a saját palettádból",
    "combos": [[CRYSTAL, "{p0}", "lágy pasztell változat"], ["{p1}", "{p2}", "mélyebb és telibb"], ["{p3}", "{p0}", "egy új árnyalat"]],
    "example_body": "Kívül {p1}, belül {p2}: mélyebb és telibb. Kívül {p3}, belül {p0}: egy árnyalat, ami önálló lufiként nem létezik. És {p0} Crystal Clear 390-ben lágy pasztell lesz. Az itteni eredmény közelítés: a méret, a fény és a felület is számít.",
    "client_label": "Ügyfélbeszélgetés", "client_title": "Mit válaszolsz, ha az ügyfél megkérdezi",
    "client_answers": [
        "Igen. Választok egy belső és egy külső lufit a valódi Sempertex színekből, és a kalkulátorban előre látom a keveréket. Küldd el a színkódod, és kipróbálok 2 kombinációt.",
        "Megoldható. Azt a színt egy Crystal Clear 390-be teszem: lágyabb, több mélységgel. Ha még lágyabbat szeretnél, cserélem a belső színt.",
        "Igen, ha megőrzöm a receptet. Felírom mindkét kódot, a sorrendet és a méretet. Ugyanazok a kódok, ugyanaz a fény, ugyanaz az eredmény.",
    ],
    "avoid_lead": "A receptkönyved, minden alkalommal:",
    "steps5": ["Írd fel mindkét színkódot, és hogy melyik van belül", "Próbáld ki a kombinációt a kalkulátorban rendelés előtt", "Cseréld meg a belsőt és a külsőt 1 kattintással, és hasonlítsd össze", "Ugyanaz a méret, fény és felület ugyanahhoz az eredményhez", "Rendeld meg a két színt együtt"],
    "client_body": "Az ingyenes Double Stuffing kalkulátor a sempertexeurope.com/tools oldalon megmutatja a keveréket, mielőtt bármit felfújsz, textúra szerinti szűrővel: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk és Reflex.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Double stuffing Sempertex lufikkal", "s3_cover_b": "találomra", "s3_cover_c": "vs.", "s3_cover_d": "kiszámolva",
    "s3_left": "TALÁLOMRA", "s3_right": "KISZÁMOLVA", "s3_left_meta": "felfúj és megnéz", "s3_right_meta": "keverék előre",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Próbálgatás", "Remény"], "s3_new_tags": ["Crystal Clear 390", "Sorrend", "Receptkönyv"],
    "s3_new_quote": "“A belsőt és a külsőt a valódi Sempertex színekből választom, előre látom a keveréket, és felírom mindkét kódot.”", "s3_new_badge": "1 lufi 1 lufiban",
    "s3_changed_bottom": "Ugyanaz a 2 lufi, ugyanaz az ügyfél.\nA szín már felfújás előtt stimmel.",
    "s3_topic_lbl": "SZABÁLY", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Az élénk élénk marad, nincs mit tenni",
    "s3_rule1_quote": "“Egy élénk szín Crystal Clear 390-ben lágyabb lesz és mélységet kap: a prémium pasztell look.”",
    "s3_rule2_topic": "Sorrend", "s3_rule2_old": "Mindegy, melyik van belül",
    "s3_rule2_quote": "“A külső lufi dönti el, mennyi fény jut be. Cseréld meg őket, és más színt kapsz.”",
    "s3_example_lbl": "PÉLDA", "s3_example_quote": "“Kívül {p1}, belül {p2}. Kívül {p3}, belül {p0}. És {p0} Crystal Clear 390-ben.”",
    "s3_client_lbl": "ÜGYFÉL", "s3_client_topic": "Ügyfélbeszélgetés",
    "s3_client_quote": "“Küldd el a színkódod. Kipróbálok 2 kombinációt, és látod a keveréket, mielőtt bármit felfújok.”",
    "s3_cta_kicker": "A double stuffing recepted a következő munkához",
    "outer_lbl": "kívül", "inner_lbl": "belül", "result_lbl": "eredmény", "approx_lbl": "közelítés", "swap_lbl": "cserélve",
},
"lt": {
    "cover_pills": ["1 viename…", "Crystal Clear 390…", "Tvarka svarbi…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Double stuffing…",
    "steps_title": "Vienas balionas kitame, pripūsti kartu. Šviesa sumaišo 2 spalvas į naują.", "steps_lead": "Kaip tai veikia:",
    "steps": ["Įkišk vidinį balioną visą į išorinį", "Pripūsk juos kartu, kaip vieną balioną", "Šviesa pereina per išorinį sluoksnį: matai optinį maišymąsi"],
    "steps_label": "Pagrindai",
    "rule1_label": "1 taisyklė", "rule1_title": "Crystal Clear 390 išorėje: švelniau ir giliau",
    "rule1_body": "Skaidrus išorinis sluoksnis yra atspirties taškas. Vidinė spalva tampa švelnesnė ir įgauna gylio, būtent tas premium pastelinis vaizdas, kurio prašo klientai. Ryški spalva Crystal Clear 390 viduje iškart atrodo klase ramesnė.",
    "rule2_label": "2 taisyklė", "rule2_title": "Tvarka svarbi, tekstūra taip pat",
    "rule2_body": "Išorinis balionas lemia, kiek šviesos pasiekia vidinį. Sukeisk vidinį ir išorinį ir gausi kitokį rezultatą. Matinis blizgiame atrodo kitaip nei 2 kartus matinis. Išbandyk derinį skaičiuoklėje prieš užsakydamas.",
    "example_label": "Pavyzdys", "example_title": "3 deriniai iš tavo paletės",
    "combos": [[CRYSTAL, "{p0}", "švelni pastelinė versija"], ["{p1}", "{p2}", "giliau ir sodriau"], ["{p3}", "{p0}", "naujas atspalvis"]],
    "example_body": "Išorėje {p1}, viduje {p2}: giliau ir sodriau. Išorėje {p3}, viduje {p0}: atspalvis, kurio kaip vieno baliono nėra. O {p0} Crystal Clear 390 viduje tampa švelnia pastele. Rezultatas čia yra apytikslis: dydis, šviesa ir apdaila turi įtakos.",
    "client_label": "Pokalbis su klientu", "client_title": "Ką atsakai, kai klientas klausia",
    "client_answers": [
        "Taip. Renkuosi vidinį ir išorinį balioną iš tikrų Sempertex spalvų ir mišinį pirmiausia matau skaičiuoklėje. Atsiųsk savo spalvos kodą, išbandysiu 2 derinius.",
        "Galima. Tą spalvą įdedu į Crystal Clear 390: švelniau, su daugiau gylio. Nori dar švelniau, keičiu vidinę spalvą.",
        "Taip, jei išsaugau receptą. Užsirašau abu kodus, tvarką ir dydį. Tie patys kodai, ta pati šviesa, tas pats rezultatas.",
    ],
    "avoid_lead": "Tavo receptų knyga, kiekvieną kartą:",
    "steps5": ["Užsirašyk abu spalvų kodus ir kuris eina į vidų", "Išbandyk derinį skaičiuoklėje prieš užsakydamas", "Sukeisk vidinį ir išorinį 1 paspaudimu ir palygink", "Tas pats dydis, šviesa ir apdaila tam pačiam rezultatui", "Užsisakyk abi spalvas kartu"],
    "client_body": "Nemokama Double Stuffing skaičiuoklė sempertexeurope.com/tools parodo mišinį prieš ką nors pripučiant, su filtru pagal tekstūrą: Fashion, Pastel Dusk, Neon, Metallic, Pastel Matte, Silk ir Reflex.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Double stuffing su Sempertex", "s3_cover_b": "iš vilties", "s3_cover_c": "vs.", "s3_cover_d": "suskaičiuota",
    "s3_left": "IŠ VILTIES", "s3_right": "SUSKAIČIUOTA", "s3_left_meta": "pripūti ir žiūri", "s3_right_meta": "mišinys iš anksto",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Bandymai", "Viltis"], "s3_new_tags": ["Crystal Clear 390", "Tvarka", "Receptų knyga"],
    "s3_new_quote": "“Vidinį ir išorinį renkuosi iš tikrų Sempertex spalvų, mišinį matau iš anksto ir užsirašau abu kodus.”", "s3_new_badge": "1 balionas 1 balione",
    "s3_changed_bottom": "Tie patys 2 balionai, tas pats klientas.\nSpalva teisinga dar prieš pripučiant.",
    "s3_topic_lbl": "TAISYKLĖ", "s3_rule1_topic": "Crystal Clear", "s3_rule1_old": "Ryšku lieka ryšku, nieko nepadarysi",
    "s3_rule1_quote": "“Ryški spalva Crystal Clear 390 viduje tampa švelnesnė ir įgauna gylio: premium pastelinis vaizdas.”",
    "s3_rule2_topic": "Tvarka", "s3_rule2_old": "Nesvarbu, kuris viduje",
    "s3_rule2_quote": "“Išorinis balionas lemia, kiek šviesos patenka. Sukeisk juos ir gausi kitą spalvą.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_quote": "“Išorėje {p1}, viduje {p2}. Išorėje {p3}, viduje {p0}. Ir {p0} Crystal Clear 390 viduje.”",
    "s3_client_lbl": "KLIENTAS", "s3_client_topic": "Pokalbis su klientu",
    "s3_client_quote": "“Atsiųsk savo spalvos kodą. Išbandysiu 2 derinius ir pamatysi mišinį prieš man ką nors pripučiant.”",
    "s3_cta_kicker": "Tavo double stuffing receptas kitam užsakymui",
    "outer_lbl": "išorėje", "inner_lbl": "viduje", "result_lbl": "rezultatas", "approx_lbl": "apytikslis", "swap_lbl": "sukeista",
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["Double stuffing: zo maak je met Sempertex ballonnen kleuren die niet bestaan", "Welke kleur krijg je? Double stuffing met Sempertex ballonnen, vooraf berekend", "1 ballon in 1 ballon: pastel, dieper of exact de merkkleur, met Sempertex"],
  "cover_sub": ["Eén ballon in een andere, samen opblazen, en het licht doet de rest. Uit de Sempertex blog: hoe het werkt, welke kleur je krijgt en 3 recepten.", "Zachtere pastels, diepere tinten of de merkkleur van je klant: met 2 ballonnen maak je ze zelf. Plus de regel die bepaalt welke kleur je krijgt."],
  "client_question": ["Kan je exact onze merkkleur maken?", "Ik wil een zachter roze dan wat ik online zie.", "Krijg ik volgend jaar dezelfde kleur nog?"],
  "s3_old_quote": ["“Zakken open, samen duwen, opblazen en hopen”", "“Die kleur bestaat gewoon niet”", "“Dat zien we wel als hij opgeblazen is”"],
  "s3_client_old": ["“Dat roze kan ik niet maken”", "“Ik neem de dichtstbijzijnde kleur”"],
  "cta_title_tpl": "Bestel je Sempertex ballonnen bij {name}", "cta_sub_generic": "Bestel beide kleuren van je recept in één keer.",
},
"en": {
  "cover_title": ["Double stuffing: how to make colours that don't exist with Sempertex balloons", "Which colour do you get? Double stuffing with Sempertex balloons, worked out first", "1 balloon in 1 balloon: pastel, deeper or the exact brand colour, with Sempertex"],
  "cover_sub": ["One balloon inside another, inflated together, and light does the rest. From the Sempertex blog: how it works, which colour you get and 3 recipes.", "Softer pastels, deeper tones or your client's brand colour: with 2 balloons you make them yourself. Plus the rule that decides which colour you get."],
  "client_question": ["Can you match our brand colour exactly?", "I want a softer pink than what I see online.", "Will I get the same colour again next year?"],
  "s3_old_quote": ["“Open the bags, push them together, inflate and hope”", "“That colour just doesn't exist”", "“We'll see once it's inflated”"],
  "s3_client_old": ["“I can't make that pink”", "“I'll take the nearest colour”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "Order both colours of your recipe in one go.",
},
"de": {
  "cover_title": ["Double Stuffing: so machst du mit Sempertex Ballons Farben, die es nicht gibt", "Welche Farbe kommt raus? Double Stuffing mit Sempertex Ballons, vorher berechnet", "1 Ballon in 1 Ballon: Pastell, tiefer oder exakt die Markenfarbe, mit Sempertex"],
  "cover_sub": ["Ein Ballon im anderen, zusammen aufgeblasen, und das Licht macht den Rest. Aus dem Sempertex Blog: wie es funktioniert, welche Farbe rauskommt und 3 Rezepte.", "Weichere Pastells, tiefere Töne oder die Markenfarbe deines Kunden: mit 2 Ballons machst du sie selbst. Plus die Regel, die entscheidet, welche Farbe du bekommst."],
  "client_question": ["Kannst du exakt unsere Markenfarbe machen?", "Ich will ein weicheres Rosa als das, was ich online sehe.", "Bekomme ich nächstes Jahr wieder dieselbe Farbe?"],
  "s3_old_quote": ["“Tüten auf, zusammenschieben, aufblasen und hoffen”", "“Die Farbe gibt es einfach nicht”", "“Das sehen wir, wenn er aufgeblasen ist”"],
  "s3_client_old": ["“Das Rosa kann ich nicht machen”", "“Ich nehme die nächstliegende Farbe”"],
  "cta_title_tpl": "Bestell deine Sempertex Ballons bei {name}", "cta_sub_generic": "Bestell beide Farben deines Rezepts auf einmal.",
},
"fr": {
  "cover_title": ["Double stuffing : comment créer des couleurs qui n'existent pas avec des ballons Sempertex", "Quelle couleur obtiens-tu ? Le double stuffing avec des ballons Sempertex, calculé avant", "1 ballon dans 1 ballon : pastel, plus profond ou la couleur exacte de la marque, avec Sempertex"],
  "cover_sub": ["Un ballon dans un autre, gonflés ensemble, et la lumière fait le reste. Tiré du blog Sempertex : comment ça marche, quelle couleur tu obtiens et 3 recettes.", "Des pastels plus doux, des tons plus profonds ou la couleur de marque de ton client : avec 2 ballons, tu les crées toi-même. Plus la règle qui décide de la couleur obtenue."],
  "client_question": ["Tu peux reproduire exactement notre couleur de marque ?", "Je veux un rose plus doux que ce que je vois en ligne.", "J'aurai la même couleur l'an prochain ?"],
  "s3_old_quote": ["“Sachets ouverts, on pousse, on gonfle et on espère”", "“Cette couleur n'existe pas, c'est tout”", "“On verra une fois gonflé”"],
  "s3_client_old": ["“Ce rose, je ne sais pas le faire”", "“Je prends la couleur la plus proche”"],
  "cta_title_tpl": "Commande tes ballons Sempertex chez {name}", "cta_sub_generic": "Commande les deux couleurs de ta recette en une fois.",
},
"it": {
  "cover_title": ["Double stuffing: come creare colori che non esistono con i palloncini Sempertex", "Che colore ottieni? Il double stuffing con i palloncini Sempertex, calcolato prima", "1 palloncino in 1 palloncino: pastello, più profondo o il colore esatto del brand, con Sempertex"],
  "cover_sub": ["Un palloncino dentro l'altro, gonfiati insieme, e la luce fa il resto. Dal blog Sempertex: come funziona, che colore ottieni e 3 ricette.", "Pastelli più morbidi, toni più profondi o il colore del brand del tuo cliente: con 2 palloncini li crei tu. Più la regola che decide quale colore ottieni."],
  "client_question": ["Riesci a riprodurre esattamente il colore del nostro brand?", "Voglio un rosa più morbido di quello che vedo online.", "L'anno prossimo avrò di nuovo lo stesso colore?"],
  "s3_old_quote": ["“Buste aperte, spingi insieme, gonfia e spera”", "“Quel colore semplicemente non esiste”", "“Lo vediamo quando è gonfiato”"],
  "s3_client_old": ["“Quel rosa non lo so fare”", "“Prendo il colore più vicino”"],
  "cta_title_tpl": "Ordina i tuoi palloncini Sempertex da {name}", "cta_sub_generic": "Ordina entrambi i colori della tua ricetta in una volta.",
},
"pl": {
  "cover_title": ["Double stuffing: jak z balonów Sempertex zrobić kolory, które nie istnieją", "Jaki kolor dostaniesz? Double stuffing z balonami Sempertex, policzony wcześniej", "1 balon w 1 balonie: pastel, głębiej albo dokładnie kolor marki, z Sempertex"],
  "cover_sub": ["Jeden balon w drugim, pompowane razem, a światło robi resztę. Z bloga Sempertex: jak to działa, jaki kolor dostajesz i 3 przepisy.", "Delikatniejsze pastele, głębsze odcienie albo kolor marki twojego klienta: z 2 balonów robisz je sam. Plus zasada, która decyduje, jaki kolor dostajesz."],
  "client_question": ["Zrobisz dokładnie nasz kolor firmowy?", "Chcę delikatniejszy róż niż ten, który widzę w sieci.", "Dostanę ten sam kolor za rok?"],
  "s3_old_quote": ["“Otwórz paczki, wepchnij, napompuj i miej nadzieję”", "“Takiego koloru po prostu nie ma”", "“Zobaczymy, jak będzie napompowany”"],
  "s3_client_old": ["“Takiego różu nie zrobię”", "“Wezmę najbliższy kolor”"],
  "cta_title_tpl": "Zamów balony Sempertex w {name}", "cta_sub_generic": "Zamów oba kolory ze swojego przepisu za jednym razem.",
},
"el": {
  "cover_title": ["Double stuffing: έτσι φτιάχνεις με μπαλόνια Sempertex χρώματα που δεν υπάρχουν", "Ποιο χρώμα παίρνεις; Double stuffing με μπαλόνια Sempertex, υπολογισμένο από πριν", "1 μπαλόνι μέσα σε 1 μπαλόνι: παστέλ, πιο βαθύ ή ακριβώς το χρώμα της μάρκας, με Sempertex"],
  "cover_sub": ["Ένα μπαλόνι μέσα σε άλλο, φουσκωμένα μαζί, και το φως κάνει τα υπόλοιπα. Από το blog της Sempertex: πώς λειτουργεί, ποιο χρώμα παίρνεις και 3 συνταγές.", "Πιο απαλά παστέλ, πιο βαθιοί τόνοι ή το χρώμα της μάρκας του πελάτη σου: με 2 μπαλόνια τα φτιάχνεις μόνος σου. Και ο κανόνας που καθορίζει ποιο χρώμα παίρνεις."],
  "client_question": ["Μπορείς να πετύχεις ακριβώς το χρώμα της μάρκας μας;", "Θέλω ένα πιο απαλό ροζ από αυτό που βλέπω online.", "Θα έχω το ίδιο χρώμα και του χρόνου;"],
  "s3_old_quote": ["“Ανοίγεις σακούλες, σπρώχνεις, φουσκώνεις και ελπίζεις”", "“Αυτό το χρώμα απλά δεν υπάρχει”", "“Θα δούμε όταν φουσκώσει”"],
  "s3_client_old": ["“Αυτό το ροζ δεν μπορώ να το φτιάξω”", "“Παίρνω το πιο κοντινό χρώμα”"],
  "cta_title_tpl": "Παράγγειλε τα μπαλόνια Sempertex σου από {name}", "cta_sub_generic": "Παράγγειλε και τα δύο χρώματα της συνταγής σου με μία κίνηση.",
},
"hu": {
  "cover_title": ["Double stuffing: így készítesz Sempertex lufikkal olyan színeket, amik nem léteznek", "Milyen színt kapsz? Double stuffing Sempertex lufikkal, előre kiszámolva", "1 lufi 1 lufiban: pasztell, mélyebb vagy pontosan a márkaszín, Sempertex-szel"],
  "cover_sub": ["Egy lufi a másikban, együtt felfújva, a többit a fény intézi. A Sempertex blogból: hogyan működik, milyen színt kapsz, és 3 recept.", "Lágyabb pasztellek, mélyebb tónusok vagy az ügyfeled márkaszíne: 2 lufival magad készíted el. Plusz a szabály, ami eldönti, milyen színt kapsz."],
  "client_question": ["Pontosan el tudod készíteni a márkaszínünket?", "Lágyabb rózsaszínt szeretnék, mint amit online látok.", "Jövőre is ugyanezt a színt kapom?"],
  "s3_old_quote": ["“Zacskó ki, összenyom, felfúj, és reménykedik”", "“Ilyen szín egyszerűen nincs”", "“Majd meglátjuk, ha fel van fújva”"],
  "s3_client_old": ["“Azt a rózsaszínt nem tudom megcsinálni”", "“A legközelebbi színt veszem”"],
  "cta_title_tpl": "Rendeld a Sempertex lufijaidat innen: {name}", "cta_sub_generic": "Rendeld meg a recepted mindkét színét egyszerre.",
},
"lt": {
  "cover_title": ["Double stuffing: kaip su Sempertex balionais sukurti spalvas, kurių nėra", "Kokią spalvą gausi? Double stuffing su Sempertex balionais, suskaičiuota iš anksto", "1 balionas 1 balione: pastelė, giliau arba tiksli prekės ženklo spalva, su Sempertex"],
  "cover_sub": ["Vienas balionas kitame, pripūsti kartu, o visa kita padaro šviesa. Iš Sempertex tinklaraščio: kaip tai veikia, kokią spalvą gauni ir 3 receptai.", "Švelnesnės pastelės, gilesni tonai ar tavo kliento prekės ženklo spalva: su 2 balionais sukuri pats. Ir taisyklė, kuri lemia, kokią spalvą gausi."],
  "client_question": ["Ar gali tiksliai atkurti mūsų prekės ženklo spalvą?", "Noriu švelnesnės rožinės nei matau internete.", "Ar kitąmet gausiu tą pačią spalvą?"],
  "s3_old_quote": ["“Atidarai pakuotes, sukiši, pripūti ir tikiesi”", "“Tokios spalvos tiesiog nėra”", "“Pamatysim, kai pripūsim”"],
  "s3_client_old": ["“Tos rožinės padaryti negaliu”", "“Imu artimiausią spalvą”"],
  "cta_title_tpl": "Užsisakyk Sempertex balionus iš {name}", "cta_sub_generic": "Užsisakyk abi savo recepto spalvas iš karto.",
},
}

CAPTIONS_TPL = {
 "nl": "Double stuffing: één ballon in een andere, samen opblazen, en het licht mengt 2 kleuren tot een nieuwe. In deze carousel: hoe het werkt, waarom Crystal Clear 390 buiten alles zachter maakt, waarom de volgorde telt, 3 recepten uit je eigen palet en je receptenboek. Plus wat je antwoordt als de klant exact zijn merkkleur wil.\n\nBestel je Sempertex ballonnen bij {domain}.\n\n#doublestuffing #sempertex #{tag} #ballondecoratie #ballonnen #ballonartiest",
 "en": "Double stuffing: one balloon inside another, inflated together, and light blends 2 colours into a new one. In this carousel: how it works, why Crystal Clear 390 on the outside softens everything, why order matters, 3 recipes from your own palette and your recipe book. Plus what to answer when the client wants their exact brand colour.\n\nOrder your Sempertex balloons at {domain}.\n\n#doublestuffing #sempertex #{tag} #balloondecor #balloons #balloonartist",
 "de": "Double Stuffing: ein Ballon im anderen, zusammen aufgeblasen, und das Licht mischt 2 Farben zu einer neuen. Im Carousel: wie es funktioniert, warum Crystal Clear 390 außen alles weicher macht, warum die Reihenfolge zählt, 3 Rezepte aus deiner Palette und dein Rezeptbuch. Plus, was du antwortest, wenn der Kunde exakt seine Markenfarbe will.\n\nBestell deine Sempertex Ballons bei {domain}.\n\n#doublestuffing #sempertex #{tag} #ballondeko #ballons #ballonkünstler",
 "fr": "Double stuffing : un ballon dans un autre, gonflés ensemble, et la lumière mélange 2 couleurs en une nouvelle. Dans ce carrousel : comment ça marche, pourquoi le Crystal Clear 390 à l'extérieur adoucit tout, pourquoi l'ordre compte, 3 recettes de ta palette et ton carnet de recettes. Plus ce que tu réponds quand le client veut exactement sa couleur de marque.\n\nCommande tes ballons Sempertex chez {domain}.\n\n#doublestuffing #sempertex #{tag} #decorationballons #ballons #artisteballon",
 "it": "Double stuffing: un palloncino dentro l'altro, gonfiati insieme, e la luce fonde 2 colori in uno nuovo. Nel carosello: come funziona, perché il Crystal Clear 390 all'esterno ammorbidisce tutto, perché l'ordine conta, 3 ricette dalla tua palette e il tuo ricettario. Più cosa rispondi quando il cliente vuole esattamente il colore del suo brand.\n\nOrdina i tuoi palloncini Sempertex da {domain}.\n\n#doublestuffing #sempertex #{tag} #palloncini #decorazioni #balloonartist",
 "pl": "Double stuffing: jeden balon w drugim, pompowane razem, a światło miesza 2 kolory w nowy. W karuzeli: jak to działa, dlaczego Crystal Clear 390 na zewnątrz wszystko łagodzi, dlaczego kolejność ma znaczenie, 3 przepisy z twojej palety i twoja książka przepisów. Plus co odpowiedzieć, gdy klient chce dokładnie swój kolor firmowy.\n\nZamów balony Sempertex w {domain}.\n\n#doublestuffing #sempertex #{tag} #dekoracjebalonowe #balony #artystabalonowy",
 "el": "Double stuffing: ένα μπαλόνι μέσα σε άλλο, φουσκωμένα μαζί, και το φως ανακατεύει 2 χρώματα σε ένα νέο. Στο carousel: πώς λειτουργεί, γιατί το Crystal Clear 390 απ' έξω απαλύνει τα πάντα, γιατί η σειρά μετράει, 3 συνταγές από την παλέτα σου και το βιβλίο συνταγών σου. Και τι απαντάς όταν ο πελάτης θέλει ακριβώς το χρώμα της μάρκας του.\n\nΠαράγγειλε τα μπαλόνια Sempertex σου από {domain}.\n\n#doublestuffing #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "Double stuffing: egy lufi a másikban, együtt felfújva, a fény pedig 2 színt kever egy újjá. A carouselben: hogyan működik, miért lágyít mindent a külső Crystal Clear 390, miért számít a sorrend, 3 recept a saját palettádból és a receptkönyved. Plusz mit válaszolj, ha az ügyfél pontosan a márkaszínét kéri.\n\nRendeld a Sempertex lufijaidat innen: {domain}.\n\n#doublestuffing #sempertex #{tag} #lufidekoracio #lufi #lufiművész",
 "lt": "Double stuffing: vienas balionas kitame, pripūsti kartu, o šviesa sumaišo 2 spalvas į naują. Karuselėje: kaip tai veikia, kodėl Crystal Clear 390 išorėje viską sušvelnina, kodėl svarbi tvarka, 3 receptai iš tavo paletės ir tavo receptų knyga. Ir ką atsakyti, kai klientas nori tikslios savo prekės ženklo spalvos.\n\nUžsisakyk Sempertex balionus iš {domain}.\n\n#doublestuffing #sempertex #{tag} #balionai #balionumenininkas",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}

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

def dstuff(outer, inner, size=150):
    """Gesimuleerde double stuff: binnenfoto met de buitenfoto als half-transparante laag erover.
    outer='crystal' = transparante buitenlaag (lichter en zachter)."""
    ratio = G["PHOTO_RATIO"]; h = int(size * ratio)
    if outer == "crystal":
        over = _bl("whitesand", size, extra="position:absolute;left:0;top:0;opacity:.42")
        glass = (f'<div style="position:absolute;left:{int(size*.08)}px;top:{int(size*.04)}px;width:{int(size*.84)}px;height:{int(h*.8)}px;border-radius:50%;'
                 f'background:radial-gradient(circle at 30% 24%,rgba(255,255,255,.75) 0,rgba(255,255,255,.18) 38%,rgba(255,255,255,0) 62%)"></div>')
        return f'<div style="position:relative;width:{size}px;height:{h}px">{_bl(inner, size)}{over}{glass}</div>'
    over = _bl(outer, size, extra="position:absolute;left:0;top:0;opacity:.6")
    return f'<div style="position:relative;width:{size}px;height:{h}px">{_bl(inner, size)}{over}</div>'

def combo_keys(P):
    return [("crystal", P[0]), (P[1], P[2]), (P[3], P[0])]

def combo_row(c, P, size=150, lab=20, sub=17, ink="#111", gap=30):
    """3 double-stuffs met label buiten/binnen en effect."""
    esc = G["esc"]; out = f'<div style="display:flex;align-items:flex-end;justify-content:center;gap:{gap}px">'
    for (o, i), (ol, il, eff) in zip(combo_keys(P), c["combos"]):
        out += (f'<div style="text-align:center;max-width:{int(size*1.9)}px">{dstuff(o, i, size)}'
                f'<div class="pname" style="font-size:{lab}px;margin-top:10px;color:{ink};line-height:1.2"><span style="opacity:.6">{esc(c["outer_lbl"])}</span> {esc(ol)}<br><span style="opacity:.6">{esc(c["inner_lbl"])}</span> {esc(il)}</div>'
                f'<div class="pcode-only" style="font-size:{sub}px;color:{ink};opacity:.75;margin-top:4px">{esc(eff)}</div></div>')
    return out + '</div>'

def crystal_row(c, P, size=140, lab=19, ink="#111"):
    """3 kleuren uit het palet, elk in Crystal Clear 390: links de losse ballon, rechts in crystal."""
    esc = G["esc"]; out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:18px">'
    for k in P[:3]:
        out += (f'<div style="text-align:center"><div style="display:flex;align-items:flex-end;gap:6px">{_bl(k, int(size*.7))}<div style="font-size:26px;padding-bottom:40px;color:{ink};opacity:.5">→</div>{dstuff("crystal", k, size)}</div>'
                f'<div class="pname" style="font-size:{lab}px;margin-top:8px;color:{ink}">{esc(G["pal_label"](k))} + Crystal 390</div></div>')
    return out + '</div>'

def swap_pair(c, P, size=150, lab=20, ink="#111"):
    """Zelfde 2 kleuren, andere volgorde: A buiten B binnen vs. B buiten A binnen."""
    esc = G["esc"]; a, b_ = P[1], P[2]
    def cell(o, i):
        return (f'<div style="text-align:center">{dstuff(o, i, size)}'
                f'<div class="pname" style="font-size:{lab}px;margin-top:10px;color:{ink};line-height:1.2"><span style="opacity:.6">{esc(c["outer_lbl"])}</span> {esc(G["pal_label"](o))}<br><span style="opacity:.6">{esc(c["inner_lbl"])}</span> {esc(G["pal_label"](i))}</div></div>')
    return (f'<div style="display:flex;align-items:center;justify-content:center;gap:26px">{cell(a, b_)}'
            f'<div style="font-size:54px;font-weight:900;color:{ink};opacity:.6">⇄</div>{cell(b_, a)}</div>')

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

def hope_pile(keys, ink="#111"):
    """'Op hoop': losse ballonnen en open zakjes door elkaar, met vraagtekens."""
    esc = G["esc"]; w, h = 330, 360
    pos = [(0, 30, 92), (100, 0, 84), (200, 40, 96), (40, 150, 88), (150, 140, 104), (250, 170, 80), (90, 250, 92), (200, 250, 84)]
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    for i, (x, y, s) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{_bl(keys[i % len(keys)], s)}</div>'
    for (x, y, r) in ((30, 110, -12), (210, 15, 8), (130, 300, -6)):
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg);background:#fff;color:{ink};border:3px solid {ink};'
                f'border-radius:50%;width:46px;height:46px;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:900;box-shadow:0 4px 0 rgba(0,0,0,.18)">?</div>')
    return out + '</div>'

def calc_card(c, P, ink="#111"):
    """'Uitgerekend': één double stuff groot + kaartje buiten/binnen met codes."""
    esc = G["esc"]; o, i = P[1], P[2]
    return (f'<div style="position:relative;width:330px;height:370px">'
            f'<div style="position:absolute;left:70px;top:0">{dstuff(o, i, 190)}</div>'
            f'<div style="position:absolute;left:20px;top:260px;width:290px;background:#fff;color:{ink};border:3px solid {ink};border-radius:14px;padding:12px 16px;box-shadow:0 6px 0 rgba(0,0,0,.18);font-size:18px;font-weight:700;line-height:1.3">'
            f'<div><span style="opacity:.55">{esc(c["outer_lbl"])}</span> {esc(G["pal_label"](o))}</div><div><span style="opacity:.55">{esc(c["inner_lbl"])}</span> {esc(G["pal_label"](i))}</div></div></div>')

# ---------------------------------------------------------------- STIJL 1
def s1_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c); P = b["pal"]
    esc, hl, cursor_svg, arrow_svg, balloon = G["esc"], G["hl"], G["cursor_svg"], G["arrow_svg"], G["balloon"]
    s1_footer, logo_img, rot, STX_FULL = G["s1_footer"], G["logo_img"], G["rot"], G["STX_FULL"]
    S = []
    pills = c["cover_pills"]
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:92px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
  <div class="pill" style="background:{b['c1']};color:{b['c1t']};right:60px;top:130px;transform:rotate({rot(b,-4)}deg)">{cursor_svg(b['c1'])}{esc(pills[0])}</div>
  <div class="pill" style="background:{b['c2']};color:{b['c2t']};right:90px;top:835px;transform:rotate({rot(b,3)}deg)">{cursor_svg(b['c2'])}{esc(pills[1])}</div>
  <div class="pill" style="background:{b['c3']};color:{b['c3t']};left:90px;top:880px;transform:rotate({rot(b,-2)}deg)">{cursor_svg(b['c3'])}{esc(pills[2])}</div>
  <div style="position:absolute;left:150px;top:960px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:310px;right:90px;top:1020px;font-size:29px;line-height:1.35">{esc(c['cover_sub'])}</div>
  {s1_footer(b, stx_h=84)}
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:790px;height:560px">
    <h2 data-fit style="font-size:72px;max-height:460px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:820px;top:80px;transform:rotate(12deg)">{dstuff(P[1], P[2], 190)}</div>
  <div style="position:absolute;left:120px;top:690px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:720px;width:710px;height:440px;padding:40px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:420px;padding:44px 50px">
    <h2 data-fit style="font-size:58px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:28px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:650px;height:460px">
    <div class="card" style="top:0;height:380px;transform:translate(60px,-70px) scale(.92);opacity:.5"></div>
    <div class="card" style="top:0;height:380px;transform:translate(30px,-36px) scale(.96);opacity:.75"></div>
    <div class="card" style="top:0;height:430px;display:flex;align-items:center;justify-content:center;padding:30px 30px 36px">{crystal_row(c, P, 136, 17, b['ink'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:440px;padding:44px 50px">
    <h2 data-fit style="font-size:56px;max-height:150px">{esc(c['rule2_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:28px">{esc(c['rule2_body'])}</div>
  </div>
  <div class="stack" style="top:670px;height:430px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:410px;display:flex;align-items:center;justify-content:center;padding:30px 30px 36px">{swap_pair(c, P, 160, 21, b['ink'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:580px;padding:40px 30px 36px">
    <h2 data-fit style="font-size:52px;margin-bottom:30px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    {combo_row(c, P, 150, 20, 17, b['ink'], 26)}
  </div>
  <div class="box" style="left:70px;top:790px;width:940px;padding:32px 50px"><div class="body" style="font-size:26px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:130px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:490px;display:flex;flex-direction:column;gap:20px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:26px 36px"><div style="font-size:28px;line-height:1.35">{esc(c['client_answer'])}</div></div>
    <div class="card" style="position:relative;left:auto;right:auto;padding:22px 36px"><div style="font-size:25px;font-weight:{b['body_b']};margin-bottom:2px">{esc(c['avoid_lead'])}</div>{avoid_list(c, 'avoid')}</div>
    <div class="body" style="font-size:23px;line-height:1.35">{esc(c['client_body'])}</div>
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
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:68px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;flex-direction:row;gap:36px;align-items:center">{_bl(P[1], 130)}<div style="font-size:48px;font-weight:900;color:#111;opacity:.5">+</div>{_bl(P[2], 130)}<div style="font-size:48px;font-weight:900;color:#111;opacity:.5">=</div>{dstuff(P[1], P[2], 170)}</div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px"><b style="font-size:36px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:660px;width:560px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:380px;flex-direction:row;gap:24px;align-items:center">{_bl(P[0], 110)}<div style="font-size:40px;font-weight:900;color:#111;opacity:.5">→</div>{dstuff("crystal", P[0], 150)}</div>
  </div>
  <div class="frame" style="left:600px;top:800px;width:410px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:280px">{dstuff(P[3], P[0], 140)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:440px;padding:20px;box-sizing:border-box;background:#fff">{crystal_row(c, P, 130, 18, '#111')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:900px;font-size:27px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:170px">{esc(c['rule2_title'])}</h2>
  <div class="frame" style="left:70px;top:370px;width:940px;transform:rotate({rot(b,1.5)}deg)">
    <div class="ph" style="height:420px;padding:20px;box-sizing:border-box;background:#fff">{swap_pair(c, P, 160, 21, '#111')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:900px;font-size:27px">{esc(c['rule2_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:480px;padding:20px;box-sizing:border-box;align-items:center;background:#fff">{combo_row(c, P, 140, 19, 16, '#111', 22)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:900px;font-size:25px">{esc(c['example_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:150px">{esc(c['client_title'])}</h2>
  <div class="frame" style="left:70px;top:340px;width:940px">
    <div class="ph" style="height:auto;padding:28px 34px;box-sizing:border-box;align-items:flex-start;background:#fff">
      <div style="font-size:30px;line-height:1.3;color:{b['ink']};font-style:italic">{esc(c['client_question'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:14px 0"></div>
      <div style="font-size:25px;line-height:1.35;color:{b['ink']}">{esc(c['client_answer'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:14px 0"></div>
      <div style="font-size:22px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['avoid_lead'])}</div>
      {avoid_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1060px;font-size:23px">{esc(c['client_body'])}</div>
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
    loud = P + PAL_SETS[(b["pal_idx"] + 5) % len(PAL_SETS)]
    S = []
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:50px;right:50px;top:60px;max-height:400px;font-size:84px;text-align:center;line-height:1.08">{hl(c['s3_cover_a'])} {esc(c['s3_cover_b'])} {esc(c['s3_cover_c'])}<br><span class="hl">{esc(c['s3_cover_d'])}</span></h1>
  <div class="vsmark" style="top:520px">VS</div>
  <div class="lblw" style="left:110px;top:500px;transform:rotate({rot(b,-4)}deg)">{esc(c['s3_left'])}<br><span class="meta">● {esc(c['s3_left_meta'])}</span></div>
  <div class="lbld" style="right:110px;top:500px;transform:rotate({rot(b,4)}deg)">{esc(c['s3_right'])}<br><span class="meta" style="background:rgba(255,255,255,.18)">● {esc(c['s3_right_meta'])}</span></div>
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{hope_pile(loud, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{calc_card(c, P, b['ink'])}</div>
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
    <div>{new_tags}</div>
    <div class="quote" style="font-size:30px">{esc(c['s3_new_quote'])}</div>
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
    vis1 = (f'<div style="display:flex;flex-direction:column;align-items:center;gap:16px"><div style="display:flex;align-items:flex-end;gap:10px">{_bl(P[0], 100)}<div style="font-size:30px;padding-bottom:50px;opacity:.5">→</div>{dstuff("crystal", P[0], 150)}</div>'
            f'<div class="pname" style="font-size:19px;text-align:center">{esc(G["pal_label"](P[0]))} + Crystal 390</div></div>')
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="transform:scale(.78);transform-origin:top center;margin-bottom:-60px">{swap_pair(c, P, 150, 19, "#111")}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['example_title']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:620px;padding:40px 24px;display:flex;align-items:center;justify-content:center">
    {combo_row(c, P, 150, 20, 17, "#111", 22)}
  </div>
  <div class="bottom" style="top:910px;font-size:31px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    vis6 = (f'<div style="width:100%"><div style="font-size:23px;line-height:1.3;font-style:italic;margin-bottom:12px">{esc(c["client_question"])}</div>'
            f'<div style="font-size:19px;line-height:1.3;margin-bottom:14px">{esc(c["client_answer"])}</div>'
            f'<div style="font-size:18px;font-weight:800;margin-bottom:2px">{esc(c["avoid_lead"])}</div>{avoid_list(c, "s3steps")}</div>')
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
.s1 .step{font-size:27px;margin-top:12px}
.s1 .avoid .step{font-size:24px;margin-top:9px;line-height:1.25}
.s2 .onwhite .step{color:#111;font-size:21px;margin-top:7px;line-height:1.25}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:10px;font-size:17px;line-height:1.25;margin-top:6px}
.s3 .s3steps .step b{min-width:24px;font-weight:800}
"""
