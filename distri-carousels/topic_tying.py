# -*- coding: utf-8 -*-
"""Topic: 'Balloon tying: quick work without painful fingers.'
(sempertexeurope.com/en_GB/blog/how-to-tie-a-balloon-quickly).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=tying.
Uit de blog: knopen doet pijn door wrijving (zo'n 2 cm huid op wijs- en middelvinger), herhaling (knijpen met de
vingertoppen is de zwakste manier) en stijf latex; zacht latex glijdt. Stap 1: alleen het ronde deel opblazen, nek
leeg, door de sizer. Stap 2: de tweevingerknoop in 5 stappen (knijpen, nek 2 tot 3× rekken, om wijs- en middelvinger
wikkelen, uiteinde door de lus, vingers eruit en aantrekken). Sneller: elke nek rekken voor het opblazen, in duplets
knopen (2 ballonnen nek aan nek = 1 knoop; trio = duplet + 1, kwartet = 2 duplets, sextet = 2 trio's), werken in
blokken van 20. Handverzorging: 2 minuten rekken, stoffen tape op wijs- en middelvinger, huid hydrateren, echte pauzes.
Sempertex: 100% natuurlijk latex zonder vulstoffen of weekmakers, elke ballon gecontroleerd op kleur, nek, rek en
elasticiteit, ISO- en TÜV-gecertificeerd. FAQ: leeglopen = lucht in de nek; knappen = lucht in de nek of latex
zonder treksterkte; kwaliteit is de grootste factor."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["Tweevingerknoop…", "Nek 2 tot 3× rekken…", "Geen blaren…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Knopen…",
    "steps_title": "De tweevingerknoop: sneller, en je vingers blijven heel", "steps_lead": "De knoop, in 5 stappen:",
    "steps": ["Knijp de nek dicht met duim en wijsvinger, waar het ronde deel begint", "Rek de nek met je andere hand tot 2 à 3 keer de lengte en hou even vast: zo wordt het latex zacht", "Wikkel de nek om je wijs- én middelvinger, niet om één vinger", "Spreid de vingers iets en duw het uiteinde van de nek door de lus", "Schuif je vingers eruit en trek de nek aan"],
    "steps_label": "De knoop",
    "rule1_label": "Waarom het pijn doet", "rule1_title": "Knopen doet pijn door 3 dingen: wrijving, herhaling en stijf latex",
    "rule1_body": "De nek schuurt honderden keren over dezelfde 2 cm huid op je wijs- en middelvinger, tot die rood wordt en blaart. Knijpen met de vingertoppen is bovendien de zwakste manier om je hand te gebruiken. En stijf latex vraagt meer trekkracht en schuurt harder. Zacht latex glijdt. Techniek lost de eerste twee op, materiaal het derde.",
    "rule1_facts": [["2 cm", "huid die alle wrijving opvangt"], ["2 vingers", "wijs en middel, nooit één"], ["2 tot 3×", "de nek rekken voor de knoop"], ["400", "knopen op een lange dag"]],
    "rule2_label": "Sneller", "rule2_title": "Sneller knopen met minder pijn: 5 gewoontes voor lange dagen",
    "rule2_body": "Elke gewoonte haalt een beetje wrijving of herhaling weg. Samen maken ze het verschil tussen een lange dag en een pijnlijke:",
    "alts": [["Rek elke nek vooraf", "voor het opblazen even rekken: het latex wordt zachter en de knoop gaat makkelijker."], ["Blaas alleen het ronde deel op", "nek leeg laten en elke ballon door de sizer. Lucht in de nek kost je de lengte die je nodig hebt."], ["Knoop in duplets", "2 ballonnen nek aan nek: 1 knoop in plaats van 2. Trio = duplet + 1, kwartet = 2 duplets, sextet = 2 trio's."], ["Werk in blokken van 20", "20 opblazen, 20 knopen, 20 monteren. Elke handgroep krijgt om de beurt rust."], ["Verzorg je handen", "2 minuten rekken voor en na, stoffen tape op wijs- en middelvinger, huid hydrateren, echte pauzes."]],
    "example_label": "Voorbeeld", "example_title": "Duplet en kwartet: minder knopen, zelfde Sempertex latex",
    "ex_items": [["Duplet", "{p0} en {p1} nek aan nek: 1 knoop in plaats van 2. De basis van elke slinger en kolom."], ["Kwartet", "2 duplets in elkaar gedraaid: {p0}, {p1}, {p2} en {p3}, alle vier R12 en door de sizer, zodat de set klopt."]],
    "example_body": "Sempertex latex is 100% natuurlijk, zonder vulstoffen of weekmakers. Elke ballon wordt gecontroleerd op kleur, nek, rek en elasticiteit voor hij de fabriek verlaat. ISO- en TÜV-gecertificeerd. Zacht latex glijdt, stijf latex schuurt.",
    "client_label": "Collega vraagt", "client_title": "Wat je antwoordt als een collega vraagt",
    "client_answers": [
        "Dan zit er lucht in de nek. Blaas alleen het ronde deel op en laat de nek leeg; knoop waar nog lucht zit, niet erboven. Rek de nek eerst 2 à 3 keer de lengte, dan sluit de knoop vanzelf.",
        "Drie dingen: rek de nek voor elke knoop, wikkel om wijs- én middelvinger in plaats van één, en plak op lange dagen stoffen tape op die twee vingers. En gebruik latex dat goed rekt: stijf latex schuurt het hardst.",
        "Meestal zit er lucht in de nek, of het latex mist de treksterkte en elasticiteit voor het rekken. Blaas alleen het ronde deel op. Blijft het knappen, dan ligt het aan het materiaal: vulstoffen maken latex stijf en scheurgevoelig.",
    ],
    "avoid_lead": "Voor een lange knoopdag, in 5 stappen:",
    "steps5": ["Rek vingers, handen en onderarmen: 2 minuten", "Stoffen tape op wijs- en middelvinger van je knoophand", "Alleen het ronde deel opblazen, nek leeg, door de sizer", "Elke nek 2 à 3 keer de lengte rekken voor de knoop", "Blokken van 20 en echte pauzes, wissel van hand of taak"],
    "client_body": "Slingers en kolommen opbouwen uit duplets: bekijk de video van Sempertex Europe op YouTube.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex knopen:", "s3_cover_b": "pijnlijke vingers", "s3_cover_c": "vs.", "s3_cover_d": "tweevingerknoop",
    "s3_left": "PIJNLIJKE VINGERS", "s3_right": "TWEEVINGERKNOOP", "s3_left_meta": "1 vinger, stijf latex", "s3_right_meta": "2 vingers, nek gerekt",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["1 vinger", "Niet rekken", "Stijf latex"], "s3_new_tags": ["2 vingers", "2 tot 3× rekken", "Duplets", "Tape"],
    "s3_new_quote": "“Nek rekken, om twee vingers, uiteinde door de lus. Vierhonderd knopen, en 's avonds geen blaren.”", "s3_new_badge": "Zacht latex glijdt",
    "s3_changed_bottom": "Zelfde ballonnen, zelfde handen.\nNu met 2 vingers en een gerekte nek.",
    "s3_topic_lbl": "WAAROM", "s3_rule1_topic": "Pijn", "s3_rule1_old": "Blaren horen bij het vak",
    "s3_rule1_quote": "“Wrijving, herhaling en stijf latex. Techniek lost de eerste twee op, materiaal het derde.”",
    "s3_rule2_topic": "Sneller", "s3_rule2_old": "Knijpen, trekken, 400 keer",
    "s3_rule2_quote": "“Duplets, blokken van 20 en tape op twee vingers. Minder knopen, minder wrijving.”",
    "s3_example_topic": "Duplet en kwartet", "s3_example_lbl": "VOORBEELD", "s3_example_quote": "“Duplet in {p0} en {p1}, kwartet met {p2} en {p3}. Alle R12, door de sizer, 100% natuurlijk latex.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "Lange dagen",
    "s3_client_quote": "“Rek de nek, wikkel om twee vingers, plak tape. Dat is het hele verschil.”",
    "s3_cta_kicker": "Latex dat meerekt in plaats van tegenwerkt",
    "duplet_lbl": "duplet", "quartet_lbl": "kwartet", "ouch_lbl": "2 cm blaar", "knot_lbl": "1 knoop", "chips": ["100% natuurlijk latex", "ISO + TÜV", "kleur, nek, rek, elasticiteit"],
},
"en": {
    "cover_pills": ["Two-finger knot…", "Stretch 2 to 3×…", "No blisters…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Tying…",
    "steps_title": "The two-finger knot: faster, and your fingers stay intact", "steps_lead": "The knot, in 5 steps:",
    "steps": ["Pinch the neck closed with thumb and index finger, where the round part begins", "With your other hand, stretch the neck to 2 or 3 times its length and hold briefly: this softens the latex", "Wrap the neck around your index and middle finger, never just one", "Spread the fingers slightly and push the end of the neck through the loop", "Slide your fingers out and pull the neck tight"],
    "steps_label": "The knot",
    "rule1_label": "Why it hurts", "rule1_title": "Tying hurts for 3 reasons: friction, repetition and stiff latex",
    "rule1_body": "The neck rubs hundreds of times over the same 2 cm of skin on your index and middle finger, until it goes red and blisters. Pinching with the fingertips is also the weakest way to work your hand. And stiff latex needs more pull and rubs harder. Soft latex glides. Technique fixes the first two, material fixes the third.",
    "rule1_facts": [["2 cm", "of skin that takes all the friction"], ["2 fingers", "index and middle, never one"], ["2 to 3×", "stretch the neck before the knot"], ["400", "knots on a long day"]],
    "rule2_label": "Faster", "rule2_title": "Tie faster with less pain: 5 habits for long days",
    "rule2_body": "Each habit removes a bit of friction or repetition. Together they're the difference between a long day and a painful one:",
    "alts": [["Stretch every neck first", "a quick stretch before inflating: the latex softens and the knot goes in easier."], ["Inflate only the round part", "leave the neck empty and pass every balloon through the sizer. Air in the neck steals the length you need."], ["Tie in duplets", "2 balloons neck to neck: 1 knot instead of 2. Trio = duplet + 1, quartet = 2 duplets, sextet = 2 trios."], ["Work in blocks of 20", "inflate 20, tie 20, assemble 20. Each hand group gets its turn to rest."], ["Look after your hands", "stretch 2 minutes before and after, fabric tape on index and middle finger, keep skin hydrated, take real breaks."]],
    "example_label": "Example", "example_title": "Duplet and quartet: fewer knots, same Sempertex latex",
    "ex_items": [["Duplet", "{p0} and {p1} neck to neck: 1 knot instead of 2. The base of every garland and column."], ["Quartet", "2 duplets intertwined: {p0}, {p1}, {p2} and {p3}, all four R12 and through the sizer so the set matches."]],
    "example_body": "Sempertex latex is 100% natural, with no fillers or plasticisers. Every balloon is checked for colour, neck, stretch and elasticity before it leaves the factory. ISO and TÜV certified. Soft latex glides, stiff latex rubs.",
    "client_label": "Colleague asks", "client_title": "What you answer when a colleague asks",
    "client_answers": [
        "Then there's air in the neck. Inflate only the round part and leave the neck empty; tie where air remains, never above it. Stretch the neck to 2 or 3 times its length first and the knot closes on its own.",
        "Three things: stretch the neck before every knot, wrap around index and middle finger instead of one, and on long days put fabric tape on those two fingers. And use latex that stretches well: stiff latex rubs hardest.",
        "Usually there's air trapped in the neck, or the latex lacks the tensile strength and elasticity for the stretch. Inflate only the round part. If it keeps popping, it's the material: fillers make latex stiff and easy to tear.",
    ],
    "avoid_lead": "Before a long tying day, in 5 steps:",
    "steps5": ["Stretch fingers, hands and forearms: 2 minutes", "Fabric tape on the index and middle finger of your tying hand", "Inflate only the round part, neck empty, through the sizer", "Stretch every neck to 2 or 3 times its length before the knot", "Blocks of 20 and real breaks, switch hands or tasks"],
    "client_body": "Building garlands and columns from duplets: watch the Sempertex Europe video on YouTube.",
    "cta_label": "Order",
    "s3_cover_a": "Sempertex knots:", "s3_cover_b": "sore fingers", "s3_cover_c": "vs.", "s3_cover_d": "two-finger knot",
    "s3_left": "SORE FINGERS", "s3_right": "TWO-FINGER KNOT", "s3_left_meta": "1 finger, stiff latex", "s3_right_meta": "2 fingers, neck stretched",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["1 finger", "No stretch", "Stiff latex"], "s3_new_tags": ["2 fingers", "Stretch 2 to 3×", "Duplets", "Tape"],
    "s3_new_quote": "“Stretch the neck, round two fingers, end through the loop. Four hundred knots, and no blisters at night.”", "s3_new_badge": "Soft latex glides",
    "s3_changed_bottom": "Same balloons, same hands.\nNow with 2 fingers and a stretched neck.",
    "s3_topic_lbl": "WHY", "s3_rule1_topic": "Pain", "s3_rule1_old": "Blisters are part of the job",
    "s3_rule1_quote": "“Friction, repetition and stiff latex. Technique fixes the first two, material fixes the third.”",
    "s3_rule2_topic": "Faster", "s3_rule2_old": "Pinch, pull, 400 times",
    "s3_rule2_quote": "“Duplets, blocks of 20 and tape on two fingers. Fewer knots, less friction.”",
    "s3_example_topic": "Duplet and quartet", "s3_example_lbl": "EXAMPLE", "s3_example_quote": "“Duplet in {p0} and {p1}, quartet with {p2} and {p3}. All R12, through the sizer, 100% natural latex.”",
    "s3_client_lbl": "COLLEAGUE", "s3_client_topic": "Long days",
    "s3_client_quote": "“Stretch the neck, wrap two fingers, tape up. That's the whole difference.”",
    "s3_cta_kicker": "Latex that stretches with you instead of fighting back",
    "duplet_lbl": "duplet", "quartet_lbl": "quartet", "ouch_lbl": "2 cm blister", "knot_lbl": "1 knot", "chips": ["100% natural latex", "ISO + TÜV", "colour, neck, stretch, elasticity"],
},
"de": {
    "cover_pills": ["Zwei-Finger-Knoten…", "Hals 2- bis 3-mal dehnen…", "Keine Blasen…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Knoten…",
    "steps_title": "Der Zwei-Finger-Knoten: schneller, und die Finger bleiben heil", "steps_lead": "Der Knoten, in 5 Schritten:",
    "steps": ["Hals mit Daumen und Zeigefinger zudrücken, dort wo der runde Teil beginnt", "Mit der anderen Hand den Hals auf das 2- bis 3-Fache dehnen und kurz halten: so wird das Latex weich", "Hals um Zeige- und Mittelfinger wickeln, nie nur um einen Finger", "Finger leicht spreizen und das Halsende durch die Schlaufe schieben", "Finger herausziehen und den Hals festziehen"],
    "steps_label": "Der Knoten",
    "rule1_label": "Warum es wehtut", "rule1_title": "Knoten tut aus 3 Gründen weh: Reibung, Wiederholung und steifes Latex",
    "rule1_body": "Der Hals reibt hunderte Male über dieselben 2 cm Haut an Zeige- und Mittelfinger, bis sie rot wird und Blasen wirft. Mit den Fingerspitzen zu kneifen ist außerdem die schwächste Art, die Hand zu nutzen. Und steifes Latex braucht mehr Zug und reibt stärker. Weiches Latex gleitet. Technik löst die ersten zwei Punkte, Material den dritten.",
    "rule1_facts": [["2 cm", "Haut, die die ganze Reibung abbekommt"], ["2 Finger", "Zeige und Mittel, nie einer"], ["2- bis 3-mal", "den Hals vor dem Knoten dehnen"], ["400", "Knoten an einem langen Tag"]],
    "rule2_label": "Schneller", "rule2_title": "Schneller knoten mit weniger Schmerz: 5 Gewohnheiten für lange Tage",
    "rule2_body": "Jede Gewohnheit nimmt etwas Reibung oder Wiederholung weg. Zusammen machen sie den Unterschied zwischen einem langen Tag und einem schmerzhaften:",
    "alts": [["Jeden Hals vorher dehnen", "vor dem Aufblasen kurz dehnen: das Latex wird weicher und der Knoten geht leichter."], ["Nur den runden Teil aufblasen", "Hals leer lassen und jeden Ballon durch den Sizer. Luft im Hals kostet dich die Länge, die du brauchst."], ["In Duplets knoten", "2 Ballons Hals an Hals: 1 Knoten statt 2. Trio = Duplet + 1, Quartett = 2 Duplets, Sextett = 2 Trios."], ["In 20er-Blöcken arbeiten", "20 aufblasen, 20 knoten, 20 montieren. Jede Handgruppe bekommt abwechselnd Pause."], ["Hände pflegen", "2 Minuten dehnen vorher und nachher, Gewebeband auf Zeige- und Mittelfinger, Haut eincremen, echte Pausen."]],
    "example_label": "Beispiel", "example_title": "Duplet und Quartett: weniger Knoten, dasselbe Sempertex Latex",
    "ex_items": [["Duplet", "{p0} und {p1} Hals an Hals: 1 Knoten statt 2. Die Basis jeder Girlande und Säule."], ["Quartett", "2 Duplets ineinander gedreht: {p0}, {p1}, {p2} und {p3}, alle vier R12 und durch den Sizer, damit das Set stimmt."]],
    "example_body": "Sempertex Latex ist 100% natürlich, ohne Füllstoffe oder Weichmacher. Jeder Ballon wird vor dem Verlassen der Fabrik auf Farbe, Hals, Dehnung und Elastizität geprüft. ISO- und TÜV-zertifiziert. Weiches Latex gleitet, steifes Latex reibt.",
    "client_label": "Kollegin fragt", "client_title": "Was du antwortest, wenn eine Kollegin fragt",
    "client_answers": [
        "Dann ist Luft im Hals. Blas nur den runden Teil auf und lass den Hals leer; knote dort, wo noch Luft ist, nie darüber. Dehn den Hals vorher auf das 2- bis 3-Fache, dann schließt der Knoten von allein.",
        "Drei Dinge: Hals vor jedem Knoten dehnen, um Zeige- und Mittelfinger wickeln statt um einen, und an langen Tagen Gewebeband auf diese zwei Finger. Und Latex nehmen, das gut dehnt: steifes Latex reibt am stärksten.",
        "Meistens ist Luft im Hals, oder dem Latex fehlt die Reißfestigkeit und Elastizität für die Dehnung. Blas nur den runden Teil auf. Platzt es weiter, liegt es am Material: Füllstoffe machen Latex steif und reißanfällig.",
    ],
    "avoid_lead": "Vor einem langen Knotentag, in 5 Schritten:",
    "steps5": ["Finger, Hände und Unterarme dehnen: 2 Minuten", "Gewebeband auf Zeige- und Mittelfinger der Knotenhand", "Nur den runden Teil aufblasen, Hals leer, durch den Sizer", "Jeden Hals vor dem Knoten auf das 2- bis 3-Fache dehnen", "20er-Blöcke und echte Pausen, Hand oder Aufgabe wechseln"],
    "client_body": "Girlanden und Säulen aus Duplets bauen: schau dir das Video von Sempertex Europe auf YouTube an.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex Knoten:", "s3_cover_b": "wunde Finger", "s3_cover_c": "vs.", "s3_cover_d": "Zwei-Finger-Knoten",
    "s3_left": "WUNDE FINGER", "s3_right": "ZWEI-FINGER-KNOTEN", "s3_left_meta": "1 Finger, steifes Latex", "s3_right_meta": "2 Finger, Hals gedehnt",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["1 Finger", "Nicht dehnen", "Steifes Latex"], "s3_new_tags": ["2 Finger", "2- bis 3-mal dehnen", "Duplets", "Tape"],
    "s3_new_quote": "“Hals dehnen, um zwei Finger, Ende durch die Schlaufe. Vierhundert Knoten, und abends keine Blasen.”", "s3_new_badge": "Weiches Latex gleitet",
    "s3_changed_bottom": "Dieselben Ballons, dieselben Hände.\nJetzt mit 2 Fingern und gedehntem Hals.",
    "s3_topic_lbl": "WARUM", "s3_rule1_topic": "Schmerz", "s3_rule1_old": "Blasen gehören zum Job",
    "s3_rule1_quote": "“Reibung, Wiederholung und steifes Latex. Technik löst die ersten zwei, Material den dritten.”",
    "s3_rule2_topic": "Schneller", "s3_rule2_old": "Kneifen, ziehen, 400-mal",
    "s3_rule2_quote": "“Duplets, 20er-Blöcke und Tape auf zwei Fingern. Weniger Knoten, weniger Reibung.”",
    "s3_example_topic": "Duplet und Quartett", "s3_example_lbl": "BEISPIEL", "s3_example_quote": "“Duplet in {p0} und {p1}, Quartett mit {p2} und {p3}. Alle R12, durch den Sizer, 100% natürliches Latex.”",
    "s3_client_lbl": "KOLLEGIN", "s3_client_topic": "Lange Tage",
    "s3_client_quote": "“Hals dehnen, um zwei Finger wickeln, Tape drauf. Das ist der ganze Unterschied.”",
    "s3_cta_kicker": "Latex, das mitdehnt, statt sich zu wehren",
    "duplet_lbl": "Duplet", "quartet_lbl": "Quartett", "ouch_lbl": "2 cm Blase", "knot_lbl": "1 Knoten", "chips": ["100% Naturlatex", "ISO + TÜV", "Farbe, Hals, Dehnung, Elastizität"],
},
"fr": {
    "cover_pills": ["Nœud à deux doigts…", "Étirer le col 2 à 3 fois…", "Zéro ampoule…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Nouer…",
    "steps_title": "Le nœud à deux doigts : plus vite, et tes doigts restent entiers", "steps_lead": "Le nœud, en 5 étapes :",
    "steps": ["Pince le col entre le pouce et l'index, là où la partie ronde commence", "De l'autre main, étire le col à 2 ou 3 fois sa longueur et tiens un instant : le latex s'assouplit", "Enroule le col autour de l'index et du majeur, jamais d'un seul doigt", "Écarte légèrement les doigts et passe le bout du col dans la boucle", "Retire les doigts et serre le col"],
    "steps_label": "Le nœud",
    "rule1_label": "Pourquoi ça fait mal", "rule1_title": "Nouer fait mal pour 3 raisons : le frottement, la répétition et le latex rigide",
    "rule1_body": "Le col frotte des centaines de fois sur les mêmes 2 cm de peau de l'index et du majeur, jusqu'à ce qu'elle rougisse et cloque. Pincer du bout des doigts est aussi la façon la plus faible d'utiliser sa main. Et le latex rigide demande plus de traction et frotte plus fort. Le latex souple glisse. La technique règle les deux premiers points, le matériau le troisième.",
    "rule1_facts": [["2 cm", "de peau qui encaissent tout le frottement"], ["2 doigts", "index et majeur, jamais un seul"], ["2 à 3 fois", "étirer le col avant le nœud"], ["400", "nœuds sur une longue journée"]],
    "rule2_label": "Plus vite", "rule2_title": "Nouer plus vite avec moins de douleur : 5 habitudes pour les longues journées",
    "rule2_body": "Chaque habitude enlève un peu de frottement ou de répétition. Ensemble, elles font la différence entre une longue journée et une journée douloureuse :",
    "alts": [["Étire chaque col d'abord", "un petit étirement avant de gonfler : le latex s'assouplit et le nœud passe plus facilement."], ["Gonfle seulement la partie ronde", "laisse le col vide et passe chaque ballon au calibreur. L'air dans le col te vole la longueur dont tu as besoin."], ["Noue en duplets", "2 ballons col contre col : 1 nœud au lieu de 2. Trio = duplet + 1, quatuor = 2 duplets, sextuor = 2 trios."], ["Travaille par blocs de 20", "gonfle 20, noue 20, assemble 20. Chaque groupe de la main se repose à son tour."], ["Prends soin de tes mains", "2 minutes d'étirements avant et après, tape en tissu sur l'index et le majeur, peau hydratée, vraies pauses."]],
    "example_label": "Exemple", "example_title": "Duplet et quatuor : moins de nœuds, le même latex Sempertex",
    "ex_items": [["Duplet", "{p0} et {p1} col contre col : 1 nœud au lieu de 2. La base de chaque guirlande et colonne."], ["Quatuor", "2 duplets entrelacés : {p0}, {p1}, {p2} et {p3}, les quatre en R12 et passés au calibreur pour un ensemble régulier."]],
    "example_body": "Le latex Sempertex est 100 % naturel, sans charges ni plastifiants. Chaque ballon est contrôlé sur la couleur, le col, l'étirement et l'élasticité avant de quitter l'usine. Certifié ISO et TÜV. Le latex souple glisse, le latex rigide frotte.",
    "client_label": "Un collègue demande", "client_title": "Ce que tu réponds quand un collègue demande",
    "client_answers": [
        "Alors il y a de l'air dans le col. Gonfle seulement la partie ronde et laisse le col vide ; noue là où il reste de l'air, jamais au-dessus. Étire d'abord le col à 2 ou 3 fois sa longueur et le nœud se ferme tout seul.",
        "Trois choses : étire le col avant chaque nœud, enroule autour de l'index et du majeur plutôt que d'un seul doigt, et les longs jours, mets du tape en tissu sur ces deux doigts. Et utilise un latex qui s'étire bien : le latex rigide frotte le plus.",
        "En général, il y a de l'air coincé dans le col, ou le latex n'a pas la résistance et l'élasticité pour l'étirement. Gonfle seulement la partie ronde. Si ça continue d'éclater, c'est le matériau : les charges rendent le latex rigide et fragile.",
    ],
    "avoid_lead": "Avant une longue journée de nœuds, en 5 étapes :",
    "steps5": ["Étire doigts, mains et avant-bras : 2 minutes", "Tape en tissu sur l'index et le majeur de ta main qui noue", "Gonfle seulement la partie ronde, col vide, au calibreur", "Étire chaque col à 2 ou 3 fois sa longueur avant le nœud", "Blocs de 20 et vraies pauses, change de main ou de tâche"],
    "client_body": "Monter guirlandes et colonnes à partir de duplets : regarde la vidéo de Sempertex Europe sur YouTube.",
    "cta_label": "Commander",
    "s3_cover_a": "Nœuds Sempertex :", "s3_cover_b": "doigts à vif", "s3_cover_c": "vs.", "s3_cover_d": "nœud à deux doigts",
    "s3_left": "DOIGTS À VIF", "s3_right": "NŒUD À DEUX DOIGTS", "s3_left_meta": "1 doigt, latex rigide", "s3_right_meta": "2 doigts, col étiré",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["1 doigt", "Pas d'étirement", "Latex rigide"], "s3_new_tags": ["2 doigts", "Étirer 2 à 3 fois", "Duplets", "Tape"],
    "s3_new_quote": "“Étirer le col, autour de deux doigts, le bout dans la boucle. Quatre cents nœuds, et aucune ampoule le soir.”", "s3_new_badge": "Le latex souple glisse",
    "s3_changed_bottom": "Mêmes ballons, mêmes mains.\nMaintenant avec 2 doigts et un col étiré.",
    "s3_topic_lbl": "POURQUOI", "s3_rule1_topic": "Douleur", "s3_rule1_old": "Les ampoules font partie du métier",
    "s3_rule1_quote": "“Frottement, répétition et latex rigide. La technique règle les deux premiers, le matériau le troisième.”",
    "s3_rule2_topic": "Plus vite", "s3_rule2_old": "Pincer, tirer, 400 fois",
    "s3_rule2_quote": "“Duplets, blocs de 20 et tape sur deux doigts. Moins de nœuds, moins de frottement.”",
    "s3_example_topic": "Duplet et quatuor", "s3_example_lbl": "EXEMPLE", "s3_example_quote": "“Duplet en {p0} et {p1}, quatuor avec {p2} et {p3}. Tout en R12, au calibreur, latex 100 % naturel.”",
    "s3_client_lbl": "COLLÈGUE", "s3_client_topic": "Longues journées",
    "s3_client_quote": "“Étirer le col, enrouler deux doigts, poser du tape. C'est toute la différence.”",
    "s3_cta_kicker": "Un latex qui s'étire avec toi au lieu de résister",
    "duplet_lbl": "duplet", "quartet_lbl": "quatuor", "ouch_lbl": "2 cm d'ampoule", "knot_lbl": "1 nœud", "chips": ["latex 100 % naturel", "ISO + TÜV", "couleur, col, étirement, élasticité"],
},
"it": {
    "cover_pills": ["Nodo a due dita…", "Collo allungato 2 o 3 volte…", "Zero vesciche…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Annodare…",
    "steps_title": "Il nodo a due dita: più veloce, e le dita restano intere", "steps_lead": "Il nodo, in 5 passi:",
    "steps": ["Stringi il collo tra pollice e indice, dove inizia la parte rotonda", "Con l'altra mano allunga il collo a 2 o 3 volte la sua lunghezza e tieni un attimo: il lattice si ammorbidisce", "Avvolgi il collo attorno a indice e medio, mai a un solo dito", "Apri leggermente le dita e fai passare la punta del collo nell'anello", "Sfila le dita e tira il collo"],
    "steps_label": "Il nodo",
    "rule1_label": "Perché fa male", "rule1_title": "Annodare fa male per 3 motivi: attrito, ripetizione e lattice rigido",
    "rule1_body": "Il collo sfrega centinaia di volte sugli stessi 2 cm di pelle di indice e medio, finché non si arrossa e si forma la vescica. Stringere con i polpastrelli è anche il modo più debole di usare la mano. E il lattice rigido richiede più trazione e sfrega più forte. Il lattice morbido scivola. La tecnica risolve i primi due punti, il materiale il terzo.",
    "rule1_facts": [["2 cm", "di pelle che prendono tutto l'attrito"], ["2 dita", "indice e medio, mai uno solo"], ["2 o 3 volte", "allungare il collo prima del nodo"], ["400", "nodi in una giornata lunga"]],
    "rule2_label": "Più veloce", "rule2_title": "Annodare più veloce con meno dolore: 5 abitudini per le giornate lunghe",
    "rule2_body": "Ogni abitudine toglie un po' di attrito o di ripetizione. Insieme fanno la differenza tra una giornata lunga e una dolorosa:",
    "alts": [["Allunga ogni collo prima", "un allungamento veloce prima di gonfiare: il lattice si ammorbidisce e il nodo entra più facile."], ["Gonfia solo la parte rotonda", "lascia il collo vuoto e passa ogni palloncino nel calibratore. L'aria nel collo ti ruba la lunghezza che ti serve."], ["Annoda in duplet", "2 palloncini collo contro collo: 1 nodo invece di 2. Trio = duplet + 1, quartetto = 2 duplet, sestetto = 2 trii."], ["Lavora a blocchi di 20", "gonfia 20, annoda 20, monta 20. Ogni gruppo della mano riposa a turno."], ["Cura le mani", "2 minuti di stretching prima e dopo, nastro in tessuto su indice e medio, pelle idratata, pause vere."]],
    "example_label": "Esempio", "example_title": "Duplet e quartetto: meno nodi, lo stesso lattice Sempertex",
    "ex_items": [["Duplet", "{p0} e {p1} collo contro collo: 1 nodo invece di 2. La base di ogni ghirlanda e colonna."], ["Quartetto", "2 duplet intrecciati: {p0}, {p1}, {p2} e {p3}, tutti e quattro R12 e passati nel calibratore, così il set è uniforme."]],
    "example_body": "Il lattice Sempertex è 100% naturale, senza riempitivi né plastificanti. Ogni palloncino viene controllato su colore, collo, allungamento ed elasticità prima di lasciare la fabbrica. Certificato ISO e TÜV. Il lattice morbido scivola, quello rigido sfrega.",
    "client_label": "Un collega chiede", "client_title": "Cosa rispondi quando un collega chiede",
    "client_answers": [
        "Allora c'è aria nel collo. Gonfia solo la parte rotonda e lascia il collo vuoto; annoda dove c'è ancora aria, mai sopra. Allunga prima il collo a 2 o 3 volte la sua lunghezza e il nodo si chiude da solo.",
        "Tre cose: allunga il collo prima di ogni nodo, avvolgi attorno a indice e medio invece che a un dito solo, e nelle giornate lunghe metti nastro in tessuto su quelle due dita. E usa lattice che si allunga bene: quello rigido sfrega di più.",
        "Di solito c'è aria intrappolata nel collo, oppure al lattice mancano resistenza ed elasticità per l'allungamento. Gonfia solo la parte rotonda. Se continua a scoppiare, è il materiale: i riempitivi rendono il lattice rigido e facile da strappare.",
    ],
    "avoid_lead": "Prima di una lunga giornata di nodi, in 5 passi:",
    "steps5": ["Allunga dita, mani e avambracci: 2 minuti", "Nastro in tessuto su indice e medio della mano che annoda", "Gonfia solo la parte rotonda, collo vuoto, nel calibratore", "Allunga ogni collo a 2 o 3 volte la lunghezza prima del nodo", "Blocchi di 20 e pause vere, cambia mano o compito"],
    "client_body": "Costruire ghirlande e colonne dai duplet: guarda il video di Sempertex Europe su YouTube.",
    "cta_label": "Ordina",
    "s3_cover_a": "Nodi Sempertex:", "s3_cover_b": "dita doloranti", "s3_cover_c": "vs.", "s3_cover_d": "nodo a due dita",
    "s3_left": "DITA DOLORANTI", "s3_right": "NODO A DUE DITA", "s3_left_meta": "1 dito, lattice rigido", "s3_right_meta": "2 dita, collo allungato",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["1 dito", "Niente allungamento", "Lattice rigido"], "s3_new_tags": ["2 dita", "Allungare 2 o 3 volte", "Duplet", "Nastro"],
    "s3_new_quote": "“Allungare il collo, attorno a due dita, la punta nell'anello. Quattrocento nodi, e la sera niente vesciche.”", "s3_new_badge": "Il lattice morbido scivola",
    "s3_changed_bottom": "Stessi palloncini, stesse mani.\nOra con 2 dita e il collo allungato.",
    "s3_topic_lbl": "PERCHÉ", "s3_rule1_topic": "Dolore", "s3_rule1_old": "Le vesciche fanno parte del mestiere",
    "s3_rule1_quote": "“Attrito, ripetizione e lattice rigido. La tecnica risolve i primi due, il materiale il terzo.”",
    "s3_rule2_topic": "Più veloce", "s3_rule2_old": "Stringere, tirare, 400 volte",
    "s3_rule2_quote": "“Duplet, blocchi di 20 e nastro su due dita. Meno nodi, meno attrito.”",
    "s3_example_topic": "Duplet e quartetto", "s3_example_lbl": "ESEMPIO", "s3_example_quote": "“Duplet in {p0} e {p1}, quartetto con {p2} e {p3}. Tutti R12, nel calibratore, lattice 100% naturale.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "Giornate lunghe",
    "s3_client_quote": "“Allunga il collo, avvolgi due dita, metti il nastro. È tutta qui la differenza.”",
    "s3_cta_kicker": "Lattice che si allunga con te invece di resistere",
    "duplet_lbl": "duplet", "quartet_lbl": "quartetto", "ouch_lbl": "2 cm di vescica", "knot_lbl": "1 nodo", "chips": ["lattice 100% naturale", "ISO + TÜV", "colore, collo, allungamento, elasticità"],
},
"pl": {
    "cover_pills": ["Węzeł na dwa palce…", "Szyjka rozciągnięta 2 do 3 razy…", "Zero pęcherzy…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Wiązanie…",
    "steps_title": "Węzeł na dwa palce: szybciej, a palce zostają całe", "steps_lead": "Węzeł, w 5 krokach:",
    "steps": ["Ściśnij szyjkę kciukiem i palcem wskazującym tam, gdzie zaczyna się okrągła część", "Drugą ręką rozciągnij szyjkę do 2 lub 3 razy jej długości i przytrzymaj chwilę: lateks mięknie", "Owiń szyjkę wokół palca wskazującego i środkowego, nigdy wokół jednego", "Lekko rozsuń palce i przepchnij koniec szyjki przez pętlę", "Wysuń palce i zaciągnij szyjkę"],
    "steps_label": "Węzeł",
    "rule1_label": "Dlaczego boli", "rule1_title": "Wiązanie boli z 3 powodów: tarcie, powtarzanie i sztywny lateks",
    "rule1_body": "Szyjka setki razy trze o te same 2 cm skóry na palcu wskazującym i środkowym, aż skóra robi się czerwona i pęcherzy. Szczypanie opuszkami to też najsłabszy sposób pracy dłonią. A sztywny lateks wymaga więcej siły i trze mocniej. Miękki lateks się ślizga. Technika załatwia dwa pierwsze punkty, materiał trzeci.",
    "rule1_facts": [["2 cm", "skóry, która zbiera całe tarcie"], ["2 palce", "wskazujący i środkowy, nigdy jeden"], ["2 do 3 razy", "rozciągnij szyjkę przed węzłem"], ["400", "węzłów w długi dzień"]],
    "rule2_label": "Szybciej", "rule2_title": "Szybciej i z mniejszym bólem: 5 nawyków na długie dni",
    "rule2_body": "Każdy nawyk zabiera trochę tarcia albo powtarzania. Razem robią różnicę między długim dniem a bolesnym:",
    "alts": [["Rozciągnij każdą szyjkę wcześniej", "krótkie rozciągnięcie przed pompowaniem: lateks mięknie, a węzeł wchodzi łatwiej."], ["Pompuj tylko okrągłą część", "zostaw szyjkę pustą i każdy balon przepuść przez kalibrator. Powietrze w szyjce zabiera ci długość, której potrzebujesz."], ["Wiąż w duplety", "2 balony szyjka do szyjki: 1 węzeł zamiast 2. Trio = duplet + 1, kwartet = 2 duplety, sekstet = 2 tria."], ["Pracuj w blokach po 20", "20 napompuj, 20 zawiąż, 20 zmontuj. Każda grupa mięśni dłoni odpoczywa po kolei."], ["Dbaj o dłonie", "2 minuty rozciągania przed i po, taśma materiałowa na palec wskazujący i środkowy, nawilżona skóra, prawdziwe przerwy."]],
    "example_label": "Przykład", "example_title": "Duplet i kwartet: mniej węzłów, ten sam lateks Sempertex",
    "ex_items": [["Duplet", "{p0} i {p1} szyjka do szyjki: 1 węzeł zamiast 2. Podstawa każdej girlandy i kolumny."], ["Kwartet", "2 splecione duplety: {p0}, {p1}, {p2} i {p3}, wszystkie R12 i przez kalibrator, żeby zestaw był równy."]],
    "example_body": "Lateks Sempertex jest w 100% naturalny, bez wypełniaczy i plastyfikatorów. Każdy balon jest sprawdzany pod kątem koloru, szyjki, rozciągliwości i elastyczności, zanim opuści fabrykę. Certyfikaty ISO i TÜV. Miękki lateks się ślizga, sztywny trze.",
    "client_label": "Koleżanka pyta", "client_title": "Co odpowiadasz, gdy pyta koleżanka",
    "client_answers": [
        "To powietrze w szyjce. Pompuj tylko okrągłą część i zostaw szyjkę pustą; wiąż tam, gdzie jest jeszcze powietrze, nigdy wyżej. Najpierw rozciągnij szyjkę do 2 lub 3 razy jej długości, a węzeł zamknie się sam.",
        "Trzy rzeczy: rozciągaj szyjkę przed każdym węzłem, owijaj wokół palca wskazującego i środkowego zamiast jednego, a w długie dni naklej taśmę materiałową na te dwa palce. I używaj lateksu, który dobrze się rozciąga: sztywny trze najmocniej.",
        "Zwykle w szyjce jest uwięzione powietrze albo lateksowi brakuje wytrzymałości i elastyczności na rozciąganie. Pompuj tylko okrągłą część. Jeśli dalej pęka, to materiał: wypełniacze robią lateks sztywnym i łatwym do rozerwania.",
    ],
    "avoid_lead": "Przed długim dniem wiązania, w 5 krokach:",
    "steps5": ["Rozciągnij palce, dłonie i przedramiona: 2 minuty", "Taśma materiałowa na palec wskazujący i środkowy ręki wiążącej", "Pompuj tylko okrągłą część, szyjka pusta, przez kalibrator", "Każdą szyjkę rozciągnij do 2 lub 3 razy długości przed węzłem", "Bloki po 20 i prawdziwe przerwy, zmieniaj rękę albo zadanie"],
    "client_body": "Girlandy i kolumny z dupletów: obejrzyj film Sempertex Europe na YouTube.",
    "cta_label": "Zamów",
    "s3_cover_a": "Węzły Sempertex:", "s3_cover_b": "obolałe palce", "s3_cover_c": "vs.", "s3_cover_d": "węzeł na dwa palce",
    "s3_left": "OBOLAŁE PALCE", "s3_right": "WĘZEŁ NA DWA PALCE", "s3_left_meta": "1 palec, sztywny lateks", "s3_right_meta": "2 palce, szyjka rozciągnięta",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["1 palec", "Bez rozciągania", "Sztywny lateks"], "s3_new_tags": ["2 palce", "Rozciągnij 2 do 3 razy", "Duplety", "Taśma"],
    "s3_new_quote": "“Rozciągnąć szyjkę, wokół dwóch palców, koniec przez pętlę. Czterysta węzłów i wieczorem zero pęcherzy.”", "s3_new_badge": "Miękki lateks się ślizga",
    "s3_changed_bottom": "Te same balony, te same ręce.\nTeraz na 2 palce i z rozciągniętą szyjką.",
    "s3_topic_lbl": "DLACZEGO", "s3_rule1_topic": "Ból", "s3_rule1_old": "Pęcherze to część zawodu",
    "s3_rule1_quote": "“Tarcie, powtarzanie i sztywny lateks. Technika załatwia dwa pierwsze, materiał trzeci.”",
    "s3_rule2_topic": "Szybciej", "s3_rule2_old": "Ścisnąć, pociągnąć, 400 razy",
    "s3_rule2_quote": "“Duplety, bloki po 20 i taśma na dwóch palcach. Mniej węzłów, mniej tarcia.”",
    "s3_example_topic": "Duplet i kwartet", "s3_example_lbl": "PRZYKŁAD", "s3_example_quote": "“Duplet w {p0} i {p1}, kwartet z {p2} i {p3}. Wszystko R12, przez kalibrator, lateks w 100% naturalny.”",
    "s3_client_lbl": "KOLEŻANKA", "s3_client_topic": "Długie dni",
    "s3_client_quote": "“Rozciągnij szyjkę, owiń dwa palce, naklej taśmę. To cała różnica.”",
    "s3_cta_kicker": "Lateks, który rozciąga się z tobą zamiast stawiać opór",
    "duplet_lbl": "duplet", "quartet_lbl": "kwartet", "ouch_lbl": "2 cm pęcherza", "knot_lbl": "1 węzeł", "chips": ["lateks 100% naturalny", "ISO + TÜV", "kolor, szyjka, rozciągliwość, elastyczność"],
},
"el": {
    "cover_pills": ["Κόμπος με δύο δάχτυλα…", "Λαιμός τεντωμένος 2 με 3 φορές…", "Καμία φουσκάλα…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Δέσιμο…",
    "steps_title": "Ο κόμπος με δύο δάχτυλα: πιο γρήγορα, και τα δάχτυλά σου μένουν ακέραια", "steps_lead": "Ο κόμπος, σε 5 βήματα:",
    "steps": ["Σφίξε τον λαιμό με αντίχειρα και δείκτη, εκεί που αρχίζει το στρογγυλό μέρος", "Με το άλλο χέρι τέντωσε τον λαιμό στο 2 με 3 φορές το μήκος του και κράτα λίγο: το latex μαλακώνει", "Τύλιξε τον λαιμό γύρω από δείκτη και μέσο, ποτέ μόνο γύρω από ένα δάχτυλο", "Άνοιξε ελαφρά τα δάχτυλα και πέρασε την άκρη του λαιμού μέσα από τη θηλιά", "Τράβα τα δάχτυλα έξω και σφίξε τον λαιμό"],
    "steps_label": "Ο κόμπος",
    "rule1_label": "Γιατί πονάει", "rule1_title": "Το δέσιμο πονάει για 3 λόγους: τριβή, επανάληψη και σκληρό latex",
    "rule1_body": "Ο λαιμός τρίβεται εκατοντάδες φορές στα ίδια 2 cm δέρματος σε δείκτη και μέσο, μέχρι να κοκκινίσει και να βγάλει φουσκάλα. Το τσίμπημα με τις άκρες των δαχτύλων είναι επίσης ο πιο αδύναμος τρόπος να δουλέψεις το χέρι. Και το σκληρό latex θέλει περισσότερο τράβηγμα και τρίβει πιο δυνατά. Το μαλακό latex γλιστράει. Η τεχνική λύνει τα δύο πρώτα, το υλικό το τρίτο.",
    "rule1_facts": [["2 cm", "δέρματος που παίρνουν όλη την τριβή"], ["2 δάχτυλα", "δείκτης και μέσος, ποτέ ένα"], ["2 με 3 φορές", "τέντωμα του λαιμού πριν τον κόμπο"], ["400", "κόμποι σε μια μεγάλη μέρα"]],
    "rule2_label": "Πιο γρήγορα", "rule2_title": "Πιο γρήγορο δέσιμο με λιγότερο πόνο: 5 συνήθειες για μεγάλες μέρες",
    "rule2_body": "Κάθε συνήθεια αφαιρεί λίγη τριβή ή επανάληψη. Μαζί κάνουν τη διαφορά ανάμεσα σε μια μεγάλη μέρα και μια επώδυνη:",
    "alts": [["Τέντωσε κάθε λαιμό πρώτα", "ένα γρήγορο τέντωμα πριν το φούσκωμα: το latex μαλακώνει και ο κόμπος μπαίνει πιο εύκολα."], ["Φούσκωσε μόνο το στρογγυλό μέρος", "άφησε τον λαιμό άδειο και πέρνα κάθε μπαλόνι από το sizer. Ο αέρας στον λαιμό σου κλέβει το μήκος που χρειάζεσαι."], ["Δέσε σε duplets", "2 μπαλόνια λαιμό με λαιμό: 1 κόμπος αντί για 2. Τρίο = duplet + 1, κουαρτέτο = 2 duplets, σεξτέτο = 2 τρίο."], ["Δούλεψε σε μπλοκ των 20", "φούσκωσε 20, δέσε 20, συναρμολόγησε 20. Κάθε ομάδα του χεριού ξεκουράζεται με τη σειρά της."], ["Φρόντισε τα χέρια σου", "2 λεπτά διατάσεις πριν και μετά, υφασμάτινη ταινία σε δείκτη και μέσο, ενυδατωμένο δέρμα, πραγματικά διαλείμματα."]],
    "example_label": "Παράδειγμα", "example_title": "Duplet και κουαρτέτο: λιγότεροι κόμποι, το ίδιο latex Sempertex",
    "ex_items": [["Duplet", "{p0} και {p1} λαιμό με λαιμό: 1 κόμπος αντί για 2. Η βάση κάθε γιρλάντας και κολόνας."], ["Κουαρτέτο", "2 duplets πλεγμένα: {p0}, {p1}, {p2} και {p3}, και τα τέσσερα R12 και από το sizer, ώστε το σετ να ταιριάζει."]],
    "example_body": "Το latex της Sempertex είναι 100% φυσικό, χωρίς πληρωτικά ή πλαστικοποιητές. Κάθε μπαλόνι ελέγχεται για χρώμα, λαιμό, τέντωμα και ελαστικότητα πριν φύγει από το εργοστάσιο. Πιστοποιημένο ISO και TÜV. Το μαλακό latex γλιστράει, το σκληρό τρίβει.",
    "client_label": "Ρωτάει συνάδελφος", "client_title": "Τι απαντάς όταν ρωτάει ένας συνάδελφος",
    "client_answers": [
        "Τότε υπάρχει αέρας στον λαιμό. Φούσκωσε μόνο το στρογγυλό μέρος και άφησε τον λαιμό άδειο· δέσε εκεί που υπάρχει ακόμα αέρας, ποτέ πιο πάνω. Τέντωσε πρώτα τον λαιμό στο 2 με 3 φορές το μήκος του και ο κόμπος κλείνει μόνος του.",
        "Τρία πράγματα: τέντωνε τον λαιμό πριν από κάθε κόμπο, τύλιγε γύρω από δείκτη και μέσο αντί για ένα δάχτυλο, και τις μεγάλες μέρες βάλε υφασμάτινη ταινία σε αυτά τα δύο δάχτυλα. Και χρησιμοποίησε latex που τεντώνει καλά: το σκληρό τρίβει πιο πολύ.",
        "Συνήθως έχει παγιδευτεί αέρας στον λαιμό, ή το latex δεν έχει την αντοχή και την ελαστικότητα για το τέντωμα. Φούσκωσε μόνο το στρογγυλό μέρος. Αν συνεχίζει να σκάει, φταίει το υλικό: τα πληρωτικά κάνουν το latex σκληρό και εύκολο να σκιστεί.",
    ],
    "avoid_lead": "Πριν από μια μεγάλη μέρα δεσίματος, σε 5 βήματα:",
    "steps5": ["Διατάσεις σε δάχτυλα, χέρια και πήχεις: 2 λεπτά", "Υφασμάτινη ταινία σε δείκτη και μέσο του χεριού που δένει", "Φούσκωμα μόνο στο στρογγυλό μέρος, λαιμός άδειος, από το sizer", "Τέντωμα κάθε λαιμού στο 2 με 3 φορές το μήκος πριν τον κόμπο", "Μπλοκ των 20 και πραγματικά διαλείμματα, άλλαξε χέρι ή εργασία"],
    "client_body": "Γιρλάντες και κολόνες από duplets: δες το βίντεο της Sempertex Europe στο YouTube.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Κόμποι Sempertex:", "s3_cover_b": "πονεμένα δάχτυλα", "s3_cover_c": "vs.", "s3_cover_d": "κόμπος με δύο δάχτυλα",
    "s3_left": "ΠΟΝΕΜΕΝΑ ΔΑΧΤΥΛΑ", "s3_right": "ΚΟΜΠΟΣ ΜΕ ΔΥΟ ΔΑΧΤΥΛΑ", "s3_left_meta": "1 δάχτυλο, σκληρό latex", "s3_right_meta": "2 δάχτυλα, τεντωμένος λαιμός",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["1 δάχτυλο", "Χωρίς τέντωμα", "Σκληρό latex"], "s3_new_tags": ["2 δάχτυλα", "Τέντωμα 2 με 3 φορές", "Duplets", "Ταινία"],
    "s3_new_quote": "“Τέντωμα λαιμού, γύρω από δύο δάχτυλα, άκρη μέσα από τη θηλιά. Τετρακόσιοι κόμποι, και το βράδυ καμία φουσκάλα.”", "s3_new_badge": "Το μαλακό latex γλιστράει",
    "s3_changed_bottom": "Ίδια μπαλόνια, ίδια χέρια.\nΤώρα με 2 δάχτυλα και τεντωμένο λαιμό.",
    "s3_topic_lbl": "ΓΙΑΤΙ", "s3_rule1_topic": "Πόνος", "s3_rule1_old": "Οι φουσκάλες είναι μέρος της δουλειάς",
    "s3_rule1_quote": "“Τριβή, επανάληψη και σκληρό latex. Η τεχνική λύνει τα δύο πρώτα, το υλικό το τρίτο.”",
    "s3_rule2_topic": "Πιο γρήγορα", "s3_rule2_old": "Τσίμπα, τράβα, 400 φορές",
    "s3_rule2_quote": "“Duplets, μπλοκ των 20 και ταινία σε δύο δάχτυλα. Λιγότεροι κόμποι, λιγότερη τριβή.”",
    "s3_example_topic": "Duplet και κουαρτέτο", "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_quote": "“Duplet σε {p0} και {p1}, κουαρτέτο με {p2} και {p3}. Όλα R12, από το sizer, 100% φυσικό latex.”",
    "s3_client_lbl": "ΣΥΝΑΔΕΛΦΟΣ", "s3_client_topic": "Μεγάλες μέρες",
    "s3_client_quote": "“Τέντωσε τον λαιμό, τύλιξε δύο δάχτυλα, βάλε ταινία. Αυτή είναι όλη η διαφορά.”",
    "s3_cta_kicker": "Latex που τεντώνει μαζί σου αντί να αντιστέκεται",
    "duplet_lbl": "duplet", "quartet_lbl": "κουαρτέτο", "ouch_lbl": "2 cm φουσκάλα", "knot_lbl": "1 κόμπος", "chips": ["100% φυσικό latex", "ISO + TÜV", "χρώμα, λαιμός, τέντωμα, ελαστικότητα"],
},
"hu": {
    "cover_pills": ["Kétujjas csomó…", "Nyak 2-3-szorosára nyújtva…", "Nincs hólyag…"], "cover_with": "ezzel:", "cover_brand": "Sempertex Europe", "cover_tag": "Csomózás…",
    "steps_title": "A kétujjas csomó: gyorsabb, és az ujjaid épek maradnak", "steps_lead": "A csomó, 5 lépésben:",
    "steps": ["Csípd össze a nyakat hüvelyk- és mutatóujjal ott, ahol a kerek rész kezdődik", "A másik kezeddel nyújtsd a nyakat a 2-3-szorosára, és tartsd meg egy pillanatra: így puhul meg a latex", "Tekerd a nyakat a mutató- és a középső ujjad köré, soha ne csak egy ujj köré", "Nyisd szét kicsit az ujjaidat, és told át a nyak végét a hurkon", "Húzd ki az ujjaidat, és húzd meg a nyakat"],
    "steps_label": "A csomó",
    "rule1_label": "Miért fáj", "rule1_title": "A csomózás 3 okból fáj: súrlódás, ismétlés és merev latex",
    "rule1_body": "A nyak több százszor dörzsöli ugyanazt a 2 cm bőrt a mutató- és középső ujjadon, amíg kipirosodik és felhólyagosodik. Az ujjbeggyel csípés ráadásul a leggyengébb módja a kéz használatának. A merev latex pedig több húzóerőt kér, és erősebben dörzsöl. A puha latex siklik. A technika az első kettőt oldja meg, az anyag a harmadikat.",
    "rule1_facts": [["2 cm", "bőr, ami az összes súrlódást kapja"], ["2 ujj", "mutató és középső, soha egy"], ["2-3-szoros", "nyújtsd a nyakat a csomó előtt"], ["400", "csomó egy hosszú napon"]],
    "rule2_label": "Gyorsabban", "rule2_title": "Gyorsabb csomózás kevesebb fájdalommal: 5 szokás hosszú napokra",
    "rule2_body": "Minden szokás elvesz egy kis súrlódást vagy ismétlést. Együtt ez a különbség egy hosszú nap és egy fájdalmas között:",
    "alts": [["Nyújts meg minden nyakat előre", "egy gyors nyújtás felfújás előtt: a latex megpuhul, és a csomó könnyebben megy."], ["Csak a kerek részt fújd fel", "hagyd üresen a nyakat, és minden lufit vigyél át a méretezőn. A nyakban lévő levegő elveszi a hosszt, amire szükséged van."], ["Csomózz dupletekben", "2 lufi nyakat nyakhoz: 1 csomó 2 helyett. Trió = duplet + 1, kvartett = 2 duplet, szextett = 2 trió."], ["Dolgozz 20-as blokkokban", "20 felfújás, 20 csomó, 20 szerelés. Minden kézizomcsoport sorban pihen."], ["Ápold a kezed", "2 perc nyújtás előtte és utána, textilszalag a mutató- és középső ujjra, hidratált bőr, valódi szünetek."]],
    "example_label": "Példa", "example_title": "Duplet és kvartett: kevesebb csomó, ugyanaz a Sempertex latex",
    "ex_items": [["Duplet", "{p0} és {p1} nyakat nyakhoz: 1 csomó 2 helyett. Minden girland és oszlop alapja."], ["Kvartett", "2 egymásba fordított duplet: {p0}, {p1}, {p2} és {p3}, mind a négy R12 és méretezőn átvive, hogy a szett egyforma legyen."]],
    "example_body": "A Sempertex latex 100% természetes, töltőanyag és lágyító nélkül. Minden lufit ellenőriznek szín, nyak, nyúlás és rugalmasság szerint, mielőtt elhagyja a gyárat. ISO- és TÜV-tanúsítvánnyal. A puha latex siklik, a merev dörzsöl.",
    "client_label": "Kolléga kérdezi", "client_title": "Mit válaszolsz, ha egy kolléga kérdezi",
    "client_answers": [
        "Akkor levegő van a nyakban. Csak a kerek részt fújd fel, és hagyd üresen a nyakat; ott csomózz, ahol még van levegő, soha felette. Előtte nyújtsd a nyakat a 2-3-szorosára, és a csomó magától záródik.",
        "Három dolog: nyújtsd a nyakat minden csomó előtt, tekerd a mutató- és középső ujj köré egy helyett, és hosszú napokon tegyél textilszalagot erre a két ujjra. És használj jól nyúló latexet: a merev dörzsöl a legjobban.",
        "Általában levegő szorult a nyakba, vagy a latexnek nincs meg a szakítószilárdsága és rugalmassága a nyújtáshoz. Csak a kerek részt fújd fel. Ha továbbra is durran, az anyag a gond: a töltőanyagok merevvé és könnyen szakadóvá teszik a latexet.",
    ],
    "avoid_lead": "Egy hosszú csomózós nap előtt, 5 lépésben:",
    "steps5": ["Nyújtsd az ujjakat, kezeket és alkarokat: 2 perc", "Textilszalag a csomózó kéz mutató- és középső ujjára", "Csak a kerek részt fújd fel, nyak üres, méretezőn át", "Minden nyakat nyújts a 2-3-szorosára a csomó előtt", "20-as blokkok és valódi szünetek, válts kezet vagy feladatot"],
    "client_body": "Girlandok és oszlopok dupletekből: nézd meg a Sempertex Europe videóját a YouTube-on.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Sempertex csomók:", "s3_cover_b": "fájó ujjak", "s3_cover_c": "vs.", "s3_cover_d": "kétujjas csomó",
    "s3_left": "FÁJÓ UJJAK", "s3_right": "KÉTUJJAS CSOMÓ", "s3_left_meta": "1 ujj, merev latex", "s3_right_meta": "2 ujj, nyújtott nyak",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["1 ujj", "Nincs nyújtás", "Merev latex"], "s3_new_tags": ["2 ujj", "2-3-szoros nyújtás", "Dupletek", "Szalag"],
    "s3_new_quote": "“Nyak nyújtása, két ujj köré, a vég át a hurkon. Négyszáz csomó, és este semmi hólyag.”", "s3_new_badge": "A puha latex siklik",
    "s3_changed_bottom": "Ugyanazok a lufik, ugyanazok a kezek.\nMost 2 ujjal és nyújtott nyakkal.",
    "s3_topic_lbl": "MIÉRT", "s3_rule1_topic": "Fájdalom", "s3_rule1_old": "A hólyag hozzátartozik a szakmához",
    "s3_rule1_quote": "“Súrlódás, ismétlés és merev latex. A technika az első kettőt oldja meg, az anyag a harmadikat.”",
    "s3_rule2_topic": "Gyorsabban", "s3_rule2_old": "Csípni, húzni, 400-szor",
    "s3_rule2_quote": "“Dupletek, 20-as blokkok és szalag két ujjon. Kevesebb csomó, kevesebb súrlódás.”",
    "s3_example_topic": "Duplet és kvartett", "s3_example_lbl": "PÉLDA", "s3_example_quote": "“Duplet {p0} és {p1} színben, kvartett {p2} és {p3} színnel. Mind R12, méretezőn át, 100% természetes latex.”",
    "s3_client_lbl": "KOLLÉGA", "s3_client_topic": "Hosszú napok",
    "s3_client_quote": "“Nyújtsd a nyakat, tekerd két ujj köré, ragassz szalagot. Ennyi az egész különbség.”",
    "s3_cta_kicker": "Latex, ami veled nyúlik, nem ellened dolgozik",
    "duplet_lbl": "duplet", "quartet_lbl": "kvartett", "ouch_lbl": "2 cm hólyag", "knot_lbl": "1 csomó", "chips": ["100% természetes latex", "ISO + TÜV", "szín, nyak, nyúlás, rugalmasság"],
},
"lt": {
    "cover_pills": ["Dviejų pirštų mazgas…", "Kaklelis ištemptas 2-3 kartus…", "Jokių pūslių…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Rišimas…",
    "steps_title": "Dviejų pirštų mazgas: greičiau, o pirštai lieka sveiki", "steps_lead": "Mazgas, 5 žingsniais:",
    "steps": ["Suspausk kaklelį nykščiu ir smiliumi ten, kur prasideda apvali dalis", "Kita ranka ištempk kaklelį iki 2-3 kartų jo ilgio ir trumpam palaikyk: lateksas suminkštėja", "Apvyniok kaklelį aplink smilių ir didįjį pirštą, niekada tik aplink vieną", "Šiek tiek praskėsk pirštus ir prakišk kaklelio galą pro kilpą", "Ištrauk pirštus ir užveržk kaklelį"],
    "steps_label": "Mazgas",
    "rule1_label": "Kodėl skauda", "rule1_title": "Rišti skauda dėl 3 priežasčių: trinties, kartojimo ir standaus latekso",
    "rule1_body": "Kaklelis šimtus kartų trinasi į tuos pačius 2 cm odos ant smiliaus ir didžiojo piršto, kol ji parausta ir atsiranda pūslė. Gnybimas pirštų galiukais taip pat yra silpniausias būdas dirbti ranka. O standus lateksas reikalauja daugiau traukos ir trinasi stipriau. Minkštas lateksas slysta. Technika išsprendžia pirmas dvi problemas, medžiaga trečią.",
    "rule1_facts": [["2 cm", "odos, kuri priima visą trintį"], ["2 pirštai", "smilius ir didysis, niekada vienas"], ["2-3 kartus", "ištempk kaklelį prieš mazgą"], ["400", "mazgų per ilgą dieną"]],
    "rule2_label": "Greičiau", "rule2_title": "Greičiau rišti su mažiau skausmo: 5 įpročiai ilgoms dienoms",
    "rule2_body": "Kiekvienas įprotis nuima šiek tiek trinties ar kartojimo. Kartu jie skiria ilgą dieną nuo skausmingos:",
    "alts": [["Pirma ištempk kiekvieną kaklelį", "trumpas ištempimas prieš pučiant: lateksas suminkštėja, mazgas eina lengviau."], ["Pūsk tik apvalią dalį", "palik kaklelį tuščią ir kiekvieną balioną perleisk per matuoklį. Oras kaklelyje atima reikiamą ilgį."], ["Rišk dupletais", "2 balionai kaklelis prie kaklelio: 1 mazgas vietoj 2. Trio = dupletas + 1, kvartetas = 2 dupletai, sekstetas = 2 trio."], ["Dirbk blokais po 20", "pripūsk 20, surišk 20, sumontuok 20. Kiekviena rankos raumenų grupė pailsi paeiliui."], ["Prižiūrėk rankas", "2 minutės tempimo prieš ir po, medžiaginė juosta ant smiliaus ir didžiojo piršto, drėkinta oda, tikros pertraukos."]],
    "example_label": "Pavyzdys", "example_title": "Dupletas ir kvartetas: mažiau mazgų, tas pats Sempertex lateksas",
    "ex_items": [["Dupletas", "{p0} ir {p1} kaklelis prie kaklelio: 1 mazgas vietoj 2. Kiekvienos girliandos ir kolonos pagrindas."], ["Kvartetas", "2 supinti dupletai: {p0}, {p1}, {p2} ir {p3}, visi keturi R12 ir per matuoklį, kad rinkinys būtų vienodas."]],
    "example_body": "Sempertex lateksas yra 100% natūralus, be užpildų ir plastifikatorių. Kiekvienas balionas prieš išvežant iš gamyklos tikrinamas pagal spalvą, kaklelį, tempimą ir elastingumą. ISO ir TÜV sertifikuotas. Minkštas lateksas slysta, standus trinasi.",
    "client_label": "Klausia kolegė", "client_title": "Ką atsakai, kai klausia kolegė",
    "client_answers": [
        "Tada kaklelyje yra oro. Pūsk tik apvalią dalį ir palik kaklelį tuščią; rišk ten, kur dar yra oro, niekada aukščiau. Pirma ištempk kaklelį iki 2-3 kartų jo ilgio, ir mazgas užsidaro pats.",
        "Trys dalykai: ištempk kaklelį prieš kiekvieną mazgą, vyniok aplink smilių ir didįjį pirštą, o ne vieną, o ilgomis dienomis užklijuok medžiaginę juostą ant tų dviejų pirštų. Ir naudok gerai tįstantį lateksą: standus trinasi labiausiai.",
        "Dažniausiai kaklelyje įstrigęs oras arba lateksui trūksta tvirtumo ir elastingumo tempimui. Pūsk tik apvalią dalį. Jei toliau sproginėja, kalta medžiaga: užpildai daro lateksą standų ir lengvai plyštantį.",
    ],
    "avoid_lead": "Prieš ilgą rišimo dieną, 5 žingsniais:",
    "steps5": ["Ištempk pirštus, plaštakas ir dilbius: 2 minutės", "Medžiaginė juosta ant rišančios rankos smiliaus ir didžiojo piršto", "Pūsk tik apvalią dalį, kaklelis tuščias, per matuoklį", "Kiekvieną kaklelį ištempk iki 2-3 kartų ilgio prieš mazgą", "Blokai po 20 ir tikros pertraukos, keisk ranką ar užduotį"],
    "client_body": "Girliandos ir kolonos iš dupletų: žiūrėk Sempertex Europe vaizdo įrašą YouTube.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Sempertex mazgai:", "s3_cover_b": "skaudantys pirštai", "s3_cover_c": "vs.", "s3_cover_d": "dviejų pirštų mazgas",
    "s3_left": "SKAUDANTYS PIRŠTAI", "s3_right": "DVIEJŲ PIRŠTŲ MAZGAS", "s3_left_meta": "1 pirštas, standus lateksas", "s3_right_meta": "2 pirštai, ištemptas kaklelis",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["1 pirštas", "Be tempimo", "Standus lateksas"], "s3_new_tags": ["2 pirštai", "Tempti 2-3 kartus", "Dupletai", "Juosta"],
    "s3_new_quote": "“Ištempti kaklelį, aplink du pirštus, galą pro kilpą. Keturi šimtai mazgų, ir vakare jokių pūslių.”", "s3_new_badge": "Minkštas lateksas slysta",
    "s3_changed_bottom": "Tie patys balionai, tos pačios rankos.\nDabar su 2 pirštais ir ištemptu kakleliu.",
    "s3_topic_lbl": "KODĖL", "s3_rule1_topic": "Skausmas", "s3_rule1_old": "Pūslės yra darbo dalis",
    "s3_rule1_quote": "“Trintis, kartojimas ir standus lateksas. Technika išsprendžia pirmas dvi, medžiaga trečią.”",
    "s3_rule2_topic": "Greičiau", "s3_rule2_old": "Gnybti, traukti, 400 kartų",
    "s3_rule2_quote": "“Dupletai, blokai po 20 ir juosta ant dviejų pirštų. Mažiau mazgų, mažiau trinties.”",
    "s3_example_topic": "Dupletas ir kvartetas", "s3_example_lbl": "PAVYZDYS", "s3_example_quote": "“Dupletas {p0} ir {p1} spalvomis, kvartetas su {p2} ir {p3}. Visi R12, per matuoklį, 100% natūralus lateksas.”",
    "s3_client_lbl": "KOLEGĖ", "s3_client_topic": "Ilgos dienos",
    "s3_client_quote": "“Ištempk kaklelį, apvyniok du pirštus, užklijuok juostą. Tai visas skirtumas.”",
    "s3_cta_kicker": "Lateksas, kuris tįsta kartu su tavimi, o ne priešinasi",
    "duplet_lbl": "dupletas", "quartet_lbl": "kvartetas", "ouch_lbl": "2 cm pūslė", "knot_lbl": "1 mazgas", "chips": ["100% natūralus lateksas", "ISO + TÜV", "spalva, kaklelis, tempimas, elastingumas"],
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["Sneller knopen zonder pijnlijke vingers: de tweevingerknoop met Sempertex latex", "400 knopen op een dag en geen blaren? Sempertex latex en de tweevingerknoop", "Waarom knopen pijn doet, en de knoop in 5 stappen die het oplost. Met Sempertex"],
  "cover_sub": ["Waarom je vingers pijn doen na honderden knopen, de tweevingerknoop in 5 stappen, en 5 gewoontes voor lange dagen.", "Nek rekken, om twee vingers wikkelen, in duplets knopen, blokken van 20. En latex dat meerekt in plaats van schuurt."],
  "client_question": ["Mijn ballonnen lopen leeg na de knoop. Wat doe ik fout?", "Na 100 knopen zijn mijn vingers rauw. Heb je een truc?", "Waarom knappen ballonnen terwijl ik ze knoop?"],
  "s3_old_quote": ["“Knijpen, trekken, 400 keer herhalen”", "“Blaren horen er nu eenmaal bij”", "“Goedkoop latex knoopt even goed”"],
  "s3_client_old": ["“Ik bijt wel door de pijn heen”", "“Tape? Ik knoop met blote vingers”"],
  "cta_title_tpl": "Bestel je Sempertex ballonnen bij {name}", "cta_sub_generic": "100% natuurlijk latex, gecontroleerd op nek, rek en elasticiteit.",
},
"en": {
  "cover_title": ["Tie faster without sore fingers: the two-finger knot with Sempertex latex", "400 knots a day and no blisters? Sempertex latex and the two-finger knot", "Why tying hurts, and the 5-step knot that fixes it. With Sempertex"],
  "cover_sub": ["Why your fingers hurt after hundreds of knots, the two-finger knot in 5 steps, and 5 habits for long days.", "Stretch the neck, wrap two fingers, tie in duplets, work in blocks of 20. And latex that stretches with you instead of rubbing."],
  "client_question": ["My balloons keep deflating after the knot. What am I doing wrong?", "After 100 knots my fingers are raw. Any trick?", "Why do balloons pop while I'm tying them?"],
  "s3_old_quote": ["“Pinch, pull, repeat 400 times”", "“Blisters just come with the job”", "“Cheap latex ties just as well”"],
  "s3_client_old": ["“I'll just push through the pain”", "“Tape? I tie with bare fingers”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "100% natural latex, checked for neck, stretch and elasticity.",
},
"de": {
  "cover_title": ["Schneller knoten ohne wunde Finger: der Zwei-Finger-Knoten mit Sempertex Latex", "400 Knoten am Tag und keine Blasen? Sempertex Latex und der Zwei-Finger-Knoten", "Warum Knoten wehtut, und der Knoten in 5 Schritten, der es löst. Mit Sempertex"],
  "cover_sub": ["Warum die Finger nach hunderten Knoten wehtun, der Zwei-Finger-Knoten in 5 Schritten und 5 Gewohnheiten für lange Tage.", "Hals dehnen, um zwei Finger wickeln, in Duplets knoten, 20er-Blöcke. Und Latex, das mitdehnt, statt zu reiben."],
  "client_question": ["Meine Ballons verlieren nach dem Knoten Luft. Was mache ich falsch?", "Nach 100 Knoten sind meine Finger wund. Hast du einen Trick?", "Warum platzen Ballons, während ich sie knote?"],
  "s3_old_quote": ["“Kneifen, ziehen, 400-mal wiederholen”", "“Blasen gehören eben dazu”", "“Billiges Latex knotet genauso gut”"],
  "s3_client_old": ["“Ich beiß mich durch den Schmerz”", "“Tape? Ich knote mit bloßen Fingern”"],
  "cta_title_tpl": "Bestell deine Sempertex Ballons bei {name}", "cta_sub_generic": "100% Naturlatex, geprüft auf Hals, Dehnung und Elastizität.",
},
"fr": {
  "cover_title": ["Nouer plus vite sans doigts à vif : le nœud à deux doigts avec le latex Sempertex", "400 nœuds par jour et zéro ampoule ? Le latex Sempertex et le nœud à deux doigts", "Pourquoi nouer fait mal, et le nœud en 5 étapes qui règle ça. Avec Sempertex"],
  "cover_sub": ["Pourquoi tes doigts font mal après des centaines de nœuds, le nœud à deux doigts en 5 étapes, et 5 habitudes pour les longues journées.", "Étirer le col, enrouler deux doigts, nouer en duplets, blocs de 20. Et un latex qui s'étire avec toi au lieu de frotter."],
  "client_question": ["Mes ballons se dégonflent après le nœud. Qu'est-ce que je fais mal ?", "Après 100 nœuds, j'ai les doigts à vif. Tu as une astuce ?", "Pourquoi les ballons éclatent pendant que je les noue ?"],
  "s3_old_quote": ["“Pincer, tirer, répéter 400 fois”", "“Les ampoules, ça fait partie du job”", "“Le latex bon marché se noue aussi bien”"],
  "s3_client_old": ["“Je serre les dents et je continue”", "“Du tape ? Je noue à mains nues”"],
  "cta_title_tpl": "Commande tes ballons Sempertex chez {name}", "cta_sub_generic": "Latex 100 % naturel, contrôlé sur le col, l'étirement et l'élasticité.",
},
"it": {
  "cover_title": ["Annodare più veloce senza dita doloranti: il nodo a due dita con il lattice Sempertex", "400 nodi al giorno e zero vesciche? Il lattice Sempertex e il nodo a due dita", "Perché annodare fa male, e il nodo in 5 passi che lo risolve. Con Sempertex"],
  "cover_sub": ["Perché le dita fanno male dopo centinaia di nodi, il nodo a due dita in 5 passi, e 5 abitudini per le giornate lunghe.", "Allungare il collo, avvolgere due dita, annodare in duplet, blocchi di 20. E lattice che si allunga con te invece di sfregare."],
  "client_question": ["I miei palloncini si sgonfiano dopo il nodo. Cosa sbaglio?", "Dopo 100 nodi ho le dita a pezzi. Hai un trucco?", "Perché i palloncini scoppiano mentre li annodo?"],
  "s3_old_quote": ["“Stringere, tirare, ripetere 400 volte”", "“Le vesciche fanno parte del lavoro”", "“Il lattice economico si annoda uguale”"],
  "s3_client_old": ["“Stringo i denti e vado avanti”", "“Nastro? Io annodo a mani nude”"],
  "cta_title_tpl": "Ordina i tuoi palloncini Sempertex da {name}", "cta_sub_generic": "Lattice 100% naturale, controllato su collo, allungamento ed elasticità.",
},
"pl": {
  "cover_title": ["Szybsze wiązanie bez obolałych palców: węzeł na dwa palce z lateksem Sempertex", "400 węzłów dziennie i zero pęcherzy? Lateks Sempertex i węzeł na dwa palce", "Dlaczego wiązanie boli i węzeł w 5 krokach, który to rozwiązuje. Z Sempertex"],
  "cover_sub": ["Dlaczego palce bolą po setkach węzłów, węzeł na dwa palce w 5 krokach i 5 nawyków na długie dni.", "Rozciągnij szyjkę, owiń dwa palce, wiąż w duplety, bloki po 20. I lateks, który rozciąga się z tobą zamiast trzeć."],
  "client_question": ["Moje balony schodzą po zawiązaniu. Co robię źle?", "Po 100 węzłach mam otarte palce. Masz jakiś trik?", "Dlaczego balony pękają, kiedy je wiążę?"],
  "s3_old_quote": ["“Ścisnąć, pociągnąć, powtórzyć 400 razy”", "“Pęcherze po prostu należą do zawodu”", "“Tani lateks wiąże się tak samo”"],
  "s3_client_old": ["“Zacisnę zęby i przetrzymam ból”", "“Taśma? Wiążę gołymi palcami”"],
  "cta_title_tpl": "Zamów balony Sempertex w {name}", "cta_sub_generic": "Lateks w 100% naturalny, sprawdzony pod kątem szyjki, rozciągliwości i elastyczności.",
},
"el": {
  "cover_title": ["Πιο γρήγορο δέσιμο χωρίς πονεμένα δάχτυλα: ο κόμπος με δύο δάχτυλα με latex Sempertex", "400 κόμποι τη μέρα και καμία φουσκάλα; Το latex Sempertex και ο κόμπος με δύο δάχτυλα", "Γιατί το δέσιμο πονάει, και ο κόμπος σε 5 βήματα που το λύνει. Με Sempertex"],
  "cover_sub": ["Γιατί πονάνε τα δάχτυλά σου μετά από εκατοντάδες κόμπους, ο κόμπος με δύο δάχτυλα σε 5 βήματα, και 5 συνήθειες για μεγάλες μέρες.", "Τέντωμα λαιμού, τύλιγμα σε δύο δάχτυλα, δέσιμο σε duplets, μπλοκ των 20. Και latex που τεντώνει μαζί σου αντί να τρίβει."],
  "client_question": ["Τα μπαλόνια μου ξεφουσκώνουν μετά τον κόμπο. Τι κάνω λάθος;", "Μετά από 100 κόμπους τα δάχτυλά μου είναι γδαρμένα. Έχεις κάποιο κόλπο;", "Γιατί σκάνε τα μπαλόνια ενώ τα δένω;"],
  "s3_old_quote": ["“Τσίμπα, τράβα, επανάλαβε 400 φορές”", "“Οι φουσκάλες είναι μέρος της δουλειάς”", "“Το φτηνό latex δένεται το ίδιο καλά”"],
  "s3_client_old": ["“Θα το αντέξω τον πόνο”", "“Ταινία; Εγώ δένω με γυμνά δάχτυλα”"],
  "cta_title_tpl": "Παράγγειλε τα μπαλόνια Sempertex σου από {name}", "cta_sub_generic": "100% φυσικό latex, ελεγμένο για λαιμό, τέντωμα και ελαστικότητα.",
},
"hu": {
  "cover_title": ["Gyorsabb csomózás fájó ujjak nélkül: a kétujjas csomó Sempertex latexszel", "Napi 400 csomó és semmi hólyag? A Sempertex latex és a kétujjas csomó", "Miért fáj a csomózás, és az 5 lépéses csomó, ami megoldja. Sempertex-szel"],
  "cover_sub": ["Miért fájnak az ujjaid több száz csomó után, a kétujjas csomó 5 lépésben, és 5 szokás hosszú napokra.", "Nyak nyújtása, két ujj köré tekerés, csomózás dupletekben, 20-as blokkok. És latex, ami veled nyúlik, nem dörzsöl."],
  "client_question": ["A lufijaim leeresztenek a csomó után. Mit csinálok rosszul?", "100 csomó után kisebesednek az ujjaim. Van valami trükk?", "Miért durrannak a lufik, miközben csomózom őket?"],
  "s3_old_quote": ["“Csípni, húzni, 400-szor ismételni”", "“A hólyag egyszerűen hozzátartozik”", "“Az olcsó latex ugyanúgy csomózható”"],
  "s3_client_old": ["“Összeszorítom a fogam, és kibírom”", "“Szalag? Én csupasz ujjal csomózom”"],
  "cta_title_tpl": "Rendeld a Sempertex lufijaidat innen: {name}", "cta_sub_generic": "100% természetes latex, nyak, nyúlás és rugalmasság szerint ellenőrizve.",
},
"lt": {
  "cover_title": ["Greitesnis rišimas be skaudančių pirštų: dviejų pirštų mazgas su Sempertex lateksu", "400 mazgų per dieną ir jokių pūslių? Sempertex lateksas ir dviejų pirštų mazgas", "Kodėl rišti skauda, ir 5 žingsnių mazgas, kuris tai išsprendžia. Su Sempertex"],
  "cover_sub": ["Kodėl pirštai skauda po šimtų mazgų, dviejų pirštų mazgas 5 žingsniais ir 5 įpročiai ilgoms dienoms.", "Ištempti kaklelį, apvynioti du pirštus, rišti dupletais, blokai po 20. Ir lateksas, kuris tįsta kartu su tavimi, o ne trinasi."],
  "client_question": ["Mano balionai subliūkšta po mazgo. Ką darau ne taip?", "Po 100 mazgų pirštai nutrinti. Turi kokį triuką?", "Kodėl balionai sprogsta, kol juos rišu?"],
  "s3_old_quote": ["“Gnybti, traukti, kartoti 400 kartų”", "“Pūslės tiesiog yra darbo dalis”", "“Pigus lateksas rišasi taip pat gerai”"],
  "s3_client_old": ["“Sukandu dantis ir kenčiu”", "“Juosta? Aš rišu plikais pirštais”"],
  "cta_title_tpl": "Užsisakyk Sempertex balionus iš {name}", "cta_sub_generic": "100% natūralus lateksas, patikrintas pagal kaklelį, tempimą ir elastingumą.",
},
}

CAPTIONS_TPL = {
 "nl": "Knopen doet pijn door wrijving, herhaling en stijf latex. In deze carousel: de tweevingerknoop in 5 stappen (nek 2 à 3 keer rekken, om wijs- én middelvinger wikkelen), alleen het ronde deel opblazen, knopen in duplets, werken in blokken van 20, en handverzorging met stoffen tape. Plus waarom Sempertex latex meerekt: 100% natuurlijk, zonder vulstoffen, gecontroleerd op kleur, nek, rek en elasticiteit.\n\nBestel je Sempertex ballonnen bij {domain}.\n\n#ballonnenknopen #tweevingerknoop #sempertex #{tag} #ballondecoratie #ballonartiest",
 "en": "Tying hurts because of friction, repetition and stiff latex. In this carousel: the two-finger knot in 5 steps (stretch the neck 2 or 3 times, wrap around index and middle finger), inflate only the round part, tie in duplets, work in blocks of 20, and hand care with fabric tape. Plus why Sempertex latex stretches with you: 100% natural, no fillers, checked for colour, neck, stretch and elasticity.\n\nOrder your Sempertex balloons at {domain}.\n\n#balloontying #twofingerknot #sempertex #{tag} #balloondecor #balloonartist",
 "de": "Knoten tut weh wegen Reibung, Wiederholung und steifem Latex. Im Carousel: der Zwei-Finger-Knoten in 5 Schritten (Hals auf das 2- bis 3-Fache dehnen, um Zeige- und Mittelfinger wickeln), nur den runden Teil aufblasen, in Duplets knoten, in 20er-Blöcken arbeiten und Handpflege mit Gewebeband. Plus warum Sempertex Latex mitdehnt: 100% natürlich, ohne Füllstoffe, geprüft auf Farbe, Hals, Dehnung und Elastizität.\n\nBestell deine Sempertex Ballons bei {domain}.\n\n#ballonsknoten #zweifingerknoten #sempertex #{tag} #ballondeko #ballonkünstler",
 "fr": "Nouer fait mal à cause du frottement, de la répétition et du latex rigide. Dans ce carrousel : le nœud à deux doigts en 5 étapes (étirer le col 2 à 3 fois, enrouler autour de l'index et du majeur), gonfler seulement la partie ronde, nouer en duplets, travailler par blocs de 20, et prendre soin de ses mains avec du tape en tissu. Plus pourquoi le latex Sempertex s'étire avec toi : 100 % naturel, sans charges, contrôlé sur la couleur, le col, l'étirement et l'élasticité.\n\nCommande tes ballons Sempertex chez {domain}.\n\n#nouerdesballons #noeudadeuxdoigts #sempertex #{tag} #decorationballons #artisteballon",
 "it": "Annodare fa male per attrito, ripetizione e lattice rigido. Nel carosello: il nodo a due dita in 5 passi (allungare il collo 2 o 3 volte, avvolgere attorno a indice e medio), gonfiare solo la parte rotonda, annodare in duplet, lavorare a blocchi di 20, e la cura delle mani con nastro in tessuto. Più perché il lattice Sempertex si allunga con te: 100% naturale, senza riempitivi, controllato su colore, collo, allungamento ed elasticità.\n\nOrdina i tuoi palloncini Sempertex da {domain}.\n\n#annodarepalloncini #nodoaduedita #sempertex #{tag} #palloncini #balloonartist",
 "pl": "Wiązanie boli przez tarcie, powtarzanie i sztywny lateks. W karuzeli: węzeł na dwa palce w 5 krokach (rozciągnij szyjkę 2 do 3 razy, owiń wokół palca wskazującego i środkowego), pompuj tylko okrągłą część, wiąż w duplety, pracuj w blokach po 20 i dbaj o dłonie taśmą materiałową. Plus dlaczego lateks Sempertex rozciąga się z tobą: w 100% naturalny, bez wypełniaczy, sprawdzony pod kątem koloru, szyjki, rozciągliwości i elastyczności.\n\nZamów balony Sempertex w {domain}.\n\n#wiazaniebalonow #wezelnadwapalce #sempertex #{tag} #dekoracjebalonowe #artystabalonowy",
 "el": "Το δέσιμο πονάει λόγω τριβής, επανάληψης και σκληρού latex. Στο carousel: ο κόμπος με δύο δάχτυλα σε 5 βήματα (τέντωμα λαιμού 2 με 3 φορές, τύλιγμα γύρω από δείκτη και μέσο), φούσκωμα μόνο στο στρογγυλό μέρος, δέσιμο σε duplets, δουλειά σε μπλοκ των 20, και φροντίδα χεριών με υφασμάτινη ταινία. Και γιατί το latex Sempertex τεντώνει μαζί σου: 100% φυσικό, χωρίς πληρωτικά, ελεγμένο για χρώμα, λαιμό, τέντωμα και ελαστικότητα.\n\nΠαράγγειλε τα μπαλόνια Sempertex σου από {domain}.\n\n#δεσιμομπαλονιων #κομποςδυοδαχτυλα #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "A csomózás a súrlódás, az ismétlés és a merev latex miatt fáj. A carouselben: a kétujjas csomó 5 lépésben (nyak nyújtása 2-3-szorosára, tekerés a mutató- és középső ujj köré), csak a kerek rész felfújása, csomózás dupletekben, munka 20-as blokkokban, és kézápolás textilszalaggal. Plusz miért nyúlik veled a Sempertex latex: 100% természetes, töltőanyag nélkül, szín, nyak, nyúlás és rugalmasság szerint ellenőrizve.\n\nRendeld a Sempertex lufijaidat innen: {domain}.\n\n#luficsomozas #ketujjascsomo #sempertex #{tag} #lufidekoracio #lufiművész",
 "lt": "Rišti skauda dėl trinties, kartojimo ir standaus latekso. Karuselėje: dviejų pirštų mazgas 5 žingsniais (kaklelio ištempimas 2-3 kartus, vyniojimas aplink smilių ir didįjį pirštą), pučiama tik apvali dalis, rišimas dupletais, darbas blokais po 20 ir rankų priežiūra medžiagine juosta. Ir kodėl Sempertex lateksas tįsta kartu su tavimi: 100% natūralus, be užpildų, patikrintas pagal spalvą, kaklelį, tempimą ir elastingumą.\n\nUžsisakyk Sempertex balionus iš {domain}.\n\n#balionurisimas #dviejupirstumazgas #sempertex #{tag} #balionai #balionumenininkas",
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

def facts_grid(items, cls="facts", num_size=44, lab_size=20):
    esc = G["esc"]
    def fs(n):
        L = len(n); return num_size if L <= 6 else (int(num_size * .72) if L <= 11 else int(num_size * .55))
    cells = "".join(f'<div class="fact"><b style="font-size:{fs(n)}px">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in items)
    return f'<div class="{cls}">{cells}</div>'

def duplet(keys, size=120, ink="#111"):
    """Twee ballonnen met de nekken tegen elkaar (duplet), met een knoopstip in het midden."""
    ratio = G["PHOTO_RATIO"]; h = int(size * ratio); w = int(size * 2.1); ch = int(h * 1.05)
    cx = w // 2; cy = ch - 6
    out = f'<div style="position:relative;width:{w}px;height:{ch}px">'
    for k, a in zip(keys[:2], (-30, 30)):
        out += f'<div style="position:absolute;left:{cx - size//2}px;top:{cy - h}px;transform-origin:50% 100%;transform:rotate({a}deg)">{_bl(k, size)}</div>'
    out += f'<div style="position:absolute;left:{cx-7}px;top:{cy-10}px;width:14px;height:14px;border-radius:50%;background:{ink}"></div>'
    return out + '</div>'

def quartet(keys, size=100, ink="#111"):
    """Vier ballonnen rond één knooppunt (2 duplets in elkaar gedraaid)."""
    ratio = G["PHOTO_RATIO"]; h = int(size * ratio); w = int(h * 2.05); ch = w
    cx = w // 2; cy = ch // 2
    out = f'<div style="position:relative;width:{w}px;height:{ch}px">'
    for k, a in zip(keys[:4], (-45, 45, 135, 225)):
        out += f'<div style="position:absolute;left:{cx - size//2}px;top:{cy - h}px;transform-origin:50% 100%;transform:rotate({a}deg)">{_bl(k, size)}</div>'
    out += f'<div style="position:absolute;left:{cx-8}px;top:{cy-8}px;width:16px;height:16px;border-radius:50%;background:{ink}"></div>'
    return out + '</div>'

def neck_stretch(key, size=110, ink="#111", lbl="2 - 3×"):
    """Eén ballon op zijn kant (nek naar rechts) met een gerekte nek als lijn en een maatpijl: 'rek de nek 2 tot 3×'."""
    esc = G["esc"]; ratio = G["PHOTO_RATIO"]; h = int(size * ratio); w = h + 170; ch = size + 40
    cx, cy = h / 2, ch / 2
    out = f'<div style="position:relative;width:{w}px;height:{ch}px">'
    out += f'<div style="position:absolute;left:{int(cx - size/2)}px;top:{int(cy - h/2)}px;transform:rotate(-90deg)">{_bl(key, size)}</div>'
    x0, y0 = h - 10, int(cy)
    out += (f'<svg viewBox="0 0 {w} {ch}" width="{w}" height="{ch}" style="position:absolute;left:0;top:0">'
            f'<path d="M{x0} {y0} q 60 -5 150 0" fill="none" stroke="{ink}" stroke-width="7" stroke-linecap="round" opacity=".85"/>'
            f'<path d="M{x0+15} {y0-34} h 128 m -12 -8 l 12 8 l -12 8" fill="none" stroke="{ink}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" opacity=".8"/></svg>')
    out += f'<div style="position:absolute;left:{x0+55}px;top:{y0-64}px;font-size:18px;font-weight:800;color:{ink};letter-spacing:.04em">{esc(lbl)}</div>'
    return out + '</div>'

def chips_row(items, ink="#111", bg="#fff", small=False):
    esc = G["esc"]; extra = "font-size:15px;padding:4px 10px;" if small else ""
    return '<div style="display:flex;justify-content:center;gap:6px;flex-wrap:wrap">' + "".join(f'<span class="tchip" style="{extra}border-color:{ink};color:{ink};background:{bg}">{esc(t)}</span>' for t in items) + '</div>'

def sore_visual(keys, c, ink="#111"):
    """'Pijnlijke vingers': drie ballonnen met de nek stijf omhoog, een rode '2 cm blaar'-stempel en een pleister."""
    esc = G["esc"]; w, h = 330, 380
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    pos = [(10, 20, 86, -12), (120, 0, 92, 6), (230, 24, 84, 14)]
    for i, (x, y, s, r) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg)">{_bl(keys[i % len(keys)], s)}</div>'
    # pleister
    out += (f'<div style="position:absolute;left:60px;top:200px;width:210px;height:54px;border-radius:27px;background:#f4d9c4;border:3px solid {ink};transform:rotate(-18deg);display:flex;align-items:center;justify-content:center">'
            f'<div style="width:70px;height:30px;border-radius:6px;background:#e8bfa4;opacity:.9"></div></div>')
    out += (f'<div style="position:absolute;left:30px;top:290px;transform:rotate(-6deg);background:#fff;color:#E03131;border:3px solid {ink};'
            f'border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">{esc(c["ouch_lbl"])}</div>')
    return out + '</div>'

def knot_visual(keys, c, ink="#111"):
    """'Tweevingerknoop': duplet + kwartet, chips en stempel '1 knoop'."""
    esc = G["esc"]
    return (f'<div style="position:relative;width:330px;height:380px">'
            f'<div style="position:absolute;left:0;top:0;transform:scale(.78);transform-origin:top left">{duplet(keys, 120, ink)}</div>'
            f'<div style="position:absolute;left:150px;top:30px;transform:scale(.62);transform-origin:top left">{quartet(keys, 100, ink)}</div>'
            f'<div style="position:absolute;left:-30px;right:-30px;top:240px">{chips_row(c["chips"][:2], ink, "#fff", True)}</div>'
            f'<div style="position:absolute;left:90px;top:300px;transform:rotate(-4deg);background:#fff;color:{ink};border:3px solid {ink};border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">✓ {esc(c["knot_lbl"])}</div></div>')

def two_builds(keys, c, ink="#111", body_size=21, lbl_size=24, gap=26, vh=250, sc=1.0):
    """Voorbeeldslide: links duplet, rechts kwartet, elk met titel + regel."""
    esc = G["esc"]
    vis = [f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc:.2f});transform-origin:bottom center">{duplet(keys, 120, ink)}</div></div>',
           f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc*.9:.2f});transform-origin:bottom center">{quartet(keys, 100, ink)}</div></div>']
    cols = ""
    for v, (t, body) in zip(vis, c["ex_items"]):
        cols += (f'<div style="flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;gap:10px">{v}'
                 f'<div style="font-size:{body_size}px;line-height:1.3;text-align:center"><b style="font-size:{lbl_size}px;display:block;margin-bottom:4px">{esc(t)}</b>{esc(body)}</div></div>')
    return f'<div style="display:flex;gap:{gap}px;align-items:flex-start;width:100%">{cols}</div>'

def habit_cards(c, cls="alts", title_size=24, body_size=18, font=None):
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
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:90px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
  <div class="pill" style="background:{b['c1']};color:{b['c1t']};right:60px;top:130px;transform:rotate({rot(b,-4)}deg)">{cursor_svg(b['c1'])}{esc(pills[0])}</div>
  <div class="pill" style="background:{b['c2']};color:{b['c2t']};right:90px;top:835px;transform:rotate({rot(b,3)}deg)">{cursor_svg(b['c2'])}{esc(pills[1])}</div>
  <div class="pill" style="background:{b['c3']};color:{b['c3t']};left:90px;top:880px;transform:rotate({rot(b,-2)}deg)">{cursor_svg(b['c3'])}{esc(pills[2])}</div>
  <div style="position:absolute;left:150px;top:960px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:310px;right:90px;top:1020px;font-size:29px;line-height:1.35">{esc(c['cover_sub'])}</div>
  {s1_footer(b, stx_h=84)}
</section>""")
    L = sum(len(s) for s in c["steps"]); sfs = 25 if L <= 330 else (23 if L <= 380 else 22)
    steps = "".join(f'<div class="step" style="font-size:{sfs}px"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:790px;height:470px">
    <h2 data-fit style="font-size:72px;max-height:380px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:740px;top:20px;transform:scale(.85);transform-origin:top left">{neck_stretch(b['hero'], 110, b['ink'])}</div>
  <div style="position:absolute;left:120px;top:600px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:270px;top:610px;width:740px;height:560px;padding:28px 38px">
    <div style="font-size:27px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:470px;padding:40px 48px">
    <h2 data-fit style="font-size:54px;max-height:140px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:18px;font-size:25px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:700px;height:410px">
    <div class="card" style="top:0;height:330px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:380px;padding:30px 34px">{facts_grid(c['rule1_facts'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:52px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div style="position:absolute;left:80px;right:80px;top:325px;font-size:25px;line-height:1.35" class="body">{esc(c['rule2_body'])}</div>
  <div style="position:absolute;left:70px;right:70px;top:415px">{habit_cards(c, "alts five", 26, 20, b["ui"])}</div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:660px;padding:36px 30px 30px">
    <h2 data-fit style="font-size:48px;margin-bottom:20px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    {two_builds(P, c, b['ink'], 21, 24, 26, 290, 1.15)}
  </div>
  <div class="box" style="left:70px;top:850px;width:940px;padding:20px 40px"><div class="body" style="font-size:22px">{esc(c['example_body'])}</div><div style="margin-top:12px">{chips_row(c['chips'], b['ink'], 'transparent', True)}</div></div>
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
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:64px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.1)">{knot_visual(P, c, '#111')}</div></div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px;font-size:25px"><b style="font-size:33px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:790px;width:930px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:290px;padding:20px 24px;box-sizing:border-box;background:#fff;color:#111;flex-direction:row;gap:40px;align-items:center;justify-content:center"><div style="transform:scale(.95)">{neck_stretch(P[0], 110, '#111')}</div><div style="transform:scale(.8)">{duplet(P[1:3] if len(P) > 2 else P, 120, '#111')}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:54px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:400px;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff">{facts_grid(c['rule1_facts'], 'facts onwhite')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:860px;font-size:24px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:52px;max-height:150px">{esc(c['rule2_title'])}</h2>
  <div class="body" style="position:absolute;left:70px;right:70px;top:330px;font-size:24px">{esc(c['rule2_body'])}</div>
  <div class="frame" style="left:70px;top:430px;width:940px;transform:rotate({rot(b,1)}deg)">
    <div class="ph" style="height:auto;padding:24px 28px;box-sizing:border-box;align-items:stretch;background:#fff;color:#111">{habit_cards(c, 'alts onwhite', 22, 16)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:54px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:auto;padding:24px 24px;box-sizing:border-box;align-items:flex-start;background:#fff;color:#111">{two_builds(P, c, '#111', 20, 23, 20, 260, 1.05)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:980px;font-size:22px">{esc(c['example_body'])}</div>
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
    loud = P + PAL_SETS[(b["pal_idx"] + 5) % len(PAL_SETS)]
    S = []
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:50px;right:50px;top:60px;max-height:400px;font-size:84px;text-align:center;line-height:1.08">{hl(c['s3_cover_a'])} {esc(c['s3_cover_b'])} {esc(c['s3_cover_c'])}<br><span class="hl">{esc(c['s3_cover_d'])}</span></h1>
  <div class="vsmark" style="top:520px">VS</div>
  <div class="lblw" style="left:110px;top:500px;transform:rotate({rot(b,-4)}deg)">{esc(c['s3_left'])}<br><span class="meta">● {esc(c['s3_left_meta'])}</span></div>
  <div class="lbld" style="right:110px;top:500px;transform:rotate({rot(b,4)}deg)">{esc(c['s3_right'])}<br><span class="meta" style="background:rgba(255,255,255,.18)">● {esc(c['s3_right_meta'])}</span></div>
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{sore_visual(loud, c, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{knot_visual(P, c, b['ink'])}</div>
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
    vis1 = f'<div style="width:100%">{facts_grid(c["rule1_facts"], "facts s3facts", 34, 17)}</div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="width:100%">{habit_cards(c, "alts s3alts", 17, 13)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['s3_example_topic']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:640px;padding:36px 24px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;gap:20px">
    {two_builds(P, c, '#111', 22, 25, 18, 330, 1.3)}
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
.facts{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.facts .fact{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:3px solid #111;border-radius:18px;padding:16px 12px;gap:6px;line-height:1.15}
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
