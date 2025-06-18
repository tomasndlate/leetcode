class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        windowMax = 0
        deleted = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                deleted += 1
            
            while deleted > 1:
                if nums[left] == 0:
                    deleted -= 1
                left += 1
            
            # valid now
            windowMax = max(windowMax, right - left)
        
        return windowMax