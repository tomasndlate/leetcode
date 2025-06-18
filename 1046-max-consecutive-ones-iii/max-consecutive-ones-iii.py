class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        windowMax = 0
        flip = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                flip += 1
            
            while flip > k: # while invalid
                if nums[left] == 0:
                    flip -= 1
                left += 1
        
            # valid now
            windowMax = max(windowMax, right - left + 1)

        return windowMax