class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Visual Example:
        # 1 1 1 1
        # 1 2 3 4
        # 1 3 6 10

        dp = [ [1] * n for _ in range(m) ] # possible ways until each cell

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]