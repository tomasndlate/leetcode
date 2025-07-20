class Solution:
    def climbStairs(self, n: int) -> int:
        step1 = 0
        step2 = 1 # one possibility?
        for _ in range(n):
            step1, step2 = step2, step1 + step2
        return step2