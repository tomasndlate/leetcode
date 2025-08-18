class Solution:
    def canJump(self, nums: List[int]) -> bool:
        longest = 0
        for i, num in enumerate(nums):
            if longest < i:
                return False
            longest = max(longest, i + num)
        return True