import timeit
import sys
from generator.dag_generator import generateDag
from generator.ug_generator import generateUg

if len(sys.argv) <= 2:
    print("Za mało argumentów.")
    print("gen.py <nasycenie w %> <ilość elementów>")
    exit(1)

saturation = float(sys.argv[1]) / 100
size = int(sys.argv[2])

print("Skierowane:", timeit.timeit(lambda: generateDag(size, saturation), number=1), "sekund")
print("Nieskierowane:", timeit.timeit(lambda: generateUg(size, saturation), number=1), "sekund")