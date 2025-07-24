import heapq
class MedianFinder:

    def __init__(self):
        self.leftHeap = []   # maxHeap
        self.rightHeap = []  # minHeap

    def addNum(self, num: int) -> None:
        # 3 in ( [1] [2] ) go right
        # ( [1] [2,3] ) -> ( [1,2] [3] )
        if not self.rightHeap or num < self.rightHeap[0]:
            heapq.heappush(self.leftHeap, -num)
        else:
            heapq.heappush(self.rightHeap, num)

        # want always left to be equals or higher length
        if len(self.leftHeap) > len(self.rightHeap) + 1: # swap to right
            element = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, element)

        if len(self.rightHeap) > len(self.leftHeap): # swap to left
            element = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -element)

        

    def findMedian(self) -> float:
        length = len(self.leftHeap) + len(self.rightHeap)
        # odd
        if length % 2:
            return float(-self.leftHeap[0])
        # even
        else:
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()