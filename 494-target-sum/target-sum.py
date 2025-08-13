class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def dp(i, curSum):
            if (i, curSum) in cache:
                return cache[((i, curSum))]

            if i == len(nums):
                return 1 if curSum == target else 0
            
            negative = dp(i + 1, curSum - nums[i])
            positive = dp(i + 1, curSum + nums[i])

            cache[((i, curSum))] = negative + positive
            return cache[((i, curSum))]

        
        return dp(0, 0)
