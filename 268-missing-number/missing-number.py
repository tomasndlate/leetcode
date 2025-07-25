class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        for i, num in enumerate(nums):
            res ^= num
            res ^= i + 1
        
        return res