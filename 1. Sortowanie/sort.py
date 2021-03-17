import timeit
import sys
from check import check_sort

from algos.heapsort import heapsort
from algos.insertionsort import insertionsort
from algos.mergesort import mergesort
from algos.selectionsort import selectionsort

# Zwraca obsługiwane funkcje sortujące
def get_supported_functions():
    return {
        'heap': ('Heap sort', heapsort),
        'insert': ('Insertion sort', insertionsort),
        'merge': ('Merge sort', mergesort),
        'select': ('Selection sort', selectionsort)
    }

def main():
    params = parse_command_line()
    sort_func = get_sort_func(params)

    a = []
    n = int(input())

    for _i in range(n):
        a.append(int(input()))

    time_sum = 0
    repetitions = params['repetitions']
    for i in range(repetitions):
        in_arr = copy_array(a)

        print('Przebieg ', i+1, ':', sep='')
        time_sum += sort(in_arr, sort_func)

    print('Średni czas pojedynczego sortowania:', time_sum/repetitions, 'ms')

def copy_array(a):
    return [e for e in a]

# Wykonuje pojedyncze sortowanie. Zwraca czas, w którym się wykonało
def sort(a, sort_func):
    # Tu znajdzie się posortowana tablica (obejście braku przekazywania przez referencję)
    result = []

    print('  Rozpoczęto sortowanie.')
    time = timeit.timeit(lambda: invoke_func(sort_func, a, result), number=1)
    print('  Sortowanie zakończone.')

    time = int(time * 1e4) / 10
    print('  Sortowanie zajęło', time, 'ms')

    print('  Trwa sprawdzanie sortowania...')
    print('  Wynik:', check_sort(result[0])[1])
    return time


# Wywołuje funkcję sortującą i przechwytuje jej wynik
# Służy do omijania problemu z przypisywaniem wartości w wyrażeniu lambda
# Parametr res musi być tablicą. W jej zerowym elemencie znajdzie się wynik
# Res musi być opakowany w tablicę, by ominąć brak przekazywania przez referencję
def invoke_func(f, arg, res):
    if len(res) == 0:
        res.append(0)
    res[0] = f(arg)

# Przetwarza argumenty wiersza polecenia
def parse_command_line():
    result = {
        'algo': None,
        'repetitions': 1
    }

    if len(sys.argv) <= 1:
        print('Oczekiwano przynajmniej jednego paramteru.')
        print_usage()
        exit(0)

    result['algo'] = sys.argv[1]

    if len(sys.argv) >= 3:
        result['repetitions'] = int(sys.argv[2])

    return result

# Zwraca funkcję sortującą, wybraną przez użytkownika w wierszu polecenia
def get_sort_func(params):
    supported_func = get_supported_functions()

    algo = params['algo']
    if algo in supported_func:
        return supported_func[algo][1]
    else:
        print('Nieobsługiwany algorytm: ', algo)

    print_usage()
    exit(0)

def print_usage():
    supported_func = get_supported_functions()

    print('\nSposób wywołania:')
    print('    sort.py (algorytm) [przebiegów = 1]')
    print('\nObsługiwane algorytmy:')
    for a in supported_func:
        print('    [', a, ']: ', supported_func[a][0], sep='')

main()
