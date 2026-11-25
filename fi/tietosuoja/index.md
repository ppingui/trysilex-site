> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/fi/tietosuoja/

# Tietosuojakäytäntö

Tämä on käännös. Jos se eroaa [englanninkielisestä versiosta](https://trysilex.com/privacy/), sovelletaan englanninkielistä versiota.

Päivitetty viimeksi 25. marraskuuta 2026. Selosteen varsinainen versio julkaistaan tällä sivustolla; se korvaa Notionissa olleen kopion, johon sovelluksen vanhemmat versiot linkittävät.

Silex on rakennettu yhden periaatteen varaan: **toipumisesi ei ole kenenkään tietoaineisto.**

*Me* emme tallenna sinusta mitään millekään palvelimelle, meillä ei ole käyttäjätilejä eikä meillä ole mitään keinoa lukea, mitä kirjoitat tässä sovelluksessa. (Ainoa palvelimilla ajamamme koodi on kaksi vapaaehtoista työkalua, joilla ei ole tekemistä sovelluksen kanssa: kohdan 14 Notion-liitin ja kohdan 15 Silex Help. Kumpikaan ei säilytä mitään.) Kahdella ulkopuolisella taholla on kuitenkin palvelimia, jotka saavat jotain: analytiikkapalvelulle lähetetään niiden näkymien *nimet*, joihin pääset, ja mainosten mittauspalvelulle kerrotaan, että sovellus asennettiin ja seurasiko siitä kokeilujakso tai osto. Yksi kytkin Asetuksissa lopettaa molemmat. Tällä sivulla kerrotaan tarkasti, mitä tämä tarkoittaa, myös ne harvat kohdat, joissa tietoa lähtee puhelimestasi. Tietosuojakäytäntö, joka luettelee vain rauhoittavat asiat, ei ole tietosuojakäytäntö.

Tämä seloste on kirjoitettu täyttämään EU:n yleisen tietosuoja-asetuksen (GDPR) ja Yhdistyneen kuningaskunnan tietosuoja-asetuksen (UK GDPR) vaatimukset. Jos olet ETA-alueella tai Yhdistyneessä kuningaskunnassa, oikeusperusteita, siirtoja ja oikeuksiasi koskevat kohdat koskevat sinua kokonaisuudessaan.

## 1. Se, minkä kirjaat, pysyy laitteellasi

Kaikki, minkä kirjaat (kyselyvastaukset, päivittäiset kirjaukset, päiväkirjan pohdinnat, ohjelman vastaukset, himolokin merkinnät, lipsahdusmerkinnät, jaksojen päivämäärät, rahasummat, allekirjoituksesi ja kehräkokoelmasi), tallentuu kahteen paikkaan, jotka molemmat kuuluvat sinulle:

- **iPhoneesi**, sovelluksen paikalliseen tietokantaan.
- **Yksityiseen iCloudiisi**, Applen CloudKitin yksityiseen tietokantaan, jotta historiasi säilyy, vaikka laite katoaisi tai vaihtuisi.

Yksityiseen iCloud-tietokantaasi pääsee vain sinun Apple ID:lläsi. Me emme ole siinä osapuolena emmekä voi lukea sitä. Jos iCloud ei ole saatavilla tai se on pois käytöstä, sovellus tallentaa tiedot vain laitteellesi.

**Me emme koskaan saa tätä sisältöä.** Mikään rajapintakutsu ei lähetä sitä, meillä ei ole siitä varmuuskopiota eikä avainta, jolla voisimme purkaa sen salauksen. Koska emme pääse sisältöön emmekä voi käyttää sitä, emme katso olevamme sen rekisterinpitäjä, mitä kirjoitat sovellukseen. Rekisterinpitäjä olet sinä. Kerromme siitä tässä avoimuuden vuoksi, emme siksi, että käsittelisimme sitä.

## 2. Mitä muille todella välittyy

Kuusi rajattua tapausta, jotka kaikki ovat vapaaehtoisia tai teknisesti väistämättömiä.

### Ostot: Apple ja RevenueCat

Apple käsittelee tilaukset. Käytämme RevenueCatia tilauksen tilan tarkistamiseen ja hallintaan. Se toimii henkilötietojen käsittelijänämme ja saa:

- laitteen tyypin ja käyttöjärjestelmän,
- viimeisimmän käyttöajan ja Applen kuittitiedostot,
- mahdollisesti käyttäjätunnisteen ja tietoa siitä, mistä asennus on peräisin (attribuutiometatiedot).

Kun ”Jaa anonyymit käyttötiedot” on päällä, RevenueCat välittää lisäksi AppsFlyerille tiedon kokeilujaksosta tai ostosta ja sen hinnan, jotta se voidaan laskea mainoskampanjan ansioksi. Katso *Mainosten mittaus* alempana.

RevenueCat ei koskaan saa päiväkirjaasi, vastauksiasi, jaksoasi eikä mitään toipumiseesi liittyvää sisältöä. Katso [Applen tietosuojakäytäntö](https://www.apple.com/legal/privacy/) ja [RevenueCatin tietosuojakäytäntö](https://www.revenuecat.com/privacy/).

### DNS-kilpi, vain jos otat sen käyttöön

Kilpi asentaa salatun DNS-määrityksen (DoH), jonka ansiosta rahapelidomainit eivät avaudu sovelluksissasi eivätkä selaimissasi. Kun kilpi on päällä, laitteesi DNS-kyselyihin vastaa [Mullvadin julkinen DNS-palvelin](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls), joka noudattaa Mullvadin [lokittomuuskäytäntöä](https://mullvad.net/en/help/no-logging-data-policy/). Edistyneet käyttäjät voivat ohjata kyselyt sen sijaan omaan NextDNS-määritykseensä. Mullvad ja NextDNS toimivat näiden kyselyiden osalta itsenäisinä rekisterinpitäjinä omien käytäntöjensä mukaan. Me emme ole siinä välissä emmekä koskaan näe selaamistasi. Kun kytket kilven pois iOS:n asetuksissa, tämä loppuu heti.

### Estolistojen päivitykset

Sovellus lataa aika ajoin julkisia rahapelidomainien listoja jsDelivristä ja GitHubista. Kuten minkä tahansa tiedoston latauksessa, nuo palvelimet näkevät pyynnön ja IP-osoitteesi. Pyynnössä ei ole tunnistetta eikä mitään sinusta tai toipumisestasi.

### Käyttömäärät: laskuri laitteellasi

Sovellus pitää omaa laskuria siitä, *miten sovellusta käytetään* (esimerkiksi montako kertaa jokin näkymä avattiin tiettynä päivänä). Luvut tallentuvat päivittäin yhteen tiedostoon sovelluksen omaan tallennustilaan. Siinä ei ole tunnisteita eikä mitään kirjoittamaasi, ja **tuo tiedosto ei koskaan lähde puhelimestasi**. Sovelluksen poistaminen poistaa sen. Samojen tapahtumien *nimet* lähetetään erikseen TelemetryDeckille, ellet kytke sitä pois. Siitä kertoo seuraava kohta, ja siksi tässä kohdassa ei rehellisyyden nimissä enää lue ”ei välity kenellekään”.

### Käyttöanalytiikka: TelemetryDeck, ellet kytke sitä pois

Haluamme nähdä, missä kohtaa ihmiset jättävät käyttöönoton kesken. Silloin näkymän voi korjata arvailematta. Siksi sovellus lähettää niiden vaiheiden *nimet*, joihin se pääsee, yritykselle **TelemetryDeck GmbH**, Von-der-Tann-Str. 54, 86159 Augsburg, Saksa. Lähetettävät tiedot ovat:

- jokaisen saavutetun käyttöönoton vaiheen **nimi** ja sen paikka järjestyksessä (`funnel.question_04`, `funnel.paywall`), kukin enintään kerran asennusta kohti;
- muiden sovelluksen tapahtumien **nimet**, kuten ohjelmapäivä suoritettu tai hätäpainike avattu, eikä niistä muuta kuin nimi;
- TelemetryDeckin omat vakiotiedot: käyttöjärjestelmän versio, laitemalli, kieliasetus, alue, sovelluksen versio ja vastaavat;
- satunnainen tunniste, jonka sovellus luo tälle asennukselle.

Laskemme näistä tapahtumien nimistä myös muutaman kokonaismäärän, jotka sovellus näyttää käyttöönoton aikana, esimerkiksi montako ohjelmapäivää ihmiset ovat suorittaneet. Kokonaismäärä ei kerro mitään kenestäkään yksittäisestä ihmisestä.

Koskaan ei lähetetä kyselyvastauksiasi, PGSI-pisteitäsi, viikoittaista rahankäyttöäsi, päiväkirjasi tekstiä tai lipsahdusmerkintöjäsi, eikä mitään muutakaan, minkä olet kirjoittanut tai valinnut. Signaali kertoo, että näkymään päästiin. Se ei koskaan kerro, mitä näkymässä oli tai mitä siihen kirjoitit.

**Tuosta tunnisteesta.** Se on satunnainen UUID, jonka sovellus luo, kun avaat sen ensimmäisen kerran. Se *ei* tarkoituksella ole `identifierForVendor`, jota iOS olisi muuten käyttänyt, koska se säilyy sovelluksen poiston ja uudelleenasennuksen yli ja on yhteinen kaikille saman kehittäjän sovelluksille. Meidän tunnisteemme ei ole yhteinen minkään kanssa, ja se häviää, kun poistat sovelluksen. Ennen kuin se lähtee puhelimestasi, siitä lasketaan laitteella suolattu tiiviste (hash). Perillä TelemetryDeck lisää oman suolansa ja laskee tiivisteen uudelleen, joten emme me eivätkä he pysty päättelemään tallennetusta arvosta alkuperäistä. Yksi tiivistys olisi pelkkää pseudonymisointia, ja siksi he tekevät toisen.

Kytkemme lisäksi pois kaksi asiaa, jotka TelemetryDeck muuten keräisi: istunnon alkamisesta kertovan signaalin ja istuntotilastot.

**Kytkin.** Asetukset → Tietosi → **Jaa anonyymit käyttötiedot**. Se on **oletuksena päällä**, emmekä kaunistele syytä: jos mittaus vaatisi erillisen suostumuksen, se mittaisi väärää joukkoa. Juuri ne, jotka lopettavat ensimmäiseen näkymään, eivät koskaan pääse suostumuskysymykseen asti, joten mitattava poistuma itse vääristäisi otosta. Oletuksen hinta on se, että kerromme suoraan, mitä lähetetään, ja sitä varten tämä kohta on. Kun kytket sen pois, uusia signaaleja ei enää lähde, lähetyskanava poistuu sovelluksesta ja levyllä odottavat lähettämättömät signaalit poistetaan. Jo lähtenyttä ei voi vetää takaisin, eikä mikään siinä johda sinuun.

Katso [TelemetryDeckin tietosuojakäytäntö](https://telemetrydeck.com/privacy/).

### Mainosten mittaus: AppsFlyer, saman kytkimen takana

Mainostamme Silexiä, ja mainoksesta kannattaa maksaa vain, jos sen kautta asentaneet ihmiset myös käyttävät sovellusta. Tämän laskemiseksi sovelluksessa on **AppsFlyer Ltd.** -yrityksen (14 Maskit St., Herzliya, Israel) SDK. Se saa:

- tiedon siitä, että sovellus asennettiin ja avattiin, ja milloin;
- tunnisteen, jonka AppsFlyerin SDK luo tälle sovelluksen asennukselle;
- AppsFlyerin vakiolaitetiedot: laitemalli, käyttöjärjestelmän versio, kieli, sovelluksen versio ja verkkotiedot (Wi-Fi tai operaattori). Kuten mikä tahansa palvelin, se näkee IP-osoitteesi, josta AppsFlyer kertoo voivansa päätellä karkean alueen;
- kolmen tapahtuman **nimet** eikä niistä muuta: että tilausvaihtoehdot näytettiin, että ilmainen kokeilujakso alkoi ja että ostos tehtiin;
- RevenueCatilta tiedon kokeilujaksosta tai ostosta ja sen hinnan, liitettynä samaan asennustunnisteeseen.

Näin asennus yhdistetään mainokseen: Applen omilla koostetuilla raporteilla (SKAdNetwork ja AdAttributionKit), joissa nimetään *kampanja* eikä koskaan ihmistä. Apple lähettää ne mainosverkostolle, ja iOS lähettää niistä kopion AppsFlyerille. Poikkeuksia on yksi, ja se alkoi 22. marraskuuta 2026: katso ”Metan mainokset” alempana.

Itse App Storen mainokset toimivat hieman eri tavalla. Niitä varten iOS antaa sovellukselle kertakäyttöisen tunnuksen (Applen AdServices), jonka AppsFlyer ja RevenueCat kumpikin vaihtavat Applella tietoon siitä, mikä kampanja ja hakusana johti tähän asennukseen. Tunnus yksilöi mainoksen napautuksen, ei sinua.

Yhtä ei ole mukana lainkaan, ja se on rakennettu sovellukseen eikä vain luvattu: **mainostunnistetta.** Sovellus ei koskaan näytä seurantaluvan kyselyä. Siinä on AppsFlyerin SDK:n versio, josta mainostunnisteen koodi on poistettu, ja se kytkee pois `identifierForVendor`-tunnisteen keräämisen. Se on ainoa tunniste, joka on yhteinen saman kehittäjän sovelluksille. Mitään kirjoittamaasi tai valitsemaasi ei lähetetä: sama luettelo kuin edellä.

**Yksi asia on toisin kuin analytiikan tunnisteessa, ja sanomme sen mieluummin ääneen.** AppsFlyerin tunnisteesta ei lasketa tiivistettä puhelimessasi niin kuin TelemetryDeckin tunnisteesta, ja AppsFlyerin SDK säilyttää iPhonen avainnipussa pientä merkintää, jonka avulla se erottaa uudelleenasennuksen uudesta asennuksesta. Avainnipun merkinnät voivat säilyä sovelluksen poistamisen jälkeenkin. Siksi AppsFlyerin kohdalla emme väitä, toisin kuin TelemetryDeckin kohdalla, että uudelleenasennus näyttää tuntemattomalta.

**Kytkin** on sama: Asetukset → Tietosi → **Jaa anonyymit käyttötiedot**, pois. Se lopettaa SDK:n pyynnöt, poistaa AppsFlyerin tunnisteen RevenueCatista, jotta yhtään ostotapahtumaa ei enää välitetä eteenpäin, ja poistaa levyllä odottavat pyynnöt. AppsFlyerilla on lisäksi oma kieltolomake osoitteessa [appsflyer.com/legal/opt-out](https://www.appsflyer.com/legal/opt-out/). Katso [AppsFlyerin palvelujen tietosuojakäytäntö](https://www.appsflyer.com/legal/services-privacy-policy/).

### Metan mainokset, 22. marraskuuta 2026 alkaen

Aloitamme mainostamisen Facebookissa ja Instagramissa. Metan iPhone-sovellusten asennuskampanjat laskevat asennukset vain Metan omalla menetelmällä (sen nimi on Aggregated Event Measurement), ja menetelmä tarvitsee tietoja sovelluksesta. Meille ei tarjottu mahdollisuutta laskea pelkillä Applen koostetuilla raporteilla. Siksi AppsFlyer välittää 22. marraskuuta 2026 alkaen osan saamistaan tiedoista Metalle (**Meta Platforms Ireland Ltd.** Euroopassa oleville, **Meta Platforms, Inc.** muualla):

- että sovellus asennettiin, ja jokaisen avaamiskerran: jokaisesta asennuksesta, jossa tämä kytkin on päällä, riippumatta siitä, oliko mainoksella siihen mitään tekemistä;
- asennuksista, jotka AppsFlyer katsoo jonkin Meta-mainoksemme ansioksi, edellä luetellut kolme tapahtuman nimeä;
- näiden mukana aina AppsFlyerin tunnisteen asennukselle, IP-osoitteen, josta pyyntö tuli, sekä laitemallin ja iOS-version.

Edelleenkään ei lähetetä nimeä, sähköpostiosoitetta, mainostunnistetta, `identifierForVendor`-tunnistetta eikä mitään, minkä olet kirjoittanut tai valinnut sovelluksessa.

**Mitä tämä muuttaa, suoraan sanottuna.** Ennen tätä päivää yhdestäkään yksittäisestä asennuksesta ei päätynyt mitään mainosyhtiölle. Nyt Meta saa yhden tietueen asennusta kohti. Ehtojensa mukaan se voi yhdistää tällaisen tietueen ihmiseen, joka käyttää Facebookia tai Instagramia, käyttää sitä mainostemme mittaamiseen ja sen päättämiseen, kenelle mainoksia näytetään, ja säilyttää sen enintään kaksi vuotta. Tietue kertoo, että laitteelle asennettiin sovellus ihmisille, jotka haluavat lopettaa rahapelaamisen. Se on sellainen tieto, jota kohdassa 3 käsitellään varoen. Tietoa jaetaan vain niin kauan kuin mainostamme Metassa: jos lopetamme tai jos Meta antaa Silexin kampanjan laskea asennukset pelkillä Applen koostetuilla raporteilla, kytkemme jakamisen pois ja merkitsemme päivämäärän tähän. Se, minkä Meta on siihen mennessä saanut, on Metan ehtojen alaista; emme voi vetää sitä takaisin.

**Kytkin kattaa myös tämän.** Asetukset → Tietosi → **Jaa anonyymit käyttötiedot**, pois: AppsFlyer ei saa puhelimestasi enää mitään, joten sillä ei ole mitään välitettävää. Jos haluat kysyä Metalta siitä, mitä sillä jo on, käytä Facebook- tai Instagram-tilisi työkaluja tai katso [Metan tietosuojakäytäntö](https://www.facebook.com/privacy/policy/).

App Storen omin termein sovellus ilmoittaa: **ei seurantaa** (`NSPrivacyTracking` false, ei seurantadomaineja). Kerättäviä tietotyyppejä se ilmoittaa kolme: tuotteen käyttö (Product Interaction), laitetunniste (Device ID) ja ostohistoria (Purchase History). Kaikki on merkitty tiedoiksi, *joita ei liitetä henkilöllisyyteesi* ja *joita ei käytetä seurantaan*. Niiden käyttötarkoitukset ovat analytiikka ja oman mainontamme mittaaminen (ostohistorian osalta myös tilauksen toimittaminen).

**Ei mitään muuta.** Nämä viisi verkkoyhteyttä ovat sovelluksen ainoat. Mainostunnisteita ei ole, emmekä tee profilointia tai automaattista päätöksentekoa, jolla olisi oikeudellisia tai vastaavalla tavalla merkittäviä vaikutuksia. Niin kauan kuin edellä kuvattu tietojen jakaminen Metalle on päällä, se on ainoa kohta, jossa tieto asennuksestasi voidaan yhdistää siihen, mitä toinen yritys sinusta jo tietää. Edellisen kappaleen ilmoitus kirjoitettiin ennen sen alkamista. Selvitämme, pitääkö ilmoitusta muuttaa, ja kerromme mahdollisesta muutoksesta kohdassa 11.

### Lause muille, vain jos lähetät sellaisen

Kun olet suorittanut ohjelman päivän 7, sovellus voi kysyä kerran, haluaisitko jakaa lauseen jollekulle, joka on vasta aloittamassa. Jos haluat, omaan sähköpostisovellukseesi avautuu meille osoitettu viesti, jossa on sanasi, etunimesi alkukirjain, päiviesi määrä ja suostumuksesi. Voit muuttaa tai poistaa mitä tahansa siitä ennen lähettämistä, eikä mitään lähde laitteeltasi, ellet paina lähetä.

Saamme silloin tuon sähköpostin ja osoitteesi Googlen ylläpitämään postilaatikkoon. Voimme näyttää sanasi, etunimesi alkukirjaimen ja päiviesi määrän sovelluksessa ja sovelluskauppojen sivuillamme. Emme koskaan julkaise sähköpostiosoitettasi. Kirjoita meille milloin tahansa, niin lakkaamme käyttämästä sanojasi: ne poistuvat kauppasivuilta ja sovelluksen seuraavasta versiosta, ja poistamme sähköpostin, ellei meidän ole pakko säilyttää sitä osoittaaksemme, mihin suostuit.

## 3. Oikeusperusteet (GDPR:n 6 ja 9 artikla)

| Mitä | Tarkoitus | Oikeusperuste |
|---|---|---|
| Oston ja tilauksen tila (Applen / RevenueCatin kautta) | Ostamasi tilauksen toimittaminen ja palauttaminen; vilpillisesti hankitun käyttöoikeuden estäminen | **6 artiklan 1 kohdan b alakohta**: kanssasi tehdyn sopimuksen täytäntöönpano |
| IP-osoite, jonka estolistan jakeluverkko (CDN) näkee, kun sovellus lataa listan | Sen esto-ominaisuuden toimittaminen, jota varten sovellus on olemassa | **6 artiklan 1 kohdan f alakohta**: oikeutettu etu (suojalistojen pitäminen ajan tasalla). Arviomme: mahdollisimman vähän tietoa, ei profilointia, ei yhteyttä sinuun |
| Tapahtumien nimet, asennuskohtainen tiivistetty tunniste ja TelemetryDeckin vakiolaitetiedot, kun ”Jaa anonyymit käyttötiedot” on päällä | Sen näkeminen, missä kohtaa ihmiset jättävät käyttöönoton kesken, jotta ne näkymät voidaan korjata, ja edellä kuvattujen kokonaismäärien näyttäminen | **6 artiklan 1 kohdan f alakohta**: oikeutettu etu (sovelluksen toimivuus niille, joille se on tarkoitettu). Arviomme: ei sisältöä, ei mainostunnistetta, tunniste, joka ei voi seurata sinua sovelluksesta toiseen eikä säily sovelluksen poistamisen yli, ja Asetuksissa kytkin, joka lopettaa tämän. Juuri kytkin kantaa tasapainotestin: etu, josta voit kieltäytyä yhdellä napautuksella, ei ole etu, joka ajaa sinun etusi yli |
| AppsFlyerin asennustunniste, AppsFlyerin vakiolaitetiedot, kolme tapahtuman nimeä sekä kokeilujakso- ja ostotapahtumat, kun ”Jaa anonyymit käyttötiedot” on päällä | Sen tietäminen, mitkä mainoksistamme johtavat siihen, että ihmiset oikeasti käyttävät sovellusta, jotta lakkaamme maksamasta muista | **6 artiklan 1 kohdan f alakohta**: oikeutettu etu (toipumissovelluksen mainostaminen hukkaamatta sitä rahaa, jolla se rahoitetaan). Arviomme: ei mainostunnistetta, ei sisältöä, yhdistäminen mainoksiin vain Applen koostettujen kampanjaraporttien kautta (lukuun ottamatta seuraavalla rivillä kuvattua tietojen jakamista Metalle) ja sama kytkin Asetuksissa, joka lopettaa tämän |
| 22. marraskuuta 2026 alkaen, niin kauan kuin mainostamme Metassa: asennus- ja avaustiedot, jotka AppsFlyer välittää Metalle, sekä AppsFlyerin asennustunniste, IP-osoite, laitemalli ja iOS-versio (kohta 2, ”Metan mainokset”) | Se, että Meta voi laskea mainostensa tuomat asennukset, mitä sen iPhone-asennuskampanjat edellyttävät | **6 artiklan 1 kohdan f alakohta**: oikeutettu etu, ja tässä taulukossa tuon perusteen heikoin käyttö: tieto menee yritykselle, joka voi yhdistää sen tiliin. Arviomme nojaa siihen, ettei tiedossa ole mitään kirjaamaasi, että sitä jaetaan vain niin kauan kuin mainostamme Metassa ja että sama kytkin lopettaa sen |
| DNS-kyselyt, kun kilpi on käytössä | Rahapelidomainien estäminen koko laitteessa | **6 artiklan 1 kohdan a alakohta**: suostumuksesi, jonka annat ottamalla kilven käyttöön ja hyväksymällä iOS:n kysymyksen; voit peruuttaa sen milloin tahansa kytkemällä kilven pois |
| Lause, jonka päätät lähettää meille sähköpostilla julkaistavaksi | Vasta aloittaville näyttäminen, että muutkin ovat olleet tässä | **6 artiklan 1 kohdan a alakohta ja 9 artiklan 2 kohdan a alakohta**: nimenomainen suostumuksesi, jonka annat kytkemällä hyväksynnän päälle ja lähettämällä sähköpostin; voit peruuttaa sen milloin tahansa |
| Se, mitä kirjoitat sovellukseen | Toipumisohjelman toimittaminen sinulle omalla laitteellasi | Emme saa sitä, joten emme tee käsittelyä, jota pitäisi perustella. Siltä osin kuin sitä ylipäätään käsitellään, se tapahtuu laitteellasi ja sinun hallinnassasi |

**Erityisiin henkilötietoryhmiin kuuluvat tiedot (terveystiedot).** Se, mitä kirjaat tähän sovellukseen, paljastaa tietoja terveydestäsi ja mahdollisesta toiminnallisesta riippuvuudesta. Ne ovat **9 artiklan** mukaisia erityisiin henkilötietoryhmiin kuuluvia tietoja. Juuri siksi sovellus on suunniteltu niin kuin se on: nuo tiedot eivät koskaan päädy meille, joten emme koskaan nojaa niiden osalta 9 artiklan edellytykseen. Ainoa poikkeus on lause, jonka päätät lähettää meille sähköpostilla julkaistavaksi: se voi paljastaa saman asian, joten sen osalta nojaamme nimenomaiseen suostumukseesi 9 artiklan 2 kohdan a alakohdan nojalla.

Vaikeampi kysymys on analytiikka, ja käymme sen mieluummin läpi kuin sivuutamme sen. Signaalissa `funnel.question_04` ei ole sisältöä. Silex on kuitenkin sovellus rahapelaamisesta toipumiseen, ja unionin tuomioistuin on katsonut, että myös tieto, joka paljastaa erityisen henkilötietoryhmän vain *välillisesti*, kuuluu säännön piiriin (asia C-184/20, *OT*). Emme siis väitä, että nämä signaalit olisivat aiheeltaan viattomia: ”tämä asennus tuli Silexin käyttöönottoon” kertoo puhelinta pitelevästä ihmisestä jotain, mikä on lähellä terveyttä. Nojaamme 9 artiklan toiseen puoleen, joka koskee tietoja **tunnistetusta tai tunnistettavissa olevasta** luonnollisesta henkilöstä. Näihin signaaleihin liitetty tunniste on satunnainen, luotu yhdelle asennukselle, suolattu ja tiivistetty laitteellasi, ja perillä siihen lisätään vielä TelemetryDeckin oma suola ja siitä lasketaan uusi tiiviste. Kukaan osapuoli, emme mekään, pysty siis pääsemään siitä takaisin ihmiseen tai yhdistämään sitä mihinkään muuhun. Tällä perusteella katsomme, että TelemetryDeckille päätyvä tieto jää 9 artiklan ulkopuolelle. Käsittelemme sitä silti 6 artiklan mukaisena pseudonyymina henkilötietona, jolla on oikeusperuste ja toimiva kieltomahdollisuus, koska näistä kahdesta tulkinnasta kannattaa olla väärässä varovaisemman puolella. Tilauskuitin osalta mikään ei muutu: se ei paljasta terveydentilaa sen enempää kuin että ostit sovelluksen.

AppsFlyerille päätyvä tieto kestää tuon arvion heikommin, ja kohtelemme sitä sen mukaisesti. Sen tunniste on satunnainen ja koskee vain tätä sovellusta, mutta siitä ei lasketa tiivistettä kahdesti, ja se saapuu yhdessä laitemallin, IP-osoitteen ja ostotapahtumien kanssa. Käsittelemme sitä pseudonyymina henkilötietona, joka on henkilötietojen käsittelijän hallussa tietojenkäsittelyliitteen nojalla (kohta 4), taulukon mukaisella 6 artiklan oikeusperusteella ja samalla kieltomahdollisuudella. Se sanoo: ”tämä asennus tuli Silexiin ja aloitti kokeilujakson”. Se ei kerro, kuka olet, eikä siinä ole mitään sovellukseen kirjaamaasi.

Tämä on selosteen ainoa kappale, jossa pätevät juristit voivat perustellusti päätyä eri tuloksiin, ja sanomme sen mieluummin kuin annamme sen näyttää ratkaistulta.

## 4. Kansainväliset siirrot

**RevenueCat** on yhdysvaltalainen yritys (Brandon, Florida), joka säilyttää tietoja Amazon Web Services -palvelussa Yhdysvalloissa. Siirrot katetaan sen tietojenkäsittelysopimuksella, johon sisältyvät Euroopan komission **vakiosopimuslausekkeet** (täytäntöönpanopäätös (EU) 2021/914), **moduuli kaksi: rekisterinpitäjältä henkilötietojen käsittelijälle**. Yhdistyneen kuningaskunnan osalta sovelletaan lisäksi ICO:n liitettä **International Data Transfer Addendum**, joka on päivätty 21. maaliskuuta 2022, ja Sveitsin osalta Sveitsin tietosuojalakiin (FADP) sovitettuja vakiosopimuslausekkeita. RevenueCat **ei** ole sertifioitu EU:n ja Yhdysvaltojen tietosuojakehyksen (EU–US Data Privacy Framework) mukaisesti; siirto perustuu vakiosopimuslausekkeisiin. *Tarkistettu RevenueCatin julkaisemasta tietojenkäsittelysopimuksesta 6. elokuuta 2026.*

**TelemetryDeck** on saksalainen yritys (TelemetryDeck GmbH, Augsburg). Se ilmoittaa, että käyttötiedot säilytetään **yksinomaan Euroopan unionissa** Hetznerin palvelimilla Nürnbergissä. Osa käsittelyketjusta toimii vielä Azuressa Amsterdamissa ja AWS:ssä Frankfurtissa, ja yrityksen ilmoitettu suunnitelma on siirtää kaikki Hetznerille vuoden 2026 aikana. Sen yritystason tietosuojakäytäntö nimeää näiksi vastapuoliksi Hetzner Online GmbH:n (Saksa), Microsoft Ireland Operations Ltd:n (Irlanti) ja Amazon Web Services, Inc:n (Seattle, Yhdysvallat). AWS-yhtiö on amerikkalainen, mutta alue, jolla se säilyttää tiedot, on Frankfurt. TelemetryDeckin oman ilmoituksen mukaan mikään meidän analytiikkatietomme ei siis poistu ETA-alueelta, eikä **V luvun siirtomekanismia tarvita**, koska siirtoa kolmanteen maahan ei ole. Emme ole itsenäisesti varmistaneet noita säilytysalueita emmekä pysty siihen; kerromme, mitä TelemetryDeck julkaisee.

Yhtä asiaa emme voi antaa sinulle, ja siksi tämä kohta on pidempi kuin RevenueCatin. **TelemetryDeck ei tarjoa 28 artiklan mukaista käsittelysopimusta.** Sen tietojenkäsittelyehdot ovat automaattisesti osa sen käyttöehtoja, joten mitään allekirjoitettavaa ei ole. Niissä kuitenkin todetaan, että se ei toimi ”GDPR:n 4 artiklan 8 kohdassa tarkoitettuna henkilötietojen käsittelijänä eikä yhteisrekisterinpitäjänä” ja ettei 26 ja 28 artiklaa sovelleta, sillä perusteella, että sen saamat tiedot ovat anonyymejä eivätkä henkilötietoja. Emme ole omaksuneet tätä kantaa: käsittelemme tiivistettyä asennustunnistetta pseudonyymina henkilötietona, annamme sille joka tapauksessa 6 artiklan oikeusperusteen ja kieltomahdollisuuden (kohta 3) ja kuvaamme TelemetryDeckin tosiasialliseksi henkilötietojen käsittelijäksi, koska sitä se tekee. Sinun on hyvä tietää seuraus: 28 artiklan mukaisen sopimuksen antamat takeet (dokumentoidut ohjeet, auditointioikeudet, sopimukseen perustuva poistamisvelvollisuus) eivät ole meidän saatavillamme tältä toimittajalta, koska se torjuu roolin, josta ne syntyvät. *Tarkistettu TelemetryDeckin julkaisemista tietosuojakäytännöstä, tietojenkäsittelysopimuksesta sekä arkkitehtuuri- ja tietoturvasivuista 17. elokuuta 2026.*

**AppsFlyer** on israelilainen yritys (AppsFlyer Ltd., Herzliya). Israelista on olemassa Euroopan komission päätös tietosuojan riittävyydestä (2011/61/EU). AppsFlyerin tietojenkäsittelyliite nimeää sen **henkilötietojen käsittelijäksi** ja meidät rekisterinpitäjäksi, ja sen julkaisema alikäsittelijäluettelo ilmoittaa palvelinten tarjoajiksi Amazon Web Servicesin ja Google Cloudin, sijaintina ”EU/USA”. Riittävän suojan maiden ulkopuolelle tehtäviin siirtoihin liite sisältää **vakiosopimuslausekkeet** (täytäntöönpanopäätös (EU) 2021/914), **moduuli kaksi: rekisterinpitäjältä henkilötietojen käsittelijälle**, ja Yhdistyneen kuningaskunnan osalta ICO:n liitteen **International Data Transfer Addendum**. Emme ole varmistaneet, millä alueella tietojamme säilytetään. *Tarkistettu AppsFlyerin julkaisemasta tietojenkäsittelyliitteestä (helmikuu 2023), alikäsittelijäluettelosta ja palvelujen tietosuojakäytännöstä 19. marraskuuta 2026.*

**Meta**, kohdassa 2 kuvatun tietojen jakamisen osalta. Meta Platforms Ireland Ltd. on EU:ssa ja välittää tietoja Meta Platforms, Inc:lle Yhdysvaltoihin Metan omien siirtoehtojen mukaisesti. Metan Business Tools -ehtojen mukaan se toimii henkilötietojen käsittelijänämme, kun se yhdistää tietoja ja mittaa, ja yhteisrekisterinpitäjänä kanssamme, kun se käyttää saamiaan tietoja päättääkseen, kuka näkee mainoksia. *Luettu Metan Business Tools -ehdoista 20. marraskuuta 2026; emme ole varmistaneet Metan siirtomekanismia enempää kuin mitä noissa ehdoissa sanotaan.*

**Apple**: katso Applen tietosuojakäytännöstä sen omat siirtoja koskevat suojatoimet. Yksityisiä iCloud-tietojasi koskevat Applen ehdot, emmekä me siirrä niitä, koska ne eivät koskaan ole meillä.

**Me.** Olemme sijoittautuneet Ukrainaan, joka on ETA-alueen ulkopuolella ja josta ei ole Euroopan komission päätöstä tietosuojan riittävyydestä. Kun annat tietoja suoraan meille, kyse on suorasta keräämisestä eikä V luvun mukaisesta siirrosta (Euroopan tietosuojaneuvoston ohjeet 05/2021, jotka koskevat 3 artiklan ja V luvun välistä suhdetta). Käytännössä kerättävää ei juuri ole: tiliä ei ole, ja ainoat henkilötiedot, jotka me näemme, ovat pseudonyymi tilaustieto RevenueCatin hallintanäkymässä, kootut luvut TelemetryDeckin näkymässä ja asennuskohtaiset tiedot AppsFlyerin näkymässä.

## 5. Kuinka kauan mitäkin säilytetään

- **Laitteellasi ja yksityisessä iCloudissasi:** kunnes poistat ne. Me emme voi poistaa niitä puolestasi emmekä estää sinua poistamasta niitä.
- **Meidän järjestelmissämme:** ei mitään. Kohtien 14 ja 15 kaksi pientä palvelua eivät säilytä mitään tietoja. Ulkopuoliset palvelimet, joilla on jotain meihin liittyvää, ovat RevenueCatin, TelemetryDeckin ja AppsFlyerin; katso alla.
- **Lause, jonka lähetit meille sähköpostilla julkaistavaksi:** niin kauan kuin käytämme sanojasi, kunnes pyydät meitä lopettamaan. Katso kohta 2.
- **Ostotiedot:** Apple ja RevenueCat säilyttävät ne omien säilytysaikojensa mukaan sekä vero- ja kirjanpitolainsäädännön edellyttämällä tavalla.
- **Laitteellasi olevat käyttömäärät:** poistuvat, kun sovellus poistetaan.
- **AppsFlyerin hallussa olevat asennus- ja tapahtumatiedot:** sen palvelujen tietosuojakäytännön mukaan se ei säilytä loppukäyttäjien tietoja yli **kahtakymmentäneljää kuukautta**. Tietueen voi saada poistetuksi aiemmin AppsFlyerin omalla lomakkeella (kohta 2).
- **Metalle välitetyt asennus- ja avaustiedot** (kohta 2, ”Metan mainokset”): Metan ehdot sallivat niiden säilyttämisen enintään **kaksi vuotta**.
- **TelemetryDeckin hallussa olevat tapahtumien nimet:** **se ei julkaise niille poistoaikataulua.** Sen hinnoittelupaketeissa mainitaan säilytysaika, ilmaisella tasolla 90 päivää ja maksullisilla enemmän, mutta se on *hakuikkuna*: kuinka kauas taaksepäin sen näkymistä voi katsoa. Ikkunaa vanhemmat tiedot siirretään arkistotallennukseen eikä niitä poisteta, ja ne voidaan ladata takaisin. TelemetryDeckin mukaan poistamisesta, kertaluonteisesta tai aikataulutetusta, voi sopia pyynnöstä. Emme ole sopineet siitä, joten oleta, että nämä signaalit säilyvät toistaiseksi. Koska ne ovat lukuja ilman tunnistetta, joka johtaisi sinuun, asia on pienempi kuin miltä se kuulostaa. Se on kuitenkin täsmällinen, ja kirjoitamme mieluummin sen kuin luvun, jonka keksimme itse.

## 6. Kuka on vastuussa

**Rekisterinpitäjä:** Kyrylo Lozovyi
**Osoite:** Vidpochinku 12, Kyiv, Ukraina
**Yhteydenotot tietosuoja-asioissa:** [support@trysilex.com](mailto:support@trysilex.com) (tavoitat meidät myös osoitteesta [stopgamblesupport@gmail.com](mailto:stopgamblesupport@gmail.com), joka näkyy sovelluksen nykyisissä versioissa)

Emme ole nimittäneet tietosuojavastaavaa. Meidän ei tarvitse, koska emme tee laajamittaista seurantaa emmekä säilytä järjestelmissämme erityisiin henkilötietoryhmiin kuuluvia tietoja (katso kohta 3).

## 7. Oikeutesi

Jos olet ETA-alueella tai Yhdistyneessä kuningaskunnassa, sinulla on oikeus **saada pääsy** tietoihisi, oikeus tietojen **oikaisemiseen**, **poistamiseen**, käsittelyn **rajoittamiseen** ja tietojen **siirtämiseen järjestelmästä toiseen**, oikeus **vastustaa** oikeutettuun etuun perustuvaa käsittelyä ja oikeus **peruuttaa suostumus** milloin tahansa silloin, kun käsittely perustuu suostumukseen (DNS-kilpi: peruuta se kytkemällä kilpi pois; tämä ei vaikuta jo tehtyyn käsittelyyn).

**Rehellinen rajoitus.** Lähes mistään, mihin tämä sovellus liittyy, meillä ei ole sinusta tunnistettavia tietoja eikä tiliä, joka voisi yhdistää pyynnön ihmiseen. **GDPR:n 11 artiklan** mukaan meidän ei tarvitse hankkia lisätietoja vain tunnistaaksemme sinut, emmekä pyydä sinulta henkilöllisyystodistuksia voidaksemme vastata pyyntöön, johon meillä ei ole tietoja. Käytännössä:

- **Kirjoittamasi sisältö**: käytä oikeuksiasi suoraan. Se on laitteellasi ja iCloudissasi, ja sovelluksen (ja iCloud-kopion) poistaminen hävittää sen kokonaan.
- **Ostotiedot**: ota yhteyttä Appleen, tai ota yhteyttä meihin, niin välitämme pyynnön RevenueCatille, joka toimii henkilötietojen käsittelijänämme.
- **Käyttöanalytiikka**: **21 artiklan mukaisella oikeudellasi vastustaa** oikeutettua etuamme on kytkin eikä asiakaspalvelun jonoa: Asetukset → Tietosi → **Jaa anonyymit käyttötiedot**, pois. Uusia signaaleja ei enää lähde, lähetyskanava poistuu ja levyllä odottavat signaalit poistetaan. Sinun ei tarvitse kirjoittaa meille eikä perustella. Jo lähetettyä ei voi vetää takaisin, eikä sitä voi enää löytääkään, koska mikään siinä ei yksilöi sinua.
- **Mainosten mittaus**: sama kytkin on vastustuksesi tähänkin. Jos haluat, että AppsFlyerin asennuksestasi jo hallussaan pitämät tiedot poistetaan, käytä AppsFlyerin omaa lomaketta (kohta 2). Me emme voi etsiä asennustasi puolestasi edellä kerrotusta syystä: meillä ei ole mitään, mikä yhdistäisi asennuksen ihmiseen.

Kirjoita osoitteeseen [support@trysilex.com](mailto:support@trysilex.com), niin vastaamme kuukauden kuluessa, kuten 12 artiklan 3 kohdassa edellytetään.

**Oikeus tehdä valitus.** Voit tehdä valituksen oman maasi tietosuojaviranomaiselle. Luettelo on osoitteessa [edpb.europa.eu](https://edpb.europa.eu/about-edpb/board/members_en); Yhdistyneessä kuningaskunnassa viranomainen on [ICO](https://ico.org.uk/make-a-complaint/). Sinun ei tarvitse ottaa ensin yhteyttä meihin, vaikka toivommekin sitä.

## 8. Kaiken poistaminen

- Poista sovellus iPhonestasi.
- Poista iCloud-kopio: Asetukset → [nimesi] → iCloud → Hallitse tilin tallennustilaa → Silex.
- Peruuta tilaus: Asetukset → [nimesi] → Tilaukset, tai sovelluksen Hallitse tilausta -linkki.

## 9. Arkaluonteiset tiedot, ja miksi sovelluksen rakenne on varsinainen käytäntö

Se, mitä kirjaat tähän, koskee terveyttäsi ja rahojasi, ja kohtelemme sitä sen mukaisesti. Ei tilejä, joihin murtautua, ei omilla palvelimillamme mitään, minkä voisi vaatia luovutettavaksi oikeuden määräyksellä, eikä millään toimittajalla mitään, mikä olisi luettavissa takaisin *sinun* toipumiseksesi. Vahvin suoja, jonka voimme tarjota, on se, ettei meillä ole tietojasi lainkaan. Se osa on rakenteellinen eikä lupaus: avainta, varmuuskopiota ja kopiota ei ole, joten ei ole mitään, minkä suhteen voisimme hiljaa muuttaa mieltämme.

**Mikä muuttui.** Elokuuhun 2026 asti tässä kohdassa sanottiin myös, ettei millään analytiikkatoimittajalla ole kopiota. Se ei enää pidä paikkaansa: TelemetryDeckillä on luku siitä, kuinka moni asennus pääsi mihinkin näkymään. Se on todellinen heikennys takuuseen, emmekä aio kutsua sitä muuksi. Jäljellä on se osa, joka oikeasti merkitsee: sisältö pysyy puhelimessasi, noihin lukuihin liitettyä tunnistetta ei voi yhdistää sinuun eikä seurata sovelluksesta toiseen, ja kaikella tällä on kytkin. Luovuimme mahdollisuudesta sanoa *ei mitään*.

Marraskuussa 2026 lisättiin toinen toimittaja: AppsFlyerille kerrotaan, että asennus tapahtui ja seurasiko siitä kokeilujakso tai osto, jotta tiedämme, mitä mainoksia kannattaa pitää käynnissä. Se on toinen heikennys, ja samat asiat jäävät siitäkin jäljelle: mitään kirjaamaasi ei lähde puhelimestasi, mainostunnistetta ei ole, ja kytkin kattaa tämän.

22. marraskuuta 2026 tuli kolmas, ja siitä pidämme vähiten: niin kauan kuin mainostamme Facebookissa ja Instagramissa, Metalle kerrotaan, että asennus on olemassa (kohta 2, ”Metan mainokset”). Mitään kirjaamaasi ei lähde puhelimestasi, ja kytkin kattaa tämänkin, mutta niin kauan kuin tämä kestää, emme voi enää sanoa, ettei yksikään mainosyhtiö saa tietää yhdestäkään asennuksesta. Jos se loppuu, päivämäärä tulee tähän.

## 10. Lapset

Silex on tarkoitettu aikuisille eikä sitä ole suunnattu lapsille. Emme tietoisesti kerää tietoja alle 18-vuotiailta. App Storen ikäluokitus on tämän mukainen.

## 11. Muutokset

Jos tämä käytäntö muuttuu, muuttuu myös sivun alussa oleva päivämäärä, ja voimassa oleva versio on aina julkaistu tässä osoitteessa.

TelemetryDeckin lisääminen on olennainen muutos, ja tämän kohdan edellinen versio lupasi, että olennaiset muutokset tuodaan esiin sovelluksessa. **Olemme muuttaneet tuota lupausta sen sijaan, että väittäisimme pitäneemme sen.** Sovelluksessa ei ole keinoa näyttää ilmoitusta päivityksen yhteydessä, emmekä aio kuvata sellaista, jota ei ole. Tämä julkaisu tuo käytännössä kytkimen Asetuksiin ja sen viereen selkeän kuvauksen siitä, mitä lähetetään: näkyvillä sille, joka katsoo, mutta ei tyrkytettynä sille, joka ei katso. Se on vähemmän kuin vanha lause lupasi, ja juuri siksi lausetta piti muuttaa eikä kertomusta siitä, mitä tapahtui.

AppsFlyerin lisääminen marraskuussa 2026 on samanlainen olennainen muutos, ja se tehdään samalla tavalla: se nimetään tässä ja versiotiedoissa, se on jo olemassa olleen kytkimen alla, ja kytkimen vieressä oleva lause on muutettu kertomaan siitä.

Lupaus kuuluu nyt näin: olennaiset muutokset nimetään tässä kohdassa ja sen version App Store -versiotiedoissa, joka tekee muutoksen, ja jokainen muutos, joka laajentaa sitä, mitä laitteeltasi lähtee, julkaistaan samassa versiossa sen hallintaan tarkoitetun kytkimen kanssa.

22. marraskuuta 2026 alkanut tietojen jakaminen Metalle on olennainen muutos, jota tämä lupaus ei osannut ennakoida. Mitään uutta ei lähde laitteeltasi. Muuttunut on se, että AppsFlyer välittää osan siitä eteenpäin, ja se kytkettiin päälle AppsFlyerin asetuksissa eikä sovelluksen julkaisussa. Siksi ei ollut versiotietoja, joissa sen olisi voinut nimetä. Se nimetään tässä alkamispäivänään, olemassa oleva kytkin kattaa sen, ja seuraavan julkaisun versiotiedot mainitsevat sen.

## 12. Yhteystiedot

[support@trysilex.com](mailto:support@trysilex.com)

## 13. Ilmainen selainlaajennus

Tämä seloste kattaa myös **Silex — Free Gambling Blocker** -selainlaajennuksen Chromelle, Microsoft Edgelle ja Firefoxille. Se on yksinkertaisempi kuin sovellus, ja niin on myös tämä kohta:

- **Se ei kerää mitään.** Ei tiliä, ei analytiikkaa, ei tunnisteita, eikä se tee omia verkkopyyntöjä. Sinusta tai selaamisestasi ei lähetetä mitään meille eikä kenellekään muulle.
- **Miten se estää.** Laajennuksen sisällä on luettelo rahapelidomaineista. Selaimesi vertaa avaamiasi sivuja tuohon luetteloon paikallisesti selaimen omalla `declarativeNetRequest`-toiminnolla. Selain ei kerro laajennukselle eikä meille, millä sivustoilla käyt tai mitkä niistä estettiin.
- **Miksi se pyytää pääsyä kaikille sivustoille.** Selaimet antavat laajennuksen korvata estetyn sivun omalla apusivullaan virheilmoituksen sijaan vain, jos laajennuksella on pääsy kyseisille sivustoille. Pääsyä ei käytetä mihinkään muuhun: laajennus ei lue, muuta tai kerää minkään sivun sisältöä.
- **Apusivulla** näkyy kriisipuhelimia ja linkkejä tälle sivustolle. Linkin avaaminen on tavallinen käynti trysilex.comissa, ja sen kattaa tämän selosteen muu osa.
- **Puuttuvasta sivustosta ilmoittaminen** avaa oman sähköpostisovelluksesi. Se, mitä lähetät, on sinun päätettävissäsi. Käytämme sitä vain luettelon päivittämiseen ja vastaamiseen.
- **Laajennuksen poistaminen** poistaa sen ja kaiken siinä olevan.

Domainluettelo perustuu The Blocklist Project -hankkeeseen (public domain) ja Université Toulouse Capitolen UT1-listoihin (CC BY-SA 4.0).

## 14. Toipumisen seurantasivu Notionissa

**Silex Recovery Tracker for Notion** on vapaaehtoinen, ilmainen liitin, joka luo toipumisen seurantasivun omaan Notion-työtilaasi. Se ei liity sovellukseen millään tavalla: toisen käyttäminen ei vaikuta toiseen.

- **Mitä ajetaan ja missä.** Pieni itse kirjoittamamme funktio, jota Cloudflare ylläpitää. Se toimii vain muutaman sekunnin ajan sen jälkeen, kun olet napsauttanut Connect ja hyväksynyt pääsyn Notionissa.
- **Mitä se saa.** Notion lähettää sille kertakäyttöisen koodin, jonka se vaihtaa työtilasi käyttöoikeustunnukseen. Notionin vastauksessa on myös työtilasi nimi ja Notion-profiilisi (nimi sekä mahdollisesti sähköposti ja profiilikuva). Funktio lukee vain tunnuksen ja ohittaa muun.
- **Mitä se tekee tunnuksella.** Se luo työtilaasi yhden sivun, kaksi taulukkoa ja kaksi esimerkkiriviä ja ohjaa sinut sitten tuolle sivulle. Se ei lue tai etsi olemassa olevia sivujasi, paitsi (vain jos Notion kieltää ylimmän tason sivun) löytääkseen sen yhden sivun, jonka valitsit jaettavaksi, jotta seurantasivu voidaan sijoittaa sen sisään.
- **Mitä se säilyttää.** Ei mitään. Tunnus on muistissa vain tuon yhden pyynnön ajan. Tietokantaa, tiedostoa tai kopiota siitä, mitä kirjoitat seurantasivulle, ei ole. Emme voi avata seurantasivuasi jälkikäteen, ja jos Notion palauttaa virheen, lokiin tallentuu vain Notionin virhekoodi, ei koskaan työtilan sisältöä.
- **Poistaminen.** Avaa Notionissa asetusten yhteydet (Settings → Connections) ja poista Silex. Seurantasivu jää: se on tavallinen sivu, joka kuuluu sinulle. Poista se kuten mikä tahansa sivu.

Oikeusperuste: pyyntö, jonka teet napsauttamalla Connect (GDPR:n 6 artiklan 1 kohdan b alakohta). Cloudflare käsittelee itse yhteyttä (IP-osoitettasi ja pyynnön otsaketietoja) henkilötietojen käsittelijänämme; katso [Cloudflaren tietosuojakäytäntö](https://www.cloudflare.com/privacypolicy/). Se, mitä kirjoitat seurantasivulle, on sinun ja Notionin välinen asia [Notionin tietosuojakäytännön](https://www.notion.com/trust/privacy-policy) mukaisesti.

## 15. Silex Help ChatGPT:ssä ja muissa tekoälyavustajissa

**Silex Help** on ilmainen, vain luku -palvelu, jota ChatGPT:n kaltaiset tekoälyavustajat voivat kutsua vastatakseen kysymyksiin rahapelaamisen lopettamisesta: maan auttavat puhelimet, pelikieltojärjestelmät, onko verkkosivusto rahapelidomainien luettelossamme, PGSI-itsearvio ja esto-ohjeet. Se ei liity sovellukseen, eikä siinä ole tilejä.

- **Mitä se saa.** Vain sen, mitä avustaja lähettää käyttäessään työkalua: maan, tarkistettavat verkko-osoitteet tai yhdeksän itsearvion vastaustasi. Keskusteluasi, nimeäsi ja avustajatiliäsi ei lähetetä meille.
- **Mitä se tekee.** Se hakee vastauksen palvelun mukana tulevista tiedoista ja lähettää sen takaisin. Se ei tee pyyntöjä kenellekään muulle.
- **Mitä se säilyttää.** Ei mitään. Jokainen pyyntö käsitellään muistissa ja unohdetaan. Tietokantaa ei ole, eikä lokia siitä, mitä kysyttiin.
- **Itse avustaja.** Se, mitä kirjoitat ChatGPT:lle tai muulle avustajalle, kuuluu kyseisen palveluntarjoajan oman tietosuojakäytännön piiriin, ei tämän.

Oikeusperuste: pyyntö, jonka avustajasi tekee puolestasi (GDPR:n 6 artiklan 1 kohdan b alakohta). Cloudflare ajaa palvelua ja käsittelee jokaisen yhteyden (IP-osoitteen ja pyynnön otsaketiedot) henkilötietojen käsittelijänämme; katso [Cloudflaren tietosuojakäytäntö](https://www.cloudflare.com/privacypolicy/).

## Jos tarvitset jonkun juuri nyt

- Suomi: [0800 100 101](tel:0800100101) — Peluuri, rahapelaaminen: ilmainen ja nimetön, arkisin klo 12–18
- Suomi: [09 2525 0111](tel:0925250111) — MIELI Kriisipuhelin, ympäri vuorokauden (oman operaattorin hinta)
- Hätätilanne: [112](tel:112) — Välitön hengenvaara
- Muut maat: [findahelpline.com](https://findahelpline.com) — Kriisilinjat siellä missä olet
