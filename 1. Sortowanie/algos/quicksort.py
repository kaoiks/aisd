from random import randint

# Sortuje tablicę z użyciem algorytmu quicksort - klucz środkowy
def quicksort(arr):
    return quicksort_middle(arr)

# Sortuje tablicę z użyciem algorytmu quicksort - klucz środkowy
def quicksort_middle(arr):
    quicksort_step(arr, 0, len(arr), lambda l, r: int((l+r) / 2))
    return arr

# Sortuje tablicę z użyciem algorytmu quicksort - klucz prawy
def quicksort_right(arr):
    quicksort_step(arr, 0, len(arr), lambda l, r: r-1)
    return arr

# Sortuje tablicę z użyciem algorytmu quicksort - klucz losowy
def quicksort_random(arr):
    quicksort_step(arr, 0, len(arr), lambda l, r: randint(l, r-1))
    return arr

def quicksort_step(arr, p, r, keygen):
    if p >= r - 1:
        return
    q = partition(arr, p, r, keygen)
    quicksort_step(arr, p, q, keygen)
    quicksort_step(arr, q, r, keygen)

def partition(arr, p, r, keygen):
    index = keygen(p, r)
    x = arr[index]
    i = p
    j = r - 1

    while True:
        while arr[j] > x:
            j -= 1
        while arr[i] < x:
            i += 1

        if i < j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
        else:
            return j

# QUICKSORT-MAIN(A)
# 1  QUICKSORT(A, 1, length[A])
# 2 return A
# QUICKSORT(A, p, r)
# 1 if p < r
# 2   then q = PARTITION(A, p, r)
# 3        QUICKSORT(A, p, q)
# 4        QUICKSORT(A, q + 1, r)
# PARTITION(A, p, r)
# 1  x = A[(p + r) / 2]
# 2  i = p - 1
# 3  j = r + 1
# 4 while True
# 5     do repeat
# 6              j = j - 1
# 7        until A[j] <= x
# 8        repeat
# 9              i = i + 1
# 10        until A[i] >= x
# 11 if i < j
# 12         then zamień A[i] <-> A[j]
# 13 else return j
