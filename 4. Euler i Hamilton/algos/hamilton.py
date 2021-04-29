#
# Wyszukuje cykl Hamiltona rekurencyjnie. Sposób działania jest analogiczny
# jak w przypadku wariantu pod spodem, ale ta funkcja omija limit rekurencji.
#
# Wywołania rekurencyjne są reprezentowane przez parę (v, i0), która opisuje
# przetwarzany wierzchołek v i pierwszego sąsiada do odwiedzenia i0.
#
def hamilton(graph, find_all = False):
    visited = [False] * len(graph)
    cycle = []

    call_stack = [(0, 0)]
    while len(call_stack) > 0:
        (v, i0) = call_stack.pop()
        visited[v] = True
        cycle.append(v)
        for i in range(i0, len(graph)):
            if not graph[v][i]:
                continue
            if visited[i]:
                continue

            # Wywołanie rekurencyjne
            call_stack.append((v, i+1))
            call_stack.append((i, 0))
            break
        else:
            if len(cycle) == len(graph) and graph[0][cycle[-1]] and not find_all:
                break
            visited[v] = False
            cycle.pop()

        if len(cycle) == len(graph) and graph[0][cycle[-1]] and not find_all:
            break

    return cycle

#
# Wersja rekurencyjna (odpowiednia dla grafów < 1000 elementów)
#
#
# def hamiltonStep(v, graph, visited, out_cycle, find_all):
#     out_cycle.append(v)
#     visited[v] = True
#
#     for i in range(len(graph)):
#         if not graph[v][i]:
#             continue
#         if visited[i]:
#             continue
#         hamiltonStep(i, graph, visited, out_cycle, find_all)
#
#         if len(out_cycle) == len(graph) and graph[0][out_cycle[-1]] and not find_all:
#             return
#
#     if len(out_cycle) == len(graph) and graph[0][out_cycle[-1]] and not find_all:
#         return
#     visited[v] = False
#     out_cycle.pop()