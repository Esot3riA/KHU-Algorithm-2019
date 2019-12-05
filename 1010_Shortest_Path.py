from numpy import *
import numpy as np


def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0, m):
        for j in range(0, n):
            print("%4d" % d[i][j], end=" ")
        print()


# print float matrix
def printMatrixF(d):
    n = len(d[0])
    for i in range(0, n):
        for j in range(0, n):
            print("%5.2f" % d[i][j], end=" ")
        print()


def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)


def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)


def print_postOrder(root):
    if not root:
        return

    print_postOrder(root.l_child)
    print_postOrder(root.r_child)
    print(root.data)


def allShortestPath(g, n):
    p = [[0] * n for i in range(n)]
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if g[i][k] + g[k][j] < g[i][j]:
                    p[i][j] = k + 1
                    g[i][j] = g[i][k] + g[k][j]
    return g, p


def _path(p, q, r):
    if p[q][r] != 0:
        _path(p, q, p[q][r]-1)
        print("v%d" % p[q][r], end=" ")
        _path(p, p[q][r]-1, r)


def path(p, q, r):
    print("v%d" % q, end=" ")
    _path(p, q - 1, r - 1)
    print("v%d" % r, end=" ")



inf = 1000
g = [[0, 1, inf, 1, 5],
     [9, 0, 3, 2, inf],
     [inf, inf, 0, 4, inf],
     [inf, inf, 2, 0, 3],
     [3, inf, inf, inf, 0]]
d, p = allShortestPath(g, 5)
print()
printMatrix(d)
print()
printMatrix(p)

path(p, 5, 3)
