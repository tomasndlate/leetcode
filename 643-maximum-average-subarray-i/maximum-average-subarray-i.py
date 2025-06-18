class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0.0

        windowSum = sum(nums[:k])
        windowMax = windowSum
        left = 0

        for right in range(k, len(nums)):
            windowSum = windowSum - nums[left] + nums[right]
            left += 1

            windowMax = max(windowMax, windowSum)
        
        return windowMax / k
