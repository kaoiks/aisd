from structures.bst import BSTree

def main():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    bst = createTree(numbers)
    avl = transformToAVL(bst)

    bst_depth = bst.getDepth()
    avl_depth = avl.getDepth()

    print("Głębokość drzewa BST:", bst_depth)
    print("Głębokość drzewa AVL:", avl_depth)


def createTree(numbers):
    t = BSTree()

    for number in numbers:
        t.addNode(number)

    return t

def transformToAVL(bst):
    avl = BSTree()
    numbers = bst.getElements()
    AVLTransformStep(avl, numbers, 0, len(numbers))
    return avl

def AVLTransformStep(avl, numbers, l, r):
    if l == r:
        return

    middle = int((l+r) / 2)
    avl.addNode(numbers[middle])

    if r - l == 1:
        return

    AVLTransformStep(avl, numbers, l, middle)
    AVLTransformStep(avl, numbers, middle+1, r)

main()