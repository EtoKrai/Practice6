from task2 import *

def convert(graph, from_rep, to_rep):
    res = []
    if from_rep == "Матрица смежности":
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 1:
                    res.append((i, j))

    elif from_rep == "Матрица инцидентности":
        for k in range(len(graph[0])):
            start = None
            end = None
            for i in range(len(graph)):
                if graph[i][k] == 1:
                    start = i

                if graph[i][k] == -1:
                    end = i
            res.append((start, end))

    elif from_rep == "Список смежности":
        for i in graph:
            for j in graph[i]:
                res.append((i, j))

    elif from_rep == "Список дуг":
        res = graph.copy()

    if to_rep == "Матрица смежности":
        return matrix_smezh(n, edges)

    elif to_rep == "Матрица инцидентности":
        return matrix_incin(n, edges)

    elif to_rep == "Список смежности":
        return list_smezh(n, edges)

    elif to_rep == "Список дуг":
        return list_edges(edges)

print("Из матрицы смежности в список смежности:")
print(convert(r1, "Матрица смежности", "Список смежности"))

print("\nИз списка смежности в матрицу смежности:")
print(convert(r3, "Список смежности", "Матрица смежности"))

print("\nИз матрицы инцидентности в список дуг:")
print(convert(r2, "Матрица инцидентности", "Список дуг"))

print("\nИз списка дуг в матрицу инцидентности:")
print(convert(r4, "Список дуг", "Матрица инцидентности"))