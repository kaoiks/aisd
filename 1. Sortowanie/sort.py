import timeit
import sys
from check import check_sort

from algos.heapsort import heapsort
from algos.mergesort import mergesort

# Zwraca obsługiwane funkcje sortujące
def get_supported_functions():
    return {
        'heap': ('Heapsort', heapsort),
        'merge': ('Mergesort', mergesort)
    }

def main():
    sort_func = get_sort_func()

    a = []
    n = int(input())

    for _i in range(n):
        a.append(int(input()))

    # Tu znajdzie się posortowana tablica (obejście braku przekazywania przez referencję)
    result = []

    print('Rozpoczęto sortowanie.')
    time = timeit.timeit(lambda: invoke_func(sort_func, a, result), number=1)
    print('Sortowanie zakończone.')

    time = int(time * 1e4) / 10
    print('Sortowanie zajęło', time, 'ms')

    print('Trwa sprawdzanie sortowania...')
    print('Wynik:', check_sort(result[0])[1])


# Wywołuje funkcję sortującą i przechwytuje jej wynik
# Służy do omijania problemu z przypisywaniem wartości w wyrażeniu lambda
# Parametr res musi być tablicą. W jej zerowym elemencie znajdzie się wynik
# Res musi być opakowany w tablicę, by ominąć brak przekazywania przez referencję
def invoke_func(f, arg, res):
    if len(res) == 0:
        res.append(0)
    res[0] = f(arg)

# Zwraca funkcję sortującą, wybraną przez użytkownika w wierszu polecenia
def get_sort_func():
    supported_func = get_supported_functions()

    if len(sys.argv) > 1:
        algo = sys.argv[1]
        if algo in supported_func:
            return supported_func[algo][1]
        else:
            print('Nieobsługiwany algorytm: ', algo)
    print_usage()

def print_usage():
    supported_func = get_supported_functions()

    print('\nSposób wywołania:')
    print('    main.py (algorytm)')
    print('\nObsługiwane algorytmy:')
    for a in supported_func:
        print('    [', a, ']: ', supported_func[a][0], sep='')

    exit(0)

main()
