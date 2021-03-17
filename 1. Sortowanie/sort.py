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
    params = parse_command_line(sys.argv[1:])
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


# Przetwarza argumenty wiersza polecenia
def parse_command_line(commands):
    positional_args = ['algo']
    prefix_args = {
        '-p': 'repetitions',
        '-o': 'outfile'
    }

    result = {
        'algo': None,
        'outfile': None,
        'repetitions': '1'
    }

    i = 0
    pos_arg_num = 0
    while i < len(commands):
        if commands[i].startswith('-'):
            if commands[i] in prefix_args and i < len(commands) - 1:
                key = prefix_args[commands[i]]
                result[key] = commands[i+1]
                i += 1
            else:
                print('Nieznany przełącznik:', commands[i])
                print_usage()
                exit(0)
        else:
            if pos_arg_num >= len(positional_args):
                print('Nieznany argument pozycyjny:', commands[i])
                print_usage()
                exit(0)

            result[positional_args[pos_arg_num]] = commands[i]
            pos_arg_num += 1
        i += 1

    if result['algo'] == None:
        print_usage()
        exit(0)

    result['repetitions'] = int(result['repetitions'])

    return result

# Wypisuje sposób użycia programu
def print_usage():
    supported_func = get_supported_functions()

    print('\nSposób wywołania:')
    print('    sort.py [-p przebiegów] (algorytm)')
    print('\nObsługiwane algorytmy:')
    for a in supported_func:
        print('    [', a, ']: ', supported_func[a][0], sep='')
    print('\nDomyślnie program wykonuje tylko jeden przebieg, a wyniki trafiają tylko do konsoli')

main()
