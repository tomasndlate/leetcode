class Solution:
    def climbStairs(self, n: int) -> int:
        # MEMOIZATION SOLUTION
        cache = {1: 1, 2: 2}
        def dfs(num):
            if num in cache: return cache[num]
            # position after -> 1 step + 2 steps
            cache[num] = dfs(num-1) + dfs(num-2) 
            return cache[num]
        return dfs(n)