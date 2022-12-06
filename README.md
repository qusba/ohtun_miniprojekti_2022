# ohtun_miniprojekti_2022
## Harmaa ryhmä

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
* Ohjelma pyytää syöttämään luvun 1, 2, 3 tai 4. 
* Antamalla ohjelmalle syötteen 1. Ohjelma luo uudeen kirjaviitteen: Luodakseen kirjaviitteen ohjelma pyytää syöttämään järjestyksessä:
    * Avaimen, joka ei ole vielä käytössä, muuten ohjelma ilmoittaa: "Tällä avaimella löytyy jo viite"
    * Kirjailijan nimen
    * Kirjan nimen
    * Julkaisuvuoden
    * Julkaisijan

* Antamalla ohjelmalle syötteen 2. ohjelma tulostaa listan tiedostoon lisätyistä kirjaviitteistä värikoodattuna

* Antamalla ohjelmalle syötteen 3. ohjelma luo jo valmiiksi tiedostossa olevista kirjaviitteistä BibTeX-muotoisen tiedoston

* Antamalla ohjelmalle syötteen 4. ohjelma poistaa kirjaviitteen sille annetun avaimen perusteella.

* Ohjelman sammuttaaksesi paina enteriä.
