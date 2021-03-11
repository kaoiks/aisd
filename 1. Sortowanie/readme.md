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

Dane wejściowe powinny być przekazane za pomocą standardowego wejścia w następujący sposób:
  * W pierwszej linii jedna liczba `N`, określająca ilość liczb do posortowania
  * Dalej `N` linii, z których każda zawiera jedną liczbę

## Generowanie ciągów
Za generowanie ciągów odpowiada plik `generate.py`. Po uruchomieniu zapyta o:
  * ilość liczb do wygenerowania,
  * charakter ciągu (m. in. losowy, rosnący, V-kształtny),
  * nazwę pliku, do którego zapisać ciąg (jeżeli plik istnieje, jest nadpisywany).

Plik wyjściowy będzie miał rozszerzenie `.in`. Ma to na celu uniknięcie przypadkowego nadpisania kodu lub
innych ważnych plików.

Format pliku wyjściowego odpowiada formatowi danych wejściowych oczekiwanemu przez `sort.py`.