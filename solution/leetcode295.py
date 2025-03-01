import heapq
from multiprocessing import heap


class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        heapq.heapify(self.left)
        heapq.heapify(self.right) 

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 and len(self.right) == 0:
            heapq.heappush(self.right, num)
            return
        
        if len(self.left) + len(self.right) == 1:
            if num <= heapq.nsmallest(1, self.right)[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.left, -heapq.heappop(self.right))
                heapq.heappush(self.right, num)
            return
        
        left_largest = -heapq.nsmallest(1, self.left)[0]
        right_smallest = heapq.nsmallest(1, self.right)[0]
        
        if num < left_largest:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if abs(len(self.left) - len(self.right)) > 1:
            m = (len(self.left) + len(self.right)) // 2
            if len(self.left) - len(self.right) > 0:
                temp = []
                for _ in range(len(self.left) - m):
                    temp.append(-heapq.heappop(self.left))
                heapq.heappush(self.right, *temp)
            else:
                temp = []
                for _ in range(len(self.right) - m):
                    temp.append(-heapq.heappop(self.right))
                heapq.heappush(self.left, *temp)

    def findMedian(self) -> float:
        if abs(len(self.left) - len(self.right)) == 0:
            return (-heapq.nsmallest(1, self.left)[0] + heapq.nsmallest(1, self.right)[0]) / 2
        
        if len(self.left) > len(self.right):
            return -heapq.nsmallest(1, self.left)[0]
        else:
            return heapq.nsmallest(1, self.right)[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

[[],[1],[2],[],[3],[]]
obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())