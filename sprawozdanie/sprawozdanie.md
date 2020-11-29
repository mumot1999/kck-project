# Sprawozdanie {.center}

## Temat: Wykrywanie monet {.center}

### Bartłomiej Mumot 141287 {.center}
### Paweł Szalczyk 138859 {.center}


---


### Rozwiązanie: 
Wycięte monety są filtrowane z użyciem GaussianBlur i Canny a następnie ich jakość jest obniżana do zdjęcia 5x5 pikseli w celu podziału zdjęcia na 'sekcje' a następnie są wyznaczane histogramy dla każdej monety z jasnością danego obszaru. Dane są przetwarzane przez `MLPClassifier` z modułu `sklearn.neural_network`

### Działanie:

##### 1. Oryginalna moneta która jest uzywana jako wzór
![](https://i.imgur.com/avegG7V.png)

##### 2. Filtr Canny
![](https://i.imgur.com/hMvafEl.png)

##### 3. Zmiejszenie rozdzielczości
![](https://i.imgur.com/VCHihCP.png)

##### 4. MLPClassifier
Piksele są 'spłaszczane' do jedno wymiarowej listy a następnie dane są przetwarzane przez `MLPClassifier`.
Monety do nauki są filtrowane tak samo jak monety znalezione na zdjęciu

### Podsumowanie:

#### Wersja 1 : 
Template matching. Z użyciem bibliotek OpenCV do przeszukiwania szabnlonów na obrazie staraliśmy się szukać całych monet na zdjęciu. Niestety mała różnorodność konturów zewnętrznych praktycznie uniemożliwiała poprawne rozpoznanie rodzaju monet. Algorytm działał, ale tylko "w warunkach laboratoryjnych" ![](https://i.imgur.com/xZd2nNH.png)

#### Wersja 2 : 
OCR. Za pomocą biblioteki pytesseract staraliśmy się odczytać wartość monety z użyciem optycznego rozpoznawania znaków (OCR). Algorytm działał w mniej niż 1/10 przypadów i poprawnie rozpoznawał tylko 50gr. W pozostałych przypadkach odczytanie było niemożliwe, naprawdopodobnie było to spowodowane faktem, iż monety są obietkami metalowymi bardzo dobrze odbijającymi światło, co uniemozliwia zrobienie im idealnego zdjęcia.

#### Wersja 3:
Wstępne rozpoznawanie charakterystyk obszarów (histogramy wersja 1). Naszym nastepnym podejściem było ustalenie cech charakterystycznych każdej monety poprzez wykrycie ich krawędzi a następnie podzielenie monety na 6 obszarów i wyliczenie średniego pokrycia krawędziami (białymi pixelami) w każdym obszarze.
Po wykryciu monety na zdjęciu, była ona wycinanai przekazywana do porównania z próbkami.
Dla każdej monety było przygotowanych ok 6-8 próbek (wyciętych zdjęć bazowych), gdzie każda z próbek została finalnie przedstawiona jako histogram i porównana z wykrytą monetą, gdzie za pomocą wzorów matematycznych wyliczane było procentowe podobieństwo dwóch monet. Wyniki były uśredniane dla każdego zbioru próbek i wybierane maximum.
Algorytm w tej postaci miał skuteczność rzędu 40%: ![](https://i.imgur.com/N0sqLuy.png)
![](https://i.imgur.com/EbniuJB.png)
Przyczyną stosunkowo małej dokładności było parę czynników:
- "ręczne" porównywanie za pomocą stałego wzoru matematycznego
- duża różnorodnośc w wyglądzie i oświetleniu monet w zależności od położenia na zdjęciu i odbicia światła (co skutkowało rożbieżnościami w wykrywaniu krawędzi)
- różnice w rozdzielczości zdjęc miały znaczący wpływ na jakość wykrywania krawędzi
- uśrednianie wyników dla zbioru próbek okazało się błędnym podejściem ze względu na powyższe problemy: nawet jeżeli program znalazł "prawie" idealne dopasowanie w folderze, inne próbki obniżały dopasowanie. Z kolei brak uśrednienia a wybranie najwyższego wyniku obiżało skutecznośc do ok. 20% ze względu na uniwersalność rozkładu wzorów 20gr (moneta pod względem ilości krawędzi najbardziej podobna do wszystkich pozostałych).

#### Wersja 4 (aktualna):

##### Zdjęcie benchamrkowe
Dokładność: 90%
![](https://i.imgur.com/jyS5rem.png)

##### Prawdziwe zdjęcia
Dokładność: 100%
![](https://i.imgur.com/XuOTy5n.png)

Dokładność: 100%
![](https://i.imgur.com/JdZdZl7.png)

Dokładność: 50%
Niestety zawiódł skrypt odpowiedzialny za wyszukiwanie monet na obrazie
![](https://i.imgur.com/7OxHp0U.png)

Minusem aktualnej wersji jest fakt iż monety których detektor jeszcze nie 'widział' są błędnie rozpoznawane.
Każda moneta która została znaleziona na powyższch zdjęciach została ręcznie przeniesiona do folderu odpowiadającemu wartości tej monecie w groszach (folder `coin_detector/samples_real/[0,1,2,5,...,500]`)


#### Propozycje dalszego rozwoju projektu:

Tak aktualnie wyglądają monety o nominale 5zł które zostały przetrasformowane przez skrypt
![](https://i.imgur.com/jrEIwoV.png)
Chcieliśmy aby dla każdego zdjęcia konkretnej monety znaleźć cechy wspólne, np większe zagęszczenie białych pikseli w lewej części wycinku i na tej zasadzie indentyfikować monety.
Niestety jak widać, nasz program widzi każdą monetę w inny sposób co uniemożliwia zrealizowanie nam naszego planu.
Kolejne ulepszenia miały by na celu dobrania takiego zestawu filtrów który umożliwiałby dopasowanie nowych monet do wzorców.

