> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/da/blokere-pengespil-android/

# Sådan blokerer du pengespil på Android

Af [Kyrylo Lozovyi](https://trysilex.com/da/om-silex/) · 25. november 2026

**Kort svar:** Android har den bedste gratis spærring mod pengespil af alle telefoner, og næsten ingen bruger den: **Indstillinger → Netværk og internet → Privat DNS → Hostname for privat DNS-udbyder**, sat til en filtrerende tjeneste som `family.dns.mullvad.net`. Det dækker alle apps og browsere, både på wi-fi og mobildata, på cirka to minutter og helt gratis. Læg derefter en **blokering med låst periode** oveni, en **spærring på pengene** og **ROFUS**.

**Det ærlige svar først:** Silex findes til Android nu, men du har ikke brug for appen til noget på denne side. Det her er opsætningen, vi ville give en ven med en Android, og den indbyggede gratis løsning er bedre end de fleste apps, der koster penge.

## 1. Privat DNS: to minutter, og alt er dækket

Android har haft krypteret DNS for hele systemet siden Android 9. Peg den mod en tjeneste, der filtrerer pengespil, og så holder de domæner op med at virke i alle apps og alle browsere (spiludbydernes egne apps også), på wi-fi og på mobildata.

1. Åbn **Indstillinger** → **Netværk og internet**. På nogle telefoner ligger det et andet sted. Søg så efter »Privat DNS« i Indstillinger.
2. Tryk på **Privat DNS**.
3. Vælg **Hostname for privat DNS-udbyder**.
4. Skriv hostnavnet på en filtrerende tjeneste, og tryk på **Gem**.

Tjenester, der filtrerer pengespil:

| Hostnavn | Det filtrerer den | Pris |
|---|---|---|
| `family.dns.mullvad.net` | Pengespil, voksenindhold, reklamer og sporing | Gratis, ingen konto, offentliggjort politik om ikke at logge |
| `<dit-id>.dns.nextdns.io` | Det, du selv slår til (pengespil er en kategori med ét tryk) | Gratis niveau, kræver konto, giver dig log og kontrol |

**Test det.** Åbn en browser, du normalt ikke bruger, og prøv en spilside, du faktisk har brugt. Den skal slet ikke kunne indlæses, ikke bare se mærkelig ud. Kan den det, så tjek, om en VPN er slået til. En VPN overtager DNS og tilsidesætter indstillingen, uden at du får besked.

**Haken ved den:** den kan slås fra i Indstillinger på cirka et minut. Det er stadig noget værd, for de fleste tilbagefald er impulsive, og et minuts modstand stopper mange af dem. Men en mur er det ikke. Det er det, de næste trin er til for.

## 2. Gør det sværere at fortryde

Det er det her trin, der gør et vejbump til noget mere solidt. På Android er det også det trin, der er sværest for en voksen, så vær ærlig over for dig selv om, hvad der holder.

- **Fjern de apps, du spiller i.** Play Butik → profilikonet → **Administrer apps og enheder** → **Administrer** → **Afinstaller**. Tag dem alle sammen på én gang.
- **En blokering med låst periode.** I BetBlocker vælger du selv alt fra 1 dag til 5 år, og når perioden er gået i gang, kan den ikke gøres kortere. Vælg den på et roligt tidspunkt.
- **Børnesikring med en pinkode, som en anden vælger (Android 17 og nyere).** Indstillinger → **Børnesikring** → **Konfigurer en pinkode til børnesikring**. **Filtre i appbutik** begrænser nye installationer efter aldersgrænse, og Google kræver, at apps til spil om rigtige penge har en [aldersgrænse for voksne](https://support.google.com/googleplay/android-developer/answer/9877032). **Appgrænser** blokerer en app, der stadig ligger på telefonen. Mens børnesikringen er slået til, kræver det også pinkoden at tilføje brugere og nulstille telefonen. Kontoen til gendannelse kan nulstille pinkoden, så den skal være den andens, ikke din ([Googles vejledning](https://support.google.com/android/answer/16766047?hl=da)).
- **Ældre Android: pinkode til appgrænser.** Indstillinger → **Digital balance** → **Appgrænser** → **Pinkode til appgrænser**. Har en anden pinkoden, er en tidsgrænse på nul nok til at [blokere en app](https://support.google.com/android/answer/9346420?hl=da). Uden pinkode er **Apptimere** lette at slå fra igen, så regn dem ikke som en spærring.
- **Indholdsbegrænsninger i Google Play.** Play Butik → profilikonet → **Indstillinger** → **Familie** → **Indholdsbegrænsninger**. En ældre pinkode til Play [kan nulstilles](https://support.google.com/googleplay/answer/1075738?hl=da) ved at rydde Play Butiks data, så regn den som en bremse, ikke en spærring.
- **Google Family Link holder ikke mellem voksne.** Google beskriver det til børn, og [kravet om en forælders godkendelse](https://support.google.com/families/answer/7106787?hl=da) for at stoppe ophører ved 18 år. Som voksen kan du ikke regne med, at det står imod.

Menuerne er forskellige fra producent til producent, og Google skriver ikke om nogen af de her indstillinger, at de låser selve Privat DNS.

## 3. Apps fra andre, der kan være det værd

| App | Pris | Det er den god til |
|---|---|---|
| **BetBlocker** | Gratis, ingen reklamer, drives af en nonprofitorganisation | En spærring på 1 dag til 5 år, som ikke kan forkortes, når den er begyndt. En måde at binde dig selv på forhånd, som ikke koster noget |
| **Gamban** | 4,99 pund/måned eller 29,99 pund/år, 7 dages prøveperiode | Ét abonnement til Android, iOS, Windows og Mac, [eller et af alternativerne](https://trysilex.com/da/alternativer-til-gamban/) |
| **GamBlock** | Koster penge, prisen står ikke på forsiden | Hævder, at fjernelse »ikke kan ske« på Android, og at nulstilling bliver blokeret. Den tungeste lås, hvis løfterne holder på din telefon |

Priserne er tjekket på hver udbyders egen hjemmeside den 25. november 2026. [Se hele sammenligningen →](https://trysilex.com/da/bedste-apps-blokere-pengespil/)

## 4. De to lag, der slet ikke ligger på telefonen

De virker ens på alle telefoner og er stærkere end alt det ovenfor:

1. [**ROFUS**](https://trysilex.com/da/udeluk-dig-fra-spil/): du udelukker dig selv med MitID, og det kan ikke fortrydes, uanset hvor stærk trangen er.
2. [**En spærring på pengene**](https://trysilex.com/da/spaerre-pengespil-banken/): næsten ingen danske banker beskriver en spilspærring, men Revolut har en, som det tager op til 48 timer at slå fra, og du kan gøre pengene sværere at nå på andre måder.

Har du kun ti minutter i dag, så gør de to ting først, og tag telefonens indstillinger bagefter.

## Det, der ikke virker på Android

- **Kun at afinstallere apps.** Mobilsiden virker stadig, og det tager få sekunder at hente appen igen.
- **Kun et filter i routeren eller på wi-fi.** Det slutter ved hoveddøren. Mobildata går lige uden om.
- **En almindelig VPN.** Den er ikke et filter, og den kan sætte din Privat DNS ud af kraft.
- **At blokere én browser.** Du henter en ny på tyve sekunder.

## Og så det, ingen blokering gør

Hvert lag ovenfor køber dig tid, når trangen kommer, og en trang går over på cirka 20 til 30 minutter, uanset om du spiller eller ej. Det, du bruger de minutter på, afgør, om det holder: [at ride trangen af](https://trysilex.com/da/hvor-laenge-varer-spilletrang/) og [den samlede plan](https://trysilex.com/da/stop-med-at-spille/). Ingen af delene kræver en iPhone eller et abonnement.

## Ofte stillede spørgsmål

### Hvad er den bedste gratis blokering af pengespil til Android?

Androids egen indstilling Privat DNS, peget mod en filtrerende tjeneste. Den blokerer mere end de fleste apps, der koster penge: alle apps og browsere, på mobildata såvel som på wi-fi. Vil du have en app, hvor du kan låse en periode, er BetBlocker gratis, drives af en nonprofitorganisation og virker på Android. Den findes dog ikke på dansk.

### Virker Privat DNS på mobildata?

Ja. Det er derfor, den er bedre end en spærring i routeren eller på wi-fi, som holder op med at virke, i samme øjeblik telefonen forlader huset. Privat DNS er en indstilling i telefonen og gælder overalt.

### Kan jeg forhindre mig selv i at slå Privat DNS fra?

Ikke med den alene. Den kan slås fra i Indstillinger, så den er et vejbump og ikke en mur. Family Link er ikke løsningen for en voksen: Google beskriver det til børn, og kravet om en forælders godkendelse for at stoppe ophører ved 18 år. Brug i stedet en blokering, der er svær at fjerne, og stol mest på det, der ligger uden for telefonen: ROFUS, som ikke kan annulleres, og en spærring på pengene.

### Virker Silex på Android?

Ja, på Android 8.0 og nyere, fra Google Play. Appen sætter spærringen med Privat DNS fra denne side op for dig og lægger et 90-dagesprogram, en SOS-knap til trangen og en tæller for dine penge i behold oveni. Det er et betalt abonnement. Vil du kun have spærringen, klarer den gratis opsætning her på siden plus BetBlocker eller Gamban opgaven.

### Blokerer en VPN spilsider på Android?

En almindelig VPN gør ikke. Den flytter, hvor din trafik kommer ud på nettet, den filtrerer ikke noget. Nogle VPN-tjenester har en DNS-tilstand, der filtrerer indhold, og den kan blokere pengespil. Vær opmærksom på, at en aktiv VPN kan sætte din Privat DNS ud af kraft. Det er en almindelig grund til, at spærringen holder op med at virke, uden at du opdager det.

## Hvis du har brug for at tale med nogen nu

- Danmark: [70 22 28 25](tel:70222825) — StopSpillet: gratis og fortroligt, man–tor 9–21, fre 9–17 (lukket i weekenden)
- Danmark: [70 201 201](tel:70201201) — Livslinien: hver dag kl. 9–5, anonymt, almindelig telefontakst
- Nødsituation: [112](tel:112) — Akut livsfare
- Andre lande: [findahelpline.com](https://findahelpline.com) — Krisetelefoner, hvor du er
