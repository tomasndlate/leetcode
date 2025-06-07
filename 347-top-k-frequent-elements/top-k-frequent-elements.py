from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        heap = []
        for n, freq in count.items():
            heapq.heappush(heap, (-freq, n))
        
        return [ heapq.heappop(heap)[1] for _ in range(k) ]