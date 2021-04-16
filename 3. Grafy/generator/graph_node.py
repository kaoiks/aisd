class GraphNode:

    def __init__(self):
        self.successors = []

    # Dodaje następnik do wierzchołka
    def addSuccessor(self, succ):
        self.successors.append(succ)