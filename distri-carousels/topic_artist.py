# -*- coding: utf-8 -*-
"""Topic: 'How to become a balloon artist' (sempertexeurope.com/blog/how-to-become-a-balloon-artist).
Copy in 9 talen + varianten + slide-templates voor de 3 stijlen. Wordt door build.py geladen met --topic=artist."""

G = {}  # wordt gevuld door build.setup(): helpers en constanten uit build.py
def setup(g): G.update(g)

# ---------------------------------------------------------------- COPY
BASE = {
"nl": {
    "cover_pills": ["Basis…", "Duplet…", "Oefenen…"], "cover_with": "met", "cover_brand": "Sempertex Europe", "cover_tag": "Startersgids…",
    "steps_title": "Ballonartiest worden hangt af van 3 dingen.", "steps_lead": "De 3 dingen:",
    "steps": ["Een goede basisopleiding", "Begrijpen hoe latex zich gedraagt: oxidatie, wrijving, warmte en kou", "Gericht oefenen op een paar kernbouwsels, tot het automatisch gaat"],
    "steps_label": "De basis",
    "rule1_label": "Skill 1 en 2", "rule1_title": "Ken je materiaal en knoop strak",
    "rule1_body": "Losjes knopen is de meest gemaakte fout, ook bij ervaren artiesten. De duplet is de basis van elke compositie. Zit die strak, dan is alles wat je erop bouwt stabiel.",
    "rule1_tags": ["duplet", "cluster"],
    "rule2_label": "Skill 3 en 4", "rule2_title": "Bouw veilig en ontwerp bewust",
    "rule2_body": "Gewicht, spanning, bevestigingspunten en ondergrond werken op elkaar in, zeker bij grote installaties. Let daarnaast op kleurcombinaties, verhouding en balans. Voelt het niet goed, dan is het niet af.",
    "rule2_tags": ["groot", "klein", "groot", "klein", "groot"],
    "example_label": "Oefenset", "example_title": "Je eerste oefenweek",
    "example_body": "Duplet: R12 {p0} + R12 {p1}. Cluster: voeg {p2} en {p3} toe. Ballonhond: een 260 in Red 015. Elke kleur heeft een vaste naam en code, dus je bestelt exact wat je oefende.",
    "roles": ["duplet", "duplet", "cluster", "cluster"], "dog_label": "260 Red 015",
    "client_label": "Je ideale klant", "client_title": "Schrijf in één zin wie je ideale klant is",
    "client_body": "Die ene zin bepaalt wat je oefent en aan wie je je werk toont. Begin met een echte basiscursus, kijk gratis tutorials in je vrije tijd en oefen duplets en clusters tot je ze blind kunt. Sempertex Europe geeft de 2-daagse workshop Start Your Balloon Business.",
    "client_answer": "Je eerste 5 stappen:",
    "steps5": ["Boek een echte basiscursus", "Oefen duplets en clusters tot je ze blind kunt", "Maak een ballonhond, en dan nog één met andere verhoudingen", "Onderzoek de maten en hoe latex gemaakt wordt", "Schrijf die ene zin over je ideale klant"],
    "cta_label": "Starten",
    "s3_cover_a": "Ballonartiest worden met Sempertex", "s3_cover_b": "op talent", "s3_cover_c": "vs.", "s3_cover_d": "met oefening",
    "s3_left": "OP TALENT", "s3_right": "MET OEFENING", "s3_left_meta": "losse knopen", "s3_right_meta": "strakke duplets",
    "s3_changed_title": "Wat verandert er?", "s3_old_lbl": "OUD", "s3_new_lbl": "NIEUW",
    "s3_old_tags": ["Op talent", "Alleen YouTube"], "s3_new_tags": ["Basis", "Duplet", "Oefenen"],
    "s3_new_quote": "“Eerst een basisworkshop, dan duplets tot je ze blind kunt, dan pas echte klanten”", "s3_new_badge": "4 skills",
    "s3_changed_bottom": "Zelfde ballonnen, zelfde handen.\nDe basis komt eerst.",
    "s3_topic_lbl": "SKILL", "s3_rule1_topic": "Knopen", "s3_rule1_old": "Losjes knopen gaat sneller",
    "s3_rule1_quote": "“Losjes knopen is de meest gemaakte fout. Een strakke duplet maakt alles erop stabiel.”",
    "s3_rule2_topic": "Bouwen", "s3_rule2_old": "Als het mooi is, is het af",
    "s3_rule2_quote": "“Gewicht, spanning, bevestiging en ondergrond werken op elkaar in. Voelt het niet goed, dan is het niet af.”",
    "s3_example_lbl": "OEFENSET", "s3_example_quote": "“Duplet met {p0} en {p1}, cluster met {p2} en {p3}, ballonhond met een 260 Red 015.”",
    "s3_client_lbl": "KLANT", "s3_client_topic": "Je ideale klant",
    "s3_client_quote": "“Eén zin over je ideale klant bepaalt wat je oefent en aan wie je je werk toont.”",
    "s3_cta_kicker": "Je startset voor deze week",
},
"en": {
    "cover_pills": ["Basics…", "Duplet…", "Practice…"], "cover_with": "with", "cover_brand": "Sempertex Europe", "cover_tag": "Starter guide…",
    "steps_title": "Becoming a balloon artist comes down to 3 things.", "steps_lead": "The 3 things:",
    "steps": ["Solid foundation training", "Understanding how latex behaves: oxidation, friction, heat and cold", "Focused practice on a few core builds, until it runs on autopilot"],
    "steps_label": "The foundation",
    "rule1_label": "Skills 1 and 2", "rule1_title": "Know your material and tie it tight",
    "rule1_body": "Loose tying is the most common mistake, even among experienced artists. The duplet is the base of every composition. Tie it right and everything you build on it stays stable.",
    "rule1_tags": ["duplet", "cluster"],
    "rule2_label": "Skills 3 and 4", "rule2_title": "Build it safe and design it on purpose",
    "rule2_body": "Weight, tension, attachment points and substrate all interact, especially on larger installations. Then look at colour combinations, proportion and balance. If it doesn't feel right, it isn't finished.",
    "rule2_tags": ["large", "small", "large", "small", "large"],
    "example_label": "Practice kit", "example_title": "Your first practice week",
    "example_body": "Duplet: R12 {p0} + R12 {p1}. Cluster: add {p2} and {p3}. Balloon dog: a 260 in Red 015. Every colour has a fixed name and code, so you order exactly what you practised.",
    "roles": ["duplet", "duplet", "cluster", "cluster"], "dog_label": "260 Red 015",
    "client_label": "Your ideal client", "client_title": "Write one sentence about who your ideal client is",
    "client_body": "That one sentence decides what you practise and who you show your work to. Book a real basics course, watch free tutorials in your spare time and practise duplets and clusters until you can do them with your eyes closed. Sempertex Europe runs the 2-day workshop Start Your Balloon Business.",
    "client_answer": "Your first 5 steps:",
    "steps5": ["Book a real basics course", "Practise duplets and clusters until you can do them blind", "Make a balloon dog, then another with different proportions", "Research the sizes and how latex is made", "Write that one sentence about your ideal client"],
    "cta_label": "Get started",
    "s3_cover_a": "Becoming a balloon artist with Sempertex", "s3_cover_b": "on talent", "s3_cover_c": "vs.", "s3_cover_d": "with practice",
    "s3_left": "ON TALENT", "s3_right": "WITH PRACTICE", "s3_left_meta": "loose knots", "s3_right_meta": "tight duplets",
    "s3_changed_title": "What changed?", "s3_old_lbl": "OLD", "s3_new_lbl": "NEW",
    "s3_old_tags": ["On talent", "YouTube only"], "s3_new_tags": ["Basics", "Duplet", "Practice"],
    "s3_new_quote": "“A basics workshop first, then duplets until you can do them blind, then real clients”", "s3_new_badge": "4 skills",
    "s3_changed_bottom": "Same balloons, same hands.\nThe basics come first.",
    "s3_topic_lbl": "SKILL", "s3_rule1_topic": "Tying", "s3_rule1_old": "Loose tying is faster",
    "s3_rule1_quote": "“Loose tying is the most common mistake. A tight duplet keeps everything on it stable.”",
    "s3_rule2_topic": "Building", "s3_rule2_old": "If it looks nice, it's done",
    "s3_rule2_quote": "“Weight, tension, attachment and substrate interact. If it doesn't feel right, it isn't finished.”",
    "s3_example_lbl": "PRACTICE KIT", "s3_example_quote": "“Duplet with {p0} and {p1}, cluster with {p2} and {p3}, balloon dog with a 260 Red 015.”",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Your ideal client",
    "s3_client_quote": "“One sentence about your ideal client decides what you practise and who you show your work to.”",
    "s3_cta_kicker": "Your starter kit for this week",
},
"de": {
    "cover_pills": ["Basis…", "Duplet…", "Üben…"], "cover_with": "mit", "cover_brand": "Sempertex Europe", "cover_tag": "Starter-Guide…",
    "steps_title": "Ballonkünstler werden hängt von 3 Dingen ab.", "steps_lead": "Die 3 Dinge:",
    "steps": ["Eine solide Grundausbildung", "Verstehen, wie Latex sich verhält: Oxidation, Reibung, Wärme und Kälte", "Gezielt an wenigen Kernaufbauten üben, bis es automatisch läuft"],
    "steps_label": "Die Basis",
    "rule1_label": "Skill 1 und 2", "rule1_title": "Kenn dein Material und knote fest",
    "rule1_body": "Lockeres Knoten ist der häufigste Fehler, auch bei erfahrenen Künstlern. Das Duplet ist die Basis jeder Komposition. Sitzt es fest, bleibt alles stabil, was du darauf aufbaust.",
    "rule1_tags": ["Duplet", "Cluster"],
    "rule2_label": "Skill 3 und 4", "rule2_title": "Baue sicher und gestalte bewusst",
    "rule2_body": "Gewicht, Spannung, Befestigungspunkte und Untergrund wirken zusammen, gerade bei großen Installationen. Dazu kommen Farbkombinationen, Proportion und Balance. Fühlt es sich nicht richtig an, ist es nicht fertig.",
    "rule2_tags": ["groß", "klein", "groß", "klein", "groß"],
    "example_label": "Übungsset", "example_title": "Deine erste Übungswoche",
    "example_body": "Duplet: R12 {p0} + R12 {p1}. Cluster: dazu {p2} und {p3}. Ballonhund: ein 260 in Red 015. Jede Farbe hat einen festen Namen und Code, du bestellst also genau das, was du geübt hast.",
    "roles": ["Duplet", "Duplet", "Cluster", "Cluster"], "dog_label": "260 Red 015",
    "client_label": "Dein Wunschkunde", "client_title": "Schreib in einem Satz, wer dein Wunschkunde ist",
    "client_body": "Dieser eine Satz bestimmt, was du übst und wem du deine Arbeit zeigst. Buche einen echten Grundkurs, schau in der Freizeit kostenlose Tutorials und übe Duplets und Cluster, bis du sie blind kannst. Sempertex Europe bietet den 2-tägigen Workshop Start Your Balloon Business an.",
    "client_answer": "Deine ersten 5 Schritte:",
    "steps5": ["Buche einen echten Grundkurs", "Übe Duplets und Cluster, bis du sie blind kannst", "Mach einen Ballonhund, dann noch einen mit anderen Proportionen", "Recherchiere die Größen und wie Latex hergestellt wird", "Schreib den einen Satz über deinen Wunschkunden"],
    "cta_label": "Starten",
    "s3_cover_a": "Ballonkünstler werden mit Sempertex", "s3_cover_b": "mit Talent", "s3_cover_c": "vs.", "s3_cover_d": "mit Übung",
    "s3_left": "MIT TALENT", "s3_right": "MIT ÜBUNG", "s3_left_meta": "lockere Knoten", "s3_right_meta": "feste Duplets",
    "s3_changed_title": "Was ändert sich?", "s3_old_lbl": "ALT", "s3_new_lbl": "NEU",
    "s3_old_tags": ["Mit Talent", "Nur YouTube"], "s3_new_tags": ["Basis", "Duplet", "Üben"],
    "s3_new_quote": "„Erst ein Grundlagen-Workshop, dann Duplets bis du sie blind kannst, dann echte Kunden“", "s3_new_badge": "4 Skills",
    "s3_changed_bottom": "Gleiche Ballons, gleiche Hände.\nDie Basis kommt zuerst.",
    "s3_topic_lbl": "SKILL", "s3_rule1_topic": "Knoten", "s3_rule1_old": "Locker knoten geht schneller",
    "s3_rule1_quote": "„Lockeres Knoten ist der häufigste Fehler. Ein festes Duplet hält alles darauf stabil.“",
    "s3_rule2_topic": "Bauen", "s3_rule2_old": "Wenn es schön aussieht, ist es fertig",
    "s3_rule2_quote": "„Gewicht, Spannung, Befestigung und Untergrund wirken zusammen. Fühlt es sich nicht richtig an, ist es nicht fertig.“",
    "s3_example_lbl": "ÜBUNGSSET", "s3_example_quote": "„Duplet mit {p0} und {p1}, Cluster mit {p2} und {p3}, Ballonhund mit einem 260 Red 015.“",
    "s3_client_lbl": "KUNDE", "s3_client_topic": "Dein Wunschkunde",
    "s3_client_quote": "„Ein Satz über deinen Wunschkunden bestimmt, was du übst und wem du deine Arbeit zeigst.“",
    "s3_cta_kicker": "Dein Starterset für diese Woche",
},
"fr": {
    "cover_pills": ["Bases…", "Duplet…", "Pratique…"], "cover_with": "avec", "cover_brand": "Sempertex Europe", "cover_tag": "Guide débutant…",
    "steps_title": "Devenir artiste ballon tient à 3 choses.", "steps_lead": "Les 3 choses :",
    "steps": ["Une vraie formation de base", "Comprendre comment le latex réagit : oxydation, friction, chaleur et froid", "S'entraîner sur quelques montages clés, jusqu'à ce que ce soit automatique"],
    "steps_label": "Les bases",
    "rule1_label": "Compétences 1 et 2", "rule1_title": "Connais ton matériau et noue serré",
    "rule1_body": "Nouer trop lâche est l'erreur la plus fréquente, même chez les artistes expérimentés. Le duplet est la base de toute composition. S'il est serré, tout ce que tu construis dessus reste stable.",
    "rule1_tags": ["duplet", "cluster"],
    "rule2_label": "Compétences 3 et 4", "rule2_title": "Construis en sécurité et conçois avec intention",
    "rule2_body": "Poids, tension, points de fixation et support interagissent, surtout sur les grandes installations. Pense aussi aux combinaisons de couleurs, aux proportions et à l'équilibre. Si ça ne sonne pas juste, ce n'est pas fini.",
    "rule2_tags": ["grand", "petit", "grand", "petit", "grand"],
    "example_label": "Kit d'entraînement", "example_title": "Ta première semaine d'entraînement",
    "example_body": "Duplet : R12 {p0} + R12 {p1}. Cluster : ajoute {p2} et {p3}. Chien en ballon : un 260 en Red 015. Chaque couleur a un nom et un code fixes, tu commandes donc exactement ce que tu as pratiqué.",
    "roles": ["duplet", "duplet", "cluster", "cluster"], "dog_label": "260 Red 015",
    "client_label": "Ton client idéal", "client_title": "Écris en une phrase qui est ton client idéal",
    "client_body": "Cette phrase décide de ce que tu pratiques et à qui tu montres ton travail. Réserve un vrai cours de base, regarde des tutoriels gratuits sur ton temps libre et entraîne-toi aux duplets et clusters jusqu'à les faire les yeux fermés. Sempertex Europe propose l'atelier de 2 jours Start Your Balloon Business.",
    "client_answer": "Tes 5 premières étapes :",
    "steps5": ["Réserve un vrai cours de base", "Entraîne-toi aux duplets et clusters jusqu'à les faire les yeux fermés", "Fais un chien en ballon, puis un autre avec d'autres proportions", "Renseigne-toi sur les tailles et la fabrication du latex", "Écris cette phrase sur ton client idéal"],
    "cta_label": "Commencer",
    "s3_cover_a": "Devenir artiste ballon avec Sempertex", "s3_cover_b": "au talent", "s3_cover_c": "vs.", "s3_cover_d": "avec de la pratique",
    "s3_left": "AU TALENT", "s3_right": "AVEC PRATIQUE", "s3_left_meta": "nœuds lâches", "s3_right_meta": "duplets serrés",
    "s3_changed_title": "Qu'est-ce qui change ?", "s3_old_lbl": "AVANT", "s3_new_lbl": "APRÈS",
    "s3_old_tags": ["Au talent", "YouTube seul"], "s3_new_tags": ["Bases", "Duplet", "Pratique"],
    "s3_new_quote": "« D'abord un atelier de base, puis des duplets jusqu'à les faire les yeux fermés, puis seulement de vrais clients »", "s3_new_badge": "4 compétences",
    "s3_changed_bottom": "Mêmes ballons, mêmes mains.\nLes bases d'abord.",
    "s3_topic_lbl": "COMPÉTENCE", "s3_rule1_topic": "Nouer", "s3_rule1_old": "Nouer lâche, c'est plus rapide",
    "s3_rule1_quote": "« Nouer trop lâche est l'erreur la plus fréquente. Un duplet serré garde tout stable. »",
    "s3_rule2_topic": "Construire", "s3_rule2_old": "Si c'est joli, c'est fini",
    "s3_rule2_quote": "« Poids, tension, fixation et support interagissent. Si ça ne sonne pas juste, ce n'est pas fini. »",
    "s3_example_lbl": "KIT", "s3_example_quote": "« Duplet avec {p0} et {p1}, cluster avec {p2} et {p3}, chien en ballon avec un 260 Red 015. »",
    "s3_client_lbl": "CLIENT", "s3_client_topic": "Ton client idéal",
    "s3_client_quote": "« Une phrase sur ton client idéal décide de ce que tu pratiques et à qui tu montres ton travail. »",
    "s3_cta_kicker": "Ton kit de départ pour cette semaine",
},
"it": {
    "cover_pills": ["Basi…", "Duplet…", "Pratica…"], "cover_with": "con", "cover_brand": "Sempertex Europe", "cover_tag": "Guida per iniziare…",
    "steps_title": "Diventare balloon artist dipende da 3 cose.", "steps_lead": "Le 3 cose:",
    "steps": ["Una vera formazione di base", "Capire come si comporta il lattice: ossidazione, attrito, caldo e freddo", "Allenarsi su pochi montaggi chiave, finché non diventa automatico"],
    "steps_label": "Le basi",
    "rule1_label": "Skill 1 e 2", "rule1_title": "Conosci il materiale e annoda stretto",
    "rule1_body": "Annodare lento è l'errore più comune, anche tra gli artisti esperti. Il duplet è la base di ogni composizione. Se è stretto, tutto ciò che ci costruisci sopra resta stabile.",
    "rule1_tags": ["duplet", "cluster"],
    "rule2_label": "Skill 3 e 4", "rule2_title": "Costruisci in sicurezza e progetta con criterio",
    "rule2_body": "Peso, tensione, punti di fissaggio e supporto interagiscono, soprattutto nelle installazioni grandi. Poi guarda combinazioni di colori, proporzioni ed equilibrio. Se non ti convince, non è finito.",
    "rule2_tags": ["grande", "piccolo", "grande", "piccolo", "grande"],
    "example_label": "Kit di pratica", "example_title": "La tua prima settimana di pratica",
    "example_body": "Duplet: R12 {p0} + R12 {p1}. Cluster: aggiungi {p2} e {p3}. Cagnolino: un 260 in Red 015. Ogni colore ha nome e codice fissi, quindi ordini esattamente ciò che hai provato.",
    "roles": ["duplet", "duplet", "cluster", "cluster"], "dog_label": "260 Red 015",
    "client_label": "Il tuo cliente ideale", "client_title": "Scrivi in una frase chi è il tuo cliente ideale",
    "client_body": "Quella frase decide cosa alleni e a chi mostri il tuo lavoro. Prenota un vero corso base, guarda tutorial gratuiti nel tempo libero e allena duplet e cluster finché non li fai a occhi chiusi. Sempertex Europe organizza il workshop di 2 giorni Start Your Balloon Business.",
    "client_answer": "I tuoi primi 5 passi:",
    "steps5": ["Prenota un vero corso base", "Allena duplet e cluster finché non li fai a occhi chiusi", "Fai un cagnolino, poi un altro con proporzioni diverse", "Studia le misure e come si produce il lattice", "Scrivi quella frase sul tuo cliente ideale"],
    "cta_label": "Inizia",
    "s3_cover_a": "Diventare balloon artist con Sempertex", "s3_cover_b": "a talento", "s3_cover_c": "vs.", "s3_cover_d": "con la pratica",
    "s3_left": "A TALENTO", "s3_right": "CON LA PRATICA", "s3_left_meta": "nodi lenti", "s3_right_meta": "duplet stretti",
    "s3_changed_title": "Cosa cambia?", "s3_old_lbl": "PRIMA", "s3_new_lbl": "DOPO",
    "s3_old_tags": ["A talento", "Solo YouTube"], "s3_new_tags": ["Basi", "Duplet", "Pratica"],
    "s3_new_quote": "“Prima un workshop base, poi duplet finché non li fai a occhi chiusi, poi i clienti veri”", "s3_new_badge": "4 skill",
    "s3_changed_bottom": "Stessi palloncini, stesse mani.\nPrima le basi.",
    "s3_topic_lbl": "SKILL", "s3_rule1_topic": "Annodare", "s3_rule1_old": "Annodare lento è più veloce",
    "s3_rule1_quote": "“Annodare lento è l'errore più comune. Un duplet stretto tiene stabile tutto ciò che ci sta sopra.”",
    "s3_rule2_topic": "Costruire", "s3_rule2_old": "Se è bello, è finito",
    "s3_rule2_quote": "“Peso, tensione, fissaggio e supporto interagiscono. Se non ti convince, non è finito.”",
    "s3_example_lbl": "KIT", "s3_example_quote": "“Duplet con {p0} ed {p1}, cluster con {p2} e {p3}, cagnolino con un 260 Red 015.”",
    "s3_client_lbl": "CLIENTE", "s3_client_topic": "Il tuo cliente ideale",
    "s3_client_quote": "“Una frase sul tuo cliente ideale decide cosa alleni e a chi mostri il tuo lavoro.”",
    "s3_cta_kicker": "Il tuo kit di partenza per questa settimana",
},
"pl": {
    "cover_pills": ["Podstawy…", "Duplet…", "Ćwiczenie…"], "cover_with": "z", "cover_brand": "Sempertex Europe", "cover_tag": "Przewodnik na start…",
    "steps_title": "Zostanie artystą balonowym zależy od 3 rzeczy.", "steps_lead": "Te 3 rzeczy:",
    "steps": ["Solidne szkolenie podstawowe", "Zrozumienie, jak zachowuje się lateks: utlenianie, tarcie, ciepło i zimno", "Celowe ćwiczenie kilku kluczowych konstrukcji, aż wejdzie w krew"],
    "steps_label": "Podstawy",
    "rule1_label": "Umiejętność 1 i 2", "rule1_title": "Poznaj materiał i wiąż ciasno",
    "rule1_body": "Luźne wiązanie to najczęstszy błąd, także u doświadczonych artystów. Duplet to podstawa każdej kompozycji. Gdy jest ciasny, wszystko, co na nim zbudujesz, jest stabilne.",
    "rule1_tags": ["duplet", "klaster"],
    "rule2_label": "Umiejętność 3 i 4", "rule2_title": "Buduj bezpiecznie i projektuj świadomie",
    "rule2_body": "Ciężar, naprężenie, punkty mocowania i podłoże wpływają na siebie, zwłaszcza przy dużych instalacjach. Zwracaj też uwagę na zestawienia kolorów, proporcje i równowagę. Jeśli coś nie gra, projekt nie jest skończony.",
    "rule2_tags": ["duży", "mały", "duży", "mały", "duży"],
    "example_label": "Zestaw do ćwiczeń", "example_title": "Twój pierwszy tydzień ćwiczeń",
    "example_body": "Duplet: R12 {p0} + R12 {p1}. Klaster: dodaj {p2} i {p3}. Piesek z balona: 260 w kolorze Red 015. Każdy kolor ma stałą nazwę i kod, więc zamawiasz dokładnie to, na czym ćwiczysz.",
    "roles": ["duplet", "duplet", "klaster", "klaster"], "dog_label": "260 Red 015",
    "client_label": "Twój idealny klient", "client_title": "Napisz w jednym zdaniu, kim jest twój idealny klient",
    "client_body": "To jedno zdanie decyduje, co ćwiczysz i komu pokazujesz swoje prace. Zapisz się na prawdziwy kurs podstawowy, oglądaj darmowe tutoriale w wolnym czasie i ćwicz duplety i klastry, aż zrobisz je z zamkniętymi oczami. Sempertex Europe prowadzi 2-dniowe warsztaty Start Your Balloon Business.",
    "client_answer": "Twoje pierwsze 5 kroków:",
    "steps5": ["Zapisz się na prawdziwy kurs podstawowy", "Ćwicz duplety i klastry, aż zrobisz je z zamkniętymi oczami", "Zrób pieska z balona, potem kolejnego w innych proporcjach", "Poznaj rozmiary i sposób produkcji lateksu", "Napisz to jedno zdanie o idealnym kliencie"],
    "cta_label": "Start",
    "s3_cover_a": "Artysta balonowy z Sempertex", "s3_cover_b": "na talencie", "s3_cover_c": "vs.", "s3_cover_d": "na ćwiczeniu",
    "s3_left": "NA TALENCIE", "s3_right": "NA ĆWICZENIU", "s3_left_meta": "luźne węzły", "s3_right_meta": "ciasne duplety",
    "s3_changed_title": "Co się zmienia?", "s3_old_lbl": "PRZED", "s3_new_lbl": "PO",
    "s3_old_tags": ["Na talencie", "Tylko YouTube"], "s3_new_tags": ["Podstawy", "Duplet", "Ćwiczenie"],
    "s3_new_quote": "„Najpierw warsztat podstawowy, potem duplety aż do perfekcji, dopiero potem prawdziwi klienci”", "s3_new_badge": "4 umiejętności",
    "s3_changed_bottom": "Te same balony, te same ręce.\nNajpierw podstawy.",
    "s3_topic_lbl": "UMIEJĘTNOŚĆ", "s3_rule1_topic": "Wiązanie", "s3_rule1_old": "Luźne wiązanie jest szybsze",
    "s3_rule1_quote": "„Luźne wiązanie to najczęstszy błąd. Ciasny duplet utrzymuje wszystko stabilnie.”",
    "s3_rule2_topic": "Budowanie", "s3_rule2_old": "Jak ładnie wygląda, to gotowe",
    "s3_rule2_quote": "„Ciężar, naprężenie, mocowanie i podłoże wpływają na siebie. Jeśli coś nie gra, to nie jest skończone.”",
    "s3_example_lbl": "ZESTAW", "s3_example_quote": "„Duplet z {p0} i {p1}, klaster z {p2} i {p3}, piesek z balona 260 Red 015.”",
    "s3_client_lbl": "KLIENT", "s3_client_topic": "Twój idealny klient",
    "s3_client_quote": "„Jedno zdanie o idealnym kliencie decyduje, co ćwiczysz i komu pokazujesz swoje prace.”",
    "s3_cta_kicker": "Twój zestaw startowy na ten tydzień",
},
"el": {
    "cover_pills": ["Βάσεις…", "Duplet…", "Εξάσκηση…"], "cover_with": "με", "cover_brand": "Sempertex Europe", "cover_tag": "Οδηγός για αρχή…",
    "steps_title": "Το να γίνεις balloon artist εξαρτάται από 3 πράγματα.", "steps_lead": "Τα 3 πράγματα:",
    "steps": ["Μια σωστή βασική εκπαίδευση", "Να καταλαβαίνεις πώς συμπεριφέρεται το latex: οξείδωση, τριβή, ζέστη και κρύο", "Στοχευμένη εξάσκηση σε λίγες βασικές κατασκευές, μέχρι να γίνει αυτόματο"],
    "steps_label": "Η βάση",
    "rule1_label": "Δεξιότητες 1 και 2", "rule1_title": "Γνώρισε το υλικό σου και δέσε σφιχτά",
    "rule1_body": "Το χαλαρό δέσιμο είναι το πιο συχνό λάθος, ακόμα και σε έμπειρους καλλιτέχνες. Το duplet είναι η βάση κάθε σύνθεσης. Αν είναι σφιχτό, ό,τι χτίζεις πάνω του μένει σταθερό.",
    "rule1_tags": ["duplet", "cluster"],
    "rule2_label": "Δεξιότητες 3 και 4", "rule2_title": "Χτίσε με ασφάλεια και σχεδίασε συνειδητά",
    "rule2_body": "Βάρος, τάση, σημεία στήριξης και επιφάνεια αλληλεπιδρούν, ειδικά σε μεγάλες εγκαταστάσεις. Πρόσεξε και τους χρωματικούς συνδυασμούς, την αναλογία και την ισορροπία. Αν δεν σου κάθεται σωστά, δεν έχει τελειώσει.",
    "rule2_tags": ["μεγάλο", "μικρό", "μεγάλο", "μικρό", "μεγάλο"],
    "example_label": "Σετ εξάσκησης", "example_title": "Η πρώτη σου εβδομάδα εξάσκησης",
    "example_body": "Duplet: R12 {p0} + R12 {p1}. Cluster: πρόσθεσε {p2} και {p3}. Σκυλάκι από μπαλόνι: ένα 260 σε Red 015. Κάθε χρώμα έχει σταθερό όνομα και κωδικό, άρα παραγγέλνεις ακριβώς ό,τι εξάσκησες.",
    "roles": ["duplet", "duplet", "cluster", "cluster"], "dog_label": "260 Red 015",
    "client_label": "Ο ιδανικός σου πελάτης", "client_title": "Γράψε σε μία πρόταση ποιος είναι ο ιδανικός σου πελάτης",
    "client_body": "Αυτή η μία πρόταση καθορίζει τι εξασκείς και σε ποιον δείχνεις τη δουλειά σου. Κλείσε ένα πραγματικό βασικό μάθημα, δες δωρεάν tutorials στον ελεύθερο χρόνο σου και εξασκήσου σε duplets και clusters μέχρι να τα κάνεις με κλειστά μάτια. Η Sempertex Europe διοργανώνει το διήμερο workshop Start Your Balloon Business.",
    "client_answer": "Τα πρώτα σου 5 βήματα:",
    "steps5": ["Κλείσε ένα πραγματικό βασικό μάθημα", "Εξασκήσου σε duplets και clusters μέχρι να τα κάνεις με κλειστά μάτια", "Φτιάξε ένα σκυλάκι από μπαλόνι, και μετά άλλο ένα με άλλες αναλογίες", "Μελέτησε τα μεγέθη και πώς φτιάχνεται το latex", "Γράψε τη μία πρόταση για τον ιδανικό σου πελάτη"],
    "cta_label": "Ξεκίνα",
    "s3_cover_a": "Balloon artist με Sempertex", "s3_cover_b": "με ταλέντο", "s3_cover_c": "vs.", "s3_cover_d": "με εξάσκηση",
    "s3_left": "ΜΕ ΤΑΛΕΝΤΟ", "s3_right": "ΜΕ ΕΞΑΣΚΗΣΗ", "s3_left_meta": "χαλαροί κόμποι", "s3_right_meta": "σφιχτά duplets",
    "s3_changed_title": "Τι αλλάζει;", "s3_old_lbl": "ΠΡΙΝ", "s3_new_lbl": "ΜΕΤΑ",
    "s3_old_tags": ["Με ταλέντο", "Μόνο YouTube"], "s3_new_tags": ["Βάσεις", "Duplet", "Εξάσκηση"],
    "s3_new_quote": "«Πρώτα ένα βασικό workshop, μετά duplets μέχρι να τα κάνεις με κλειστά μάτια, και μετά πραγματικοί πελάτες»", "s3_new_badge": "4 δεξιότητες",
    "s3_changed_bottom": "Ίδια μπαλόνια, ίδια χέρια.\nΠρώτα η βάση.",
    "s3_topic_lbl": "ΔΕΞΙΟΤΗΤΑ", "s3_rule1_topic": "Δέσιμο", "s3_rule1_old": "Το χαλαρό δέσιμο είναι πιο γρήγορο",
    "s3_rule1_quote": "«Το χαλαρό δέσιμο είναι το πιο συχνό λάθος. Ένα σφιχτό duplet κρατά τα πάντα σταθερά.»",
    "s3_rule2_topic": "Κατασκευή", "s3_rule2_old": "Αν είναι όμορφο, τελείωσε",
    "s3_rule2_quote": "«Βάρος, τάση, στήριξη και επιφάνεια αλληλεπιδρούν. Αν δεν σου κάθεται σωστά, δεν έχει τελειώσει.»",
    "s3_example_lbl": "ΣΕΤ", "s3_example_quote": "«Duplet με {p0} και {p1}, cluster με {p2} και {p3}, σκυλάκι με ένα 260 Red 015.»",
    "s3_client_lbl": "ΠΕΛΑΤΗΣ", "s3_client_topic": "Ο ιδανικός σου πελάτης",
    "s3_client_quote": "«Μία πρόταση για τον ιδανικό σου πελάτη καθορίζει τι εξασκείς και σε ποιον δείχνεις τη δουλειά σου.»",
    "s3_cta_kicker": "Το σετ εκκίνησής σου για αυτή την εβδομάδα",
},
"hu": {
    "cover_pills": ["Alapok…", "Duplet…", "Gyakorlás…"], "cover_with": "partner:", "cover_brand": "Sempertex Europe", "cover_tag": "Kezdő útmutató…",
    "steps_title": "A lufiművésszé válás 3 dolgon múlik.", "steps_lead": "A 3 dolog:",
    "steps": ["Egy rendes alapképzés", "Érteni, hogyan viselkedik a latex: oxidáció, súrlódás, meleg és hideg", "Célzott gyakorlás néhány alapkonstrukción, amíg automatikus nem lesz"],
    "steps_label": "Az alap",
    "rule1_label": "1. és 2. készség", "rule1_title": "Ismerd az anyagot és kösd szorosra",
    "rule1_body": "A laza kötés a leggyakoribb hiba, tapasztalt művészeknél is. A duplet minden kompozíció alapja. Ha szoros, minden stabil marad, amit ráépítesz.",
    "rule1_tags": ["duplet", "klaszter"],
    "rule2_label": "3. és 4. készség", "rule2_title": "Építs biztonságosan és tervezz tudatosan",
    "rule2_body": "A súly, a feszítés, a rögzítési pontok és az alap hatnak egymásra, főleg nagy installációknál. Figyelj a színkombinációkra, az arányokra és az egyensúlyra is. Ha nem érzed jónak, nincs kész.",
    "rule2_tags": ["nagy", "kicsi", "nagy", "kicsi", "nagy"],
    "example_label": "Gyakorlókészlet", "example_title": "Az első gyakorlóheted",
    "example_body": "Duplet: R12 {p0} + R12 {p1}. Klaszter: add hozzá a {p2}-ot és a {p3}-et. Lufikutya: egy 260-as Red 015-ben. Minden színnek fix neve és kódja van, így pontosan azt rendeled, amit gyakoroltál.",
    "roles": ["duplet", "duplet", "klaszter", "klaszter"], "dog_label": "260 Red 015",
    "client_label": "Az ideális ügyfeled", "client_title": "Írd le egy mondatban, ki az ideális ügyfeled",
    "client_body": "Ez az egy mondat dönti el, mit gyakorolsz és kinek mutatod meg a munkádat. Foglalj egy igazi alaptanfolyamot, nézz ingyenes oktatóvideókat szabadidődben, és gyakorold a dupleteket és klasztereket, amíg csukott szemmel is mennek. A Sempertex Europe 2 napos workshopja: Start Your Balloon Business.",
    "client_answer": "Az első 5 lépésed:",
    "steps5": ["Foglalj egy igazi alaptanfolyamot", "Gyakorold a dupleteket és klasztereket, amíg csukott szemmel is mennek", "Készíts egy lufikutyát, majd még egyet más arányokkal", "Nézz utána a méreteknek és a latex gyártásának", "Írd le azt az egy mondatot az ideális ügyfeledről"],
    "cta_label": "Kezdés",
    "s3_cover_a": "Lufiművész a Sempertex-szel", "s3_cover_b": "tehetségből", "s3_cover_c": "vs.", "s3_cover_d": "gyakorlással",
    "s3_left": "TEHETSÉGBŐL", "s3_right": "GYAKORLÁSSAL", "s3_left_meta": "laza csomók", "s3_right_meta": "szoros dupletek",
    "s3_changed_title": "Mi változik?", "s3_old_lbl": "ELŐTTE", "s3_new_lbl": "UTÁNA",
    "s3_old_tags": ["Tehetségből", "Csak YouTube"], "s3_new_tags": ["Alapok", "Duplet", "Gyakorlás"],
    "s3_new_quote": "„Először alapworkshop, aztán dupletek csukott szemmel, csak utána igazi ügyfelek”", "s3_new_badge": "4 készség",
    "s3_changed_bottom": "Ugyanazok a lufik, ugyanazok a kezek.\nElőbb az alapok.",
    "s3_topic_lbl": "KÉSZSÉG", "s3_rule1_topic": "Kötés", "s3_rule1_old": "Lazán kötni gyorsabb",
    "s3_rule1_quote": "„A laza kötés a leggyakoribb hiba. Egy szoros duplet mindent stabilan tart.”",
    "s3_rule2_topic": "Építés", "s3_rule2_old": "Ha szép, akkor kész",
    "s3_rule2_quote": "„Súly, feszítés, rögzítés és alap hatnak egymásra. Ha nem érzed jónak, nincs kész.”",
    "s3_example_lbl": "KÉSZLET", "s3_example_quote": "„Duplet {p0}-zel és {p1}-tel, klaszter {p2}-tal és {p3}-nel, lufikutya egy 260-as Red 015-ből.”",
    "s3_client_lbl": "ÜGYFÉL", "s3_client_topic": "Az ideális ügyfeled",
    "s3_client_quote": "„Egy mondat az ideális ügyfeledről eldönti, mit gyakorolsz és kinek mutatod meg a munkádat.”",
    "s3_cta_kicker": "A heti kezdőkészleted",
},
"lt": {
    "cover_pills": ["Pagrindai…", "Dupletas…", "Praktika…"], "cover_with": "su", "cover_brand": "Sempertex Europe", "cover_tag": "Pradedančiojo gidas…",
    "steps_title": "Tapti balionų menininku lemia 3 dalykai.", "steps_lead": "Tie 3 dalykai:",
    "steps": ["Tvirti pagrindiniai mokymai", "Suprasti, kaip elgiasi lateksas: oksidacija, trintis, šiluma ir šaltis", "Kryptinga praktika su keliomis pagrindinėmis konstrukcijomis, kol tai tampa automatiška"],
    "steps_label": "Pagrindas",
    "rule1_label": "1 ir 2 įgūdis", "rule1_title": "Pažink medžiagą ir rišk tvirtai",
    "rule1_body": "Laisvas rišimas yra dažniausia klaida, net tarp patyrusių menininkų. Dupletas yra kiekvienos kompozicijos pagrindas. Jei jis tvirtas, viskas, ką ant jo statai, lieka stabilu.",
    "rule1_tags": ["dupletas", "klasteris"],
    "rule2_label": "3 ir 4 įgūdis", "rule2_title": "Statyk saugiai ir kurk sąmoningai",
    "rule2_body": "Svoris, įtempimas, tvirtinimo taškai ir pagrindas veikia vienas kitą, ypač didelėse instaliacijose. Taip pat žiūrėk į spalvų derinius, proporcijas ir balansą. Jei kažkas neatrodo gerai, darbas nebaigtas.",
    "rule2_tags": ["didelis", "mažas", "didelis", "mažas", "didelis"],
    "example_label": "Praktikos rinkinys", "example_title": "Pirmoji tavo praktikos savaitė",
    "example_body": "Dupletas: R12 {p0} + R12 {p1}. Klasteris: pridėk {p2} ir {p3}. Balionų šuniukas: 260 Red 015 spalvos. Kiekviena spalva turi pastovų pavadinimą ir kodą, tad užsakai tiksliai tai, ką praktikavai.",
    "roles": ["dupletas", "dupletas", "klasteris", "klasteris"], "dog_label": "260 Red 015",
    "client_label": "Tavo idealus klientas", "client_title": "Parašyk vienu sakiniu, kas yra tavo idealus klientas",
    "client_body": "Tas vienas sakinys lemia, ką praktikuoji ir kam rodai savo darbus. Užsiregistruok į tikrus pagrindų kursus, laisvalaikiu žiūrėk nemokamas pamokas ir praktikuok dupletus bei klasterius, kol darysi juos užsimerkęs. Sempertex Europe rengia 2 dienų dirbtuves Start Your Balloon Business.",
    "client_answer": "Pirmieji 5 tavo žingsniai:",
    "steps5": ["Užsiregistruok į tikrus pagrindų kursus", "Praktikuok dupletus ir klasterius, kol darysi juos užsimerkęs", "Padaryk balionų šuniuką, paskui dar vieną kitokių proporcijų", "Išsiaiškink dydžius ir kaip gaminamas lateksas", "Parašyk tą vieną sakinį apie idealų klientą"],
    "cta_label": "Pradėk",
    "s3_cover_a": "Balionų menininkas su Sempertex", "s3_cover_b": "iš talento", "s3_cover_c": "vs.", "s3_cover_d": "iš praktikos",
    "s3_left": "IŠ TALENTO", "s3_right": "IŠ PRAKTIKOS", "s3_left_meta": "laisvi mazgai", "s3_right_meta": "tvirti dupletai",
    "s3_changed_title": "Kas keičiasi?", "s3_old_lbl": "PRIEŠ", "s3_new_lbl": "PO",
    "s3_old_tags": ["Iš talento", "Tik YouTube"], "s3_new_tags": ["Pagrindai", "Dupletas", "Praktika"],
    "s3_new_quote": "„Pirma pagrindų dirbtuvės, tada dupletai, kol darai juos užsimerkęs, ir tik tada tikri klientai“", "s3_new_badge": "4 įgūdžiai",
    "s3_changed_bottom": "Tie patys balionai, tos pačios rankos.\nPirmiausia pagrindai.",
    "s3_topic_lbl": "ĮGŪDIS", "s3_rule1_topic": "Rišimas", "s3_rule1_old": "Laisvai rišti greičiau",
    "s3_rule1_quote": "„Laisvas rišimas yra dažniausia klaida. Tvirtas dupletas išlaiko viską stabiliai.“",
    "s3_rule2_topic": "Statymas", "s3_rule2_old": "Jei gražu, vadinasi baigta",
    "s3_rule2_quote": "„Svoris, įtempimas, tvirtinimas ir pagrindas veikia vienas kitą. Jei neatrodo gerai, darbas nebaigtas.“",
    "s3_example_lbl": "RINKINYS", "s3_example_quote": "„Dupletas su {p0} ir {p1}, klasteris su {p2} ir {p3}, šuniukas iš 260 Red 015.“",
    "s3_client_lbl": "KLIENTAS", "s3_client_topic": "Tavo idealus klientas",
    "s3_client_quote": "„Vienas sakinys apie idealų klientą lemia, ką praktikuoji ir kam rodai savo darbus.“",
    "s3_cta_kicker": "Tavo starto rinkinys šiai savaitei",
},
}

VARIANTS = {
"nl": {
  "cover_title": ["Zo word je ballonartiest, stap voor stap, met Sempertex", "Ballonartiest worden: 4 skills, 5 stappen en Sempertex ballonnen", "Van eerste ballon tot eerste klant: ballonartiest worden met Sempertex"],
  "cover_sub": ["Geen standaardprofiel, wel een vak dat je kunt leren. De 4 skills, je eerste 5 stappen en het antwoord op de diplomavraag.", "Alberto, Denise en Audrey begonnen alle drie anders. Wat ze delen: een goede basis, materiaalkennis en oefenen op een paar bouwsels."],
  "client_question": ["Mijn ideale klant: jonge ouders die een babyshower of eerste verjaardag vieren.", "Mijn ideale klant: eventplanners die elke maand een bedrijfsfeest aankleden.", "Mijn ideale klant: winkels die elk seizoen een nieuwe etalage willen."],
  "s3_old_quote": ["“Ik leer het wel al doende”", "“Een cursus is weggegooid geld”", "“Naar die knopen kijkt toch niemand”"],
  "s3_client_old": ["“Ik doe alles voor iedereen”", "“Ik zie wel wie er belt”"],
  "cta_title_tpl": "Haal je eerste Sempertex ballonnen bij {name}", "cta_sub_generic": "Bestel met de codes uit deze post en begin deze week met oefenen.",
},
"en": {
  "cover_title": ["How to become a balloon artist, step by step, with Sempertex", "Becoming a balloon artist: 4 skills, 5 steps and Sempertex balloons", "From first balloon to first client: becoming a balloon artist with Sempertex"],
  "cover_sub": ["No standard profile, but a craft you can learn. The 4 skills, your first 5 steps and the answer to the licence question.", "Alberto, Denise and Audrey all started differently. What they share: solid basics, material knowledge and practice on a few core builds."],
  "client_question": ["My ideal client: young parents celebrating a baby shower or first birthday.", "My ideal client: event planners dressing a corporate party every month.", "My ideal client: shops that want a new window display every season."],
  "s3_old_quote": ["“I'll pick it up as I go”", "“A course is money down the drain”", "“Nobody looks at the knots anyway”"],
  "s3_client_old": ["“I do everything for everyone”", "“I'll see who calls”"],
  "cta_title_tpl": "Get your first Sempertex balloons at {name}", "cta_sub_generic": "Order with the codes in this post and start practising this week.",
},
"de": {
  "cover_title": ["So wirst du Ballonkünstler, Schritt für Schritt, mit Sempertex", "Ballonkünstler werden: 4 Skills, 5 Schritte und Sempertex Ballons", "Vom ersten Ballon zum ersten Kunden: Ballonkünstler werden mit Sempertex"],
  "cover_sub": ["Kein Standardprofil, aber ein Handwerk, das man lernen kann. Die 4 Skills, deine ersten 5 Schritte und die Antwort auf die Lizenzfrage.", "Alberto, Denise und Audrey haben alle anders angefangen. Was sie teilen: eine solide Basis, Materialwissen und Übung an wenigen Aufbauten."],
  "client_question": ["Mein Wunschkunde: junge Eltern, die eine Babyparty oder den ersten Geburtstag feiern.", "Mein Wunschkunde: Eventplaner, die jeden Monat eine Firmenfeier ausstatten.", "Mein Wunschkunde: Läden, die jede Saison ein neues Schaufenster wollen."],
  "s3_old_quote": ["„Das lerne ich schon nebenbei“", "„Ein Kurs ist rausgeworfenes Geld“", "„Auf die Knoten schaut doch keiner“"],
  "s3_client_old": ["„Ich mache alles für alle“", "„Mal sehen, wer anruft“"],
  "cta_title_tpl": "Hol dir deine ersten Sempertex Ballons bei {name}", "cta_sub_generic": "Bestell mit den Codes aus diesem Post und fang diese Woche an zu üben.",
},
"fr": {
  "cover_title": ["Comment devenir artiste ballon, étape par étape, avec Sempertex", "Devenir artiste ballon : 4 compétences, 5 étapes et des ballons Sempertex", "Du premier ballon au premier client : devenir artiste ballon avec Sempertex"],
  "cover_sub": ["Pas de profil type, mais un métier qui s'apprend. Les 4 compétences, tes 5 premières étapes et la réponse à la question du diplôme.", "Alberto, Denise et Audrey ont tous commencé différemment. Ce qu'ils partagent : des bases solides, la connaissance du matériau et de la pratique sur quelques montages."],
  "client_question": ["Mon client idéal : de jeunes parents qui fêtent une baby shower ou un premier anniversaire.", "Mon client idéal : des organisateurs d'événements qui habillent une fête d'entreprise chaque mois.", "Mon client idéal : des boutiques qui veulent une nouvelle vitrine chaque saison."],
  "s3_old_quote": ["« J'apprendrai sur le tas »", "« Un cours, c'est de l'argent jeté »", "« Personne ne regarde les nœuds »"],
  "s3_client_old": ["« Je fais tout pour tout le monde »", "« On verra qui appelle »"],
  "cta_title_tpl": "Prends tes premiers ballons Sempertex chez {name}", "cta_sub_generic": "Commande avec les codes de ce post et commence à t'entraîner cette semaine.",
},
"it": {
  "cover_title": ["Come diventare balloon artist, passo dopo passo, con Sempertex", "Diventare balloon artist: 4 skill, 5 passi e palloncini Sempertex", "Dal primo palloncino al primo cliente: diventare balloon artist con Sempertex"],
  "cover_sub": ["Nessun profilo standard, ma un mestiere che si impara. Le 4 skill, i tuoi primi 5 passi e la risposta alla domanda sul diploma.", "Alberto, Denise e Audrey hanno iniziato in modi diversi. Cosa hanno in comune: basi solide, conoscenza del materiale e pratica su pochi montaggi."],
  "client_question": ["Il mio cliente ideale: giovani genitori che festeggiano un baby shower o un primo compleanno.", "Il mio cliente ideale: event planner che allestiscono una festa aziendale ogni mese.", "Il mio cliente ideale: negozi che vogliono una vetrina nuova ogni stagione."],
  "s3_old_quote": ["“Lo imparo strada facendo”", "“Un corso sono soldi buttati”", "“Tanto i nodi non li guarda nessuno”"],
  "s3_client_old": ["“Faccio tutto per tutti”", "“Vediamo chi chiama”"],
  "cta_title_tpl": "Prendi i tuoi primi palloncini Sempertex da {name}", "cta_sub_generic": "Ordina con i codici di questo post e inizia ad allenarti questa settimana.",
},
"pl": {
  "cover_title": ["Jak zostać artystą balonowym, krok po kroku, z Sempertex", "Artysta balonowy: 4 umiejętności, 5 kroków i balony Sempertex", "Od pierwszego balonu do pierwszego klienta: artysta balonowy z Sempertex"],
  "cover_sub": ["Nie ma jednego profilu, ale jest fach, którego można się nauczyć. 4 umiejętności, pierwsze 5 kroków i odpowiedź na pytanie o dyplom.", "Alberto, Denise i Audrey zaczynali zupełnie inaczej. Co ich łączy: solidne podstawy, znajomość materiału i ćwiczenie kilku konstrukcji."],
  "client_question": ["Mój idealny klient: młodzi rodzice świętujący baby shower albo pierwsze urodziny.", "Mój idealny klient: organizatorzy eventów, którzy co miesiąc dekorują imprezę firmową.", "Mój idealny klient: sklepy, które co sezon chcą nową witrynę."],
  "s3_old_quote": ["„Nauczę się w praktyce”", "„Kurs to wyrzucone pieniądze”", "„Na węzły i tak nikt nie patrzy”"],
  "s3_client_old": ["„Robię wszystko dla wszystkich”", "„Zobaczę, kto zadzwoni”"],
  "cta_title_tpl": "Pierwsze balony Sempertex kup w {name}", "cta_sub_generic": "Zamów z kodami z tego posta i zacznij ćwiczyć w tym tygodniu.",
},
"el": {
  "cover_title": ["Πώς να γίνεις balloon artist, βήμα βήμα, με Sempertex", "Balloon artist: 4 δεξιότητες, 5 βήματα και μπαλόνια Sempertex", "Από το πρώτο μπαλόνι στον πρώτο πελάτη: balloon artist με Sempertex"],
  "cover_sub": ["Δεν υπάρχει τυπικό προφίλ, υπάρχει όμως τέχνη που μαθαίνεται. Οι 4 δεξιότητες, τα πρώτα 5 βήματα και η απάντηση για το δίπλωμα.", "Ο Alberto, η Denise και η Audrey ξεκίνησαν διαφορετικά. Κοινό τους: γερές βάσεις, γνώση του υλικού και εξάσκηση σε λίγες κατασκευές."],
  "client_question": ["Ο ιδανικός μου πελάτης: νέοι γονείς που γιορτάζουν baby shower ή πρώτα γενέθλια.", "Ο ιδανικός μου πελάτης: event planners που στολίζουν εταιρικό πάρτι κάθε μήνα.", "Ο ιδανικός μου πελάτης: καταστήματα που θέλουν νέα βιτρίνα κάθε σεζόν."],
  "s3_old_quote": ["«Θα το μάθω στην πορεία»", "«Το μάθημα είναι πεταμένα λεφτά»", "«Τους κόμπους δεν τους κοιτάει κανείς»"],
  "s3_client_old": ["«Κάνω τα πάντα για όλους»", "«Βλέπουμε ποιος θα πάρει»"],
  "cta_title_tpl": "Πάρε τα πρώτα σου μπαλόνια Sempertex από {name}", "cta_sub_generic": "Παράγγειλε με τους κωδικούς αυτού του post και ξεκίνα εξάσκηση αυτή την εβδομάδα.",
},
"hu": {
  "cover_title": ["Így leszel lufiművész, lépésről lépésre, a Sempertex-szel", "Lufiművész: 4 készség, 5 lépés és Sempertex lufik", "Az első lufitól az első ügyfélig: lufiművész a Sempertex-szel"],
  "cover_sub": ["Nincs tipikus profil, de van tanulható szakma. A 4 készség, az első 5 lépésed és a válasz a diplomakérdésre.", "Alberto, Denise és Audrey mind másképp kezdték. Ami közös: erős alapok, anyagismeret és gyakorlás néhány konstrukción."],
  "client_question": ["Az ideális ügyfelem: fiatal szülők, akik babavárót vagy első szülinapot ünnepelnek.", "Az ideális ügyfelem: rendezvényszervezők, akik havonta céges bulit dekorálnak.", "Az ideális ügyfelem: üzletek, amelyek minden szezonban új kirakatot akarnak."],
  "s3_old_quote": ["„Menet közben megtanulom”", "„A tanfolyam kidobott pénz”", "„A csomókat úgysem nézi senki”"],
  "s3_client_old": ["„Mindent csinálok mindenkinek”", "„Majd meglátom, ki hív”"],
  "cta_title_tpl": "Az első Sempertex lufijaidat itt szerezd be: {name}", "cta_sub_generic": "Rendelj a posztban lévő kódokkal, és kezdj el gyakorolni még ezen a héten.",
},
"lt": {
  "cover_title": ["Kaip tapti balionų menininku, žingsnis po žingsnio, su Sempertex", "Balionų menininkas: 4 įgūdžiai, 5 žingsniai ir Sempertex balionai", "Nuo pirmo baliono iki pirmo kliento: balionų menininkas su Sempertex"],
  "cover_sub": ["Nėra standartinio profilio, bet yra amatas, kurio galima išmokti. 4 įgūdžiai, pirmieji 5 žingsniai ir atsakymas apie diplomą.", "Alberto, Denise ir Audrey pradėjo skirtingai. Kas bendra: tvirti pagrindai, medžiagos išmanymas ir praktika su keliomis konstrukcijomis."],
  "client_question": ["Mano idealus klientas: jauni tėvai, švenčiantys kūdikio sutiktuves ar pirmą gimtadienį.", "Mano idealus klientas: renginių organizatoriai, kas mėnesį puošiantys įmonės šventę.", "Mano idealus klientas: parduotuvės, kurios kiekvieną sezoną nori naujos vitrinos."],
  "s3_old_quote": ["„Išmoksiu dirbdamas“", "„Kursai yra išmesti pinigai“", "„Į mazgus vis tiek niekas nežiūri“"],
  "s3_client_old": ["„Darau viską visiems“", "„Pažiūrėsiu, kas paskambins“"],
  "cta_title_tpl": "Pirmuosius Sempertex balionus įsigyk iš {name}", "cta_sub_generic": "Užsisakyk pagal šio įrašo kodus ir pradėk praktikuotis šią savaitę.",
},
}

CAPTIONS_TPL = {
 "nl": "Ballonartiest worden draait om herhaling: een goede basis, weten hoe latex zich gedraagt en oefenen op een paar bouwsels. In deze carousel: de 4 skills van elke professional, je eerste 5 stappen en een oefenset met Sempertex codes.\n\nHaal je eerste Sempertex ballonnen bij {domain}.\n\n#ballonartiest #sempertex #{tag} #ballondecoratie #ballonnen #startyourballoonbusiness",
 "en": "Becoming a balloon artist is about repetition: solid basics, knowing how latex behaves and practising a few core builds. In this carousel: the 4 skills every professional has, your first 5 steps and a practice kit with Sempertex codes.\n\nGet your first Sempertex balloons at {domain}.\n\n#balloonartist #sempertex #{tag} #balloondecor #balloons #startyourballoonbusiness",
 "de": "Ballonkünstler werden ist Wiederholung: eine solide Basis, wissen, wie Latex sich verhält, und Übung an wenigen Aufbauten. Im Carousel: die 4 Skills jedes Profis, deine ersten 5 Schritte und ein Übungsset mit Sempertex Codes.\n\nHol dir deine ersten Sempertex Ballons bei {domain}.\n\n#ballonkünstler #sempertex #{tag} #ballondeko #ballons #startyourballoonbusiness",
 "fr": "Devenir artiste ballon, c'est de la répétition : des bases solides, savoir comment le latex réagit et s'entraîner sur quelques montages. Dans ce carrousel : les 4 compétences de chaque pro, tes 5 premières étapes et un kit d'entraînement avec les codes Sempertex.\n\nPrends tes premiers ballons Sempertex chez {domain}.\n\n#artisteballon #sempertex #{tag} #decorationballons #ballons #startyourballoonbusiness",
 "it": "Diventare balloon artist è ripetizione: basi solide, sapere come si comporta il lattice e allenarsi su pochi montaggi. Nel carosello: le 4 skill di ogni professionista, i tuoi primi 5 passi e un kit di pratica con i codici Sempertex.\n\nPrendi i tuoi primi palloncini Sempertex da {domain}.\n\n#balloonartist #sempertex #{tag} #palloncini #decorazioni #startyourballoonbusiness",
 "pl": "Artysta balonowy to kwestia powtarzania: solidne podstawy, znajomość lateksu i ćwiczenie kilku konstrukcji. W karuzeli: 4 umiejętności każdego profesjonalisty, pierwsze 5 kroków i zestaw do ćwiczeń z kodami Sempertex.\n\nPierwsze balony Sempertex kup w {domain}.\n\n#artystabalonowy #sempertex #{tag} #dekoracjebalonowe #balony #startyourballoonbusiness",
 "el": "Το να γίνεις balloon artist είναι επανάληψη: γερές βάσεις, γνώση του latex και εξάσκηση σε λίγες κατασκευές. Στο carousel: οι 4 δεξιότητες κάθε επαγγελματία, τα πρώτα 5 βήματα και ένα σετ εξάσκησης με κωδικούς Sempertex.\n\nΠάρε τα πρώτα σου μπαλόνια Sempertex από {domain}.\n\n#balloonartist #sempertex #{tag} #μπαλονια #startyourballoonbusiness",
 "hu": "A lufiművésszé válás ismétlés: erős alapok, a latex ismerete és gyakorlás néhány konstrukción. A carouselben: minden profi 4 készsége, az első 5 lépésed és egy gyakorlókészlet Sempertex kódokkal.\n\nAz első Sempertex lufijaidat itt szerezd be: {domain}.\n\n#lufiművész #sempertex #{tag} #lufidekoracio #lufi #startyourballoonbusiness",
 "lt": "Tapti balionų menininku reiškia kartoti: tvirti pagrindai, latekso išmanymas ir praktika su keliomis konstrukcijomis. Karuselėje: 4 kiekvieno profesionalo įgūdžiai, pirmieji 5 žingsniai ir praktikos rinkinys su Sempertex kodais.\n\nPirmuosius Sempertex balionus įsigyk iš {domain}.\n\n#balionumenininkas #sempertex #{tag} #balionai #startyourballoonbusiness",
}

# ---------------------------------------------------------------- VISUALS

def fill_pal(b, c):
    """Vult {p0}..{p3} in de copy met de kleurnamen + codes van het palet van deze distri."""
    lab = {f"p{i}": G["pal_label"](k, short=False).replace("Fashion ", "").replace("Pastel ", "") for i, k in enumerate(b["pal"][:4])}
    out = {}
    for k, v in c.items():
        if isinstance(v, str): out[k] = v.format(**lab) if "{p" in v else v
        elif isinstance(v, list): out[k] = [x.format(**lab) if isinstance(x, str) and "{p" in x else x for x in v]
        else: out[k] = v
    return out
CUR = {"pal": ["rosewood", "eucalyptus", "greentea", "golddust"]}  # wordt per distri gezet (b["pal"], zie build.assign_palettes)
def _bl(key, size, cls=""):
    return G["balloon"](key, "fashion", size, cls=cls)

def duplet(size=150, keys=None):
    keys = keys or CUR["pal"][:2]
    """Twee ballonnen met de knopen tegen elkaar (duplet). Container-breedte ~ 2.1*size."""
    h = int(size * G["PHOTO_RATIO"]); w = int(size * 2.1); ch = int(h * 1.05)
    cx = w // 2; cy = ch - 6
    out = f'<div style="position:relative;width:{w}px;height:{ch}px">'
    for k, a in zip(keys, (-30, 30)):
        out += f'<div style="position:absolute;left:{cx - size//2}px;top:{cy - h}px;transform-origin:50% 100%;transform:rotate({a}deg)">{_bl(k, size)}</div>'
    return out + '</div>'

def cluster4(size=110, keys=None):
    keys = keys or CUR["pal"][:4]
    """Vier ballonnen rond één knooppunt (cluster van bovenaf)."""
    h = int(size * G["PHOTO_RATIO"]); w = int(h * 2.05); ch = w
    cx = w // 2; cy = ch // 2
    out = f'<div style="position:relative;width:{w}px;height:{ch}px">'
    for k, a in zip(keys, (-45, 45, 135, 225)):
        out += f'<div style="position:absolute;left:{cx - size//2}px;top:{cy - h}px;transform-origin:50% 100%;transform:rotate({a}deg)">{_bl(k, size)}</div>'
    return out + '</div>'

def garland(big=120, small=78, keys=None, labels=None):
    keys = keys or (CUR["pal"] + CUR["pal"][:1])
    """Slinger: groot, klein, groot, klein, groot, licht gedraaid, onderkant uitgelijnd."""
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:0">'
    for i, k in enumerate(keys):
        s = big if i % 2 == 0 else small
        rotv = (-10, 12, -6, 10, -12)[i % 5]
        lab = f'<div class="pname" style="font-size:22px;margin-top:12px">{G["esc"](labels[i])}</div>' if labels else ""
        out += f'<div style="text-align:center;margin:0 -10px"><div style="transform:rotate({rotv}deg)">{_bl(k, s)}</div>{lab}</div>'
    return out + '</div>'

def kit_row(c, size=140):
    """Oefenset: 4 R12 + 260 + label met codes."""
    SX = G["SX"]; esc = G["esc"]; PHOTO = G["PHOTO_RATIO"]
    keys = CUR["pal"][:4]
    out = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:22px">'
    for k, role in zip(keys, c["roles"]):
        nm = SX[k]["name"].replace("Fashion ", "").replace("Pastel Dusk ", "P. Dusk ")
        out += (f'<div class="pitem">{_bl(k, size)}<div class="pname" style="font-size:20px">{esc(nm)}<span class="pcode"> {SX[k]["code"]}</span></div>'
                f'<div class="pcode-only" style="opacity:.8">{esc(role)}</div></div>')
    w260 = int(size * 0.17)
    out += (f'<div class="pitem" style="margin-left:6px"><div style="position:relative;width:{int(size*1.3)}px;height:{int(size*PHOTO)}px;overflow:visible">'
            f'<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-55deg)">{G["balloon"]("red260", "fashion", w260)}</div></div>'
            f'<div class="pname" style="font-size:20px">{esc(c["dog_label"])}</div><div class="pcode-only" style="opacity:.8">260</div></div>')
    return out + '</div>'

def steps5_list(c, cls=""):
    esc = G["esc"]
    return ('<div class="' + cls + '">' + "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps5"])) + '</div>')

# ---------------------------------------------------------------- STIJL 1
def s1_slides(b, c):
    CUR["pal"] = b["pal"]; c = fill_pal(b, c)
    esc, hl, cursor_svg, arrow_svg, balloon = G["esc"], G["hl"], G["cursor_svg"], G["arrow_svg"], G["balloon"]
    s1_footer, logo_img, rot, STX_FULL = G["s1_footer"], G["logo_img"], G["rot"], G["STX_FULL"]
    S = []
    pills = c["cover_pills"]
    S.append(f"""
<section class="slide s1">
  <h1 data-fit style="position:absolute;left:70px;right:70px;top:250px;max-height:560px;font-size:104px;text-align:center;line-height:1.06">{hl(c['cover_title'])}</h1>
  <div class="pill" style="background:{b['c1']};color:{b['c1t']};right:60px;top:130px;transform:rotate({rot(b,-4)}deg)">{cursor_svg(b['c1'])}{esc(pills[0])}</div>
  <div class="pill" style="background:{b['c2']};color:{b['c2t']};right:90px;top:835px;transform:rotate({rot(b,3)}deg)">{cursor_svg(b['c2'])}{esc(pills[1])}</div>
  <div class="pill" style="background:{b['c3']};color:{b['c3t']};left:90px;top:880px;transform:rotate({rot(b,-2)}deg)">{cursor_svg(b['c3'])}{esc(pills[2])}</div>
  <div style="position:absolute;left:150px;top:960px">{arrow_svg(b['ink'], 130, 120)}</div>
  <div style="position:absolute;left:310px;right:90px;top:1020px;font-size:30px;line-height:1.35">{esc(c['cover_sub'])}</div>
  {s1_footer(b, stx_h=84)}
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s1">
  <div class="box" style="left:70px;top:120px;width:800px;height:560px">
    <h2 data-fit style="font-size:84px;max-height:460px;line-height:1.1">{esc(c['steps_title'])}</h2>
  </div>
  <div class="bigballoon" style="left:830px;top:90px;transform:rotate(14deg)">{balloon(b['hero'], 'fashion', 180)}</div>
  <div style="position:absolute;left:120px;top:690px">{arrow_svg(b['ink'], 150, 140)}</div>
  <div class="box" style="left:300px;top:720px;width:710px;height:440px;padding:40px 46px">
    <div style="font-size:30px;font-weight:{b['body_b']}">{esc(c['steps_lead'])}</div>
    {steps}
  </div>
  {s1_footer(b)}
</section>""")
    tags = c["rule1_tags"]
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule1_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:420px;padding:44px 50px">
    <h2 data-fit style="font-size:62px;max-height:150px">{esc(c['rule1_title'])}</h2>
    <div class="body" style="margin-top:22px">{esc(c['rule1_body'])}</div>
  </div>
  <div class="stack" style="top:650px;height:460px">
    <div class="card" style="top:0;height:380px;transform:translate(60px,-70px) scale(.92);opacity:.5"></div>
    <div class="card" style="top:0;height:380px;transform:translate(30px,-36px) scale(.96);opacity:.75"></div>
    <div class="card" style="top:0;height:430px;display:flex;align-items:flex-end;justify-content:space-around;padding:30px 40px 36px">
      <div style="text-align:center">{duplet(160)}<div class="pname" style="font-size:24px;margin-top:10px;font-weight:{b['body_b']}">{esc(tags[0])}</div></div>
      <div style="text-align:center">{cluster4(112)}<div class="pname" style="font-size:24px;margin-top:10px;font-weight:{b['body_b']}">{esc(tags[1])}</div></div>
    </div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['rule2_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:460px;padding:44px 50px">
    <h2 data-fit style="font-size:58px;max-height:200px">{esc(c['rule2_title'])}</h2>
    <div class="body" style="margin-top:22px">{esc(c['rule2_body'])}</div>
  </div>
  <div class="stack" style="top:700px;height:400px">
    <div class="card" style="top:0;height:340px;transform:translate(40px,-50px) scale(.95);opacity:.6"></div>
    <div class="card" style="top:0;height:380px;display:flex;align-items:flex-end;justify-content:center;padding:30px 30px 40px">{garland(150, 96, labels=c['rule2_tags'])}</div>
  </div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['example_label'])}</div>
  <div class="box" style="left:70px;top:160px;width:940px;height:520px;padding:44px 30px 36px">
    <h2 data-fit style="font-size:54px;margin-bottom:40px;text-align:center;max-height:130px">{esc(c['example_title'])}</h2>
    {kit_row(c, 140)}
  </div>
  <div class="box" style="left:70px;top:730px;width:940px;padding:40px 50px"><div class="body" style="font-size:31px">{esc(c['example_body'])}</div></div>
  {s1_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s1">
  <div class="tag" style="right:70px;top:70px"><span class="ast">✳</span>{esc(c['client_label'])}</div>
  <h2 data-fit style="position:absolute;left:80px;right:80px;top:160px;font-size:54px;max-height:140px">{esc(c['client_title'])}</h2>
  <div class="chat" style="top:320px;min-height:150px;padding-right:120px">{esc(c['client_question'])}<div class="send">↑</div></div>
  <div style="position:absolute;left:80px;right:80px;top:510px;display:flex;flex-direction:column;gap:22px">
    <div class="card" style="position:relative;left:auto;right:auto;padding:26px 36px"><div style="font-size:27px;font-weight:{b['body_b']};margin-bottom:4px">{esc(c['client_answer'])}</div>{steps5_list(c)}</div>
    <div style="font-size:25px;line-height:1.35" class="body">{esc(c['client_body'])}</div>
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
    CUR["pal"] = b["pal"]; c = fill_pal(b, c)
    esc, hl, balloon, rot = G["esc"], G["hl"], G["balloon"], G["rot"]
    s2_footer, STX_WT = G["s2_footer"], G["STX_WT"]
    S = []
    S.append(f"""
<section class="slide s2">
  <div class="sq" style="left:70px;top:70px;width:200px;height:120px"><img src="file://{b['logo']}" style="max-width:170px;max-height:90px"></div>
  <div class="conn" style="left:170px;top:190px;width:140px;height:380px"></div>
  <div style="position:absolute;left:300px;top:552px;width:0;height:0;border-left:22px solid #fff;border-top:14px solid transparent;border-bottom:14px solid transparent"></div>
  <h1 data-fit style="position:absolute;left:320px;right:70px;top:70px;max-height:430px;font-size:74px">{hl(c['cover_title'])}</h1>
  <div class="frame" style="left:320px;top:520px;width:690px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:460px;flex-direction:row;gap:40px">{duplet(150)}{cluster4(98)}</div>
  </div>
  <div class="tagw" style="right:70px;top:960px;white-space:nowrap"><span class="ast">✳</span>{esc(c['cover_tag'])}</div>
  <div style="position:absolute;left:70px;top:1060px;font-size:36px;line-height:1.1">{esc(c['cover_with'])}</div>
  <div style="position:absolute;left:70px;bottom:52px"><img src="file://{STX_WT}" style="height:120px"></div>
</section>""")
    steps = "".join(f'<div class="step"><b>{i+1}.</b><span>{esc(s)}</span></div>' for i, s in enumerate(c["steps"]))
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['steps_label'])}</div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:160px"><b style="font-size:40px">{esc(c['steps_title'])}</b>{steps}</div>
  <div class="frame" style="left:80px;top:640px;width:600px;transform:rotate({rot(b,-2)}deg)">
    <div class="ph" style="height:400px">{duplet(165)}</div>
  </div>
  <div class="frame" style="left:560px;top:780px;width:430px;transform:rotate({rot(b,3)}deg)">
    <div class="ph" style="height:300px">{balloon(b['hero'], 'fashion', 150)}</div>
  </div>
  {s2_footer(b)}
</section>""")
    tags = c["rule1_tags"]
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule1_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:64px;max-height:160px">{esc(c['rule1_title'])}</h2>
  <div class="frame" style="left:70px;top:350px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:440px;flex-direction:row;justify-content:space-around;align-items:flex-end;padding:0 20px 30px;box-sizing:border-box">
      <div style="text-align:center">{duplet(165)}<div class="pname" style="font-size:22px;margin-top:8px">{esc(tags[0])}</div></div>
      <div style="text-align:center">{cluster4(112)}<div class="pname" style="font-size:22px;margin-top:8px">{esc(tags[1])}</div></div>
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:900px">{esc(c['rule1_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['rule2_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:60px;max-height:170px">{esc(c['rule2_title'])}</h2>
  <div class="frame" style="left:70px;top:370px;width:940px;transform:rotate({rot(b,1.5)}deg)">
    <div class="ph" style="height:400px;flex-direction:row;justify-content:center;align-items:flex-end;padding:0 20px 30px;box-sizing:border-box">{garland(150, 96, labels=c['rule2_tags'])}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:890px">{esc(c['rule2_body'])}</div>
  {s2_footer(b)}
</section>""")
    S.append(f"""
<section class="slide s2">
  <div class="label" style="top:70px">{esc(c['example_label'])}</div>
  <h2 data-fit style="position:absolute;left:70px;right:70px;top:160px;font-size:60px;max-height:150px">{esc(c['example_title'])}</h2>
  <div class="frame" style="left:70px;top:330px;width:940px;transform:rotate({rot(b,-1.5)}deg)">
    <div class="ph" style="height:460px;padding:20px;box-sizing:border-box">{kit_row(c, 130)}</div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:880px;font-size:29px">{esc(c['example_body'])}</div>
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
      <div style="font-size:24px;font-weight:{b['body_b']};color:{b['ink']}">{esc(c['client_answer'])}</div>
      {steps5_list(c, 'onwhite')}
    </div>
  </div>
  <div class="body" style="position:absolute;left:70px;right:70px;top:960px;font-size:26px">{esc(c['client_body'])}</div>
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
    CUR["pal"] = b["pal"]; c = fill_pal(b, c)
    esc, hl, balloon, rot = G["esc"], G["hl"], G["balloon"], G["rot"]
    s3_footer, messy_cluster, clean_cluster, STX_FULL = G["s3_footer"], G["messy_cluster"], G["clean_cluster"], G["STX_FULL"]
    S = []
    S.append(f"""
<section class="slide s3">
  <h1 data-fit style="position:absolute;left:50px;right:50px;top:60px;max-height:400px;font-size:88px;text-align:center;line-height:1.08">{hl(c['s3_cover_a'])} {esc(c['s3_cover_b'])} {esc(c['s3_cover_c'])}<br><span class="hl">{esc(c['s3_cover_d'])}</span></h1>
  <div class="vsmark" style="top:520px">VS</div>
  <div class="lblw" style="left:110px;top:500px;transform:rotate({rot(b,-4)}deg)">{esc(c['s3_left'])}<br><span class="meta">● {esc(c['s3_left_meta'])}</span></div>
  <div class="lbld" style="right:110px;top:500px;transform:rotate({rot(b,4)}deg)">{esc(c['s3_right'])}<br><span class="meta" style="background:rgba(255,255,255,.18)">● {esc(c['s3_right_meta'])}</span></div>
  <div style="position:absolute;left:60px;top:680px;transform:scale(1.18);transform-origin:top left">{messy_cluster()}</div>
  <div style="position:absolute;right:60px;top:680px;transform:scale(1.18);transform-origin:top right">{clean_cluster()}</div>
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
    <div class="quote" style="font-size:32px">{esc(c['s3_new_quote'])}</div>
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
    <div class="strike" style="font-size:42px;line-height:1.2;color:#fff;text-decoration-color:#E03131;margin-top:34px;font-weight:700;font-family:'{b['ui']}'">{esc(old_text)}</div>
    <div style="position:absolute;left:36px;right:36px;bottom:34px;font-size:22px;opacity:.55;font-weight:600">{esc(old_meta)}</div>
  </div>
  <div class="cardw onwhite" style="left:570px;top:230px;width:440px;height:600px;padding:34px 36px">
    <span class="newlbl">{esc(c['s3_new_lbl'])}</span>
    <div style="margin-top:30px;display:flex;justify-content:center">{new_visual}</div>
  </div>
  <div class="bottom" style="top:890px;font-size:34px;font-weight:700">{esc(quote)}</div>
  {s3_footer(b)}
</section>"""
    vis1 = f'<div style="display:flex;flex-direction:column;align-items:center;gap:30px">{duplet(140)}<div class="pname" style="font-size:22px">{esc(c["rule1_tags"][0])}</div></div>'
    S.append(topic_slide(c["s3_rule1_topic"], c["s3_rule1_old"], vis1, c["s3_rule1_quote"]))
    vis2 = f'<div style="display:flex;flex-direction:column;align-items:center;gap:26px">{cluster4(100)}<div class="pname" style="font-size:22px">{esc(c["rule1_tags"][1])}</div></div>'
    S.append(topic_slide(c["s3_rule2_topic"], c["s3_rule2_old"], vis2, c["s3_rule2_quote"]))
    S.append(f"""
<section class="slide s3">
  <div class="topic" style="top:80px"><span class="k">{esc(c['s3_example_lbl'])}</span><span class="v">{esc(c['example_title'])}</span></div>
  <div class="cardw onwhite" style="left:70px;right:70px;top:230px;height:620px;padding:50px 24px;display:flex;align-items:center;justify-content:center">
    {kit_row(c, 128)}
  </div>
  <div class="bottom" style="top:910px;font-size:32px;font-weight:700">{esc(c['s3_example_quote'])}</div>
  {s3_footer(b)}
</section>""")
    vis6 = (f'<div style="width:100%"><div style="font-size:24px;line-height:1.3;font-style:italic;margin-bottom:14px">{esc(c["client_question"])}</div>'
            f'<div style="font-size:20px;font-weight:800;margin-bottom:4px">{esc(c["client_answer"])}</div>{steps5_list(c, "s3steps")}</div>')
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
.s2 .onwhite .step{color:#111;font-size:24px;margin-top:10px}
.s2 .onwhite .step b{color:#6b3fb9}
.s3 .s3steps .step{display:flex;gap:12px;font-size:20px;line-height:1.25;margin-top:9px}
.s3 .s3steps .step b{min-width:28px;font-weight:800}
"""
