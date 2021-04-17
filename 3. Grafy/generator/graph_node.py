class GraphNode:

    def __init__(self):
        self.successors = []
        self.weights = []

    # Dodaje następnik do wierzchołka
    def addSuccessor(self, succ, weight=1):
        self.successors.append(succ)
        self.weights.append(weight)