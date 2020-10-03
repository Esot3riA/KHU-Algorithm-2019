import math


class Heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        # heap size를 하나 줄여야 한다. 인덱스는 1부터. 인덱스의 2* 연산 가능하도록.
        self.n = len(self.data) - 1

    def addElt(self, elt):
        self.data.append(elt)
        self.n = len(self.data) - 1
        self.siftUp(self.n)

    def siftUp(self, i):
        while (i >= 2):
            # i번 노드 위의 부모 노드와 비교해서 값이 큰지 점검
            if self.data[i] > self.data[math.floor(i/2)]:
                temp = self.data[math.floor(i/2)]
                self.data[math.floor(i/2)] = self.data[i]
                self.data[i] = temp
            i = math.floor(i/2)

    def siftDown(self, i):
        siftkey = self.data[i]
        parent = i
        spotfound = False
        while 2*parent <= self.n and spotfound is False:
            print(parent)
            if 2*parent <= self.n and self.data[2*parent] < self.data[2*parent+1]:
                largerchild = 2 * parent + 1
            else:
                largerchild = 2 * parent
            if siftkey < self.data[largerchild]:
                self.data[parent] = self.data[largerchild]
                parent = largerchild
            else:
                spotfound = True
        self.data[parent] = siftkey

    def makeHeap(self):
        leaf = math.floor(len(self.data)/2)
        for i in range(math.floor(leaf), 0, -1):
            self.siftDown(i)

    # 힙의 루트를 가져온 후, siftdown 해서 maxheap으로 다시 만듦.
    def root(self):
        keyout = self.data[1]
        self.data[1] = self.data[self.n]
        del self.data[self.n]
        self.n = self.n - 1
        if self.n > 0:
            self.siftDown(1)
        return keyout

    def removeKeys(self):
        s = []
        for i in range(self.n+1, 0, -1):
            a = self.root()
            s.append(a)
        return s


def heapSort(a):
    a = Heap(a)
    a.makeHeap()
    s = a.removeKeys()
    return s


# 인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가
a = [0, 11, 14, 2, 7, 6, 3, 9]
b = Heap(a)
b.makeHeap()
print(b.data)
b.addElt(50)
print(b.data)
s = heapSort(a)
print(s)
