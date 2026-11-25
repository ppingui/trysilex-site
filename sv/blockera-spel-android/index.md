> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/sv/blockera-spel-android/

# Så blockerar du spel om pengar på Android

Av [Kyrylo Lozovyi](https://trysilex.com/sv/om-silex/) · 25 november 2026

**Kort svar:** Android har den bästa inbyggda gratisspärren mot spel av alla telefoner, och nästan ingen använder den: **Inställningar → Nätverk och internet → Privat DNS → Värdnamn för privat DNS-leverantör**, inställt på en filtrerande tjänst som `family.dns.mullvad.net`. Det täcker alla appar och webbläsare, både på wifi och i mobilnätet, på ungefär två minuter och utan kostnad. Lägg sedan på en **pinkod för föräldrakontroller** som någon annan väljer (Android 17 och senare), en **spärr hos banken** och **Spelpaus**.

**Rakt svar först:** Silex finns på Android nu, men du behöver inte appen till något på den här sidan. Det här är vad vi skulle rekommendera en vän med Android, och det inbyggda gratisalternativet är bättre än de flesta betalapparna.

## 1. Privat DNS: två minuter, och allt täcks

Android har haft stöd för krypterad DNS i hela systemet sedan Android 9. Rikta den mot en tjänst som filtrerar spel, så slutar de domänerna att fungera i alla appar och alla webbläsare (spelbolagens egna appar också), på wifi och i mobilnätet.

1. Öppna **Inställningar** → **Nätverk och internet**. På en del telefoner, till exempel från Samsung, ligger det på ett annat ställe. Sök då efter ”Privat DNS” i Inställningar.
2. Tryck på **Privat DNS**.
3. Välj **Värdnamn för privat DNS-leverantör**.
4. Skriv in värdnamnet till en filtrerande tjänst och tryck på **Spara**.

Tjänster som filtrerar spel om pengar:

| Värdnamn | Vad den filtrerar | Kostnad |
|---|---|---|
| `family.dns.mullvad.net` | Spel om pengar, vuxeninnehåll, annonser och spårare | Gratis, inget konto, publicerad policy om att inget loggas |
| `<ditt-id>.dns.nextdns.io` | Det du själv slår på (spel om pengar är en kategori med ett tryck) | Gratisnivå, kräver konto, ger dig loggar och kontroll |

**Testa att det fungerar.** Öppna en webbläsare du inte brukar använda och försök gå till en spelsajt som du faktiskt har använt. Den ska inte ladda alls, inte bara se konstig ut. Laddar den, kolla att ingen VPN är på. En VPN tar över DNS och kör tyst över den här inställningen.

**Haken:** den går att stänga av i Inställningar på ungefär en minut. Det är ändå värt något. De flesta återfall är impulsiva, och en minuts motstånd stoppar många av dem. Men en mur är det inte. Därför kommer nästa steg.

## 2. Se till att du inte kan ändra inställningarna själv

Det är det här steget som gör ett farthinder till något stadigare.

- **Pinkod för föräldrakontroller (Android 17 och senare).** Gå till Inställningar → **Föräldrakontroller** → **Ställ in en pinkod för föräldrakontroller**, och låt en partner, förälder eller vän välja koden och behålla den. Där går det att blockera appar, och **Appbutiksfilter** begränsar nya installationer efter åldersgräns. Google kräver att appar för spel om riktiga pengar har en [åldersgräns för vuxna](https://support.google.com/googleplay/android-developer/answer/9877032). Medan kontrollerna är på krävs pinkoden även för att lägga till användare och återställa telefonen. Om ni lägger till ett återställningskonto ska det vara den andras, inte ditt, för det kan återställa pinkoden ([Googles anvisning](https://support.google.com/android/answer/16766047?hl=sv)).
- **Äldre Android: pinkod för appgränser.** Inställningar → **Digitalt välmående** → **Appgränser** → **Pinkod för appgränser**. Om någon annan har pinkoden räcker tidsgränsen noll för att [blockera en app](https://support.google.com/android/answer/9346420?hl=sv).
- **Innehållsbegränsningar i Google Play.** Play Butik → profilikonen → **Inställningar** → **Familj** → **Innehållsbegränsningar**. En äldre pinkod för Play [går att återställa](https://support.google.com/googleplay/answer/1075738?hl=sv) genom att rensa Play Butiks data, så räkna den som ett hinder, inte en spärr.
- **Google Family Link fungerar sämre mellan vuxna.** Google beskriver det för barn och tonåringar, och det är bara den som är under 18 som behöver en förälders godkännande för att avsluta kontrollen. Som vuxen kan du alltså inte räkna med att det håller emot.
- **Ta bort apparna.** Play Butik → profilikonen → **Hantera appar och enheter** → **Hantera** → **Avinstallera**. Gör det med varje spelapp innan den andra personen ställer in sin pinkod.
- **Digitalt välmående utan pinkod** har apptimers och Fokusläge. Bra för att bromsa en vana, men det går att stänga av hur lätt som helst, så räkna inte det som en spärr.

Menyerna skiljer sig mellan tillverkare, och för ingen av de här inställningarna skriver Google att de låser själva Privat DNS.

## 3. Appar som kan vara värda det

| App | Pris | Värd det för |
|---|---|---|
| **BetBlocker** | Gratis, inga annonser, drivs av en ideell organisation | En spärr på 1 dag till 5 år som inte går att korta när den väl har börjat. Ett sätt att binda dig i förväg som inte kostar något |
| **Gamban** | 4,99 pund/månad eller 29,99 pund/år, 7 dagars provperiod | Ett abonnemang för Android, iOS, Windows och Mac, [eller något av alternativen](https://trysilex.com/sv/alternativ-till-gamban/) |
| **GamBlock** | Kostar pengar, priset står inte på startsidan | Hävdar att borttagning ”inte kan hända” på Android och att fabriksåterställning blockeras. Det tyngsta låset, om löftena håller på din telefon |

Priserna är kollade på varje företags egen sajt den 25 november 2026. [Hela jämförelsen →](https://trysilex.com/sv/basta-apparna-blockera-spel/)

## 4. De två lagren som inte sitter i telefonen

De fungerar likadant på alla telefoner och är starkare än allt ovan:

1. [**Spelpaus**](https://trysilex.com/sv/stang-av-dig-fran-spel/): gratis, gäller alla spelbolag med svensk licens och kan inte avslutas i förtid, hur starkt suget än är.
2. [**En spärr på pengarna**](https://trysilex.com/sv/sparra-speltransaktioner-banken/): få svenska banker har en färdig spelspärr, men Revolut har en som tar upp till 48 timmar att häva, och hos till exempel Nordea och Handelsbanken kan du stänga kortet för internetköp.

Om du bara har tio minuter i dag, börja med de här två och ta telefonens inställningar efteråt.

## Det som inte fungerar på Android

- **Att bara avinstallera apparna.** Mobilsajten fungerar, och att installera om tar några sekunder.
- **Bara filter i routern eller på wifi.** Det slutar vid ytterdörren. Mobilnätet går rakt förbi.
- **En vanlig VPN.** Den filtrerar inget, och den kan slå ut din inställning för Privat DNS.
- **Att blockera en enda webbläsare.** På tjugo sekunder har du installerat en annan.

## Sedan kommer det som ingen blockerare gör

Varje lager ovan ger dig tid när suget kommer, och ett sug går över på ungefär 20 till 30 minuter vare sig du spelar eller inte. Det du gör med de minuterna avgör om det håller: [att rida ut suget](https://trysilex.com/sv/hur-lange-varar-spelsug/), och [hela planen](https://trysilex.com/sv/sluta-spela/). Inget av det kräver en iPhone eller en prenumeration.

## Vanliga frågor

### Vilken är den bästa gratis spelblockeraren för Android?

Androids egen inställning Privat DNS, riktad mot en filtrerande tjänst. Den blockerar mer än de flesta betalappar: alla appar och webbläsare, i mobilnätet såväl som på wifi. Vill du ha en app där du kan låsa en bestämd tid är BetBlocker gratis, drivs av en ideell organisation och fungerar på Android.

### Fungerar Privat DNS i mobilnätet?

Ja. Det är därför den är bättre än spärrar i routern eller på wifi, som slutar fungera så fort telefonen lämnar hemmet. Privat DNS är en inställning i telefonen och gäller överallt.

### Kan jag hindra mig själv från att stänga av Privat DNS?

Inte med bara den inställningen. Den går att stänga av i Inställningar, så den är ett farthinder och ingen mur. Family Link hjälper inte mycket för en vuxen: Google beskriver det för barn och tonåringar, och det är bara den som är under 18 som behöver en förälders godkännande för att avsluta kontrollen. På Android 17 och senare kan någon annan välja din pinkod för föräldrakontroller, och det finns blockerare som är svåra att ta bort. Lita i första hand på Spelpaus, som inte kan avslutas i förtid, och på en spärr på pengarna som tar tid att häva.

### Fungerar Silex på Android?

Ja, på Android 8.0 och senare, från Google Play. Appen ställer in Privat DNS-spärren från den här sidan åt dig och lägger till ett 90-dagarsprogram, en SOS-knapp mot suget och en räknare för dina behållna pengar. Det är en betald prenumeration. Om du bara vill ha spärren klarar gratisinställningen på den här sidan plus BetBlocker eller Gamban det jobbet.

### Blockerar en VPN spelsajter på Android?

En vanlig VPN, nej. Den flyttar platsen där din trafik går ut på nätet, den filtrerar inget. En del integritets-VPN har ett DNS-läge som filtrerar innehåll och som kan blockera spel. Tänk på att en aktiv VPN kan köra över inställningen Privat DNS. Det är en vanlig orsak till att blockeringen slutar fungera utan att du märker det.

## Om du behöver prata med någon nu

- Sverige: [020-81 91 00](tel:020819100) — Stödlinjen, spel om pengar: gratis och anonymt, vardagar (mån 9–19, tis–ons 9–17, tors 11–19, fre 9–15)
- Sverige: [08-37 43 00](tel:08374300) — Föreningen Spelfriheten, kamratstöd för spelare och anhöriga, dygnet runt
- Sverige: [90101](tel:90101) — Självmordslinjen (Mind), dygnet runt, anonymt
- Sverige: [90390](tel:90390) — Hjälplinjen, dygnet runt, gratis och anonymt
- Nödläge: [112](tel:112) — Vid direkt livsfara
- Andra länder: [findahelpline.com](https://findahelpline.com) — Krislinjer där du är
