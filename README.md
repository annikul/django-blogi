# Django-harjoitus 2023 tammi-maaliskuu

Tässä repositoryssä on Django-harjoitteluprojekti, jota on koodattu alkuvuodesta 2023

## Asennus
1. Tee Python-virtuaaliympäristö
```
python3 -m venv venv
```
2. Aktivoi virtuaaliympäristö
- Vastaamalla VSCodessa Yes kun VSCode kysyy aktivoidaanko virtuaaliympäristö.
- Avaa uusi terminaali niin näät että `venv` on aktivoitu (terminaalin rivin alussa lukee tällöin `venv`)
3. Asenna tarvittavat Python-paketit
```
pip install -r requirements.txt
```
- Tarvittaessa lataa `pip:n`uudempi versio `python3 -m pip install --upgrade pip`
4. Aja migraatiot tietokantaan:
```
python3 manage.py migrate
```
- Tämä luo SQLite-tietokannan `db.sqlite3`-tiedostoon
5. Luo pääkäyttäjä:
```
python3 manage.py createsuperuser
```
- Käytä käyttäjätunnusta ja salasanaa, jotka muistat helposti. Esim. "admin" ja "admin".

## Kehitysympäristön käynnistäminen
Aja Djangon runserver komento:
```
python3 manage.py runserver
```
## Uusien Migraatiotiedostojen tekeminen
Kun teet muutoksia models.py-tiedostoon, niin model-muutokset pitää saada myös tietokantaan. Tähän käytetään migraatiotiedostoja. Tehtyjen muutosten pohjalta voi luoda uuden migraatiotiedoston komennolla:
```
python3 manage.py makemigrations
```
Muista myös ajaa luodut migraatiotiedostot komennolla:
```
python3 manage.py migrate
```
