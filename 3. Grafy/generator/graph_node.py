from collections import deque

class GraphNode:

    def __init__(self):
        self.successors = deque()

    # Dodaje następnik do wierzchołka
    def addSuccessor(self, succ, weight=1):
        self.successors.append((succ, weight))
