> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/no/personvern/

# Personvernerklæring

Dette er en oversettelse. Hvis den avviker fra den [engelske versjonen](https://trysilex.com/privacy/), er det den engelske versjonen som gjelder.

Sist oppdatert: 25. november 2026. Den engelske versjonen på trysilex.com er originalen av denne erklæringen; den erstatter kopien hos Notion som eldre versjoner av appen lenker til.

Silex bygger på ett prinsipp: **Bedringen din er ingens datasett.**

*Vi* lagrer ingenting om deg på noen server, har ingen kontoer og har ingen måte å lese det du skriver i denne appen på. (Den eneste koden vi kjører på servere, er to valgfrie verktøy som ikke har noe med appen å gjøre: Notion-koblingen i punkt 14 og Silex Help i punkt 15. Ingen av dem beholder noe.) To tredjeparter har derimot servere som mottar noe: En analysetjeneste får *navnene* på skjermene du kommer til, og en tjeneste for annonsemåling får vite at appen ble installert, og om det førte til en prøveperiode eller et kjøp. Én bryter i Innstillinger stopper begge. Denne siden forklarer nøyaktig hva det betyr, også de få stedene der data faktisk forlater telefonen din. En personvernerklæring som bare lister opp det beroligende, er ikke en personvernerklæring.

Erklæringen er skrevet for å oppfylle EUs personvernforordning (GDPR) og den britiske utgaven, UK GDPR. Er du i EØS eller Storbritannia, gjelder delene om behandlingsgrunnlag, overføringer og rettighetene dine fullt ut for deg.

## 1. Det du skriver inn, blir på enheten din

Alt du registrerer – svar på spørsmål, innsjekker, refleksjoner i dagboken, svar i programmet, logger over sug, sprekker, datoer for strekk, pengebeløp, signaturen din og orbsamlingen din – blir lagret på to steder, og begge tilhører deg:

- **På din iPhone**, i appens lokale database.
- **I din private iCloud**, gjennom den private databasen i Apples CloudKit, så historikken din overlever at en enhet blir borte eller byttes ut.

Den private iCloud-databasen din er bare tilgjengelig for Apple-kontoen din (Apple-ID). Vi er ikke part i den og kan ikke lese den. Hvis iCloud ikke er tilgjengelig eller er slått av, lagrer appen bare data på enheten din.

**Vi mottar aldri dette innholdet.** Det finnes ikke noe API-kall som sender det, ingen sikkerhetskopi hos oss, og ingen nøkkel som ville latt oss dekryptere det. Fordi vi ikke har tilgang til det og ikke kan bruke det, regner vi oss ikke som behandlingsansvarlig for det du skriver i appen. Det er du. Vi beskriver det her for åpenhetens skyld, ikke fordi vi behandler det.

## 2. Hva som faktisk når noen andre

Seks snevre tilfeller, alle valgfrie eller teknisk uunngåelige.

### Kjøp: Apple og RevenueCat

Abonnementer behandles av Apple. Vi bruker RevenueCat til å kontrollere og administrere abonnementsstatus. RevenueCat er databehandler for oss og mottar:

- enhetstype og operativsystem,
- når appen sist ble brukt, og kvitteringsfiler fra Apple,
- eventuelt en brukeridentifikator og metadata om attribusjon.

Mens «Del anonym bruk» er på, gir RevenueCat også opplysningen om at en prøveperiode eller et kjøp har skjedd, og prisen, videre til AppsFlyer, slik at det kan telles for en annonsekampanje. Se *Annonsemåling* nedenfor.

RevenueCat mottar aldri dagboken din, svarene dine, strekket ditt eller noe annet innhold om bedringen din. Se [Apples personvernerklæring](https://www.apple.com/legal/privacy/) og [RevenueCats personvernerklæring](https://www.revenuecat.com/privacy/).

### DNS-skjoldet, bare hvis du slår det på

Dette installerer en konfigurasjon for kryptert DNS (DoH), slik at spilldomener ikke lar seg slå opp i appene og nettleserne dine. Mens den er på, blir enhetens DNS-oppslag besvart av [Mullvads offentlige DNS-tjeneste](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls) etter deres [policy om ikke å logge](https://mullvad.net/en/help/no-logging-data-policy/). Avanserte brukere kan i stedet peke den mot sin egen NextDNS-konfigurasjon. Mullvad eller NextDNS er selvstendig behandlingsansvarlige for disse oppslagene etter sine egne retningslinjer. Vi er ikke med i den veien og ser aldri hva du surfer på. Slår du av skjoldet i Innstillinger i iOS, tar dette slutt med én gang.

### Oppdateringer av blokkeringslisten

Appen laster med jevne mellomrom ned offentlige lister over spilldomener fra jsDelivr og GitHub. Som ved alle nedlastinger av filer kan de serverne se forespørselen og IP-adressen din. Forespørselen inneholder ingen identifikator og ingenting om deg eller bedringen din.

### Brukstall: tellingen på enheten din

Appen fører sin egen telling av *hvordan appen brukes* (for eksempel hvor mange ganger en skjerm ble åpnet en gitt dag), lagret som antall per dag i én fil i appens eget lagringsområde. Den inneholder ingen identifikatorer og ikke noe innhold du har skrevet, og **den filen forlater aldri telefonen din**. Sletter du appen, slettes den. De samme *navnene* på hendelser sendes hver for seg til TelemetryDeck, med mindre du slår det av. Det er neste avsnitt, og den ærlige grunnen til at dette avsnittet ikke lenger sier «når ikke fram til noen».

### Bruksanalyse: TelemetryDeck, med mindre du slår det av

For å se hvor folk gir opp introduksjonen, og det er forskjellen på å rette en skjerm og å gjette, sender appen *navnene* på stegene den kommer til, til **TelemetryDeck GmbH**, Von-der-Tann-Str. 54, 86159 Augsburg, Tyskland. Dette sendes:

- **navnet** på hvert steg i introduksjonen som blir nådd, og plassen det har i rekkefølgen (`funnel.question_04`, `funnel.paywall`), hvert av dem høyst én gang per installasjon;
- **navnene** på andre hendelser i appen – en programdag fullført, panikknappen åpnet – og ingenting om dem ut over navnet;
- TelemetryDecks egne standardopplysninger: versjon av operativsystemet, enhetsmodell, språkinnstilling, region, appversjon og lignende;
- en tilfeldig identifikator som appen lager for denne installasjonen.

Vi legger også disse hendelsesnavnene sammen til noen løpende totaler som appen viser i introduksjonen, for eksempel hvor mange programdager folk har fullført. En total sier ingenting om noen enkeltperson.

Dette sendes aldri: svarene dine på spørsmålene, PGSI-scoren din, det du bruker per uke, teksten i dagboken, sprekkene du har logget, eller noe annet du har skrevet eller valgt. Signalet er at en skjerm ble nådd, aldri hva som sto på den, og aldri hva du la inn på den.

**Om den identifikatoren.** Den er en tilfeldig UUID som appen lager første gang den kjøres. Den er med vilje *ikke* `identifierForVendor`, identifikatoren iOS ellers ville ha brukt, fordi den overlever at du sletter appen og installerer den igjen, og deles med alle andre apper fra samme utvikler. Vår deles med ingen og forsvinner når du sletter appen. Før den forlater telefonen din, blir den hashet med et salt på enheten; når den kommer fram, legger TelemetryDeck til sitt eget salt og hasher den én gang til, slik at verken vi eller de kan regne seg tilbake fra den lagrede verdien til den opprinnelige. Én enkelt hash ville bare vært pseudonymisering, og det er derfor de gjør den andre.

Vi slår også av to ting TelemetryDeck ellers ville samlet inn: signalet om at en økt har begynt, og statistikk over økter.

**Bryteren.** Innstillinger → Dine data → **Del anonym bruk**. Den er **på som standard**, og vi pynter ikke på grunnen: En måling folk må melde seg på, måler feil gruppe, fordi de som gir seg på den første skjermen, er nettopp de som aldri kommer til et spørsmål om samtykke. Da ville selve frafallet vi vil måle, ha gjort utvalget skjevt. Prisen for den standarden er å si tydelig hva som sendes, og det er det denne delen er til for. Slår du den av, stopper nye signaler med én gang, mottakeren for dem fjernes fra appen, og bunken med usendte signaler som venter på enheten, blir slettet. Det som alt er sendt, kan ikke hentes tilbake, og ingenting i det peker tilbake på deg.

Se [TelemetryDecks personvernerklæring](https://telemetrydeck.com/privacy/).

### Annonsemåling: AppsFlyer, under samme bryter

Vi annonserer for Silex, og en annonse er bare verdt å betale for hvis folk som installerer appen fra den, fortsetter å bruke appen. For å telle det inneholder appen SDK-en til **AppsFlyer Ltd.**, 14 Maskit St., Herzliya, Israel. AppsFlyer mottar:

- at appen ble installert og åpnet, og når;
- en identifikator som AppsFlyers SDK lager for denne installasjonen av denne appen;
- AppsFlyers standardopplysninger om enheten: enhetsmodell, versjon av operativsystemet, språk, appversjon og opplysninger om nettverket (Wi-Fi eller mobiloperatør). Som alle servere ser den IP-adressen din, og AppsFlyer sier at de kan knytte den til en grov region;
- **navnene** på tre hendelser og ingenting om dem: at skjermen med abonnementer ble vist, at en gratis prøveperiode startet, at et kjøp ble gjort;
- fra RevenueCat, at en prøveperiode eller et kjøp har skjedd, og prisen, knyttet til den samme installasjonsidentifikatoren.

Slik kobles en installasjon til en annonse: gjennom Apples egne samlerapporter (SKAdNetwork og AdAttributionKit), som navngir en *kampanje* og aldri en person. Apple sender dem til annonsenettverket, og iOS sender AppsFlyer en kopi. Det finnes ett unntak, som begynte 22. november 2026: se «Meta-annonser» nedenfor.

Annonser i selve App Store virker litt annerledes. For dem gir iOS appen et engangstoken (Apples AdServices), og AppsFlyer og RevenueCat bytter det hver for seg hos Apple mot kampanjen og søkeordet som førte til denne installasjonen. Tokenet identifiserer trykket på annonsen, ikke deg.

Dette er ikke med i bildet, og det er bygget inn, ikke bare lovet: **ingen annonse-ID.** Appen viser aldri spørsmålet om å tillate sporing, den bruker utgaven av AppsFlyers SDK der koden for annonse-ID er fjernet, og den slår av innsamlingen av `identifierForVendor`, den ene identifikatoren som deles mellom apper fra samme utvikler. Ingenting du har skrevet eller valgt, blir sendt; det er den samme listen som ovenfor.

**Én ting er annerledes enn for identifikatoren til analysen, og vi sier det heller enn å la være.** AppsFlyers identifikator blir ikke hashet på telefonen din slik TelemetryDecks blir, og AppsFlyers SDK beholder en liten markør i nøkkelringen på iPhone, slik at den kan skille en reinstallasjon fra en ny installasjon. Oppføringer i nøkkelringen kan overleve at en app slettes. For AppsFlyer påstår vi derfor ikke, slik vi gjør for TelemetryDeck, at en reinstallasjon ser ut som en fremmed.

**Bryteren** er den samme: Innstillinger → Dine data → **Del anonym bruk**, av. Den stopper forespørslene fra SDK-en, fjerner AppsFlyers identifikator fra RevenueCat slik at ingen flere kjøp blir videresendt, og sletter forespørsler som venter på enheten. AppsFlyer har også sitt eget skjema for å reservere seg, på [appsflyer.com/legal/opt-out](https://www.appsflyer.com/legal/opt-out/). Se [AppsFlyers personvernerklæring for tjenestene](https://www.appsflyer.com/legal/services-privacy-policy/).

### Meta-annonser: fra 22. november 2026

Vi begynner å annonsere på Facebook og Instagram. Metas installasjonskampanjer for iPhone-apper teller bare installasjoner med Metas egen metode (de kaller den Aggregated Event Measurement), og den metoden trenger opplysninger fra appen. Apples samlerapporter alene ble ikke tilbudt oss som en måte å telle på. Fra 22. november 2026 gir AppsFlyer derfor en del av det de mottar, videre til Meta (**Meta Platforms Ireland Ltd.** for folk i Europa, **Meta Platforms, Inc.** ellers):

- at appen ble installert, og hver gang den blir åpnet. Det gjelder hver installasjon der denne bryteren er på, enten en annonse hadde noe med den å gjøre eller ikke;
- for installasjoner som AppsFlyer tilskriver en av Meta-annonsene våre, de tre hendelsesnavnene som er listet opp ovenfor;
- sammen med hver av disse: AppsFlyers identifikator for installasjonen, IP-adressen forespørselen kom fra, og enhetsmodellen og iOS-versjonen.

Dette sendes fortsatt ikke: navn, e-postadresse, annonse-ID, `identifierForVendor`, eller noe du har skrevet eller valgt i appen.

**Hva dette endrer, sagt rett ut.** Før denne datoen nådde ingenting om en enkelt installasjon fram til et annonseselskap. Nå mottar Meta én registrering per installasjon. Etter vilkårene sine kan Meta koble en slik registrering til en person som bruker Facebook eller Instagram, bruke den til å måle annonsene våre og til å bestemme hvem som får se annonser, og beholde den i inntil to år. Registreringen sier at en enhet installerte en app for folk som vil slutte å spille om penger. Det er den typen opplysning punkt 3 behandler med varsomhet. Denne delingen skjer bare mens vi annonserer på Meta. Hvis vi slutter, eller hvis Meta lar en kampanje for Silex telles med Apples samlerapporter alene, slår vi den av og skriver datoen her. Det Meta har mottatt til da, blir værende under Metas vilkår; vi kan ikke trekke det tilbake.

**Bryteren dekker dette også.** Innstillinger → Dine data → **Del anonym bruk**, av: AppsFlyer mottar ikke noe mer fra telefonen din og har dermed ingenting å gi videre. Vil du spørre Meta om det de allerede har, kan du bruke verktøyene i Facebook- eller Instagram-kontoen din, eller se [Metas personvernerklæring](https://www.facebook.com/privacy/policy/).

Med App Stores egne ord erklærer appen **ingen sporing** (`NSPrivacyTracking` false, ingen sporingsdomener) og tre typer innsamlede data – produktinteraksjon (Product Interaction), enhets-ID (Device ID) og kjøpshistorikk (Purchase History) – alle merket som *ikke knyttet til identiteten din* og *ikke brukt til sporing*, med analyse og måling av vår egen annonsering som formål (kjøpshistorikk også for å levere abonnementet).

**Ingenting annet.** De fem nettverksveiene er de eneste appen har. Det finnes ingen annonseidentifikatorer, og vi driver ikke med profilering eller automatiserte avgjørelser som har rettsvirkning eller på lignende måte påvirker deg i vesentlig grad. Mens delingen med Meta ovenfor er på, er det det ene stedet der en registrering av installasjonen din kan settes sammen med det et annet selskap alt vet om deg. Erklæringen i avsnittet over ble skrevet før den begynte; vi vurderer om den må endres, og enhver endring vil bli nevnt i punkt 11.

### En setning til andre, bare hvis du sender en

Etter at du har fullført programdag 7, kan appen én gang spørre om du vil dele en setning med noen som akkurat begynner. Velger du det, åpner den en e-post i din egen e-postapp, adressert til oss, med ordene dine, den første bokstaven i navnet ditt, antall dager og samtykket ditt. Du kan endre eller slette hva som helst av det før du sender, og ingenting forlater enheten din med mindre du trykker på send.

Da mottar vi e-posten og adressen din, i en postkasse hos Google. Vi kan vise ordene dine, den første bokstaven i navnet ditt og antall dager i appen og på butikksidene våre. Vi offentliggjør aldri e-postadressen din. Skriv til oss når som helst, så slutter vi å bruke ordene dine: De tas bort fra butikksidene og fra neste versjon av appen, og vi sletter e-posten, med mindre vi må beholde den for å vise hva du samtykket til.

## 3. Behandlingsgrunnlag (GDPR art. 6 og art. 9)

| Hva | Formål | Behandlingsgrunnlag |
|---|---|---|
| Kjøp og abonnementsstatus (via Apple / RevenueCat) | Levere og gjenopprette abonnementet du har kjøpt; hindre at noen får tilgang på falskt grunnlag | **Art. 6 nr. 1 bokstav b**: oppfyllelse av en avtale med deg |
| IP-adresse som innholdsnettverket (CDN) ser når appen laster ned en blokkeringsliste | Levere blokkeringen som appen er til for | **Art. 6 nr. 1 bokstav f**: berettiget interesse (holde blokkeringslistene oppdatert). Vår vurdering: minimalt med data, ingen profilering, ingen kobling til deg |
| Navn på hendelser, en hashet identifikator for installasjonen og TelemetryDecks standardopplysninger om enheten, mens «Del anonym bruk» er på | Se hvor folk gir opp introduksjonen, så skjermene som mister dem, kan rettes, og vise de løpende totalene som er beskrevet ovenfor | **Art. 6 nr. 1 bokstav f**: berettiget interesse (få appen til å virke for dem den er ment for). Vår vurdering: ikke noe innhold, ingen annonse-ID, en identifikator som ikke kan følge deg mellom apper eller overleve at du sletter appen, og en bryter i Innstillinger som gjør slutt på det. Det er bryteren som bærer interesseavveiingen: En interesse du kan si nei til med ett trykk, er ikke en som blir hevdet over hodet på deg |
| En installasjonsidentifikator fra AppsFlyer, AppsFlyers standardopplysninger om enheten, navnet på tre hendelser og hendelser om prøveperiode eller kjøp, mens «Del anonym bruk» er på | Vite hvilke av annonsene våre som fører til at folk faktisk bruker appen, så vi slutter å betale for dem som ikke gjør det | **Art. 6 nr. 1 bokstav f**: berettiget interesse (annonsere for en app som skal hjelpe folk ut av pengespill, uten å sløse bort det som finansierer den). Vår vurdering: ingen annonse-ID, ikke noe innhold, kobling til annonser bare gjennom Apples samlerapporter for kampanjer (bortsett fra delingen med Meta i neste rad), og den samme bryteren i Innstillinger som gjør slutt på det |
| Fra 22. november 2026, mens vi annonserer på Meta: opplysningene om installasjon og åpning av appen som AppsFlyer gir til Meta, med AppsFlyers installasjonsidentifikator, IP-adresse, enhetsmodell og iOS-versjon (punkt 2, «Meta-annonser») | La Meta telle installasjonene annonsene deres fører til, noe installasjonskampanjene for iPhone krever | **Art. 6 nr. 1 bokstav f**: berettiget interesse, og den svakeste bruken av det grunnlaget i denne tabellen. Registreringen går til et selskap som kan koble den til en konto. Vår vurdering hviler på at ingenting du har registrert, er med i den, at den bare skjer mens vi annonserer på Meta, og at den samme bryteren gjør slutt på den |
| DNS-oppslag, mens skjoldet er på | Blokkere spilldomener på hele enheten | **Art. 6 nr. 1 bokstav a**: samtykket ditt, gitt ved at du slår på skjoldet og godkjenner dialogen fra iOS; kan trekkes tilbake når som helst ved å slå det av |
| En setning du velger å sende oss på e-post for publisering | Vise folk som akkurat begynner, at andre har vært der de er | **Art. 6 nr. 1 bokstav a og art. 9 nr. 2 bokstav a**: det uttrykkelige samtykket ditt, gitt ved at du slår på bryteren for samtykke og sender e-posten; kan trekkes tilbake når som helst |
| Det du skriver i appen | Levere programmet til deg på din egen enhet | Vi mottar det ikke, så vi utfører ingen behandling vi må begrunne. I den grad det behandles i det hele tatt, skjer det på enheten din og under din kontroll |

**Særlige kategorier av personopplysninger (helse).** Det du registrerer her, avslører opplysninger om helse og om en mulig atferdsavhengighet, og det er en særlig kategori av personopplysninger etter **art. 9**. Nettopp derfor er appen laget slik den er: De dataene når aldri fram til oss, så vi bygger aldri på et vilkår i art. 9 for dem. Det ene unntaket er en setning du velger å sende oss på e-post for publisering: Den kan avsløre det samme, så for den bygger vi på det uttrykkelige samtykket ditt etter art. 9 nr. 2 bokstav a.

Det vanskeligere spørsmålet er analysen, og vi vil heller arbeide oss gjennom det enn å vifte det bort. Et signal som lyder `funnel.question_04`, har ikke noe innhold, men Silex er en app for folk som vil ut av pengespill, og EU-domstolen har fastslått at opplysninger som bare *indirekte* avslører en særlig kategori, omfattes likevel (sak C-184/20, *OT*). Vi påstår derfor ikke at temaet for disse signalene er uskyldig: «denne installasjonen gikk inn i introduksjonen til Silex» sier noe som grenser til helse, om den som holdt telefonen. Det vi bygger på, er den andre halvdelen av art. 9, som gjelder opplysninger om en **identifisert eller identifiserbar** fysisk person. Identifikatoren som er knyttet til disse signalene, er tilfeldig, laget for én enkelt installasjon, saltet og hashet på enheten din, og saltet på nytt med TelemetryDecks eget salt og hashet igjen når den kommer fram. Dermed kan ingen av partene, heller ikke vi, regne seg tilbake til en person eller koble den mot noe annet. På det grunnlaget regner vi det som når fram til TelemetryDeck, for å ligge utenfor art. 9. Vi behandler det likevel som pseudonyme personopplysninger etter art. 6, med et behandlingsgrunnlag og en måte å reservere seg på som virker, for skal vi ta feil, vil vi ta feil på den forsiktige siden. For en abonnementskvittering er ingenting endret: Den avslører ikke en helsetilstand ut over det at du kjøpte en app.

Det som når AppsFlyer, står svakere på den prøven, og vi behandler det deretter. Identifikatoren deres er tilfeldig og gjelder bare denne appen, men den er ikke hashet to ganger, og den kommer sammen med en enhetsmodell, en IP-adresse og hendelser om kjøp. Vi behandler det som pseudonyme personopplysninger, hos en databehandler med databehandlervilkår (punkt 4), på art. 6-grunnlaget i tabellen og med samme reservasjon. Det sier «denne installasjonen kom til Silex og startet en prøveperiode»; det sier ikke hvem du er, og det inneholder ingenting du har registrert i appen.

Dette er det ene avsnittet her der dyktige jurister med rimelighet kan komme til ulike svar, og vi sier det heller enn å la det leses som avgjort.

## 4. Internasjonale overføringer

**RevenueCat** er et amerikansk selskap (Brandon, Florida) som lagrer data hos Amazon Web Services i USA. Overføringene er dekket av databehandleravtalen deres, som tar inn EU-kommisjonens **standard personvernbestemmelser (Standard Contractual Clauses)** (gjennomføringsbeslutning (EU) 2021/914), **modul to: behandlingsansvarlig til databehandler**. For Storbritannia gjelder i tillegg ICOs **International Data Transfer Addendum** av 21. mars 2022, og for Sveits standardbestemmelsene tilpasset den sveitsiske personvernloven (FADP). RevenueCat er **ikke** sertifisert under EU–US Data Privacy Framework; standardbestemmelsene er mekanismen. *Kontrollert mot RevenueCats publiserte databehandleravtale 6. august 2026.*

**TelemetryDeck** er et tysk selskap (TelemetryDeck GmbH, Augsburg). De oppgir at bruksdata lagres **utelukkende innenfor Den europeiske union**, på infrastruktur fra Hetzner i Nürnberg, med deler av behandlingskjeden fortsatt på Azure i Amsterdam og AWS i Frankfurt og en uttalt plan om å samle alt hos Hetzner i løpet av 2026. Selskapets egen personvernerklæring navngir disse leverandørene som Hetzner Online GmbH (Tyskland), Microsoft Ireland Operations Ltd (Irland) og Amazon Web Services, Inc. (Seattle, USA). AWS-selskapet er amerikansk, men regionen det lagrer i, er Frankfurt. Etter TelemetryDecks egen fremstilling forlater dermed ingen av analysedataene våre EØS, og **ingen overføringsmekanisme etter kapittel V kommer til anvendelse**, fordi det ikke finnes noen overføring til et tredjeland å dekke. Vi har ikke kontrollert disse lagringsregionene selv og kan ikke gjøre det; vi gjengir det TelemetryDeck publiserer.

Det er én ting vi ikke kan gi deg, og det er grunnen til at dette punktet er lengre enn RevenueCats. **TelemetryDeck tilbyr ingen databehandleravtale etter art. 28.** Databehandlervilkårene deres er automatisk en del av tjenestevilkårene, så det er ingenting å signere, men de sier at selskapet opptrer «verken som databehandler etter artikkel 4 nr. 8 i GDPR eller som felles behandlingsansvarlig», og at artikkel 26 og 28 ikke gjelder, med den begrunnelsen at det de mottar er anonymt og ikke personopplysninger. Vi har ikke sluttet oss til det synet: Vi behandler den hashede installasjonsidentifikatoren som pseudonyme personopplysninger, gir den et art. 6-grunnlag og en reservasjon uansett (punkt 3), og beskriver TelemetryDeck som databehandler i realiteten, fordi det er det de gjør. Konsekvensen du bør vite om, er at garantiene en avtale etter art. 28 ville gitt – dokumenterte instrukser, rett til revisjon, en avtalt plikt til å slette – ikke er tilgjengelige for oss fra denne leverandøren, fordi den sier nei til rollen som skaper dem. *Kontrollert mot TelemetryDecks publiserte personvernerklæring, databehandleravtale og sider om arkitektur og sikkerhet 17. august 2026.*

**AppsFlyer** er et israelsk selskap (AppsFlyer Ltd., Herzliya). For Israel finnes det en beslutning fra EU-kommisjonen om tilstrekkelig beskyttelsesnivå (2011/61/EU). AppsFlyers databehandlervilkår utpeker dem som **databehandler** og oss som behandlingsansvarlig, og den publiserte listen over underdatabehandlere oppgir Amazon Web Services og Google Cloud som vertstjenester, i «EU/USA». For overføringer utenfor land med tilstrekkelig beskyttelsesnivå tar vilkårene inn **standard personvernbestemmelser (Standard Contractual Clauses)** (gjennomføringsbeslutning (EU) 2021/914), **modul to: behandlingsansvarlig til databehandler**, og for Storbritannia ICOs **International Data Transfer Addendum**. Vi har ikke kontrollert hvilken region dataene våre lagres i. *Kontrollert mot AppsFlyers publiserte databehandlervilkår (februar 2023), listen over underdatabehandlere og personvernerklæringen for tjenestene 19. november 2026.*

**Meta**, for delingen som er beskrevet i punkt 2. Meta Platforms Ireland Ltd. er i EU og gir data videre til Meta Platforms, Inc. i USA etter Metas egne overføringsvilkår. Etter Metas vilkår for forretningsverktøy (Business Tools Terms) er Meta databehandler for oss når de kobler og måler, og felles behandlingsansvarlig med oss når de bruker det de mottar, til å bestemme hvem som ser annonser. *Lest fra Metas Business Tools Terms 20. november 2026; vi har ikke kontrollert Metas overføringsmekanisme ut over det vilkårene sier.*

**Apple**: se Apples personvernerklæring for hvordan de sikrer overføringene sine. Dataene i din private iCloud er underlagt Apples vilkår og overføres ikke av oss, fordi vi aldri har dem.

**Vi.** Vi er etablert i Ukraina, som er utenfor EØS og ikke har noen beslutning fra EU-kommisjonen om tilstrekkelig beskyttelsesnivå. Når du gir oss data direkte, er det en direkte innsamling og ikke en overføring etter kapittel V (se EDPBs retningslinjer 05/2021 om samspillet mellom art. 3 og kapittel V). I praksis er det nesten ingenting å samle inn: Det finnes ingen konto, og de eneste personopplysningene vi kan se, er den pseudonyme abonnementsoppføringen i RevenueCats kontrollpanel, de samlede tallene i TelemetryDecks, og oppføringene per installasjon i AppsFlyers.

## 5. Hvor lenge noe blir oppbevart

- **På enheten din og i din private iCloud:** til du sletter det. Vi kan ikke slette det for deg, og vi kan ikke hindre deg i å slette det.
- **På våre systemer:** ingenting. De to små tjenestene i punkt 14 og 15 beholder ingen opplysninger. Serverne hos tredjeparter som har noe av vårt, er RevenueCats, TelemetryDecks og AppsFlyers; se nedenfor.
- **En setning du har sendt oss på e-post for publisering:** så lenge vi bruker ordene dine, til du ber oss slutte. Se punkt 2.
- **Kjøpsoppføringer:** oppbevares av Apple og RevenueCat etter deres egne frister, og slik skatte- og regnskapslovgivningen krever.
- **Brukstall på enheten din:** fjernes når appen slettes.
- **Opplysninger om installasjon og hendelser hos AppsFlyer:** Personvernerklæringen for tjenestene deres sier at de ikke oppbevarer sluttbrukerdata i mer enn **tjuefire måneder**. En oppføring kan slettes tidligere gjennom AppsFlyers eget skjema (punkt 2).
- **Opplysninger om installasjon og åpning av appen som er gitt til Meta** (punkt 2, «Meta-annonser»): Metas vilkår tillater dem å beholde dem i inntil **to år**.
- **Navn på hendelser hos TelemetryDeck:** **De publiserer ingen frist for sletting av dem.** Prisplanene deres oppgir et tall for oppbevaring – 90 dager i gratisversjonen, lengre i de betalte – men det er et vindu for *spørringer*: hvor langt tilbake kontrollpanelene kan se. Data som er eldre enn vinduet, flyttes til kaldlagring i stedet for å bli slettet, og kan lastes inn igjen. TelemetryDeck sier at sletting, én gang eller etter en fast plan, kan avtales på forespørsel; det har vi ikke avtalt, så gå ut fra at disse signalene blir liggende på ubestemt tid. Siden de er tall uten noen identifikator som når tilbake til deg, er det en mindre påstand enn det høres ut som, men det er den riktige, og vi vil heller skrive den enn et tall vi har funnet på.

## 6. Hvem som er ansvarlig

**Behandlingsansvarlig:** Kyrylo Lozovyi
**Adresse:** Vidpochinku 12, Kyiv, Ukraina
**Kontakt om personvern:** [support@trysilex.com](mailto:support@trysilex.com) (også på [stopgamblesupport@gmail.com](mailto:stopgamblesupport@gmail.com), adressen som vises i de nåværende versjonene av appen)

Vi har ikke utpekt et personvernombud; vi er ikke pliktige til det, fordi vi ikke driver overvåking i stort omfang og ikke har særlige kategorier av personopplysninger på systemene våre (se punkt 3).

## 7. Rettighetene dine

Hvis du er i EØS eller Storbritannia, har du rett til **innsyn** i dataene dine, til **retting**, til **sletting**, til **begrensning** av behandlingen, til **dataportabilitet**, til å **protestere** mot behandling som bygger på berettiget interesse, og til å **trekke tilbake samtykke** når som helst der samtykke er grunnlaget (DNS-skjoldet: Trekk det tilbake ved å slå det av; det påvirker ikke behandling som allerede er gjort).

**En ærlig begrensning.** For nesten alt denne appen berører, har vi ingen opplysninger som kan identifisere deg, og ingen konto som kan koble en forespørsel til en person. Etter **GDPR art. 11** er vi ikke pliktige til å innhente ekstra opplysninger bare for å identifisere deg, og vi ber deg ikke om legitimasjon for å behandle en forespørsel vi ikke har data til å svare på. I praksis:

- **Innhold du har skrevet:** Bruk disse rettighetene direkte. Det ligger på enheten din og i din iCloud, og sletter du appen (pluss iCloud-kopien), er det helt borte.
- **Kjøpsdata:** Kontakt Apple, eller kontakt oss, så sender vi forespørselen videre til RevenueCat, som er databehandler for oss.
- **Bruksanalyse:** Retten din etter **art. 21 til å protestere** mot vår berettigede interesse har en bryter i stedet for en supportkø: Innstillinger → Dine data → **Del anonym bruk**, av. Den stopper nye signaler med én gang, fjerner mottakeren og sletter bunken som venter på enheten. Du trenger ikke skrive til oss, og du trenger ikke gi noen grunn. Det som allerede er sendt, kan ikke trekkes tilbake, og det kan heller ikke finnes igjen, fordi ingenting i det identifiserer deg.
- **Annonsemåling:** Den samme bryteren er protesten din mot dette også. Vil du ha det AppsFlyer allerede har om installasjonen din, slettet, bruker du AppsFlyers eget skjema (punkt 2). Vi kan ikke slå opp installasjonen din for deg, av grunnen over: Vi har ingenting som knytter en installasjon til en person.

Skriv til [support@trysilex.com](mailto:support@trysilex.com), så svarer vi innen én måned, slik art. 12 nr. 3 krever.

**Retten til å klage.** Du kan klage til den nasjonale tilsynsmyndigheten for personvern der du er. I Norge er det [Datatilsynet](https://www.datatilsynet.no/om-datatilsynet/kontakt-oss/klage-til-datatilsynet/). Listen ligger på [edpb.europa.eu](https://edpb.europa.eu/about-edpb/board/members_en); i Storbritannia er det [ICO](https://ico.org.uk/make-a-complaint/). Du trenger ikke kontakte oss først, selv om vi helst ser at du gjør det.

## 8. Å slette alt

- Slett appen fra iPhone.
- Fjern iCloud-kopien: Innstillinger → navnet ditt → iCloud → Administrer kontolagring → Silex.
- Avslutt et abonnement: Innstillinger → navnet ditt → Abonnementer, eller valget «Administrer abonnementer» i appen.

## 9. Sensitive opplysninger, og hvorfor måten appen er laget på, er selve erklæringen

Det du registrerer her, gjelder helsen din og økonomien din, og vi behandler det deretter. Ingen kontoer å bryte seg inn på, ingenting på noen server hos oss som noen kan kreve innsyn i, og ingenting hos noen leverandør som kan leses tilbake som *din* bedring. Det sterkeste vernet vi kan tilby, er å la være å ha dataene dine i det hele tatt, og den delen ligger i oppbygningen, ikke i et løfte: Det finnes ingen nøkkel, ingen sikkerhetskopi og ingen kopi, så det finnes ingenting vi i det stille kan ombestemme oss om.

**Hva som endret seg.** Til august 2026 sto det også her at ingen analyseleverandør hadde en kopi. Det er ikke lenger sant: TelemetryDeck har et tall for hvor mange installasjoner som kom til hver skjerm. Det er en reell svekkelse av garantien, og vi kommer ikke til å kalle den noe annet. Det som står igjen, er den delen som gjør jobben: Innholdet blir på telefonen din, identifikatoren som er knyttet til de tallene, kan ikke knyttes til deg eller følges mellom apper, og hele opplegget har en bryter. Det vi ga fra oss, er muligheten til å si ordet *ingen*.

I november 2026 kom en leverandør til: AppsFlyer får vite at en installasjon skjedde, og om det førte til en prøveperiode eller et kjøp, så vi kan se hvilke annonser det er verdt å betale for. Det er den andre svekkelsen, og de samme tingene overlever den: Ingenting du har registrert, forlater telefonen din, det finnes ingen annonse-ID, og bryteren dekker det.

22. november 2026 kom den tredje, og det er den vi liker minst: Mens vi annonserer på Facebook og Instagram, får Meta vite at en installasjon finnes (punkt 2, «Meta-annonser»). Ingenting du har registrert, forlater telefonen din, og bryteren dekker det fortsatt, men så lenge det varer, kan vi ikke lenger si at ingen annonseselskaper får vite om en eneste installasjon. Hvis det tar slutt, kommer datoen her.

## 10. Barn

Silex er ment for voksne og retter seg ikke mot barn. Vi samler ikke bevisst inn opplysninger fra noen under 18 år. Aldersgrensen i App Store er satt deretter.

## 11. Endringer

Hvis denne erklæringen endres, endres datoen øverst, og den gjeldende versjonen ligger alltid på denne adressen.

Å ta i bruk TelemetryDeck er en vesentlig endring, og den forrige versjonen av denne delen lovet at vesentlige endringer ville bli vist i appen. **Vi har endret det løftet i stedet for å påstå at vi holdt det.** Appen har ingen mekanisme som viser en melding ved oppdatering, og vi kommer ikke til å beskrive en som ikke finnes. Det denne versjonen faktisk gjør, er å legge bryteren i Innstillinger med en klar beskrivelse av hva som sendes ved siden av, synlig for alle som ser etter, men ikke dyttet på noen som ikke gjør det. Det er mindre enn den gamle setningen lovet, og det er nettopp derfor det var setningen som måtte endres, ikke fremstillingen av hva som skjedde.

Å ta i bruk AppsFlyer i november 2026 er en vesentlig endring av samme slag, og den kommer på samme måte: nevnt her og i versjonsmerknadene, under bryteren som allerede var der, med setningen ved siden av bryteren endret til å si det.

Nå lyder løftet derfor slik: Vesentlige endringer blir nevnt i denne delen og i versjonsmerknadene i App Store for versjonen som gjør dem, og enhver endring som utvider hva som forlater enheten din, kommer sammen med kontrollen for den i samme versjon.

Delingen med Meta 22. november 2026 er en vesentlig endring som det løftet ikke forutså. Ingenting nytt forlater enheten din; det som endret seg, er at AppsFlyer gir en del av det videre, og det ble slått på i innstillingene hos AppsFlyer, ikke i en ny versjon av appen. Dermed fantes det ingen versjonsmerknader å nevne det i. Det er nevnt her samme dag som det begynte, den eksisterende bryteren dekker det, og merknadene til neste versjon vil nevne det.

## 12. Kontakt

[support@trysilex.com](mailto:support@trysilex.com)

## 13. Den gratis nettleserutvidelsen

Denne erklæringen dekker også **Silex — Free Gambling Blocker**, nettleserutvidelsen for Chrome, Microsoft Edge og Firefox. Den er enklere enn appen, og det er denne delen også:

- **Den samler ikke inn noe.** Ingen konto, ingen analyse, ingen identifikatorer, og den gjør ingen nettverksforespørsler på egen hånd. Ingenting om deg eller surfingen din sendes til oss eller noen andre.
- **Hvordan den blokkerer.** Utvidelsen har en liste over spilldomener inni seg. Nettleseren din sammenligner sidene du åpner, med den listen lokalt, med den innebygde funksjonen `declarativeNetRequest`. Nettleseren melder ikke tilbake til utvidelsen, eller til oss, hvilke nettsteder du besøker, eller hvilke som ble blokkert.
- **Hvorfor den ber om tilgang til alle nettsteder.** Nettlesere lar bare en utvidelse erstatte en blokkert side med sin egen hjelpeside, i stedet for å vise en feil, hvis den har tilgang til nettstedene det gjelder. Den tilgangen brukes ikke til noe annet: Utvidelsen leser ikke, endrer ikke og samler ikke inn innholdet på noen side.
- **Hjelpesiden** viser kriselinjer og lenker til dette nettstedet. Å følge en lenke er et vanlig besøk på trysilex.com, som dekkes av resten av denne erklæringen.
- **Å melde fra om et nettsted vi har gått glipp av** åpner din egen e-postapp. Hva du sender, er opp til deg; vi bruker det bare til å oppdatere listen og svare.
- **Å fjerne utvidelsen** fjerner den og alt i den.

Domenelisten bygger på The Blocklist Project (offentlig eie) og UT1-listene fra Université Toulouse Capitole (CC BY-SA 4.0).

## 14. Loggen i Notion

**Silex Recovery Tracker for Notion** er en valgfri, gratis kobling som setter opp en loggside i ditt eget arbeidsområde i Notion. Den har ingenting med appen å gjøre: Å bruke den ene påvirker ikke den andre.

- **Hva som kjører, og hvor.** En liten funksjon vi har skrevet, driftet hos Cloudflare. Den kjører bare i de få sekundene etter at du klikker på Koble til og godkjenner tilgangen i Notion.
- **Hva den mottar.** Notion sender den en engangskode, som den bytter mot et tilgangstoken til arbeidsområdet ditt. Svaret fra Notion inneholder også navnet på arbeidsområdet og Notion-profilen din (navn, og kanskje e-post og profilbilde). Funksjonen leser bare tokenet og ser bort fra resten.
- **Hva den gjør med tokenet.** Den lager én side, to tabeller og to eksempelrader i arbeidsområdet ditt, og sender deg så til siden. Den leser ikke og søker ikke i de andre sidene dine, med ett unntak: Bare hvis Notion nekter den å lage en side på øverste nivå, finner den den ene siden du valgte å dele, så loggen kan legges inni den.
- **Hva den beholder.** Ingenting. Tokenet finnes bare i minnet for den ene forespørselen; det finnes ingen database, ingen fil og ingen kopi av noe du skriver i loggen. Vi kan ikke åpne loggen din etterpå, og hvis Notion gir en feil, blir bare feilkoden fra Notion logget, aldri innhold fra arbeidsområdet.
- **Å fjerne den.** I Notion går du til Settings → Connections (innstillingene for tilkoblinger) og fjerner Silex. Loggen blir liggende: Den er en vanlig side som tilhører deg. Slett den som en hvilken som helst annen side.

Behandlingsgrunnlag: forespørselen du gjør når du klikker på Koble til (GDPR art. 6 nr. 1 bokstav b). Cloudflare behandler selve tilkoblingen (IP-adressen din og hodefeltene i forespørselen) som databehandler for oss; se [Cloudflares personvernerklæring](https://www.cloudflare.com/privacypolicy/). Det du skriver i loggen, er mellom deg og Notion, etter [Notions personvernerklæring](https://www.notion.com/trust/privacy-policy).

## 15. Silex Help i ChatGPT og andre KI-assistenter

**Silex Help** er en gratis tjeneste som bare kan leses fra, og som KI-assistenter som ChatGPT kan bruke for å svare på spørsmål om å slutte med pengespill: hjelpelinjer i et land, ordninger for selvutestengelse, om et nettsted står på listen vår over spilldomener, PGSI-selvtesten og guider til blokkering. Den har ingenting med appen å gjøre, og den har ingen kontoer.

- **Hva den mottar.** Bare det assistenten sender når den bruker et verktøy: et land, nettadressene som skal kontrolleres, eller de ni svarene dine på selvtesten. Samtalen din, navnet ditt og kontoen din hos assistenten blir ikke sendt til oss.
- **Hva den gjør.** Den slår opp svaret i data som følger med tjenesten, og sender det tilbake. Den gjør ingen forespørsler til noen andre.
- **Hva den beholder.** Ingenting. Hver forespørsel blir behandlet i minnet og glemt; det finnes ingen database og ingen logg over hva det ble spurt om.
- **Assistenten selv.** Det du skriver til ChatGPT eller en annen assistent, dekkes av den leverandørens egen personvernerklæring, ikke av denne.

Behandlingsgrunnlag: forespørselen assistenten gjør på dine vegne (GDPR art. 6 nr. 1 bokstav b). Cloudflare kjører tjenesten og behandler hver tilkobling (IP-adresse og hodefeltene i forespørselen) som databehandler for oss; se [Cloudflares personvernerklæring](https://www.cloudflare.com/privacypolicy/).

## Hvis du trenger å snakke med noen nå

- Norge: [800 800 40](tel:80080040) — Hjelpelinjen for pengespill: gratis og anonym, hverdager 09–18
- Norge: [116 123](tel:116123) — Mental Helse: gratis og døgnåpen, for alle som trenger noen å snakke med
- Nødsituasjon: [113](tel:113) — Fare for liv og helse
- Andre land: [findahelpline.com](https://findahelpline.com) — Krisetelefoner der du er
