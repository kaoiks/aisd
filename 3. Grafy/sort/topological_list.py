def topologicalSortList(graph):
    stack = []
    visited = [False] * len(graph.vertices)
    for i in range(len(graph.vertices)):
        topologicalSortStep(graph, i, stack, visited)

    stack.reverse()
    return stack

def topologicalSortStep(graph, node_index, stack, visited):
    if visited[node_index]:
        return

    node = graph.getVertex(node_index)
    successors = node.getImmediateSuccessors()

    for succ in successors:
        topologicalSortStep(graph, succ.id, stack, visited)

    visited[node_index] = True
    stack.append(node_index)