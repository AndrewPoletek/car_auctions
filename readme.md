# Car auctions
### Opis (PL):
To jest projekt zaliczeniowy na przedmiot "Zaawansowane Programowanie".

Projekt posiada dwa podprojekty:
- car_auctions_backend
- car_auctions_fontend

Wstępnie architektura miała wyglądać tak że 
1. będzie backend w django 
2. frontend w reactjs 
3. komunikacja będzie odbywać się z wykorzystaniem graphql.

Niestety ze względu na terminy koncepcja się zmieniła i całość projektu jest wykonana w samym django w podprojekcie car_auctions_backend na potrzeby zaliczenia przedmiotu

Podprojekt car_auctions_frontend został ponieważ mam zamiar projekt rozbudować o architekture opisaną powyżej.

Autor: Andrzej Połetek

nr indeksu: 13899

### Car auctions Backend
Na ten moment główny podprojekt który zawiera wszystko co jest niezbędne do zaliczenia przedmiotu Zaawansowane Programowanie.
#### Deployment:
1. Instalacja ```pip3 install -r requirements.txt```
2. Tworzenie aukcji przetestowałem z zdjęciem o rozmiarach 1600x1068px i wyglądało to dobrze
3. Na ten moment zaimplementowana jest baza sqlite
4. W środowisku developerskim wkorzystywałem "Python 3.10.4"

### Car auctions frontend
Podprojekt który zawiera wstępny szablon tego jak aplikacja miałaby wyglądać, nie ma żadnej sensownej funkcjonalności.

W przyszłości będzie wykorzystany tutaj graphql do komunikacji z backendem.