> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/fi/docs/protection/

# Suojakerrokset

Suoja-välilehti näyttää viisi kerrosta renkaana, *N/5 kerrosta*. Kaksi otetaan käyttöön sovelluksessa, ja niiden tila tarkistetaan järjestelmästä. Kolme tehdään sovelluksen ulkopuolella, ja merkitset ne itse tehdyiksi.

## 1. Koko järjestelmän DNS-kilpi

Kilpi on kerroksista suurin. Se asentaa salatun DNS-asetuksen (DNS over HTTPS), jonka ansiosta rahapelidomainit eivät lataudu missään puhelimen sovelluksessa tai selaimessa, ei vain Safarissa. Kyselyihin vastaa Mullvadin family-DNS-palvelin Mullvadin lokittomuuskäytännön mukaan. Silex ei ole siinä välissä eikä koskaan näe selaamistasi. Family-palvelin suodattaa rahapelien lisäksi mainokset, seurantaohjelmat, haittaohjelmat ja aikuisviihdesivustot.

1. Avaa Silexissä **Suoja** ja napauta DNS-kilpeä (tai neuvoa *Ota kilpesi käyttöön* päivän 1 loppupuolella).
2. Hyväksy iOS:n kysymys, jossa pyydetään lupaa lisätä DNS-määritys.
3. Avaa **Asetukset › Yleiset › VPN, DNS ja laitehallinta › DNS** ja valitse **Silex Shield**. Vanhemmissa iOS-versioissa valikon nimi on VPN ja laitehallinta.

Silexin rivillä lukee sen jälkeen *Aktiivinen — estää rahapelaamisen apeissasi ja selaimissasi*. Jos siinä lukee *Asennettu*, vaihe 3 on vielä tekemättä.

## 2. Safari-esto

Safarin sisällönesto nimeltään **Silex Site Blocker** estää rahapelidomainit Safarissa puhelimeesi tallennetun listan perusteella. Mukana tulevassa listassa on noin 294 000 domainia, ja Silex lisää siihen julkisen rahapelien estolistan (noin 698 000 domainia 25. marraskuuta 2026), jonka se lataa ja päivittää taustalla muutaman päivän välein. Sivuston vertaaminen listaan tapahtuu puhelimessa; selaamisestasi ei lähetetä mitään mihinkään.

1. Avaa Silexissä **Suoja** ja noudata Safarin opastusta, tai mene suoraan iOS:n Asetuksiin.
2. Avaa **Asetukset › Apit › Safari › Laajennukset**.
3. Ota **Silex Site Blocker** käyttöön.

Kun se on päällä, rivi näyttää, montako rahapelidomainia on estetty. Se kattaa vain Safarin; muut selaimet kattaa DNS-kilpi.

## 3. Pelikielto

Pelikielto sulkee sinut peliyhtiön palveluista, eikä sitä voi purkaa hetken mielijohteesta. Suomessa ei ole vielä yhtä rekisteriä, joka sulkisi sinut kaikkialta: keskitetty rekisteri tulee käyttöön vasta uuden järjestelmän alkaessa heinäkuussa 2027. Siihen asti kielto asetetaan jokaiseen palveluun erikseen, ja Silex opastaa sen vaiheittain. Veikkauksella kielto on nimeltään peliesto. [Pelikielto-oppaassamme](https://trysilex.com/fi/pelikielto/) on yksityiskohdat. Napauta *Tein tämän*, kun kielto on voimassa.

## 4. Pankin rahapeliesto

Jotkin pankit osaavat hylätä maksut rahapeliyrityksille. Suomessa esto on vahvistettu Nordealla: kortin asetuksissa on kohta Verkkouhkapelaaminen, jonka voi sallia tai estää. Odotusaikaa ei mainita, joten oleta, että eston saa heti pois. Muista pankeista kannattaa kysyä. Silex opastaa, mistä asetusta etsitään pankkisovelluksessasi. Katso [miten pankin esto toimii](https://trysilex.com/fi/esta-rahapelimaksut-pankissa/).

## 5. Mainokset pois

Peruuta rahapelisähköpostit ja -tekstiviestit ja kytke vedonlyöntisovellusten push-ilmoitukset pois, jotta tarjoukset eivät tule silloin, kun olet haavoittuva. Silex antaa ohjeet sähköpostiin, tekstiviesteihin ja push-ilmoituksiin.

## Rajat, suoraan sanottuna

- Mikään iPhone-sovellus ei voi tehdä itsestään mahdotonta poistaa. Kuka tahansa päättäväinen voi kytkeä kilven pois tai poistaa Silexin sekunneissa. Siksi kerrokset 3 ja 4 ovat tärkeitä: pelikieltoa ei pureta hetken mielijohteesta, ja pankin esto tuo yhden esteen lisää rahan tielle.
- Ruutuaika ja Family Controls (yksittäisten sovellusten estäminen) eivät ole vielä osa Silexiä. Voit silti antaa luottamasi ihmisen asettaa iOS:n Ruutuajan pääsykoodin. [iPhone-opas](https://trysilex.com/fi/esta-rahapelit-iphone/) näyttää, missä se on iOS 27:ssä ja iOS 26:ssa.
- Työpaikan tai koulun laitehallintaprofiili voi ohittaa kilven, ja hallitussa puhelimessa se voi olla kokonaan estetty.
- Kilpi ei säily tehdasasetusten palautuksessa eikä siirtyessä uuteen puhelimeen. Tee asetukset silloin uudelleen.

## Silexin ohjeet

- [Silexin ohjeet](https://trysilex.com/fi/docs/)
- [Näin pääset alkuun](https://trysilex.com/fi/docs/getting-started/)
- [Suojakerrokset](https://trysilex.com/fi/docs/protection/)
- [SOS-painike](https://trysilex.com/fi/docs/sos/)
- [90 päivän ohjelma](https://trysilex.com/fi/docs/program/)
- [Edistys, säästetyt rahat ja kehrät](https://trysilex.com/fi/docs/progress/)
- [Ilmoitukset ja widgetit](https://trysilex.com/fi/docs/notifications/)
- [Tilaukset](https://trysilex.com/fi/docs/subscriptions/)
- [Tietosuoja ja tietosi](https://trysilex.com/fi/docs/privacy-and-data/)
- [Asetukset-opas](https://trysilex.com/fi/docs/settings/)
- [Vianmääritys](https://trysilex.com/fi/docs/troubleshooting/)

## Jos tarvitset jonkun juuri nyt

- Suomi: [0800 100 101](tel:0800100101) — Peluuri, rahapelaaminen: ilmainen ja nimetön, arkisin klo 12–18
- Suomi: [09 2525 0111](tel:0925250111) — MIELI Kriisipuhelin, ympäri vuorokauden (oman operaattorin hinta)
- Hätätilanne: [112](tel:112) — Välitön hengenvaara
- Muut maat: [findahelpline.com](https://findahelpline.com) — Kriisilinjat siellä missä olet
