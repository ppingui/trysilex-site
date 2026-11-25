> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/da/privatliv/

# Privatlivspolitik

Dette er en oversættelse. Hvis den afviger fra den [engelske version](https://trysilex.com/privacy/), er det den engelske version, der gælder.

Senest opdateret: 25. november 2026. Den engelske version på trysilex.com er originalen. Den erstatter den kopi hos Notion, som ældre versioner af appen linker til.

Silex er bygget på ét princip: **din bedring er ingens datasæt.**

*Vi* gemmer intet om dig på nogen server, har ingen konti og har ingen mulighed for at læse noget af det, du skriver i appen. (Den eneste kode, vi kører på servere, er to valgfrie værktøjer, der intet har med appen at gøre: Notion-forbindelsen i afsnit 14 og Silex Help i afsnit 15. Ingen af dem gemmer noget.) To tredjeparter driver servere, der modtager noget: en analysetjeneste får tilsendt *navnene* på de skærme, du når til, og en tjeneste til annoncemåling får at vide, at appen blev installeret, og om det førte til en prøveperiode eller et køb. Én kontakt i Indstillinger stopper begge dele. Denne side forklarer præcis, hvad det betyder, også de få steder, hvor data faktisk forlader din telefon, for en privatlivspolitik, der kun nævner det beroligende, er ikke en privatlivspolitik.

Teksten er skrevet, så den opfylder EU's databeskyttelsesforordning (GDPR) og Storbritanniens udgave af den (UK GDPR). Befinder du dig i EØS eller Storbritannien, gælder afsnittene om retsgrundlag, overførsler og dine rettigheder fuldt ud for dig.

## 1. Det, du indtaster, bliver på din enhed

Alt, hvad du registrerer – svar på spørgsmålene, check-ins, refleksioner i dagbogen, svar i programmet, logget trang, smuttere, datoer for dine dage i træk, beløb, din underskrift og din samling af sfærer – gemmes to steder, og begge tilhører dig:

- **På din iPhone**, i appens lokale database.
- **I din private iCloud**, i den private database i Apples CloudKit, så din historik overlever, hvis telefonen bliver væk eller udskiftet.

Kun din Apple-konto har adgang til din private iCloud-database. Vi er ikke part i den og kan ikke læse den. Hvis iCloud ikke er tilgængelig eller er slået fra, gemmer appen kun data på din enhed.

**Vi modtager aldrig dette indhold.** Der er intet API-kald, der sender det, ingen sikkerhedskopi hos os og ingen nøgle, der ville lade os dekryptere det. Fordi vi hverken har adgang til det eller mulighed for at bruge det, anser vi os ikke for at være dataansvarlige for det, du skriver i appen. Det er du. Vi beskriver det her af hensyn til åbenheden, ikke fordi vi behandler det.

## 2. Hvad der faktisk når frem til andre

Seks snævre tilfælde, som alle er valgfrie eller teknisk uundgåelige.

### Køb: Apple og RevenueCat

Abonnementer håndteres af Apple. Vi bruger RevenueCat til at kontrollere og administrere abonnementets status. RevenueCat er vores databehandler og modtager:

- enhedstype og styresystem,
- hvornår appen sidst var i brug, og Apples kvitteringsfiler,
- eventuelt en brugeridentifikator og metadata om attribution (hvor du kom fra).

Så længe »Del anonym brug« er slået til, sender RevenueCat også oplysningen om, at en prøveperiode eller et køb har fundet sted, og prisen, videre til AppsFlyer, så det kan tælle med under en annoncekampagne. Se *Annoncemåling* nedenfor.

RevenueCat modtager aldrig din dagbog, dine svar, dine dage i træk eller noget andet indhold om din bedring. Se [Apples privatlivspolitik](https://www.apple.com/legal/privacy/) og [RevenueCats privatlivspolitik](https://www.revenuecat.com/privacy/).

### DNS-skjoldet: kun hvis du slår det til

Skjoldet installerer en konfiguration til krypteret DNS (DoH), så spildomæner ikke kan slås op i dine apps og browsere. Mens det er slået til, besvares din enheds DNS-opslag af [Mullvads offentlige DNS-server](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls) efter deres [politik om ikke at logge](https://mullvad.net/en/help/no-logging-data-policy/). Øvede brugere kan i stedet pege det mod deres egen NextDNS-konfiguration. Mullvad eller NextDNS er selvstændigt dataansvarlige for de opslag efter deres egne politikker. Vi er ikke inde over opslagene og ser aldrig, hvad du browser. Slår du skjoldet fra i iPhonens Indstillinger, stopper det med det samme.

### Opdatering af blokeringslisten

Appen henter med mellemrum offentlige lister over spildomæner fra jsDelivr og GitHub. Som ved enhver download af en fil kan de servere se anmodningen og din IP-adresse. Anmodningen indeholder ingen identifikator og intet om dig eller din bedring.

### Brugstal: optællingen på din enhed

Appen fører sin egen optælling af, *hvordan appen bliver brugt* (for eksempel hvor mange gange en skærm blev åbnet en bestemt dag), gemt som antal pr. dag i én enkelt fil i appens eget lager. Den indeholder ingen identifikatorer og intet indhold, du har skrevet, og **den fil forlader aldrig din telefon**. Sletter du appen, forsvinder filen. De samme *navne* på hændelser sendes separat til TelemetryDeck, medmindre du slår det fra. Det er næste afsnit, og det er den ærlige grund til, at der ikke længere står »når ingen« her.

### Brugsanalyse: TelemetryDeck, medmindre du slår det fra

For at se, hvor folk falder fra i introduktionen (det er forskellen på at rette en skærm og at gætte sig frem), sender appen *navnene* på de trin, den når til, til **TelemetryDeck GmbH**, Von-der-Tann-Str. 54, 86159 Augsburg, Tyskland. Der sendes:

- **navnet** på hvert trin, der nås i introduktionen, og dets plads i rækkefølgen (`funnel.question_04`, `funnel.paywall`), hver højst én gang pr. installation,
- **navnene** på andre hændelser i appen, for eksempel at en programdag er gennemført, eller at panikknappen er åbnet, og intet om dem ud over navnet,
- TelemetryDecks egne standardoplysninger: styresystemets version, enhedsmodel, sprog- og landeindstilling, region, appversion og lignende,
- en tilfældig identifikator, som appen laver til netop denne installation.

Vi lægger også de hændelsesnavne sammen til nogle få løbende totaler, som appen viser i introduktionen, for eksempel hvor mange programdage folk har gennemført. En total siger intet om nogen enkelt person.

Det, der aldrig sendes: dine svar på spørgsmålene, din PGSI-score, hvor meget du spiller for om ugen, teksten i din dagbog, dine smuttere eller noget andet, du har skrevet eller valgt. Signalet er, at en skærm blev nået, aldrig hvad der stod på den, og aldrig hvad du skrev i den.

**Om den identifikator.** Det er et tilfældigt UUID, som appen laver ved første start. Det er med vilje *ikke* `identifierForVendor`, den identifikator, iOS ellers ville have brugt, fordi den overlever, at appen slettes og installeres igen, og deles med alle andre apps fra den samme udvikler. Vores deles med ingenting og forsvinder, når du sletter appen. Inden den forlader din telefon, hashes den med et salt på enheden. Når den kommer frem, tilføjer TelemetryDeck sit eget salt og hasher den igen, så hverken vi eller de kan regne sig tilbage fra den gemte værdi til den oprindelige. En enkelt hash ville kun være pseudonymisering, og derfor laver de en til.

Vi slår også to ting fra, som TelemetryDeck ellers ville indsamle: signalet om, at en session er begyndt, og sessionsstatistik.

**Kontakten.** Indstillinger → Dine data → **Del anonym brug**. Den er **slået til som standard**, og grunden er ikke en pænt pakket undskyldning: hvis målingen krævede, at man først sagde ja, ville den måle de forkerte mennesker. De, der stopper på den første skærm, er præcis dem, der aldrig når frem til et spørgsmål om samtykke, så det frafald, vi prøver at måle, ville i sig selv gøre stikprøven skæv. Prisen for det valg er at sige rent ud, hvad der sendes, og det er det, dette afsnit er til for. Når du slår den fra, stopper nye signaler med det samme, den del af appen, der sender dem, kobles fra, og den bunke usendte signaler, der venter på enheden, slettes. Det, der allerede er sendt, kan ikke kaldes tilbage, og intet i det peger tilbage på dig.

Se [TelemetryDecks privatlivspolitik](https://telemetrydeck.com/privacy/).

### Annoncemåling: AppsFlyer, under den samme kontakt

Vi annoncerer for Silex, og en annonce er kun pengene værd, hvis de, der installerer på grund af den, også bruger appen. For at tælle det indeholder appen et SDK fra **AppsFlyer Ltd.**, 14 Maskit St., Herzliya, Israel. AppsFlyer modtager:

- at appen blev installeret og åbnet, og hvornår,
- en identifikator, som AppsFlyers SDK laver til denne installation af denne app,
- AppsFlyers standardoplysninger om enheden: enhedsmodel, styresystemets version, sprog, appversion og oplysninger om netværket (wi-fi eller mobilselskab). Som enhver server ser AppsFlyers server din IP-adresse, og AppsFlyer oplyser, at den kan blive omsat til en omtrentlig region,
- **navnene** på tre hændelser og intet om dem: at skærmen med abonnementer blev vist, at en gratis prøveperiode begyndte, at et køb blev gennemført,
- fra RevenueCat: at en prøveperiode eller et køb har fundet sted, og prisen, knyttet til den samme installationsidentifikator.

Sådan matches en installation med en annonce: gennem Apples egne aggregerede rapporter, altså samlede tal (SKAdNetwork og AdAttributionKit), som nævner en *kampagne* og aldrig en person. Apple sender dem til annoncenetværket, og iOS sender AppsFlyer en kopi. Der er én undtagelse, som begyndte den 22. november 2026: se »Annoncer hos Meta« nedenfor.

Annoncer i selve App Store fungerer lidt anderledes. Til dem giver iOS appen en engangskode (Apples AdServices), og AppsFlyer og RevenueCat bruger den hver for sig hos Apple til at få oplyst den kampagne og det søgeord, der førte til installationen. Koden identificerer trykket på annoncen, ikke dig.

Hvad der ikke er med, og det er bygget ind, ikke bare lovet: **intet annonce-id.** Appen viser aldrig spørgsmålet om at tillade sporing, den bruger den udgave af AppsFlyers SDK, hvor koden til annonce-id er fjernet, og den slår indsamlingen fra for `identifierForVendor`, den eneste identifikator, der deles mellem apps fra den samme udvikler. Intet, du har skrevet eller valgt, sendes. Det er den samme liste som ovenfor.

**Én ting er anderledes end ved identifikatoren i analysen, og det siger vi hellere højt.** AppsFlyers identifikator hashes ikke på din telefon, sådan som TelemetryDecks gør, og AppsFlyers SDK gemmer en lille markering i iPhonens nøglering, så det kan skelne en geninstallation fra en ny installation. Poster i nøgleringen kan blive liggende, efter at en app er slettet. For AppsFlyer, i modsætning til TelemetryDeck, påstår vi derfor ikke, at en geninstallation ligner en fremmed.

**Kontakten** er den samme: Indstillinger → Dine data → **Del anonym brug**, slået fra. Så stopper SDK'ets anmodninger, AppsFlyers identifikator fjernes fra RevenueCat, så der ikke sendes flere købshændelser videre, og anmodninger, der venter på enheden, slettes. AppsFlyer har også sin egen formular til fravalg: [appsflyer.com/legal/opt-out](https://www.appsflyer.com/legal/opt-out/). Se [AppsFlyers privatlivspolitik for tjenesterne](https://www.appsflyer.com/legal/services-privacy-policy/).

### Annoncer hos Meta: fra den 22. november 2026

Vi begynder at annoncere på Facebook og Instagram. Metas installationskampagner til iPhone-apps tæller kun installationer med Metas egen metode (Meta kalder den Aggregated Event Measurement), og den metode har brug for oplysninger fra appen. At tælle alene med Apples aggregerede rapporter blev ikke tilbudt os. Derfor sender AppsFlyer fra den 22. november 2026 en del af det, det modtager, videre til Meta (**Meta Platforms Ireland Ltd.** for folk i Europa, **Meta Platforms, Inc.** andre steder):

- at appen blev installeret, og hver gang den åbnes, for hver installation, hvor kontakten er slået til, uanset om en annonce havde noget med det at gøre,
- for installationer, som AppsFlyer tilskriver en af vores Meta-annoncer: navnene på de tre hændelser ovenfor,
- sammen med hver af disse: AppsFlyers identifikator for installationen, den IP-adresse, anmodningen kom fra, samt enhedsmodel og iOS-version.

Det, der stadig ikke sendes: navn, e-mailadresse, annonce-id, `identifierForVendor` eller noget, du har skrevet eller valgt i appen.

**Hvad det ændrer, sagt lige ud.** Før denne dato nåede intet om en enkelt installation frem til en annoncevirksomhed. Nu modtager Meta én post pr. installation. Ifølge sine vilkår må Meta matche sådan en post med en person, der bruger Facebook eller Instagram, bruge den til at måle vores annoncer og til at bestemme, hvem der får vist annoncer, og beholde den i op til to år. Posten siger, at en enhed installerede en app til folk, der vil stoppe med at spille om penge. Det er netop den slags oplysning, afsnit 3 behandler med varsomhed. Delingen kører kun, mens vi annoncerer hos Meta: hvis vi stopper, eller hvis Meta lader en kampagne for Silex tælles alene med Apples aggregerede rapporter, slår vi den fra og skriver datoen her. Det, Meta da har modtaget, forbliver under Metas vilkår, og vi kan ikke trække det tilbage.

**Kontakten dækker også dette.** Indstillinger → Dine data → **Del anonym brug**, slået fra: så modtager AppsFlyer intet mere fra din telefon og har derfor intet at sende videre. Vil du spørge Meta om det, de allerede har, så brug værktøjerne i din Facebook- eller Instagram-konto, eller [Metas privatlivspolitik](https://www.facebook.com/privacy/policy/).

Med App Stores egne ord angiver appen **ingen sporing** (`NSPrivacyTracking` false, ingen sporingsdomæner) og tre indsamlede datatyper – Interaktion med produkter, Enheds-id og Købshistorik – alle markeret som *ikke knyttet til din identitet* og *ikke brugt til sporing*, med formålene analyse og måling af vores egen annoncering (Købshistorik også for at kunne levere abonnementet).

**Intet andet.** De fem netværksveje ovenfor er de eneste, appen har. Der er ingen annonce-id'er, og vi laver ingen profilering og træffer ingen automatiske afgørelser, der har retsvirkning eller på tilsvarende vis betydeligt påvirker dig. Så længe delingen med Meta ovenfor er slået til, er den det ene sted, hvor en post om din installation kan blive lagt sammen med det, en anden virksomhed allerede ved om dig. Erklæringen i stykket ovenfor blev skrevet, før delingen begyndte. Vi undersøger, om den skal ændres, og en eventuel ændring nævnes i afsnit 11.

### Et par ord til andre: kun hvis du sender dem

Når du har gennemført programdag 7, kan appen én gang spørge, om du vil dele en sætning til en, der lige er begyndt. Vælger du at gøre det, åbner den en e-mail i din egen mailapp, adresseret til os, med dine ord, din første initial, dit antal dage og dit samtykke. Du kan ændre eller slette alt i den, før du sender, og intet forlader din enhed, medmindre du trykker på send.

Vi modtager så den e-mail og din adresse i en postkasse hos Google. Vi kan vise dine ord, din første initial og dit antal dage i appen og på vores sider i appbutikkerne. Vi offentliggør aldrig din e-mailadresse. Skriv til os når som helst, så holder vi op med at bruge dine ord: de fjernes fra butikssiderne og i den næste version af appen, og vi sletter e-mailen, medmindre vi er nødt til at beholde den for at kunne vise, hvad du sagde ja til.

## 3. Retsgrundlag (GDPR art. 6 og art. 9)

| Hvad | Formål | Retsgrundlag |
|---|---|---|
| Køb og abonnementsstatus (via Apple og RevenueCat) | Levere og gendanne det abonnement, du har købt, og forhindre, at nogen får adgang på et falsk grundlag | **Art. 6, stk. 1, litra b** – opfyldelse af en kontrakt med dig |
| IP-adressen, som er synlig for blokeringslistens netværk til indholdslevering (CDN), når appen henter en liste | Levere den blokering, appen er til for | **Art. 6, stk. 1, litra f** – legitime interesser (at holde beskyttelseslisterne opdateret). Vores vurdering: minimale data, ingen profilering, ingen kobling til dig |
| Hændelsesnavne, en hashet identifikator, der kun gælder installationen, og TelemetryDecks standardoplysninger om enheden, så længe »Del anonym brug« er slået til | Se, hvor folk falder fra i introduktionen, så de skærme, der taber dem, kan rettes, og vise de løbende totaler, der er beskrevet ovenfor | **Art. 6, stk. 1, litra f** – legitime interesser (at få appen til at virke for dem, den er lavet til). Vores vurdering: intet indhold, intet annonce-id, en identifikator, der ikke kan følge dig mellem apps eller overleve, at appen slettes, og en kontakt i Indstillinger, der stopper det. Det er kontakten, der bærer interesseafvejningen: en interesse, du kan sige nej til med ét tryk, er ikke en, der gøres gældende hen over hovedet på dig |
| En AppsFlyer-installationsidentifikator, AppsFlyers standardoplysninger om enheden, tre hændelsesnavne og hændelser om prøveperiode og køb, så længe »Del anonym brug« er slået til | Vide, hvilke af vores annoncer der fører til, at folk faktisk bruger appen, så vi holder op med at betale for dem, der ikke gør | **Art. 6, stk. 1, litra f** – legitime interesser (at annoncere for en app, der skal hjælpe folk fri af pengespil, uden at spilde det, der finansierer den). Vores vurdering: intet annonce-id, intet indhold, matchning med annoncer kun gennem Apples aggregerede kampagnerapporter (bortset fra delingen med Meta i næste række) og den samme kontakt i Indstillinger, der stopper det |
| Fra den 22. november 2026, så længe vi annoncerer hos Meta: de poster om installation og åbning af appen, som AppsFlyer sender videre til Meta, med AppsFlyers installationsidentifikator, IP-adresse, enhedsmodel og iOS-version (afsnit 2, »Annoncer hos Meta«) | Lade Meta tælle de installationer, dets annoncer fører til, hvilket dets installationskampagner til iPhone kræver | **Art. 6, stk. 1, litra f** – legitime interesser, og den svageste brug af det grundlag i denne tabel: posten går til en virksomhed, der kan matche den med en konto. Vores vurdering hviler på, at intet af det, du har registreret, er med i den, at det kun kører, mens vi annoncerer hos Meta, og at den samme kontakt stopper det |
| DNS-opslag, mens skjoldet er slået til | Blokere spildomæner på hele enheden | **Art. 6, stk. 1, litra a** – dit samtykke, som du giver ved at slå skjoldet til og godkende dialogboksen fra iOS. Du kan til enhver tid trække det tilbage ved at slå skjoldet fra |
| Et par ord, du vælger at sende os på e-mail til offentliggørelse | Vise folk, der lige er begyndt, at andre har været her | **Art. 6, stk. 1, litra a, og art. 9, stk. 2, litra a** – dit udtrykkelige samtykke, som du giver ved at slå accepten til og sende e-mailen. Det kan trækkes tilbage til enhver tid |
| Det, du skriver i appen | Levere bedringsprogrammet til dig på din egen enhed | Vi modtager det ikke, så vi foretager ingen behandling, der skal begrundes. I det omfang det overhovedet behandles, sker det på din enhed under din kontrol |

**Særlige kategorier af personoplysninger (helbredsoplysninger).** Det, du registrerer her, afslører oplysninger om helbred og om en mulig adfærdsafhængighed, og det er en særlig kategori af personoplysninger efter **art. 9**. Det er netop derfor, appen er designet, som den er: de oplysninger når aldrig frem til os, så vi støtter os aldrig på en betingelse i art. 9 for dem. Den eneste undtagelse er et par ord, du vælger at sende os på e-mail til offentliggørelse: de kan afsløre det samme, så for dem støtter vi os på dit udtrykkelige samtykke efter art. 9, stk. 2, litra a.

Det sværere spørgsmål er analysen, og vi vil hellere arbejde os igennem det end vifte det væk. Et signal, der lyder `funnel.question_04`, rummer intet indhold. Men Silex er en app til folk, der vil fri af pengespil, og EU-Domstolen har fastslået, at data, der kun *indirekte* afslører en særlig kategori, alligevel er omfattet (sag C-184/20, *OT*). Vi påstår derfor ikke, at signalerne er uskyldige i kraft af deres emne: »denne installation gik ind i introduktionen i Silex« siger noget, der ligger tæt på helbred, om den, der holdt telefonen. Det, vi støtter os på, er den anden halvdel af art. 9, som gælder oplysninger om en **identificeret eller identificerbar** fysisk person. Den identifikator, der følger med signalerne, er tilfældig, lavet til én enkelt installation, saltet og hashet på din enhed og derefter saltet igen med TelemetryDecks eget salt og hashet på ny, når den kommer frem. Derfor kan ingen part, heller ikke vi, regne sig tilbage til en person eller matche den med noget andet. På det grundlag behandler vi det, der når frem til TelemetryDeck, som liggende uden for art. 9, men stadig som pseudonymiserede personoplysninger efter art. 6 med et retsgrundlag og en fravalgsmulighed, der virker. Skal vi tage fejl, gør vi det hellere med den mere forsigtige af de to læsninger. For en abonnementskvittering er intet ændret: den afslører ingen helbredstilstand ud over, at du har købt en app.

Det, der når frem til AppsFlyer, klarer den prøve dårligere, og vi behandler det derefter. Dets identifikator er tilfældig og gælder kun denne app, men den er ikke hashet to gange, og den kommer frem sammen med en enhedsmodel, en IP-adresse og købshændelser. Vi behandler den som pseudonymiserede personoplysninger hos en databehandler under dens tillæg om databehandling (afsnit 4), på det grundlag i art. 6, der står i tabellen, og med den samme mulighed for at sige nej. Den siger »denne installation kom til Silex og begyndte en prøveperiode«. Den siger ikke, hvem du er, og den indeholder intet, du har registreret i appen.

Dette er det eneste stykke på siden, hvor dygtige jurister med rimelighed kan nå til forskellige resultater, og det vil vi hellere sige end lade det fremstå som afgjort.

## 4. Internationale overførsler

**RevenueCat** er en amerikansk virksomhed (Brandon, Florida), der opbevarer data hos Amazon Web Services i USA. Overførslerne er dækket af dens databehandleraftale, som indeholder Europa-Kommissionens **standardkontraktbestemmelser** (gennemførelsesafgørelse (EU) 2021/914), **modul to: fra dataansvarlig til databehandler**. For Storbritannien anvender den desuden ICO's **International Data Transfer Addendum** af 21. marts 2022 og for Schweiz standardkontraktbestemmelserne tilpasset den schweiziske databeskyttelseslov (FADP). RevenueCat er **ikke** certificeret under databeskyttelsesrammen mellem EU og USA (EU–US Data Privacy Framework). Det er standardkontraktbestemmelserne, der er mekanismen. *Kontrolleret mod RevenueCats offentliggjorte databehandleraftale den 6. august 2026.*

**TelemetryDeck** er en tysk virksomhed (TelemetryDeck GmbH, Augsburg). Den oplyser, at brugsdata **udelukkende opbevares inden for Den Europæiske Union**, på Hetzners infrastruktur i Nürnberg, at dele af kæden stadig kører på Azure i Amsterdam og AWS i Frankfurt, og at planen er at samle det hele hos Hetzner i løbet af 2026. Virksomhedens egen privatlivspolitik nævner disse parter som Hetzner Online GmbH (Tyskland), Microsoft Ireland Operations Ltd (Irland) og Amazon Web Services, Inc. (Seattle, USA). AWS-selskabet er altså amerikansk, men regionen, det opbevarer i, er Frankfurt. Efter TelemetryDecks egen beskrivelse forlader ingen af vores analysedata derfor EØS, og **ingen overførselsmekanisme efter kapitel V bliver relevant**, fordi der ikke er nogen overførsel til et tredjeland at dække. Vi har ikke selv kontrolleret, hvor dataene opbevares, og det kan vi ikke. Vi gengiver, hvad TelemetryDeck offentliggør.

Én ting kan vi ikke give dig, og det er derfor, denne omtale er længere end RevenueCats. **TelemetryDeck tilbyder ingen databehandleraftale efter art. 28.** Dens vilkår for databehandling er automatisk en del af brugsvilkårene, så der er intet at underskrive. Men de siger, at den handler »hverken som databehandler i betydningen i GDPR artikel 4, nr. 8, eller som fælles dataansvarlig« (vores oversættelse), og at artikel 26 og 28 ikke gælder, fordi det, den modtager, er anonymt og ikke personoplysninger. Vi har ikke tilsluttet os den holdning: vi behandler den hashede installationsidentifikator som pseudonymiserede personoplysninger, giver den et grundlag i art. 6 og en fravalgsmulighed alligevel (afsnit 3) og beskriver TelemetryDeck som databehandler i realiteten, fordi det er det, den gør. Den følge, du bør kende, er, at de garantier, en aftale efter art. 28 ville rumme (dokumenterede instrukser, ret til revision, en kontraktlig pligt til at slette), ikke kan fås fra denne leverandør, fordi den afviser den rolle, der skaber dem. *Kontrolleret mod TelemetryDecks offentliggjorte privatlivspolitik, databehandlingsaftale og sider om arkitektur og sikkerhed den 17. august 2026.*

**AppsFlyer** er en israelsk virksomhed (AppsFlyer Ltd., Herzliya). Israel er omfattet af en afgørelse fra Europa-Kommissionen om tilstrækkeligt beskyttelsesniveau (2011/61/EU). AppsFlyers tillæg om databehandling angiver den som **databehandler** og os som dataansvarlig, og dens offentliggjorte liste over underdatabehandlere nævner Amazon Web Services og Google Cloud i »EU/USA« som dens hostingudbydere. For overførsler uden for lande med et tilstrækkeligt beskyttelsesniveau indeholder tillægget **standardkontraktbestemmelserne** (gennemførelsesafgørelse (EU) 2021/914), **modul to: fra dataansvarlig til databehandler**, og for Storbritannien ICO's **International Data Transfer Addendum**. Vi har ikke kontrolleret, i hvilken region vores data opbevares. *Kontrolleret mod AppsFlyers offentliggjorte tillæg om databehandling (februar 2023), liste over underdatabehandlere og privatlivspolitik for tjenesterne den 19. november 2026.*

**Meta**, for den deling, der er beskrevet i afsnit 2. Meta Platforms Ireland Ltd. ligger i EU og overfører data til Meta Platforms, Inc. i USA efter Metas egne vilkår for overførsel. Efter Metas vilkår for virksomhedsværktøjer (Business Tools Terms) er Meta vores databehandler, når den matcher og måler, og fælles dataansvarlig med os, når den bruger det, den modtager, til at bestemme, hvem der ser annoncer. *Læst i Metas Business Tools Terms den 20. november 2026. Vi har ikke kontrolleret Metas overførselsmekanisme ud over det, de vilkår siger.*

**Apple**: se Apples privatlivspolitik for dens egne garantier ved overførsel. Dine private iCloud-data er underlagt Apples vilkår og overføres ikke af os, fordi vi aldrig har dem.

**Os.** Vi er etableret i Ukraine, som ligger uden for EØS og ikke er omfattet af en afgørelse fra Europa-Kommissionen om tilstrækkeligt beskyttelsesniveau. Når du giver oplysninger direkte til os, er det en direkte indsamling og ikke en overførsel efter kapitel V (efter EDPB's retningslinjer 05/2021 om samspillet mellem art. 3 og kapitel V). I praksis er der næsten intet at indsamle: der er ingen konto, og de eneste personoplysninger, vi kan se, er den pseudonymiserede abonnementspost i RevenueCats oversigt, de samlede antal i TelemetryDecks og posterne pr. installation i AppsFlyers.

## 5. Hvor længe noget opbevares

- **På din enhed og i din private iCloud:** indtil du sletter det. Vi kan ikke slette det for dig, og vi kan ikke forhindre dig i at slette det.
- **På vores systemer:** intet. De to små tjenester i afsnit 14 og 15 gemmer ingen oplysninger. De tredjepartsservere, der har noget, som er vores, er RevenueCats, TelemetryDecks og AppsFlyers. Se nedenfor.
- **Et par ord, du har sendt os på e-mail til offentliggørelse:** så længe vi bruger dine ord, indtil du beder os om at stoppe. Se afsnit 2.
- **Købsoplysninger:** opbevares af Apple og RevenueCat efter deres egne opbevaringsplaner og i det omfang, skatte- og regnskabslovgivning kræver det.
- **Brugstal på din enhed:** forsvinder, når appen slettes.
- **Poster om installation og hændelser hos AppsFlyer:** dens privatlivspolitik for tjenesterne siger, at den ikke opbevarer slutbrugeres data i mere end **24 måneder**. En post kan slettes før gennem AppsFlyers egen formular (afsnit 2).
- **Poster om installation og åbning af appen, der er sendt videre til Meta** (afsnit 2, »Annoncer hos Meta«): Metas vilkår tillader den at beholde dem i op til **to år**.
- **Hændelsesnavne hos TelemetryDeck:** **den offentliggør ingen plan for sletning af dem.** Dens prisplaner angiver en opbevaringsperiode (90 dage på gratisniveauet, længere på de betalte), men det er et *forespørgselsvindue*: hvor langt tilbage dens oversigter kan se. Data, der er ældre end vinduet, flyttes til koldt lager (cold storage) i stedet for at blive slettet og kan indlæses igen. TelemetryDeck siger, at sletning, enten en enkelt gang eller efter en plan, kan aftales på anmodning. Vi har ikke aftalt nogen, så gå ud fra, at signalerne bliver liggende på ubestemt tid. Da de er antal uden nogen identifikator, der fører tilbage til dig, er det mindre alvorligt, end det lyder, men det er den korrekte oplysning, og vi skriver den hellere end et tal, vi har fundet på.

## 6. Hvem der er ansvarlig

**Dataansvarlig:** Kyrylo Lozovyi
**Adresse:** Vidpochinku 12, Kyiv, Ukraine
**Kontakt om privatliv:** [support@trysilex.com](mailto:support@trysilex.com) (kan også kontaktes på [stopgamblesupport@gmail.com](mailto:stopgamblesupport@gmail.com), den adresse, der vises i de nuværende versioner af appen)

Vi har ikke udpeget en databeskyttelsesrådgiver. Det har vi ikke pligt til, fordi vi ikke foretager overvågning i stort omfang og ikke har særlige kategorier af personoplysninger på vores systemer (se afsnit 3).

## 7. Dine rettigheder

Befinder du dig i EØS eller Storbritannien, har du ret til **indsigt** i dine data, til **berigtigelse**, til **sletning**, til **begrænsning** af behandlingen, til **dataportabilitet**, til at gøre **indsigelse** mod behandling, der er baseret på legitime interesser, og til når som helst at **trække dit samtykke tilbage**, hvor samtykke er grundlaget (DNS-skjoldet: træk det tilbage ved at slå skjoldet fra; det påvirker ikke behandling, der allerede er sket).

**En ærlig begrænsning.** For næsten alt, hvad denne app rører ved, har vi ingen oplysninger, der kan identificere dig, og ingen konto, der kunne forbinde en anmodning med en person. Efter **GDPR art. 11** har vi ikke pligt til at indhente ekstra oplysninger blot for at identificere dig, og vi beder dig ikke om identitetspapirer for at behandle en anmodning, vi ikke har data til at besvare. I praksis:

- **Indhold, du har skrevet:** udøv rettighederne direkte. Det ligger på din enhed og i din iCloud, og når du sletter appen (plus kopien i iCloud), er det slettet helt.
- **Købsdata:** kontakt Apple, eller kontakt os, så sender vi anmodningen videre til RevenueCat, som er vores databehandler.
- **Brugsanalyse:** din **ret efter art. 21 til at gøre indsigelse** mod vores legitime interesser har en kontakt i stedet for en supportkø: Indstillinger → Dine data → **Del anonym brug**, slået fra. Så stopper nye signaler med det samme, den del af appen, der sender dem, kobles fra, og den bunke, der venter på enheden, slettes. Du behøver ikke skrive til os, og du behøver ikke give en grund. Det, der allerede er sendt, kan ikke trækkes tilbage, og det kan heller ikke findes igen, fordi intet i det identificerer dig.
- **Annoncemåling:** den samme kontakt er også din indsigelse mod dette. Vil du have det, AppsFlyer allerede har om din installation, slettet, så brug AppsFlyers egen formular (afsnit 2). Vi kan ikke slå din installation op for dig, af grunden ovenfor: vi har intet, der knytter en installation til en person.

Skriv til [support@trysilex.com](mailto:support@trysilex.com), så svarer vi inden for en måned, som art. 12, stk. 3, kræver.

**Retten til at klage.** Du kan klage til din nationale databeskyttelsesmyndighed. I Danmark er det [Datatilsynet](https://www.datatilsynet.dk/borger/klage/saadan-klager-du). Listen over myndigheder er på [edpb.europa.eu](https://edpb.europa.eu/about-edpb/board/members_en), og i Storbritannien er det [ICO](https://ico.org.uk/make-a-complaint/). Du behøver ikke kontakte os først, men vi vil sætte pris på, at du gør.

## 8. Slet det hele

- Slet appen fra din iPhone.
- Fjern kopien i iCloud: Indstillinger → dit navn → iCloud → Administrer kontolagringsplads → Silex.
- Opsig et abonnement: Indstillinger → dit navn → Abonnementer, eller linket Administrer abonnement i appen.

## 9. Følsomme oplysninger, og hvorfor designet er politikken

Det, du registrerer her, handler om dit helbred og din økonomi, og sådan behandler vi det. Der er ingen konti at bryde ind i, intet på nogen server hos os at kræve udleveret og intet hos nogen leverandør, der kunne læses som *din* bedring. Den stærkeste beskyttelse, vi kan give, er slet ikke at have dine data. Den del ligger i konstruktionen og er ikke bare et løfte: der er ingen nøgle, ingen sikkerhedskopi og ingen kopi, så der er intet, vi i stilhed kan ombestemme os om.

**Hvad der er ændret.** Indtil august 2026 stod der også her, at ingen analyseleverandør havde en kopi. Det passer ikke længere: TelemetryDeck har en optælling af, hvor mange installationer der nåede hver skærm. Det er en reel forringelse af garantien, og det vil vi ikke kalde noget andet. Det, der står tilbage, er den del, der gør arbejdet: indholdet bliver på din telefon, den identifikator, der følger med optællingerne, kan ikke knyttes til dig eller følges mellem apps, og det hele har en kontakt. Det, vi gav afkald på, er muligheden for at sige ordet *ingen*.

I november 2026 kom der en leverandør mere: AppsFlyer får at vide, at en installation har fundet sted, og om det førte til en prøveperiode eller et køb, så vi kan se, hvilke annoncer der er pengene værd. Det er en anden forringelse, og det samme står tilbage: intet, du har registreret, forlader din telefon, der er intet annonce-id, og kontakten dækker det.

Den 22. november 2026 kom en tredje, og det er den, vi bryder os mindst om: mens vi annoncerer på Facebook og Instagram, får Meta at vide, at en installation findes (afsnit 2, »Annoncer hos Meta«). Intet, du har registreret, forlader din telefon, og kontakten dækker det stadig, men så længe det varer, kan vi ikke længere sige, at ingen annoncevirksomhed får kendskab til en enkelt installation. Hvis det slutter, skriver vi datoen her.

## 10. Børn

Silex er beregnet til voksne og henvender sig ikke til børn. Vi indsamler ikke bevidst oplysninger fra nogen under 18 år. Aldersgrænsen i App Store er sat derefter.

## 11. Ændringer

Hvis denne politik ændres, ændres datoen øverst, og den gældende version findes altid på denne adresse.

At tilføje TelemetryDeck er en væsentlig ændring, og den tidligere version af dette afsnit lovede, at væsentlige ændringer ville blive vist i appen. **Vi har ændret det løfte i stedet for at påstå, at vi holdt det.** Appen har ingen funktion, der viser en besked ved en opdatering, og vi vil ikke beskrive en, der ikke findes. Det, denne version faktisk gør, er at sætte kontakten i Indstillinger med en tydelig beskrivelse af, hvad der sendes, lige ved siden af: synlig for enhver, der kigger, og ikke presset på nogen, der ikke gør. Det er mindre, end den gamle sætning lovede, og det er netop derfor, det var sætningen, der skulle ændres, og ikke beretningen om, hvad der skete.

At tilføje AppsFlyer i november 2026 er en væsentlig ændring af samme slags, og den kommer på samme måde: nævnt her og i versionsnoterne, under den kontakt, der allerede var der, og med teksten ved siden af kontakten ændret, så det fremgår.

Løftet lyder altså nu: væsentlige ændringer nævnes i dette afsnit og i versionsnoterne i App Store til den version, der indfører dem, og enhver ændring, der udvider, hvad der forlader din enhed, kommer i samme version som den kontakt, du styrer den med.

Delingen med Meta den 22. november 2026 er en væsentlig ændring, som dette løfte ikke forudså. Der forlader ikke noget nyt din enhed. Det, der er ændret, er, at AppsFlyer sender en del af det videre, og det blev slået til i AppsFlyers indstillinger, ikke i en version af appen. Der var derfor ingen versionsnoter at nævne det i. Det nævnes her den dag, det begyndte, den eksisterende kontakt dækker det, og noterne til den næste version vil nævne det.

## 12. Kontakt

[support@trysilex.com](mailto:support@trysilex.com)

## 13. Den gratis browserudvidelse

Denne tekst gælder også **Silex — Free Gambling Blocker**, browserudvidelsen til Chrome, Microsoft Edge og Firefox. Den er enklere end appen, og det er dette afsnit også:

- **Den indsamler intet.** Ingen konto, ingen analyse, ingen identifikatorer, og den sender ingen netværksanmodninger af sig selv. Intet om dig, eller om hvad du browser, sendes til os eller til nogen anden.
- **Sådan blokerer den.** Udvidelsen har en liste over spildomæner med sig. Din browser sammenligner de sider, du åbner, med den liste lokalt ved hjælp af den indbyggede funktion `declarativeNetRequest`. Browseren melder ikke tilbage til udvidelsen, eller til os, hvilke sider du besøger, eller hvilke der blev blokeret.
- **Hvorfor den beder om adgang til alle websteder.** Browsere lader kun en udvidelse erstatte en blokeret side med sin egen hjælpeside, i stedet for at vise en fejl, hvis den har adgang til de websteder, det drejer sig om. Den adgang bruges ikke til andet: udvidelsen læser, ændrer eller indsamler ikke indholdet på nogen side.
- **Hjælpesiden** viser hjælpelinjer og links til dette websted. At følge et link er et almindeligt besøg på trysilex.com og er omfattet af resten af denne tekst.
- **At indberette et overset websted** åbner din egen mailapp. Hvad du sender, er op til dig. Vi bruger det kun til at opdatere listen og svare.
- **At fjerne udvidelsen** fjerner den og alt i den.

Domænelisten bygger på The Blocklist Project (frit tilgængelig, public domain) og UT1-listerne fra Université Toulouse Capitole (CC BY-SA 4.0).

## 14. Logbogen i Notion

**Silex Recovery Tracker for Notion** er en valgfri, gratis forbindelse, der opretter en logbog til bedring i dit eget Notion-arbejdsområde. Den har intet med appen at gøre: at bruge den ene rører ikke ved den anden.

- **Hvad der kører, og hvor.** En lille funktion, vi har skrevet, og som ligger hos Cloudflare. Den kører kun i de få sekunder, efter at du klikker på Connect og godkender adgangen i Notion.
- **Hvad den modtager.** Notion sender den en engangskode, som den bytter til en adgangsnøgle til dit arbejdsområde. Notions svar indeholder også navnet på dit arbejdsområde og din Notion-profil (navn og muligvis e-mail og profilbillede). Funktionen læser kun adgangsnøglen og ser bort fra resten.
- **Hvad den gør med adgangsnøglen.** Den opretter én side, to tabeller og to eksempelrækker i dit arbejdsområde og sender dig så hen til den side. Den læser ikke dine eksisterende sider og søger ikke i dem, undtagen for at finde den ene side, du har valgt at dele, så logbogen kan lægges ind i den. Det sker kun, hvis Notion afviser en side på øverste niveau.
- **Hvad den gemmer.** Intet. Adgangsnøglen findes kun i hukommelsen under den ene anmodning. Der er ingen database, ingen fil og ingen kopi af det, du skriver i logbogen. Vi kan ikke åbne din logbog bagefter, og hvis Notion giver en fejl, logges kun Notions fejlkode, aldrig indhold fra arbejdsområdet.
- **Sådan fjerner du den.** Gå til Settings → Connections (indstillingerne for forbindelser) i Notion, og fjern Silex. Logbogen bliver liggende: den er en almindelig side, der tilhører dig. Slet den som enhver anden side.

Retsgrundlag: den anmodning, du fremsætter ved at klikke på Connect (GDPR art. 6, stk. 1, litra b). Cloudflare behandler selve forbindelsen (din IP-adresse og anmodningens headere) som vores databehandler. Se [Cloudflares privatlivspolitik](https://www.cloudflare.com/privacypolicy/). Det, du skriver i logbogen, er en sag mellem dig og Notion efter [Notions privatlivspolitik](https://www.notion.com/trust/privacy-policy).

## 15. Silex Help i ChatGPT og andre AI-assistenter

**Silex Help** er en gratis tjeneste, der kun læser, og som AI-assistenter som ChatGPT kan kalde for at svare på spørgsmål om at stoppe med at spille om penge: hjælpelinjer i et land, ordninger for selvudelukkelse, om et websted står på vores liste over spildomæner, PGSI-selvtesten og guider til blokering. Den har intet med appen at gøre, og den har ingen konti.

- **Hvad den modtager.** Kun det, assistenten sender, når den bruger et værktøj: et land, de webadresser, der skal tjekkes, eller dine ni svar i selvtesten. Din samtale, dit navn og din konto hos assistenten sendes ikke til os.
- **Hvad den gør.** Den slår svaret op i data, der følger med tjenesten, og sender det tilbage. Den sender ingen anmodninger til nogen andre.
- **Hvad den gemmer.** Intet. Hver anmodning behandles i hukommelsen og glemmes. Der er ingen database og ingen log over, hvad der er spurgt om.
- **Selve assistenten.** Det, du skriver til ChatGPT eller en anden assistent, er omfattet af den udbyders egen privatlivspolitik, ikke denne.

Retsgrundlag: den anmodning, din assistent fremsætter på dine vegne (GDPR art. 6, stk. 1, litra b). Cloudflare driver tjenesten og behandler hver forbindelse (IP-adresse og anmodningens headere) som vores databehandler. Se [Cloudflares privatlivspolitik](https://www.cloudflare.com/privacypolicy/).

## Hvis du har brug for at tale med nogen nu

- Danmark: [70 22 28 25](tel:70222825) — StopSpillet: gratis og fortroligt, man–tor 9–21, fre 9–17 (lukket i weekenden)
- Danmark: [70 201 201](tel:70201201) — Livslinien: hver dag kl. 9–5, anonymt, almindelig telefontakst
- Nødsituation: [112](tel:112) — Akut livsfare
- Andre lande: [findahelpline.com](https://findahelpline.com) — Krisetelefoner, hvor du er
