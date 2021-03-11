# Sortuje tablicę z użyciem algorytmu mergesort
def mergesort(arr):
    b = [0] * len(arr)
    mergesort_step(arr, 0, len(arr), b)
    return arr

def mergesort_step(arr, l, r, b):
    m = int((l + r) / 2)
    if m > l:
        mergesort_step(arr, l, m, b)
    if r > m + 1:
        mergesort_step(arr, m, r, b)

    i = l
    j = m
    for k in range(l, r):
        if (i < m and j >= r) or (i < m and j < r and arr[i] <= arr[j]):
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
    for k in range(l, r):
        arr[k] = b[k]
