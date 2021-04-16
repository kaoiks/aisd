class MatrixGraph:

    def __init__(self, vertices):
        self.adjacency = [None] * len(vertices)
        self.succ_cnt = [0] * len(vertices)
        for i in range(len(vertices)):
            self.adjacency[i] = [False] * len(vertices)

        for i in range(len(vertices)):
            for succ in vertices[i].successors:
                self.adjacency[i][succ.id] = True
                self.succ_cnt[i] += 1

    def getVertexCount(self):
        return len(self.adjacency)

    def getImmediateSuccessors(self, index):
        succ = [0] * self.succ_cnt[index]
        j = 0
        for i in range(len(self.adjacency[index])):
            if self.adjacency[index][i]:
                succ[j] = i
                j += 1
        return succ