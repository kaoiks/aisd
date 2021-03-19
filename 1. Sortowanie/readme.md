# 1. Sortowanie
W tym katalogu znajdują się kody źródłowe potrzebne do przygotowania sprawozdania
z sortowania na AiSD. Repozytorium zawiera:
  * procedurę wejściową dla sortowania (wczytywanie wejścia, mierzenie czasu),
  * kod sprawdzający poprawność sortowania,
  * zbiór implementacji algorytmów, które miały zostać zbadane,
  * generator ciągów wejściowych o różnym charakterze (m. in. losowe, rosnące, V-kształtne).

## Wywoływanie sortowania
Do wywołania sortowania służy plik `sort.py`. Jako argument w wierszu polecenia należy przekazać
mu symbol algorytmu, który należy uruchomić. W przypadku kiedy nie przekazano żadnego symbolu lub
przekazano błędny, program wypisze wszystkie obsługiwane algorytmy.

Dane wejściowe powinny być przekazane za pomocą standardowego wejścia lub pliku w następujący sposób:
  * W pierwszej linii jedna liczba `N`, określająca ilość liczb do posortowania
  * Dalej `N` linii, z których każda zawiera jedną liczbę

Pełna składnia polecenia `sort.py` wygląda następująco:
```
sort.py (algorytm) [-i plik_wejściowy] [-o plik_wyjściowy] [-p ilość powtórzeń] [-s plik_skryptu]
```
  * `-i` Określa plik, z którego zostaną odczytane liczby do posortowania. Format określono powyżej.
  W przypadku kiedy parametr nie wystąpi, dane są odczytywane ze standardowego wejścia.
  * `-o` Określa plik, do którego będą trafiały informacje o średnich czasach wykonywania się sortowania.
  Format wyjściowy to CSV. Plik nie będzie nadpisywany, ale nowe dane zostaną zapisane na końcu.
  * `-p` Określa ilość powtórzeń sortowania dla podanych danych wejściowych. Do pliku zostanie zapisany
  jedynie średni czas wykonywania.
  * `-s` Określa plik, z którego brać polecenia do wykonania. Skrypt pozwala przeprowadzić wiele
  sortowań przy jednym uruchomieniu programu sortującego.

### Pisanie skryptów
Skrypt jest plikiem tekstowym, w którym każda linia zawiera opcje, które normalnie znalazłyby
się w wierszu polecenia. Linijka nie musi zawierać kompletu opcji, bowiem te, których nie podano
są dziedziczone z opcji ustawionych przy wywoływaniu programu.

Przykładowy skrypt:
```
# Komentarz
insert -i input.txt
-p 5
```
Kiedy program zostanie wywołany w następujący sposób: `sort.py -s skrypt heap -p 2`, wykonane zostaną zadania:
  * Posortowanie algorytmem Insertion Sort pliku `input.txt` z dwoma powtórzeniami,
  * Posortowania danych ze standardowego wejścia algorytmem Heap Sort pięciokrotnie.

## Generowanie ciągów
Za generowanie ciągów odpowiada plik `generate.py`. Po uruchomieniu zapyta o:
  * ilość liczb do wygenerowania,
  * charakter ciągu (m. in. losowy, rosnący, V-kształtny),
  * nazwę pliku, do którego zapisać ciąg (jeżeli plik istnieje, jest nadpisywany).

Plik wyjściowy będzie miał rozszerzenie `.in`. Ma to na celu uniknięcie przypadkowego nadpisania kodu lub
innych ważnych plików.

Format pliku wyjściowego odpowiada formatowi danych wejściowych oczekiwanemu przez `sort.py`.

Możliwe jest wygenerowanie wielu ciągów z użyciem tego narzędzia. W tym celu należy podać liczbę
ciągów do wygenerowania jako argument w wierszu polecenia. Takie wywołanie przybierze postać:
`generate.py [ciągów]`. Paramtery opisujące ciąg można przekazywać z pliku za pomocą operatora `<`.