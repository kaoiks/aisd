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
