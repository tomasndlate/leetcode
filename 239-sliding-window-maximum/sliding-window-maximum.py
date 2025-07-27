from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # index
        res = []
        
        left = 0
        for right in range(len(nums)):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            # remove out of bounds indexes
            while queue and queue[0] < left:
                queue.popleft()

            if (right - left + 1) == k:
                res.append(nums[queue[0]])
                left += 1
        
        return res