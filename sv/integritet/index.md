> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/sv/integritet/

# Integritetspolicy

Det här är en översättning. Om den skiljer sig från den [engelska versionen](https://trysilex.com/privacy/) är det den engelska versionen som gäller.

Senast uppdaterad: 25 november 2026. Den engelska versionen på trysilex.com är originalet. Den ersätter kopian hos Notion som äldre versioner av appen länkar till.

Silex bygger på en enda princip: **ditt tillfrisknande är ingens datamängd.**

*Vi* lagrar ingenting om dig på någon server, har inga konton och har inget sätt att läsa det du skriver i appen. (Den enda kod vi kör på servrar är två valfria verktyg som inte har något med appen att göra: Notion-kopplingen i avsnitt 14 och Silex Help i avsnitt 15. Ingen av dem sparar något.) Två utomstående företag driver servrar som tar emot något: en analystjänst får *namnen* på de skärmar du når, och en tjänst för annonsmätning får veta att appen installerades och om det ledde till en provperiod eller ett köp. Ett enda reglage i Inställningar stoppar båda. Den här sidan förklarar exakt vad det innebär, även de få fall där data faktiskt lämnar din telefon. En integritetspolicy som bara räknar upp det lugnande är ingen integritetspolicy.

Texten är skriven för att uppfylla EU:s dataskyddsförordning (GDPR) och Storbritanniens motsvarighet (UK GDPR). Om du finns i EES eller Storbritannien gäller avsnitten om rättsliga grunder, överföringar och dina rättigheter fullt ut för dig.

## 1. Det du skriver in stannar på din enhet

Allt du registrerar – svar på frågorna, avstämningar, reflektioner i dagboken, svar i programmet, loggade sug, snedsteg, datum för din svit, belopp, din namnteckning och din samling av klot – lagras på två ställen, och båda tillhör dig:

- **På din iPhone**, i appens lokala databas.
- **I din privata iCloud**, i den privata databasen i Apples CloudKit, så att din historik finns kvar även om telefonen försvinner eller byts ut.

Bara ditt Apple-konto kommer åt din privata iCloud-databas. Vi är ingen part i den och kan inte läsa den. Om iCloud inte är tillgängligt, eller är avstängt, lagrar appen data enbart på din enhet.

**Vi tar aldrig emot det innehållet.** Det finns inget API-anrop som skickar det, ingen säkerhetskopia hos oss och ingen nyckel som skulle låta oss dekryptera det. Eftersom vi varken har tillgång till det eller kan använda det, anser vi oss inte vara personuppgiftsansvariga för det du skriver i appen. Det är du. Vi beskriver det här för öppenhetens skull, inte för att vi behandlar det.

## 2. Vad som faktiskt når någon annan

Sex snävt avgränsade fall, alla valfria eller tekniskt oundvikliga.

### Köp: Apple och RevenueCat

Prenumerationer hanteras av Apple. Vi använder RevenueCat för att kontrollera och hantera prenumerationens status. RevenueCat är vårt personuppgiftsbiträde och får:

- typ av enhet och operativsystem,
- när appen senast användes, och Apples kvittofiler,
- valfritt: en användaridentifierare och metadata om attribuering (varifrån du kom till appen).

Så länge ”Dela anonym användning” är på skickar RevenueCat också uppgiften att en provperiod eller ett köp har skett, och priset, till AppsFlyer, så att det kan räknas till en annonskampanj. Se *Annonsmätning* längre ner.

RevenueCat får aldrig din dagbok, dina svar, din svit eller något annat innehåll om ditt tillfrisknande. Se [Apples integritetspolicy](https://www.apple.com/legal/privacy/) och [RevenueCats integritetspolicy](https://www.revenuecat.com/privacy/).

### DNS-skölden: bara om du slår på den

Skölden installerar en konfiguration för krypterad DNS (DoH), så att speldomäner inte går att slå upp i någon av dina appar eller webbläsare. Medan den är på besvaras enhetens DNS-uppslag av [Mullvads publika DNS-server](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls) enligt deras [policy att inte logga](https://mullvad.net/en/help/no-logging-data-policy/). Den som är van kan i stället peka den mot sin egen NextDNS-konfiguration. Mullvad eller NextDNS är självständigt personuppgiftsansvariga för de uppslagen enligt sina egna policyer. Vi är inte inblandade i uppslagen och ser aldrig vad du surfar på. Det upphör direkt när du stänger av skölden i iPhonens inställningar.

### Uppdateringar av blocklistan

Appen laddar med jämna mellanrum ner offentliga listor över speldomäner från jsDelivr och GitHub. Som vid all filnedladdning kan de servrarna se förfrågan och din IP-adress. Förfrågan innehåller ingen identifierare och ingenting om dig eller ditt tillfrisknande.

### Användningssiffror: räkningen på din enhet

Appen för en egen räkning över *hur appen används* (till exempel hur många gånger en skärm öppnades en viss dag). Den lagras som antal per dag i en enda fil i appens eget lagringsutrymme. Den innehåller inga identifierare och inget du har skrivit, och **filen lämnar aldrig din telefon**. Tar du bort appen försvinner filen. Samma *namn* på händelser skickas separat till TelemetryDeck om du inte stänger av det. Det är nästa avsnitt, och det ärliga skälet till att det inte längre står ”når ingen” här.

### Användningsanalys: TelemetryDeck, om du inte stänger av den

För att se var folk hoppar av introduktionen, vilket är skillnaden mellan att rätta till en skärm och att gissa sig fram, skickar appen *namnen* på de steg den når till **TelemetryDeck GmbH**, Von-der-Tann-Str. 54, 86159 Augsburg, Tyskland. Det som skickas är:

- **namnet** på varje steg i introduktionen som nås och dess plats i ordningen (`funnel.question_04`, `funnel.paywall`), vart och ett högst en gång per installation,
- **namnen** på andra händelser i appen, som att en programdag blivit klar eller att panikknappen öppnats, och ingenting om dem utöver namnet,
- TelemetryDecks egna standarduppgifter: operativsystemets version, enhetsmodell, språk- och regioninställning, region, appversion och liknande,
- en slumpmässig identifierare som appen skapar för just den här installationen.

Vi räknar också ihop de händelsenamnen till några löpande totalsiffror som appen visar under introduktionen, till exempel hur många programdagar som folk har gjort klart. En totalsiffra säger ingenting om någon enskild person.

Det som aldrig skickas: dina svar på frågorna, din PGSI-poäng, hur mycket du spelar för per vecka, texten i din dagbok, dina snedsteg, eller något annat du har skrivit eller valt. Signalen är att en skärm nåddes, aldrig vad som stod på den och aldrig vad du fyllde i.

**Om den identifieraren.** Det är ett slumpmässigt UUID som appen skapar vid första starten. Identifieraren är med avsikt *inte* `identifierForVendor`, den identifierare som iOS annars skulle ha använt, eftersom den överlever att appen raderas och installeras om, och delas med varje annan app från samma utvecklare. Vår delas med ingenting och försvinner när du tar bort appen. Innan den lämnar telefonen hashas den tillsammans med ett salt på enheten. När den kommer fram lägger TelemetryDeck till sitt eget salt och hashar den en gång till, så att varken vi eller de kan räkna sig tillbaka från det lagrade värdet till det ursprungliga. En enda hashning hade bara varit pseudonymisering, och därför gör de den andra.

Vi har också stängt av två saker som TelemetryDeck annars skulle samla in: signalen om att en session har börjat, och sessionsstatistik.

**Reglaget.** Inställningar → Dina data → **Dela anonym användning**. Det är **på från början**, och skälet är ingen finputsad ursäkt: om mätningen krävde att man tackade ja skulle den mäta fel människor. De som slutar på första skärmen är precis de som aldrig når frågan om samtycke, så det bortfall vi försöker mäta skulle i sig snedvrida urvalet. Priset för att ha det på från början är att säga rakt ut vad som skickas, och det är vad det här avsnittet är till för. När du stänger av reglaget stoppas nya signaler direkt, sändaren kopplas bort från appen och de signaler som ligger på enheten och väntar på att skickas raderas. Det som redan har gått iväg går inte att återkalla, och ingenting i det pekar tillbaka på dig.

Se [TelemetryDecks integritetspolicy](https://telemetrydeck.com/privacy/).

### Annonsmätning: AppsFlyer, under samma reglage

Vi annonserar för Silex, och en annons är bara värd pengarna om de som installerar via den också använder appen. För att räkna det innehåller appen ett SDK från **AppsFlyer Ltd.**, 14 Maskit St., Herzliya, Israel. AppsFlyer får:

- att appen installerades och öppnades, och när,
- en identifierare som AppsFlyers SDK skapar för den här installationen av den här appen,
- AppsFlyers standarduppgifter om enheten: enhetsmodell, operativsystemets version, språk, appversion och uppgifter om nätet (wifi eller operatör). Som alla servrar ser den din IP-adress, som AppsFlyer enligt egen uppgift kan översätta till en ungefärlig region,
- **namnen** på tre händelser och ingenting om dem: att skärmen med abonnemang visades, att en gratis provperiod startade, att ett köp gjordes,
- från RevenueCat: att en provperiod eller ett köp har skett, och priset, kopplat till samma installationsidentifierare.

Så här matchas en installation med en annons: genom Apples egna sammanställda rapporter (SKAdNetwork och AdAttributionKit), som namnger en *kampanj* och aldrig en person. Apple skickar dem till annonsnätverket, och iOS skickar en kopia till AppsFlyer. Det finns ett undantag, som började den 22 november 2026: se ”Annonser hos Meta” nedan.

Annonser i själva App Store fungerar lite annorlunda. För dem ger iOS appen en engångskod (Apples AdServices). AppsFlyer och RevenueCat byter var för sig in koden hos Apple mot uppgift om vilken kampanj och vilket sökord som ledde till installationen. Koden identifierar trycket på annonsen, inte dig.

Det som inte är inblandat, och det är inbyggt snarare än utlovat: **inget annons-ID.** Appen visar aldrig frågan om att tillåta spårning, den använder den variant av AppsFlyers SDK där koden för annons-ID är borttagen, och den stänger av insamlingen av `identifierForVendor`, den enda identifierare som delas mellan appar från samma utvecklare. Ingenting du har skrivit eller valt skickas. Det är samma lista som ovan.

**En sak skiljer sig från identifieraren i analysen, och det säger vi hellre rakt ut.** AppsFlyers identifierare hashas inte på din telefon på det sätt som TelemetryDecks gör, och AppsFlyers SDK sparar en liten markering i iPhonens nyckelring, så att den kan skilja en ominstallation från en ny installation. Poster i nyckelringen kan finnas kvar efter att en app har raderats. För AppsFlyer, till skillnad från TelemetryDeck, påstår vi därför inte att en ominstallation ser ut som en främling.

**Reglaget** är detsamma: Inställningar → Dina data → **Dela anonym användning**, av. Då stoppas SDK:ts förfrågningar, AppsFlyers identifierare tas bort från RevenueCat så att inga fler köphändelser skickas vidare, och förfrågningar som väntar på enheten raderas. AppsFlyer har också ett eget formulär för att välja bort mätningen: [appsflyer.com/legal/opt-out](https://www.appsflyer.com/legal/opt-out/). Se [AppsFlyers integritetspolicy för tjänsterna](https://www.appsflyer.com/legal/services-privacy-policy/).

### Annonser hos Meta: från den 22 november 2026

Vi börjar annonsera på Facebook och Instagram. Metas installationskampanjer för iPhone-appar räknar installationer bara med Metas egen metod (Meta kallar den Aggregated Event Measurement), och den metoden behöver uppgifter från appen. Att räkna enbart med Apples sammanställda rapporter erbjöds oss inte. Från den 22 november 2026 skickar AppsFlyer därför en del av det den tar emot vidare till Meta (**Meta Platforms Ireland Ltd.** för människor i Europa, **Meta Platforms, Inc.** på andra håll):

- att appen installerades, och varje gång den öppnas, för varje installation där reglaget är på, oavsett om en annons hade med saken att göra,
- för installationer som AppsFlyer räknar till en av våra annonser hos Meta: namnen på de tre händelserna ovan,
- tillsammans med vart och ett av dessa: AppsFlyers identifierare för installationen, IP-adressen som förfrågan kom från, samt enhetsmodell och iOS-version.

Det som fortfarande inte skickas: namn, e-postadress, annons-ID, `identifierForVendor` eller något du har skrivit eller valt i appen.

**Vad det här förändrar, rakt ut sagt.** Före det datumet nådde ingenting om en enskild installation något annonsföretag. Nu får Meta en post per installation. Enligt sina villkor får Meta matcha en sådan post med en person som använder Facebook eller Instagram, använda den för att mäta våra annonser och för att avgöra vem som ska se annonser, och spara den i upp till två år. Posten säger att en enhet installerade en app för människor som vill sluta spela om pengar. Det är just en sådan uppgift som avsnitt 3 behandlar varsamt. Delningen pågår bara så länge vi annonserar hos Meta: om vi slutar, eller om Meta låter en kampanj för Silex räknas enbart med Apples sammanställda rapporter, stänger vi av den och skriver in datumet här. Det Meta då redan har fått ligger kvar under Metas villkor, och vi kan inte ta tillbaka det.

**Reglaget täcker även detta.** Inställningar → Dina data → **Dela anonym användning**, av: AppsFlyer får ingenting mer från din telefon och har då ingenting att skicka vidare. Vill du fråga Meta om det de redan har, använd verktygen i ditt Facebook- eller Instagram-konto, eller läs [Metas integritetspolicy](https://www.facebook.com/privacy/policy/).

Med App Stores egna ord uppger appen **ingen spårning** (`NSPrivacyTracking` false, inga spårningsdomäner) och tre insamlade datatyper – Produktinteraktion, Enhets-ID och Köphistorik – alla markerade som *inte kopplade till din identitet* och *inte använda för spårning*. Syftena är analys och att mäta vår egen annonsering (Köphistorik även för att kunna leverera prenumerationen).

**Inget annat.** De fem nätverksvägarna ovan är de enda appen har. Det finns inget annons-ID, och vi gör ingen profilering och fattar inga automatiserade beslut som får rättsliga eller liknande betydande följder. Så länge delningen med Meta ovan är på är den det enda stället där en uppgift om din installation kan läggas ihop med det ett annat företag redan vet om dig. Deklarationen i stycket ovan skrevs innan delningen började. Vi går igenom om den behöver ändras, och en ändring kommer i så fall att nämnas i avsnitt 11.

### En rad till andra: bara om du skickar en

När du har gjort klart programdag 7 kan appen en gång fråga om du vill dela en mening till någon som precis har börjat. Om du väljer att göra det öppnas ett mejl i din egen mejlapp, adresserat till oss, med dina ord, din första initial, hur många dagar du har klarat och ditt samtycke. Du kan ändra eller ta bort vad som helst innan du skickar, och ingenting lämnar enheten om du inte trycker på skicka.

Vi får då mejlet och din adress, i en brevlåda hos Google. Vi kan visa dina ord, din första initial och ditt antal dagar i appen och på våra sidor i appbutikerna. Din e-postadress publicerar vi aldrig. Skriv till oss när som helst, så slutar vi använda dina ord: de tas bort från butikssidorna och från nästa version av appen, och vi raderar mejlet om vi inte måste behålla det för att kunna visa vad du gick med på.

## 3. Rättsliga grunder (GDPR art. 6 och art. 9)

| Vad | Syfte | Rättslig grund |
|---|---|---|
| Köp och prenumerationsstatus (via Apple och RevenueCat) | Leverera och återställa den prenumeration du köpt, och förhindra att någon får tillgång på falska grunder | **Art. 6.1 b** – fullgörande av ett avtal med dig |
| IP-adressen som syns för innehållsnätverket (CDN) när appen laddar ner en blocklista | Leverera blockeringen, som är det appen finns till för | **Art. 6.1 f** – berättigat intresse (hålla skyddslistorna aktuella). Vår bedömning: minimalt med data, ingen profilering, ingen koppling till dig |
| Namn på händelser, en hashad identifierare som bara gäller installationen och TelemetryDecks standarduppgifter om enheten, så länge ”Dela anonym användning” är på | Se var folk hoppar av introduktionen, så att de skärmar som tappar dem kan rättas till, och visa totalsiffrorna som beskrivs ovan | **Art. 6.1 f** – berättigat intresse (få appen att fungera för dem den är till för). Vår bedömning: inget innehåll, inget annons-ID, en identifierare som inte kan följa dig mellan appar eller överleva att appen raderas, och ett reglage i Inställningar som avslutar det. Det är reglaget som bär intresseavvägningen. Ett intresse som du kan säga nej till med ett tryck är inget som drivs igenom över ditt huvud |
| En installationsidentifierare från AppsFlyer, AppsFlyers standarduppgifter om enheten, namnen på tre händelser samt händelser om provperiod och köp, så länge ”Dela anonym användning” är på | Veta vilka av våra annonser som leder till att människor faktiskt använder appen, så att vi slutar betala för dem som inte gör det | **Art. 6.1 f** – berättigat intresse (annonsera för en app för tillfrisknande utan att slösa bort det som finansierar den). Vår bedömning: inget annons-ID, inget innehåll, matchning mot annonser bara genom Apples sammanställda kampanjrapporter (bortsett från delningen med Meta i nästa rad), och samma reglage i Inställningar som avslutar det |
| Från den 22 november 2026, så länge vi annonserar hos Meta: de uppgifter om installation och öppnad app som AppsFlyer skickar till Meta, med AppsFlyers installationsidentifierare, IP-adress, enhetsmodell och iOS-version (avsnitt 2, ”Annonser hos Meta”) | Låta Meta räkna de installationer som deras annonser leder till, vilket deras installationskampanjer för iPhone kräver | **Art. 6.1 f** – berättigat intresse, och den svagaste användningen av den grunden i den här tabellen: uppgiften går till ett företag som kan matcha den med ett konto. Vår bedömning vilar på att inget du registrerat ingår, att det bara pågår medan vi annonserar hos Meta och att samma reglage avslutar det |
| DNS-uppslag, medan skölden är på | Blockera speldomäner på hela enheten | **Art. 6.1 a** – ditt samtycke, som du ger genom att slå på skölden och godkänna frågan från iOS. Du kan när som helst återkalla det genom att stänga av skölden |
| En rad som du väljer att mejla oss för publicering | Visa människor som precis har börjat att andra har varit här | **Art. 6.1 a och art. 9.2 a** – ditt uttryckliga samtycke, som du ger genom att slå på godkännandet och skicka mejlet. Du kan återkalla det när som helst |
| Det du skriver i appen | Leverera programmet för tillfrisknande till dig på din egen enhet | Vi tar inte emot det, så det finns ingen behandling från vår sida att motivera. I den mån det över huvud taget behandlas sker det på din enhet, under din kontroll |

**Särskilda kategorier av personuppgifter (uppgifter om hälsa).** Det du registrerar här avslöjar uppgifter om hälsa och om ett möjligt beteendeberoende. Det är en särskild kategori av personuppgifter enligt **art. 9**. Just därför är appen byggd som den är: de uppgifterna når oss aldrig, så vi behöver aldrig stödja oss på något villkor i art. 9 för dem. Det enda undantaget är en rad som du väljer att mejla oss för publicering. Den kan avslöja samma sak, så för den stödjer vi oss på ditt uttryckliga samtycke enligt art. 9.2 a.

Den svårare frågan är analysen, och vi resonerar hellre igenom den än viftar bort den. En signal som lyder `funnel.question_04` bär inget innehåll. Men Silex är en app för den som vill sluta spela om pengar, och EU-domstolen har slagit fast att även uppgifter som bara *indirekt* avslöjar en särskild kategori omfattas (mål C-184/20, *OT*). Vi påstår därför inte att signalerna är harmlösa till sitt ämne: ”den här installationen gick in i introduktionen i Silex” säger något som ligger nära hälsa om den som höll i telefonen. Det vi stödjer oss på är den andra halvan av art. 9, som gäller uppgifter om en **identifierad eller identifierbar** fysisk person. Identifieraren som följer med signalerna är slumpmässig, skapad för en enda installation, saltad och hashad på din enhet och sedan saltad igen med TelemetryDecks eget salt och hashad på nytt när den kommer fram. Ingen inblandad, inte heller vi, kan därför räkna sig tillbaka till en person eller matcha den mot något annat. Av det skälet behandlar vi det som når TelemetryDeck som att det ligger utanför art. 9, men ändå som pseudonymiserade personuppgifter enligt art. 6, med en rättslig grund och ett reglage som fungerar. Om vi ändå ska ha fel vill vi ha det med den försiktigare av de två tolkningarna. För ett kvitto på en prenumeration ändras inget: det avslöjar inget hälsotillstånd utöver att du har köpt en app.

Det som når AppsFlyer klarar den prövningen sämre, och vi behandlar det därefter. Deras identifierare är slumpmässig och gäller bara den här appen, men den är inte hashad två gånger, och den kommer fram tillsammans med en enhetsmodell, en IP-adress och händelser om köp. Vi behandlar den som pseudonymiserade personuppgifter hos ett personuppgiftsbiträde, enligt dess tilläggsavtal om databehandling (avsnitt 4), på den grund i art. 6 som står i tabellen och med samma möjlighet att välja bort det. Den säger ”den här installationen kom till Silex och startade en provperiod”. Den säger inte vem du är, och den innehåller inget du har registrerat i appen.

Det här är det enda stycket på sidan där kunniga jurister rimligen kan landa olika, och vi säger hellre det än låter det framstå som avgjort.

## 4. Internationella överföringar

**RevenueCat** är ett amerikanskt företag (Brandon, Florida) som lagrar data hos Amazon Web Services i USA. Överföringarna omfattas av dess personuppgiftsbiträdesavtal, som innehåller EU-kommissionens **standardavtalsklausuler** (genomförandebeslut (EU) 2021/914), **modul två: personuppgiftsansvarig till personuppgiftsbiträde**. För Storbritannien gäller dessutom ICO:s **International Data Transfer Addendum** av den 21 mars 2022, och för Schweiz standardavtalsklausulerna anpassade till den schweiziska dataskyddslagen (FADP). RevenueCat är **inte** certifierat enligt ramen för dataskydd mellan EU och USA (EU–US Data Privacy Framework). Det är standardavtalsklausulerna som är mekanismen. *Kontrollerat mot RevenueCats publicerade personuppgiftsbiträdesavtal den 6 augusti 2026.*

**TelemetryDeck** är ett tyskt företag (TelemetryDeck GmbH, Augsburg). Det uppger att användningsdata lagras **uteslutande inom Europeiska unionen**, på Hetzners infrastruktur i Nürnberg, att delar av kedjan fortfarande körs på Azure i Amsterdam och AWS i Frankfurt, och att planen är att samla allt hos Hetzner under 2026. I företagets egen integritetspolicy anges dessa parter som Hetzner Online GmbH (Tyskland), Microsoft Ireland Operations Ltd (Irland) och Amazon Web Services, Inc. (Seattle, USA). AWS-bolaget är alltså amerikanskt, men regionen där det lagrar är Frankfurt. Enligt TelemetryDecks egen beskrivning lämnar därmed inga av våra analysdata EES, och **ingen överföringsmekanism enligt kapitel V blir aktuell**, eftersom det inte finns någon överföring till tredjeland att täcka. Vi har inte självständigt kontrollerat lagringsregionerna och kan inte göra det. Vi återger det TelemetryDeck publicerar.

En sak kan vi inte ge dig, och det är därför det här stycket är längre än det om RevenueCat. **TelemetryDeck erbjuder inget biträdesavtal enligt art. 28.** Dess villkor för databehandling ingår automatiskt i användarvillkoren, så det finns inget att skriva under. Men de säger att företaget agerar ”varken som personuppgiftsbiträde i den mening som avses i artikel 4.8 i GDPR eller som gemensamt personuppgiftsansvarig” (vår översättning) och att artiklarna 26 och 28 inte gäller, med motiveringen att det som tas emot är anonymt och inte personuppgifter. Vi har inte anslutit oss till den ståndpunkten. Vi behandlar den hashade installationsidentifieraren som pseudonymiserade personuppgifter, ger den ändå en grund i art. 6 och en möjlighet att välja bort den (avsnitt 3), och beskriver TelemetryDeck som ett personuppgiftsbiträde i sak, eftersom det är vad företaget gör. Följden som du bör känna till är att de garantier ett avtal enligt art. 28 skulle ge – dokumenterade instruktioner, rätt till granskning, en avtalad skyldighet att radera – inte finns att få av den här leverantören, eftersom den avböjer den roll som skapar dem. *Kontrollerat mot TelemetryDecks publicerade integritetspolicy, avtal om databehandling samt sidor om arkitektur och säkerhet den 17 augusti 2026.*

**AppsFlyer** är ett israeliskt företag (AppsFlyer Ltd., Herzliya). Israel omfattas av ett beslut från EU-kommissionen om adekvat skyddsnivå (2011/61/EU). I AppsFlyers tilläggsavtal om databehandling anges företaget som **personuppgiftsbiträde** och vi som personuppgiftsansvarig. Dess publicerade lista över underbiträden anger Amazon Web Services och Google Cloud, i ”EU/USA”, som leverantörer av drift. För överföringar till länder utan adekvat skyddsnivå innehåller tilläggsavtalet **standardavtalsklausulerna** (genomförandebeslut (EU) 2021/914), **modul två: personuppgiftsansvarig till personuppgiftsbiträde**, och för Storbritannien ICO:s **International Data Transfer Addendum**. Vi har inte kontrollerat i vilken region våra data lagras. *Kontrollerat mot AppsFlyers publicerade tilläggsavtal om databehandling (februari 2023), listan över underbiträden och integritetspolicyn för tjänsterna den 19 november 2026.*

**Meta**, för delningen som beskrivs i avsnitt 2. Meta Platforms Ireland Ltd. finns i EU och för över data till Meta Platforms, Inc. i USA enligt Metas egna villkor för överföring. Enligt Metas villkor för företagsverktyg (Business Tools Terms) är Meta vårt personuppgiftsbiträde när det matchar och mäter, och gemensamt personuppgiftsansvarigt med oss när det använder det som tas emot för att avgöra vem som ser annonser. *Läst i Metas Business Tools Terms den 20 november 2026. Vi har inte kontrollerat Metas överföringsmekanism utöver vad de villkoren säger.*

**Apple**: se Apples integritetspolicy för dess egna skyddsåtgärder vid överföring. Din privata iCloud-data styrs av Apples villkor och förs inte över av oss, eftersom vi aldrig har den.

**Vi.** Vi är etablerade i Ukraina, som ligger utanför EES och inte omfattas av något beslut från EU-kommissionen om adekvat skyddsnivå. När du lämnar uppgifter direkt till oss är det en direkt insamling och ingen överföring enligt kapitel V (enligt EDPB:s riktlinjer 05/2021 om samspelet mellan art. 3 och kapitel V). I praktiken finns det nästan inget att samla in: det finns inget konto, och de enda personuppgifter vi kan se är den pseudonymiserade prenumerationsposten i RevenueCats översikt, de sammanräknade antalen i TelemetryDecks och posterna per installation i AppsFlyers.

## 5. Hur länge något sparas

- **På din enhet och i din privata iCloud:** tills du raderar det. Vi kan inte radera det åt dig, och vi kan inte hindra dig från att göra det.
- **I våra system:** ingenting. De två små tjänsterna i avsnitt 14 och 15 sparar inga uppgifter. De utomstående servrar som har något av vårt är RevenueCats, TelemetryDecks och AppsFlyers. Se nedan.
- **En rad du mejlat oss för publicering:** så länge vi använder dina ord, tills du ber oss sluta. Se avsnitt 2.
- **Uppgifter om köp:** sparas av Apple och RevenueCat enligt deras egna lagringstider, och så länge skatte- och bokföringslagar kräver.
- **Användningssiffror på din enhet:** försvinner när appen raderas.
- **Uppgifter om installation och händelser hos AppsFlyer:** enligt dess integritetspolicy för tjänsterna sparas slutanvändares data inte längre än **tjugofyra månader**. En post kan raderas tidigare genom AppsFlyers eget formulär (avsnitt 2).
- **Uppgifter om installation och öppnad app som skickats till Meta** (avsnitt 2, ”Annonser hos Meta”): enligt Metas villkor får de sparas i upp till **två år**.
- **Namn på händelser hos TelemetryDeck:** **företaget publicerar ingen plan för när de raderas.** I dess prisplaner anges en lagringstid, 90 dagar på gratisnivån och längre på de betalda, men det är ett *sökfönster*: hur långt tillbaka översikterna kan visa. Data som är äldre än fönstret flyttas till kall lagring i stället för att raderas, och kan läsas in igen. TelemetryDeck säger att radering, en gång eller enligt schema, kan ordnas på begäran. Vi har inte ordnat någon, så räkna med att signalerna ligger kvar på obestämd tid. Eftersom de är antal utan någon identifierare som leder tillbaka till dig är det mindre allvarligt än det låter, men det är så det ligger till, och vi skriver hellre det än en siffra vi hittat på.

## 6. Vem som är ansvarig

**Personuppgiftsansvarig:** Kyrylo Lozovyi
**Adress:** Vidpochinku 12, Kyiv, Ukraina
**Kontakt i integritetsfrågor:** [support@trysilex.com](mailto:support@trysilex.com) (nås också på [stopgamblesupport@gmail.com](mailto:stopgamblesupport@gmail.com), adressen som visas i de nuvarande versionerna av appen)

Vi har inte utsett något dataskyddsombud. Vi är inte skyldiga att göra det, eftersom vi inte övervakar i stor skala och inte har några särskilda kategorier av personuppgifter i våra system (se avsnitt 3).

## 7. Dina rättigheter

Om du finns i EES eller Storbritannien har du rätt till **tillgång** till dina uppgifter, till **rättelse**, till **radering**, till **begränsning** av behandlingen, till **dataportabilitet**, att **invända** mot behandling som bygger på berättigat intresse, och att när som helst **återkalla ditt samtycke** där samtycke är grunden (DNS-skölden: återkalla genom att stänga av den; det påverkar inte behandling som redan skett).

**En ärlig begränsning.** För nästan allt som appen rör vid har vi inga uppgifter som kan identifiera dig och inget konto som skulle kunna koppla en begäran till en person. Enligt **GDPR art. 11** är vi inte skyldiga att skaffa extra information bara för att kunna identifiera dig, och vi kommer inte att be dig om ID-handlingar för att hantera en begäran som vi inte har några data att besvara med. I praktiken:

- **Innehåll du skrivit:** utöva rättigheterna direkt. Det finns på din enhet och i din iCloud, och om du raderar appen (och kopian i iCloud) försvinner det helt.
- **Uppgifter om köp:** kontakta Apple, eller kontakta oss så skickar vi din begäran vidare till RevenueCat, som är vårt personuppgiftsbiträde.
- **Användningsanalys:** din **rätt enligt art. 21 att invända** mot våra berättigade intressen har ett reglage i stället för en supportkö: Inställningar → Dina data → **Dela anonym användning**, av. Då stoppas nya signaler direkt, sändaren kopplas bort och de signaler som väntar på enheten raderas. Du behöver inte skriva till oss och du behöver inte ange något skäl. Det som redan skickats går inte att hämta tillbaka, och går inte heller att hitta igen, eftersom inget i det identifierar dig.
- **Annonsmätning:** samma reglage är din invändning även mot detta. Vill du få det AppsFlyer redan har om din installation raderat, använd AppsFlyers eget formulär (avsnitt 2). Vi kan inte söka upp din installation åt dig, av skälet ovan: vi har inget som knyter en installation till en person.

Skriv till [support@trysilex.com](mailto:support@trysilex.com) så svarar vi inom en månad, som art. 12.3 kräver.

**Rätt att klaga.** Du kan lämna in ett klagomål till dataskyddsmyndigheten i ditt land. I Sverige är det [Integritetsskyddsmyndigheten (IMY)](https://www.imy.se/privatperson/utfora-arenden/lamna-ett-klagomal/). Listan över myndigheter finns på [edpb.europa.eu](https://edpb.europa.eu/about-edpb/board/members_en), och i Storbritannien är det [ICO](https://ico.org.uk/make-a-complaint/). Du behöver inte kontakta oss först, men vi uppskattar om du gör det.

## 8. Radera allt

- Ta bort appen från din iPhone.
- Ta bort kopian i iCloud: Inställningar → ditt namn → iCloud → Hantera lagring för kontot → Silex.
- Säg upp en prenumeration: Inställningar → ditt namn → Abonnemang, eller länken Hantera prenumeration i appen.

## 9. Känsliga uppgifter, och varför konstruktionen är policyn

Det du registrerar här handlar om din hälsa och din ekonomi, och vi behandlar det så. Inga konton att göra intrång i, ingenting på någon server hos oss att begära ut, och ingenting hos någon leverantör som kan läsas som *ditt* tillfrisknande. Det starkaste skydd vi kan erbjuda är att inte ha dina uppgifter alls. Den delen är byggd in i konstruktionen och inte ett löfte: det finns ingen nyckel, ingen säkerhetskopia och ingen kopia, så det finns inget att i tysthet ändra sig om.

**Vad som har ändrats.** Fram till augusti 2026 stod det också här att ingen analysleverantör hade någon kopia. Det stämmer inte längre: TelemetryDeck har en räkning av hur många installationer som nått varje skärm. Det är en verklig försvagning av garantin, och vi tänker inte kalla det något annat. Det som står kvar är den del som gör jobbet: innehållet stannar på din telefon, identifieraren som följer med räkningen går inte att knyta till dig eller följa mellan appar, och allt har ett reglage. Det vi gav upp är möjligheten att säga ordet *ingen*.

I november 2026 tillkom en andra leverantör: AppsFlyer får veta att en installation har skett och om det ledde till en provperiod eller ett köp, så att vi kan se vilka annonser som är värda pengarna. Det är en andra försvagning, och samma saker står kvar: inget du registrerat lämnar din telefon, det finns inget annons-ID och reglaget täcker det.

Den 22 november 2026 kom en tredje, och det är den vi tycker minst om: så länge vi annonserar på Facebook och Instagram får Meta veta att en installation finns (avsnitt 2, ”Annonser hos Meta”). Inget du registrerat lämnar din telefon och reglaget täcker det fortfarande, men så länge det pågår kan vi inte längre säga att inget annonsföretag får veta om en enskild installation. Om det upphör skriver vi in datumet här.

## 10. Barn

Silex är avsedd för vuxna och riktar sig inte till barn. Vi samlar inte medvetet in uppgifter från någon under 18 år. Åldersgränsen i App Store är satt därefter.

## 11. Ändringar

Om den här policyn ändras, ändras datumet högst upp, och den gällande versionen finns alltid på den här adressen.

Att lägga till TelemetryDeck är en väsentlig ändring, och den tidigare versionen av det här avsnittet lovade att väsentliga ändringar skulle visas i appen. **Vi har ändrat det löftet i stället för att påstå att vi höll det.** Appen har ingen funktion som visar ett meddelande vid uppdatering, och vi tänker inte beskriva en som inte finns. Det den här versionen faktiskt gör är att lägga reglaget i Inställningar med en tydlig beskrivning bredvid av vad som skickas. Det syns för den som tittar, men trycks inte på den som inte gör det. Det är mindre än vad den gamla meningen lovade, och just därför var det meningen som måste ändras och inte berättelsen om vad som hände.

Att lägga till AppsFlyer i november 2026 är en väsentlig ändring av samma slag, och den görs på samma sätt: den nämns här och i versionsnyheterna, under det reglage som redan fanns, och texten intill reglaget har ändrats så att det framgår.

Löftet lyder alltså nu: väsentliga ändringar nämns i det här avsnittet och i versionsnyheterna i App Store för den version som gör dem, och varje ändring som utökar vad som lämnar din enhet kommer tillsammans med reglaget för det i samma version.

Delningen med Meta den 22 november 2026 är en väsentlig ändring som det löftet inte förutsåg. Inget nytt lämnar din enhet. Det som ändrades är att AppsFlyer skickar en del av det vidare, och det slogs på i AppsFlyers inställningar, inte i en version av appen. Det fanns därför inga versionsnyheter att nämna det i. Det nämns här samma dag som det började, det befintliga reglaget täcker det, och versionsnyheterna till nästa version kommer att ta upp det.

## 12. Kontakt

[support@trysilex.com](mailto:support@trysilex.com)

## 13. Det kostnadsfria webbläsartillägget

Den här texten gäller också **Silex — Free Gambling Blocker**, webbläsartillägget för Chrome, Microsoft Edge och Firefox. Det är enklare än appen, och det är avsnittet också:

- **Det samlar inte in något.** Inget konto, ingen analys, inga identifierare, och det gör inga egna nätverksförfrågningar. Ingenting om dig eller om vad du surfar på skickas till oss eller till någon annan.
- **Så blockerar det.** Tillägget bär med sig en lista över speldomäner. Din webbläsare jämför sidorna du öppnar med den listan lokalt, med sin inbyggda funktion `declarativeNetRequest`. Webbläsaren rapporterar inte tillbaka till tillägget, eller till oss, vilka sajter du besöker eller vilka som blockerades.
- **Varför det ber om åtkomst till alla sajter.** Webbläsare låter bara ett tillägg ersätta en blockerad sida med sin egen hjälpsida, i stället för att visa ett fel, om det har åtkomst till de sajter det gäller. Åtkomsten används inte till något annat: tillägget läser, ändrar och samlar inte in innehållet på någon sida.
- **Hjälpsidan** visar stödlinjer och länkar till den här webbplatsen. Att följa en länk är ett vanligt besök på trysilex.com, som omfattas av resten av den här texten.
- **Att rapportera en sajt som saknas** öppnar din egen mejlapp. Vad du skickar är upp till dig. Vi använder det bara för att uppdatera listan och svara.
- **Att ta bort tillägget** tar bort det och allt som finns i det.

Domänlistan bygger på The Blocklist Project (fri att använda, public domain) och UT1-listorna från Université Toulouse Capitole (CC BY-SA 4.0).

## 14. Loggboken i Notion

**Silex Recovery Tracker for Notion** är en valfri, kostnadsfri koppling som skapar en loggbok för ditt tillfrisknande i din egen arbetsyta i Notion. Den har inget med appen att göra: det ena påverkar inte det andra.

- **Vad som körs, och var.** En liten funktion som vi har skrivit och som ligger hos Cloudflare. Den körs bara de få sekunderna efter att du har klickat på Connect och godkänt åtkomsten i Notion.
- **Vad den tar emot.** Notion skickar en engångskod, som den byter mot en åtkomstnyckel till din arbetsyta. Notions svar innehåller också arbetsytans namn och din Notion-profil (namn, och eventuellt e-postadress och profilbild). Funktionen läser bara åtkomstnyckeln och bortser från resten.
- **Vad den gör med åtkomstnyckeln.** Den skapar en sida, två tabeller och två exempelrader i din arbetsyta och skickar dig sedan till sidan. Den läser eller söker inte igenom dina befintliga sidor, utom, och bara om Notion nekar en sida på översta nivån, för att hitta den enda sida du valde att dela, så att loggboken kan läggas där.
- **Vad den sparar.** Ingenting. Åtkomstnyckeln finns bara i minnet under den enda förfrågan. Det finns ingen databas, ingen fil och ingen kopia av det du skriver i loggboken. Vi kan inte öppna den efteråt, och om Notion ger ett felsvar loggas bara Notions felkod, aldrig något innehåll från arbetsytan.
- **Ta bort den.** Gå till Settings → Connections (inställningarna för anslutningar) i Notion och ta bort Silex. Loggboken ligger kvar: den är en vanlig sida som tillhör dig. Radera den som vilken annan sida som helst.

Rättslig grund: den begäran du gör genom att klicka på Connect (GDPR art. 6.1 b). Cloudflare behandlar själva anslutningen (din IP-adress och förfrågans rubriker) som vårt personuppgiftsbiträde. Se [Cloudflares integritetspolicy](https://www.cloudflare.com/privacypolicy/). Det du skriver i loggboken är en sak mellan dig och Notion, enligt [Notions integritetspolicy](https://www.notion.com/trust/privacy-policy).

## 15. Silex Help i ChatGPT och andra AI-assistenter

**Silex Help** är en kostnadsfri tjänst som bara läser och svarar. AI-assistenter som ChatGPT kan anropa den för att svara på frågor om att sluta spela om pengar: stödlinjer i ett land, system för självavstängning, om en webbplats finns på vår lista över speldomäner, självtestet PGSI och guider för blockering. Den har inget med appen att göra, och den har inga konton.

- **Vad den tar emot.** Bara det assistenten skickar när den använder ett verktyg: ett land, webbadresserna som ska kontrolleras eller dina nio svar på självtestet. Din konversation, ditt namn och ditt konto hos assistenten skickas inte till oss.
- **Vad den gör.** Den slår upp svaret i data som följer med tjänsten och skickar tillbaka det. Den gör inga förfrågningar till någon annan.
- **Vad den sparar.** Ingenting. Varje förfrågan hanteras i minnet och glöms bort. Det finns ingen databas och ingen logg över vad som frågats.
- **Själva assistenten.** Det du skriver till ChatGPT eller en annan assistent omfattas av den leverantörens egen integritetspolicy, inte den här.

Rättslig grund: den begäran din assistent gör för din räkning (GDPR art. 6.1 b). Cloudflare driver tjänsten och behandlar varje anslutning (IP-adress och förfrågans rubriker) som vårt personuppgiftsbiträde. Se [Cloudflares integritetspolicy](https://www.cloudflare.com/privacypolicy/).

## Om du behöver prata med någon nu

- Sverige: [020-81 91 00](tel:020819100) — Stödlinjen, spel om pengar: gratis och anonymt, vardagar (mån 9–19, tis–ons 9–17, tors 11–19, fre 9–15)
- Sverige: [08-37 43 00](tel:08374300) — Föreningen Spelfriheten, kamratstöd för spelare och anhöriga, dygnet runt
- Sverige: [90101](tel:90101) — Självmordslinjen (Mind), dygnet runt, anonymt
- Sverige: [90390](tel:90390) — Hjälplinjen, dygnet runt, gratis och anonymt
- Nödläge: [112](tel:112) — Vid direkt livsfara
- Andra länder: [findahelpline.com](https://findahelpline.com) — Krislinjer där du är
