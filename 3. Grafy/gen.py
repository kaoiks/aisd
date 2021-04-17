import timeit
import sys
from generator.dag_generator import generateDag
from generator.ug_generator import generateUg

saturation = float(sys.argv[1]) / 100
size = int(sys.argv[2])

print("DAG:", timeit.timeit(lambda: generateDag(size, saturation), number=1))
print(" UG:", timeit.timeit(lambda: generateUg(size, saturation), number=1))