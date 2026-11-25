> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/da/blokere-pengespil-iphone/

# Sådan blokerer du spilsider og spilapps på iPhone

Af [Kyrylo Lozovyi](https://trysilex.com/da/om-silex/) · 25. november 2026

**Kort svar:** Skærmtid alene er ikke nok. Det, der holder, er kombinationen: en **DNS-profil for hele telefonen** (dækker alle apps og browsere), **Skærmtid med en kode, som en anden har** (gør det sværere at hente apps igen), og to lag uden for telefonen: **ROFUS**, som ikke kan annulleres, og en **spærring på pengene**. Det tager cirka en halv time at sætte det hele op.

Har du Android i stedet? [Her er guiden til Android](https://trysilex.com/da/blokere-pengespil-android/). Den indbyggede gratis løsning dér er faktisk bedre.

Der er fem forskellige måder at blokere pengespil på en iPhone, og de dækker forskellige ting. De fleste guider nævner én, den har et hul, og det er gennem hullet, tilbagefaldet kommer. Her er de alle fem med de ærlige begrænsninger ved hver.

## Begynd her: hvad hver måde faktisk dækker

| Måde | Dækker | Hvor hurtigt kan du fortryde? | Pris |
|---|---|---|---|
| Begrænsninger i Skærmtid | Installation af apps, udvalgte hjemmesider i Safari, at skjule apps | Få sekunder, lidt længere hvis en anden har koden | Gratis |
| DNS-profil for hele telefonen | **Alle apps og alle browsere**, på wi-fi og mobildata | Cirka et minut, i Indstillinger | Findes gratis |
| Safari-blokering | Kun Safari | Få sekunder | Gratis eller med i en app |
| Spilspærring i banken | Kortbetalinger til spiludbydere | Op til 48 timer hos Revolut. Næsten ingen danske banker beskriver sådan en | Spørg din bank |
| ROFUS | Onlinespil hos spiludbydere med dansk tilladelse, fysiske kasinoer og væddemål i butikker | **Ikke før tid** (24 timer, 1, 3 eller 6 måneder, eller endelig udelukkelse, der tidligst kan søges slettet efter et år) | Du registrerer dig selv med MitID |

Læs tabellen som lag oven på hinanden, ikke som et menukort. De tre første gør det besværligt at spille. De to sidste gør det for alvor svært. Den, der kun tager de tre første, får ofte sit tilbagefald gennem en browser eller en betalingsmåde, der var glemt.

## 1. Skærmtid: stop installationer og udvalgte hjemmesider

Skærmtid er gratis og indbygget, og du får mest ud af det, den *forhindrer*, ikke af det, den filtrerer.

**Stop nye spilapps.** Slet først de apps, du spiller i. Derefter afhænger det af din version af iOS:

- **iOS 27:** Indstillinger → Skærmtid → **Apps og websteder** → **Begrænsninger** → slå **Installering af apps** fra. Står App Store, Internet og Appmarkedspladser under kontakten, bliver alle tre sat til **Blokeret**, når du slår den fra.
- **iOS 26 og tidligere:** Indstillinger → Skærmtid → **Indhold og anonymitet** → slå til → **Appinstalleringer og køb** (på nogle versioner **Køb i iTunes og App Store**) → **Installering af apps** → **Tillad ikke**.
- **I EU på iOS 26** kan apps også hentes uden om App Store, så det er ikke nok at lukke for den. Sæt **Appmarkedspladser** og **Web** til **Tillad ikke** samme sted. [Apple skriver](https://support.apple.com/da-dk/118128), at de to stadig er tilladt efter en opdatering, selv om du allerede havde begrænsninger slået til, så se efter.

Det er den mest værdifulde indstilling på hele telefonen. Når den er slået fra, kan apps ikke hentes igen uden koden til Skærmtid.

**Blokér spilsider i Safari:**

- **iOS 27:** Skærmtid → **Apps og websteder** → **Blokeret** → **+**. Skriv adressen på hver spiludbyder, eller indsæt en hel liste. Vælg også **Begræns voksenindhold** under **Begrænsninger** → **Filtrering**: ifølge iOS blokerer det også webproxyer. Når der er sat en kode til Skærmtid, begrænser iOS desuden privat browsing.
- **iOS 26 og tidligere:** Skærmtid → Indhold og anonymitet → **App Store, Medier, Internet og Spil** → **Webindhold** → **Begræns voksenindhold**. Tryk på **Tilføj websted** under **Tillad aldrig**, og skriv adressen på hver spiludbyder. Det slår også privat browsing fra i Safari, og det er en god sidegevinst.

Vi tjekkede menuerne til iOS 27 i iOS 27.1 i Apples simulator den 25. november 2026. Apples egen [hjælpeside](https://support.apple.com/da-dk/105121) beskriver kun spærringer for installation og websteder på et barns enhed (Indstillinger → Familie → barnets navn → Apps og websteder), så en etiket kan hedde noget lidt andet hos dig.

**Haken, som ingen nævner:** iOS har ingen kategori for pengespil. Begræns voksenindhold er et filter for voksenindhold. Det rammer tilfældigvis nogle spilsider og overser de fleste bookmakere. Er det alt, du har, er intet af det, du faktisk bruger, blokeret. At tilføje sider én for én virker, men så passer du listen i hånden mod en branche med tusindvis af spejldomæner.

**Gør den her del ordentligt:** sæt en kode til Skærmtid, som du ikke kender. På iOS 27: Skærmtid → **Kode og administration** (i iOS 27.1 hedder det **Administrer skærmtid**) → **Lås indstillinger til Skærmtid**. På iOS 26 ligger Lås indstillinger til Skærmtid direkte under Skærmtid. Lad din partner, en ven eller et familiemedlem taste koden og beholde den. Bruger I gendannelse af koden, skal det være den andens Apple-konto og ikke din, for den, der ejer kontoen, kan nulstille koden.

Men regn ikke koden for en mur. Apples sider siger hver sit om at skifte den på iOS 27: [den ene](https://support.apple.com/da-dk/102677) kræver Face ID eller telefonens egen kode og Apple-kontoen til gendannelse, hvis iOS spørger, [den anden](https://support.apple.com/da-dk/guide/iphone/iph272b4c4bd/ios) kræver den nuværende kode til Skærmtid. Derfor er det lagene uden for telefonen, du skal stole mest på.

## 2. En DNS-profil for hele telefonen: den, der dækker alt

Den her springer de fleste guider over, og den er det stærkeste, der kan ligge på selve telefonen. Alle apps og browsere skal slå et domænenavn op, før de kan forbinde. Mislykkes opslaget, mislykkes appen. Du skal ikke bruge udvidelser eller indstille hver browser for sig, og det virker lige så godt på mobildata som på wi-fi.

iOS lader en app eller en konfigurationsprofil installere en indstilling for krypteret DNS (DoH), der gælder hele telefonen. Peg den mod en tjeneste, der filtrerer pengespil, og så kan hverken bookmakere, kasinoer eller sider med spilleautomater findes. Heller ikke dem uden dansk tilladelse.

Gratis og betalte muligheder, der filtrerer pengespil:

- **Mullvads åbne DoH-tjeneste**: en gratis »family«-udgave, der blokerer pengespil sammen med andre kategorier, med en offentliggjort politik om ikke at logge.
- **NextDNS**: gratis niveau, der rækker til almindeligt brug, med en blokeringsliste for pengespil, som du slår til, og et stort katalog af lister fra andre brugere.
- **Control D**: samme idé, filtrering efter kategori, findes med et gratis niveau.
- **En blokeringsapp, der installerer profilen for dig**, for eksempel [Silex](https://trysilex.com/da/), som sætter et krypteret DNS-skjold op og samler offentlige lister over spildomæner, så du aldrig skal passe en selv.

Tjek det bagefter: under Indstillinger → Generelt → **VPN og Administration af enhed** (med en DNS-profil kan der stå **VPN, DNS og Administration af enhed**) → DNS skal din konfiguration være valgt, og en kendt spilside må ikke kunne indlæses i en browser, du normalt ikke bruger.

**Begrænsningen, sagt lige ud:** du kan slå den fra i Indstillinger på under et minut. DNS-filtrering er et vejbump mod en stærk trang, ikke en mur. Det er et glimrende vejbump (de fleste tilbagefald er impulsive, og et minuts modstand er ofte nok), men gør det ikke til din sidste forsvarslinje.

## 3. Safari-blokering

En udvidelse kan få Safari til at afvise en liste af domæner. Slå den til under Indstillinger → Apps → Safari → **Udvidelser** → **Tillad udvidelse**. Silex har en, og det har de fleste andre apps, der er lavet til at blokere.

Nyttig, men smal: den dækker Safari og intet andet. Chrome, Firefox, Edge, browseren inde i en social app og spiludbyderens egen app mærker den ikke. Se en Safari-blokering som et supplement til DNS-filteret, aldrig som en erstatning.

## 4. Gør pengene svære at flytte

At lukke vejen til spillet er kun det halve. Den anden halvdel er at gøre pengene svære at flytte. Her er Danmark anderledes end for eksempel Storbritannien: næsten ingen danske banker beskriver en spilspærring, du selv kan slå til. Den eneste, vi har fået bekræftet på dansk, er Revolut. Den gælder kortbetalinger, og det tager op til 48 timer at slå den fra. Har du en anden bank, så spørg, og brug de råd, Center for Ludomani giver om at begrænse din adgang til penge.

Det er ventetiden, der er pointen: spærringen skal leve længere end trangen. [Sådan gør du.](https://trysilex.com/da/spaerre-pengespil-banken/)

## 5. Udeluk dig selv ved kilden

Det stærkeste lag ligger slet ikke på telefonen. Selvudelukkelse betyder, at spiludbyderne skal afvise dig i en periode. I Danmark klarer du det med én registrering i **[ROFUS](https://rofus.nu/)**, som Spillemyndigheden driver. Du logger på med MitID, og udelukkelsen gælder onlinespil hos alle spiludbydere med dansk tilladelse, alle fysiske kasinoer og væddemål i butikker.

Du kan ikke fortryde den undervejs. Det er netop derfor, den virker. [Hele guiden til ROFUS er her.](https://trysilex.com/da/udeluk-dig-fra-spil/)

## Det, der ikke virker

- **Kun at slette apps.** Det tager femten sekunder at hente dem igen, og mobilsiden virker fint helt uden en app.
- **Kun en spærring i routeren.** Et filter på wi-fi derhjemme, også en Pi-hole eller ændret DNS i routeren, er væk i samme øjeblik, telefonen skifter til mobildata. Gør det gerne også, men aldrig i stedet.
- **En almindelig VPN.** Den flytter din trafik, den filtrerer den ikke. Nogle VPN-tjenester har en DNS-tilstand, der filtrerer indhold, og den virker. En helt almindelig VPN gør ikke noget for dig her.
- **En app, der kun tæller dage.** At tælle er motivation, ikke en barriere. Du har brug for begge dele, og barrieren skal op først.
- **Alt, der lover, at det ikke kan fjernes på iOS.** Det tillader systemet ikke. Den slags løfter er reklame, og den, der tror på dem, ender med ét lag i stedet for fire.

## Den halve time, i rækkefølge

1. Slet alle apps til pengespil. Log ud af de spilkonti, der stadig er åbne i browseren.
2. Slå en filtrerende DNS-profil til, og tjek, at en spilside ikke kan indlæses.
3. Slå Installering af apps fra i Skærmtid, og Appmarkedspladser og Web med, hvis din iPhone har dem. Blokér de sider, du faktisk har brugt. Lad en anden sætte koden.
4. Slå en Safari-blokering til.
5. Spørg banken om en spilspærring, og gør pengene sværere at nå.
6. Registrér dig i ROFUS. Har du konti hos spiludbydere uden dansk tilladelse, så bed dem hver for sig om permanent udelukkelse.

Trin 5 og 6 er dem, man udskyder, og det er dem, der holder. Begynd med dem, hvis du kun har ti minutter.

## Spærringer er gulvet, ikke planen

Hvert lag ovenfor køber dig tid i de halvfems sekunder, hvor en trang er på sit højeste. Det, du gør med den tid, afgør, om det også virker næste gang. [En trang stiger, topper og falder i en ret forudsigelig kurve](https://trysilex.com/da/hvor-laenge-varer-spilletrang/), og at vente den ud er noget, man bliver bedre til af at øve sig. Det er det, [den 90 dage lange del af det her](https://trysilex.com/da/stop-med-at-spille/) er til for.

## Stop med at spille. Behold pengene.

Silex blokerer pengespil på hele din telefon og følger dig gennem 90 dage, én ad gangen.

[Hent Silex til iPhone](https://apps.apple.com/app/id6798826038?mt=8) [Hent Silex til Android](https://play.google.com/store/apps/details?id=com.klozovyi.stopgamble&referrer=utm_source%3Dtrysilex%26utm_campaign%3Dda_iphone_guide)

## Ofte stillede spørgsmål

### Kan jeg blokere pengespil på iPhone uden en app?

Ja. Skærmtid kan begrænse installation af apps og bestemte hjemmesider, og iOS kan bruge en DNS-konfiguration, så spildomæner ikke kan findes i nogen app. Begge dele er gratis og indbygget. Det, iOS ikke selv kan, er at holde en liste over hundredtusindvis af spildomæner opdateret. Det er det, en blokeringsapp eller en filtrerende DNS-tjeneste lægger til.

### Blokerer Skærmtid spilapps?

Delvist. Skærmtid kan begrænse installation af nye apps, skjule apps, du har, og blokere bestemte hjemmesider i Safari. Men der er ingen kategori for pengespil, så Begræns voksenindhold er ikke et spilfilter. Du skal selv tilføje domænerne eller bruge en filtrerende DNS-tjeneste, der passer listen for dig.

### Kan spilapps blokeres for altid på iPhone?

Nej, og apps, der påstår det, lover for meget. På iOS kan du altid fjerne en profil eller slette en app. Det, der skal holde, må komme udefra: ROFUS, som hverken kan annulleres eller forkortes, og en spærring på pengene, der tager tid at slå fra. Det er nok til, at trangen når at gå over.

### Blokerer en VPN spilsider?

En almindelig VPN gør ikke. Den ændrer, hvor din trafik kommer ud på nettet, ikke hvad den kan nå. Det, du har brug for, er en filtrerende DNS-tjeneste eller en blokering, der bygger på DNS. Nogle VPN-tjenester har en DNS-tilstand, der filtrerer indhold, og den virker.

### Virker blokeringen også på mobildata?

En DNS-konfiguration, der er installeret på telefonen, gør, for den hører til telefonen. En spærring i routeren gør ikke. Den slutter ved hoveddøren, og telefonen er tilbage på spilsiderne, så snart den skifter til 5G. Det er den mest almindelige grund til, at spærringer derhjemme ikke holder.

## Hvis du har brug for at tale med nogen nu

- Danmark: [70 22 28 25](tel:70222825) — StopSpillet: gratis og fortroligt, man–tor 9–21, fre 9–17 (lukket i weekenden)
- Danmark: [70 201 201](tel:70201201) — Livslinien: hver dag kl. 9–5, anonymt, almindelig telefontakst
- Nødsituation: [112](tel:112) — Akut livsfare
- Andre lande: [findahelpline.com](https://findahelpline.com) — Krisetelefoner, hvor du er
