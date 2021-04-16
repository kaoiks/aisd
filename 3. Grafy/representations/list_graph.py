from collections import deque

class ListGraph:
    def __init__(self, vertices):
        self.vertices = [None] * len(vertices)
        for i in range(len(vertices)):
            self.vertices[vertices[i].id] = ListGraphNode(vertices[i].id)
        
        for i in range(len(vertices)):
            for node in vertices[i].successors:
                self.vertices[vertices[i].id].addSuccessor(node)
    
    def getVertex(self, num):
        return self.vertices[num]
    
    def getVertexCount(self):
        return len(self.vertices)


class ListGraphNode:
    def __init__(self, val):
        self.successors = deque()
        self.id = val
        self.isVisited = False

    def addSuccessor(self, succ):
        self.successors.append(succ)
    
    def getImmediateSuccessors(self):
        return self.successors