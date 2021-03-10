from heapsort import heapsort
from check import check_sort

def main():
    a = []
    n = int(input())

    for _i in range(n):
        a.append(int(input()))

    a = heapsort(a)
    print(a)
    print(check_sort(a))

main()