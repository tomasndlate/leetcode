import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        # new num left part
        if not self.left or -self.left[0] >= num: 
            heapq.heappush(self.left, -num)
        # new num right part
        else: 
            heapq.heappush(self.right, num)

        if len(self.left) - len(self.right) > 1: # left is overload
            move = heapq.heappop(self.left)
            heapq.heappush(self.right, -move)
        elif len(self.right) - len(self.left) > 0: # right is overload
            move = heapq.heappop(self.right)
            heapq.heappush(self.left, -move)

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        # odd
        if total % 2:
            return float(-self.left[0])
        # even
        else:
            return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()