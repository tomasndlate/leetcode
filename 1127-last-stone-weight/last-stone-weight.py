import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, - stone)

        while len(heap) > 1:
            y = - heapq.heappop(heap)
            x = - heapq.heappop(heap)

            if y - x > 0:
                heapq.heappush(heap, - (y - x))
    
        return - heapq.heappop(heap) if heap else 0
            