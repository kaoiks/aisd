from generator.graph_node import GraphNode

def readGraph() -> list:
    size = int(input())
    graph = createEmptyGraph(size)

    for i in range(size):
        weights = list(map(int, input().split()))
        for j in range(size):
            weight = weights[j]
            if weight == 0:
                continue
            graph[i].addSuccessor(graph[j], weight)
    return graph

# Tworzy graf bez łuków
def createEmptyGraph(nodes_count: int) -> list:
    graph = []

    for i in range(nodes_count):
        node = GraphNode()
        node.id = i
        node.isAttached = True
        graph.append(node)

    return graph