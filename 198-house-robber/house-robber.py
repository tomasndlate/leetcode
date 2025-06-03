class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP BOTTOM-UP - Tabulation
        n = len(nums)
        if n == 1: return nums[0]

        for i in range(n-2, -1, -1):
            first =  nums[i+2] if i+2 < n else 0
            second = nums[i+3] if i+3 < n else 0

            nums[i] += max(first, second)

        return max(nums[0], nums[1])

        # MEMOIZATION - Recursion + Cache        
        #cache = {}

        #def dfs(i):
            #if i >= len(nums): return 0
            #if i in cache: return cache[i]
            
            #cache[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            #return cache[i]

        #return max(dfs(0), dfs(1))
        