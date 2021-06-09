from generator import generate
from algos.greedy import greedy
from algos.dynamic import dynamic
from timeit import timeit
import sys



def main():
    # file = open("plecak.txt")

    # n = int(file.readline().split(" - ")[0]) #liczba kontenerow
    # sizes = [int(x) for x in file.readline().split(" - ")[0].split(" ")] #wagi
    # values = [int(x) for x in file.readline().split(" - ")[0].split(" ")] #wartosc
    # b = int(file.readline().split(" - ")[0]) #ladownosc statku
    # kontenery = []
    # #wagi=[]
    # for i in range(n):
    #     kontener = [sizes[i],values[i]]
    #     kontenery.append(kontener)

    if(len(sys.argv) <= 3):
        print("Sposób użycia:")
        print("   ", sys.argv[0], "(pojemność statku) (całkowity rozmiar kontenerów) (współczynnik fragmentacji)")
        exit(1)

    b = int(sys.argv[1])  #1000
    cont_total = int(sys.argv[2])  #2*b
    size_factor = int(sys.argv[3])  #4

    repetitions = 10

    time_d = 0
    time_g = 0
    avg_err = 0

    for i in range(repetitions):
        print("Przebieg", i+1)

        kontenery = generate(b, cont_total, size_factor)
        n = len(kontenery)
        dynamic_ship = [ None ]
        greedy_ship = [ None ]
        time_d += timeit(lambda: invoke(dynamic, dynamic_ship, kontenery, n, b), number=1)
        time_g += timeit(lambda: invoke(greedy, greedy_ship, kontenery, n, b), number=1)

        D_gr = count_value(greedy_ship[0])
        D_dyn = count_value(dynamic_ship[0])
        avg_err += (D_dyn - D_gr) / D_dyn
        print("Zach: ", D_gr, "  Dyn: ", D_dyn)
    
    time_d /= repetitions
    time_g /= repetitions
    avg_err /= repetitions

    time_d = int(1e5 * time_d) / 100
    time_g = int(1e5 * time_g) / 100
    avg_err = int(1e4 * avg_err) / 100

    print("Kontenery:", cont_total)
    print("    Dynamiczny:", time_d, "ms")
    print("     Zachłanny:", time_g, "ms")
    print("          Błąd:", avg_err, "%")


def count_value(containers):
    total = 0
    for cont in containers:
        total += cont[1]
    return total

def invoke(func, ret, arg0, arg1, arg2):
    ret[0] = func(arg0, arg1, arg2)

main()