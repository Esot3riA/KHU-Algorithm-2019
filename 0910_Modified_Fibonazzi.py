import time


class Algorithm:
    def __init__(self):
        self.length = input("Input length : ")
        self.arr = list(map(int, input("Input array on one line(ex: 1 2 3 4 5) : ").split()))
        # Arbitrary array: only for testing
        # self.arr = range(1, 40002)

    def sum1(self, n):
        if n is 0:
            return 1
        else:
            result = 0
            for i in range(n):
                result += self.sum1(i)
            result += self.arr[n]
            return result

    def sum2(self, n):
        memoized_array = [1, 1 + self.arr[1]]
        for i in range(2, n + 1):
            next_element = (2 * memoized_array[i-1]) - self.arr[i-1] + self.arr[i]
            memoized_array.append(next_element)
        return memoized_array[n]

algorithm = Algorithm()
algorithm_num = input("Select algorithm 1 or 2 (Recursion or Memoization) : ")
sumNum = input("Input N : ")

start = time.time()
if algorithm_num is "1":
    print("Answer : ", algorithm.sum1(int(sumNum)))
elif algorithm_num is "2":
    print("Answer : ", algorithm.sum2(int(sumNum)))
end = time.time()
print("Execution time : ", end - start)
