class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dp(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]
            
            # Possible Ways
            negative = dp(i + 1, total - nums[i])
            positive = dp(i + 1, total + nums[i])

            cache[(i, total)] = negative + positive
            return cache[(i, total)]
        
        return dp(0, 0)


            