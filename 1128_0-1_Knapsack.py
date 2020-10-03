n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
maxp = 0
include = [0] * len(p)
bestset = [0] * len(p)

# 맨 처음 정렬하는 부분이 빠져 있음
def promising(i, weight, profit):
    global maxp
    if weight >= W:
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while j <= n-1 and totweight + w[j] <= W:
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if k <= n-1:
            bound += (W - totweight) * p[k]/w[k]
        return bound > maxp


def knapsack(i, profit, weight):
    global maxp
    global bestset
    if weight <= W and profit > maxp:
        maxp = profit
        bestset = include[:]
    if promising(i, weight, profit):
        include[i+1] = 1
        knapsack(i+1, profit+p[i+1], weight+w[i+1])
        include[i+1] = 0
        knapsack(i+1, profit, weight)


knapsack(-1, 0, 0)
print(maxp)
print(bestset)
