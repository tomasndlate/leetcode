from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        left, right = 0, 0

        while left <= right:
            if right >= len(nums) - 1:
                return jumps

            farthest = left
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left, right = right + 1, farthest
            jumps += 1
        
        return 0