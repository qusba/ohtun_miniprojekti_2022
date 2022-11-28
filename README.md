# ohtun_miniprojekti_2022
## Harmaa ryhmä

[Product- ja Sprint backlog](https://docs.google.com/spreadsheets/d/1dSeB2DVMEAkoBBqOm-5AjHcTrGz0yfAUg2ushvxjXvA/edit#gid=0)

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
* Ohjelma pyytää syöttämään luvun 1 tai luvun 2. Syötteellä 1. ohjelma luo uudeen viitteen ja syötteellä 2. ohjelma listaa tiedostoon lisätyt viitteet.
* Valittiin syöte 1. Nyt ohjelma pyytää syöttämään erikseen peräkkäin järjestyksessä: uuden viitteen avaimen eli viitteen yksilöivän tunnisteen, kirjailijan nimen, Kirjan nimen, Julkaisuvuoden, Julkaisijan.
* Valittiin syöte 2. Nyt ohjelma tulostaa listan kaikista tiedostoon jo lisätyistä viitteistä.
* Ohjelman sammuttaaksesi paina enteriä.