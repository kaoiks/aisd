from structures.bst import BSTree

def main():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    tree = createTree(numbers)

    print("Głębokość:", tree.getDepth())
    print("Postorder:", tree.postorder())
    print("Poziom najmniejszego:", tree.getSmallestDepth())


def createTree(numbers):
    t = BSTree()

    for number in numbers:
        t.addNode(number)

    return t

main()
