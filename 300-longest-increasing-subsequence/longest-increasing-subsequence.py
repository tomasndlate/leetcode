class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP
        # TOP-DOWN: RECURSION + MEMOIZATION
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            max_depth = 1
            for next_i in range(i + 1, len(nums)):
                if nums[next_i] > nums[i]: # valid
                    max_depth = max(max_depth, 1 + dfs(next_i))
            
            cache[i] = max_depth
            return cache[i]
        
        return max( dfs(i) for i in range(len(nums)) )


        # BOTTOM-UP: TABULATION