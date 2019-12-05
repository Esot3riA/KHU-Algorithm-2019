class MergeSortAlgorithm:
    def mergeSort(self, n, S):
        h = int(n / 2)
        m = n - h
        if n > 1:
            U = S[:h]
            V = S[h:]
            self.mergeSort(h, U)
            self.mergeSort(m, V)
            self.merge(h, m, U, V, S)

    def merge(self, h, m, U, V, S):
        i, j, k = 0, 0, 0
        while i <= h - 1 and j <= m - 1:
            if U[i] < V[j]:
                S[k] = U[i]
                i += 1
            else:
                S[k] = V[j]
                j += 1
            k += 1
        if i > h - 1:
            for iterator in range(j, m):
                S[k - j + iterator] = V[iterator]
        else:
            for iterator in range(i, h):
                S[k - i + iterator] = U[iterator]

    globalS = []

    def setGlobalS(self, S):
        self.globalS = S

    def mergeSort2(self, low, high):
        if low < high:
            mid = int((low + high) / 2)
            self.mergeSort2(low, mid)
            self.mergeSort2(mid+1, high)
            self.merge2(low, mid, high)

    def merge2(self, low, mid, high):
        print(low, mid, high)
        i = low
        j = mid + 1
        k = 0
        U = [0] * (high - low + 1)
        while i <= mid and j <= high:
            if self.globalS[i] < self.globalS[j]:
                U[k] = self.globalS[i]
                i += 1
            else:
                U[k] = self.globalS[j]
                j += 1
            k += 1
        if i > mid:
            for iterator in range(j, high + 1):
                U[k - j + iterator] = self.globalS[iterator]
        else:
            for iterator in range(i, mid + 1):
                U[k - i + iterator] = self.globalS[iterator]
        for iterator in range(low, high + 1):
            self.globalS[iterator] = U[iterator - low]


s = [3, 5, 2, 9, 10, 14, 4, 8]
mergeSortAlgorithm = MergeSortAlgorithm()
mergeSortAlgorithm.mergeSort(8, s)
print(s)

s3 = [3, 5, 2, 9, 10, 14, 4, 8]
mergeSortAlgorithm.setGlobalS(s3)
mergeSortAlgorithm.mergeSort2(0, 7)
print(mergeSortAlgorithm.globalS)
