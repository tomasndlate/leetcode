from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxWindowSum = 0
        windowSum = 0
        window = defaultdict(int)

        for i, first in enumerate(nums):
            
            windowSum += first
            window[first] += 1

            if i >= k: # shrink last element (constant size)
                last = nums[i - k]
                windowSum -= last
                window[last] -= 1
                if window[last] == 0:
                    del window[last]

            if len(window) == k: # distinct elements subarray
                maxWindowSum = max(maxWindowSum, windowSum)
        
        return maxWindowSum
            
            