# ohtun_miniprojekti_2022
## Harmaa ryhmä

[Loppuraportti](https://docs.google.com/document/d/1aPiCDaj-eSyMlc4cHEsy6Xs8pbnhsTw2e1hg8kxBDvA/edit)

[Product- ja Sprint backlog](https://docs.google.com/spreadsheets/d/1dSeB2DVMEAkoBBqOm-5AjHcTrGz0yfAUg2ushvxjXvA/edit#gid=0)

![Status Badge](https://github.com/qusba/ohtun_miniprojekti_2022/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/qusba/ohtun_miniprojekti_2022/branch/main/graph/badge.svg?token=X48HWMD7NB)](https://codecov.io/gh/qusba/ohtun_miniprojekti_2022)
### Definition of done
* Testikattavuus on vähintään 80%
* Ainakin yksi ryhmänjäsen, joka ei ole itse kirjoittanut sitä, on lukenut koodin
* Koodi on integroitu buildiin


### Ohjelman asennus- ja käyttöohje

#### Asennusohje
* Avaa terminaali
* Kirjoita komentoriville: git clone git@github.com:qusba/ohtun_miniprojekti_2022.git
* Mene kansioon ohtun_miniprojekti_2022 sisälle
* Kirjoita komentoriville: poetry install
* Kirjoita komentoriville: poetry run python3 src/index.py

#### Käyttöohje
* Ohjelma pyytää syöttämään luvun 1, 2, 3, 4 tai 5
* Antamalla ohjelmalle syötteen 1. Ohjelma luo uudeen kirjaviitteen: Luodakseen kirjaviitteen ohjelma pyytää syöttämään järjestyksessä:
    * Avaimen, joka ei ole vielä käytössä, muuten ohjelma ilmoittaa: "Tällä avaimella löytyy jo viite"
    * Kirjailijan etunimen
    * Kirjailijan sukunimen
    * Kirjan nimen
    * Kirjan julkaisuvuoden
    * Kirjan julkaisijan
    * Tägin, joita voi lisätä useita, mutta yksi kerrallaan
    * Painamaan enteriä viitteen luomiseksi

* Antamalla ohjelmalle syötteen 2. ohjelma tulostaa listan tiedostoon lisätyistä kirjaviitteistä annetun syötteen perusteella:
    * Annettaessa syöte 1.: Ohjelma tulostaa kirjaviitteet lisäysjärjestyksessä vanhinpana lisätty viite ensin.
    * Annettaessa syöte 2.: Ohjelma tulostaa kirjaviitteet lisäysjärjesteyksessä viimeisimpänä lisätty viite ensin.
    * Annettaessa syöte 3.: Ohjelma tulostaa kirjaviitteet aakkosjärjestyksessä kirjailijan sukunimen mukaan.
    * Annettaessa syöte 4.: Ohjelma tulostaa kirjaviitteet käänteisessä aakkosjärjestyksessä kirjailijan sukunimen mukaan.
    * Painamalla enter pääsee takaisin alkuperäiseen valikkoon, jossa voi valita syötteistä 1, 2, 3, 4 tai 5 mitä haluaa tehdä.

* Antamalla ohjelmalle syötteen 3. ohjelma luo jo valmiiksi tiedostossa olevista kirjaviitteistä BibTeX-muotoisen tiedoston

* Antamalla ohjelmalle syötteen 4. ohjelma poistaa kirjaviitteen sille annetun avaimen perusteella.
    * Ohjelma pyytää syöttämään poistettavan kirjaviitteen avaimen ja poistaa viitteen

* Antamalla ohjelmalle syötteen 5. ohjelma lisää tägin jo valmiiksi olemassa olevaan kirjaviitteeseen
    * Ohjelma pyytää syöttämään tägättävän kirjavitteen avaimen ja sen jälkeen annettavan tägin
    * Painamalla enter pääsee takaisin alkuperäiseen valikkoon

* Ohjelman sammuttaaksesi paina enteriä.
