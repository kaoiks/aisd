# Sortuje tablicę z użyciem algorytmu heapsort
def heapsort(arr):
    build_heap(arr)
    heapsize = len(arr)
    
    for i in range(heapsize - 1, 0, -1):
        t = arr[i]
        arr[i] = arr[0]
        arr[0] = t
        heapsize -= 1
        heapify(arr, 0, heapsize)
    return arr

def build_heap(arr):
    heapsize = len(arr)
    for i in range(int(heapsize / 2), -1, -1):
        heapify(arr, i, heapsize)

def heapify(arr, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2

    largest = i
    if l < heapsize and arr[l] > arr[i]:
        largest = l
    if r < heapsize and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        t = arr[largest]
        arr[largest] = arr[i]
        arr[i] = t
        heapify(arr, largest, heapsize)
