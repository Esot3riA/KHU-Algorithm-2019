import utility
import queue

e = {0: [1, 2, 3], 1: [2, 5], 2: [3, 4, 5, 6], 3: [4, 6], 4: [6, 7]}
n = 8
a = [[0 for j in range(0, n)] for i in range(0, n)]
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if i in e:
            if j in e[i]:
                a[i][j] = 1
                a[j][i] = 1
utility.printMatrix(a)
visited_dfs = n * [0]
visited_bfs = n * [0]


def DFS(a, v):
    print(v)
    visited_dfs[v] = 1

    nodes = a[v]
    for i in range(0, n):
        if nodes[i] == 1 and visited_dfs[i] == 0:
            DFS(a, i)


def BFS(a, v):
    q = queue.Queue()
    q.put(v)
    while q.empty() is False:
        i = q.get()
        print(i)
        visited_bfs[i] = 1
        for j in range(0, n):
            if a[i][j] == 1 and visited_bfs[j] == 0:
                q.put(j)
                visited_bfs[j] = 1


DFS(a, 0)
print()
BFS(a, 0)
