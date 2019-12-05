class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def bs(self, item, low, high):
        if low > high:
            return 0
        else:
            mid = int((low + high) / 2)
            if item == data[mid]:
                return mid
            elif item < data[mid]:
                return self.bs(item, low, mid - 1)
            else:
                return self.bs(item, mid + 1, high)


data = [1, 3, 5, 6, 7, 9, 10, 14, 17, 19, 21, 23, 28]
algorithm = BinarySearch(data)
location = algorithm.bs(19, 0, len(data))
print(location)
