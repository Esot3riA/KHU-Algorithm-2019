from numpy import *
import numpy as np
import time


class BinaryCoffee:
    def bin(self, n, k):
        if k == 0 or n == k:
            return 1
        else:
            return self.bin(n-1, k-1) + self.bin(n-1, k)

    def bin2(self, n, k):
        b = np.empty((n+1, n+1))
        for i in range(0, n+1):
            for j in range(min(i, k)+1):
                if j == 0 or j == i:
                    b[i][j] = 1
                else:
                    b[i][j] = b[i-1][j-1] + b[i-1][j]
        return b[n][k]


binaryCoffee = BinaryCoffee()
print(binaryCoffee.bin(10, 5), binaryCoffee.bin2(10, 5))

start = time.time()
result1 = binaryCoffee.bin(20, 10)
end = time.time()
print("bin1 exec time in N=30 : ", end - start, ", result : ", result1)

start = time.time()
result2 = binaryCoffee.bin2(1000, 500)
end = time.time()
print("bin2 exec time in N=1000 : ", end - start, ", result : ", result2)
