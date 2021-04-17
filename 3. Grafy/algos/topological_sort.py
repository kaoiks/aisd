def topologicalSort(graph):
    stack = []
    visited = [False] * graph.getVertexCount()
    for i in range(graph.getVertexCount()):
        topologicalSortStep(graph, i, stack, visited)

    stack.reverse()
    return stack

def topologicalSortStep(graph, node_index, stack, visited):
    if visited[node_index]:
        return

    successors = graph.getImmediateSuccessors(node_index)

    for succ, _weight in successors:
        topologicalSortStep(graph, succ, stack, visited)

    visited[node_index] = True
    stack.append(node_index)