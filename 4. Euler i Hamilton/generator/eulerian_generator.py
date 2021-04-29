from random import randint, random, shuffle

# Tworzy graf eulerowski o podanym rozmiarze i nasyceniu
def generateEulerianGraph(size: int, saturation: float) -> list:
    graph = createEmptyGraph(size)
    makeGraphLoop(graph)
    fillGraph(graph, saturation)
    return graph

# Tworzy pusty graf o podanym rozmiarze
def createEmptyGraph(size: int) -> list:
    graph = [None] * size
    for i in range(size):
        graph[i] = [False] * size
    return graph

# Łączy wszystkie wierzchołki w pętlę, by zagwarantować spójność
def makeGraphLoop(graph: list):
    loop = list(range(len(graph)))
    shuffle(loop)
    for i in range(len(graph) - 1):
        graph[loop[i]][loop[i+1]] = graph[loop[i+1]][loop[i]] = True
    graph[loop[0]][loop[-1]] = graph[loop[-1]][loop[0]] = True

# Wypełnia graf krawędziami, tak by uzyskać odpowiednie nasycenie
def fillGraph(graph: list, target_saturation: float):
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if random() > target_saturation:
                continue
            graph[i][j] = graph[j][i] = True

# Dodaje krawędzie między wierzchołkami o nieparzystym stopniu
def adjustEulerity(graph: list):
    neighbors = [graph[i].count(True) for i in range(len(graph))]
    for i in range(len(neighbors)):
        if neighbors[i] % 2 == 0:
            continue

        for j in range(i+1, len(neighbors)):
            if neighbors[j] % 2 == 0:
                continue

            graph[i][j] = graph[j][i] = True
            neighbors[i] += 1
            neighbors[j] += 1
            break
