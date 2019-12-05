# Prim과 다익스트라 알고리즘은 형태가 매우 유사함.

import utility

inf = 1000
w = [[0, 1, 3, inf, inf],
     [1, 0, 3, 6, inf],
     [3,  3, 0, 4,  2],
     [inf, 6, 4, 0, 5],
     [inf, inf, 2, 5, 0]]

F = set()
utility.printMatrix(w)
n = len(w)
nearest = n * [0]
distance = n * [0]
for i in range(1, n):
    nearest[i] = 0
    distance[i] = w[0][i]

for iterator in range(1, n):
    min = inf
    vnear = 0   # 새로 추가될 노드
    for i in range(1, n):
        if 0 <= distance[i] < min:
            min = distance[i]
            vnear = i
    F.add((vnear, nearest[vnear]))
    distance[vnear] = -1    # 방금 추가한 vnear 노드 배제
    for i in range(1, n):
        if w[i][vnear] < distance[i]:   # 방금 추가한 vnear와 가까운 노드가 있는지 검증
            distance[i] = w[i][vnear]
            nearest[i] = vnear
print()
print(F)
