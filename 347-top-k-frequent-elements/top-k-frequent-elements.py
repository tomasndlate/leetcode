import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # HEAP
        #minHeap = []
        #for n, freq in count.items():
        #    heapq.heappush(minHeap, (freq, n))
        #    if len(minHeap) > k:
        #        heapq.heappop(minHeap)
        #return [n for freq, n in minHeap]

        # BUCKET SORT
        buckets = [ [] for i in range(len(nums)+1) ]
        for n, freq in count.items():
            buckets[freq].append(n)
        
        res = []
        for numbers in reversed(buckets):
            for n in numbers:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []