class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # TOP-DOWN: RECURSION + MEMOIZATION
        cache = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return cache[i]
        
        return min(dfs(0), dfs(1))

        # BOTTOM-UP: TABULATION
            
        