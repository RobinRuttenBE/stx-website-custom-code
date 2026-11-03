# -*- coding: utf-8 -*-
"""Topic: 'How do you make a flower bouquet of balloons? Step-by-step tutorial' (ballonbloemen).
(sempertexeurope.com/en_GB/blog/how-to-make-balloon-flowers).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=flowers.
Uit de blog: bloemen uit modelleerballonnen 260; per bloem 1 × 260 voor de bloem en 1 voor de steel, 1 extra voor
de strik; boeket van 3 = ca. 8 × 260 (3 bloemen, 3 stelen, 1 strik, 1 leeg om te bundelen), +2 per extra bloem.
3 regels: niet vol opblazen (lange lege staart, elke draai duwt lucht terug), bubbels klein en gelijk (meten met je
vingers, lussen 2 à 3 vingers), elke draai 2 à 3 keer in dezelfde richting. Tulp: eerste bubbel vouwen en knoop
erdoor trekken, 5 blaadjes, overschot naar binnen rollen, steel = Eucalyptus 260 bijna vol met lusvoet. Lavendel:
bubbel + 2 pinch twists, herhalen. Zesbladige bloem: 6 lussen van 2 à 3 vingers, vastdraaien, blaadjes om en om
hoog en laag, hart = kleine bubbel op een nieuwe 260 die de steel wordt. Boeket: stelen bundelen met een lege 260,
hoogtes aanpassen, stelen als laatste knippen. Strik: Reflex Gold 260 vol en iets leeglaten, dubbele pinch twist in
het midden, 2 lussen eromheen, gelijke linten. Kleuren tutorial: Pastel Dusk Rose (tulp), Pastel Dusk Lavender,
Pastel Dusk Blue, Eucalyptus (stelen), Reflex Gold (strik). FAQ: 260 standaard, 160 fijner, 360 groter; ruimte tekort
= te vol of lussen te groot; op een boog: bevestigingspunten, ballonnek van boog naar achterkant bloem, onregelmatig.
Gereedschap: handpomp en snijder. CTA blog: Audrey maakt de 3 bloemen en de strik op YouTube."""

G = {}
def setup(g): G.update(g)
NB = " "
STEM = "#8FA68E"

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["8 × 260…", "3 bloemen…", "Lange lege staart…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Ballonbloemen…",
    "steps_title": "Ballonbloemen uit 260's: 3 regels voor de eerste draai", "steps_lead": "Voor je begint:",
    "steps": ["Blaas nooit vol op: laat een lange lege staart, want elke draai duwt lucht terug in de ballon", "Hou bubbels klein en gelijk, meet ze met je vingers. Lussen: 2 à 3 vingers", "Draai elke twist 2 à 3 keer, altijd in dezelfde richting, anders komt hij los", "Per bloem 2 × 260 (bloem en steel). Boeket van 3: zo'n 8 × 260, met strik en een lege om te bundelen", "Gereedschap: een handpomp en een snijder. Meer niet"],
    "steps_label": "De regels",
    "rule1_label": "De 3 bloemen", "rule1_title": "Tulp, lavendel en zesbladige bloem: elk uit 1 × 260",
    "rule1_body": "Tulp: eerste bubbel vouwen en de knoop erdoor trekken, 2 gelijke blaadjes, dan de rest, overschot naar binnen rollen. Lavendel: een bubbel en 2 pinch twists, herhalen over de hele lengte. Zesbladige bloem: 6 lussen van 2 à 3 vingers, vastdraaien, blaadjes om en om hoog en laag tot hij rond is; het hart is een kleine bubbel op een nieuwe 260, de rest wordt de steel. Een pinch twist is een kleinere bubbel die je van je af trekt en 2 à 3 keer om zijn eigen as draait, zodat hij strak tegen de ballon ligt.",
    "rule1_facts": [["5", "blaadjes in de tulp, uit 1 × 260"], ["2", "pinch twists na elke bubbel van de lavendel"], ["6", "lussen van 2 à 3 vingers in de zesbladige bloem"], ["8", "260's voor een boeket van 3, +2 per extra bloem"]],
    "rule2_label": "Boeket", "rule2_title": "Strik, boeket en de 3 vragen die iedereen stelt",
    "rule2_body": "De bloemen zijn de helft van het werk. De afwerking maakt er een boeket van:",
    "alts": [["Bundel de stelen", "wikkel een lege 260 losjes om de 3 stelen, zet de hoogtes goed, knip de stelen als laatste."], ["De strik", "Reflex Gold 260 vol opblazen en iets laten leeglopen, dubbele pinch twist in het midden, 2 lussen eromheen, gelijke linten."], ["Ballon te kort op het einde?", "te vol opgeblazen of lussen te groot. Laat een ruime staart en hou lussen op 2 à 3 vingers."], ["Op een boog", "maak bevestigingspunten, knoop een ballonnek van de boog naar de achterkant van elke bloem, verdeel ze onregelmatig."], ["Andere maten", "260 is de standaard. 160 voor fijnere bloemen, 360 voor grotere."]],
    "example_label": "Voorbeeld", "example_title": "Eén boeket, twee paletten",
    "ex_items": [["Zoals in de tutorial", "tulp in Pastel Dusk Rose 110, lavendel in Pastel Dusk Lavender, zesbladige bloem in Pastel Dusk Blue. Stelen in Eucalyptus 027, strik in Reflex Gold 970."], ["Uit het rek van je distri", "kies 3 kleuren uit de 260-lijn, bijvoorbeeld {p0}, {p1} en {p2}, hou Eucalyptus 027 voor de stelen en {p3} voor de strik."]],
    "example_body": "Alles in 260. Voor fijnere bloemen neem je 160, voor grotere 360. Reken 8 × 260 voor een boeket van 3 en 2 extra per bloem erbij.",
    "client_label": "Collega vraagt", "client_title": "Wat je antwoordt als een collega vraagt",
    "client_answers": [
        "De 260 is de standaard voor alles: bloem, steel en strik. Wil je fijnere bloemen, neem dan een 160. Grotere bloemen voor een boog of een groot stuk: een 360. Leer het eerst op de 260, daar past de hele tutorial op.",
        "Zo'n 8: 3 voor de bloemen, 3 voor de stelen, 1 voor de strik en 1 lege om de stelen te bundelen. Elke extra bloem kost er 2 meer, één voor de bloem en één voor de steel.",
        "Ja. Maak bevestigingspunten op de boog, knoop een ballonnek van de boog naar het knooppunt aan de achterkant van elke bloem, en verdeel ze onregelmatig. Dat oogt natuurlijker dan een strak patroon.",
    ],
    "avoid_lead": "Je eerste boeket, in 5 stappen:",
    "steps5": ["3 × 260 opblazen voor de bloemen, lange lege staart", "Tulp: eerste bubbel vouwen, knoop erdoor, 5 blaadjes", "Lavendel: bubbel + 2 pinch twists, herhalen over de hele lengte", "Zesbladige bloem: 6 lussen van 2 à 3 vingers, hart op een nieuwe 260", "Bundelen met een lege 260, strik in Reflex Gold, stelen als laatste knippen"],
    "client_body": "Liever kijken dan lezen? Audrey maakt deze 3 bloemen en de strik op het YouTube-kanaal van Sempertex Europe.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex bloemen:", "s3_cover_b": "vol opgeblazen", "s3_cover_c": "vs.", "s3_cover_d": "lange staart",
    "s3_left": "VOL OPGEBLAZEN", "s3_right": "LANGE STAART", "s3_left_meta": "1 draai, grote lussen", "s3_right_meta": "3 draaien, 2-3 vingers",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Vol opblazen", "Grote lussen", "1 draai"], "s3_new_tags": ["Lange staart", "2 à 3 vingers", "3 draaien", "Zelfde richting"],
    "s3_new_quote": "“Lange staart, kleine bubbels, drie keer draaien. Drie bloemen uit acht 260's, en de laatste lus past nog.”", "s3_new_badge": "8 × 260, 3 bloemen",
    "s3_changed_bottom": "Zelfde 260's, zelfde handen.\nNu blijft elke draai zitten.",
    "s3_topic_lbl": "WAAROM", "s3_rule1_topic": "3 bloemen", "s3_rule1_old": "Eén bloem kennen is genoeg",
    "s3_rule1_quote": "“Tulp, lavendel en zesbladige bloem: 3 technieken, elk uit 1 × 260, samen 1 boeket.”",
    "s3_rule2_topic": "Boeket", "s3_rule2_old": "Stelen knippen en klaar",
    "s3_rule2_quote": "“Bundelen met een lege 260, strik in Reflex Gold, stelen als laatste knippen.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_topic": "Twee paletten", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 en Reflex Gold 970 zoals in de tutorial, of {p0}, {p1} en {p2} uit het rek.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "Eerste boeket",
    "s3_client_quote": "“Acht 260's, een handpomp en een snijder. Meer heeft een boeket niet nodig.”",
    "s3_cta_kicker": "8 × 260, 3 bloemen, 1 boeket",
    "tulip_lbl": "tulp", "lav_lbl": "lavendel", "six_lbl": "zesbladig", "bow_lbl": "strik", "noroom_lbl": "te kort", "bouquet_lbl": "3 bloemen", "chips": ["8 × 260", "2 à 3 vingers", "3× draaien"],
},
"en": {
    "cover_pills": ["8 × 260…", "3 flowers…", "Long empty tail…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Balloon flowers…",
    "steps_title": "Balloon flowers from 260s: 3 rules before the first twist", "steps_lead": "Before you start:",
    "steps": ["Never inflate fully: leave a long empty tail, because every twist pushes air back into the balloon", "Keep bubbles small and even, measure them with your fingers. Loops: 2 to 3 fingers", "Twist every twist 2 or 3 times, always in the same direction, or it loosens", "Per flower 2 × 260 (flower and stem). Bouquet of 3: about 8 × 260, with the bow and a deflated one to bundle", "Tools: a hand pump and a cutter. Nothing else"],
    "steps_label": "The rules",
    "rule1_label": "The 3 flowers", "rule1_title": "Tulip, lavender and six-petal flower: each from 1 × 260",
    "rule1_body": "Tulip: fold the first bubble and pull the knot through, 2 equal petals, then the rest, roll the excess inward. Lavender: one bubble and 2 pinch twists, repeated along the whole length. Six-petal flower: 6 loops of 2 to 3 fingers, lock with a twist, open the petals alternating high and low until it's round; the heart is a small bubble on a new 260, the rest becomes the stem. A pinch twist is a smaller bubble you pull away from you and twist 2 or 3 times around its own axis, so it sits tight against the balloon.",
    "rule1_facts": [["5", "petals in the tulip, from 1 × 260"], ["2", "pinch twists after every bubble of the lavender"], ["6", "loops of 2 to 3 fingers in the six-petal flower"], ["8", "260s for a bouquet of 3, +2 per extra flower"]],
    "rule2_label": "Bouquet", "rule2_title": "Bow, bouquet and the 3 questions everyone asks",
    "rule2_body": "The flowers are half the work. The finish turns them into a bouquet:",
    "alts": [["Bundle the stems", "wrap a deflated 260 loosely around the 3 stems, set the heights, trim the stems last."], ["The bow", "Reflex Gold 260 inflated fully then let a little air out, double pinch twist in the centre, 2 loops around it, equal tails."], ["Running out of balloon?", "inflated too far or loops too big. Leave a generous tail and keep loops at 2 to 3 fingers."], ["On an arch", "make attachment points, tie a balloon neck from the arch to the back of each flower, spread them irregularly."], ["Other sizes", "260 is the standard. 160 for finer flowers, 360 for bigger ones."]],
    "example_label": "Example", "example_title": "One bouquet, two palettes",
    "ex_items": [["As in the tutorial", "tulip in Pastel Dusk Rose 110, lavender in Pastel Dusk Lavender, six-petal flower in Pastel Dusk Blue. Stems in Eucalyptus 027, bow in Reflex Gold 970."], ["From your distributor's shelf", "pick 3 colours from the 260 range, for instance {p0}, {p1} and {p2}, keep Eucalyptus 027 for the stems and {p3} for the bow."]],
    "example_body": "Everything in 260. For finer flowers take 160, for bigger ones 360. Count 8 × 260 for a bouquet of 3 and 2 more per extra flower.",
    "client_label": "Colleague asks", "client_title": "What you answer when a colleague asks",
    "client_answers": [
        "The 260 is the standard for everything: flower, stem and bow. For finer flowers take a 160. Bigger flowers for an arch or a large piece: a 360. Learn it on the 260 first, the whole tutorial fits on it.",
        "About 8: 3 for the flowers, 3 for the stems, 1 for the bow and 1 deflated to bundle the stems. Every extra flower costs 2 more, one for the flower and one for the stem.",
        "Yes. Make attachment points on the arch, tie a balloon neck from the arch to the connection point at the back of each flower, and spread them irregularly. That looks more natural than a tight pattern.",
    ],
    "avoid_lead": "Your first bouquet, in 5 steps:",
    "steps5": ["Inflate 3 × 260 for the flowers, long empty tail", "Tulip: fold the first bubble, pull the knot through, 5 petals", "Lavender: bubble + 2 pinch twists, repeat along the whole length", "Six-petal flower: 6 loops of 2 to 3 fingers, heart on a new 260", "Bundle with a deflated 260, bow in Reflex Gold, trim the stems last"],
    "client_body": "Rather watch than read? Audrey makes these 3 flowers and the bow on the Sempertex Europe YouTube channel.",
    "cta_label": "Order",
    "s3_cover_a": "Sempertex flowers:", "s3_cover_b": "fully inflated", "s3_cover_c": "vs.", "s3_cover_d": "long tail",
    "s3_left": "FULLY INFLATED", "s3_right": "LONG TAIL", "s3_left_meta": "1 twist, big loops", "s3_right_meta": "3 twists, 2-3 fingers",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Inflate fully", "Big loops", "1 twist"], "s3_new_tags": ["Long tail", "2 to 3 fingers", "3 twists", "Same direction"],
    "s3_new_quote": "“Long tail, small bubbles, twist three times. Three flowers from eight 260s, and the last loop still fits.”", "s3_new_badge": "8 × 260, 3 flowers",
    "s3_changed_bottom": "Same 260s, same hands.\nNow every twist stays put.",
    "s3_topic_lbl": "WHY", "s3_rule1_topic": "3 flowers", "s3_rule1_old": "Knowing one flower is enough",
    "s3_rule1_quote": "“Tulip, lavender and six-petal flower: 3 techniques, each from 1 × 260, together 1 bouquet.”",
    "s3_rule2_topic": "Bouquet", "s3_rule2_old": "Cut the stems and done",
    "s3_rule2_quote": "“Bundle with a deflated 260, bow in Reflex Gold, trim the stems last.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_topic": "Two palettes", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 and Reflex Gold 970 as in the tutorial, or {p0}, {p1} and {p2} from the shelf.”",
    "s3_client_lbl": "COLLEAGUE", "s3_client_topic": "First bouquet",
    "s3_client_quote": "“Eight 260s, a hand pump and a cutter. A bouquet needs nothing more.”",
    "s3_cta_kicker": "8 × 260, 3 flowers, 1 bouquet",
    "tulip_lbl": "tulip", "lav_lbl": "lavender", "six_lbl": "six-petal", "bow_lbl": "bow", "noroom_lbl": "no room", "bouquet_lbl": "3 flowers", "chips": ["8 × 260", "2 to 3 fingers", "3× twist"],
},
"de": {
    "cover_pills": ["8 × 260…", "3 Blumen…", "Langer leerer Schwanz…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Ballonblumen…",
    "steps_title": "Ballonblumen aus 260ern: 3 Regeln vor dem ersten Twist", "steps_lead": "Bevor du anfängst:",
    "steps": ["Nie ganz aufblasen: einen langen leeren Schwanz lassen, denn jeder Twist drückt Luft zurück in den Ballon", "Blasen klein und gleichmäßig halten, mit den Fingern messen. Schlaufen: 2 bis 3 Finger", "Jeden Twist 2- bis 3-mal drehen, immer in dieselbe Richtung, sonst löst er sich", "Pro Blume 2 × 260 (Blume und Stiel). Strauß aus 3: etwa 8 × 260, mit Schleife und einem leeren zum Bündeln", "Werkzeug: eine Handpumpe und ein Cutter. Mehr nicht"],
    "steps_label": "Die Regeln",
    "rule1_label": "Die 3 Blumen", "rule1_title": "Tulpe, Lavendel und sechsblättrige Blume: jede aus 1 × 260",
    "rule1_body": "Tulpe: erste Blase falten und den Knoten durchziehen, 2 gleiche Blätter, dann der Rest, Überschuss nach innen rollen. Lavendel: eine Blase und 2 Pinch Twists, über die ganze Länge wiederholt. Sechsblättrige Blume: 6 Schlaufen von 2 bis 3 Fingern, mit einem Twist sichern, Blätter abwechselnd hoch und tief öffnen, bis sie rund ist; das Herz ist eine kleine Blase auf einem neuen 260, der Rest wird der Stiel. Ein Pinch Twist ist eine kleinere Blase, die du von dir wegziehst und 2- bis 3-mal um die eigene Achse drehst, damit sie eng am Ballon anliegt.",
    "rule1_facts": [["5", "Blätter in der Tulpe, aus 1 × 260"], ["2", "Pinch Twists nach jeder Blase beim Lavendel"], ["6", "Schlaufen von 2 bis 3 Fingern in der sechsblättrigen Blume"], ["8", "260er für einen Strauß aus 3, +2 pro extra Blume"]],
    "rule2_label": "Strauß", "rule2_title": "Schleife, Strauß und die 3 Fragen, die jeder stellt",
    "rule2_body": "Die Blumen sind die halbe Arbeit. Die Fertigstellung macht einen Strauß daraus:",
    "alts": [["Stiele bündeln", "einen leeren 260 locker um die 3 Stiele wickeln, Höhen einstellen, Stiele zuletzt schneiden."], ["Die Schleife", "Reflex Gold 260 ganz aufblasen und etwas Luft ablassen, doppelter Pinch Twist in der Mitte, 2 Schlaufen drumherum, gleiche Bänder."], ["Ballon zu kurz am Ende?", "zu weit aufgeblasen oder Schlaufen zu groß. Großzügigen Schwanz lassen und Schlaufen bei 2 bis 3 Fingern halten."], ["Am Bogen", "Befestigungspunkte machen, einen Ballonhals vom Bogen zur Rückseite jeder Blume knoten, unregelmäßig verteilen."], ["Andere Größen", "260 ist der Standard. 160 für feinere Blumen, 360 für größere."]],
    "example_label": "Beispiel", "example_title": "Ein Strauß, zwei Paletten",
    "ex_items": [["Wie im Tutorial", "Tulpe in Pastel Dusk Rose 110, Lavendel in Pastel Dusk Lavender, sechsblättrige Blume in Pastel Dusk Blue. Stiele in Eucalyptus 027, Schleife in Reflex Gold 970."], ["Aus dem Regal deines Händlers", "wähl 3 Farben aus der 260er-Linie, zum Beispiel {p0}, {p1} und {p2}, behalte Eucalyptus 027 für die Stiele und {p3} für die Schleife."]],
    "example_body": "Alles in 260. Für feinere Blumen nimm 160, für größere 360. Rechne 8 × 260 für einen Strauß aus 3 und 2 mehr pro extra Blume.",
    "client_label": "Kollegin fragt", "client_title": "Was du antwortest, wenn eine Kollegin fragt",
    "client_answers": [
        "Der 260 ist der Standard für alles: Blume, Stiel und Schleife. Für feinere Blumen nimm einen 160. Größere Blumen für einen Bogen oder ein großes Stück: einen 360. Lern es zuerst auf dem 260, das ganze Tutorial passt darauf.",
        "Etwa 8: 3 für die Blumen, 3 für die Stiele, 1 für die Schleife und 1 leeren zum Bündeln der Stiele. Jede extra Blume kostet 2 mehr, einen für die Blume und einen für den Stiel.",
        "Ja. Mach Befestigungspunkte am Bogen, knote einen Ballonhals vom Bogen zum Verbindungspunkt auf der Rückseite jeder Blume und verteile sie unregelmäßig. Das wirkt natürlicher als ein strenges Muster.",
    ],
    "avoid_lead": "Dein erster Strauß, in 5 Schritten:",
    "steps5": ["3 × 260 für die Blumen aufblasen, langer leerer Schwanz", "Tulpe: erste Blase falten, Knoten durchziehen, 5 Blätter", "Lavendel: Blase + 2 Pinch Twists, über die ganze Länge wiederholen", "Sechsblättrige Blume: 6 Schlaufen von 2 bis 3 Fingern, Herz auf einem neuen 260", "Mit einem leeren 260 bündeln, Schleife in Reflex Gold, Stiele zuletzt schneiden"],
    "client_body": "Lieber schauen als lesen? Audrey macht diese 3 Blumen und die Schleife auf dem YouTube-Kanal von Sempertex Europe.",
    "cta_label": "Bestellen",
    "s3_cover_a": "Sempertex Blumen:", "s3_cover_b": "ganz aufgeblasen", "s3_cover_c": "vs.", "s3_cover_d": "langer Schwanz",
    "s3_left": "GANZ AUFGEBLASEN", "s3_right": "LANGER SCHWANZ", "s3_left_meta": "1 Twist, große Loops", "s3_right_meta": "3 Twists, 2-3 Finger",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Ganz aufblasen", "Große Schlaufen", "1 Twist"], "s3_new_tags": ["Langer Schwanz", "2 bis 3 Finger", "3 Twists", "Gleiche Richtung"],
    "s3_new_quote": "“Langer Schwanz, kleine Blasen, dreimal drehen. Drei Blumen aus acht 260ern, und die letzte Schlaufe passt noch.”", "s3_new_badge": "8 × 260, 3 Blumen",
    "s3_changed_bottom": "Dieselben 260er, dieselben Hände.\nJetzt bleibt jeder Twist sitzen.",
    "s3_topic_lbl": "WARUM", "s3_rule1_topic": "3 Blumen", "s3_rule1_old": "Eine Blume zu können reicht",
    "s3_rule1_quote": "“Tulpe, Lavendel und sechsblättrige Blume: 3 Techniken, jede aus 1 × 260, zusammen 1 Strauß.”",
    "s3_rule2_topic": "Strauß", "s3_rule2_old": "Stiele schneiden und fertig",
    "s3_rule2_quote": "“Mit einem leeren 260 bündeln, Schleife in Reflex Gold, Stiele zuletzt schneiden.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_topic": "Zwei Paletten", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 und Reflex Gold 970 wie im Tutorial, oder {p0}, {p1} und {p2} aus dem Regal.”",
    "s3_client_lbl": "KOLLEGIN", "s3_client_topic": "Erster Strauß",
    "s3_client_quote": "“Acht 260er, eine Handpumpe und ein Cutter. Mehr braucht ein Strauß nicht.”",
    "s3_cta_kicker": "8 × 260, 3 Blumen, 1 Strauß",
    "tulip_lbl": "Tulpe", "lav_lbl": "Lavendel", "six_lbl": "sechsblättrig", "bow_lbl": "Schleife", "noroom_lbl": "zu kurz", "bouquet_lbl": "3 Blumen", "chips": ["8 × 260", "2 bis 3 Finger", "3× drehen"],
},
"fr": {
    "cover_pills": ["8 × 260…", "3 fleurs…", "Longue queue vide…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Fleurs en ballons…",
    "steps_title": "Fleurs en ballons avec des 260 : 3 règles avant la première torsion", "steps_lead": "Avant de commencer :",
    "steps": ["Ne gonfle jamais à fond : laisse une longue queue vide, car chaque torsion renvoie de l'air dans le ballon", "Garde des bulles petites et régulières, mesure-les avec tes doigts. Boucles : 2 à 3 doigts", "Tords chaque torsion 2 ou 3 fois, toujours dans le même sens, sinon elle se défait", "Par fleur 2 × 260 (fleur et tige). Bouquet de 3 : environ 8 × 260, avec le nœud et un ballon dégonflé pour lier", "Outils : une pompe à main et un cutter. Rien d'autre"],
    "steps_label": "Les règles",
    "rule1_label": "Les 3 fleurs", "rule1_title": "Tulipe, lavande et fleur à six pétales : chacune avec 1 × 260",
    "rule1_body": "Tulipe : plie la première bulle et passe le nœud à travers, 2 pétales égaux, puis le reste, roule le surplus vers l'intérieur. Lavande : une bulle et 2 pinch twists, répétés sur toute la longueur. Fleur à six pétales : 6 boucles de 2 à 3 doigts, verrouille d'une torsion, ouvre les pétales en alternant haut et bas jusqu'à ce qu'elle soit ronde ; le cœur est une petite bulle sur un nouveau 260, le reste devient la tige. Un pinch twist est une bulle plus petite que tu tires vers toi et tords 2 ou 3 fois sur son axe, pour qu'elle reste plaquée contre le ballon.",
    "rule1_facts": [["5", "pétales dans la tulipe, avec 1 × 260"], ["2", "pinch twists après chaque bulle de la lavande"], ["6", "boucles de 2 à 3 doigts dans la fleur à six pétales"], ["8", "260 pour un bouquet de 3, +2 par fleur en plus"]],
    "rule2_label": "Bouquet", "rule2_title": "Nœud, bouquet et les 3 questions que tout le monde pose",
    "rule2_body": "Les fleurs, c'est la moitié du travail. La finition en fait un bouquet :",
    "alts": [["Lie les tiges", "enroule un 260 dégonflé sans serrer autour des 3 tiges, règle les hauteurs, coupe les tiges en dernier."], ["Le nœud", "Reflex Gold 260 gonflé à fond puis un peu dégonflé, double pinch twist au centre, 2 boucles autour, rubans égaux."], ["Plus de ballon à la fin ?", "trop gonflé ou boucles trop grandes. Laisse une queue généreuse et garde les boucles à 2 ou 3 doigts."], ["Sur une arche", "crée des points d'attache, noue un col de ballon de l'arche à l'arrière de chaque fleur, répartis-les irrégulièrement."], ["Autres tailles", "le 260 est la base. 160 pour des fleurs plus fines, 360 pour des plus grandes."]],
    "example_label": "Exemple", "example_title": "Un bouquet, deux palettes",
    "ex_items": [["Comme dans le tutoriel", "tulipe en Pastel Dusk Rose 110, lavande en Pastel Dusk Lavender, fleur à six pétales en Pastel Dusk Blue. Tiges en Eucalyptus 027, nœud en Reflex Gold 970."], ["Depuis l'étagère de ton distributeur", "choisis 3 couleurs dans la gamme 260, par exemple {p0}, {p1} et {p2}, garde Eucalyptus 027 pour les tiges et {p3} pour le nœud."]],
    "example_body": "Tout en 260. Pour des fleurs plus fines, prends du 160 ; pour des plus grandes, du 360. Compte 8 × 260 pour un bouquet de 3 et 2 de plus par fleur supplémentaire.",
    "client_label": "Un collègue demande", "client_title": "Ce que tu réponds quand un collègue demande",
    "client_answers": [
        "Le 260 est la base pour tout : fleur, tige et nœud. Pour des fleurs plus fines, prends un 160. Des fleurs plus grandes pour une arche ou une grande pièce : un 360. Apprends d'abord sur le 260, tout le tutoriel tient dessus.",
        "Environ 8 : 3 pour les fleurs, 3 pour les tiges, 1 pour le nœud et 1 dégonflé pour lier les tiges. Chaque fleur en plus en coûte 2 de plus, une pour la fleur et une pour la tige.",
        "Oui. Crée des points d'attache sur l'arche, noue un col de ballon de l'arche au point de jonction à l'arrière de chaque fleur, et répartis-les irrégulièrement. C'est plus naturel qu'un motif régulier.",
    ],
    "avoid_lead": "Ton premier bouquet, en 5 étapes :",
    "steps5": ["Gonfle 3 × 260 pour les fleurs, longue queue vide", "Tulipe : plie la première bulle, passe le nœud, 5 pétales", "Lavande : bulle + 2 pinch twists, répète sur toute la longueur", "Fleur à six pétales : 6 boucles de 2 à 3 doigts, cœur sur un nouveau 260", "Lie avec un 260 dégonflé, nœud en Reflex Gold, coupe les tiges en dernier"],
    "client_body": "Tu préfères regarder que lire ? Audrey fait ces 3 fleurs et le nœud sur la chaîne YouTube de Sempertex Europe.",
    "cta_label": "Commander",
    "s3_cover_a": "Fleurs Sempertex :", "s3_cover_b": "gonflé à fond", "s3_cover_c": "vs.", "s3_cover_d": "longue queue",
    "s3_left": "GONFLÉ À FOND", "s3_right": "LONGUE QUEUE", "s3_left_meta": "1 tour, boucles larges", "s3_right_meta": "3 tours, 2 à 3 doigts",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Gonfler à fond", "Grandes boucles", "1 torsion"], "s3_new_tags": ["Longue queue", "2 à 3 doigts", "3 torsions", "Même sens"],
    "s3_new_quote": "“Longue queue, petites bulles, trois torsions. Trois fleurs avec huit 260, et la dernière boucle passe encore.”", "s3_new_badge": "8 × 260, 3 fleurs",
    "s3_changed_bottom": "Mêmes 260, mêmes mains.\nMaintenant chaque torsion tient.",
    "s3_topic_lbl": "POURQUOI", "s3_rule1_topic": "3 fleurs", "s3_rule1_old": "Connaître une fleur suffit",
    "s3_rule1_quote": "“Tulipe, lavande et fleur à six pétales : 3 techniques, chacune avec 1 × 260, ensemble 1 bouquet.”",
    "s3_rule2_topic": "Bouquet", "s3_rule2_old": "Couper les tiges et c'est fini",
    "s3_rule2_quote": "“Lier avec un 260 dégonflé, nœud en Reflex Gold, couper les tiges en dernier.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_topic": "Deux palettes", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 et Reflex Gold 970 comme dans le tutoriel, ou {p0}, {p1} et {p2} de l'étagère.”",
    "s3_client_lbl": "COLLÈGUE", "s3_client_topic": "Premier bouquet",
    "s3_client_quote": "“Huit 260, une pompe à main et un cutter. Un bouquet n'a besoin de rien d'autre.”",
    "s3_cta_kicker": "8 × 260, 3 fleurs, 1 bouquet",
    "tulip_lbl": "tulipe", "lav_lbl": "lavande", "six_lbl": "six pétales", "bow_lbl": "nœud", "noroom_lbl": "trop court", "bouquet_lbl": "3 fleurs", "chips": ["8 × 260", "2 à 3 doigts", "3× tordre"],
},
"it": {
    "cover_pills": ["8 × 260…", "3 fiori…", "Coda vuota lunga…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Fiori di palloncini…",
    "steps_title": "Fiori di palloncini con i 260: 3 regole prima del primo twist", "steps_lead": "Prima di iniziare:",
    "steps": ["Non gonfiare mai del tutto: lascia una coda vuota lunga, perché ogni twist spinge aria indietro nel palloncino", "Tieni le bolle piccole e uguali, misurale con le dita. Anelli: 2 o 3 dita", "Gira ogni twist 2 o 3 volte, sempre nella stessa direzione, altrimenti si allenta", "Per fiore 2 × 260 (fiore e stelo). Bouquet da 3: circa 8 × 260, con il fiocco e uno sgonfio per legare", "Attrezzi: una pompa a mano e un cutter. Nient'altro"],
    "steps_label": "Le regole",
    "rule1_label": "I 3 fiori", "rule1_title": "Tulipano, lavanda e fiore a sei petali: ognuno da 1 × 260",
    "rule1_body": "Tulipano: piega la prima bolla e fai passare il nodo, 2 petali uguali, poi il resto, arrotola l'eccesso verso l'interno. Lavanda: una bolla e 2 pinch twist, ripetuti per tutta la lunghezza. Fiore a sei petali: 6 anelli di 2 o 3 dita, blocca con un twist, apri i petali alternando alto e basso finché è rotondo; il cuore è una bolla piccola su un nuovo 260, il resto diventa lo stelo. Un pinch twist è una bolla più piccola che tiri verso di te e giri 2 o 3 volte sul suo asse, così resta stretta contro il palloncino.",
    "rule1_facts": [["5", "petali nel tulipano, da 1 × 260"], ["2", "pinch twist dopo ogni bolla della lavanda"], ["6", "anelli di 2 o 3 dita nel fiore a sei petali"], ["8", "260 per un bouquet da 3, +2 per ogni fiore in più"]],
    "rule2_label": "Bouquet", "rule2_title": "Fiocco, bouquet e le 3 domande che fanno tutti",
    "rule2_body": "I fiori sono metà del lavoro. La finitura li trasforma in un bouquet:",
    "alts": [["Lega gli steli", "avvolgi un 260 sgonfio senza stringere attorno ai 3 steli, regola le altezze, taglia gli steli per ultimi."], ["Il fiocco", "Reflex Gold 260 gonfiato del tutto e poi un po' sgonfiato, doppio pinch twist al centro, 2 anelli attorno, nastri uguali."], ["Palloncino finito prima della fine?", "gonfiato troppo o anelli troppo grandi. Lascia una coda abbondante e tieni gli anelli a 2 o 3 dita."], ["Su un arco", "crea punti di fissaggio, annoda un collo di palloncino dall'arco al retro di ogni fiore, distribuiscili in modo irregolare."], ["Altre misure", "il 260 è lo standard. 160 per fiori più fini, 360 per fiori più grandi."]],
    "example_label": "Esempio", "example_title": "Un bouquet, due palette",
    "ex_items": [["Come nel tutorial", "tulipano in Pastel Dusk Rose 110, lavanda in Pastel Dusk Lavender, fiore a sei petali in Pastel Dusk Blue. Steli in Eucalyptus 027, fiocco in Reflex Gold 970."], ["Dallo scaffale del tuo distributore", "scegli 3 colori dalla linea 260, per esempio {p0}, {p1} e {p2}, tieni Eucalyptus 027 per gli steli e {p3} per il fiocco."]],
    "example_body": "Tutto in 260. Per fiori più fini prendi il 160, per più grandi il 360. Conta 8 × 260 per un bouquet da 3 e 2 in più per ogni fiore aggiunto.",
    "client_label": "Un collega chiede", "client_title": "Cosa rispondi quando un collega chiede",
    "client_answers": [
        "Il 260 è lo standard per tutto: fiore, stelo e fiocco. Per fiori più fini prendi un 160. Fiori più grandi per un arco o un pezzo grande: un 360. Imparalo prima sul 260, tutto il tutorial ci sta sopra.",
        "Circa 8: 3 per i fiori, 3 per gli steli, 1 per il fiocco e 1 sgonfio per legare gli steli. Ogni fiore in più ne costa 2, uno per il fiore e uno per lo stelo.",
        "Sì. Crea punti di fissaggio sull'arco, annoda un collo di palloncino dall'arco al punto di giunzione sul retro di ogni fiore, e distribuiscili in modo irregolare. Sembra più naturale di uno schema rigido.",
    ],
    "avoid_lead": "Il tuo primo bouquet, in 5 passi:",
    "steps5": ["Gonfia 3 × 260 per i fiori, coda vuota lunga", "Tulipano: piega la prima bolla, fai passare il nodo, 5 petali", "Lavanda: bolla + 2 pinch twist, ripeti per tutta la lunghezza", "Fiore a sei petali: 6 anelli di 2 o 3 dita, cuore su un nuovo 260", "Lega con un 260 sgonfio, fiocco in Reflex Gold, taglia gli steli per ultimi"],
    "client_body": "Preferisci guardare che leggere? Audrey realizza questi 3 fiori e il fiocco sul canale YouTube di Sempertex Europe.",
    "cta_label": "Ordina",
    "s3_cover_a": "Fiori Sempertex:", "s3_cover_b": "gonfiato del tutto", "s3_cover_c": "vs.", "s3_cover_d": "coda lunga",
    "s3_left": "GONFIATO DEL TUTTO", "s3_right": "CODA LUNGA", "s3_left_meta": "1 twist, anelli grandi", "s3_right_meta": "3 twist, 2 o 3 dita",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Gonfiare del tutto", "Anelli grandi", "1 twist"], "s3_new_tags": ["Coda lunga", "2 o 3 dita", "3 twist", "Stessa direzione"],
    "s3_new_quote": "“Coda lunga, bolle piccole, tre giri. Tre fiori da otto 260, e l'ultimo anello ci sta ancora.”", "s3_new_badge": "8 × 260, 3 fiori",
    "s3_changed_bottom": "Stessi 260, stesse mani.\nOra ogni twist resta al suo posto.",
    "s3_topic_lbl": "PERCHÉ", "s3_rule1_topic": "3 fiori", "s3_rule1_old": "Basta saper fare un fiore",
    "s3_rule1_quote": "“Tulipano, lavanda e fiore a sei petali: 3 tecniche, ognuna da 1 × 260, insieme 1 bouquet.”",
    "s3_rule2_topic": "Bouquet", "s3_rule2_old": "Tagliare gli steli e via",
    "s3_rule2_quote": "“Legare con un 260 sgonfio, fiocco in Reflex Gold, tagliare gli steli per ultimi.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_topic": "Due palette", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 e Reflex Gold 970 come nel tutorial, o {p0}, {p1} e {p2} dallo scaffale.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "Primo bouquet",
    "s3_client_quote": "“Otto 260, una pompa a mano e un cutter. A un bouquet non serve altro.”",
    "s3_cta_kicker": "8 × 260, 3 fiori, 1 bouquet",
    "tulip_lbl": "tulipano", "lav_lbl": "lavanda", "six_lbl": "sei petali", "bow_lbl": "fiocco", "noroom_lbl": "troppo corto", "bouquet_lbl": "3 fiori", "chips": ["8 × 260", "2 o 3 dita", "3× girare"],
},
"pl": {
    "cover_pills": ["8 × 260…", "3 kwiaty…", "Długi pusty ogon…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Kwiaty z balonów…",
    "steps_title": "Kwiaty z balonów 260: 3 zasady przed pierwszym skrętem", "steps_lead": "Zanim zaczniesz:",
    "steps": ["Nigdy nie pompuj do pełna: zostaw długi pusty ogon, bo każdy skręt wpycha powietrze z powrotem do balonu", "Trzymaj bąbelki małe i równe, mierz je palcami. Pętle: 2 do 3 palców", "Każdy skręt obracaj 2 lub 3 razy, zawsze w tę samą stronę, inaczej się poluzuje", "Na kwiat 2 × 260 (kwiat i łodyga). Bukiet z 3: około 8 × 260, z kokardą i jednym pustym do związania", "Narzędzia: pompka ręczna i nożyk. Nic więcej"],
    "steps_label": "Zasady",
    "rule1_label": "3 kwiaty", "rule1_title": "Tulipan, lawenda i kwiat o sześciu płatkach: każdy z 1 × 260",
    "rule1_body": "Tulipan: złóż pierwszy bąbelek i przeciągnij przez niego węzeł, 2 równe płatki, potem reszta, nadmiar zwiń do środka. Lawenda: bąbelek i 2 pinch twisty, powtarzane na całej długości. Kwiat o sześciu płatkach: 6 pętli po 2 do 3 palców, zablokuj skrętem, otwórz płatki na przemian wyżej i niżej, aż będzie okrągły; serce to mały bąbelek na nowym 260, reszta staje się łodygą. Pinch twist to mniejszy bąbelek, który odciągasz od siebie i obracasz 2 lub 3 razy wokół jego osi, żeby leżał ciasno przy balonie.",
    "rule1_facts": [["5", "płatków w tulipanie, z 1 × 260"], ["2", "pinch twisty po każdym bąbelku lawendy"], ["6", "pętli po 2 do 3 palców w kwiecie o sześciu płatkach"], ["8", "balonów 260 na bukiet z 3, +2 na każdy dodatkowy kwiat"]],
    "rule2_label": "Bukiet", "rule2_title": "Kokarda, bukiet i 3 pytania, które zadaje każdy",
    "rule2_body": "Kwiaty to połowa roboty. Wykończenie robi z nich bukiet:",
    "alts": [["Zwiąż łodygi", "owiń pusty 260 luźno wokół 3 łodyg, ustaw wysokości, łodygi przytnij na końcu."], ["Kokarda", "Reflex Gold 260 napompowany do pełna i lekko spuszczony, podwójny pinch twist w środku, 2 pętle dookoła, równe wstążki."], ["Kończy się balon?", "za mocno napompowany albo za duże pętle. Zostaw hojny ogon i trzymaj pętle na 2 do 3 palcach."], ["Na łuku", "zrób punkty mocowania, zawiąż szyjkę balonu od łuku do tyłu każdego kwiatu, rozmieść je nieregularnie."], ["Inne rozmiary", "260 to standard. 160 na drobniejsze kwiaty, 360 na większe."]],
    "example_label": "Przykład", "example_title": "Jeden bukiet, dwie palety",
    "ex_items": [["Jak w tutorialu", "tulipan w Pastel Dusk Rose 110, lawenda w Pastel Dusk Lavender, kwiat o sześciu płatkach w Pastel Dusk Blue. Łodygi w Eucalyptus 027, kokarda w Reflex Gold 970."], ["Z półki twojego dystrybutora", "wybierz 3 kolory z linii 260, na przykład {p0}, {p1} i {p2}, zostaw Eucalyptus 027 na łodygi i {p3} na kokardę."]],
    "example_body": "Wszystko w 260. Na drobniejsze kwiaty weź 160, na większe 360. Licz 8 × 260 na bukiet z 3 i 2 więcej na każdy dodatkowy kwiat.",
    "client_label": "Koleżanka pyta", "client_title": "Co odpowiadasz, gdy pyta koleżanka",
    "client_answers": [
        "260 to standard do wszystkiego: kwiat, łodyga i kokarda. Na drobniejsze kwiaty weź 160. Większe kwiaty na łuk albo dużą dekorację: 360. Najpierw naucz się na 260, cały tutorial się na nim mieści.",
        "Około 8: 3 na kwiaty, 3 na łodygi, 1 na kokardę i 1 pusty do związania łodyg. Każdy dodatkowy kwiat to 2 więcej, jeden na kwiat i jeden na łodygę.",
        "Tak. Zrób punkty mocowania na łuku, zawiąż szyjkę balonu od łuku do punktu łączenia z tyłu każdego kwiatu i rozmieść je nieregularnie. Wygląda to naturalniej niż sztywny wzór.",
    ],
    "avoid_lead": "Twój pierwszy bukiet, w 5 krokach:",
    "steps5": ["Napompuj 3 × 260 na kwiaty, długi pusty ogon", "Tulipan: złóż pierwszy bąbelek, przeciągnij węzeł, 5 płatków", "Lawenda: bąbelek + 2 pinch twisty, powtarzaj na całej długości", "Kwiat o sześciu płatkach: 6 pętli po 2 do 3 palców, serce na nowym 260", "Zwiąż pustym 260, kokarda w Reflex Gold, łodygi przytnij na końcu"],
    "client_body": "Wolisz oglądać niż czytać? Audrey robi te 3 kwiaty i kokardę na kanale YouTube Sempertex Europe.",
    "cta_label": "Zamów",
    "s3_cover_a": "Kwiaty Sempertex:", "s3_cover_b": "do pełna", "s3_cover_c": "vs.", "s3_cover_d": "długi ogon",
    "s3_left": "DO PEŁNA", "s3_right": "DŁUGI OGON", "s3_left_meta": "1 skręt, duże pętle", "s3_right_meta": "3 skręty, 2-3 palce",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Do pełna", "Duże pętle", "1 skręt"], "s3_new_tags": ["Długi ogon", "2 do 3 palców", "3 skręty", "Ta sama strona"],
    "s3_new_quote": "“Długi ogon, małe bąbelki, trzy obroty. Trzy kwiaty z ośmiu 260 i ostatnia pętla wciąż się mieści.”", "s3_new_badge": "8 × 260, 3 kwiaty",
    "s3_changed_bottom": "Te same 260, te same ręce.\nTeraz każdy skręt zostaje na miejscu.",
    "s3_topic_lbl": "DLACZEGO", "s3_rule1_topic": "3 kwiaty", "s3_rule1_old": "Wystarczy umieć jeden kwiat",
    "s3_rule1_quote": "“Tulipan, lawenda i kwiat o sześciu płatkach: 3 techniki, każda z 1 × 260, razem 1 bukiet.”",
    "s3_rule2_topic": "Bukiet", "s3_rule2_old": "Przyciąć łodygi i gotowe",
    "s3_rule2_quote": "“Związać pustym 260, kokarda w Reflex Gold, łodygi przyciąć na końcu.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_topic": "Dwie palety", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 i Reflex Gold 970 jak w tutorialu, albo {p0}, {p1} i {p2} z półki.”",
    "s3_client_lbl": "KOLEŻANKA", "s3_client_topic": "Pierwszy bukiet",
    "s3_client_quote": "“Osiem 260, pompka ręczna i nożyk. Bukiet nie potrzebuje nic więcej.”",
    "s3_cta_kicker": "8 × 260, 3 kwiaty, 1 bukiet",
    "tulip_lbl": "tulipan", "lav_lbl": "lawenda", "six_lbl": "sześć płatków", "bow_lbl": "kokarda", "noroom_lbl": "za krótko", "bouquet_lbl": "3 kwiaty", "chips": ["8 × 260", "2 do 3 palców", "3× skręt"],
},
"el": {
    "cover_pills": ["8 × 260…", "3 λουλούδια…", "Μακριά άδεια ουρά…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Λουλούδια από μπαλόνια…",
    "steps_title": "Λουλούδια από 260: 3 κανόνες πριν το πρώτο στρίψιμο", "steps_lead": "Πριν ξεκινήσεις:",
    "steps": ["Μη φουσκώνεις ποτέ πλήρως: άφησε μια μακριά άδεια ουρά, γιατί κάθε στρίψιμο σπρώχνει αέρα πίσω στο μπαλόνι", "Κράτα τις φούσκες μικρές και ίσες, μέτρα τες με τα δάχτυλά σου. Θηλιές: 2 με 3 δάχτυλα", "Στρίψε κάθε στρίψιμο 2 με 3 φορές, πάντα προς την ίδια κατεύθυνση, αλλιώς λύνεται", "Ανά λουλούδι 2 × 260 (λουλούδι και κοτσάνι). Μπουκέτο των 3: περίπου 8 × 260, με τον φιόγκο και ένα ξεφούσκωτο για δέσιμο", "Εργαλεία: μια τρόμπα χειρός και ένας κόφτης. Τίποτα άλλο"],
    "steps_label": "Οι κανόνες",
    "rule1_label": "Τα 3 λουλούδια", "rule1_title": "Τουλίπα, λεβάντα και λουλούδι με έξι πέταλα: το καθένα από 1 × 260",
    "rule1_body": "Τουλίπα: δίπλωσε την πρώτη φούσκα και πέρασε τον κόμπο μέσα, 2 ίσα πέταλα, μετά τα υπόλοιπα, τύλιξε το περίσσευμα προς τα μέσα. Λεβάντα: μία φούσκα και 2 pinch twists, επαναλαμβανόμενα σε όλο το μήκος. Λουλούδι με έξι πέταλα: 6 θηλιές των 2 με 3 δαχτύλων, κλείδωσε με ένα στρίψιμο, άνοιξε τα πέταλα εναλλάξ ψηλά και χαμηλά μέχρι να γίνει στρογγυλό· η καρδιά είναι μια μικρή φούσκα σε νέο 260, το υπόλοιπο γίνεται κοτσάνι. Το pinch twist είναι μια μικρότερη φούσκα που τραβάς μακριά σου και στρίβεις 2 με 3 φορές γύρω από τον άξονά της, ώστε να κάθεται σφιχτά πάνω στο μπαλόνι.",
    "rule1_facts": [["5", "πέταλα στην τουλίπα, από 1 × 260"], ["2", "pinch twists μετά από κάθε φούσκα της λεβάντας"], ["6", "θηλιές των 2 με 3 δαχτύλων στο λουλούδι με έξι πέταλα"], ["8", "260 για μπουκέτο των 3, +2 ανά επιπλέον λουλούδι"]],
    "rule2_label": "Μπουκέτο", "rule2_title": "Φιόγκος, μπουκέτο και οι 3 ερωτήσεις που κάνουν όλοι",
    "rule2_body": "Τα λουλούδια είναι η μισή δουλειά. Το φινίρισμα τα κάνει μπουκέτο:",
    "alts": [["Δέσε τα κοτσάνια", "τύλιξε ένα ξεφούσκωτο 260 χαλαρά γύρω από τα 3 κοτσάνια, ρύθμισε τα ύψη, κόψε τα κοτσάνια τελευταία."], ["Ο φιόγκος", "Reflex Gold 260 πλήρως φουσκωμένο και λίγο ξεφουσκωμένο, διπλό pinch twist στο κέντρο, 2 θηλιές γύρω του, ίσες κορδέλες."], ["Τελείωσε το μπαλόνι;", "πολύ φουσκωμένο ή θηλιές πολύ μεγάλες. Άφησε γενναιόδωρη ουρά και κράτα τις θηλιές στα 2 με 3 δάχτυλα."], ["Σε αψίδα", "φτιάξε σημεία στερέωσης, δέσε έναν λαιμό μπαλονιού από την αψίδα στο πίσω μέρος κάθε λουλουδιού, μοίρασέ τα ακανόνιστα."], ["Άλλα μεγέθη", "το 260 είναι το στάνταρ. 160 για πιο λεπτά λουλούδια, 360 για μεγαλύτερα."]],
    "example_label": "Παράδειγμα", "example_title": "Ένα μπουκέτο, δύο παλέτες",
    "ex_items": [["Όπως στο tutorial", "τουλίπα σε Pastel Dusk Rose 110, λεβάντα σε Pastel Dusk Lavender, λουλούδι με έξι πέταλα σε Pastel Dusk Blue. Κοτσάνια σε Eucalyptus 027, φιόγκος σε Reflex Gold 970."], ["Από το ράφι του διανομέα σου", "διάλεξε 3 χρώματα από τη σειρά 260, για παράδειγμα {p0}, {p1} και {p2}, κράτα Eucalyptus 027 για τα κοτσάνια και {p3} για τον φιόγκο."]],
    "example_body": "Όλα σε 260. Για πιο λεπτά λουλούδια πάρε 160, για μεγαλύτερα 360. Υπολόγισε 8 × 260 για μπουκέτο των 3 και 2 επιπλέον για κάθε έξτρα λουλούδι.",
    "client_label": "Ρωτάει συνάδελφος", "client_title": "Τι απαντάς όταν ρωτάει ένας συνάδελφος",
    "client_answers": [
        "Το 260 είναι το στάνταρ για όλα: λουλούδι, κοτσάνι και φιόγκο. Για πιο λεπτά λουλούδια πάρε ένα 160. Μεγαλύτερα λουλούδια για αψίδα ή μεγάλη κατασκευή: ένα 360. Μάθε το πρώτα στο 260, όλο το tutorial χωράει εκεί.",
        "Περίπου 8: 3 για τα λουλούδια, 3 για τα κοτσάνια, 1 για τον φιόγκο και 1 ξεφούσκωτο για να δέσεις τα κοτσάνια. Κάθε επιπλέον λουλούδι κοστίζει 2 ακόμα, ένα για το λουλούδι και ένα για το κοτσάνι.",
        "Ναι. Φτιάξε σημεία στερέωσης στην αψίδα, δέσε έναν λαιμό μπαλονιού από την αψίδα στο σημείο ένωσης πίσω από κάθε λουλούδι, και μοίρασέ τα ακανόνιστα. Φαίνεται πιο φυσικό από ένα αυστηρό μοτίβο.",
    ],
    "avoid_lead": "Το πρώτο σου μπουκέτο, σε 5 βήματα:",
    "steps5": ["Φούσκωσε 3 × 260 για τα λουλούδια, μακριά άδεια ουρά", "Τουλίπα: δίπλωσε την πρώτη φούσκα, πέρασε τον κόμπο, 5 πέταλα", "Λεβάντα: φούσκα + 2 pinch twists, επανάλαβε σε όλο το μήκος", "Λουλούδι με έξι πέταλα: 6 θηλιές των 2 με 3 δαχτύλων, καρδιά σε νέο 260", "Δέσε με ξεφούσκωτο 260, φιόγκος σε Reflex Gold, κόψε τα κοτσάνια τελευταία"],
    "client_body": "Προτιμάς να βλέπεις παρά να διαβάζεις; Η Audrey φτιάχνει αυτά τα 3 λουλούδια και τον φιόγκο στο κανάλι YouTube της Sempertex Europe.",
    "cta_label": "Παραγγελία",
    "s3_cover_a": "Λουλούδια Sempertex:", "s3_cover_b": "πλήρως φουσκωμένο", "s3_cover_c": "vs.", "s3_cover_d": "μακριά ουρά",
    "s3_left": "ΠΛΗΡΩΣ ΦΟΥΣΚΩΜΕΝΟ", "s3_right": "ΜΑΚΡΙΑ ΟΥΡΑ", "s3_left_meta": "1 στροφή, μεγάλη θηλιά", "s3_right_meta": "3 στροφές, 2-3 δάχτυλα",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Πλήρες φούσκωμα", "Μεγάλες θηλιές", "1 στρίψιμο"], "s3_new_tags": ["Μακριά ουρά", "2 με 3 δάχτυλα", "3 στριψίματα", "Ίδια κατεύθυνση"],
    "s3_new_quote": "“Μακριά ουρά, μικρές φούσκες, τρία στριψίματα. Τρία λουλούδια από οκτώ 260, και η τελευταία θηλιά χωράει ακόμα.”", "s3_new_badge": "8 × 260, 3 λουλούδια",
    "s3_changed_bottom": "Ίδια 260, ίδια χέρια.\nΤώρα κάθε στρίψιμο μένει στη θέση του.",
    "s3_topic_lbl": "ΓΙΑΤΙ", "s3_rule1_topic": "3 λουλούδια", "s3_rule1_old": "Ένα λουλούδι αρκεί να ξέρεις",
    "s3_rule1_quote": "“Τουλίπα, λεβάντα και λουλούδι με έξι πέταλα: 3 τεχνικές, η καθεμία από 1 × 260, μαζί 1 μπουκέτο.”",
    "s3_rule2_topic": "Μπουκέτο", "s3_rule2_old": "Κόβω τα κοτσάνια και τέλος",
    "s3_rule2_quote": "“Δέσιμο με ξεφούσκωτο 260, φιόγκος σε Reflex Gold, κοτσάνια τελευταία.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_topic": "Δύο παλέτες", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 και Reflex Gold 970 όπως στο tutorial, ή {p0}, {p1} και {p2} από το ράφι.”",
    "s3_client_lbl": "ΣΥΝΑΔΕΛΦΟΣ", "s3_client_topic": "Πρώτο μπουκέτο",
    "s3_client_quote": "“Οκτώ 260, μια τρόμπα χειρός και ένας κόφτης. Ένα μπουκέτο δεν χρειάζεται τίποτα άλλο.”",
    "s3_cta_kicker": "8 × 260, 3 λουλούδια, 1 μπουκέτο",
    "tulip_lbl": "τουλίπα", "lav_lbl": "λεβάντα", "six_lbl": "έξι πέταλα", "bow_lbl": "φιόγκος", "noroom_lbl": "δεν χωράει", "bouquet_lbl": "3 λουλούδια", "chips": ["8 × 260", "2 με 3 δάχτυλα", "3× στρίψιμο"],
},
"hu": {
    "cover_pills": ["8 × 260…", "3 virág…", "Hosszú üres farok…"], "cover_with": "ezzel:", "cover_brand": "Sempertex Europe", "cover_tag": "Lufivirágok…",
    "steps_title": "Lufivirágok 260-asból: 3 szabály az első csavarás előtt", "steps_lead": "Mielőtt elkezded:",
    "steps": ["Soha ne fújd fel teljesen: hagyj hosszú üres farkat, mert minden csavarás levegőt nyom vissza a lufiba", "Tartsd a buborékokat kicsinek és egyformának, mérd őket az ujjaiddal. Hurkok: 2-3 ujj", "Minden csavarást 2-3-szor forgass, mindig ugyanabba az irányba, különben kilazul", "Virágonként 2 × 260 (virág és szár). 3 virágos csokor: kb. 8 × 260, masnival és egy üres lufival az összefogáshoz", "Eszközök: kézipumpa és vágó. Semmi más"],
    "steps_label": "A szabályok",
    "rule1_label": "A 3 virág", "rule1_title": "Tulipán, levendula és hatszirmú virág: mindegyik 1 × 260-asból",
    "rule1_body": "Tulipán: hajtsd be az első buborékot és húzd át a csomót, 2 egyforma szirom, aztán a többi, a felesleget tekerd befelé. Levendula: egy buborék és 2 pinch twist, ismételve a teljes hosszon. Hatszirmú virág: 6 hurok 2-3 ujjnyi, rögzítés egy csavarással, a szirmokat felváltva magasra és mélyre nyitod, amíg kerek nem lesz; a közepe egy kis buborék egy új 260-ason, a többi lesz a szár. A pinch twist egy kisebb buborék, amit elhúzol magadtól és 2-3-szor a saját tengelye körül forgatsz, hogy szorosan a lufihoz simuljon.",
    "rule1_facts": [["5", "szirom a tulipánban, 1 × 260-asból"], ["2", "pinch twist a levendula minden buboréka után"], ["6", "hurok 2-3 ujjnyi a hatszirmú virágban"], ["8", "260-as egy 3 virágos csokorhoz, +2 minden további virághoz"]],
    "rule2_label": "Csokor", "rule2_title": "Masni, csokor és a 3 kérdés, amit mindenki feltesz",
    "rule2_body": "A virágok a munka fele. A befejezés teszi csokorrá őket:",
    "alts": [["Fogd össze a szárakat", "tekerj egy üres 260-ast lazán a 3 szár köré, állítsd be a magasságokat, a szárakat utoljára vágd."], ["A masni", "Reflex Gold 260 teljesen felfújva, majd kicsit leeresztve, dupla pinch twist középen, 2 hurok köré, egyforma szalagok."], ["Elfogy a lufi a végén?", "túl erősen felfújtad, vagy túl nagyok a hurkok. Hagyj bő farkat, és tartsd a hurkokat 2-3 ujjnyin."], ["Íven", "készíts rögzítési pontokat, köss lufinyakat az ívtől minden virág hátuljához, oszd el őket szabálytalanul."], ["Más méretek", "a 260 a standard. 160 finomabb virágokhoz, 360 nagyobbakhoz."]],
    "example_label": "Példa", "example_title": "Egy csokor, két paletta",
    "ex_items": [["Ahogy a tutorialban", "tulipán Pastel Dusk Rose 110, levendula Pastel Dusk Lavender, hatszirmú virág Pastel Dusk Blue színben. Szárak Eucalyptus 027, masni Reflex Gold 970."], ["A forgalmazód polcáról", "válassz 3 színt a 260-as vonalból, például {p0}, {p1} és {p2}, tartsd meg az Eucalyptus 027-et a szárakhoz és a {p3}-t a masnihoz."]],
    "example_body": "Minden 260-asban. Finomabb virágokhoz 160-ast, nagyobbakhoz 360-ast végy. Számolj 8 × 260-assal egy 3 virágos csokorhoz, és 2-vel többel minden további virághoz.",
    "client_label": "Kolléga kérdezi", "client_title": "Mit válaszolsz, ha egy kolléga kérdezi",
    "client_answers": [
        "A 260 a standard mindenhez: virág, szár és masni. Finomabb virágokhoz végy 160-ast. Nagyobb virágokhoz ívre vagy nagy darabhoz: 360-ast. Először a 260-ason tanuld meg, arra ráfér az egész tutorial.",
        "Kb. 8: 3 a virágokhoz, 3 a szárakhoz, 1 a masnihoz és 1 üres a szárak összefogásához. Minden további virág 2-vel több, egy a virághoz és egy a szárhoz.",
        "Igen. Készíts rögzítési pontokat az íven, köss lufinyakat az ívtől minden virág hátulján lévő csatlakozási ponthoz, és oszd el őket szabálytalanul. Így természetesebb, mint egy szigorú minta.",
    ],
    "avoid_lead": "Az első csokrod, 5 lépésben:",
    "steps5": ["Fújj fel 3 × 260-ast a virágokhoz, hosszú üres farok", "Tulipán: hajtsd be az első buborékot, húzd át a csomót, 5 szirom", "Levendula: buborék + 2 pinch twist, ismételd a teljes hosszon", "Hatszirmú virág: 6 hurok 2-3 ujjnyi, közép egy új 260-ason", "Fogd össze üres 260-assal, masni Reflex Goldban, szárak utoljára"],
    "client_body": "Inkább néznéd, mint olvasnád? Audrey elkészíti ezt a 3 virágot és a masnit a Sempertex Europe YouTube-csatornáján.",
    "cta_label": "Rendelés",
    "s3_cover_a": "Sempertex virágok:", "s3_cover_b": "teljesen felfújva", "s3_cover_c": "vs.", "s3_cover_d": "hosszú farok",
    "s3_left": "TELJESEN FELFÚJVA", "s3_right": "HOSSZÚ FAROK", "s3_left_meta": "1 csavarás, nagy hurok", "s3_right_meta": "3 csavarás, 2-3 ujj",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Teljesen felfújva", "Nagy hurkok", "1 csavarás"], "s3_new_tags": ["Hosszú farok", "2-3 ujj", "3 csavarás", "Egy irány"],
    "s3_new_quote": "“Hosszú farok, kis buborékok, háromszori csavarás. Három virág nyolc 260-asból, és az utolsó hurok is kifér.”", "s3_new_badge": "8 × 260, 3 virág",
    "s3_changed_bottom": "Ugyanazok a 260-asok, ugyanazok a kezek.\nMost minden csavarás a helyén marad.",
    "s3_topic_lbl": "MIÉRT", "s3_rule1_topic": "3 virág", "s3_rule1_old": "Egy virágot tudni elég",
    "s3_rule1_quote": "“Tulipán, levendula és hatszirmú virág: 3 technika, mindegyik 1 × 260-asból, együtt 1 csokor.”",
    "s3_rule2_topic": "Csokor", "s3_rule2_old": "Szárak levágva, kész",
    "s3_rule2_quote": "“Összefogás üres 260-assal, masni Reflex Goldban, szárak utoljára.”",
    "s3_example_lbl": "PÉLDA", "s3_example_topic": "Két paletta", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 és Reflex Gold 970, ahogy a tutorialban, vagy {p0}, {p1} és {p2} a polcról.”",
    "s3_client_lbl": "KOLLÉGA", "s3_client_topic": "Első csokor",
    "s3_client_quote": "“Nyolc 260-as, egy kézipumpa és egy vágó. Egy csokornak nem kell több.”",
    "s3_cta_kicker": "8 × 260, 3 virág, 1 csokor",
    "tulip_lbl": "tulipán", "lav_lbl": "levendula", "six_lbl": "hatszirmú", "bow_lbl": "masni", "noroom_lbl": "elfogyott", "bouquet_lbl": "3 virág", "chips": ["8 × 260", "2-3 ujj", "3× csavarás"],
},
"lt": {
    "cover_pills": ["8 × 260…", "3 gėlės…", "Ilga tuščia uodega…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Balionų gėlės…",
    "steps_title": "Balionų gėlės iš 260: 3 taisyklės prieš pirmą sukimą", "steps_lead": "Prieš pradedant:",
    "steps": ["Niekada nepripūsk pilnai: palik ilgą tuščią uodegą, nes kiekvienas sukimas stumia orą atgal į balioną", "Laikyk burbulus mažus ir vienodus, matuok juos pirštais. Kilpos: 2-3 pirštai", "Kiekvieną sukimą suk 2-3 kartus, visada ta pačia kryptimi, kitaip atsileidžia", "Vienai gėlei 2 × 260 (gėlė ir stiebas). 3 gėlių puokštė: apie 8 × 260, su kaspinu ir vienu tuščiu surišimui", "Įrankiai: rankinė pompa ir pjoviklis. Nieko daugiau"],
    "steps_label": "Taisyklės",
    "rule1_label": "3 gėlės", "rule1_title": "Tulpė, levanda ir šešių žiedlapių gėlė: kiekviena iš 1 × 260",
    "rule1_body": "Tulpė: perlenk pirmą burbulą ir pertrauk mazgą, 2 vienodi žiedlapiai, tada likusieji, perteklių susuk į vidų. Levanda: vienas burbulas ir 2 pinch twist, kartojama per visą ilgį. Šešių žiedlapių gėlė: 6 kilpos po 2-3 pirštus, užfiksuok sukimu, atverk žiedlapius pakaitomis aukštai ir žemai, kol bus apvali; širdis yra mažas burbulas ant naujo 260, likusi dalis tampa stiebu. Pinch twist yra mažesnis burbulas, kurį patrauki nuo savęs ir pasuki 2-3 kartus apie jo ašį, kad tvirtai priglustų prie baliono.",
    "rule1_facts": [["5", "žiedlapiai tulpėje, iš 1 × 260"], ["2", "pinch twist po kiekvieno levandos burbulo"], ["6", "kilpos po 2-3 pirštus šešių žiedlapių gėlėje"], ["8", "260 balionai 3 gėlių puokštei, +2 kiekvienai papildomai gėlei"]],
    "rule2_label": "Puokštė", "rule2_title": "Kaspinas, puokštė ir 3 klausimai, kuriuos užduoda visi",
    "rule2_body": "Gėlės yra pusė darbo. Užbaigimas paverčia jas puokšte:",
    "alts": [["Surišk stiebus", "laisvai apvyniok tuščią 260 aplink 3 stiebus, nustatyk aukščius, stiebus nukirpk paskutinius."], ["Kaspinas", "Reflex Gold 260 pilnai pripūstas ir šiek tiek išleistas, dvigubas pinch twist viduryje, 2 kilpos aplink, vienodos juostelės."], ["Pritrūko baliono?", "per daug pripūsta arba per didelės kilpos. Palik dosnią uodegą ir laikyk kilpas 2-3 pirštų."], ["Ant arkos", "padaryk tvirtinimo taškus, pririšk baliono kaklelį nuo arkos prie kiekvienos gėlės nugaros, išdėstyk jas netaisyklingai."], ["Kiti dydžiai", "260 yra standartas. 160 smulkesnėms gėlėms, 360 didesnėms."]],
    "example_label": "Pavyzdys", "example_title": "Viena puokštė, dvi paletės",
    "ex_items": [["Kaip tutoriale", "tulpė Pastel Dusk Rose 110, levanda Pastel Dusk Lavender, šešių žiedlapių gėlė Pastel Dusk Blue. Stiebai Eucalyptus 027, kaspinas Reflex Gold 970."], ["Iš tavo platintojo lentynos", "pasirink 3 spalvas iš 260 linijos, pavyzdžiui {p0}, {p1} ir {p2}, palik Eucalyptus 027 stiebams ir {p3} kaspinui."]],
    "example_body": "Viskas 260. Smulkesnėms gėlėms imk 160, didesnėms 360. Skaičiuok 8 × 260 3 gėlių puokštei ir 2 daugiau kiekvienai papildomai gėlei.",
    "client_label": "Klausia kolegė", "client_title": "Ką atsakai, kai klausia kolegė",
    "client_answers": [
        "260 yra standartas viskam: gėlei, stiebui ir kaspinui. Smulkesnėms gėlėms imk 160. Didesnėms gėlėms arkai ar dideliam kūriniui: 360. Pirma išmok ant 260, visas tutorialas telpa ant jo.",
        "Apie 8: 3 gėlėms, 3 stiebams, 1 kaspinui ir 1 tuščias stiebams surišti. Kiekviena papildoma gėlė kainuoja 2 daugiau, vieną gėlei ir vieną stiebui.",
        "Taip. Padaryk tvirtinimo taškus ant arkos, pririšk baliono kaklelį nuo arkos prie jungties kiekvienos gėlės nugaroje ir išdėstyk jas netaisyklingai. Tai atrodo natūraliau nei griežtas raštas.",
    ],
    "avoid_lead": "Tavo pirma puokštė, 5 žingsniais:",
    "steps5": ["Pripūsk 3 × 260 gėlėms, ilga tuščia uodega", "Tulpė: perlenk pirmą burbulą, pertrauk mazgą, 5 žiedlapiai", "Levanda: burbulas + 2 pinch twist, kartok per visą ilgį", "Šešių žiedlapių gėlė: 6 kilpos po 2-3 pirštus, širdis ant naujo 260", "Surišk tuščiu 260, kaspinas Reflex Gold, stiebus nukirpk paskutinius"],
    "client_body": "Geriau žiūrėti nei skaityti? Audrey padaro šias 3 gėles ir kaspiną Sempertex Europe YouTube kanale.",
    "cta_label": "Užsakyti",
    "s3_cover_a": "Sempertex gėlės:", "s3_cover_b": "pilnai pripūsta", "s3_cover_c": "vs.", "s3_cover_d": "ilga uodega",
    "s3_left": "PILNAI PRIPŪSTA", "s3_right": "ILGA UODEGA", "s3_left_meta": "1 sukimas, plati kilpa", "s3_right_meta": "3 sukimai, 2-3 pirštai",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Pilnai pripūsti", "Didelės kilpos", "1 sukimas"], "s3_new_tags": ["Ilga uodega", "2-3 pirštai", "3 sukimai", "Ta pati kryptis"],
    "s3_new_quote": "“Ilga uodega, maži burbulai, trys sukimai. Trys gėlės iš aštuonių 260, ir paskutinė kilpa dar telpa.”", "s3_new_badge": "8 × 260, 3 gėlės",
    "s3_changed_bottom": "Tie patys 260, tos pačios rankos.\nDabar kiekvienas sukimas laikosi.",
    "s3_topic_lbl": "KODĖL", "s3_rule1_topic": "3 gėlės", "s3_rule1_old": "Užtenka mokėti vieną gėlę",
    "s3_rule1_quote": "“Tulpė, levanda ir šešių žiedlapių gėlė: 3 technikos, kiekviena iš 1 × 260, kartu 1 puokštė.”",
    "s3_rule2_topic": "Puokštė", "s3_rule2_old": "Nukirpti stiebus ir baigta",
    "s3_rule2_quote": "“Surišti tuščiu 260, kaspinas Reflex Gold, stiebai nukerpami paskutiniai.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_topic": "Dvi paletės", "s3_example_quote": "“Pastel Dusk Rose 110, Eucalyptus 027 ir Reflex Gold 970 kaip tutoriale, arba {p0}, {p1} ir {p2} iš lentynos.”",
    "s3_client_lbl": "KOLEGĖ", "s3_client_topic": "Pirma puokštė",
    "s3_client_quote": "“Aštuoni 260, rankinė pompa ir pjoviklis. Puokštei daugiau nieko nereikia.”",
    "s3_cta_kicker": "8 × 260, 3 gėlės, 1 puokštė",
    "tulip_lbl": "tulpė", "lav_lbl": "levanda", "six_lbl": "šeši žiedlapiai", "bow_lbl": "kaspinas", "noroom_lbl": "pritrūko", "bouquet_lbl": "3 gėlės", "chips": ["8 × 260", "2-3 pirštai", "3× sukti"],
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["3 ballonbloemen uit 8 Sempertex 260's: tulp, lavendel en zesbladige bloem, stap voor stap", "Een boeket dat nooit verwelkt: ballonbloemen uit Sempertex 260's, met de 3 regels van Audrey", "Tulp, lavendel, zesbladige bloem: 8 Sempertex 260's, 1 boeket, en de 3 regels voor elke draai"],
  "cover_sub": ["De 3 regels voor je begint, de 3 bloemen elk uit 1 × 260, de strik in Reflex Gold en het boeket. Met de kleuren uit de tutorial.", "Lange lege staart, kleine bubbels, 2 à 3 keer draaien. Daarna: tulp, lavendel, zesbladige bloem en een strik."],
  "client_question": ["Welke ballonnen neem ik voor bloemen: 160, 260 of 360?", "Hoeveel 260's heb ik nodig voor een boeket van 3?", "Kan ik de bloemen op een boog zetten?"],
  "s3_old_quote": ["“Vol opblazen, dan heb je tenminste lucht genoeg”", "“Eén draai houdt ook wel”", "“Grote lussen, grotere bloem”"],
  "s3_client_old": ["“Ik ken één bloem, dat is genoeg”", "“Stelen knippen en klaar”"],
  "cta_title_tpl": "Bestel je Sempertex 260's bij {name}", "cta_sub_generic": "8 × 260 voor een boeket van 3, plus 2 per extra bloem.",
},
"en": {
  "cover_title": ["3 balloon flowers from 8 Sempertex 260s: tulip, lavender and six-petal flower, step by step", "A bouquet that never wilts: balloon flowers from Sempertex 260s, with Audrey's 3 rules", "Tulip, lavender, six-petal flower: 8 Sempertex 260s, 1 bouquet, and the 3 rules for every twist"],
  "cover_sub": ["The 3 rules before you start, the 3 flowers each from 1 × 260, the bow in Reflex Gold and the bouquet. With the colours from the tutorial.", "Long empty tail, small bubbles, twist 2 or 3 times. Then: tulip, lavender, six-petal flower and a bow."],
  "client_question": ["Which balloons do I use for flowers: 160, 260 or 360?", "How many 260s do I need for a bouquet of 3?", "Can I put the flowers on an arch?"],
  "s3_old_quote": ["“Inflate it fully, at least then you've got enough air”", "“One twist holds fine”", "“Bigger loops, bigger flower”"],
  "s3_client_old": ["“I know one flower, that's enough”", "“Cut the stems and done”"],
  "cta_title_tpl": "Order your Sempertex 260s at {name}", "cta_sub_generic": "8 × 260 for a bouquet of 3, plus 2 per extra flower.",
},
"de": {
  "cover_title": ["3 Ballonblumen aus 8 Sempertex 260ern: Tulpe, Lavendel und sechsblättrige Blume, Schritt für Schritt", "Ein Strauß, der nie verwelkt: Ballonblumen aus Sempertex 260ern, mit Audreys 3 Regeln", "Tulpe, Lavendel, sechsblättrige Blume: 8 Sempertex 260er, 1 Strauß und die 3 Regeln für jeden Twist"],
  "cover_sub": ["Die 3 Regeln vor dem Start, die 3 Blumen je aus 1 × 260, die Schleife in Reflex Gold und der Strauß. Mit den Farben aus dem Tutorial.", "Langer leerer Schwanz, kleine Blasen, 2- bis 3-mal drehen. Dann: Tulpe, Lavendel, sechsblättrige Blume und eine Schleife."],
  "client_question": ["Welche Ballons nehme ich für Blumen: 160, 260 oder 360?", "Wie viele 260er brauche ich für einen Strauß aus 3?", "Kann ich die Blumen an einen Bogen hängen?"],
  "s3_old_quote": ["“Ganz aufblasen, dann hast du wenigstens genug Luft”", "“Ein Twist hält auch”", "“Größere Schlaufen, größere Blume”"],
  "s3_client_old": ["“Ich kann eine Blume, das reicht”", "“Stiele schneiden und fertig”"],
  "cta_title_tpl": "Bestell deine Sempertex 260er bei {name}", "cta_sub_generic": "8 × 260 für einen Strauß aus 3, plus 2 pro extra Blume.",
},
"fr": {
  "cover_title": ["3 fleurs en ballons avec 8 Sempertex 260 : tulipe, lavande et fleur à six pétales, pas à pas", "Un bouquet qui ne fane jamais : des fleurs en ballons Sempertex 260, avec les 3 règles d'Audrey", "Tulipe, lavande, fleur à six pétales : 8 Sempertex 260, 1 bouquet, et les 3 règles de chaque torsion"],
  "cover_sub": ["Les 3 règles avant de commencer, les 3 fleurs chacune avec 1 × 260, le nœud en Reflex Gold et le bouquet. Avec les couleurs du tutoriel.", "Longue queue vide, petites bulles, 2 ou 3 torsions. Ensuite : tulipe, lavande, fleur à six pétales et un nœud."],
  "client_question": ["Quels ballons pour des fleurs : 160, 260 ou 360 ?", "Combien de 260 pour un bouquet de 3 ?", "Je peux mettre les fleurs sur une arche ?"],
  "s3_old_quote": ["“Gonfle à fond, au moins tu as assez d'air”", "“Une torsion, ça tient aussi”", "“Grandes boucles, grande fleur”"],
  "s3_client_old": ["“Je connais une fleur, ça suffit”", "“Couper les tiges et c'est fini”"],
  "cta_title_tpl": "Commande tes Sempertex 260 chez {name}", "cta_sub_generic": "8 × 260 pour un bouquet de 3, plus 2 par fleur en plus.",
},
"it": {
  "cover_title": ["3 fiori di palloncini con 8 Sempertex 260: tulipano, lavanda e fiore a sei petali, passo per passo", "Un bouquet che non appassisce mai: fiori di palloncini Sempertex 260, con le 3 regole di Audrey", "Tulipano, lavanda, fiore a sei petali: 8 Sempertex 260, 1 bouquet e le 3 regole per ogni twist"],
  "cover_sub": ["Le 3 regole prima di iniziare, i 3 fiori ognuno da 1 × 260, il fiocco in Reflex Gold e il bouquet. Con i colori del tutorial.", "Coda vuota lunga, bolle piccole, 2 o 3 giri. Poi: tulipano, lavanda, fiore a sei petali e un fiocco."],
  "client_question": ["Quali palloncini uso per i fiori: 160, 260 o 360?", "Quanti 260 mi servono per un bouquet da 3?", "Posso mettere i fiori su un arco?"],
  "s3_old_quote": ["“Gonfia del tutto, almeno hai aria a sufficienza”", "“Un giro tiene lo stesso”", "“Anelli grandi, fiore grande”"],
  "s3_client_old": ["“So fare un fiore, basta”", "“Tagliare gli steli e via”"],
  "cta_title_tpl": "Ordina i tuoi Sempertex 260 da {name}", "cta_sub_generic": "8 × 260 per un bouquet da 3, più 2 per ogni fiore in più.",
},
"pl": {
  "cover_title": ["3 kwiaty z balonów z 8 Sempertex 260: tulipan, lawenda i kwiat o sześciu płatkach, krok po kroku", "Bukiet, który nigdy nie więdnie: kwiaty z balonów Sempertex 260, z 3 zasadami Audrey", "Tulipan, lawenda, kwiat o sześciu płatkach: 8 Sempertex 260, 1 bukiet i 3 zasady każdego skrętu"],
  "cover_sub": ["3 zasady przed startem, 3 kwiaty każdy z 1 × 260, kokarda w Reflex Gold i bukiet. Z kolorami z tutorialu.", "Długi pusty ogon, małe bąbelki, 2 lub 3 obroty. Potem: tulipan, lawenda, kwiat o sześciu płatkach i kokarda."],
  "client_question": ["Jakie balony na kwiaty: 160, 260 czy 360?", "Ile 260 potrzebuję na bukiet z 3?", "Czy mogę umieścić kwiaty na łuku?"],
  "s3_old_quote": ["“Napompuj do pełna, przynajmniej będzie dość powietrza”", "“Jeden skręt też trzyma”", "“Większe pętle, większy kwiat”"],
  "s3_client_old": ["“Umiem jeden kwiat, wystarczy”", "“Przyciąć łodygi i gotowe”"],
  "cta_title_tpl": "Zamów balony Sempertex 260 w {name}", "cta_sub_generic": "8 × 260 na bukiet z 3, plus 2 na każdy dodatkowy kwiat.",
},
"el": {
  "cover_title": ["3 λουλούδια από 8 Sempertex 260: τουλίπα, λεβάντα και λουλούδι με έξι πέταλα, βήμα βήμα", "Ένα μπουκέτο που δεν μαραίνεται ποτέ: λουλούδια από Sempertex 260, με τους 3 κανόνες της Audrey", "Τουλίπα, λεβάντα, λουλούδι με έξι πέταλα: 8 Sempertex 260, 1 μπουκέτο, και οι 3 κανόνες για κάθε στρίψιμο"],
  "cover_sub": ["Οι 3 κανόνες πριν ξεκινήσεις, τα 3 λουλούδια το καθένα από 1 × 260, ο φιόγκος σε Reflex Gold και το μπουκέτο. Με τα χρώματα του tutorial.", "Μακριά άδεια ουρά, μικρές φούσκες, 2 με 3 στριψίματα. Μετά: τουλίπα, λεβάντα, λουλούδι με έξι πέταλα και φιόγκος."],
  "client_question": ["Ποια μπαλόνια παίρνω για λουλούδια: 160, 260 ή 360;", "Πόσα 260 χρειάζομαι για μπουκέτο των 3;", "Μπορώ να βάλω τα λουλούδια σε αψίδα;"],
  "s3_old_quote": ["“Φούσκωσέ το πλήρως, τουλάχιστον έχεις αρκετό αέρα”", "“Ένα στρίψιμο κρατάει μια χαρά”", "“Μεγαλύτερες θηλιές, μεγαλύτερο λουλούδι”"],
  "s3_client_old": ["“Ξέρω ένα λουλούδι, αρκεί”", "“Κόβω τα κοτσάνια και τέλος”"],
  "cta_title_tpl": "Παράγγειλε τα Sempertex 260 σου από {name}", "cta_sub_generic": "8 × 260 για μπουκέτο των 3, συν 2 ανά επιπλέον λουλούδι.",
},
"hu": {
  "cover_title": ["3 lufivirág 8 Sempertex 260-asból: tulipán, levendula és hatszirmú virág, lépésről lépésre", "Egy csokor, ami sosem hervad el: lufivirágok Sempertex 260-asból, Audrey 3 szabályával", "Tulipán, levendula, hatszirmú virág: 8 Sempertex 260-as, 1 csokor és a 3 szabály minden csavaráshoz"],
  "cover_sub": ["A 3 szabály indulás előtt, a 3 virág egyenként 1 × 260-asból, a masni Reflex Goldban és a csokor. A tutorial színeivel.", "Hosszú üres farok, kis buborékok, 2-3-szori csavarás. Aztán: tulipán, levendula, hatszirmú virág és egy masni."],
  "client_question": ["Melyik lufit vegyem virágokhoz: 160, 260 vagy 360?", "Hány 260-as kell egy 3 virágos csokorhoz?", "Tehetem a virágokat ívre?"],
  "s3_old_quote": ["“Fújd fel teljesen, legalább van elég levegő”", "“Egy csavarás is megtartja”", "“Nagyobb hurkok, nagyobb virág”"],
  "s3_client_old": ["“Egy virágot tudok, az elég”", "“Szárak levágva, kész”"],
  "cta_title_tpl": "Rendeld a Sempertex 260-asokat innen: {name}", "cta_sub_generic": "8 × 260 egy 3 virágos csokorhoz, plusz 2 minden további virághoz.",
},
"lt": {
  "cover_title": ["3 balionų gėlės iš 8 Sempertex 260: tulpė, levanda ir šešių žiedlapių gėlė, žingsnis po žingsnio", "Puokštė, kuri niekada nevysta: balionų gėlės iš Sempertex 260, su 3 Audrey taisyklėmis", "Tulpė, levanda, šešių žiedlapių gėlė: 8 Sempertex 260, 1 puokštė ir 3 taisyklės kiekvienam sukimui"],
  "cover_sub": ["3 taisyklės prieš pradedant, 3 gėlės kiekviena iš 1 × 260, kaspinas Reflex Gold ir puokštė. Su tutorialo spalvomis.", "Ilga tuščia uodega, maži burbulai, 2-3 sukimai. Tada: tulpė, levanda, šešių žiedlapių gėlė ir kaspinas."],
  "client_question": ["Kokius balionus imti gėlėms: 160, 260 ar 360?", "Kiek 260 reikia 3 gėlių puokštei?", "Ar galiu dėti gėles ant arkos?"],
  "s3_old_quote": ["“Pripūsk pilnai, bent jau oro užteks”", "“Vienas sukimas irgi laiko”", "“Didesnės kilpos, didesnė gėlė”"],
  "s3_client_old": ["“Moku vieną gėlę, užtenka”", "“Nukirpti stiebus ir baigta”"],
  "cta_title_tpl": "Užsisakyk Sempertex 260 iš {name}", "cta_sub_generic": "8 × 260 3 gėlių puokštei, plius 2 kiekvienai papildomai gėlei.",
},
}

CAPTIONS_TPL = {
 "nl": "Ballonbloemen uit modelleerballonnen 260: tulp, lavendel en zesbladige bloem, samen in 1 boeket. In deze carousel: de 3 regels voor je begint (lange lege staart, kleine gelijke bubbels, 2 à 3 keer draaien in dezelfde richting), elke bloem stap voor stap, de strik in Reflex Gold en het bundelen. Reken 8 × 260 voor een boeket van 3. Kleuren uit de tutorial: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 en Reflex Gold 970.\n\nBestel je Sempertex 260's bij {domain}.\n\n#ballonbloemen #modelleerballonnen #sempertex #{tag} #ballondecoratie #ballonartiest",
 "en": "Balloon flowers from 260 modelling balloons: tulip, lavender and six-petal flower, together in 1 bouquet. In this carousel: the 3 rules before you start (long empty tail, small even bubbles, twist 2 or 3 times in the same direction), each flower step by step, the bow in Reflex Gold and the bundling. Count 8 × 260 for a bouquet of 3. Colours from the tutorial: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 and Reflex Gold 970.\n\nOrder your Sempertex 260s at {domain}.\n\n#balloonflowers #modellingballoons #sempertex #{tag} #balloondecor #balloonartist",
 "de": "Ballonblumen aus Modellierballons 260: Tulpe, Lavendel und sechsblättrige Blume, zusammen in 1 Strauß. Im Carousel: die 3 Regeln vor dem Start (langer leerer Schwanz, kleine gleichmäßige Blasen, 2- bis 3-mal in dieselbe Richtung drehen), jede Blume Schritt für Schritt, die Schleife in Reflex Gold und das Bündeln. Rechne 8 × 260 für einen Strauß aus 3. Farben aus dem Tutorial: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 und Reflex Gold 970.\n\nBestell deine Sempertex 260er bei {domain}.\n\n#ballonblumen #modellierballons #sempertex #{tag} #ballondeko #ballonkünstler",
 "fr": "Des fleurs en ballons à modeler 260 : tulipe, lavande et fleur à six pétales, réunies en 1 bouquet. Dans ce carrousel : les 3 règles avant de commencer (longue queue vide, petites bulles régulières, 2 ou 3 torsions dans le même sens), chaque fleur pas à pas, le nœud en Reflex Gold et le liage. Compte 8 × 260 pour un bouquet de 3. Couleurs du tutoriel : Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 et Reflex Gold 970.\n\nCommande tes Sempertex 260 chez {domain}.\n\n#fleursenballons #ballonsamodeler #sempertex #{tag} #decorationballons #artisteballon",
 "it": "Fiori di palloncini modellabili 260: tulipano, lavanda e fiore a sei petali, insieme in 1 bouquet. Nel carosello: le 3 regole prima di iniziare (coda vuota lunga, bolle piccole e uguali, 2 o 3 giri nella stessa direzione), ogni fiore passo per passo, il fiocco in Reflex Gold e la legatura. Conta 8 × 260 per un bouquet da 3. Colori del tutorial: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 e Reflex Gold 970.\n\nOrdina i tuoi Sempertex 260 da {domain}.\n\n#fioridipalloncini #palloncinimodellabili #sempertex #{tag} #palloncini #balloonartist",
 "pl": "Kwiaty z balonów do modelowania 260: tulipan, lawenda i kwiat o sześciu płatkach, razem w 1 bukiecie. W karuzeli: 3 zasady przed startem (długi pusty ogon, małe równe bąbelki, 2 lub 3 obroty w tę samą stronę), każdy kwiat krok po kroku, kokarda w Reflex Gold i związanie. Licz 8 × 260 na bukiet z 3. Kolory z tutorialu: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 i Reflex Gold 970.\n\nZamów balony Sempertex 260 w {domain}.\n\n#kwiatyzbalonow #balonydomodelowania #sempertex #{tag} #dekoracjebalonowe #artystabalonowy",
 "el": "Λουλούδια από μπαλόνια μοντελισμού 260: τουλίπα, λεβάντα και λουλούδι με έξι πέταλα, μαζί σε 1 μπουκέτο. Στο carousel: οι 3 κανόνες πριν ξεκινήσεις (μακριά άδεια ουρά, μικρές ίσες φούσκες, 2 με 3 στριψίματα προς την ίδια κατεύθυνση), κάθε λουλούδι βήμα βήμα, ο φιόγκος σε Reflex Gold και το δέσιμο. Υπολόγισε 8 × 260 για μπουκέτο των 3. Χρώματα από το tutorial: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 και Reflex Gold 970.\n\nΠαράγγειλε τα Sempertex 260 σου από {domain}.\n\n#λουλουδιααπομπαλονια #μπαλονιαμοντελισμου #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "Lufivirágok 260-as modellezőlufiból: tulipán, levendula és hatszirmú virág, együtt 1 csokorban. A carouselben: a 3 szabály indulás előtt (hosszú üres farok, kis egyforma buborékok, 2-3-szori csavarás ugyanabba az irányba), minden virág lépésről lépésre, a masni Reflex Goldban és az összefogás. Számolj 8 × 260-assal egy 3 virágos csokorhoz. A tutorial színei: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 és Reflex Gold 970.\n\nRendeld a Sempertex 260-asokat innen: {domain}.\n\n#lufiviragok #modellezolufi #sempertex #{tag} #lufidekoracio #lufiművész",
 "lt": "Balionų gėlės iš modeliavimo balionų 260: tulpė, levanda ir šešių žiedlapių gėlė, kartu 1 puokštėje. Karuselėje: 3 taisyklės prieš pradedant (ilga tuščia uodega, maži vienodi burbulai, 2-3 sukimai ta pačia kryptimi), kiekviena gėlė žingsnis po žingsnio, kaspinas Reflex Gold ir surišimas. Skaičiuok 8 × 260 3 gėlių puokštei. Tutorialo spalvos: Pastel Dusk Rose 110, Pastel Dusk Lavender, Pastel Dusk Blue, Eucalyptus 027 ir Reflex Gold 970.\n\nUžsisakyk Sempertex 260 iš {domain}.\n\n#balionugeles #modeliavimobalionai #sempertex #{tag} #balionai #balionumenininkas",
}

# ---------------------------------------------------------------- VISUALS
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}
TUT = ["duskrose", "violet", "matteblue", "reflexgold"]   # tulp, lavendel (benadering), zesbladig, strik

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

def _petal(key, size, angle, x, y):
    """Eén blaadje: een kleine ballon gedraaid rond zijn nek (onderkant)."""
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform-origin:50% 100%;transform:rotate({angle}deg)">{_bl(key, size)}</div>'

def flower6(key, centre, size=40):
    """Zesbladige bloem: 6 lussen rond één punt, hart in een tweede kleur."""
    ratio = G["PHOTO_RATIO"]; h = int(size * ratio); w = h * 2 + 6; cx = w // 2; cy = w // 2
    out = f'<div style="position:relative;width:{w}px;height:{w}px">'
    for a in (0, 60, 120, 180, 240, 300):
        out += _petal(key, size, a, cx - size // 2, cy - h)
    cs = int(size * .55); ch = int(cs * ratio)
    out += f'<div style="position:absolute;left:{cx - cs//2}px;top:{cy - ch//2}px">{_bl(centre, cs)}</div>'
    return out + '</div>'

def tulip(key, size=46):
    """Tulp: 5 blaadjes die vanuit één punt omhoog waaieren."""
    ratio = G["PHOTO_RATIO"]; h = int(size * ratio); w = int(h * 1.5) + size; cx = w // 2
    out = f'<div style="position:relative;width:{w}px;height:{h + 8}px">'
    for a in (-52, -26, 0, 26, 52):
        out += _petal(key, size, a, cx - size // 2 + int(a / 52 * size * .42), 0)
    return out + '</div>'

def lavender(key, size=24, n=7):
    """Lavendel: kolom van kleine bubbels (pinch twists) links en rechts van de steel."""
    ratio = G["PHOTO_RATIO"]; h = int(size * ratio); step = int(h * .62); w = int(size * 2.6); cx = w // 2
    H = step * n + h
    out = f'<div style="position:relative;width:{w}px;height:{H}px">'
    out += f'<div style="position:absolute;left:{cx-3}px;top:{h//2}px;width:6px;height:{H - h//2}px;background:{STEM};border-radius:3px"></div>'
    for i in range(n):
        a = -62 if i % 2 == 0 else 62
        out += _petal(key, size, a, cx - size // 2, i * step)
    return out + '</div>'

def stems_svg(w, h, pts, gx, gy, leaf=True):
    """Stelen van elk bloempunt naar het bundelpunt, met een blaadje op de langste."""
    svg = f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;left:0;top:0">'
    for (x, y) in pts:
        svg += f'<path d="M{x} {y} C {x} {y+60}, {gx} {gy-70}, {gx} {gy}" fill="none" stroke="{STEM}" stroke-width="7" stroke-linecap="round"/>'
    if leaf:
        svg += f'<ellipse cx="{gx-34}" cy="{gy-110}" rx="9" ry="22" transform="rotate(-35 {gx-34} {gy-110})" fill="{STEM}"/>'
    return svg + '</svg>'

def bow(key, size=34, ink="#111"):
    """Strik: 2 lussen (kleine ballonnen) rond een knoop, 2 linten."""
    ratio = G["PHOTO_RATIO"]; h = int(size * ratio); w = int(h * 1.9); cx = w // 2
    out = f'<div style="position:relative;width:{w}px;height:{int(h*1.35)}px">'
    out += _petal(key, size, -75, cx - size // 2, 2)
    out += _petal(key, size, 75, cx - size // 2, 2)
    out += f'<svg viewBox="0 0 {w} {int(h*1.35)}" width="{w}" height="{int(h*1.35)}" style="position:absolute;left:0;top:0"><path d="M{cx} {h} l -14 {int(h*.35)}" stroke="{G["SX"][key]["hex"]}" stroke-width="6" stroke-linecap="round"/><path d="M{cx} {h} l 14 {int(h*.35)}" stroke="{G["SX"][key]["hex"]}" stroke-width="6" stroke-linecap="round"/></svg>'
    out += f'<div style="position:absolute;left:{cx-7}px;top:{h-9}px;width:14px;height:14px;border-radius:50%;background:{ink}"></div>'
    return out + '</div>'

def bouquet(keys, ink="#111", w=330, h=380):
    """Boeket: tulp links, zesbladige bloem rechts, lavendel in het midden, stelen naar één punt, strik onderaan.
    keys = [tulp, lavendel, zesbladig, strik]."""
    gx, gy = w // 2, h - 60
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    out += stems_svg(w, h, [(78, 92), (w - 80, 118)], gx, gy)
    out += f'<div style="position:absolute;left:18px;top:14px">{tulip(keys[0], 46)}</div>'
    out += f'<div style="position:absolute;left:{w - 150}px;top:10px">{flower6(keys[2], keys[3] if len(keys) > 3 else keys[0], 38)}</div>'
    out += f'<div style="position:absolute;left:{gx - 31}px;top:96px">{lavender(keys[1], 24, 7)}</div>'
    out += f'<div style="position:absolute;left:{gx - 48}px;top:{gy - 36}px">{bow(keys[3] if len(keys) > 3 else "reflexgold", 34, ink)}</div>'
    return out + '</div>'

def stick260(key="red260", size=30, rot=0):
    """Packshot van een 260 modelleerballon, liggend: doos van L x size, optioneel licht gedraaid."""
    L = int(size * G["photo_ratio"](key)) if "photo_ratio" in G else int(size * 8.7)
    inner = f'<div style="position:absolute;left:{(L - size)//2}px;top:{(size - L)//2}px;transform:rotate(90deg)">{G["balloon"](key, "fashion", size)}</div>'
    return f'<div style="position:relative;width:{L}px;height:{size}px;transform:rotate({rot}deg);transform-origin:left center">{inner}</div>'

def chips_row(items, ink="#111", bg="#fff", small=False):
    esc = G["esc"]; extra = "font-size:15px;padding:4px 10px;" if small else ""
    return '<div style="display:flex;justify-content:center;gap:6px;flex-wrap:wrap">' + "".join(f'<span class="tchip" style="{extra}border-color:{ink};color:{ink};background:{bg}">{esc(t)}</span>' for t in items) + '</div>'

def noroom_visual(keys, c, ink="#111"):
    """'Vol opgeblazen': losse, te grote lussen die nergens heen gaan, een 260 op zijn kant en een rode stempel."""
    esc = G["esc"]; w, h = 330, 380
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    for i, (x, y, s, r) in enumerate([(20, 20, 70, -30), (110, 0, 78, 15), (205, 30, 72, 40), (60, 110, 66, 70), (170, 120, 74, -60)]):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg)">{_bl(keys[i % len(keys)], s)}</div>'
    out += f'<div style="position:absolute;left:10px;top:262px">{stick260("red260", 30, -7)}</div>'
    out += (f'<div style="position:absolute;left:150px;top:300px;transform:rotate(-6deg);background:#fff;color:#E03131;border:3px solid {ink};'
            f'border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">{esc(c["noroom_lbl"])} ✕</div>')
    return out + '</div>'

def bouquet_visual(keys, c, ink="#111"):
    """'Lange staart': het boeket + stempel '3 bloemen'."""
    esc = G["esc"]
    return (f'<div style="position:relative;width:330px;height:380px">'
            f'<div style="position:absolute;left:0;top:0">{bouquet(keys, ink)}</div>'
            f'<div style="position:absolute;left:0;top:328px;transform:rotate(-4deg);background:#fff;color:{ink};border:3px solid {ink};border-radius:10px;padding:8px 16px;font-size:22px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 4px 0 rgba(0,0,0,.18);white-space:nowrap">✓ {esc(c["bouquet_lbl"])}</div></div>')

def three_flowers(keys, c, ink="#111", lbl_size=17):
    """Drie losse bloemen naast elkaar met label: tulp, lavendel, zesbladig."""
    esc = G["esc"]
    def lab(t): return f'<div style="margin-top:8px;font-size:{lbl_size}px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:{ink};opacity:.65;white-space:nowrap">{esc(t)}</div>'
    cols = [f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end"><div style="height:150px;display:flex;align-items:flex-end">{tulip(keys[0], 54)}</div>{lab(c["tulip_lbl"])}</div>',
            f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end"><div style="height:150px;display:flex;align-items:flex-end"><div style="transform:scale(.8);transform-origin:bottom center">{lavender(keys[1], 24, 7)}</div></div>{lab(c["lav_lbl"])}</div>',
            f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end"><div style="height:150px;display:flex;align-items:flex-end">{flower6(keys[2], keys[3] if len(keys) > 3 else keys[0], 42)}</div>{lab(c["six_lbl"])}</div>']
    return '<div style="display:flex;gap:30px;align-items:flex-end;justify-content:center">' + "".join(cols) + '</div>'

def two_bouquets(keys, c, ink="#111", body_size=21, lbl_size=24, gap=26, vh=300, sc=1.0):
    """Voorbeeldslide: links het tutorial-boeket, rechts het boeket in het distri-palet."""
    esc = G["esc"]
    vis = [f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc:.2f});transform-origin:bottom center">{bouquet(TUT, ink, 330, 380)}</div></div>',
           f'<div style="height:{vh}px;display:flex;align-items:flex-end;justify-content:center;width:100%"><div style="transform:scale({sc:.2f});transform-origin:bottom center">{bouquet(keys, ink, 330, 380)}</div></div>']
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
    L = sum(len(s) for s in c["steps"]); sfs = 25 if L <= 380 else (23 if L <= 450 else 22)
    steps = "".join(f'<div class="step" style="font-size:{sfs}px"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:790px;height:440px">
    <h2 data-fit style="font-size:70px;max-height:350px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:905px;top:110px;transform:rotate(-16deg)">{_bl("red260", 34)}</div>
  <div style="position:absolute;left:110px;top:570px">{arrow_svg(b['ink'], 140, 120)}</div>
  <div class="box" style="left:250px;top:585px;width:760px;height:585px;padding:26px 36px">
    <div style="font-size:26px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:470px;padding:34px 44px">
    <h2 data-fit style="font-size:50px;max-height:130px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:14px;font-size:22px;line-height:1.32">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:690px;height:440px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:400px;padding:26px 30px">{facts_grid(c['rule1_facts'], 'facts', 48, 19)}</div>
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
  <div class="box" style="left:70px;top:160px;width:940px;height:720px;padding:30px 28px 26px">
    <h2 data-fit style="font-size:50px;margin-bottom:10px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    {two_bouquets(P, c, b['ink'], 20, 23, 24, 370, 1.0)}
  </div>
  <div class="box" style="left:70px;top:905px;width:940px;padding:18px 40px"><div class="body" style="font-size:21px">{esc(c['example_body'])}</div><div style="margin-top:10px">{chips_row(c['chips'], b['ink'], 'transparent', True)}</div></div>
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
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.08)">{bouquet_visual(P, c, '#111')}</div></div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px;font-size:24px"><b style="font-size:33px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:800px;width:930px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:290px;padding:16px 24px;box-sizing:border-box;background:#fff;color:#111;align-items:center;justify-content:flex-end"><div style="transform:scale(.95);transform-origin:bottom center">{three_flowers(P, c, '#111')}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:50px;max-height:150px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:360px;padding:22px 28px;box-sizing:border-box;align-items:stretch;background:#fff">{facts_grid(c['rule1_facts'], 'facts onwhite', 40, 17)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:790px;font-size:21px;line-height:1.32">{esc(c['rule1_body'])}</div>
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
    <div class="ph" style="height:auto;padding:20px 20px;box-sizing:border-box;align-items:flex-start;background:#fff;color:#111">{two_bouquets(P, c, '#111', 19, 22, 18, 300, .85)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1010px;font-size:20px">{esc(c['example_body'])}</div>
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
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{noroom_visual(loud, c, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{bouquet_visual(P, c, b['ink'])}</div>
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
    {two_bouquets(P, c, '#111', 20, 23, 18, 340, .95)}
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
