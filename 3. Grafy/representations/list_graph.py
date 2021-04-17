from collections import deque

class ListGraph:
    def __init__(self, vertices):
        self.successors = [None] * len(vertices)
        for i in range(len(vertices)):
            self.successors[vertices[i].id] = deque()
        
        for i in range(len(vertices)):
            for node, weight in vertices[i].successors:
                self.successors[vertices[i].id].append((node.id, weight))
    
    def getVertexCount(self):
        return len(self.successors)

    def getImmediateSuccessors(self, index):
        return self.successors[index]