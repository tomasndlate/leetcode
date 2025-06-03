class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP BOTTOM-UP
        #costTwo = cost[-1]
        #costOne = cost[-2]
        #for i in range(len(cost) - 3, -1, -1):
            #costOne, costTwo = cost[i] + costTwo, costOne
        #return min(costOne, costTwo)
        # MEMOIZATION
        cache = {}
        def dfs(i):
            if i >= len(cost): return 0
            if i in cache: return cache[i]

            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]

        return min(dfs(0), dfs(1))