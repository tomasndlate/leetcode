class Solution:
    def rob(self, nums: List[int]) -> int:
        # TOP-DOWN
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0 # total stole
            
            rob = nums[i] + dfs(i+2) # rob and skip 1
            skip = dfs(i+1) # go to next

            cache[i] = max(rob, skip)
            return cache[i]
        
        return dfs(0)
        # BOTTOM-UP