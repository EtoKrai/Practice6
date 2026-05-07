from task2 import *


def get_outgoing_edges(graph, representation, n):
    res = []

    if representation == "Матрица смежности":
        for i in range(len(graph)):
            if graph[n][i] == 1:
                res.append((n, i))

    elif representation == "Матрица инцидентности":
        for i in range(len(graph[0])):
            if graph[n][i] == -1:
                for v in range(len(graph)):
                    if graph[v][i] == 1:
                        res.append((n, v))

    elif representation == "Список смежности":
        for i in graph[n]:
            res.append((n, i))

    elif representation == "Список дуг":
        for x, y in graph:
            if x == n:
                res.append((x, y))

    return res

i=0
print(get_outgoing_edges(r1, "Матрица смежности", i))
print(get_outgoing_edges(r2, "Матрица инцидентности", i))
print(get_outgoing_edges(r3, "Список смежности", i))
print(get_outgoing_edges(r4, "Список дуг", i))