> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/sv/blockera-spel-iphone/

# Så blockerar du spelsajter och spelappar på iPhone

Av [Kyrylo Lozovyi](https://trysilex.com/sv/om-silex/) · 25 november 2026

**Kort svar:** Skärmtid räcker inte ensamt. Det som håller är kombinationen: en **DNS-profil för hela telefonen** (täcker alla appar och webbläsare), **Skärmtid med en lösenkod som någon annan har** (stoppar ominstallation) och två lager utanför telefonen: **Spelpaus**, som inte kan avslutas i förtid, och en **spärr på pengarna hos banken**. Att ställa in alltihop tar ungefär en halvtimme.

Har du Android i stället? [Här är guiden för Android](https://trysilex.com/sv/blockera-spel-android/). Det inbyggda gratisalternativet där är faktiskt bättre.

Det finns fem olika sätt att blockera spel om pengar på en iPhone, och de täcker olika saker. De flesta guider tar upp ett, det har ett hål, och det är genom hålet som återfallet kommer. Här är allihop, med ärliga begränsningar för vart och ett.

## Börja här: vad varje sätt faktiskt täcker

| Sätt | Täcker | Hur fort kan du ångra det? | Kostnad |
|---|---|---|---|
| Begränsningar i Skärmtid | Installation av appar, utvalda webbplatser i Safari, att dölja appar | Några sekunder, om inte någon annan har lösenkoden | Gratis |
| DNS-profil för hela telefonen | **Alla appar och alla webbläsare**, på wifi och i mobilnätet | Ungefär en minut, i Inställningar | Det finns gratisalternativ |
| Safari-blockerare | Bara Safari | Några sekunder | Gratis eller ingår i en app |
| Spelspärr hos banken | Kortköp hos spelbolag | Upp till 48 timmar hos Revolut. De flesta svenska banker har ingen sådan knapp | Fråga din bank |
| Spelpaus | Allt spel som kräver registrering hos spelbolag med svensk licens | **Inte i förtid** (10 dagar, 1, 3 eller 6 månader, eller tills vidare med minst 12 månader) | Gratis |

Läs tabellen som lager ovanpå varandra, inte som en meny. De tre första gör det krångligt att spela. De två sista gör det svårt på riktigt. Den som bara gör de tre första får ofta återfall genom en webbläsare eller ett betalsätt som hen glömt bort.

## 1. Skärmtid: stoppa installationer och utvalda sajter

Skärmtid är gratis, finns redan i telefonen och gör mest nytta genom det den *hindrar*, inte det den filtrerar.

**Stoppa nya spelappar.** Radera spelapparna först. Var du sedan stänger av installationen beror på vilken version av iOS du har:

- **iOS 27:** Inställningar → Skärmtid → **Appar och webbplatser** → **Begränsningar** → stäng av **Installera appar**. Där App Store, Webb och Appmarknadsplatser står under reglaget sätts alla tre till **Blockerat** när du stänger av det.
- **iOS 26 och tidigare:** Inställningar → Skärmtid → **Begränsa innehåll/integritet** → slå på → **Installation och köp av appar** (i en del versioner **Köp i iTunes och App Store**) → **Installera appar** → **Tillåt inte**.
- **I EU på iOS 26** går det också att hämta appar utanför App Store, så det räcker inte att spärra den. Sätt **Appmarknadsplatser** och **Webb** till **Tillåt inte** på samma ställe. [Apple skriver](https://support.apple.com/sv-se/118128) att de två förblir tillåtna efter en uppdatering även om du redan hade begränsningar på, så titta efter.

Det är den mest värdefulla knappen i hela telefonen. När den är på krävs lösenkoden för Skärmtid för att installera om apparna.

**Blockera spelsajter i Safari:**

- **iOS 27:** Skärmtid → **Appar och webbplatser** → **Blockerat** → **+**. Skriv in varje spelbolags adress eller klistra in en hel lista. Välj också **Begränsa vuxet innehåll** under **Begränsningar** → **Filtrering**: enligt iOS blockerar det webbproxyer också. När en lösenkod för Skärmtid är inställd begränsar iOS dessutom privat surfning.
- **iOS 26 och tidigare:** Begränsa innehåll/integritet → **App Store, medier, webb och spel** → **Webbinnehåll** → **Begränsa vuxet innehåll**. Tryck sedan på **Lägg till webbplats** under **Tillåt aldrig** och lägg in varje spelbolag. Det stänger också av privat surfning i Safari, vilket är en bra bieffekt.

Vi kontrollerade menyerna för iOS 27 i iOS 27.1 i Apples simulator den 25 november 2026. Apples egen [hjälpsida](https://support.apple.com/sv-se/105121) beskriver spärrar för installation och webbplatser bara på ett barns enhet (Inställningar → Familj → barnets namn → Appar och webbplatser), så en etikett kan skilja sig lite på din.

**Haken som ingen nämner:** iOS har ingen kategori för spel om pengar. Begränsa vuxet innehåll är ett filter för vuxeninnehåll. Det råkar fånga en del spelsajter och missar de flesta spelbolag. Är det allt du har blockeras inget av det du faktiskt använder. Att lägga in sajterna själv fungerar, men då sköter du listan för hand mot en bransch med tusentals spegeldomäner.

**Gör den här delen ordentligt:** ställ in en lösenkod för Skärmtid som du inte känner till. På iOS 27: Skärmtid → **Lösenkod och hantering** → **Lås inställningarna för Skärmtid** (i iOS 27.1 heter det första steget **Hantera Skärmtid**). Låt din partner, en vän eller någon i familjen skriva in koden och behålla den. Använd inte ditt eget Apple-konto för **Återställning av lösenkod för Skärmtid**: det konto som anges där kan återställa koden. Låt den andra personen ange sitt. Allt ovan är ångrat på fem sekunder för den som har koden, så se till att det inte är du klockan ett på natten.

Och ta inte koden för en mur. Apples sidor säger olika saker om att byta den på iOS 27: [den ena](https://support.apple.com/sv-se/102677) kräver Face ID eller telefonens egen lösenkod, och Apple-kontot för återställning om iOS frågar, [den andra](https://support.apple.com/sv-se/guide/iphone/iph272b4c4bd/ios) kräver den nuvarande lösenkoden för Skärmtid. Det är lagren utanför telefonen du ska luta dig mot.

## 2. En DNS-profil för hela telefonen: det som täcker allt

Det här hoppar de flesta guider över, och det är det starkaste som kan sitta i själva telefonen. Varje app och webbläsare måste slå upp ett domännamn innan den kan ansluta. Om uppslagningen misslyckas så misslyckas appen. Inga tillägg behövs, inget ska ställas in per webbläsare, och det fungerar lika bra i mobilnätet som på wifi.

iOS låter en app eller en konfigurationsprofil installera en inställning för krypterad DNS (DoH) som gäller hela telefonen. Rikta den mot en tjänst som filtrerar spel, så slutar varje spelbolag, nätkasino och slotssajt att gå att nå. Även de utan svensk licens.

Gratis och betalda alternativ som filtrerar spel om pengar:

- **Mullvads öppna DoH-tjänst**: en gratis ”family”-variant som blockerar spel om pengar bland flera kategorier, med en publicerad policy om att inget loggas.
- **NextDNS**: gratisnivå som räcker för måttlig användning, med en blockeringslista för spel som du slår på plus en stor katalog med listor från andra användare.
- **Control D**: samma idé, filtrering per kategori, gratisnivå finns.
- **En blockerare som installerar profilen åt dig**, till exempel [Silex](https://trysilex.com/sv/), som ställer in en krypterad DNS-sköld och slår ihop öppna listor med speldomäner så att du slipper sköta någon själv.

Kontrollera efteråt: under Inställningar → Allmänt → **VPN och enhetshantering** (med en DNS-profil heter den **VPN, DNS och enhetshantering**) → DNS ska din konfiguration vara vald, och en känd spelsajt ska inte ladda i en webbläsare du inte brukar använda.

**Begränsningen, rakt ut:** du kan stänga av den i Inställningar på under en minut. DNS-filtrering är ett farthinder mot ett starkt sug, inte en mur. Det är ett utmärkt farthinder (de flesta återfall är impulsiva, och en minuts motstånd räcker ofta), men se det inte som sista linjen.

## 3. Safari-blockerare

Ett blockerande tillägg kan få Safari att vägra ladda en lista med domäner. Slå på det under Inställningar → Appar → Safari → **Tillägg** och sedan **Tillåt tillägg**. Silex har ett, och det har de flesta appar som är gjorda för att blockera.

Användbart, men smalt: det täcker Safari och inget annat. Chrome, Firefox, Edge, webbläsaren inuti en social app och spelbolagets egen app påverkas inte alls. Se en Safari-blockerare som ett komplement till DNS-filtret, aldrig som en ersättning.

## 4. Gör det svårt att betala

Att stänga vägen till spelet är bara halva jobbet. Den andra halvan är att göra pengarna svåra att flytta. Det är här Sverige skiljer sig från till exempel Storbritannien: vi har inte hittat någon svensk storbank som beskriver en spelspärr som du själv kan slå på. Revolut har en Spelspärr för kortköp som tar upp till 48 timmar att häva. Hos Nordea och Handelsbanken kan du stänga kortet för internetköp. Stödlinjen skriver att vissa banker kan hjälpa dig att blockera vissa typer av köp, så fråga din.

Det är fördröjningen som är poängen: spärren ska överleva suget. [Så gör du, bank för bank.](https://trysilex.com/sv/sparra-speltransaktioner-banken/)

## 5. Stäng av dig vid källan

Det starkaste lagret sitter inte i telefonen. Självavstängning betyder att spelbolagen måste neka dig under en viss tid. I Sverige räcker det med en registrering: **[Spelpaus.se](https://www.spelpaus.se/)** är gratis och gäller allt spel som kräver registrering hos alla spelbolag med svensk licens, på nätet, i butik och på bana.

Du kan inte avsluta den i förtid. Det är just därför den fungerar. [Hela guiden till självavstängning finns här.](https://trysilex.com/sv/stang-av-dig-fran-spel/)

## Det som inte fungerar

- **Att bara radera apparna.** Att installera om tar femton sekunder, och mobilsajten fungerar utmärkt utan någon app.
- **Bara spärr i routern.** Filter på wifi hemma, även en Pi-hole eller ändrad DNS i routern, försvinner så fort telefonen byter till mobilnätet. Gör det gärna också, men aldrig i stället.
- **En vanlig VPN.** Den flyttar din trafik, den filtrerar den inte. En del integritets-VPN har ett DNS-läge som filtrerar innehåll, och det fungerar. Den vanliga VPN:en gör inget för dig här.
- **En app som bara räknar dagar.** Att räkna ger motivation men är inget hinder. Du behöver båda, och hindret först.
- **Allt som lovar att det inte går att ta bort på iOS.** Systemet tillåter det inte. Sådana löften är reklam, och den som tror på dem får ett lager i stället för fyra.

## Halvtimmen, i rätt ordning

1. Radera alla spelappar. Logga ut från konton hos spelbolag som fortfarande är inloggade i webbläsaren.
2. Slå på en filtrerande DNS-profil och kontrollera att en spelsajt inte laddar.
3. Stäng av Installera appar i Skärmtid, och Appmarknadsplatser och Webb om din iPhone har dem. Blockera de sajter du faktiskt har använt. Låt någon annan ställa in lösenkoden.
4. Slå på en Safari-blockerare.
5. Fråga banken om en spelspärr, eller stäng kortet för internetköp.
6. Stäng av dig på Spelpaus. Har du konton hos spelbolag utan svensk licens, be dem om permanent avstängning var för sig.

Steg 5 och 6 är de man skjuter upp, och det är de som gör störst skillnad. Börja med dem om du bara har tio minuter.

## Spärrarna är golvet, inte planen

Varje lager ovan ger dig tid under de nittio sekunder då suget är som starkast. Det du gör med den tiden avgör om det fungerar nästa gång också. [Ett sug stiger, toppar och sjunker i en ganska förutsägbar kurva](https://trysilex.com/sv/hur-lange-varar-spelsug/), och att vänta ut ett är en färdighet som blir bättre av övning. Det är vad [90-dagarsdelen av det här](https://trysilex.com/sv/sluta-spela/) är till för.

## Sluta spela. Behåll pengarna.

Silex blockerar spel om pengar i hela telefonen och följer dig genom 90 dagar, en i taget.

[Hämta Silex till iPhone](https://apps.apple.com/app/id6798826038?mt=8) [Hämta Silex till Android](https://play.google.com/store/apps/details?id=com.klozovyi.stopgamble&referrer=utm_source%3Dtrysilex%26utm_campaign%3Dsv_iphone_guide)

## Vanliga frågor

### Kan jag blockera spel på iPhone utan en app?

Ja. Skärmtid kan hindra installation av appar och blockera vissa webbplatser, och iOS kan använda en DNS-konfiguration som gör att speldomäner inte går att nå i någon app. Båda är gratis och inbyggda. Det iOS inte klarar på egen hand är att hålla en lista med hundratusentals speldomäner aktuell. Det är det en blockerare eller en filtrerande DNS-tjänst lägger till.

### Blockerar Skärmtid spelappar?

Delvis. Skärmtid kan hindra att nya appar installeras, dölja appar du har och blockera vissa webbplatser i Safari. Men den har ingen kategori för spel om pengar, så Begränsa vuxet innehåll är inget spelfilter. Du får lägga till domäner själv, eller använda en filtrerande DNS-tjänst som sköter listan åt dig.

### Går det att blockera spelappar för alltid på iPhone?

Nej, och appar som påstår det lovar för mycket. På iOS kan du alltid ta bort en profil eller radera en app. Det som ska hålla måste komma utifrån: Spelpaus, som inte kan avslutas i förtid, och en spärr på pengarna som tar tid att häva. Det räcker för att suget ska hinna gå över.

### Blockerar en VPN spelsajter?

En vanlig VPN gör inte det. Den ändrar var din trafik går ut på nätet, inte vad den når. Det du vill ha är en filtrerande DNS-tjänst eller en blockerare som bygger på DNS. En del integritets-VPN har ett DNS-läge som filtrerar innehåll, och det fungerar.

### Fungerar blockeringen i mobilnätet också?

En DNS-konfiguration som är installerad på telefonen gör det, för den hör till telefonen. En spärr i routern gör det inte. Den slutar vid ytterdörren, och telefonen är tillbaka på spelsajterna så fort den byter till 5G. Det är den vanligaste orsaken till att spärrar hemma inte håller.

## Om du behöver prata med någon nu

- Sverige: [020-81 91 00](tel:020819100) — Stödlinjen, spel om pengar: gratis och anonymt, vardagar (mån 9–19, tis–ons 9–17, tors 11–19, fre 9–15)
- Sverige: [08-37 43 00](tel:08374300) — Föreningen Spelfriheten, kamratstöd för spelare och anhöriga, dygnet runt
- Sverige: [90101](tel:90101) — Självmordslinjen (Mind), dygnet runt, anonymt
- Sverige: [90390](tel:90390) — Hjälplinjen, dygnet runt, gratis och anonymt
- Nödläge: [112](tel:112) — Vid direkt livsfara
- Andra länder: [findahelpline.com](https://findahelpline.com) — Krislinjer där du är
