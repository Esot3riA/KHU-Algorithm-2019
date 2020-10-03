import utility

inf = 1000
w = [[0, 7, 4, 6, 1],
     [inf, 0, inf, inf, inf],
     [inf, 2, 0, 5, inf],
     [inf, 3, inf, 0, inf],
     [inf, inf, inf, 1, 0]]
w_copy = [[0, 7, 4, 6, 1],
          [inf, 0, inf, inf, inf],
          [inf, 2, 0, 5, inf],
          [inf, 3, inf, 0, inf],
          [inf, inf, inf, 1, 0]]
n = 5
f = set()
touch = n * [0]
length = n * [0]
NoC = 0  # vnear에서 length update 체크 횟수


def _path(end):
    if touch[end] != 0:
        _path(touch[end])
        print("v%d" % (int(touch[end]) + 1), end=" ")


def path(end):
    print("v1", end=" ")
    _path(end - 1)
    print("v%d" % end, end=" ")


for i in range(1, n):
    touch[i] = 0
    length[i] = w[0][i]

for iterator in range(1, n):
    min = inf
    vnear = 0
    for i in range(1, n):
        if 0 <= length[i] < min:
            min = length[i]
            vnear = i
    e = (touch[vnear], vnear)
    f.add(e)

    for i in range(1, n):
        if 0 < w[vnear][i] < inf:
            NoC += 1
            # 여기 중요
            if length[vnear] + w[vnear][i] < length[i]:
                length[i] = length[vnear] + w[vnear][i]
                touch[i] = vnear
    length[vnear] = -1

print(f)
print("Update count : ", NoC)
print()
print("Shortest route of 1 to 2 : ", end="")
path(2)
print()