class GraphNode:

    def __init__(self):
        self.successors = []

    # Dodaje następnik do wierzchołka
    def addSuccessor(self, succ, weight=1):
        self.successors.append((succ, weight))
