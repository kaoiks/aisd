import sys
import timeit
from generator.ug_generator import generateUg
from representations.list_graph import ListGraph
from representations.matrix_graph import MatrixGraph
from algos.prim import prim

def main():
    if len(sys.argv) <= 2:
        print("Nie podano wymaganych argumentów. Sposób wywołania:")
        print("prim_cnt.py <nasycenie w %> <ilość wierzchołków>")
        exit(1)
    saturation = float(sys.argv[1]) / 100
    size = int(sys.argv[2])

    searches = measureSearches(size, saturation)

    print()
    print(" Elementów: ", str(size).rjust(8, " "), sep="")
    print("Przeszukań: ", str(searches).rjust(8, " "), sep="")
    print()

def measureSearches(size, saturation):
    repetitions = 5

    print("Pomiar ilości przeszukań...")
    count = 0
    for i in range(repetitions):
        list_graph = ListGraph(generateUg(size, saturation))
        print("Rozpoczęto przebieg #", i+1, sep="")
        out = [0]
        prim(list_graph, out)
        count += out[0]
    count = int(count / repetitions)
    
    return count

main()