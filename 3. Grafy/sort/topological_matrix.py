def topologicalSortMatrix(graph):
    stack = []
    visited = [False] * len(graph.adjacency)
    for i in range(len(graph.adjacency)):
        topologicalSortStep(graph, i, stack, visited)

    stack.reverse()
    return stack

def topologicalSortStep(graph, node_index, stack, visited):
    if visited[node_index]:
        return

    successors = graph.getImmediateSuccessors(node_index)

    for succ in successors:
        topologicalSortStep(graph, succ, stack, visited)

    visited[node_index] = True
    stack.append(node_index)