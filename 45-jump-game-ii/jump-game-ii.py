class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left = right = 0
        jumps = 0

        while right < len(nums) - 1:
            longest = 0
            for i in range(left, right + 1):
                longest = max(longest, i + nums[i])
            left = right + 1
            right = longest
            jumps += 1
        
        return jumps