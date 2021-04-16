def topologicalSortList(graph):
    stack = []
    for i in range(len(graph.vertices)):
        topologicalSortStep(graph, i, stack)

    stack.reverse()
    return stack

def topologicalSortStep(graph, node_index, visited_stack):
    node = graph.getVertex(node_index)
    if node.isVisited:
        return

    successors = node.getImmediateSuccessors()

    for succ in successors:
        topologicalSortStep(graph, succ.id, visited_stack)

    node.isVisited = True
    visited_stack.append(node_index)