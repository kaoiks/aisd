class MatrixGraph:

    def __init__(self, vertices):
        self.adjacency = []
        self.isVisited = [False] * len(vertices)
        for _ in range(len(vertices)):
            self.adjacency.append([False] * len(vertices))

        for i in range(len(vertices)):
            for succ in vertices[i].successors:
                self.adjacency[i][succ.id] = True

    def getVertexCount(self):
        return len(self.adjacency)

    def getImmediateSuccessors(self, index):
        succ = []
        for i in range(len(self.adjacency[index])):
            if self.adjacency[index][i]:
                succ.append(i)
        return succ