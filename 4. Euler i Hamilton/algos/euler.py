#
# Wyszukuje cykl Eulera rekurencyjnie. Sposób działania jest analogiczny
# jak w przypadku wariantu pod spodem, ale ta funkcja omija limit rekurencji.
#
# Wywołania rekurencyjne są reprezentowane przez parę (v, i0), która opisuje
# przetwarzany wierzchołek v i pierwszego sąsiada do odwiedzenia i0.
#
def euler(graph: list):
    is_visited = [None] * len(graph)
    for i in range(len(graph)):
        is_visited[i] = [False] * len(graph)

    cycle = []

    call_stack = [(0, 0)]

    while len(call_stack) > 0:
        (v, i0) = call_stack.pop()
        for i in range(i0, len(graph)):
            if not graph[v][i]:
                continue
            if is_visited[v][i]:
                continue
            is_visited[v][i] = is_visited[i][v] = True

            # Po zakończeniu przetwarzania wierzchołka i, należy wrócić z powrotem do v
            call_stack.append((v, i+1))
            call_stack.append((i, 0))
            break
        else:
            cycle.append(v)

    return cycle


#
# Wersja rekurencyjna (odpowiednia dla niewielkich grafów)
#
#
# euler(0, graph, [False, ...], [])
# def euler(v: int, graph: list, is_visited: list, cycle: list):
#     for i in range(len(graph)):
#         if not graph[v][i]:
#             continue
#         if is_visited[v][i]:
#             continue
#         is_visited[v][i] = is_visited[i][v] = True
#         euler(i, graph, is_visited, cycle)
#     cycle.append(v)
