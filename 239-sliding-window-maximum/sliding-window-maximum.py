from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        maxHeap = [] # (-num, index)

        res = []
        
        for i, num in enumerate(nums):
            window.append(num)
            heapq.heappush(maxHeap, (-num, i))

            if len(window) > k:
                window.popleft()

                while maxHeap[0][1] < (i - k) + 1:
                    heapq.heappop(maxHeap)
            
            if len(window) == k:
                maxValue = - maxHeap[0][0]
                res.append(maxValue)
        
        return res