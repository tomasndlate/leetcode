class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        cache = {}
        def dfs(i, bound):
            key = (i, bound)
            if key in cache:
                return cache[key]
            if i >= bound:
                return 0

            robRes = nums[i] + dfs(i+2, bound)
            skipRes = dfs(i+1, bound)

            cache[key] = max(robRes, skipRes)
            return cache[key]

        
        return max(dfs(0, n-1), dfs(1, n))