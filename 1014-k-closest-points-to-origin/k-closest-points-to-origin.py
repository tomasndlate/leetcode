import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        getDist = lambda x, y: x**2 + y**2

        for x, y in points:
            heapq.heappush(minHeap, (-getDist(x,y), [x, y]))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [ point for dist, point in minHeap ]