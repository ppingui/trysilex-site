> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/no/blokkere-pengespill-android/

# Slik blokkerer du pengespill på Android

Av [Kyrylo Lozovyi](https://trysilex.com/no/om-silex/) · 25. november 2026

**Kort svar:** Android har den beste gratis sperren mot pengespill av alle mobiler, og nesten ingen bruker den: **Innstillinger → Nettverk og internett → Privat DNS → Vertsnavn for privat DNS-leverandør**, med en tjeneste som filtrerer pengespill, for eksempel `family.dns.mullvad.net`. Det dekker alle apper og nettlesere, på wifi og mobildata, på omtrent to minutter og helt gratis. Legg så til **Gamban, som er gratis i Norge**, la **noen andre sette PIN-koden for appgrenser**, og ta de to lagene som ikke ligger på telefonen: **banken** og **utestenging**.

**Det ærlige svaret først:** Silex finnes på Android nå, men du trenger den ikke til noe på denne siden. Dette er oppsettet vi ville gitt en venn med Android, og gratisvalget som allerede ligger i telefonen, er bedre enn de fleste betalappene.

## 1. Privat DNS: to minutter, og det dekker alt

Android har hatt kryptert DNS for hele systemet siden Android 9. Pek den mot en tjeneste som filtrerer pengespill, så slutter de domenene å virke i alle apper og alle nettlesere (også spillselskapenes egne apper), på wifi og på mobildata.

1. Åpne **Innstillinger** → **Nettverk og internett**. Heter menyen noe annet på din telefon, søk etter «Privat DNS» i Innstillinger.
2. Trykk på **Privat DNS**.
3. Velg **Vertsnavn for privat DNS-leverandør**.
4. Skriv inn vertsnavnet til en filtrerende tjeneste, og trykk på **Lagre**.

Tjenester som filtrerer pengespill:

| Vertsnavn | Hva det filtrerer | Pris |
|---|---|---|
| `family.dns.mullvad.net` | Pengespill, innhold for voksne, reklame og sporing | Gratis, ingen konto, publisert policy om at ingenting logges |
| `<din-id>.dns.nextdns.io` | Det du velger selv (pengespill er en egen kategori, ett trykk) | Gratisnivå, krever konto, gir deg logg og kontroll |

**Test det.** Åpne en nettleser du ikke pleier å bruke, og prøv en spillside du faktisk har brukt. Den skal ikke laste i det hele tatt, ikke bare se rar ut. Laster den, sjekk at ingen VPN er på. En VPN tar over DNS og overstyrer denne innstillingen uten å si fra.

**Velg bare en tjeneste som filtrerer pengespill.** Siden 1. januar 2025 blokkeres en liste med ulovlige spillsider i Norge via DNS hos nettleverandørene. Bytter du DNS, går du utenom den blokkeringen, så den nye tjenesten må gjøre jobben selv. Det bør den uansett: Selskapene bytter adresser for å komme seg rundt den norske listen.

**Haken:** Det er en bryter i Innstillinger, så du kan angre på omtrent et minutt. Det betyr likevel noe (de fleste tilbakefall er impulsive, og et minutt med motstand stopper mange av dem), men det er ikke en mur. Det er det de neste stegene er til for.

## 2. Gjør innstillingene til noe du ikke kan endre alene

Dette er steget som gjør en fartsdump til noe som holder bedre.

- **Foreldrekontroll med PIN-kode (Android 17 og nyere).** Innstillinger → **Foreldrekontroll** → **Konfigurer en PIN-kode for foreldrekontroll**. La noen andre velge koden og beholde den. **Appbutikkfiltre** begrenser nye installeringer etter aldersgrense, og Google krever at apper for pengespill har en [aldersgrense for voksne](https://support.google.com/googleplay/android-developer/answer/9877032). **Appgrenser** blokkerer en app som fortsatt ligger på telefonen. Mens kontrollen er på, kreves PIN-koden også for å legge til brukere og tilbakestille telefonen. Gjenopprettingskontoen kan tilbakestille PIN-koden, så den bør være den andres, ikke din ([Googles veiledning](https://support.google.com/android/answer/16766047?hl=no)).
- **Digital balanse med en PIN-kode du ikke kan.** På eldre Android, men ikke på alle telefoner. Gå til Innstillinger → **Digital balanse** → **Appgrenser** → **PIN-kode for appgrenser**. La partneren din, en venn eller noen i familien velge koden og sette tidsgrensen til null for appene du spiller i. Uten en slik PIN-kode kan du selv oppheve en apptimer når du vil, så da er den ikke mye til sperre.
- **Fjern appene.** Google Play → profilikonet → **Administrer apper og enheter** → **Administrer** → velg appen → **Avinstaller**. Ta alle spillappene på én gang.
- **Innholdsbegrensninger i Google Play.** Play-butikken → profilikonet → **Innstillinger** → **Familie** → **Innholdsbegrensninger**. En eldre PIN-kode for Play [kan tilbakestilles](https://support.google.com/googleplay/answer/1075738?hl=no) ved å tømme dataene til Play-butikken, så regn den som en brems, ikke en sperre.
- **Google Family Link holder ikke mellom voksne.** Google beskriver den for barn og unge, og [bare de under 18 år trenger foreldregodkjenning](https://support.google.com/families/answer/7106787?hl=no) for å avslutte tilsynet.

Menyene varierer mellom produsenter, og for ingen av disse innstillingene skriver Google at de låser selve Privat DNS.

## 3. Apper som er verdt å legge til

| App | Pris | Verdt det fordi |
|---|---|---|
| **Gamban** | **Gratis i Norge** når du får lisensen gjennom Hjelpelinjen, Norsk Tipping, Spillavhengighet Norge eller Rikstoto. Ellers 4,99 pund/måned eller 29,99 pund/år | Én lisens for Android, iOS, Windows og Mac, [eller et av alternativene](https://trysilex.com/no/alternativer-til-gamban/) |
| **BetBlocker** | Gratis, uten reklame, drevet av en ideell organisasjon | En sperreperiode du setter fra 1 dag til 5 år og ikke kan korte ned når den er i gang. En måte å binde deg på, og den koster ingenting |
| **GamBlock** | Koster penger, men prisen står ikke på forsiden | Hevder at det «ikke kan skje» at den fjernes fra Android, og at den stopper fabrikkgjenoppretting. Den tyngste låsen, hvis løftene holder på din telefon |

**Slik får du Gamban gratis:** Ta kontakt med Hjelpelinjen på [800 800 40](tel:80080040) (hverdager 09.00–18.00, chat 11.00–15.00), der du er anonym, eller Spillavhengighet Norge på [477 00 200](tel:47700200) (hverdager 10–15). Norsk Tipping ([62 50 77 70](tel:62507770)) og Rikstoto ([ansvarligspill@rikstoto.no](mailto:ansvarligspill@rikstoto.no)) deler den også ut. Er det stengt akkurat nå, legg inn BetBlocker i mellomtiden.

Prisene er sjekket på hver leverandørs egen side 25. november 2026. [Hele sammenligningen →](https://trysilex.com/no/beste-apper-blokkere-pengespill/)

## 4. De to lagene som ikke ligger på telefonen

De er like på alle mobiler, og sterkere enn alt over:

1. [**Utestenging**](https://trysilex.com/no/utesteng-deg-fra-pengespill/): Norge har ikke ett felles register i dag, så du gjør det hos Norsk Tipping, hos Rikstoto og hos hvert bingoselskap du spiller hos på nett. Den kan ikke oppheves før det har gått minst ett år.
2. [**Banken**](https://trysilex.com/no/sperre-pengespill-banken/): Den skal stoppe betalinger til spillselskaper uten tillatelse i Norge. Be skriftlig om en sperre som bare banken kan oppheve, i tillegg.

Har du bare ti minutter i dag, gjør disse to, og kom tilbake til telefonen etterpå.

## Det som ikke virker på Android

- **Bare å avinstallere appene.** Mobilsiden virker, og å installere på nytt tar noen sekunder.
- **Bare en sperre i ruteren eller på wifi.** Den slutter ved ytterdøren. Mobildata går rett forbi.
- **En vanlig VPN.** Den filtrerer ikke, og den kan slå ut Privat DNS.
- **Å blokkere én nettleser.** Android installerer gjerne en ny på tjue sekunder.

## Så kommer delen ingen blokkering tar seg av

Hvert lag over kjøper deg tid mens suget står på, og sug går over på omtrent 20 til 30 minutter enten du spiller eller ikke. Hva du gjør med de minuttene, avgjør om dette holder: [å ri av deg suget](https://trysilex.com/no/hvor-lenge-varer-spillesug/) og [hele planen](https://trysilex.com/no/slutte-a-spille/). Ingen av delene krever en iPhone eller et abonnement.

## Vanlige spørsmål

### Hva er den beste gratis blokkeringen av pengespill på Android?

Androids egen innstilling Privat DNS, pekt mot en tjeneste som filtrerer pengespill, blokkerer mer enn de fleste betalapper: alle apper og nettlesere, på mobildata så vel som wifi. Vil du ha en app i tillegg, får du Gamban gratis i Norge gjennom Hjelpelinjen, Norsk Tipping, Spillavhengighet Norge eller Rikstoto. BetBlocker er også gratis, drives av en ideell organisasjon og lar deg låse en sperreperiode.

### Virker Privat DNS på mobildata?

Ja. Det er det som gjør den bedre enn sperrer i ruteren eller bare på wifi, som slutter å virke i det telefonen forlater huset. Privat DNS er en innstilling på selve telefonen og gjelder overalt.

### Kan jeg hindre meg selv i å slå av Privat DNS?

Ikke bare med den. Det er en bryter i Innstillinger, altså en fartsdump og ikke en mur. Bruk en blokkering som er vanskeligere å fjerne i tillegg, la noen andre sette PIN-koden for appgrenser, og støtt deg på lagene du ikke kan angre i suget: utestenging og en sperre i banken som bare banken kan oppheve.

### Virker Silex på Android?

Ja, på Android 8.0 og nyere, fra Google Play. Den setter opp Privat DNS-sperren fra denne siden for deg og legger til et 90-dagersprogram for å slutte, en pulsknapp for suget og en teller for pengene du beholder. Den er et betalt abonnement. Er det bare sperren du vil ha, gjør gratisoppsettet på denne siden sammen med Gamban eller BetBlocker jobben.

### Blokkerer en VPN spillsider på Android?

En vanlig VPN gjør ikke det. Den flytter hvor trafikken din går ut, den filtrerer den ikke. Noen personvern-VPN-er har et DNS-valg som filtrerer innhold, og det kan stoppe pengespill. Merk at en aktiv VPN kan overstyre innstillingen Privat DNS. Det er en vanlig grunn til at sperren slutter å virke uten at du merker det.

## Hvis du trenger å snakke med noen nå

- Norge: [800 800 40](tel:80080040) — Hjelpelinjen for pengespill: gratis og anonym, hverdager 09–18
- Norge: [116 123](tel:116123) — Mental Helse: gratis og døgnåpen, for alle som trenger noen å snakke med
- Nødsituasjon: [113](tel:113) — Fare for liv og helse
- Andre land: [findahelpline.com](https://findahelpline.com) — Krisetelefoner der du er
