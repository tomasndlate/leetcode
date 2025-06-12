import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            dist = math.sqrt( x**2 + y**2 )
            heapq.heappush(minHeap, (dist, [x, y]))
        
        return [ heapq.heappop(minHeap)[1] for _ in range(k) ]
    