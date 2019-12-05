import utility


def minmult(n, d, m, p):
    for i in range(0, n):
        m[i][i] = 0
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            final_result = 9999
            for k in range(i, j):
                print(i, j, k)
                local_result = m[i][k] + m[k+1][j] + (d[i-1] * d[k] * d[j])
                if final_result > local_result:
                    final_result = local_result
                    p[i][j] = k
            m[i][j] = final_result


def order(n, i, j):
    if i == j:
        print("A" + str(i), end='')
    else:
        k = n[i][j]
        print("(", end='')
        order(n, i, k)
        order(n, k+1, j)
        print(")", end='')


d = [5, 2, 3, 4, 6, 7, 8]
n = len(d) - 1
m = [[0 for j in range(0, n+1)] for i in range(0, n+1)]
p = [[0 for j in range(0, n+1)] for i in range(0, n+1)]

minmult(n, d, m, p)
utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p, 1, 6)
