# Sortuje tablicę z użyciem algorytmu selectionsort
def selectionsort(arr):
    for j in range(len(arr)-1, 0, -1):
        max = j
        for i in range(j-1, -1, -1):
            if arr[i] > arr[max]:
                max = i
        temp = arr[j]
        arr[j] = arr[max]
        arr[max] = temp
    return arr
