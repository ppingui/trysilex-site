> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/fi/esta-rahapelit-iphone/

# Näin estät rahapelisivustot ja -sovellukset iPhonessa

Kirjoittanut [Kyrylo Lozovyi](https://trysilex.com/fi/tietoa-silexista/) · 25. marraskuuta 2026

**Lyhyesti:** Ruutuaika ei yksin riitä. Yhdistelmä, joka pitää, on tämä: **koko järjestelmän DNS-profiili** (kattaa kaikki sovellukset ja selaimet), **Ruutuajan rajoitukset, joiden pääsykoodi on jollakulla muulla** (estää uudelleenasennuksen), ja kaksi kerrosta, jotka ovat puhelimen ulkopuolella: **pelikielto** ja **rahan reittien sulkeminen**. Puhelimen osuus vie noin 30 minuuttia. Suomessa siitä kannattaa aloittaa, koska kansallista pelikieltorekisteriä ei vielä ole.

Onko sinulla Android? [Androidin ohje on täällä](https://trysilex.com/fi/esta-rahapelit-android/). Sen oma ilmainen keino on oikeasti parempi.

Rahapelit voi estää iPhonessa viidellä eri tavalla, ja jokainen kattaa eri asian. Useimmat ohjeet kertovat yhden, siinä on aukko, ja retkahdus kulkee aukosta. Tässä ovat kaikki, rajoituksineen.

## Aloita tästä: mitä kukin tapa kattaa

| Tapa | Kattaa | Kuinka nopeasti sen saa pois? | Hinta |
|---|---|---|---|
| Ruutuajan rajoitukset | Appien asennukset, nimetyt sivustot Safarissa, appien piilottaminen | Sekunneissa, ellei koodi ole jollakulla muulla | Ilmainen |
| Koko järjestelmän DNS-profiili | **Kaikki sovellukset ja selaimet**, Wi-Fi ja mobiiliverkko | Noin minuutissa, asetuksista | Ilmaisia vaihtoehtoja on |
| Safari-esto | Vain Safari | Sekunneissa | Ilmainen tai sovelluksen mukana |
| Maksujen esto | Korttimaksut rahapelisivustoille, jos pankki tarjoaa eston; tilisiirrot maksunvälittäjien kautta erikseen | Nordean kortista oletettavasti heti, odotusaikaa ei mainita | Ilmainen |
| Pelikielto | Pelitilisi suoraan yhtiössä: Veikkaus nyt, ulkomaiset yksi kerrallaan | **Veikkauksen toistaiseksi voimassa oleva: kuukausia** | Ilmainen |

Lue taulukko pinona, älä ruokalistana. Kolme ensimmäistä tekevät pelaamisesta hankalaa. Kaksi viimeistä ovat puhelimen ulkopuolella, eikä niitä kierretä puhelimen asetuksista. Se, joka tekee vain kolme ensimmäistä, retkahtaa yleensä selaimen tai maksutavan kautta, jonka unohti.

## 1. Ruutuaika: estä asennukset ja nimetyt sivustot

Ruutuaika on ilmainen ja valmiina puhelimessa, ja siitä on enemmän hyötyä siinä, mitä se *ehkäisee*, kuin siinä, mitä se suodattaa. Apple siirsi asetuksia iOS 27:ssä, joten tässä ovat molemmat polut.

**Estä uusien rahapeliappien asentaminen.** Poista ensin kaikki rahapeliapit. Sitten:

- **iOS 27:** Asetukset → **Ruutuaika** → **Apit ja sivustot** → **Rajoitukset** → kytke **Appien asentaminen** pois. Jos kytkimen alla ovat App Store, Verkko ja Markkinapaikat, kaikki kolme menevät tilaan **Estetty**.
- **iOS 26 ja vanhemmat:** Asetukset → **Ruutuaika** → **Sisältö ja tietosuoja** → kytke päälle → **Appien asennukset ja ostot** (joissakin versioissa **iTunes- ja App Store -ostot**) → **Appien asentaminen** → **Älä salli**.
- **EU:ssa iOS 26:lla vielä yksi kohta.** iPhoneen saa appeja myös App Storen ohi, joten pelkän App Storen sulkeminen ei riitä. Aseta samassa paikassa **Appien markkinapaikat** ja **Verkko** tilaan **Älä salli**. [Applen mukaan](https://support.apple.com/fi-fi/118128) ne jäävät sallituiksi päivityksen jälkeen, vaikka rajoitukset olisivat jo olleet päällä, joten tarkista.

Tämä on koko puhelimen arvokkain asetus. Sen jälkeen uudelleenasennus vaatii Ruutuajan pääsykoodin.

**Estä rahapelisivustot Safarissa.**

- **iOS 27:** Ruutuaika → **Apit ja sivustot** → **Estetty** → **+**. Kirjoita jokaisen peliyhtiön osoite tai liitä koko lista. Valitse myös **Rajoitukset** → **Suodatus** → **Rajoita aikuisviihdesivustoja**: iOS:n mukaan se estää myös verkkovälityspalvelimet. Kun Ruutuajan pääsykoodi on asetettu, iOS rajoittaa lisäksi yksityistä selausta.
- **iOS 26 ja vanhemmat:** **Sisältö ja tietosuoja** → **App Store, media, verkko ja pelit** → **Verkkosisältö** → **Rajoita aikuisviihdesivuja**, ja lisää jokainen peliyhtiö kohdassa **Älä salli koskaan** → **Lisää sivusto**.

iOS 26:ssa Rajoita aikuisviihdesivuja poistaa samalla Safarin yksityisen selauksen käytöstä, ja se on ihan oikea lisähyöty.

Tarkistimme iOS 27:n valikot iOS 27.1:ssä Applen simulaattorissa 25. marraskuuta 2026. Applen oma [ohje](https://support.apple.com/fi-fi/105121) kuvaa asennusten ja sivustojen eston vain lapsen laitteella (Asetukset → Perhe → lapsen nimi → Apit ja sivustot), joten omassa puhelimessasi rivin nimi voi olla hiukan eri.

**Haittapuoli, josta kukaan ei puhu:** iOS:ssä ei ole rahapeliluokkaa. ”Rajoita aikuisviihdesivuja” on aikuissisällön suodatin. Se osuu joihinkin rahapelisivustoihin sattumalta ja ohittaa useimmat. Jos luotat pelkästään siihen, se ei estä mitään, mitä oikeasti käytät. Sivustojen lisääminen yksitellen toimii, mutta ylläpidät listaa käsin alaa vastaan, jolla on tuhansia peilisivustoja.

**Tee tämä kohta kunnolla:** aseta Ruutuajalle pääsykoodi, jota et itse tiedä. iOS 27:ssä se on kohdassa Ruutuaika → **Pääsykoodi ja hallinta** (iOS 27.1:ssä **Hallitse Ruutuaikaa**) → **Lukitse ruutuajan asetukset**. iOS 26:ssa Lukitse ruutuajan asetukset on suoraan Ruutuajassa. Anna kumppanin, ystävän tai perheenjäsenen näppäillä koodi ja pitää se omana tietonaan. Älä käytä omaa Apple-tiliäsi, kun iOS tarjoaa **Ruutuajan pääsykoodin palautusta**: siihen annettu tili voi nollata koodin. Anna toisen antaa omansa. Se, jolla koodi on, purkaa kaiken yllä olevan viidessä sekunnissa. Varmista siis, ettei se ole sinä kello yksi yöllä.

Äläkä pidä koodia muurina. Applen sivut kertovat sen vaihtamisesta iOS 27:ssä eri tavalla: [toinen](https://support.apple.com/fi-fi/102677) pyytää Face ID:n tai puhelimen oman pääsykoodin sekä palautukseen annetun Apple-tilin, jos iOS kysyy sitä, ja [toinen](https://support.apple.com/fi-fi/guide/iphone/iph272b4c4bd/ios) nykyisen Ruutuajan pääsykoodin. Nojaa kerroksiin, jotka ovat puhelimen ulkopuolella.

## 2. Koko järjestelmän DNS-profiili: se, joka kattaa kaiken

Tämän tavan useimmat ohjeet ohittavat, ja se on vahvin, joka toimii itse puhelimessa. Jokaisen sovelluksen ja selaimen on haettava sivuston nimi ennen kuin se voi yhdistää. Jos haku ei onnistu, yhteyttä ei synny. Laajennuksia tai selainkohtaisia asetuksia ei tarvita, ja se toimii myös mobiiliverkossa.

iOS antaa sovelluksen tai profiilin asentaa salatun DNS:n (DoH), joka koskee koko laitetta. Kun se osoittaa nimipalvelimeen, joka suodattaa rahapelit, vedonlyönti-, kasino- ja automaattisivustot lakkaavat avautumasta. Se ei kysy, onko sivustolla lupa Suomessa, ja siksi se on meillä juuri nyt tärkeämpi kuin maissa, joissa on kansallinen pelikieltorekisteri.

Ilmaisia ja maksullisia vaihtoehtoja, jotka suodattavat rahapelit:

- **Mullvadin julkiset DoH-palvelimet**: ilmainen ”family”-palvelin, joka estää muun muassa rahapelit ja jonka julkisen käytännön mukaan lokeja ei tallenneta.
- **NextDNS**: ilmainen taso kohtuulliseen käyttöön, kytkettävä rahapelilista ja suuri valikoima yhteisön listoja.
- **Control D**: sama ajatus, suodatus luokittain, ilmainen taso.
- **Estosovellus, joka asentaa profiilin puolestasi**, esimerkiksi [Silex](https://trysilex.com/fi/). Se ottaa käyttöön salatun DNS-kilven ja yhdistää julkiset rahapelilistat, joten et ylläpidä listaa itse.

Tarkista lopuksi: kohdassa Asetukset → **Yleiset** → **VPN, DNS ja laitehallinta** → **DNS** pitää näkyä valittuna oma määrityksesi, ja tutun rahapelisivuston pitää jäädä latautumatta selaimessa, jota et yleensä käytä. Valikon nimi vaihtelee iOS-version mukaan, Applen ohjeissa se on myös VPN ja mobiililaitteen hallinta.

**Rajoitus suoraan sanottuna:** saat sen pois asetuksista alle minuutissa. DNS-suodatus on hidaste päättäväistä himoa vastaan, ei muuri. Se on erinomainen hidaste, sillä useimmat retkahdukset ovat äkillisiä ja minuutin kitka usein riittää. Älä kuitenkaan pidä sitä viimeisenä linjana.

## 3. Safari-estot

Sisältöä estävä laajennus voi jättää listan sivustoja lataamatta Safarissa. Ota se käyttöön: Asetukset → **Apit** → **Safari** → **Laajennukset**, valitse laajennus ja kytke päälle **Salli laajennus**. Silexissä on sellainen, kuten useimmissa estosovelluksissa.

Hyödyllinen, mutta kapea: se kattaa Safarin eikä muuta. Chrome, Firefox, Edge, somesovelluksen oma selain ja peliyhtiön oma sovellus jäävät koskematta. Pidä Safari-estoa DNS-suodatuksen lisänä, älä koskaan sen korvaajana.

## 4. Katkaise maksut

Pääsyn esto on vasta puolet. Toinen puoli on tehdä rahan liikuttamisesta vaikeaa. Suomessa pankin esto on harvinainen. Nordean kortin asetuksissa on **Verkkouhkapelaaminen**, jonka voi estää, ja muilta pankeilta kannattaa kysyä. Kortti ei silti ole suurin aukko: nettikasinoille maksetaan usein pankkitunnuksilla maksunvälittäjän kautta, ja välittäjiltäkin voi pyytää estoa.

Viive on tässä koko ajatus: se saa eston kestämään himoa kauemmin. Kun pankki ei sitä tarjoa, viiveen voi rakentaa itse. [Näin se tehdään Suomessa.](https://trysilex.com/fi/esta-rahapelimaksut-pankissa/)

## 5. Pelikielto suoraan peliyhtiöltä

Pitkäkestoisin kerros ei ole puhelimessasi ollenkaan. Pelikielto tarkoittaa, että peliyhtiö ei enää päästä sinua pelaamaan. Suomessa asetat sen nyt **Veikkauksella**: kaiken pelaamisen peliesto, toistaiseksi voimassa oleva. Päihdelinkin mukaan sen purku tulee voimaan vasta kolmen kuukauden kuluttua pyynnöstä. Ulkomaiset kasinot käydään läpi yksi kerrallaan. Kansallinen rekisteri tulee 1.7.2027.

Tätä ei pureta yhdessä himossa, ja juuri siksi se toimii. [Koko pelikielto-opas on täällä.](https://trysilex.com/fi/pelikielto/)

## Mikä ei toimi

- **Pelkkä appien poistaminen.** Uudelleenasennus vie viisitoista sekuntia, ja mobiilisivusto toimii ilman appia.
- **Pelkkä reitittimen esto.** Kodin Wi-Fi-suodatus, Pi-hole tai reitittimen DNS mukaan lukien, haihtuu heti, kun puhelin siirtyy mobiiliverkkoon. Tee sekin, mutta ei ainoana.
- **Tavallinen VPN.** Se siirtää liikenteesi, ei suodata sitä. Joissakin VPN:issä on suodattava DNS, ja se toimii. Tavallisesta VPN:stä ei tässä ole hyötyä.
- **Sovellus, jonka ainoa toiminto on päivälaskuri.** Laskeminen motivoi, mutta se ei ole este. Tarvitset molemmat, ja este tulee ensin.
- **Kaikki, mikä lupaa olla poistamaton iOS:ssä.** Hiekkalaatikko ei salli sitä. Sellaiset väitteet ovat markkinointia, ja niihin uskomalla ihmiset jäävät yhden kerroksen varaan neljän sijasta.

## 30 minuutin käyttöönotto, järjestyksessä

1. Poista kaikki rahapeliapit. Kirjaudu ulos peliyhtiöiden tileiltä, jotka ovat selaimessa auki.
2. Ota käyttöön suodattava DNS-profiili ja varmista, ettei rahapelisivusto lataudu.
3. Kytke Appien asentaminen pois Ruutuajassa, ja samalla markkinapaikat ja Verkko, jos iPhonessasi on ne. Estä sivustot, joilla oikeasti pelasit. Anna jonkun muun asettaa koodi.
4. Ota Safari-esto käyttöön.
5. Estä Verkkouhkapelaaminen, jos pankkisi on Nordea. Muussa pankissa kysy estoa. Lähetä estopyyntö maksunvälittäjille.
6. Aseta Veikkaukselle kaiken pelaamisen peliesto toistaiseksi voimassa olevana ja pyydä kielto jokaiselta ulkomaiselta kasinolta, jolla sinulla on tili.

Kohtia 5 ja 6 lykätään eniten, vaikka juuri kohta 6 kestää pisimpään. Jos sinulla on vain kymmenen minuuttia ja pelaat Veikkauksella, tee kohta 6 ensin. Jos pelaat ulkomaisilla sivustoilla, tee kohta 2 ensin.

## Esto on pohja, ei suunnitelma

Jokainen yllä oleva kerros antaa sinulle aikaa niinä yhdeksänäkymmenenä sekuntina, jolloin himo on huipussaan. Se, mitä teet sillä ajalla, ratkaisee, pitääkö esto seuraavallakin kerralla. [Himo nousee, huipentuu ja laskee melko ennustettavasti](https://trysilex.com/fi/kauanko-pelihimo-kestaa/), ja himon odottaminen ohi on taito, joka paranee harjoittelemalla. Sitä varten on [koko 90 päivän suunnitelma](https://trysilex.com/fi/lopeta-rahapelaaminen/).

Esto voi vahingossa estää myös apua antavia sivustoja. Tallenna Peluurin numero [0800 100 101](tel:0800100101) puhelimeesi: maksuton, ma–pe klo 12–18.

## Lopeta rahapelaaminen. Pidä rahasi.

Silex estää rahapelit koko puhelimessa ja kulkee kanssasi 90 päivää, yhden kerrallaan.

[Lataa Silex iPhoneen](https://apps.apple.com/app/id6798826038?mt=8) [Lataa Silex Androidiin](https://play.google.com/store/apps/details?id=com.klozovyi.stopgamble&referrer=utm_source%3Dtrysilex%26utm_campaign%3Dfi_iphone_guide)

## Usein kysyttyä

### Voinko estää rahapelit iPhonessa ilman erillistä sovellusta?

Voit. Ruutuaika voi estää asennukset ja yksittäiset sivustot, ja iOS:ään voi asentaa DNS-määrityksen, jonka jälkeen rahapelisivustot eivät avaudu missään sovelluksessa. Kumpikin on ilmainen ja valmiina puhelimessa. Sitä iOS ei tee itse, että se pitäisi yllä satojen tuhansien rahapelisivustojen listaa. Sen tuo estosovellus tai suodattava DNS-palvelu.

### Estääkö Ruutuaika rahapelisovellukset?

Osittain. Se voi estää uusien appien asentamisen, piilottaa jo asennettuja ja estää yksittäisiä sivustoja Safarissa. Rahapeleille siinä ei ole omaa luokkaa, joten ”Rajoita aikuisviihdesivuja” ei ole rahapelisuodatin. Sivustot pitää lisätä itse tai käyttää nimipalvelinta, joka ylläpitää listaa puolestasi.

### Voiko rahapelit estää iPhonessa pysyvästi?

Ei, ja jos sovellus väittää muuta, se lupaa liikaa. iOS:ssä voit aina poistaa profiilin tai sovelluksen. Pysyvyys tulee puhelimen ulkopuolelta: pelikiellosta, jonka purku vie kuukausia, ja siitä, että osa rahoistasi on jonkun toisen hallussa. Niitä et saa auki niissä yhdeksässäkymmenessä sekunnissa, jotka himon huippu kestää.

### Estääkö VPN rahapelisivustot?

Tavallinen VPN ei estä. Se muuttaa paikkaa, josta liikenteesi tulee ulos, ei sitä, minne pääset. Tarvitset suodattavan DNS-palvelun tai DNS-pohjaisen eston. Joissakin yksityisyyteen keskittyvissä VPN:issä on mukana suodattava DNS, ja se toimii.

### Toimiiko esto mobiiliverkossa yhtä hyvin kuin Wi-Fissä?

iPhoneen asennettu DNS-määritys toimii, koska se kuuluu laitteelle. Reitittimen esto ei toimi: se loppuu kotiovelle, ja puhelin palaa rahapeleihin heti, kun se siirtyy 5G:hen. Tämä on tavallisin syy siihen, että kodin esto pettää.

## Jos tarvitset jonkun juuri nyt

- Suomi: [0800 100 101](tel:0800100101) — Peluuri, rahapelaaminen: ilmainen ja nimetön, arkisin klo 12–18
- Suomi: [09 2525 0111](tel:0925250111) — MIELI Kriisipuhelin, ympäri vuorokauden (oman operaattorin hinta)
- Hätätilanne: [112](tel:112) — Välitön hengenvaara
- Muut maat: [findahelpline.com](https://findahelpline.com) — Kriisilinjat siellä missä olet
