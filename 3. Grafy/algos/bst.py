class BSTree:

    def __init__(self):
        self.root = None

    # Dodaje element do drzewa
    def addNode(self, content):
        if self.root == None:
            self.root = TreeNode(content)
        else:
            self.root.addChild(content)

    # Wypisuje wszystkie elementy drzewa
    def print(self):
        if self.root != None:
            self.root.print()

    # Usuwa wszystkie wierzchołki drzewa
    def clear(self):
        if self.root == None:
            return

        self.root.removeChildren()
        self.root = None

    # Sprawdza, czy podana wartość istnieje w drzewie
    def find(self, needle):
        if self.root == None:
            return False
        return self.root.find(needle)

    # Zwraca zawartość drzewa
    def getElements(self):
        if self.root == None:
            return []
        return self.root.getElements()

    # Zwraca głębokość drzewa
    def getDepth(self):
        if self.root == None:
            return 0
        return self.root.getDepth()

    # Zwraca tablicę elementów w post-order
    def postorder(self):
        if self.root == None:
            return []
        return self.root.postorder()

    # Zwraca głębokość na której znajuje się najmniejszy element
    def getSmallestDepth(self):
        if self.root == None:
            return -1
        return self.root.getSmallestDepth()


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Dodaje węzeł potomny w odpowiednim miejscu
    def addChild(self, content):
        if content < self.value:
            if self.left != None:
                self.left.addChild(content)
            else:
                self.left = TreeNode(content)
        else:
            if self.right != None:
                self.right.addChild(content)
            else:
                self.right = TreeNode(content)

    # Usuwa wszystkie węzły potomne w porządku postorder
    def removeChildren(self):
        if self.left != None:
            self.left.removeChildren()
            self.left = None
        if self.right != None:
            self.right.removeChildren()
            self.right = None

    # Wypisuje wszystkie elementy drzewa w porządku inorder
    def print(self):
        if self.left != None:
            self.left.print()
        print(self.value, end=' ')
        if self.right != None:
            self.right.print()

    # Wyszukuje element o konkretnej wartości
    def find(self, needle):
        if self.value == needle:
            return True

        if needle < self.value:
            if self.left == None:
                return False
            return self.left.find(needle)
        else:
            if self.right == None:
                return False
            return self.right.find(needle)
    
    # Zwraca zawartość drzewa
    def getElements(self):
        elem = []
        if self.left != None:
            elem += self.left.getElements()
        elem.append(self.value)
        if self.right != None:
            elem += self.right.getElements()
        return elem

    # Zwraca głębokość drzewa
    def getDepth(self):
        depth = -1
        if self.left != None:
            depth = max(depth, self.left.getDepth())
        if self.right != None:
            depth = max(depth, self.right.getDepth())
        return depth + 1

    # Zwraca drzewo w kolejności post-order
    def postorder(self):
        arr = []
        if self.left != None:
            arr += self.left.postorder()
        if self.right != None:
            arr += self.right.postorder()
        arr += [self.value]
        return arr

    # Zwraca poziom najmniejszego elementu
    def getSmallestDepth(self):
        if self.left == None:
            return 0
        return self.left.getSmallestDepth() + 1
