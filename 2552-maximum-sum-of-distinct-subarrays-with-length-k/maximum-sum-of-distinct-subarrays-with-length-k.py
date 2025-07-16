from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxWindowSum = 0
        windowSum = 0
        window = defaultdict(int)

        # initialise window
        for i in range(k):
            windowSum += nums[i]
            window[nums[i]] += 1

        # first window edge case
        if len(window) == k:
            maxWindowSum = windowSum

        for i in range(k, len(nums)):
            first = nums[i] 
            last = nums[i - k]

            # remove last
            windowSum -= last
            window[last] -= 1
            if window[last] == 0:
                del window[last]

            # add first
            windowSum += first
            window[first] += 1
            if len(window) == k:
                maxWindowSum = max(maxWindowSum, windowSum)
        
        return maxWindowSum
            
            