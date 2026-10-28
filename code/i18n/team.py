# Vertaaltabel voor de teampagina (bron: Robins sempertex-team-pagina.html, Nederlands).
# Sleutel = tekst zoals hij in de bron staat. Een sleutel met HTML (koppen met een gele
# markering) wordt als geheel vervangen; de rest per tekststuk.
# Rollen staan in de bron al in het Engels en blijven in elke taal Engels (KEEP).
# Pas je de bron aan, dan meldt build-shadow-section.py welke stukken nog geen vertaling hebben.
# Duits met du (zoals de rest van de site), Frans met vous.

SOURCE = 'nl'
LANGS = ['en', 'fr', 'de']

KEEP = [
    'CEO', 'SV', 'KD', 'RV', 'KC', 'RR', 'VE', 'GC', 'JJ', 'TC', 'AU', 'AM', 'JV', 'JH', 'ML', 'AL',
    'DD', 'AP', 'MB', 'AF', 'TT', 'PA',
    'Sofie Vandewyer', 'Koen Van Damme', 'Rani Vandiest', 'Kim Cuppens', 'Robin Rutten', 'Vroni Effner',
    'Gigi Canale', 'Julie Joris', 'Tijl Ceyssens', 'Atilla Ucum', 'Anouk Mussen', 'Jan Verbeeck',
    'Jeroen Heylen', 'Matisse Lambrichts', 'Aziz Lagouireh', 'Denise Van Dooren', 'Audrey Parsons',
    'Melissa Bellefontaine', 'Alberto Falcone', 'Tobi Twist', 'Paula Ardron-Gemmell',
    'CEO Sempertex Europe', 'Head of Technical &amp; Events', 'Head of Operations &amp; Customer Experience',
    'Finance &amp; Data', 'Head of Marketing &amp; Sales', 'Customer Service', 'Event &amp; Office Assistant',
    'Media &amp; Content Creator', 'Videographer &amp; Editor', 'Creative &amp; Color Specialist',
    'Head of Warehouse', 'Warehouse Operator', 'Creative ambassador',
    'Mie&euml;nbroekstraat 43', 'sempertexeurope.com',
]

# alt-teksten van de portretten: "<naam>, <rol> bij Sempertex Europe"
PATTERNS = [
    (r'^(.*) bij Sempertex Europe$', {'en': r'\1 at Sempertex Europe', 'fr': r'\1 chez Sempertex Europe', 'de': r'\1 bei Sempertex Europe'}),
]

T = {
    # ---- koppen met gele markering (als geheel) ----
    'Het team achter <span class="hl">de ballon</span>': {
        'en': 'The team behind <span class="hl">the balloon</span>',
        'fr': 'L’équipe derrière <span class="hl">le ballon</span>',
        'de': 'Das Team hinter <span class="hl">dem Ballon</span>'},
    'Onze <span class="hl">CEO</span>': {
        'en': 'Our <span class="hl">CEO</span>',
        'fr': 'Notre <span class="hl">CEO</span>',
        'de': 'Unsere <span class="hl">CEO</span>'},
    'Onze <span class="hl">leidinggevenden</span>': {
        'en': 'Our <span class="hl">leadership</span>',
        'fr': 'Nos <span class="hl">responsables</span>',
        'de': 'Unsere <span class="hl">Führung</span>'},
    'Klantendienst &amp; <span class="hl">kantoor</span>': {
        'en': 'Customer service &amp; <span class="hl">office</span>',
        'fr': 'Service client &amp; <span class="hl">bureau</span>',
        'de': 'Kundenservice &amp; <span class="hl">Büro</span>'},
    'Creatie &amp; <span class="hl">media</span>': {
        'en': 'Creative &amp; <span class="hl">media</span>',
        'fr': 'Création &amp; <span class="hl">médias</span>',
        'de': 'Kreation &amp; <span class="hl">Medien</span>'},
    'In het <span class="hl">magazijn</span>': {
        'en': 'In the <span class="hl">warehouse</span>',
        'fr': 'À l’<span class="hl">entrepôt</span>',
        'de': 'Im <span class="hl">Lager</span>'},
    'Onze creative <span class="hl">ambassadors</span>': {
        'en': 'Our creative <span class="hl">ambassadors</span>',
        'fr': 'Nos <span class="hl">ambassadeurs</span> créatifs',
        'de': 'Unsere kreativen <span class="hl">Botschafter</span>'},
    'Achter elke bestelling, elke workshop en elke kleur staat een mens die je kan <span class="hl">bellen</span>.': {
        'en': 'Behind every order, every workshop and every colour is a person you can <span class="hl">call</span>.',
        'fr': 'Derrière chaque commande, chaque atelier et chaque couleur, il y a une personne que vous pouvez <span class="hl">appeler</span>.',
        'de': 'Hinter jeder Bestellung, jedem Workshop und jeder Farbe steht ein Mensch, den du <span class="hl">anrufen</span> kannst.'},
    'Kom gerust <span class="hl">langs</span>': {
        'en': 'Come and <span class="hl">visit</span>',
        'fr': 'Passez nous <span class="hl">voir</span>',
        'de': 'Komm gern <span class="hl">vorbei</span>'},
    'Zin om met dit team te <span class="hl">werken?</span>': {
        'en': 'Want to work with <span class="hl">this team?</span>',
        'fr': 'Envie de travailler avec <span class="hl">cette équipe ?</span>',
        'de': 'Lust, mit diesem Team zu <span class="hl">arbeiten?</span>'},

    # ---- navigatie ----
    'Afdelingen': {'en': 'Departments', 'fr': 'Services', 'de': 'Abteilungen'},
    'Spring naar': {'en': 'Jump to', 'fr': 'Aller à', 'de': 'Springe zu'},
    'Leiding': {'en': 'Leadership', 'fr': 'Direction', 'de': 'Führung'},
    'Klantendienst': {'en': 'Customer service', 'fr': 'Service client', 'de': 'Kundenservice'},
    'Creatie &amp; media': {'en': 'Creative &amp; media', 'fr': 'Création &amp; médias', 'de': 'Kreation &amp; Medien'},
    'Magazijn': {'en': 'Warehouse', 'fr': 'Entrepôt', 'de': 'Lager'},
    'Ambassadors': {'en': 'Ambassadors', 'fr': 'Ambassadeurs', 'de': 'Botschafter'},
    'Kom langs': {'en': 'Visit us', 'fr': 'Nous rendre visite', 'de': 'Besuch uns'},

    # ---- CEO ----
    'Sofie stuurt Sempertex Europe aan, van markt tot magazijn.': {
        'en': 'Sofie runs Sempertex Europe, from market to warehouse.',
        'fr': 'Sofie dirige Sempertex Europe, du marché à l’entrepôt.',
        'de': 'Sofie leitet Sempertex Europe, vom Markt bis ins Lager.'},
    'Eigenaar': {'en': 'Owner', 'fr': 'Propriétaire', 'de': 'Inhaberin'},
    'Denkt in kleuren, spreekt in strategie en houdt het overzicht, ook wanneer alles tegelijk beweegt.': {
        'en': 'Thinks in colours, speaks in strategy and keeps the overview, even when everything moves at once.',
        'fr': 'Pense en couleurs, parle en stratégie et garde la vue d’ensemble, même quand tout bouge en même temps.',
        'de': 'Denkt in Farben, spricht in Strategie und behält den Überblick, auch wenn sich alles gleichzeitig bewegt.'},
    'Bouwt markten, stuurt groei en bewaart de balans tussen cijfers en creativiteit. Niet bang voor een uitdaging maar wel voor meetings zonder einde.': {
        'en': 'Builds markets, steers growth and keeps the balance between numbers and creativity. Not afraid of a challenge, but definitely afraid of meetings that never end.',
        'fr': 'Développe des marchés, pilote la croissance et garde l’équilibre entre chiffres et créativité. Pas peur d’un défi, mais bien des réunions sans fin.',
        'de': 'Baut Märkte auf, steuert das Wachstum und hält die Balance zwischen Zahlen und Kreativität. Keine Angst vor Herausforderungen, aber vor Meetings ohne Ende.'},

    # ---- leiding ----
    'De mensen die hun team sturen, de cijfers bewaken en de lijnen uitzetten.': {
        'en': 'The people who lead their teams, watch the numbers and set the direction.',
        'fr': 'Les personnes qui pilotent leur équipe, surveillent les chiffres et fixent le cap.',
        'de': 'Die Menschen, die ihr Team führen, die Zahlen im Blick behalten und die Richtung vorgeben.'},
    'Zorgt dat alles technisch blijft draaien en krijgt alles voor mekaar, ook wanneer het complex wordt. Meer dan 30 jaar ervaring in het ballonvak en nog altijd even gedreven. Brengt mensen samen, is altijd aanspreekbaar en nooit verlegen om een grapje.': {
        'en': 'Keeps everything running on the technical side and gets things done, even when it gets complicated. More than 30 years in the balloon trade and still just as driven. Brings people together, always approachable and never short of a joke.',
        'fr': 'Veille à ce que tout tourne sur le plan technique et trouve toujours une solution, même quand ça se complique. Plus de 30 ans d’expérience dans le métier du ballon et toujours aussi passionné. Rassemble les gens, reste toujours disponible et a toujours une blague en réserve.',
        'de': 'Sorgt dafür, dass technisch alles läuft, und bekommt alles hin, auch wenn es kompliziert wird. Mehr als 30 Jahre Erfahrung in der Ballonbranche und noch immer genauso motiviert. Bringt Menschen zusammen, ist immer ansprechbar und nie um einen Witz verlegen.'},
    'Houdt alles draaiende en zorgt dat niets tussen de mazen van het net valt. Altijd stipt en houdt overzicht en structuur, zelfs wanneer alles tegelijk loopt. Regelt wat geregeld moet worden, vaak nog vóór iemand het doorheeft.': {
        'en': 'Keeps everything running and makes sure nothing slips through the cracks. Always punctual, keeps the overview and the structure, even when everything happens at once. Sorts out what needs sorting, often before anyone notices.',
        'fr': 'Fait tourner la machine et veille à ce que rien ne passe entre les mailles du filet. Toujours ponctuelle, elle garde la vue d’ensemble et la structure, même quand tout arrive en même temps. Règle ce qui doit l’être, souvent avant que quelqu’un s’en rende compte.',
        'de': 'Hält alles am Laufen und sorgt dafür, dass nichts durchs Raster fällt. Immer pünktlich, behält Überblick und Struktur, auch wenn alles gleichzeitig passiert. Regelt, was geregelt werden muss, oft noch bevor es jemand merkt.'},
    'Brengt cijfers tot leven en zorgt dat alles klopt, tot in de details. Combineert boekhouding met data-analyse en maakt van cijfers heldere inzichten. Haar eerste vraag? Wat kost dat?': {
        'en': 'Brings numbers to life and makes sure everything adds up, down to the details. Combines accounting with data analysis and turns figures into clear insights. Her first question? What does it cost?',
        'fr': 'Donne vie aux chiffres et veille à ce que tout soit juste, jusque dans les détails. Associe comptabilité et analyse de données pour transformer les chiffres en informations claires. Sa première question ? Combien ça coûte ?',
        'de': 'Erweckt Zahlen zum Leben und sorgt dafür, dass alles stimmt, bis ins Detail. Verbindet Buchhaltung mit Datenanalyse und macht aus Zahlen klare Erkenntnisse. Ihre erste Frage? Was kostet das?'},
    'Zorgt dat het merk zichtbaar is op de juiste momenten, op de juiste plaatsen. Denkt in campagnes, content en groei, en vertaalt ideeën naar sterke marketing. Jong, ambitieus en altijd op zoek naar wat beter, slimmer of sterker kan.': {
        'en': 'Makes sure the brand is seen at the right moments, in the right places. Thinks in campaigns, content and growth, and turns ideas into strong marketing. Young, ambitious and always looking for what can be better, smarter or stronger.',
        'fr': 'Veille à ce que la marque soit visible au bon moment, au bon endroit. Pense en campagnes, contenus et croissance, et transforme les idées en marketing fort. Jeune, ambitieux et toujours à la recherche de ce qui peut être mieux, plus malin ou plus fort.',
        'de': 'Sorgt dafür, dass die Marke zur richtigen Zeit am richtigen Ort sichtbar ist. Denkt in Kampagnen, Content und Wachstum und macht aus Ideen starkes Marketing. Jung, ehrgeizig und immer auf der Suche nach dem, was besser, klüger oder stärker geht.'},

    # ---- klantendienst ----
    'De stem aan de telefoon en de hand achter je bestelling. Dit is het team dat je het vaakst spreekt.': {
        'en': 'The voice on the phone and the hands behind your order. This is the team you talk to most.',
        'fr': 'La voix au téléphone et la main derrière votre commande. C’est l’équipe avec qui vous parlez le plus souvent.',
        'de': 'Die Stimme am Telefon und die Hand hinter deiner Bestellung. Mit diesem Team sprichst du am häufigsten.'},
    'Zorgt dat klanten zich gehoord en geholpen voelen, van eerste vraag tot laatste detail. Schakelt snel, denkt mee en vertaalt vragen meteen naar oplossingen. Volgt alles nauwkeurig op en maakt het verschil in de kleine dingen.': {
        'en': 'Makes sure customers feel heard and helped, from the first question to the last detail. Quick to switch, thinks along and turns questions straight into solutions. Follows everything up carefully and makes the difference in the small things.',
        'fr': 'Veille à ce que chaque client se sente écouté et aidé, de la première question au dernier détail. Réagit vite, réfléchit avec vous et transforme aussitôt les questions en solutions. Assure un suivi précis et fait la différence dans les petites choses.',
        'de': 'Sorgt dafür, dass sich Kunden gehört und gut betreut fühlen, von der ersten Frage bis zum letzten Detail. Schaltet schnell, denkt mit und macht aus Fragen sofort Lösungen. Verfolgt alles genau nach und macht den Unterschied in den kleinen Dingen.'},
    'Is het eerste aanspreekpunt en zit vol energie van het eerste tot het laatste telefoontje. Denkt mee, pakt alles meteen aan en gaat er altijd vol voor. Brengt tempo, positiviteit en zorgt voor the Italian Drama ;-).': {
        'en': 'The first point of contact, full of energy from the first call to the last. Thinks along, tackles everything straight away and always goes all in. Brings pace, positivity and a good dose of Italian Drama ;-).',
        'fr': 'Premier point de contact, pleine d’énergie du premier au dernier appel. Réfléchit avec vous, s’attaque à tout immédiatement et se donne toujours à fond. Apporte du rythme, de la bonne humeur et une touche d’Italian Drama ;-).',
        'de': 'Die erste Ansprechpartnerin, voller Energie vom ersten bis zum letzten Anruf. Denkt mit, packt alles sofort an und gibt immer alles. Bringt Tempo, gute Laune und sorgt für das Italian Drama ;-).'},
    'Springt in waar nodig en voelt zich even thuis achter een bureau, aan de kassa als op een evenement. Schakelt snel tussen taken, mensen en situaties zonder een stap te missen. Veelzijdig inzetbaar en altijd klaar voor wat er ook komt.': {
        'en': 'Steps in wherever needed and feels just as at home behind a desk or at the till as at an event. Switches quickly between tasks, people and situations without missing a beat. Versatile and always ready for whatever comes next.',
        'fr': 'Intervient là où il faut et se sent aussi à l’aise derrière un bureau qu’à la caisse ou sur un événement. Passe rapidement d’une tâche, d’une personne ou d’une situation à l’autre sans rien manquer. Polyvalente et toujours prête pour la suite.',
        'de': 'Springt ein, wo es nötig ist, und fühlt sich am Schreibtisch, an der Kasse und auf Events gleichermaßen zu Hause. Wechselt schnell zwischen Aufgaben, Menschen und Situationen, ohne etwas zu verpassen. Vielseitig einsetzbar und immer bereit für das, was kommt.'},

    # ---- creatie & media ----
    'Kleur, beeld en verhaal. Alles wat je van ons ziet op social media, in campagnes en op events.': {
        'en': 'Colour, image and story. Everything you see from us on social media, in campaigns and at events.',
        'fr': 'Couleur, image et histoire. Tout ce que vous voyez de nous sur les réseaux sociaux, dans nos campagnes et lors de nos événements.',
        'de': 'Farbe, Bild und Geschichte. Alles, was du von uns auf Social Media, in Kampagnen und auf Events siehst.'},
    'Komt altijd met frisse ideeën en content die niemand zag aankomen. Houdt trends in de gaten, denkt creatief en is niet bang om buiten de lijntjes te kleuren. Brengt energie, humor en net genoeg chaos om het hele team scherp te houden.': {
        'en': 'Always comes up with fresh ideas and content nobody saw coming. Keeps an eye on trends, thinks creatively and is not afraid to colour outside the lines. Brings energy, humour and just enough chaos to keep the whole team sharp.',
        'fr': 'Arrive toujours avec des idées fraîches et des contenus que personne n’avait vus venir. Suit les tendances, pense de façon créative et n’a pas peur de sortir des cases. Apporte de l’énergie, de l’humour et juste assez de chaos pour garder toute l’équipe en alerte.',
        'de': 'Kommt immer mit frischen Ideen und Content, mit dem niemand gerechnet hat. Behält Trends im Blick, denkt kreativ und malt auch gern mal über den Rand. Bringt Energie, Humor und genau so viel Chaos, dass das ganze Team wach bleibt.'},
    'Vangt elk moment op camera en zorgt dat het er in de montage precies goed uitziet. Laat niets aan het toeval over en heeft een scherp oog voor detail. Geduldig, precies en altijd gefocust op het eindresultaat.': {
        'en': 'Captures every moment on camera and makes sure it looks exactly right in the edit. Leaves nothing to chance and has a sharp eye for detail. Patient, precise and always focused on the end result.',
        'fr': 'Capte chaque moment à la caméra et veille à ce que tout soit parfait au montage. Ne laisse rien au hasard et a l’œil pour le détail. Patient, précis et toujours concentré sur le résultat final.',
        'de': 'Fängt jeden Moment mit der Kamera ein und sorgt dafür, dass im Schnitt alles genau stimmt. Überlässt nichts dem Zufall und hat ein scharfes Auge für Details. Geduldig, präzise und immer auf das Endergebnis fokussiert.'},
    'Brengt kleur tot leven en creëert palettes die meteen blijven hangen. Zet ideeën om in visuals en ondersteunt het social media team waar nodig. Cameraschuw, creatief, en overal inzetbaar.': {
        'en': 'Brings colour to life and creates palettes that stick straight away. Turns ideas into visuals and supports the social media team where needed. Camera-shy, creative and ready to help anywhere.',
        'fr': 'Donne vie à la couleur et crée des palettes qu’on retient tout de suite. Transforme les idées en visuels et soutient l’équipe réseaux sociaux quand il le faut. Timide devant la caméra, créative et polyvalente.',
        'de': 'Erweckt Farbe zum Leben und kreiert Farbpaletten, die sofort hängen bleiben. Setzt Ideen in Visuals um und unterstützt das Social-Media-Team, wo es nötig ist. Kamerascheu, kreativ und überall einsetzbar.'},

    # ---- magazijn ----
    'Waar je bestelling echt gemaakt wordt. Picken, klaarzetten, inladen, en dat elke dag opnieuw.': {
        'en': 'Where your order really comes together. Picking, preparing, loading, and all over again every day.',
        'fr': 'Là où votre commande prend vraiment forme. Préparer, emballer, charger, et ça recommence chaque jour.',
        'de': 'Wo deine Bestellung wirklich entsteht. Kommissionieren, bereitstellen, verladen, und das jeden Tag aufs Neue.'},
    'Leidt de flow in het magazijn met een rustige en zachte aanpak. Neemt tijd voor mensen, houdt de sfeer goed en zorgt dat iedereen mee is. Blijft kalm in de drukte of doet erg goed alsof ;-)': {
        'en': 'Leads the flow in the warehouse with a calm and gentle approach. Takes time for people, keeps the atmosphere good and makes sure everyone is on board. Stays calm when it gets busy, or is very good at pretending ;-)',
        'fr': 'Mène le rythme de l’entrepôt avec calme et douceur. Prend le temps pour les gens, entretient la bonne ambiance et veille à ce que tout le monde suive. Reste calme dans le rush, ou fait très bien semblant ;-)',
        'de': 'Leitet den Ablauf im Lager mit einer ruhigen und sanften Art. Nimmt sich Zeit für Menschen, sorgt für gute Stimmung und dafür, dass alle mitkommen. Bleibt ruhig im Trubel, oder tut sehr überzeugend so ;-)'},
    'Zorgt dat het werk gedaan is en dat er ondertussen ook gelachen wordt. Brengt energie in het magazijn en steekt iedereen aan met zijn humeur. De lolbroek van het team maar wel eentje die altijd meedraait.': {
        'en': 'Makes sure the work gets done and that there is a laugh along the way. Brings energy to the warehouse and lifts everyone with his good mood. The joker of the team, but one who always pulls his weight.',
        'fr': 'Veille à ce que le travail soit fait, et qu’on rigole un peu au passage. Met de l’énergie dans l’entrepôt et contamine tout le monde avec sa bonne humeur. Le blagueur de l’équipe, mais toujours au rendez-vous.',
        'de': 'Sorgt dafür, dass die Arbeit erledigt wird und dabei auch gelacht wird. Bringt Energie ins Lager und steckt alle mit seiner Laune an. Der Spaßvogel im Team, aber einer, der immer mit anpackt.'},
    'Pikt orders met precisie en zorgt dat alles netjes klaarstaat. Werkt rustig, doet gewoon zijn ding en houdt het graag simpel. Maakt in het magazijn alles klaar en thuis gewoon pizza.': {
        'en': 'Picks orders with precision and makes sure everything is neatly ready. Works calmly, just does his thing and likes to keep it simple. Gets everything ready in the warehouse, and pizza at home.',
        'fr': 'Prépare les commandes avec précision et veille à ce que tout soit prêt, bien rangé. Travaille calmement, fait son truc et aime que ça reste simple. Prépare tout à l’entrepôt, et des pizzas à la maison.',
        'de': 'Kommissioniert Bestellungen präzise und sorgt dafür, dass alles ordentlich bereitsteht. Arbeitet ruhig, macht einfach sein Ding und mag es unkompliziert. Macht im Lager alles fertig und zu Hause einfach Pizza.'},
    'Altijd goedgezind en altijd in beweging in het magazijn. Zorgt dat elke bestelling klaarstaat voor vertrek. Na de uren vind je hem terug op het voetbalveld.': {
        'en': 'Always cheerful and always on the move in the warehouse. Makes sure every order is ready to go. After hours you will find him on the football pitch.',
        'fr': 'Toujours de bonne humeur et toujours en mouvement dans l’entrepôt. Veille à ce que chaque commande soit prête au départ. Après le travail, on le retrouve sur le terrain de foot.',
        'de': 'Immer gut gelaunt und immer in Bewegung im Lager. Sorgt dafür, dass jede Bestellung versandbereit ist. Nach Feierabend findest du ihn auf dem Fußballplatz.'},

    # ---- ambassadors ----
    'Artiesten die met ons meedenken, workshops geven en het merk uitdragen in heel Europa.': {
        'en': 'Artists who think along with us, give workshops and carry the brand across Europe.',
        'fr': 'Des artistes qui réfléchissent avec nous, animent des ateliers et portent la marque dans toute l’Europe.',
        'de': 'Künstler, die mit uns mitdenken, Workshops geben und die Marke in ganz Europa vertreten.'},

    # ---- principe + bezoek ----
    'Waar we voor staan': {'en': 'What we stand for', 'fr': 'Ce que nous défendons', 'de': 'Wofür wir stehen'},
    'Liever iemand spreken dan een formulier invullen? Dat kan. Je vindt ons in Genk.': {
        'en': 'Rather talk to someone than fill in a form? You can. You will find us in Genk.',
        'fr': 'Vous préférez parler à quelqu’un plutôt que remplir un formulaire ? C’est possible. Vous nous trouverez à Genk.',
        'de': 'Lieber mit jemandem sprechen als ein Formular ausfüllen? Gern. Du findest uns in Genk.'},
    'Openingsuren': {'en': 'Opening hours', 'fr': 'Heures d’ouverture', 'de': 'Öffnungszeiten'},
    'Maandag tot donderdag, 10u tot 16u': {
        'en': 'Monday to Thursday, 10:00 to 16:00', 'fr': 'Du lundi au jeudi, de 10:00 à 16:00', 'de': 'Montag bis Donnerstag, 10:00 bis 16:00'},
    'Lunchpauze van 12u tot 13u. Gesloten op vrijdag, in het weekend en op feestdagen.': {
        'en': 'Lunch break from 12:00 to 13:00. Closed on Fridays, at weekends and on public holidays.',
        'fr': 'Pause déjeuner de 12:00 à 13:00. Fermé le vendredi, le week-end et les jours fériés.',
        'de': 'Mittagspause von 12:00 bis 13:00. Freitags, am Wochenende und an Feiertagen geschlossen.'},
    'Online bestellingen afhalen kan van maandag tot donderdag tussen 10u en 12u en tussen 13u en 16u. We contacteren je zodra je bestelling klaarstaat.': {
        'en': 'You can collect online orders from Monday to Thursday between 10:00 and 12:00 and between 13:00 and 16:00. We contact you as soon as your order is ready.',
        'fr': 'Les commandes en ligne peuvent être retirées du lundi au jeudi entre 10:00 et 12:00 et entre 13:00 et 16:00. Nous vous contactons dès que votre commande est prête.',
        'de': 'Online-Bestellungen kannst du montags bis donnerstags zwischen 10:00 und 12:00 und zwischen 13:00 und 16:00 abholen. Wir melden uns, sobald deine Bestellung bereitliegt.'},
    'Waar je ons vindt': {'en': 'Where to find us', 'fr': 'Où nous trouver', 'de': 'Hier findest du uns'},
    '3600 Genk, Belgi&euml;': {'en': '3600 Genk, Belgium', 'fr': '3600 Genk, Belgique', 'de': '3600 Genk, Belgien'},
    'Een vraag stellen via de helpdesk': {
        'en': 'Ask a question through the helpdesk', 'fr': 'Poser une question via le helpdesk', 'de': 'Eine Frage über den Helpdesk stellen'},

    # ---- afsluiter ----
    'Shop het volledige gamma, schrijf je in voor een workshop, of stel je vraag gewoon rechtstreeks aan de mensen hierboven. We antwoorden sneller dan je denkt.': {
        'en': 'Shop the full range, sign up for a workshop, or simply ask the people above your question directly. We answer faster than you think.',
        'fr': 'Découvrez toute la gamme, inscrivez-vous à un atelier ou posez simplement votre question directement aux personnes ci-dessus. Nous répondons plus vite que vous ne le pensez.',
        'de': 'Entdecke das ganze Sortiment, melde dich für einen Workshop an oder stell deine Frage einfach direkt an die Menschen oben. Wir antworten schneller, als du denkst.'},
    'Naar de shop': {'en': 'Go to the shop', 'fr': 'Vers la boutique', 'de': 'Zum Shop'},
    'Bekijk de workshops': {'en': 'See the workshops', 'fr': 'Voir les ateliers', 'de': 'Workshops ansehen'},
    'Contacteer ons': {'en': 'Contact us', 'fr': 'Nous contacter', 'de': 'Kontakt'},
    'Sempertex Europe, ons team': {'en': 'Sempertex Europe, our team', 'fr': 'Sempertex Europe, notre équipe', 'de': 'Sempertex Europe, unser Team'},
}
