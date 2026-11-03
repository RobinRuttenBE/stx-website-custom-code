# -*- coding: utf-8 -*-
"""Topic: 'How to store your balloons correctly?' (sempertexeurope.com/en_GB/blog/how-to-store-your-balloons).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=storage.
Uit de blog: stabiel 10 tot 30 °C (Sempertex Europe bewaart op 18 °C), warmte versnelt licht/vocht/oxidatie, koud = minder
elastisch en scheurtjes, nooit invriezen, eerst op kamertemperatuur; donker (UV versnelt oxidatie, folie: inkt en metallic glans);
droog, max 35% vocht (schimmel); luchtdicht, zak dicht na openen en op jobs; FIFO; kwaliteit stopt niet bij het magazijn."""

G = {}
def setup(g): G.update(g)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["10 tot 30 °C…", "Max 35% vocht…", "FIFO…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Bewaargids…",
    "steps_title": "Latex blijft jaren goed, als je 5 dingen doet.", "steps_lead": "De 5 bewaarregels:",
    "steps": ["Stabiele temperatuur tussen 10 en 30 °C", "Donker of in de schaduw, nooit in direct zonlicht", "Droog: liefst niet meer dan 35% vocht", "Zak dicht, luchtdicht", "Roteer je stock: oudste eerst (FIFO)"],
    "steps_label": "De basis",
    "rule1_label": "Regel 1", "rule1_title": "Stabiel tussen 10 en 30 °C",
    "rule1_body": "Geen klimaatkamer nodig, wel zo weinig mogelijk schommeling. Sempertex Europe bewaart alles op 18 °C. Warmte versnelt de schade van licht, vocht en oxidatie. Heel koud latex verliest elasticiteit en scheurt sneller: nooit invriezen, en na een koude rit eerst op kamertemperatuur laten komen.",
    "rule1_facts": [["10 tot 30 °C", "stabiel, weinig schommeling"], ["18 °C", "het magazijn van Sempertex Europe"], ["0 °C", "nooit invriezen"], ["kamertemp.", "eerst opwarmen, dan opblazen"]],
    "rule2_label": "Regel 2", "rule2_title": "Donker, droog en de zak dicht",
    "rule2_body": "UV-licht versnelt de oxidatie van latex, en bij folie tast langdurig fel licht de inkt en de metallic glans aan. Hou de vochtigheid laag, liefst niet boven 35%: vocht plus slechte ventilatie geeft schimmel in je hele voorraad. Bewaar luchtdicht en sluit een geopende zak meteen weer. Neem naar een job enkel de kleuren mee die je nodig hebt.",
    "rule2_cards": [["UV", "schaduw, geen direct zonlicht"], ["≤ 35%", "vocht, goed geventileerd"], ["dicht", "luchtdicht, ook na openen"]],
    "example_label": "Voorbeeld", "example_title": "Je stock op de plank, in FIFO",
    "shelf_lbls": ["oudste", "", "", "nieuwste"],
    "example_body": "Vier zakken R12 op de plank: {p0}, {p1}, {p2} en {p3}. De oudste staat vooraan en gaat eerst mee naar de job, de nieuwste achteraan. Zakken dicht, uit de zon, droog. Zo zien de kleuren eruit zoals bedoeld als je de zak opent om te bouwen.",
    "client_label": "In de praktijk", "client_title": "Wat je antwoordt als een collega vraagt",
    "client_answers": [
        "Direct zonlicht en hitte versnellen de oxidatie. Haal ze uit de wagen, laat ze in de schaduw op kamertemperatuur komen en test er 2 voor je ermee bouwt. Voor de volgende keer: in een afgesloten bak, uit de zon.",
        "Een open zak staat maanden bloot aan lucht en vocht. Sluit hem nu, bewaar hem donker en gebruik hem als eerste op. Nieuwe zakken gaan erachter: oudste eerst.",
        "Correct bewaard, dus stabiel tussen 10 en 30 °C, donker, droog en luchtdicht, blijven ze jaren goed. Fout bewaard, een zomer in de bestelwagen, en je ziet het aan de kleur en de elasticiteit.",
    ],
    "avoid_lead": "Je bewaarcheck, elke levering:",
    "steps5": ["Stabiel tussen 10 en 30 °C, geen zon, geen vorst", "Donker of in de schaduw", "Droog, liefst niet boven 35% vocht", "Zak dicht na elke job", "Oudste zakken vooraan: FIFO"],
    "client_body": "Kwaliteit stopt niet bij het magazijn. Sempertex Europe levert in topconditie, de rest bepaal jij: koel, droog, donker en dicht.",
    "cta_label": "Bijbestellen",
    "s3_cover_a": "Sempertex ballonnen bewaren", "s3_cover_b": "in de bestelwagen", "s3_cover_c": "vs.", "s3_cover_d": "op de plank",
    "s3_left": "IN DE BESTELWAGEN", "s3_right": "OP DE PLANK", "s3_left_meta": "zon, hitte, zak open", "s3_right_meta": "18 °C, donker, dicht",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Zak open", "Waar plaats is"], "s3_new_tags": ["10 tot 30 °C", "Donker en droog", "Zak dicht", "FIFO"],
    "s3_new_quote": "“Stabiel, donker, droog en dicht. En de oudste zak gaat eerst mee.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Zelfde ballonnen, zelfde leverancier.\nDe kleur klopt nog als je de zak opent.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Temperatuur", "s3_rule1_old": "Latex kan wel tegen een stootje",
    "s3_rule1_quote": "“Stabiel tussen 10 en 30 °C. Nooit invriezen, nooit in de zon. Sempertex bewaart op 18 °C.”",
    "s3_rule2_topic": "Licht en vocht", "s3_rule2_old": "Die zak ligt al maanden open, wat zou het",
    "s3_rule2_quote": "“UV versnelt oxidatie, vocht boven 35% geeft schimmel. Donker, droog en de zak dicht.”",
    "s3_example_lbl": "VOORBEELD", "s3_example_quote": "“Vier zakken op de plank: {p0}, {p1}, {p2}, {p3}. Oudste vooraan, dicht, uit de zon.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "In de praktijk",
    "s3_client_quote": "“Correct bewaard blijven ze jaren goed. Een zomer in de bestelwagen zie je aan de kleur.”",
    "s3_cta_kicker": "Je bewaarcheck voor de volgende levering",
    "sun_lbl": "zon", "shade_lbl": "schaduw", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"en": {
    "cover_pills": ["10 to 30 °C…", "Max 35% humidity…", "FIFO…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Storage guide…",
    "steps_title": "Latex stays good for years, if you do 5 things.", "steps_lead": "The 5 storage rules:",
    "steps": ["Stable temperature between 10 and 30 °C", "Dark or shaded, never in direct sun", "Dry: ideally no more than 35% humidity", "Bag closed, airtight", "Rotate your stock: oldest first (FIFO)"],
    "steps_label": "The basics",
    "rule1_label": "Rule 1", "rule1_title": "Stable between 10 and 30 °C",
    "rule1_body": "No climate room needed, just as little swing as possible. Sempertex Europe stores everything at 18 °C. Heat speeds up the damage from light, moisture and oxidation. Very cold latex loses elasticity and tears more easily: never freeze it, and after a cold drive let it reach room temperature first.",
    "rule1_facts": [["10 to 30 °C", "stable, minimal swings"], ["18 °C", "the Sempertex Europe warehouse"], ["0 °C", "never freeze"], ["room temp.", "warm up first, then inflate"]],
    "rule2_label": "Rule 2", "rule2_title": "Dark, dry and the bag closed",
    "rule2_body": "UV light speeds up latex oxidation, and on foil prolonged bright light affects the inks and the metallic sheen. Keep humidity low, ideally no higher than 35%: moisture plus poor airflow means mould across your whole stock. Store airtight and reseal an opened bag straight away. Take only the colours you need to a job.",
    "rule2_cards": [["UV", "shade, no direct sun"], ["≤ 35%", "humidity, well ventilated"], ["sealed", "airtight, also after opening"]],
    "example_label": "Example", "example_title": "Your stock on the shelf, in FIFO",
    "shelf_lbls": ["oldest", "", "", "newest"],
    "example_body": "Four bags of R12 on the shelf: {p0}, {p1}, {p2} and {p3}. The oldest sits at the front and goes to the job first, the newest at the back. Bags closed, out of the sun, dry. That's how colours look as intended when you open a bag to build.",
    "client_label": "In practice", "client_title": "What you answer when a colleague asks",
    "client_answers": [
        "Direct sun and heat speed up oxidation. Take them out of the van, let them reach room temperature in the shade and test 2 before you build with them. Next time: in a closed box, out of the sun.",
        "An open bag sits exposed to air and moisture for months. Close it now, store it dark and use it up first. New bags go behind it: oldest first.",
        "Stored correctly, so stable between 10 and 30 °C, dark, dry and airtight, they stay good for years. Stored badly, a summer in the van, and you'll see it in the colour and the elasticity.",
    ],
    "avoid_lead": "Your storage check, every delivery:",
    "steps5": ["Stable between 10 and 30 °C, no sun, no frost", "Dark or shaded", "Dry, ideally no more than 35% humidity", "Bag closed after every job", "Oldest bags at the front: FIFO"],
    "client_body": "Quality doesn't stop at the warehouse. Sempertex Europe delivers in top condition, the rest is up to you: cool, dry, dark and closed.",
    "cta_label": "Restock",
    "s3_cover_a": "Storing Sempertex balloons", "s3_cover_b": "in the van", "s3_cover_c": "vs.", "s3_cover_d": "on the shelf",
    "s3_left": "IN THE VAN", "s3_right": "ON THE SHELF", "s3_left_meta": "sun, heat, bag open", "s3_right_meta": "18 °C, dark, sealed",
    "s3_changed_title": "What changes?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["Bag open", "Wherever there's room"], "s3_new_tags": ["10 to 30 °C", "Dark and dry", "Bag closed", "FIFO"],
    "s3_new_quote": "“Stable, dark, dry and sealed. And the oldest bag goes out first.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Same balloons, same supplier.\nThe colour is still right when you open the bag.",
    "s3_topic_lbl": "RULE", "s3_rule1_topic": "Temperature", "s3_rule1_old": "Latex can take a knock",
    "s3_rule1_quote": "“Stable between 10 and 30 °C. Never freeze, never in the sun. Sempertex stores at 18 °C.”",
    "s3_rule2_topic": "Light and moisture", "s3_rule2_old": "That bag's been open for months, so what",
    "s3_rule2_quote": "“UV speeds up oxidation, humidity above 35% means mould. Dark, dry and the bag closed.”",
    "s3_example_lbl": "EXAMPLE", "s3_example_quote": "“Four bags on the shelf: {p0}, {p1}, {p2}, {p3}. Oldest at the front, closed, out of the sun.”",
    "s3_client_lbl": "COLLEAGUE", "s3_client_topic": "In practice",
    "s3_client_quote": "“Stored correctly they stay good for years. A summer in the van shows in the colour.”",
    "s3_cta_kicker": "Your storage check for the next delivery",
    "sun_lbl": "sun", "shade_lbl": "shade", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"de": {
    "cover_pills": ["10 bis 30 °C…", "Max. 35% Feuchte…", "FIFO…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Lager-Guide…",
    "steps_title": "Latex bleibt jahrelang gut, wenn du 5 Dinge tust.", "steps_lead": "Die 5 Lagerregeln:",
    "steps": ["Stabile Temperatur zwischen 10 und 30 °C", "Dunkel oder im Schatten, nie in direkter Sonne", "Trocken: am besten nicht über 35% Luftfeuchte", "Beutel zu, luftdicht", "Bestand rotieren: Ältestes zuerst (FIFO)"],
    "steps_label": "Die Basis",
    "rule1_label": "Regel 1", "rule1_title": "Stabil zwischen 10 und 30 °C",
    "rule1_body": "Kein Klimaraum nötig, aber so wenig Schwankung wie möglich. Sempertex Europe lagert alles bei 18 °C. Wärme beschleunigt die Schäden durch Licht, Feuchtigkeit und Oxidation. Sehr kaltes Latex verliert Elastizität und reißt leichter: nie einfrieren, und nach einer kalten Fahrt erst auf Raumtemperatur kommen lassen.",
    "rule1_facts": [["10 bis 30 °C", "stabil, kaum Schwankung"], ["18 °C", "das Lager von Sempertex Europe"], ["0 °C", "nie einfrieren"], ["Raumtemp.", "erst aufwärmen, dann aufblasen"]],
    "rule2_label": "Regel 2", "rule2_title": "Dunkel, trocken und Beutel zu",
    "rule2_body": "UV-Licht beschleunigt die Oxidation von Latex, und bei Folie greift lange helles Licht Farben und Metallic-Glanz an. Halte die Luftfeuchte niedrig, am besten nicht über 35%: Feuchtigkeit plus schlechte Belüftung bringt Schimmel in den ganzen Bestand. Luftdicht lagern und einen geöffneten Beutel sofort wieder verschließen. Zum Job nur die Farben mitnehmen, die du brauchst.",
    "rule2_cards": [["UV", "Schatten, keine direkte Sonne"], ["≤ 35%", "Feuchte, gut belüftet"], ["zu", "luftdicht, auch nach dem Öffnen"]],
    "example_label": "Beispiel", "example_title": "Dein Bestand im Regal, nach FIFO",
    "shelf_lbls": ["ältester", "", "", "neuester"],
    "example_body": "Vier Beutel R12 im Regal: {p0}, {p1}, {p2} und {p3}. Der älteste steht vorne und geht zuerst mit zum Job, der neueste hinten. Beutel zu, aus der Sonne, trocken. So sehen die Farben aus wie gedacht, wenn du den Beutel zum Bauen öffnest.",
    "client_label": "In der Praxis", "client_title": "Was du antwortest, wenn eine Kollegin fragt",
    "client_answers": [
        "Direkte Sonne und Hitze beschleunigen die Oxidation. Raus aus dem Wagen, im Schatten auf Raumtemperatur kommen lassen und 2 Stück testen, bevor du damit baust. Fürs nächste Mal: in einer geschlossenen Box, aus der Sonne.",
        "Ein offener Beutel liegt monatelang an Luft und Feuchtigkeit. Jetzt schließen, dunkel lagern und als Erstes aufbrauchen. Neue Beutel dahinter: Ältestes zuerst.",
        "Richtig gelagert, also stabil zwischen 10 und 30 °C, dunkel, trocken und luftdicht, bleiben sie jahrelang gut. Falsch gelagert, ein Sommer im Transporter, und du siehst es an Farbe und Elastizität.",
    ],
    "avoid_lead": "Dein Lager-Check, bei jeder Lieferung:",
    "steps5": ["Stabil zwischen 10 und 30 °C, keine Sonne, kein Frost", "Dunkel oder im Schatten", "Trocken, am besten nicht über 35% Feuchte", "Beutel zu nach jedem Job", "Älteste Beutel vorne: FIFO"],
    "client_body": "Qualität hört nicht im Lager auf. Sempertex Europe liefert in Topzustand, der Rest liegt bei dir: kühl, trocken, dunkel und zu.",
    "cta_label": "Nachbestellen",
    "s3_cover_a": "Sempertex Ballons lagern", "s3_cover_b": "im Transporter", "s3_cover_c": "vs.", "s3_cover_d": "im Regal",
    "s3_left": "IM TRANSPORTER", "s3_right": "IM REGAL", "s3_left_meta": "Sonne, Hitze, Beutel offen", "s3_right_meta": "18 °C, dunkel, zu",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Beutel offen", "Wo Platz ist"], "s3_new_tags": ["10 bis 30 °C", "Dunkel und trocken", "Beutel zu", "FIFO"],
    "s3_new_quote": "“Stabil, dunkel, trocken und zu. Und der älteste Beutel geht zuerst mit.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Gleiche Ballons, gleicher Lieferant.\nDie Farbe stimmt noch, wenn du den Beutel öffnest.",
    "s3_topic_lbl": "REGEL", "s3_rule1_topic": "Temperatur", "s3_rule1_old": "Latex hält schon was aus",
    "s3_rule1_quote": "“Stabil zwischen 10 und 30 °C. Nie einfrieren, nie in die Sonne. Sempertex lagert bei 18 °C.”",
    "s3_rule2_topic": "Licht und Feuchte", "s3_rule2_old": "Der Beutel ist seit Monaten offen, na und",
    "s3_rule2_quote": "“UV beschleunigt Oxidation, Feuchte über 35% bringt Schimmel. Dunkel, trocken und Beutel zu.”",
    "s3_example_lbl": "BEISPIEL", "s3_example_quote": "“Vier Beutel im Regal: {p0}, {p1}, {p2}, {p3}. Ältester vorne, zu, aus der Sonne.”",
    "s3_client_lbl": "KOLLEGIN", "s3_client_topic": "In der Praxis",
    "s3_client_quote": "“Richtig gelagert bleiben sie jahrelang gut. Einen Sommer im Transporter sieht man an der Farbe.”",
    "s3_cta_kicker": "Dein Lager-Check für die nächste Lieferung",
    "sun_lbl": "Sonne", "shade_lbl": "Schatten", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"fr": {
    "cover_pills": ["10 à 30 °C…", "Max 35 % d'humidité…", "FIFO…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Guide de stockage…",
    "steps_title": "Le latex reste bon des années, si tu fais 5 choses.", "steps_lead": "Les 5 règles de stockage :",
    "steps": ["Température stable entre 10 et 30 °C", "Dans le noir ou à l'ombre, jamais en plein soleil", "Au sec : idéalement pas plus de 35 % d'humidité", "Sachet fermé, hermétique", "Fais tourner ton stock : le plus ancien d'abord (FIFO)"],
    "steps_label": "La base",
    "rule1_label": "Règle 1", "rule1_title": "Stable entre 10 et 30 °C",
    "rule1_body": "Pas besoin de pièce climatisée, mais le moins de variations possible. Sempertex Europe stocke tout à 18 °C. La chaleur accélère les dégâts de la lumière, de l'humidité et de l'oxydation. Un latex très froid perd son élasticité et se déchire plus vite : ne le congèle jamais, et après un trajet froid, laisse-le revenir à température ambiante.",
    "rule1_facts": [["10 à 30 °C", "stable, peu de variations"], ["18 °C", "l'entrepôt de Sempertex Europe"], ["0 °C", "ne jamais congeler"], ["temp. ambiante", "réchauffer d'abord, gonfler ensuite"]],
    "rule2_label": "Règle 2", "rule2_title": "Au noir, au sec et sachet fermé",
    "rule2_body": "Les UV accélèrent l'oxydation du latex, et sur le foil une lumière forte prolongée altère les encres et le brillant métallique. Garde l'humidité basse, idéalement pas plus de 35 % : humidité plus mauvaise aération, c'est de la moisissure dans tout ton stock. Stocke hermétiquement et referme tout de suite un sachet ouvert. N'emporte sur une prestation que les couleurs dont tu as besoin.",
    "rule2_cards": [["UV", "à l'ombre, jamais en plein soleil"], ["≤ 35 %", "d'humidité, bien aéré"], ["fermé", "hermétique, même après ouverture"]],
    "example_label": "Exemple", "example_title": "Ton stock sur l'étagère, en FIFO",
    "shelf_lbls": ["plus ancien", "", "", "plus récent"],
    "example_body": "Quatre sachets de R12 sur l'étagère : {p0}, {p1}, {p2} et {p3}. Le plus ancien devant, il part en premier sur la prestation, le plus récent derrière. Sachets fermés, à l'abri du soleil, au sec. C'est comme ça que les couleurs sont fidèles quand tu ouvres un sachet pour monter.",
    "client_label": "En pratique", "client_title": "Ce que tu réponds quand un collègue demande",
    "client_answers": [
        "Le plein soleil et la chaleur accélèrent l'oxydation. Sors-les du camion, laisse-les revenir à température ambiante à l'ombre et testes-en 2 avant de monter. La prochaine fois : dans un bac fermé, à l'abri du soleil.",
        "Un sachet ouvert reste exposé à l'air et à l'humidité pendant des mois. Ferme-le maintenant, stocke-le au noir et utilise-le en premier. Les nouveaux sachets passent derrière : le plus ancien d'abord.",
        "Bien stockés, donc stables entre 10 et 30 °C, au noir, au sec et hermétiques, ils restent bons des années. Mal stockés, un été dans le camion, et ça se voit à la couleur et à l'élasticité.",
    ],
    "avoid_lead": "Ton check stockage, à chaque livraison :",
    "steps5": ["Stable entre 10 et 30 °C, ni soleil ni gel", "Au noir ou à l'ombre", "Au sec, idéalement pas plus de 35 % d'humidité", "Sachet fermé après chaque prestation", "Sachets les plus anciens devant : FIFO"],
    "client_body": "La qualité ne s'arrête pas à l'entrepôt. Sempertex Europe livre en parfait état, le reste dépend de toi : au frais, au sec, au noir et fermé.",
    "cta_label": "Réassort",
    "s3_cover_a": "Stocker ses ballons Sempertex", "s3_cover_b": "dans le camion", "s3_cover_c": "vs.", "s3_cover_d": "sur l'étagère",
    "s3_left": "DANS LE CAMION", "s3_right": "SUR L'ÉTAGÈRE", "s3_left_meta": "soleil, chaleur, sachet ouvert", "s3_right_meta": "18 °C, noir, fermé",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Sachet ouvert", "Là où il y a de la place"], "s3_new_tags": ["10 à 30 °C", "Noir et sec", "Sachet fermé", "FIFO"],
    "s3_new_quote": "“Stable, au noir, au sec et fermé. Et le sachet le plus ancien part en premier.”", "s3_new_badge": "Sempertex : 18 °C",
    "s3_changed_bottom": "Mêmes ballons, même fournisseur.\nLa couleur est encore juste quand tu ouvres le sachet.",
    "s3_topic_lbl": "RÈGLE", "s3_rule1_topic": "Température", "s3_rule1_old": "Le latex, ça encaisse",
    "s3_rule1_quote": "“Stable entre 10 et 30 °C. Jamais congelé, jamais au soleil. Sempertex stocke à 18 °C.”",
    "s3_rule2_topic": "Lumière et humidité", "s3_rule2_old": "Ce sachet est ouvert depuis des mois, et alors",
    "s3_rule2_quote": "“Les UV accélèrent l'oxydation, plus de 35 % d'humidité, c'est de la moisissure. Noir, sec et sachet fermé.”",
    "s3_example_lbl": "EXEMPLE", "s3_example_quote": "“Quatre sachets sur l'étagère : {p0}, {p1}, {p2}, {p3}. Le plus ancien devant, fermé, à l'abri du soleil.”",
    "s3_client_lbl": "COLLÈGUE", "s3_client_topic": "En pratique",
    "s3_client_quote": "“Bien stockés, ils restent bons des années. Un été dans le camion, ça se voit à la couleur.”",
    "s3_cta_kicker": "Ton check stockage pour la prochaine livraison",
    "sun_lbl": "soleil", "shade_lbl": "ombre", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"it": {
    "cover_pills": ["10 a 30 °C…", "Max 35% umidità…", "FIFO…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Guida alla conservazione…",
    "steps_title": "Il lattice resta buono per anni, se fai 5 cose.", "steps_lead": "Le 5 regole di conservazione:",
    "steps": ["Temperatura stabile tra 10 e 30 °C", "Al buio o all'ombra, mai al sole diretto", "All'asciutto: meglio non oltre il 35% di umidità", "Busta chiusa, ermetica", "Ruota lo stock: prima il più vecchio (FIFO)"],
    "steps_label": "La base",
    "rule1_label": "Regola 1", "rule1_title": "Stabile tra 10 e 30 °C",
    "rule1_body": "Niente stanza climatizzata, ma meno sbalzi possibile. Sempertex Europe conserva tutto a 18 °C. Il caldo accelera i danni di luce, umidità e ossidazione. Il lattice molto freddo perde elasticità e si strappa più facilmente: mai congelarlo, e dopo un viaggio al freddo lascialo tornare a temperatura ambiente.",
    "rule1_facts": [["10 a 30 °C", "stabile, pochi sbalzi"], ["18 °C", "il magazzino di Sempertex Europe"], ["0 °C", "mai congelare"], ["temp. ambiente", "prima scalda, poi gonfia"]],
    "rule2_label": "Regola 2", "rule2_title": "Al buio, all'asciutto e busta chiusa",
    "rule2_body": "La luce UV accelera l'ossidazione del lattice, e sul foil una luce forte prolungata rovina inchiostri e brillantezza metallica. Tieni bassa l'umidità, meglio non oltre il 35%: umidità più scarsa aerazione significa muffa in tutto lo stock. Conserva in modo ermetico e richiudi subito una busta aperta. Al lavoro porta solo i colori che ti servono.",
    "rule2_cards": [["UV", "all'ombra, niente sole diretto"], ["≤ 35%", "umidità, ben ventilato"], ["chiusa", "ermetica, anche dopo l'apertura"]],
    "example_label": "Esempio", "example_title": "Il tuo stock sullo scaffale, in FIFO",
    "shelf_lbls": ["più vecchia", "", "", "più nuova"],
    "example_body": "Quattro buste di R12 sullo scaffale: {p0}, {p1}, {p2} e {p3}. La più vecchia davanti, parte per prima verso il lavoro, la più nuova dietro. Buste chiuse, lontano dal sole, all'asciutto. Così i colori sono come previsto quando apri una busta per montare.",
    "client_label": "In pratica", "client_title": "Cosa rispondi quando un collega chiede",
    "client_answers": [
        "Sole diretto e calore accelerano l'ossidazione. Tirali fuori dal furgone, lasciali tornare a temperatura ambiente all'ombra e provane 2 prima di montare. La prossima volta: in una scatola chiusa, lontano dal sole.",
        "Una busta aperta resta esposta ad aria e umidità per mesi. Chiudila adesso, conservala al buio e usala per prima. Le buste nuove vanno dietro: prima la più vecchia.",
        "Conservati bene, quindi stabili tra 10 e 30 °C, al buio, all'asciutto ed ermetici, restano buoni per anni. Conservati male, un'estate nel furgone, e lo vedi dal colore e dall'elasticità.",
    ],
    "avoid_lead": "Il tuo check di conservazione, a ogni consegna:",
    "steps5": ["Stabile tra 10 e 30 °C, niente sole, niente gelo", "Al buio o all'ombra", "All'asciutto, meglio non oltre il 35% di umidità", "Busta chiusa dopo ogni lavoro", "Buste più vecchie davanti: FIFO"],
    "client_body": "La qualità non finisce in magazzino. Sempertex Europe consegna in condizioni perfette, il resto dipende da te: fresco, asciutto, buio e chiuso.",
    "cta_label": "Riordina",
    "s3_cover_a": "Conservare i palloncini Sempertex", "s3_cover_b": "nel furgone", "s3_cover_c": "vs.", "s3_cover_d": "sullo scaffale",
    "s3_left": "NEL FURGONE", "s3_right": "SULLO SCAFFALE", "s3_left_meta": "sole, caldo, busta aperta", "s3_right_meta": "18 °C, buio, chiusa",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["Busta aperta", "Dove c'è posto"], "s3_new_tags": ["10 a 30 °C", "Buio e asciutto", "Busta chiusa", "FIFO"],
    "s3_new_quote": "“Stabile, al buio, all'asciutto e chiusa. E la busta più vecchia parte per prima.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Stessi palloncini, stesso fornitore.\nIl colore è ancora giusto quando apri la busta.",
    "s3_topic_lbl": "REGOLA", "s3_rule1_topic": "Temperatura", "s3_rule1_old": "Il lattice regge tutto",
    "s3_rule1_quote": "“Stabile tra 10 e 30 °C. Mai congelare, mai al sole. Sempertex conserva a 18 °C.”",
    "s3_rule2_topic": "Luce e umidità", "s3_rule2_old": "Quella busta è aperta da mesi, e allora",
    "s3_rule2_quote": "“Gli UV accelerano l'ossidazione, umidità sopra il 35% significa muffa. Buio, asciutto e busta chiusa.”",
    "s3_example_lbl": "ESEMPIO", "s3_example_quote": "“Quattro buste sullo scaffale: {p0}, {p1}, {p2}, {p3}. La più vecchia davanti, chiusa, lontano dal sole.”",
    "s3_client_lbl": "COLLEGA", "s3_client_topic": "In pratica",
    "s3_client_quote": "“Conservati bene restano buoni per anni. Un'estate nel furgone si vede dal colore.”",
    "s3_cta_kicker": "Il tuo check di conservazione per la prossima consegna",
    "sun_lbl": "sole", "shade_lbl": "ombra", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"pl": {
    "cover_pills": ["10 do 30 °C…", "Max 35% wilgoci…", "FIFO…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Przewodnik przechowywania…",
    "steps_title": "Lateks zostaje dobry przez lata, jeśli zrobisz 5 rzeczy.", "steps_lead": "5 zasad przechowywania:",
    "steps": ["Stała temperatura między 10 a 30 °C", "W ciemności albo w cieniu, nigdy w pełnym słońcu", "Sucho: najlepiej nie więcej niż 35% wilgotności", "Torebka zamknięta, szczelnie", "Rotuj zapas: najstarsze pierwsze (FIFO)"],
    "steps_label": "Podstawy",
    "rule1_label": "Zasada 1", "rule1_title": "Stabilnie między 10 a 30 °C",
    "rule1_body": "Nie potrzebujesz klimatyzowanego pomieszczenia, tylko jak najmniej wahań. Sempertex Europe przechowuje wszystko w 18 °C. Ciepło przyspiesza szkody od światła, wilgoci i utleniania. Bardzo zimny lateks traci elastyczność i łatwiej pęka: nigdy nie zamrażaj, a po zimnej podróży daj mu najpierw dojść do temperatury pokojowej.",
    "rule1_facts": [["10 do 30 °C", "stabilnie, małe wahania"], ["18 °C", "magazyn Sempertex Europe"], ["0 °C", "nigdy nie zamrażaj"], ["temp. pokojowa", "najpierw ogrzej, potem pompuj"]],
    "rule2_label": "Zasada 2", "rule2_title": "Ciemno, sucho i torebka zamknięta",
    "rule2_body": "Światło UV przyspiesza utlenianie lateksu, a na folii długie ostre światło niszczy nadruk i metaliczny połysk. Trzymaj wilgotność nisko, najlepiej nie powyżej 35%: wilgoć plus słaba wentylacja to pleśń w całym zapasie. Przechowuj szczelnie i od razu zamykaj otwartą torebkę. Na zlecenie bierz tylko kolory, których potrzebujesz.",
    "rule2_cards": [["UV", "cień, bez pełnego słońca"], ["≤ 35%", "wilgotność, dobra wentylacja"], ["zamknięta", "szczelnie, także po otwarciu"]],
    "example_label": "Przykład", "example_title": "Twój zapas na półce, w FIFO",
    "shelf_lbls": ["najstarsza", "", "", "najnowsza"],
    "example_body": "Cztery torebki R12 na półce: {p0}, {p1}, {p2} i {p3}. Najstarsza stoi z przodu i pierwsza jedzie na zlecenie, najnowsza z tyłu. Torebki zamknięte, z dala od słońca, sucho. Dzięki temu kolory wyglądają tak, jak powinny, gdy otwierasz torebkę do pracy.",
    "client_label": "W praktyce", "client_title": "Co odpowiadasz, gdy koleżanka pyta",
    "client_answers": [
        "Pełne słońce i ciepło przyspieszają utlenianie. Wyjmij je z auta, daj im dojść do temperatury pokojowej w cieniu i przetestuj 2, zanim zaczniesz budować. Na przyszłość: w zamkniętym pojemniku, z dala od słońca.",
        "Otwarta torebka przez miesiące jest wystawiona na powietrze i wilgoć. Zamknij ją teraz, trzymaj w ciemności i zużyj jako pierwszą. Nowe torebki idą za nią: najstarsze pierwsze.",
        "Dobrze przechowywane, czyli stabilnie między 10 a 30 °C, ciemno, sucho i szczelnie, zostają dobre przez lata. Źle przechowywane, jedno lato w aucie, i widać to po kolorze i elastyczności.",
    ],
    "avoid_lead": "Twój check przechowywania, przy każdej dostawie:",
    "steps5": ["Stabilnie między 10 a 30 °C, bez słońca, bez mrozu", "Ciemno albo w cieniu", "Sucho, najlepiej nie powyżej 35% wilgotności", "Torebka zamknięta po każdym zleceniu", "Najstarsze torebki z przodu: FIFO"],
    "client_body": "Jakość nie kończy się w magazynie. Sempertex Europe dostarcza w idealnym stanie, reszta zależy od ciebie: chłodno, sucho, ciemno i szczelnie.",
    "cta_label": "Dokup",
    "s3_cover_a": "Przechowywanie balonów Sempertex", "s3_cover_b": "w aucie", "s3_cover_c": "vs.", "s3_cover_d": "na półce",
    "s3_left": "W AUCIE", "s3_right": "NA PÓŁCE", "s3_left_meta": "słońce, ciepło, torebka otwarta", "s3_right_meta": "18 °C, ciemno, zamknięta",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "STARE", "s3_new_lbl": "NOWE",
    "s3_old_tags": ["Torebka otwarta", "Gdzie jest miejsce"], "s3_new_tags": ["10 do 30 °C", "Ciemno i sucho", "Torebka zamknięta", "FIFO"],
    "s3_new_quote": "“Stabilnie, ciemno, sucho i szczelnie. A najstarsza torebka jedzie pierwsza.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Te same balony, ten sam dostawca.\nKolor wciąż się zgadza, gdy otwierasz torebkę.",
    "s3_topic_lbl": "ZASADA", "s3_rule1_topic": "Temperatura", "s3_rule1_old": "Lateks wiele zniesie",
    "s3_rule1_quote": "“Stabilnie między 10 a 30 °C. Nigdy nie zamrażaj, nigdy w słońcu. Sempertex przechowuje w 18 °C.”",
    "s3_rule2_topic": "Światło i wilgoć", "s3_rule2_old": "Ta torebka jest otwarta od miesięcy, i co z tego",
    "s3_rule2_quote": "“UV przyspiesza utlenianie, wilgotność powyżej 35% to pleśń. Ciemno, sucho i torebka zamknięta.”",
    "s3_example_lbl": "PRZYKŁAD", "s3_example_quote": "“Cztery torebki na półce: {p0}, {p1}, {p2}, {p3}. Najstarsza z przodu, zamknięta, z dala od słońca.”",
    "s3_client_lbl": "KOLEŻANKA", "s3_client_topic": "W praktyce",
    "s3_client_quote": "“Dobrze przechowywane zostają dobre przez lata. Jedno lato w aucie widać po kolorze.”",
    "s3_cta_kicker": "Twój check przechowywania na następną dostawę",
    "sun_lbl": "słońce", "shade_lbl": "cień", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"el": {
    "cover_pills": ["10 έως 30 °C…", "Max 35% υγρασία…", "FIFO…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Οδηγός αποθήκευσης…",
    "steps_title": "Το latex μένει καλό για χρόνια, αν κάνεις 5 πράγματα.", "steps_lead": "Οι 5 κανόνες αποθήκευσης:",
    "steps": ["Σταθερή θερμοκρασία 10 έως 30 °C", "Σκοτεινά ή σε σκιά, ποτέ σε άμεσο ήλιο", "Στεγνά: ιδανικά όχι πάνω από 35% υγρασία", "Σακούλα κλειστή, αεροστεγής", "Εναλλαγή αποθέματος: τα παλιότερα πρώτα (FIFO)"],
    "steps_label": "Τα βασικά",
    "rule1_label": "Κανόνας 1", "rule1_title": "Σταθερά μεταξύ 10 και 30 °C",
    "rule1_body": "Δεν χρειάζεται κλιματιζόμενος χώρος, μόνο όσο το δυνατόν λιγότερες διακυμάνσεις. Η Sempertex Europe αποθηκεύει τα πάντα στους 18 °C. Η ζέστη επιταχύνει τη ζημιά από φως, υγρασία και οξείδωση. Το πολύ κρύο latex χάνει ελαστικότητα και σκίζεται πιο εύκολα: ποτέ στην κατάψυξη, και μετά από κρύα διαδρομή άφησέ το πρώτα να έρθει σε θερμοκρασία δωματίου.",
    "rule1_facts": [["10 έως 30 °C", "σταθερά, λίγες διακυμάνσεις"], ["18 °C", "η αποθήκη της Sempertex Europe"], ["0 °C", "ποτέ κατάψυξη"], ["θερμ. δωματίου", "πρώτα ζέσταμα, μετά φούσκωμα"]],
    "rule2_label": "Κανόνας 2", "rule2_title": "Σκοτεινά, στεγνά και σακούλα κλειστή",
    "rule2_body": "Το UV φως επιταχύνει την οξείδωση του latex, και στο foil το παρατεταμένο έντονο φως χαλάει τα μελάνια και τη μεταλλική λάμψη. Κράτα την υγρασία χαμηλά, ιδανικά όχι πάνω από 35%: υγρασία και κακός αερισμός σημαίνει μούχλα σε όλο το απόθεμα. Αποθήκευε αεροστεγώς και ξανακλείνε αμέσως μια ανοιγμένη σακούλα. Σε δουλειά πάρε μόνο τα χρώματα που χρειάζεσαι.",
    "rule2_cards": [["UV", "σκιά, όχι άμεσος ήλιος"], ["≤ 35%", "υγρασία, καλός αερισμός"], ["κλειστή", "αεροστεγώς, και μετά το άνοιγμα"]],
    "example_label": "Παράδειγμα", "example_title": "Το απόθεμά σου στο ράφι, σε FIFO",
    "shelf_lbls": ["παλιότερη", "", "", "νεότερη"],
    "example_body": "Τέσσερις σακούλες R12 στο ράφι: {p0}, {p1}, {p2} και {p3}. Η παλιότερη μπροστά, πάει πρώτη στη δουλειά, η νεότερη πίσω. Σακούλες κλειστές, μακριά από τον ήλιο, στεγνά. Έτσι τα χρώματα είναι όπως πρέπει όταν ανοίγεις σακούλα για να στήσεις.",
    "client_label": "Στην πράξη", "client_title": "Τι απαντάς όταν ρωτά ένας συνάδελφος",
    "client_answers": [
        "Ο άμεσος ήλιος και η ζέστη επιταχύνουν την οξείδωση. Βγάλ' τα από το αυτοκίνητο, άφησέ τα στη σκιά να έρθουν σε θερμοκρασία δωματίου και δοκίμασε 2 πριν στήσεις. Για την επόμενη φορά: σε κλειστό κουτί, μακριά από τον ήλιο.",
        "Μια ανοιχτή σακούλα μένει εκτεθειμένη σε αέρα και υγρασία για μήνες. Κλείσ' την τώρα, αποθήκευσέ τη σκοτεινά και χρησιμοποίησέ τη πρώτη. Οι νέες σακούλες πάνε πίσω της: τα παλιότερα πρώτα.",
        "Σωστά αποθηκευμένα, δηλαδή σταθερά μεταξύ 10 και 30 °C, σκοτεινά, στεγνά και αεροστεγώς, μένουν καλά για χρόνια. Λάθος αποθηκευμένα, ένα καλοκαίρι στο αυτοκίνητο, και το βλέπεις στο χρώμα και στην ελαστικότητα.",
    ],
    "avoid_lead": "Ο έλεγχος αποθήκευσης, σε κάθε παράδοση:",
    "steps5": ["Σταθερά μεταξύ 10 και 30 °C, χωρίς ήλιο, χωρίς παγετό", "Σκοτεινά ή σε σκιά", "Στεγνά, ιδανικά όχι πάνω από 35% υγρασία", "Σακούλα κλειστή μετά από κάθε δουλειά", "Παλιότερες σακούλες μπροστά: FIFO"],
    "client_body": "Η ποιότητα δεν σταματά στην αποθήκη. Η Sempertex Europe παραδίδει σε άριστη κατάσταση, τα υπόλοιπα εξαρτώνται από σένα: δροσερά, στεγνά, σκοτεινά και κλειστά.",
    "cta_label": "Ανανέωση αποθέματος",
    "s3_cover_a": "Αποθήκευση μπαλονιών Sempertex", "s3_cover_b": "στο αυτοκίνητο", "s3_cover_c": "vs.", "s3_cover_d": "στο ράφι",
    "s3_left": "ΣΤΟ ΑΥΤΟΚΙΝΗΤΟ", "s3_right": "ΣΤΟ ΡΑΦΙ", "s3_left_meta": "ήλιος, ζέστη, σακούλα ανοιχτή", "s3_right_meta": "18 °C, σκοτεινά, κλειστή",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Σακούλα ανοιχτή", "Όπου έχει χώρο"], "s3_new_tags": ["10 έως 30 °C", "Σκοτεινά και στεγνά", "Σακούλα κλειστή", "FIFO"],
    "s3_new_quote": "“Σταθερά, σκοτεινά, στεγνά και κλειστά. Και η παλιότερη σακούλα φεύγει πρώτη.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Ίδια μπαλόνια, ίδιος προμηθευτής.\nΤο χρώμα είναι ακόμα σωστό όταν ανοίγεις τη σακούλα.",
    "s3_topic_lbl": "ΚΑΝΟΝΑΣ", "s3_rule1_topic": "Θερμοκρασία", "s3_rule1_old": "Το latex αντέχει τα πάντα",
    "s3_rule1_quote": "“Σταθερά μεταξύ 10 και 30 °C. Ποτέ κατάψυξη, ποτέ στον ήλιο. Η Sempertex αποθηκεύει στους 18 °C.”",
    "s3_rule2_topic": "Φως και υγρασία", "s3_rule2_old": "Αυτή η σακούλα είναι ανοιχτή μήνες, και τι έγινε",
    "s3_rule2_quote": "“Το UV επιταχύνει την οξείδωση, υγρασία πάνω από 35% σημαίνει μούχλα. Σκοτεινά, στεγνά και σακούλα κλειστή.”",
    "s3_example_lbl": "ΠΑΡΑΔΕΙΓΜΑ", "s3_example_quote": "“Τέσσερις σακούλες στο ράφι: {p0}, {p1}, {p2}, {p3}. Η παλιότερη μπροστά, κλειστή, μακριά από τον ήλιο.”",
    "s3_client_lbl": "ΣΥΝΑΔΕΛΦΟΣ", "s3_client_topic": "Στην πράξη",
    "s3_client_quote": "“Σωστά αποθηκευμένα μένουν καλά για χρόνια. Ένα καλοκαίρι στο αυτοκίνητο φαίνεται στο χρώμα.”",
    "s3_cta_kicker": "Ο έλεγχος αποθήκευσης για την επόμενη παράδοση",
    "sun_lbl": "ήλιος", "shade_lbl": "σκιά", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"hu": {
    "cover_pills": ["10 és 30 °C között…", "Max 35% pára…", "FIFO…"], "cover_with": "partner:", "cover_brand": "Sempertex Europe", "cover_tag": "Tárolási útmutató…",
    "steps_title": "A latex évekig jó marad, ha 5 dolgot megteszel.", "steps_lead": "Az 5 tárolási szabály:",
    "steps": ["Stabil hőmérséklet 10 és 30 °C között", "Sötétben vagy árnyékban, soha ne tűző napon", "Szárazon: lehetőleg legfeljebb 35% páratartalom", "Zacskó zárva, légmentesen", "Forgasd a készletet: a legrégebbi először (FIFO)"],
    "steps_label": "Az alapok",
    "rule1_label": "1. szabály", "rule1_title": "Stabilan 10 és 30 °C között",
    "rule1_body": "Nem kell klimatizált helyiség, csak minél kevesebb ingadozás. A Sempertex Europe mindent 18 °C-on tárol. A meleg felgyorsítja a fény, a nedvesség és az oxidáció okozta kárt. A nagyon hideg latex veszít a rugalmasságából és könnyebben szakad: soha ne fagyaszd le, és hideg út után előbb hagyd szobahőmérsékletre melegedni.",
    "rule1_facts": [["10 és 30 °C", "stabilan, kevés ingadozás"], ["18 °C", "a Sempertex Europe raktára"], ["0 °C", "soha ne fagyaszd"], ["szobahőm.", "előbb melegítsd, aztán fújd fel"]],
    "rule2_label": "2. szabály", "rule2_title": "Sötét, száraz, és a zacskó zárva",
    "rule2_body": "Az UV-fény felgyorsítja a latex oxidációját, a fólián pedig a tartós erős fény tönkreteszi a festéket és a metálfényt. Tartsd alacsonyan a párát, lehetőleg 35% alatt: pára és rossz szellőzés együtt penészt jelent az egész készletben. Tárold légmentesen, és a felbontott zacskót azonnal zárd vissza. Munkára csak azokat a színeket vidd, amikre szükséged van.",
    "rule2_cards": [["UV", "árnyék, tűző nap nélkül"], ["≤ 35%", "pára, jól szellőző"], ["zárva", "légmentesen, felbontás után is"]],
    "example_label": "Példa", "example_title": "A készleted a polcon, FIFO szerint",
    "shelf_lbls": ["legrégebbi", "", "", "legújabb"],
    "example_body": "Négy zacskó R12 a polcon: {p0}, {p1}, {p2} és {p3}. A legrégebbi elöl áll, az megy először munkára, a legújabb hátul. Zacskók zárva, naptól távol, szárazon. Így a színek olyanok, amilyennek lenniük kell, amikor kinyitod a zacskót építeni.",
    "client_label": "A gyakorlatban", "client_title": "Mit válaszolsz, ha egy kolléga megkérdezi",
    "client_answers": [
        "A tűző nap és a meleg felgyorsítja az oxidációt. Vedd ki őket az autóból, hagyd őket árnyékban szobahőmérsékletre melegedni, és próbálj ki 2-t, mielőtt építesz velük. Legközelebb: zárt dobozban, naptól távol.",
        "A nyitott zacskó hónapokig levegőnek és párának van kitéve. Zárd le most, tárold sötétben, és használd fel először. Az új zacskók mögé kerülnek: a legrégebbi először.",
        "Helyesen tárolva, vagyis stabilan 10 és 30 °C között, sötétben, szárazon és légmentesen, évekig jók maradnak. Rosszul tárolva, egy nyár az autóban, és látszik a színen és a rugalmasságon.",
    ],
    "avoid_lead": "A tárolási ellenőrzésed, minden szállításnál:",
    "steps5": ["Stabilan 10 és 30 °C között, se nap, se fagy", "Sötétben vagy árnyékban", "Szárazon, lehetőleg 35% pára alatt", "Zacskó zárva minden munka után", "A legrégebbi zacskók elöl: FIFO"],
    "client_body": "A minőség nem ér véget a raktárban. A Sempertex Europe kifogástalan állapotban szállít, a többi rajtad múlik: hűvös, száraz, sötét és zárt.",
    "cta_label": "Utánrendelés",
    "s3_cover_a": "Sempertex lufik tárolása", "s3_cover_b": "az autóban", "s3_cover_c": "vs.", "s3_cover_d": "a polcon",
    "s3_left": "AZ AUTÓBAN", "s3_right": "A POLCON", "s3_left_meta": "nap, meleg, nyitott zacskó", "s3_right_meta": "18 °C, sötét, zárva",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "RÉGI", "s3_new_lbl": "ÚJ",
    "s3_old_tags": ["Nyitott zacskó", "Ahol hely van"], "s3_new_tags": ["10 és 30 °C", "Sötét és száraz", "Zacskó zárva", "FIFO"],
    "s3_new_quote": "“Stabilan, sötétben, szárazon és zárva. És a legrégebbi zacskó megy először.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Ugyanazok a lufik, ugyanaz a beszállító.\nA szín még stimmel, amikor kinyitod a zacskót.",
    "s3_topic_lbl": "SZABÁLY", "s3_rule1_topic": "Hőmérséklet", "s3_rule1_old": "A latex sokat kibír",
    "s3_rule1_quote": "“Stabilan 10 és 30 °C között. Soha ne fagyaszd, soha ne napon. A Sempertex 18 °C-on tárol.”",
    "s3_rule2_topic": "Fény és pára", "s3_rule2_old": "Az a zacskó hónapok óta nyitva van, na és",
    "s3_rule2_quote": "“Az UV gyorsítja az oxidációt, 35% feletti pára penészt jelent. Sötét, száraz, és a zacskó zárva.”",
    "s3_example_lbl": "PÉLDA", "s3_example_quote": "“Négy zacskó a polcon: {p0}, {p1}, {p2}, {p3}. A legrégebbi elöl, zárva, naptól távol.”",
    "s3_client_lbl": "KOLLÉGA", "s3_client_topic": "A gyakorlatban",
    "s3_client_quote": "“Helyesen tárolva évekig jók maradnak. Egy nyár az autóban meglátszik a színen.”",
    "s3_cta_kicker": "A tárolási ellenőrzésed a következő szállításhoz",
    "sun_lbl": "nap", "shade_lbl": "árnyék", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
"lt": {
    "cover_pills": ["10 iki 30 °C…", "Max 35% drėgmė…", "FIFO…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Laikymo gidas…",
    "steps_title": "Lateksas išlieka geras metų metus, jei darai 5 dalykus.", "steps_lead": "5 laikymo taisyklės:",
    "steps": ["Stabili temperatūra nuo 10 iki 30 °C", "Tamsoje arba pavėsyje, niekada tiesioginėje saulėje", "Sausai: geriausia ne daugiau kaip 35% drėgmės", "Maišelis uždarytas, sandariai", "Keisk atsargas: seniausios pirmiausia (FIFO)"],
    "steps_label": "Pagrindai",
    "rule1_label": "1 taisyklė", "rule1_title": "Stabiliai nuo 10 iki 30 °C",
    "rule1_body": "Klimato kontrolės nereikia, tik kuo mažiau svyravimų. Sempertex Europe viską laiko 18 °C. Šiluma pagreitina šviesos, drėgmės ir oksidacijos žalą. Labai šaltas lateksas praranda elastingumą ir lengviau plyšta: niekada neužšaldyk, o po šaltos kelionės pirmiausia leisk sušilti iki kambario temperatūros.",
    "rule1_facts": [["10 iki 30 °C", "stabiliai, mažai svyravimų"], ["18 °C", "Sempertex Europe sandėlis"], ["0 °C", "niekada neužšaldyk"], ["kambario temp.", "pirma sušildyk, tada pūsk"]],
    "rule2_label": "2 taisyklė", "rule2_title": "Tamsu, sausa ir maišelis uždarytas",
    "rule2_body": "UV šviesa pagreitina latekso oksidaciją, o folijai ilga ryški šviesa gadina dažus ir metalinį blizgesį. Laikyk drėgmę žemą, geriausia ne aukščiau 35%: drėgmė ir prasta ventiliacija reiškia pelėsį visose atsargose. Laikyk sandariai ir atidarytą maišelį iškart vėl uždaryk. Į darbą imk tik tas spalvas, kurių reikia.",
    "rule2_cards": [["UV", "pavėsis, be tiesioginės saulės"], ["≤ 35%", "drėgmė, gerai vėdinama"], ["uždarytas", "sandariai, ir po atidarymo"]],
    "example_label": "Pavyzdys", "example_title": "Tavo atsargos lentynoje, pagal FIFO",
    "shelf_lbls": ["seniausias", "", "", "naujausias"],
    "example_body": "Keturi R12 maišeliai lentynoje: {p0}, {p1}, {p2} ir {p3}. Seniausias stovi priekyje ir pirmas keliauja į darbą, naujausias gale. Maišeliai uždaryti, atokiau nuo saulės, sausai. Taip spalvos atrodo taip, kaip turi, kai atidarai maišelį montuoti.",
    "client_label": "Praktikoje", "client_title": "Ką atsakai, kai kolega klausia",
    "client_answers": [
        "Tiesioginė saulė ir karštis pagreitina oksidaciją. Išimk juos iš automobilio, leisk pavėsyje sušilti iki kambario temperatūros ir išbandyk 2 prieš montuodamas. Kitą kartą: uždaroje dėžėje, atokiau nuo saulės.",
        "Atidarytas maišelis mėnesius būna veikiamas oro ir drėgmės. Uždaryk jį dabar, laikyk tamsoje ir sunaudok pirmiausia. Nauji maišeliai eina už jo: seniausi pirmiausia.",
        "Teisingai laikomi, tai yra stabiliai nuo 10 iki 30 °C, tamsoje, sausai ir sandariai, jie išlieka geri metų metus. Netinkamai laikomi, viena vasara automobilyje, ir tai matyti iš spalvos ir elastingumo.",
    ],
    "avoid_lead": "Tavo laikymo patikra, kiekvieno pristatymo metu:",
    "steps5": ["Stabiliai nuo 10 iki 30 °C, be saulės, be šalčio", "Tamsoje arba pavėsyje", "Sausai, geriausia ne daugiau kaip 35% drėgmės", "Maišelis uždarytas po kiekvieno darbo", "Seniausi maišeliai priekyje: FIFO"],
    "client_body": "Kokybė nesibaigia sandėlyje. Sempertex Europe pristato puikios būklės, visa kita priklauso nuo tavęs: vėsiai, sausai, tamsiai ir uždarytai.",
    "cta_label": "Papildyti atsargas",
    "s3_cover_a": "Sempertex balionų laikymas", "s3_cover_b": "automobilyje", "s3_cover_c": "vs.", "s3_cover_d": "lentynoje",
    "s3_left": "AUTOMOBILYJE", "s3_right": "LENTYNOJE", "s3_left_meta": "saulė, karštis, atidarytas maišelis", "s3_right_meta": "18 °C, tamsu, uždarytas",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "SENA", "s3_new_lbl": "NAUJA",
    "s3_old_tags": ["Atidarytas maišelis", "Kur yra vietos"], "s3_new_tags": ["10 iki 30 °C", "Tamsu ir sausa", "Maišelis uždarytas", "FIFO"],
    "s3_new_quote": "“Stabiliai, tamsoje, sausai ir uždarytai. O seniausias maišelis keliauja pirmas.”", "s3_new_badge": "Sempertex: 18 °C",
    "s3_changed_bottom": "Tie patys balionai, tas pats tiekėjas.\nSpalva vis dar teisinga, kai atidarai maišelį.",
    "s3_topic_lbl": "TAISYKLĖ", "s3_rule1_topic": "Temperatūra", "s3_rule1_old": "Lateksas daug ką atlaiko",
    "s3_rule1_quote": "“Stabiliai nuo 10 iki 30 °C. Niekada neužšaldyk, niekada saulėje. Sempertex laiko 18 °C.”",
    "s3_rule2_topic": "Šviesa ir drėgmė", "s3_rule2_old": "Tas maišelis atidarytas mėnesius, ir kas",
    "s3_rule2_quote": "“UV pagreitina oksidaciją, drėgmė virš 35% reiškia pelėsį. Tamsu, sausa ir maišelis uždarytas.”",
    "s3_example_lbl": "PAVYZDYS", "s3_example_quote": "“Keturi maišeliai lentynoje: {p0}, {p1}, {p2}, {p3}. Seniausias priekyje, uždarytas, atokiau nuo saulės.”",
    "s3_client_lbl": "KOLEGA", "s3_client_topic": "Praktikoje",
    "s3_client_quote": "“Teisingai laikomi jie išlieka geri metų metus. Viena vasara automobilyje matyti iš spalvos.”",
    "s3_cta_kicker": "Tavo laikymo patikra kitam pristatymui",
    "sun_lbl": "saulė", "shade_lbl": "pavėsis", "van_temp": "34 °C", "shelf_temp": "18 °C", "fifo_lbl": "FIFO",
},
}

# ---------------------------------------------------------------- VARIANTEN
VARIANTS = {
"nl": {
  "cover_title": ["Zo bewaar je je Sempertex ballonnen: 10 tot 30 °C, donker, droog en de zak dicht", "Sempertex bewaart alles op 18 °C. Dit zijn de 5 regels voor je eigen stock", "Ballonnen die jaren goed blijven: de 5 bewaarregels voor Sempertex latex"],
  "cover_sub": ["Temperatuur, licht, vocht, verpakking en rotatie, uit de Sempertex blog. Vijf regels die je morgen in je magazijn toepast.", "Een zomer in de bestelwagen zie je aan de kleur. Deze 5 regels houden je voorraad in de staat waarin hij geleverd werd."],
  "client_question": ["Mijn ballonnen lagen een dag in de bestelwagen in de zon. Kan ik ze nog gebruiken?", "Ik heb een zak van vorig jaar open laten staan. Weggooien?", "Hoe lang blijven ballonnen eigenlijk goed?"],
  "s3_old_quote": ["“Latex gaat toch niet kapot”", "“In de zon drogen ze gewoon sneller”", "“Ik pak gewoon de bovenste zak”"],
  "s3_client_old": ["“Van vorig jaar? Gaat wel”", "“Die zak staat al maanden open, wat zou het”"],
  "cta_title_tpl": "Bestel je Sempertex ballonnen bij {name}", "cta_sub_generic": "Vul je stock aan en zet de nieuwe zakken achteraan.",
},
"en": {
  "cover_title": ["How to store your Sempertex balloons: 10 to 30 °C, dark, dry and the bag closed", "Sempertex stores everything at 18 °C. These are the 5 rules for your own stock", "Balloons that stay good for years: the 5 storage rules for Sempertex latex"],
  "cover_sub": ["Temperature, light, humidity, packaging and rotation, from the Sempertex blog. Five rules you can apply in your stockroom tomorrow.", "A summer in the van shows in the colour. These 5 rules keep your stock in the condition it was delivered in."],
  "client_question": ["My balloons sat in the van in the sun for a day. Can I still use them?", "I left a bag from last year open. Bin it?", "How long do balloons actually stay good?"],
  "s3_old_quote": ["“Latex doesn't go off anyway”", "“They just dry faster in the sun”", "“I just grab the top bag”"],
  "s3_client_old": ["“From last year? It'll be fine”", "“That bag's been open for months, so what”"],
  "cta_title_tpl": "Order your Sempertex balloons at {name}", "cta_sub_generic": "Restock and put the new bags at the back.",
},
"de": {
  "cover_title": ["So lagerst du deine Sempertex Ballons: 10 bis 30 °C, dunkel, trocken und Beutel zu", "Sempertex lagert alles bei 18 °C. Das sind die 5 Regeln für deinen eigenen Bestand", "Ballons, die jahrelang gut bleiben: die 5 Lagerregeln für Sempertex Latex"],
  "cover_sub": ["Temperatur, Licht, Feuchte, Verpackung und Rotation, aus dem Sempertex Blog. Fünf Regeln, die du morgen in deinem Lager umsetzt.", "Einen Sommer im Transporter sieht man an der Farbe. Diese 5 Regeln halten deinen Bestand im Zustand, in dem er geliefert wurde."],
  "client_question": ["Meine Ballons lagen einen Tag im Transporter in der Sonne. Kann ich sie noch nutzen?", "Ich habe einen Beutel vom letzten Jahr offen stehen lassen. Wegwerfen?", "Wie lange bleiben Ballons eigentlich gut?"],
  "s3_old_quote": ["“Latex geht doch nicht kaputt”", "“In der Sonne trocknen sie einfach schneller”", "“Ich nehme einfach den obersten Beutel”"],
  "s3_client_old": ["“Vom letzten Jahr? Geht schon”", "“Der Beutel ist seit Monaten offen, na und”"],
  "cta_title_tpl": "Bestell deine Sempertex Ballons bei {name}", "cta_sub_generic": "Füll deinen Bestand auf und stell die neuen Beutel nach hinten.",
},
"fr": {
  "cover_title": ["Comment stocker tes ballons Sempertex : 10 à 30 °C, au noir, au sec et sachet fermé", "Sempertex stocke tout à 18 °C. Voici les 5 règles pour ton propre stock", "Des ballons qui restent bons des années : les 5 règles de stockage du latex Sempertex"],
  "cover_sub": ["Température, lumière, humidité, emballage et rotation, tirés du blog Sempertex. Cinq règles à appliquer dès demain dans ta réserve.", "Un été dans le camion, ça se voit à la couleur. Ces 5 règles gardent ton stock dans l'état où il a été livré."],
  "client_question": ["Mes ballons sont restés une journée dans le camion au soleil. Je peux encore les utiliser ?", "J'ai laissé un sachet de l'an dernier ouvert. Je jette ?", "Combien de temps les ballons restent-ils bons ?"],
  "s3_old_quote": ["“Le latex, ça ne s'abîme pas”", "“Au soleil, ils sèchent juste plus vite”", "“Je prends le sachet du dessus”"],
  "s3_client_old": ["“De l'an dernier ? Ça ira”", "“Ce sachet est ouvert depuis des mois, et alors”"],
  "cta_title_tpl": "Commande tes ballons Sempertex chez {name}", "cta_sub_generic": "Refais ton stock et mets les nouveaux sachets derrière.",
},
"it": {
  "cover_title": ["Come conservare i tuoi palloncini Sempertex: 10 a 30 °C, buio, asciutto e busta chiusa", "Sempertex conserva tutto a 18 °C. Queste sono le 5 regole per il tuo stock", "Palloncini che restano buoni per anni: le 5 regole di conservazione del lattice Sempertex"],
  "cover_sub": ["Temperatura, luce, umidità, confezione e rotazione, dal blog Sempertex. Cinque regole da applicare domani nel tuo magazzino.", "Un'estate nel furgone si vede dal colore. Queste 5 regole tengono il tuo stock nello stato in cui è stato consegnato."],
  "client_question": ["I miei palloncini sono rimasti un giorno nel furgone al sole. Posso ancora usarli?", "Ho lasciato aperta una busta dell'anno scorso. La butto?", "Quanto restano buoni i palloncini?"],
  "s3_old_quote": ["“Il lattice non si rovina mica”", "“Al sole si asciugano solo più in fretta”", "“Prendo la busta in cima e via”"],
  "s3_client_old": ["“Dell'anno scorso? Va bene lo stesso”", "“Quella busta è aperta da mesi, e allora”"],
  "cta_title_tpl": "Ordina i tuoi palloncini Sempertex da {name}", "cta_sub_generic": "Rifornisci lo stock e metti le buste nuove dietro.",
},
"pl": {
  "cover_title": ["Jak przechowywać balony Sempertex: 10 do 30 °C, ciemno, sucho i torebka zamknięta", "Sempertex przechowuje wszystko w 18 °C. Oto 5 zasad dla twojego zapasu", "Balony, które zostają dobre przez lata: 5 zasad przechowywania lateksu Sempertex"],
  "cover_sub": ["Temperatura, światło, wilgoć, opakowanie i rotacja, z bloga Sempertex. Pięć zasad do wdrożenia jutro w magazynie.", "Jedno lato w aucie widać po kolorze. Te 5 zasad utrzymuje zapas w stanie, w jakim został dostarczony."],
  "client_question": ["Moje balony leżały dzień w aucie na słońcu. Mogę ich jeszcze użyć?", "Zostawiłam otwartą torebkę z zeszłego roku. Wyrzucić?", "Jak długo balony w ogóle zostają dobre?"],
  "s3_old_quote": ["“Lateks się przecież nie psuje”", "“Na słońcu po prostu szybciej schną”", "“Biorę po prostu torebkę z wierzchu”"],
  "s3_client_old": ["“Z zeszłego roku? Będzie dobrze”", "“Ta torebka jest otwarta od miesięcy, i co z tego”"],
  "cta_title_tpl": "Zamów balony Sempertex w {name}", "cta_sub_generic": "Uzupełnij zapas i postaw nowe torebki z tyłu.",
},
"el": {
  "cover_title": ["Έτσι αποθηκεύεις τα μπαλόνια Sempertex: 10 έως 30 °C, σκοτεινά, στεγνά και σακούλα κλειστή", "Η Sempertex αποθηκεύει τα πάντα στους 18 °C. Αυτοί είναι οι 5 κανόνες για το δικό σου απόθεμα", "Μπαλόνια που μένουν καλά για χρόνια: οι 5 κανόνες αποθήκευσης για latex Sempertex"],
  "cover_sub": ["Θερμοκρασία, φως, υγρασία, συσκευασία και εναλλαγή, από το blog της Sempertex. Πέντε κανόνες που εφαρμόζεις αύριο στην αποθήκη σου.", "Ένα καλοκαίρι στο αυτοκίνητο φαίνεται στο χρώμα. Αυτοί οι 5 κανόνες κρατούν το απόθεμά σου στην κατάσταση που παραδόθηκε."],
  "client_question": ["Τα μπαλόνια μου έμειναν μια μέρα στο αυτοκίνητο στον ήλιο. Μπορώ να τα χρησιμοποιήσω;", "Άφησα μια σακούλα από πέρυσι ανοιχτή. Την πετάω;", "Πόσο καιρό μένουν καλά τα μπαλόνια;"],
  "s3_old_quote": ["“Το latex δεν χαλάει έτσι κι αλλιώς”", "“Στον ήλιο απλά στεγνώνουν πιο γρήγορα”", "“Παίρνω απλά την πάνω σακούλα”"],
  "s3_client_old": ["“Από πέρυσι; Μια χαρά είναι”", "“Αυτή η σακούλα είναι ανοιχτή μήνες, και τι έγινε”"],
  "cta_title_tpl": "Παράγγειλε τα μπαλόνια Sempertex σου από {name}", "cta_sub_generic": "Ανανέωσε το απόθεμα και βάλε τις νέες σακούλες πίσω.",
},
"hu": {
  "cover_title": ["Így tárold a Sempertex lufijaidat: 10 és 30 °C között, sötétben, szárazon, zárt zacskóban", "A Sempertex mindent 18 °C-on tárol. Ez az 5 szabály a saját készletedhez", "Lufik, amik évekig jók maradnak: az 5 tárolási szabály a Sempertex latexhez"],
  "cover_sub": ["Hőmérséklet, fény, pára, csomagolás és forgatás, a Sempertex blogból. Öt szabály, amit holnap bevezetsz a raktáradban.", "Egy nyár az autóban meglátszik a színen. Ez az 5 szabály abban az állapotban tartja a készleted, ahogy megérkezett."],
  "client_question": ["A lufijaim egy napig az autóban voltak a napon. Használhatom még őket?", "Nyitva hagytam egy tavalyi zacskót. Kidobjam?", "Meddig maradnak jók a lufik egyáltalán?"],
  "s3_old_quote": ["“A latex úgysem megy tönkre”", "“A napon csak gyorsabban száradnak”", "“Egyszerűen a legfelső zacskót veszem”"],
  "s3_client_old": ["“Tavalyi? Jó lesz az”", "“Az a zacskó hónapok óta nyitva van, na és”"],
  "cta_title_tpl": "Rendeld a Sempertex lufijaidat innen: {name}", "cta_sub_generic": "Töltsd fel a készleted, és tedd az új zacskókat hátra.",
},
"lt": {
  "cover_title": ["Kaip laikyti Sempertex balionus: 10 iki 30 °C, tamsiai, sausai ir uždarytame maišelyje", "Sempertex viską laiko 18 °C. Štai 5 taisyklės tavo atsargoms", "Balionai, kurie išlieka geri metų metus: 5 Sempertex latekso laikymo taisyklės"],
  "cover_sub": ["Temperatūra, šviesa, drėgmė, pakuotė ir rotacija iš Sempertex tinklaraščio. Penkios taisyklės, kurias rytoj pritaikysi savo sandėlyje.", "Viena vasara automobilyje matyti iš spalvos. Šios 5 taisyklės išlaiko atsargas tokios būklės, kokios jos buvo pristatytos."],
  "client_question": ["Mano balionai dieną gulėjo automobilyje saulėje. Ar dar galiu juos naudoti?", "Palikau atidarytą pernykštį maišelį. Išmesti?", "Kiek laiko balionai apskritai išlieka geri?"],
  "s3_old_quote": ["“Lateksas juk nesugenda”", "“Saulėje jie tiesiog greičiau džiūsta”", "“Tiesiog imu viršutinį maišelį”"],
  "s3_client_old": ["“Pernykščiai? Tiks”", "“Tas maišelis atidarytas mėnesius, ir kas”"],
  "cta_title_tpl": "Užsisakyk Sempertex balionus iš {name}", "cta_sub_generic": "Papildyk atsargas ir naujus maišelius padėk gale.",
},
}

CAPTIONS_TPL = {
 "nl": "Latex blijft jaren goed, als je 5 dingen doet: stabiel tussen 10 en 30 °C (Sempertex Europe bewaart op 18 °C), donker, droog met max 35% vocht, zak dicht en FIFO. In deze carousel: de 5 regels, waarom koud en warm allebei kwaad kunnen, en wat je doet met een zak die een dag in de zon lag.\n\nBestel je Sempertex ballonnen bij {domain}.\n\n#ballonnenbewaren #sempertex #{tag} #ballondecoratie #ballonnen #ballonartiest",
 "en": "Latex stays good for years, if you do 5 things: stable between 10 and 30 °C (Sempertex Europe stores at 18 °C), dark, dry with max 35% humidity, bag closed and FIFO. In this carousel: the 5 rules, why cold and heat both do harm, and what to do with a bag that sat in the sun for a day.\n\nOrder your Sempertex balloons at {domain}.\n\n#balloonstorage #sempertex #{tag} #balloondecor #balloons #balloonartist",
 "de": "Latex bleibt jahrelang gut, wenn du 5 Dinge tust: stabil zwischen 10 und 30 °C (Sempertex Europe lagert bei 18 °C), dunkel, trocken mit max. 35% Feuchte, Beutel zu und FIFO. Im Carousel: die 5 Regeln, warum Kälte und Hitze beide schaden, und was du mit einem Beutel machst, der einen Tag in der Sonne lag.\n\nBestell deine Sempertex Ballons bei {domain}.\n\n#ballonslagern #sempertex #{tag} #ballondeko #ballons #ballonkünstler",
 "fr": "Le latex reste bon des années, si tu fais 5 choses : stable entre 10 et 30 °C (Sempertex Europe stocke à 18 °C), au noir, au sec avec max 35 % d'humidité, sachet fermé et FIFO. Dans ce carrousel : les 5 règles, pourquoi le froid et la chaleur font tous deux des dégâts, et quoi faire d'un sachet resté une journée au soleil.\n\nCommande tes ballons Sempertex chez {domain}.\n\n#stockageballons #sempertex #{tag} #decorationballons #ballons #artisteballon",
 "it": "Il lattice resta buono per anni, se fai 5 cose: stabile tra 10 e 30 °C (Sempertex Europe conserva a 18 °C), buio, asciutto con max 35% di umidità, busta chiusa e FIFO. Nel carosello: le 5 regole, perché freddo e caldo fanno entrambi danni, e cosa fare con una busta rimasta un giorno al sole.\n\nOrdina i tuoi palloncini Sempertex da {domain}.\n\n#conservazionepalloncini #sempertex #{tag} #palloncini #decorazioni #balloonartist",
 "pl": "Lateks zostaje dobry przez lata, jeśli zrobisz 5 rzeczy: stabilnie między 10 a 30 °C (Sempertex Europe przechowuje w 18 °C), ciemno, sucho z max 35% wilgotności, torebka zamknięta i FIFO. W karuzeli: 5 zasad, dlaczego zimno i ciepło oba szkodzą, i co zrobić z torebką, która dzień leżała na słońcu.\n\nZamów balony Sempertex w {domain}.\n\n#przechowywaniebalonow #sempertex #{tag} #dekoracjebalonowe #balony #artystabalonowy",
 "el": "Το latex μένει καλό για χρόνια, αν κάνεις 5 πράγματα: σταθερά μεταξύ 10 και 30 °C (η Sempertex Europe αποθηκεύει στους 18 °C), σκοτεινά, στεγνά με max 35% υγρασία, σακούλα κλειστή και FIFO. Στο carousel: οι 5 κανόνες, γιατί κρύο και ζέστη κάνουν και τα δύο ζημιά, και τι κάνεις με μια σακούλα που έμεινε μια μέρα στον ήλιο.\n\nΠαράγγειλε τα μπαλόνια Sempertex σου από {domain}.\n\n#αποθηκευσημπαλονιων #sempertex #{tag} #μπαλονια #balloonartist",
 "hu": "A latex évekig jó marad, ha 5 dolgot megteszel: stabilan 10 és 30 °C között (a Sempertex Europe 18 °C-on tárol), sötétben, szárazon max 35% párával, zárt zacskóban és FIFO szerint. A carouselben: az 5 szabály, miért árt a hideg és a meleg is, és mit tegyél egy zacskóval, ami egy napig a napon volt.\n\nRendeld a Sempertex lufijaidat innen: {domain}.\n\n#lufitarolas #sempertex #{tag} #lufidekoracio #lufi #lufiművész",
 "lt": "Lateksas išlieka geras metų metus, jei darai 5 dalykus: stabiliai nuo 10 iki 30 °C (Sempertex Europe laiko 18 °C), tamsiai, sausai su max 35% drėgme, uždarytame maišelyje ir pagal FIFO. Karuselėje: 5 taisyklės, kodėl kenkia ir šaltis, ir karštis, ir ką daryti su maišeliu, kuris dieną gulėjo saulėje.\n\nUžsisakyk Sempertex balionus iš {domain}.\n\n#balionulaikymas #sempertex #{tag} #balionai #balionumenininkas",
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

def facts_grid(items, cls="facts", num_size=46, lab_size=20):
    esc = G["esc"]
    def fs(n):
        L = len(n); return num_size if L <= 9 else (int(num_size * .76) if L <= 14 else int(num_size * .62))
    cells = "".join(f'<div class="fact"><b style="font-size:{fs(n)}px">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>' for n, l in items)
    return f'<div class="{cls}">{cells}</div>'

def rules3(c, cls="facts three", num_size=46, lab_size=19):
    """UV (doorgestreept) / ≤ 35% / zak dicht."""
    esc = G["esc"]; items = c["rule2_cards"]; out = f'<div class="{cls}">'
    for i, (n, l) in enumerate(items):
        style = "text-decoration:line-through;text-decoration-color:#E03131;text-decoration-thickness:5px" if i == 0 else ""
        out += f'<div class="fact"><b style="font-size:{num_size}px;{style}">{esc(n)}</b><span style="font-size:{lab_size}px">{esc(l)}</span></div>'
    return out + '</div>'

def shelf_row(c, P, size=120, lab=19, ink="#111", gap=26):
    """4 zakken op een plank: ballon + naam/code, 'oudste' vooraan en 'nieuwste' achteraan."""
    esc = G["esc"]; out = '<div style="display:flex;flex-direction:column;align-items:center;width:100%">'
    out += f'<div style="display:flex;align-items:flex-end;justify-content:center;gap:{gap}px">'
    for i, k in enumerate(P[:4]):
        tag = c["shelf_lbls"][i]
        tagh = f'<div style="font-size:16px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:{ink};opacity:.6;margin-bottom:8px;height:20px">{esc(tag)}</div>'
        out += (f'<div style="text-align:center">{tagh}<div class="bag">{_bl(k, size)}</div>'
                f'<div class="pname" style="font-size:{lab}px;margin-top:10px;color:{ink};white-space:nowrap">{esc(G["pal_label"](k))}</div></div>')
    out += '</div>'
    out += f'<div style="width:96%;height:10px;background:{ink};border-radius:4px;margin-top:-4px;opacity:.9"></div>'
    out += f'<div style="font-size:18px;font-weight:800;letter-spacing:.1em;color:{ink};opacity:.6;margin-top:10px">{esc(c["fifo_lbl"])} →</div>'
    return out + '</div>'

def avoid_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

def sun_svg(size=90, color="#F2B21D"):
    rays = "".join(f'<line x1="50" y1="4" x2="50" y2="18" stroke="{color}" stroke-width="7" stroke-linecap="round" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45))
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}"><circle cx="50" cy="50" r="22" fill="{color}"/>{rays}</svg>'

def in_the_van(keys, c, ink="#111"):
    """'In de bestelwagen': ballonnen kriskras, zon, open zak, 34 °C."""
    esc = G["esc"]; w, h = 330, 360
    pos = [(10, 60, 92), (110, 40, 84), (200, 70, 96), (40, 170, 88), (150, 160, 104), (250, 190, 80), (90, 260, 92), (200, 260, 84)]
    out = f'<div style="position:relative;width:{w}px;height:{h}px">'
    out += f'<div style="position:absolute;left:230px;top:-10px">{sun_svg(96)}</div>'
    for i, (x, y, s) in enumerate(pos):
        out += f'<div style="position:absolute;left:{x}px;top:{y}px">{_bl(keys[i % len(keys)], s)}</div>'
    out += (f'<div style="position:absolute;left:10px;top:0;transform:rotate(-8deg);background:#fff;color:#E03131;border:3px solid {ink};'
            f'border-radius:10px;padding:6px 14px;font-size:26px;font-weight:900;box-shadow:0 4px 0 rgba(0,0,0,.18)">{esc(c["van_temp"])}</div>')
    return out + '</div>'

def on_the_shelf(keys, c, ink="#111"):
    """'Op de plank': 4 ballonnen netjes op een plank, 18 °C, FIFO."""
    esc = G["esc"]
    row = "".join(f'<div class="bag" style="margin:0 2px">{_bl(k, 72)}</div>' for k in keys[:4])
    return (f'<div style="position:relative;width:330px;height:370px">'
            f'<div style="position:absolute;left:0;top:70px;width:330px;display:flex;align-items:flex-end;justify-content:center">{row}</div>'
            f'<div style="position:absolute;left:10px;top:182px;width:310px;height:10px;background:{ink};border-radius:4px"></div>'
            f'<div style="position:absolute;left:0;top:220px;width:330px;display:flex;align-items:flex-end;justify-content:center">{row}</div>'
            f'<div style="position:absolute;left:10px;top:332px;width:310px;height:10px;background:{ink};border-radius:4px"></div>'
            f'<div style="position:absolute;left:10px;top:0;transform:rotate(-6deg);background:#fff;color:{ink};border:3px solid {ink};border-radius:10px;padding:6px 14px;font-size:26px;font-weight:900;box-shadow:0 4px 0 rgba(0,0,0,.18)">{esc(c["shelf_temp"])}</div>'
            f'<div style="position:absolute;right:10px;top:0;transform:rotate(5deg);background:{ink};color:#fff;border-radius:10px;padding:8px 14px;font-size:20px;font-weight:900;letter-spacing:.08em">{esc(c["fifo_lbl"])}</div></div>')

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
  <div class="box" style="left:70px;top:120px;width:800px;height:500px">
    <h2 data-fit style="font-size:78px;max-height:400px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:830px;top:90px;transform:rotate(14deg)">{balloon(b['hero'], 'fashion', 180)}</div>
  <div style="position:absolute;left:120px;top:630px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:660px;width:710px;height:500px;padding:36px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:460px;padding:44px 50px">
    <h2 data-fit style="font-size:60px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:27px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:690px;height:420px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:390px;padding:30px 34px">{facts_grid(c['rule1_facts'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:480px;padding:44px 50px">
    <h2 data-fit style="font-size:58px;max-height:150px">{esc(c['rule2_title'])}</h2>
    <div class="body" style="margin-top:22px;font-size:27px">{esc(c['rule2_body'])}</div>
  </div>
  <div class="stack" style="top:710px;height:400px">
    <div class="card" style="top:0;height:320px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:360px;padding:30px 34px;display:flex;align-items:center">{rules3(c)}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:560px;padding:40px 30px 36px">
    <h2 data-fit style="font-size:52px;margin-bottom:30px;text-align:center;max-height:120px">{esc(c['example_title'])}</h2>
    {shelf_row(c, P, 150, 19, b['ink'], 30)}
  </div>
  <div class="box" style="left:70px;top:770px;width:940px;padding:32px 50px"><div class="body" style="font-size:27px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:130px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:490px;display:flex;flex-direction:column;gap:20px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:26px 36px"><div style="font-size:27px;line-height:1.35">{esc(c['client_answer'])}</div></div>
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
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:66px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box"><div style="transform:scale(1.1)">{on_the_shelf(P, c, '#111')}</div></div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px;font-size:27px"><b style="font-size:36px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:700px;width:560px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:340px;padding:10px;box-sizing:border-box"><div style="transform:scale(.85)">{in_the_van(P, c, '#111')}</div></div>
  </div>
  <div class="frame" style="left:600px;top:820px;width:410px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:260px;padding:10px;box-sizing:border-box"><div style="transform:scale(.8)">{balloon(b['hero'], 'fashion', 150)}</div></div>
  </div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:60px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:400px;padding:26px 30px;box-sizing:border-box;align-items:stretch;background:#fff">{facts_grid(c['rule1_facts'], 'facts onwhite')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:860px;font-size:26px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:170px">{esc(c['rule2_title'])}</h2>
  <div class="frame" style="left:70px;top:370px;width:940px;transform:rotate({rot(b,1.5)}deg)">
    <div class="ph" style="height:340px;padding:26px 30px;box-sizing:border-box;align-items:center;background:#fff">{rules3(c, 'facts three onwhite')}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:820px;font-size:26px">{esc(c['rule2_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:58px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:470px;padding:24px 30px;box-sizing:border-box;align-items:center;background:#fff">{shelf_row(c, P, 120, 18, '#111', 26)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:890px;font-size:26px">{esc(c['example_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:56px;max-height:150px">{esc(c['client_title'])}</h2>
  <div class="frame" style="left:70px;top:340px;width:940px">
    <div class="ph" style="height:auto;padding:28px 34px;box-sizing:border-box;align-items:flex-start;background:#fff">
      <div style="font-size:29px;line-height:1.3;color:{b['ink']};font-style:italic">{esc(c['client_question'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:14px 0"></div>
      <div style="font-size:24px;line-height:1.35;color:{b['ink']}">{esc(c['client_answer'])}</div>
      <div style="width:100%;height:2px;background:{b['tint']};margin:14px 0"></div>
      <div style="font-size:22px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['avoid_lead'])}</div>
      {avoid_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:1070px;font-size:23px">{esc(c['client_body'])}</div>
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
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{in_the_van(loud, c, b['ink'])}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{on_the_shelf(P, c, b['ink'])}</div>
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
    vis1 = f'<div style="width:100%">{facts_grid(c["rule1_facts"], "facts s3facts", 34, 17)}</div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="width:100%">{rules3(c, "facts s3facts", 34, 17)}</div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    t = c['example_title']
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v" style="font-size:{44 if len(t) <= 24 else (36 if len(t) <= 30 else 30)}px">{esc(t)}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:620px;padding:40px 30px;display:flex;align-items:center;justify-content:center">
    {shelf_row(c, P, 130, 19, "#111", 26)}
  </div>
  <div class="bottom" style="top:910px;font-size:31px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    vis6 = (f'<div style="width:100%"><div style="font-size:22px;line-height:1.3;font-style:italic;margin-bottom:12px">{esc(c["client_question"])}</div>'
            f'<div style="font-size:18px;line-height:1.3;margin-bottom:14px">{esc(c["client_answer"])}</div>'
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
.s1 .step{font-size:26px;margin-top:10px}
.s1 .avoid .step{font-size:24px;margin-top:9px;line-height:1.25}
.s2 .onwhite .step{color:#111;font-size:21px;margin-top:7px;line-height:1.25}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:10px;font-size:17px;line-height:1.25;margin-top:6px}
.s3 .s3steps .step b{min-width:24px;font-weight:800}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.facts.three{grid-template-columns:1fr 1fr 1fr;gap:16px}
.facts .fact{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:3px solid #111;border-radius:18px;padding:16px 12px;gap:6px;line-height:1.15}
.facts .fact b{letter-spacing:-.01em;line-height:1;white-space:nowrap}
.facts.onwhite .fact{color:#111}
.facts.s3facts{grid-template-columns:1fr;gap:12px}
.facts.s3facts .fact{border-width:2px;padding:10px 14px;border-radius:14px;align-items:flex-start;text-align:left;gap:3px}
.facts.s3facts .fact b{white-space:normal}
.bag{display:inline-block;padding:10px 10px 6px;border:3px dashed rgba(0,0,0,.35);border-radius:14px;background:rgba(255,255,255,.55)}
"""
