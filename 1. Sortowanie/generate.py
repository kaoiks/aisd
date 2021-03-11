#
# Generator tablic liczb, do wykorzystania przy testowaniu
# algorytmów sortujących
#

from generators.rand import random_generator
from generators.const import const_generator
from generators.asc import asc_generator
from generators.desc import desc_generator

def main():
    size = get_size()
    generator = get_generator_func()
    output_file = get_file()

    generator(output_file, size)
    output_file.close()

# Pobiera od użytkownika ilość liczb do wygenerowania
def get_size():
    while True:
        try:
            print('Podaj ilość liczb do wygenerowania: ', end='')
            size = int(input())

            if size <= 0:
                raise ValueError(size)

            return size
        except ValueError:
            print('Podano niewłaściwą liczbę')

# Zwraca funkcję generującą taki rodzaj ciągu, jakiego zażyczył sobie użytkownik
def get_generator_func():
    # Obsługiwane generatory ciągu
    legal_types = {
        '~': ('Losowy', random_generator),
        '-': ('Stały', const_generator),
        '/': ('Rosnący', asc_generator),
        '\\': ('Malejący', desc_generator),
        'A': ('A-kształtny', no_generator),
        'V': ('V-kształtny', no_generator)
    }

    # Pyta użytkownika o wybór tak długo, aż dostanie prawidłowy wybór
    choice = ''
    while True:
        print('Wybierz rodzaj zestawu danych [', ' '.join(legal_types.keys()), ']: (? to pomoc) ', end='', sep='')
        choice = input().strip()
        if choice in legal_types:
            break

        if choice == '?':
            for t in legal_types:
                print('\'', t, '\': ', legal_types[t][0], sep='')
        else:
            print('Podano niepoprawny symbol generatora danych')

    # Zwraca generator dla wybranego typu
    return legal_types[choice][1]

# Zwraca odwołanie do pliku wybranego przez użytkownika
def get_file():
    while True:
        try:
            print('Podaj nazwę pliku wyjściowego (rozszerzenie: .in): ', end='')
            filename = input()

            if not filename.endswith('.in'):
                filename += '.in'
            f = open(filename, 'w')
            break
        except IOError:
            print('Nie udało się otworzyć pliku')

    return f

# Funkcja, która jest używana, gdy dany generator nie jest zaimplementowany
def no_generator(file, count):
    print('Żądany generator nie został zaimplementowany')

main()
