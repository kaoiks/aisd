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

    if params['scriptfile'] == None:
        execute([], params)
    else:
        try:
            f = open(params['scriptfile'], 'r')
            for line in f:
                line = line.strip()
                if line.startswith('#') or line == '':
                    continue
                tokens = line.split(' ')
                execute(tokens, params)
        except IOError:
            print('Nie udało sie odczytać skryptu.')

# Wykonuje grupę sortowań
def execute(command_src, def_params):
    params = parse_command_line(command_src, def_params)
    sort_func = get_sort_func(params)
    outfile = get_output(params)

    a = read_input(params)

    time_sum = 0
    repetitions = params['repetitions']
    for i in range(repetitions):
        in_arr = a[:]

        print('Przebieg ', i+1, ':', sep='')
        time_sum += sort(in_arr, sort_func)

    avg = int(10 * time_sum / repetitions) / 10
    print('Średni czas pojedynczego sortowania:', avg, 'ms')

    if outfile != None:
        outfile.write(params['algo'] + ', ' + str(len(a)) + ', ' + str(avg) + '\n')
        outfile.close()


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


# Zwraca uchwyt do pliku wyjściowego
def get_output(params):
    if params['outfile'] == None:
        return None

    try:
        file = open(params['outfile'], 'a')
        return file
    except IOError:
        print('Nie udało się otworzyć pliku wyjściowego.')
        exit(0)


# Odczytuje dane do posortowania
def read_input(params):
    read_fun = input
    if params['infile'] != None:
        try:
            file = open(params['infile'], 'r')
            read_fun = file.readline
        except IOError:
            print('Nie udało się odczytać pliku', params['infile'])
            return []

    a = []
    n = int(read_fun())

    for _i in range(n):
        a.append(int(read_fun()))

    if params['infile'] != None:
        file.close()

    return a

# Przetwarza argumenty wiersza polecenia
def parse_command_line(commands, result=None):
    positional_args = ['algo']
    prefix_args = {
        '-i': 'infile',
        '-o': 'outfile',
        '-p': 'repetitions',
        '-s': 'scriptfile'
    }

    if result == None:
        result = {
            'algo': None,
            'infile': None,
            'outfile': None,
            'repetitions': '1',
            'scriptfile': None
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

    if result['algo'] == None and result['scriptfile'] == None:
        print_usage()
        exit(0)

    result['repetitions'] = int(result['repetitions'])

    return result

# Wypisuje sposób użycia programu
def print_usage():
    supported_func = get_supported_functions()

    print('\nSposób wywołania:')
    print('    sort.py [-i plik_wejściowy] [-o plik_wyjściowy] [-p przebiegów] (algorytm)')
    print('\nObsługiwane algorytmy:')
    for a in supported_func:
        print('    [', a, ']: ', supported_func[a][0], sep='')
    print('\nDomyślnie program wykonuje tylko jeden przebieg, a wyniki trafiają tylko na standardowe wyjście.')
    print('Możliwe jest wybranie pliku wyjściowego, do którego dane będą zapisywane w formacie CSV.')
    print('Zamiast odczytywania ze standardowego wejścia, program jest w stanie wczytać dane do sortowania z pliku.')

main()
