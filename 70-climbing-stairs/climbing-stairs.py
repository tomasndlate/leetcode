class Solution:
    def climbStairs(self, n: int) -> int:
        stair1 = 0
        stair2 = 1
        for _ in range(n):
            stair1, stair2 = stair2, stair1 + stair2
        
        return stair2
