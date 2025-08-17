class Solution:
    def canJump(self, nums: List[int]) -> bool:
        longest = 0

        for i, jump in enumerate(nums):
            if longest < i:
                return False
            longest = max(longest, i + jump)
        
        return True