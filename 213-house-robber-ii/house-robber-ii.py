class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(houses):
            prev1 = 0
            prev2 = 0

            for house in houses:
                prev1, prev2 = prev2, max(prev1 + house, prev2)
            
            return prev2
        
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[1:]), helper(nums[:-1]))