class Solution:
    def rob(self, nums: List[int]) -> int:
        # TOP-DOWN
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0 # total stole
            
            res1 = dfs(i+2) # 1 of interval
            res2 = dfs(i+3) # 2 of interval

            cache[i] = nums[i] + max(res1, res2)
            return cache[i]
        
        return max(dfs(0), dfs(1))
        # BOTTOM-UP