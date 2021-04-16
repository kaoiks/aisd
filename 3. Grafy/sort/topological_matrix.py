def topologicalSortMatrix(graph):
    stack = []
    for i in range(len(graph.adjacency)):
        topologicalSortStep(graph, i, stack)

    stack.reverse()
    return stack

def topologicalSortStep(graph, node_index, visited_stack):
    if graph.isVisited[node_index]:
        return

    successors = graph.getImmediateSuccessors(node_index)

    for succ in successors:
        topologicalSortStep(graph, succ, visited_stack)

    graph.isVisited[node_index] = True
    visited_stack.append(node_index)