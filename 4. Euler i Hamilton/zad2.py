import sys
from timeit import timeit
from generator.eulerian_generator import generateEulerianGraph
from algos.euler import euler
from algos.hamilton import hamilton

def main():
    if(len(sys.argv) <= 2):
        print("Nie podano wszystkich parametrów. Sposób wywołania:")
        print("zad2.py <nasycenie w %> <ilość wierzchołków>")
        exit(1)
    pass

    saturation = float(sys.argv[1])

    if saturation < 0 or saturation > 100:
        print("Nasycenie musi być z przedziału [0%, 100%]")
        print("Podano: ", saturation, "%", sep="")
        exit(1)
    saturation /= 100

    size = int(sys.argv[2])

    hamilton_time = measureTime(size, saturation)

    print()
    print("      Elementów | ", str(size).rjust(10, " "), sep="")
    print("----------------+------------")
    print("    Algorytm    | Wynik (ms) ")
    print("----------------+------------")
    print(" Cykl Hamiltona | ", str(hamilton_time).rjust(10, " "), sep="")
    print()

def measureTime(size, saturation):
    repetitions = 5

    print("Wyznaczanie cyklu Hamiltona...")
    hamilton_time = 0
    for i in range(repetitions):
        graph = generateEulerianGraph(size, saturation)
        print("Przebieg #", i+1, ": ...", sep="")
        time = timeit(lambda: hamilton(graph, True), number=1)
        print("\033[1APrzebieg #", i+1, ": ", int(time * 1e3), " ms", sep="")
        hamilton_time += time / repetitions
    hamilton_time = int(hamilton_time * 1e4) / 10

    return hamilton_time

main()