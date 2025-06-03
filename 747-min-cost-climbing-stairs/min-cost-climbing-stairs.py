class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP BOTTOM-UP
        one, two = cost[-1], 0
        for i in range(len(cost) - 2, -1, -1):
            one, two = cost[i] + min(one, two), one
        return min(one, two)

        ## MEMOIZATION
        #cache = {}
        #def dfs(i):
            #if i >= len(cost): return 0
            #if i in cache: return cache[i]

            #cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            #return cache[i]

        #return min(dfs(0), dfs(1))