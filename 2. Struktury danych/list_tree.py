import timeit

from structures.linked_list import LinkedList
from structures.bst import BSTree

def main():
    repetitions = 5
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    sum_createl = sum_findl = sum_clearl = 0
    sum_createt = sum_findt = sum_cleart = 0
    for i in range(repetitions):
        print("Przebieg #", i+1, sep='')

        list_wrapper = [None]
        t_createl = timeit.timeit(lambda: createList(numbers, list_wrapper), number=1)
        t_createl = int(t_createl * 10e4) / 10
        print("    Lista - tworzenie:", t_createl, "ms")
        sum_createl += t_createl

        t_findl = timeit.timeit(lambda: findAllInList(list_wrapper, numbers), number=1)
        t_findl = int(t_findl * 10e4) / 10
        print("    Lista - wyszukiwanie wszystkich:", t_findl, "ms")
        sum_findl += t_findl

        t_clearl = timeit.timeit(lambda: clearList(list_wrapper), number=1)
        t_clearl = int(t_clearl * 10e4) / 10
        print("    Lista - czyszczenie:", t_clearl, "ms")
        sum_clearl += t_clearl

        tree_wrapper = [None]
        t_createt = timeit.timeit(lambda: createTree(numbers, tree_wrapper), number=1)
        t_createt = int(t_createt * 10e4) / 10
        print("    Drzewo - tworzenie:", t_createt, "ms")
        sum_createt += t_createt

        t_findt = timeit.timeit(lambda: findAllInTree(tree_wrapper, numbers), number=1)
        t_findt = int(t_findt * 10e4) / 10
        print("    Drzewo - wyszukiwanie wszystkich:", t_findt, "ms")
        sum_findt += t_findt

        t_cleart = timeit.timeit(lambda: clearTree(tree_wrapper), number=1)
        t_cleart = int(t_cleart * 10e4) / 10
        print("    Drzewo - czyszczenie:", t_cleart, "ms")
        sum_cleart += t_cleart

    sum_createl = int(10 * sum_createl / repetitions) / 10
    sum_findl = int(10 * sum_findl / repetitions) / 10
    sum_clearl = int(10 * sum_clearl / repetitions) / 10

    sum_createt = int(10 * sum_createt / repetitions) / 10
    sum_findt = int(10 * sum_findt / repetitions) / 10
    sum_cleart = int(10 * sum_cleart / repetitions) / 10

    print("Lista - tworzenie średnio:", sum_createl, "ms")
    print("Lista - wyszukiwanie wszystkich średnio:", sum_findl, "ms")
    print("Lista - czyszczenie średnio:", sum_clearl, "ms")

    print("Drzewo - tworzenie średnio:", sum_createt, "ms")
    print("Drzewo - wyszukiwanie wszystkich średnio:", sum_findt, "ms")
    print("Drzewo - czyszczenie średnio:", sum_cleart, "ms")


def createList(numbers, out_list):
    l = LinkedList()

    for number in numbers:
        l.push_sorted(number)

    out_list[0] = l

def createTree(numbers, out_tree):
    t = BSTree()

    for number in numbers:
        t.addNode(number)

    out_tree[0] = t

def findAllInList(wrapped_list, numbers):
    l = wrapped_list[0]
    for number in numbers:
        l.exists(number)

def findAllInTree(wrapped_tree, numbers):
    t = wrapped_tree[0]
    for number in numbers:
        t.find(number)

def clearList(wrapped_list):
    l = wrapped_list[0]
    l.clear()

def clearTree(wrapped_tree):
    t = wrapped_tree[0]
    t.clear()

main()
