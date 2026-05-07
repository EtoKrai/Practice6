import numpy as np

edges=[(0, 1), (0, 2), (2, 3)]
n=4

def matrix_smezh(n, edges):
    m=np.zeros((n, n))
    for x,y in edges:
        m[x][y]=1
    return m

def matrix_incin(n, edges):
    m=np.zeros((n, len(edges)))
    for i, (x,y) in enumerate(edges):
        m[x][i]= -1
        m[y][i]= 1
    return m

def list_smezh(n, edges):
    s= {i: [] for i in range(n)}
    for x,y in edges:
        s[x].append(y)
    return s

def list_edges(edges):
    s=edges.copy()
    return s

r1=matrix_smezh(n, edges)
r2=matrix_incin(n, edges)
r3=list_smezh(n, edges)
r4=list_edges(edges)

if __name__=="__main__":
    print("Матрица смежности:\n", r1)
    print("Матрица инцидентности:\n", r2)
    print("Список смежности:", r3)
    print("Список дуг:", r4)