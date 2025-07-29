class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0

        while r < len(nums) - 1: # didn't reach final
            jumps += 1
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
        
        return jumps