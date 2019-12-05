import time


def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n-1]


for i in range(2, 200):
    start = time.time()
    print(fib1(i))
    endtime = time.time() - start
    print(i, "\t", endtime)
