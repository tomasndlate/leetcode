class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(start, end):
            prev1 = prev2 = 0
            for i in range(start, end):
                prev1, prev2 = prev2, max(nums[i] + prev1, prev2)
            return prev2
        
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))