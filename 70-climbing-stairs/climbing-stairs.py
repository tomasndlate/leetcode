class Solution:
    def climbStairs(self, n: int) -> int:
        #  0,    1,    2,    3,    4,    5
        # [                      one=1 two=1]
        # DP BOTTOM-UP
        one, two = 1, 1
        for num in range(1, n):
            one, two = one + two, one
        return one
        ## MEMOIZATION SOLUTION
        #cache = {1: 1, 2: 2}
        #def dfs(num):
            #if num in cache: return cache[num]
            ## position after -> 1 step + 2 steps
            #cache[num] = dfs(num-1) + dfs(num-2) 
            #return cache[num]
        #return dfs(n)