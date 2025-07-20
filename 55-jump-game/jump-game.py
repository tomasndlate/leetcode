class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        buffer = 1
        for num in nums[:n-1]:
            buffer -= 1
            buffer = max(buffer, num)
            if buffer == 0:
                return False
        return True